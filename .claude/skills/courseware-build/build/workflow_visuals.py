"""Render compact learner-guide workflow models, labelled as design diagrams."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import textwrap
ROOT=Path(__file__).resolve().parents[4]/'courseware'/'assets'/'workflows'
FONTP='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
MODELS={
1:[('1  Choose + connect','One accessible assistant'),('2  Read sources','Assigned Gmail + Calendar'),('3  Draft + review','Source check + correction'),('4  Stop + evidence','Own request/result image')],
2:[('1  Install Desktop','Official app + local profile'),('2  Review skills','Procedure + tools + access'),('3  Read company pack','Source IDs + research brief'),('4  Human decision','Choose angle + verify recall')],
3:[('1  Confirm identity','Assigned Google account'),('2  Read sources','Gmail / Calendar / Drive'),('3  Analyse Excel','Schema + formulas + totals'),('4  Human checks','Sources + recommendations')],
4:[('1  Dashboard + PPT','Verified interactive outputs'),('2  Single-agent video','Approved scenes + real MP4'),('3  Human decision','Exact test-email approval'),('4  Verify + evidence','Sent readback + artifact')],
6:[('1  Register corpus','Source ID / version / owner'),('2  Retrieve passages','Supported or missing evidence'),('3  Independent check','Auditor detects stale fixture'),('4  Assess upkeep','Refresh / access / evaluation')],
7:[('1  Verify access','Dots account + approved files'),('2  Delegate review','Named pack / bounded scope'),('3  Inspect and steer','Source support + correction'),('4  Stop and compare','Actual state + review effort')],
8:[('1  Re-plan team tasks','Bots / owners / parent edges'),('2  Produce video','Approved copy -> actual MP4'),('3  Audit independently','Scenes / sources / metadata'),('4  Human accepts','Exact hash / local release')],
}
def build():
 ROOT.mkdir(parents=True,exist_ok=True)
 for n,stages in MODELS.items():
  im=Image.new('RGB',(1200,460),'#FAF9F5');d=ImageDraw.Draw(im)
  for j,(title,body) in enumerate(stages):
   x=15+(j%2)*605;y=12+(j//2)*225
   d.rounded_rectangle((x,y,x+565,y+185),radius=16,fill='#FFFFFF',outline='#3A7D7B',width=3)
   d.text((x+24,y+25),title,font=ImageFont.truetype(BOLD,31),fill='#21201C')
   for k,line in enumerate(textwrap.wrap(body,33)):
    d.text((x+24,y+83+k*37),line,font=ImageFont.truetype(FONTP,29),fill='#3A7D7B')
  for x,y in [(590,105),(590,330)]:
   d.line((x,y,x+21,y),fill='#C2603F',width=4);d.polygon([(x+25,y),(x+15,y-7),(x+15,y+7)],fill='#C2603F')
  im.save(ROOT/f'activity-{n:02d}.png')
 hub_spoke()
 return ROOT
if __name__=='__main__':build()

def hub_spoke():
 """Learner Guide 3.2: the hub-and-spoke model, redrawn from the trainer's v3.5 screenshot with the Activity 4 team."""
 im=Image.new('RGB',(1200,560),'#FAF9F5');d=ImageDraw.Draw(im)
 B=lambda n:ImageFont.truetype(BOLD,n);R=lambda n:ImageFont.truetype(FONTP,n)
 hx,hy=250,280
 spokes=[('Rafi','market research'),('Lin','LinkedIn post'),('Farah','Facebook post'),('Ivy','Instagram post'),('Pixel','post images')]
 for i,(n,job) in enumerate(spokes):
  y=40+i*100
  d.line((hx+95,hy,700,y+40),fill='#B9B4A9',width=4)
  d.rounded_rectangle((700,y,1170,y+80),radius=14,fill='#FFFFFF',outline='#3A7D7B',width=3)
  d.ellipse((718,y+14,770,y+66),fill='#3A7D7B');d.text((744,y+40),n[0],font=B(28),fill='#FFFFFF',anchor='mm')
  d.text((790,y+20),n,font=B(32),fill='#21201C');d.text((925,y+24),job,font=R(28),fill='#6B6862')
 d.ellipse((hx-95,hy-95,hx+95,hy+95),fill='#D97757')
 d.text((hx,hy-14),'HUB',font=B(40),fill='#FFFFFF',anchor='mm');d.text((hx,hy+28),'coordinator',font=R(26),fill='#FFFFFF',anchor='mm')
 d.text((hx,hy+130),'You, in Activity 4',font=B(30),fill='#21201C',anchor='mm')
 d.text((935,548),'SPOKES · the specialists',font=B(24),fill='#3A7D7B',anchor='mb')
 im.save(ROOT/'hub-and-spoke.png')
