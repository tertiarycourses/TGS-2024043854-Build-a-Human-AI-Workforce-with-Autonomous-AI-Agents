#!/usr/bin/env python3
"""Reviewed classroom tool: calculate synthetic workbook metrics, build editable artifacts.
The agent must inspect, adapt, render and verify outputs; this is a starting point.
"""
import argparse,json,math,csv,hashlib
from pathlib import Path
from collections import defaultdict,Counter
from openpyxl import load_workbook,Workbook
from openpyxl.styles import Font,PatternFill

def analyse(src,out):
 wb=load_workbook(src,data_only=True); sheets={}
 required={'Reviews':['review_id','outlet','rating'],'Sales':['week_start','outlet','revenue_sgd','cups_sold'],'Metrics':['post_id','reach','likes','comments','shares']}
 rejected=[]
 for name,cols in required.items():
  if name not in wb.sheetnames:raise ValueError('Missing sheet: '+name)
  rows=list(wb[name].values);head=list(rows[0])
  if any(c not in head for c in cols):raise ValueError(f'{name}: required columns {cols}, found {head}')
  sheets[name]=[dict(zip(head,r)) for r in rows[1:] if any(v is not None for v in r)]
 totals=defaultdict(lambda:{'revenue_sgd':0.0,'cups_sold':0,'cold_brew_cups':0,'app_preorders':0})
 seen=set()
 for idx,r in enumerate(sheets['Sales'],2):
  key=(r['week_start'],r['outlet'])
  try:
   if key in seen:raise ValueError('duplicate week/outlet')
   if not r['outlet']:raise ValueError('missing outlet')
   vals={k:float(r[k]) for k in totals['__schema__']}
   if any(not math.isfinite(v) or v<0 for v in vals.values()):raise ValueError('invalid numeric value')
   seen.add(key)
   for k,v in vals.items():totals[r['outlet']][k]+=v
  except (ValueError,TypeError,KeyError) as e:rejected.append({'sheet':'Sales','row':idx,'reason':str(e)})
 totals.pop('__schema__',None)
 ratings=Counter();review_ids=set()
 for idx,r in enumerate(sheets['Reviews'],2):
  try:
   n=int(r['rating'])
   if n not in range(1,6) or r['review_id'] in review_ids:raise ValueError('invalid rating or duplicate ID')
   review_ids.add(r['review_id']);ratings[n]+=1
  except (ValueError,TypeError) as e:rejected.append({'sheet':'Reviews','row':idx,'reason':str(e)})
 metrics=[];ids=set()
 for idx,r in enumerate(sheets['Metrics'],2):
  try:
   if r['post_id'] in ids:raise ValueError('duplicate post_id')
   reach=float(r['reach']);eng=sum(float(r[k]) for k in ['likes','comments','shares'])
   if not math.isfinite(reach) or reach<0 or not math.isfinite(eng) or eng<0:raise ValueError('invalid reach/engagement')
   ids.add(r['post_id']);metrics.append({'post_id':r['post_id'],'reach':reach,'engagements':eng,'engagement_rate':eng/reach if reach else None})
  except (ValueError,TypeError) as e:rejected.append({'sheet':'Metrics','row':idx,'reason':str(e)})
 result={'source':str(src),'sha256':hashlib.sha256(Path(src).read_bytes()).hexdigest(),'synthetic':True,
  'row_counts':{k:len(v) for k,v in sheets.items()},'outlets':[dict(outlet=k,**v) for k,v in sorted(totals.items())],
  'revenue_total_sgd':round(sum(v['revenue_sgd'] for v in totals.values()),2),'ratings':dict(sorted(ratings.items())),
  'mean_rating':sum(k*v for k,v in ratings.items())/sum(ratings.values()) if ratings else None,'post_metrics':metrics,'rejected_rows':rejected,
  'formulas':{'revenue':'SUM of supplied revenue_sgd, not inferred from units','engagement_rate':'(likes+comments+shares)/reach; zero reach -> null'}}
 (out/'analysis.json').write_text(json.dumps(result,indent=2))
 book=Workbook();ws=book.active;ws.title='Outlet Summary';cols=['outlet','revenue_sgd','cups_sold','cold_brew_cups','app_preorders'];ws.append(cols)
 for r in result['outlets']:ws.append([r[c] for c in cols])
 ws.append(['TOTAL',f'=SUM(B2:B{ws.max_row})',f'=SUM(C2:C{ws.max_row})',f'=SUM(D2:D{ws.max_row})',f'=SUM(E2:E{ws.max_row})'])
 for cell in ws[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='5B3A29')
 for col in 'ABCDE':ws.column_dimensions[col].width=23
 w=book.create_sheet('Post Metrics');w.append(['post_id','reach','engagements','engagement_rate'])
 for r in metrics:w.append([r[k] for k in ['post_id','reach','engagements','engagement_rate']])
 for cell in w['D'][1:]:cell.number_format='0.00%'
 w=book.create_sheet('Provenance');w.append(['source',str(src)]);w.append(['sha256',result['sha256']]);w.append(['Revenue method',result['formulas']['revenue']]);w.append(['Expected numeric total',result['revenue_total_sgd']]);w.append(['Synthetic training data',True])
 w=book.create_sheet('Rejected Rows');w.append(['sheet','row','reason'])
 for r in rejected:w.append([r['sheet'],r['row'],r['reason']])
 book.save(out/'analysis.xlsx');print('Analysed',result['row_counts'],'revenue',result['revenue_total_sgd'],'rejected',len(rejected))

def dashboard(out):
 data=json.loads((out/'analysis.json').read_text());encoded=json.dumps(data).replace('<','\\u003c')
 html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kopi Kaki Launch Office</title><style>
:root{font-family:system-ui;color:#34251d;background:#f8f3e9}body{overflow-wrap:anywhere;max-width:1100px;margin:40px auto;padding:0 22px}h1{font-size:38px}button,select{font:inherit;padding:10px;border-radius:8px;border:1px solid #7c6a59;background:white;min-height:44px}label{display:block;margin-bottom:6px}.controls{display:flex;gap:12px;align-items:end;flex-wrap:wrap}.kpi{background:#5b3a29;color:white;padding:25px;border-radius:14px;margin:25px 0}.kpi strong{font-size:38px;display:block}.bar{display:grid;grid-template-columns:170px 1fr 110px;gap:12px;align-items:center;margin:12px 0}.track{background:#e3ddcf;border-radius:5px}.fill{background:#4e8a3e;height:24px;border-radius:5px}table{width:100%;border-collapse:collapse;background:white;margin:30px 0}td,th{text-align:left;padding:12px;border-bottom:1px solid #ddd}th button{border:0;font-weight:bold;background:transparent}.note{color:#5a5147}a{color:#5b3a29}@media(max-width:600px){.bar{grid-template-columns:110px 1fr 80px}h1{font-size:30px}table{font-size:13px}td,th{padding:7px}}
</style><body><p>LAUNCH OFFICE · FICTIONAL TRAINING DATA</p><h1>Kopi Kaki: Decide with Evidence</h1><p>Filter the outlet view, compare revenue and inspect the same rows in the workbook.</p><div class="controls"><div><label for="outlet">Outlet</label><select id="outlet"><option value="">All outlets</option></select></div><button id="reset">Reset view</button><button id="export">Export visible CSV</button></div><section class="kpi" aria-live="polite"><span>Revenue (SGD)</span><strong id="total"></strong><span id="count"></span></section><h2>Outlet revenue</h2><div id="chart" role="img" aria-label="Outlet revenue bar chart"></div><table><thead><tr><th>Outlet</th><th><button id="sort">Revenue ↕</button></th><th>Cups sold</th><th>Cold brew cups</th></tr></thead><tbody id="rows"></tbody></table><p class="note" id="provenance"></p><p>Revenue = sum of supplied revenue_sgd. Training figures do not establish campaign causality. All code and data are embedded; this page works offline.</p><footer>Powered by <a href="https://www.tertiaryinfotech.com/">Tertiary Infotech Academy Pte Ltd</a></footer><script>
const DATA=__DATA__;const picker=document.querySelector('#outlet');let ascending=false;
const money=n=>Number(n).toLocaleString('en-SG',{minimumFractionDigits:2,maximumFractionDigits:2});
DATA.outlets.forEach(r=>{let o=document.createElement('option');o.value=r.outlet;o.textContent=r.outlet;picker.appendChild(o)});
function visible(){return DATA.outlets.filter(r=>!picker.value||r.outlet===picker.value).slice().sort((a,b)=>ascending?a.revenue_sgd-b.revenue_sgd:b.revenue_sgd-a.revenue_sgd)}
function draw(){let rows=visible();document.querySelector('#total').textContent=money(rows.reduce((s,r)=>s+r.revenue_sgd,0));document.querySelector('#count').textContent=rows.length+' outlet(s)';let body=document.querySelector('#rows');body.replaceChildren();let chart=document.querySelector('#chart');chart.replaceChildren();let max=Math.max(...DATA.outlets.map(r=>r.revenue_sgd),1);rows.forEach(r=>{let tr=document.createElement('tr');[r.outlet,money(r.revenue_sgd),r.cups_sold,r.cold_brew_cups].forEach(v=>{let td=document.createElement('td');td.textContent=v;tr.appendChild(td)});body.appendChild(tr);let b=document.createElement('div');b.className='bar';let name=document.createElement('span');name.textContent=r.outlet;let track=document.createElement('div');track.className='track';let fill=document.createElement('div');fill.className='fill';fill.style.width=(100*r.revenue_sgd/max)+'%';track.appendChild(fill);let value=document.createElement('span');value.textContent=money(r.revenue_sgd);b.append(name,track,value);chart.appendChild(b)});}
picker.addEventListener('change',draw);document.querySelector('#reset').onclick=()=>{picker.value='';ascending=false;draw()};document.querySelector('#sort').onclick=()=>{ascending=!ascending;draw()};
document.querySelector('#export').onclick=()=>{let keys=['outlet','revenue_sgd','cups_sold','cold_brew_cups'];let q=v=>'"'+String(v).replaceAll('"','""')+'"';let csv=[keys.join(','),...visible().map(r=>keys.map(k=>q(r[k])).join(','))].join('\\r\\n');let url=URL.createObjectURL(new Blob([csv],{type:'text/csv'}));let a=document.createElement('a');a.href=url;a.download='kopi-visible-outlets.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)};
document.querySelector('#provenance').textContent='Source: '+DATA.source+' | SHA256 '+DATA.sha256;draw();</script></body></html>'''
 (out/'dashboard.html').write_text(html.replace('__DATA__',encoded));print('Wrote interactive dashboard')

def ppt(out):
 from pptx import Presentation
 from pptx.util import Inches,Pt
 from pptx.dml.color import RGBColor
 from pptx.enum.chart import XL_CHART_TYPE
 from pptx.chart.data import CategoryChartData
 from pptx.enum.shapes import MSO_SHAPE
 data=json.loads((out/'analysis.json').read_text());p=Presentation();p.slide_width=Inches(13.333);p.slide_height=Inches(7.5)
 def txt(s,x,y,w,h,t,size=22,color='34251D',bold=False):
  box=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=box.text_frame;tf.word_wrap=True
  for i,line in enumerate(t.split('\n')):
   q=tf.paragraphs[0] if i==0 else tf.add_paragraph();q.text=line;q.font.size=Pt(size);q.font.name='Aptos';q.font.bold=bold;q.font.color.rgb=RGBColor.from_string(color)
  return box
 def slide(title,sub):
  s=p.slides.add_slide(p.slide_layouts[6]);s.background.fill.solid();s.background.fill.fore_color.rgb=RGBColor.from_string('F8F3E9');txt(s,.65,.4,12,.3,'KOPI KAKI · MANAGEMENT DECISION PACK · SYNTHETIC DATA',11,'775B41',True);txt(s,.65,1,12,1,title,34,bold=True);txt(s,.65,2,12,.5,sub,17,'69594B');txt(s,.65,7,12,.2,'Training scenario · © Tertiary Infotech Academy Pte Ltd',10,'69594B');return s
 def panel(s,x,y,w,title,body):
  sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(2.8));sh.fill.solid();sh.fill.fore_color.rgb=RGBColor.from_string('FFFFFF');sh.line.fill.background();txt(s,x+.2,y+.2,w-.4,.6,title,22,bold=True);txt(s,x+.2,y+1,w-.4,1.65,body,19)
 s=slide('Which Launch Priority Should We Fund?','Human decision required: confirm the campaign angle and one operational priority.');panel(s,.65,3,5.8,'Decision context','Use verified outlet revenue and customer evidence to choose one next action.');panel(s,6.8,3,5.8,'Evidence rule','Every chart and recommendation must trace to the approved office pack.');
 s=slide('One Brief, One Shared Set of Facts','Revise with the agent after checking the source documents.');panel(s,.65,3,5.8,'Approved product facts','Gula Melaka Cold Brew\nSGD 6.80 · launch 1 Dec 2026');panel(s,6.8,3,5.8,'Source boundaries','Use campaign-brief.md and product-catalogue.csv. Do not infer campaign impact from one week of sales.');
 s=slide('Outlet Revenue: Compare the Same Period','Revenue is the supplied revenue_sgd, aggregated by outlet.');cd=CategoryChartData();cd.categories=[r['outlet'] for r in data['outlets']];cd.add_series('Revenue SGD',[r['revenue_sgd'] for r in data['outlets']]);chart=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,Inches(.8),Inches(2.7),Inches(11.8),Inches(3.9),cd).chart;chart.category_axis.tick_label_spacing=1;chart.category_axis.tick_labels.font.size=Pt(12);s.notes_slide.notes_text_frame.text='Source: campaign-data.xlsx Sales sheet; analysis.json; source SHA256 '+data['sha256'];
 s=slide('Customer Evidence Must Support the Angle','Mean rating and distributions describe the supplied reviews; themes still need review IDs.');panel(s,.65,3,5.8,'Verified review summary',f"{sum(data['ratings'].values())} reviews\nMean rating: {data['mean_rating']:.2f}/5");panel(s,6.8,3,5.8,'Human challenge','Ask the agent which review IDs support its chosen angle. Compare with at least one contradictory review.');
 s=slide('Choose Between Two Testable Options','Use one controlled change so the next review can explain the result.');panel(s,.65,3,5.8,'Option A: focused outlet test','Pilot an approved launch message in a selected outlet. Measure a defined baseline and test period.');panel(s,6.8,3,5.8,'Option B: broader awareness','Prepare a wider campaign only after checking evidence, capacity and the approved budget.');
 s=slide('Approve the Next Action and Its Check','The agent recommends; the manager selects the actual next step.');panel(s,.65,3,5.8,'Record the decision','Chosen option · owner · review date\nUpdate after the human discussion.');panel(s,6.8,3,5.8,'Acceptance evidence',f"Source revenue total: SGD {data['revenue_total_sgd']:,.2f}\nDashboard and workbook must reconcile.");
 p.save(out/'management-brief.pptx');print('Wrote six-slide editable PPT starter')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['analyse','dashboard','ppt']);ap.add_argument('--input',default='campaign-data.xlsx');ap.add_argument('--out',default='outputs/lab02');a=ap.parse_args();o=Path(a.out);o.mkdir(parents=True,exist_ok=True)
 if a.mode=='analyse':analyse(a.input,o)
 elif a.mode=='dashboard':dashboard(o)
 else:ppt(o)
