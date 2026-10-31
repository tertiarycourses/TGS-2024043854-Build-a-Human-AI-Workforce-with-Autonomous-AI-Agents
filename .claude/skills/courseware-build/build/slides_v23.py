"""Visual Day 1: history -> collaboration -> always-on -> Big Five -> real setup.
All diagrams are editable teaching models, not simulated execution screenshots.
"""
from ccdeck import *
from slides_2026 import trace,proof,tag,case_pair
from labs_v23 import NEWS,IOS,ANDROID
ARTICLE='https://buldrr.com/claude-duet-vs-muse-vs-grokbot-vs-dots'
METAHELP='https://www.meta.com/help/superintelligence/1687253048996149/'
DUET='https://claude.com/resources/articles/claude-duet'
GROK='https://docs.x.ai/grok-bot/computer-and-apps'
DOTS='https://learn.chatgpt.com/docs/dots/getting-started'
MANUS='https://manus.im/blog/introducing-manus-2-0'
CUE='https://cue.im/'
HERMES='https://hermes-agent.nousresearch.com/docs/user-guide/desktop'
def source(D,url,label='Official source · checked 29 Oct 2026'):
 s=D.prs.slides[-1];t=text(s,.7,6.72,11.9,.24,label,10,TEAL);t.text_frame.paragraphs[0].runs[0].hyperlink.address=url

def links(D,items,y=6.82,step=3.05):
 s=D.prs.slides[-1]
 for k,(label,url) in enumerate(items):
  t=text(s,.7+k*step,y,step-.1,.24,label,10,TEAL);t.text_frame.paragraphs[0].runs[0].hyperlink.address=url

import os
T1A=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','..','courseware','assets','topic1')
def t1a(f):return os.path.normpath(os.path.join(T1A,f))
DOTS_VIDEO='https://www.youtube.com/shorts/gdHwOn2kvT8'
MUSE_VIDEO='https://www.youtube.com/shorts/zuAAjV5dNMA'
GROK_VIDEO='https://www.youtube.com/shorts/Gm_dlNAVOGI'
CUE_VIDEO='https://www.youtube.com/shorts/ZW7gCKTLtpo'
DUET_VIDEO='https://www.youtube.com/shorts/7G5hOD6oF4M'

def _narrow_header(s,w=10.55):
 """Keep kicker/title/subtitle clear of a header-right image."""
 for sh in s.shapes:
  if sh.has_text_frame and sh.top<Inches(2.2) and sh.width>Inches(11): sh.width=Inches(w)

def online_video(s,url,poster,x,y,w,h,name='Online video'):
 """Click-to-play YouTube video, written exactly as PowerPoint's Insert > Video > Online Film does
 (pptx_online_video.py is a copy of the user-level pptx-youtube-video skill). The poster is what PDF exports show."""
 from pptx_online_video import add_online_video
 pic=add_online_video(s,url,x,y,w,h,poster=poster,name=name)
 # Fallback under every video: PowerPoint blocks online media until Enable Content, and offline rooms cannot stream.
 t=text(s,x-.1,y+h+.07,w+.2,.26,'▶ Open in YouTube',10.5,TEAL,bold=True,align='c',autofit=False)
 t.text_frame.paragraphs[0].runs[0].hyperlink.address=url
 return pic

def brief(D,name,sub_,feats,steps,tipt,refs,logo=None,step=3.05,video=None):
 """One briefing slide per always-on agent: what it can do | how to set it up | embedded setup video; app logo top right."""
 s=D.new();header(D,s,'Topic 1 · '+name,name+': What It Does and How to Set It Up',sub_)
 if logo:_narrow_header(s);s.shapes.add_picture(t1a(logo),Inches(11.42),Inches(.5),Inches(1.28),Inches(1.28))
 top,bot=2.3,6.32
 if video:   # three columns: features 4.55 | setup 4.95 | 9:16 player 2.2
  lw,rx,rw=4.55,5.35,4.95;vh=bot-top-.36;vw=vh*9/16;vx=12.7-.1-vw   # 9:16 player, room below for the YouTube link
  card(s,vx-.06,top-.06,vw+.12,vh+.12,fill=INK)
  online_video(s,video[0],t1a(video[1]),vx,top,vw,vh,name=name+' video')
 else:lw,rx,rw=5.6,6.4,6.3
 card(s,.6,top,lw,bot-top);text(s,.85,top+.14,lw-.5,.36,'What it can do',15,ACC,bold=True,font=SERIF,autofit=False)
 rh=(bot-top-.62)/len(feats)
 for i,(ic,t,d) in enumerate(feats):
  y=top+.6+i*rh;icon(s,ic,.85,y+.03,.42)
  text(s,1.42,y-.03,lw-.97,.34,t,13.5,INK,bold=True,font=SERIF,minpt=10.5)
  text(s,1.42,y+.29,lw-.97,rh-.3,d,11 if not video else 10.5,MUTED,minpt=9)
 card(s,rx,top,rw,bot-top,fill=CHAR);text(s,rx+.25,top+.14,rw-.5,.36,'How to set it up',15,ACC,bold=True,font=SERIF,autofit=False)
 rh=(bot-top-.62)/len(steps)
 for i,(t,d) in enumerate(steps):
  y=top+.6+i*rh;circle(s,rx+.25,y+.02,.4,ACC)
  text(s,rx+.25,y+.02,.4,.4,str(i+1),13,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  text(s,rx+.8,y-.03,rw-1.0,.32,t,13.5,WHITE,bold=True,font=SERIF,minpt=10.5)
  text(s,rx+.8,y+.28,rw-1.0,rh-.3,d,11.5 if not video else 10.5,SOFT,minpt=9)
 tip(D,s,tipt,y=6.38);tag(D,'CASE',' ; '.join(u for _,u in refs));links(D,refs,step=step)

def scenario(D,n,title,pitch,hook,examples,img,shot=None,shot_cap=None,tipt=None):
 """One collaboration scenario: a vivid hook and three named real-world examples (left), illustration + optional screenshot (right)."""
 s=D.new();header(D,s,'Topic 1 · Five collaboration scenarios',f'Scenario {n} · {title}',pitch)
 top,bot=2.3,6.3;side=bot-top
 lw=4.95 if shot else 12.1-side-.25
 card(s,.6,top,lw,bot-top)
 text(s,.85,top+.16,lw-.5,1.12,hook,13,INK,font=SERIF,minpt=10.5,lh=1.12)
 text(s,.85,top+1.36,lw-.5,.26,'WHERE YOU SEE IT TODAY',10,TEAL,bold=True,autofit=False)
 y0=top+1.66;rh=(bot-.1-y0)/len(examples)
 for i,(ic,t,d) in enumerate(examples):
  y=y0+i*rh;icon(s,ic,.85,y+.02,.38)
  text(s,1.35,y-.03,lw-.95,.3,t,12.5,INK,bold=True,font=SERIF,minpt=10,autofit=False)
  text(s,1.35,y+.26,lw-.95,rh-.28,d,10.5,MUTED,minpt=9)
 picture(s,t1a(img),12.7-side,top,side,side,frame=True)
 if shot:
  x0=.6+lw+.22;bw=12.7-side-.22-x0
  text(s,x0,top-.02,bw,.26,shot_cap or 'Real example',10,TEAL,bold=True,autofit=False,align='c')
  picture(s,t1a(shot),x0,top+.32,frame=True,maxw=bw,maxh=side-.36)
 if tipt:tip(D,s,tipt,y=6.42)
 return s

def cta(D,label,url,y=6.08,icon_name='download'):
 """A wide click-to-open button below the tip line (whole shape is the link, so the text keeps its styling)."""
 s=D.prs.slides[-1];b=box(s,.6,y,12.1,.66,fill=ACC,shape=MSO_SHAPE.ROUNDED_RECTANGLE);b.click_action.hyperlink.address=url
 icon(s,icon_name,.8,y+.11,.44,fill=ACC_D)
 t=text(s,1.4,y+.08,11.1,.5,label,16,WHITE,bold=True,font=SERIF,anchor='m',autofit=False);t.click_action.hyperlink.address=url
 return b

WHATSAPP='https://wa.me/message/YMQB2CFYVGL3I1'
def whatsapp_try(D):
 """Scenario 2, live: every learner messages the same Tertiary Infotech Academy WhatsApp Business account."""
 s=D.new();header(D,s,'Topic 1 · Try Scenario 2 now','Scan It: One WhatsApp Account, the Whole Room Chatting',
  'Everyone here messages the same Tertiary Infotech Academy account at once. That is Scenario 2 in your pocket.')
 x,y,w,h=picture(s,t1a('whatsapp-qr.png'),.6,2.25,maxw=3.9,maxh=3.7)
 t=text(s,.6,y+h+.12,3.9,.26,'No camera? Click: wa.me/message/YMQB2CFYVGL3I1',10,TEAL,align='c',autofit=False);t.text_frame.paragraphs[0].runs[0].hyperlink.address=WHATSAPP
 rx,rw=4.95,7.75
 for i,(ic,ti,de) in enumerate([('camera','Scan the code','Point your phone camera at it. WhatsApp opens a chat with Tertiary Infotech Academy.'),
   ('chat','Ask it something real','“Which AI agent courses run next month?”   “Send me this course’s brochure.”   “How do I check my SkillsFuture credit?”'),
   ('users','Compare with your neighbour','Same question, same answer? Which replies came back instantly, and which waited for a person?')]):
  yy=2.25+i*1.27;card(s,rx,yy,rw,1.12)
  circle(s,rx+.22,yy+.3,.52,ACC);text(s,rx+.22,yy+.3,.52,.52,str(i+1),16,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  icon(s,ic,rx+.9,yy+.33,.46,fill=TEAL)
  text(s,rx+1.55,yy+.12,rw-1.75,.36,ti,15,INK,bold=True,font=SERIF,autofit=False)
  text(s,rx+1.55,yy+.48,rw-1.75,.6,de,12 if i!=1 else 11.5,MUTED,minpt=9.5,italic=(i==1))
 tip(D,s,'One account, twenty conversations at once: notice how each chat stays separate, and when a human steps in.',y=6.3)
 tag(D,'CASE',WHATSAPP);return s

MUSE_WEB='https://muse.ai/';MUSE_CODE='H1KWDZ'
def muse_invite(D,kick):
 """Activity 1A: everyone joins Muse on the web and redeems the trainer's invite code."""
 s=D.new();header(D,s,kick,'Activity 1A · Join Meta Muse and Claim 1 Billion Tokens',
  'Sign in with Facebook, key in your trainer’s code within 48 hours, and you both get 1 billion Muse tokens.')
 picture(s,t1a('muse-invite.png'),.6,2.2,maxw=3.45,maxh=4.0)
 rx,rw=4.45,8.25
 for i,(ti,de) in enumerate([('Open muse.ai','Sign in with Facebook. It works much like ChatGPT. On your phone? Install Muse from Meta.'),
   ('Settings › General › Usage','Tap Redeem invite code.'),
   ('Key in the code within 48 hours of joining','You and your trainer each receive 1 billion Muse tokens.')]):
  yy=2.2+i*.88;circle(s,rx,yy+.04,.5,ACC)
  text(s,rx,yy+.04,.5,.5,str(i+1),16,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  text(s,rx+.7,yy-.02,rw-.7,.36,ti,16,INK,bold=True,font=SERIF,autofit=False)
  text(s,rx+.7,yy+.36,rw-.7,.42,de,12.5,MUTED,minpt=10)
 card(s,rx,4.9,rw,1.3,fill=CHAR)
 text(s,rx+.35,5.0,3.0,.3,'YOUR TRAINER’S INVITE CODE',11,SOFT,bold=True,autofit=False)
 text(s,rx+.35,5.3,4.2,.8,MUSE_CODE,44,ACC,bold=True,font=MONO,autofit=False,anchor='m')
 t=text(s,rx+4.7,5.12,3.3,.9,'muse.ai\nclick to open',20,WHITE,bold=True,font=SERIF,align='r',autofit=False)
 t.click_action.hyperlink.address=MUSE_WEB   # shape-level link keeps the white text styling
 tip(D,s,'Next, connect Gmail and Google Calendar in Settings → Connectors. Keep retrieve-only access and approve every send.',y=6.35)
 tag(D,'CASE',MUSE_WEB+' ; Muse in-app Invite friends card, 30 Oct 2026');return s

def dots_setup(D,kick):
 """Activity 1B: learners whose ChatGPT plan includes dots set one up; everyone else watches the demo."""
 s=D.new();header(D,s,kick,'Activity 1B · Give Your Own OpenAI Dot Its First Job',
  'On ChatGPT Pro or Business Premium? Set up a dot that keeps working after you close the chat.')
 top,bot=2.2,6.2
 card(s,.6,top,3.7,bot-top,fill=CHAR);text(s,.85,top+.14,3.2,.32,'DO YOU HAVE DOTS?',12,ACC,bold=True,autofit=False)
 for i,(ic,ti,de) in enumerate([('check','Pro · Business Premium','Rolling out now; your first dot is included.'),
   ('building','Enterprise · Edu · Healthcare','Beta, once your workspace admin turns it on.'),
   ('clock','Free · Go · Plus','Not in the launch rollout. Watch the demo; your Muse from 1A does the lab.')]):
  yy=top+.6+i*1.1;icon(s,ic,.85,yy+.02,.42,fill=ACC if i==0 else PANEL)
  text(s,1.4,yy-.04,2.8,.32,ti,13,WHITE,bold=True,font=SERIF,minpt=10.5,autofit=False)
  text(s,1.4,yy+.28,2.8,.75,de,11,SOFT,minpt=9)
 mx,mw=4.5,5.75
 for i,(ti,de) in enumerate([('Open chatgpt.com/dots','ChatGPT mobile or desktop app, or a desktop browser (not mobile web).'),
   ('Create and name your dot','Follow the intro; pick its look. You can change both later.'),
   ('Connect Gmail and Calendar','Add each plugin and authorise it separately in the browser.'),
   ('Give it a standing job','“Every weekday at 8 am, check my calendar for Kopi Kaki meetings and flag any clash.”')]):
  yy=top+i*1.0;circle(s,mx,yy+.04,.46,ACC)
  text(s,mx,yy+.04,.46,.46,str(i+1),15,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  text(s,mx+.62,yy-.02,mw-.62,.34,ti,14.5,INK,bold=True,font=SERIF,autofit=False)
  text(s,mx+.62,yy+.32,mw-.62,.6,de,11.5,MUTED,minpt=9.5,italic=(i==3))
 vh=bot-top-.36;vw=vh*9/16;vx=12.7-.1-vw
 card(s,vx-.06,top-.06,vw+.12,vh+.12,fill=INK);online_video(s,DOTS_VIDEO,t1a('video-dots.jpg'),vx,top,vw,vh,name='OpenAI Dots setup video')
 tip(D,s,'Closing the chat does not stop a dot. Open Activity to see what it is doing, and pause it when class ends.',y=6.35)
 tag(D,'CASE','https://openai.com/index/introducing-dots/ ; '+DOTS)
 links(D,[('OpenAI: Introducing dots (plans) · click','https://openai.com/index/introducing-dots/'),('ChatGPT Learn: Get started with your dot · click',DOTS)],y=6.8,step=4.2)
 return s

WISPR='https://wisprflow.ai/'
def wispr(D,kick):
 """Activity 1C: speak to agents with Wispr Flow instead of typing (facts from wisprflow.ai, 30 Oct 2026)."""
 s=D.new();header(D,s,kick,'Activity 1C · Talk to Your Agents. Stop Typing to Them.',
  'Wispr Flow turns your voice into clean text in any app, so every prompt to Muse, Dots or Hermes can be spoken.')
 top,bot=2.2,5.9
 card(s,.6,top,3.35,bot-top,fill=CHAR)
 text(s,.85,top+.1,2.9,1.2,'4×',72,ACC,bold=True,font=SERIF,autofit=False)
 text(s,.85,top+1.32,2.9,.36,'faster than your keyboard',16,WHITE,bold=True,font=SERIF,autofit=False)
 text(s,.85,top+1.68,2.9,.26,'Wispr Flow’s own claim',10,SOFT,italic=True,autofit=False)
 for i,(ic,t) in enumerate([('globe','100+ languages'),('coins','Free: 2,000 words a week'),('phone','Mac · Windows · iPhone · Android')]):
  yy=top+2.12+i*.5;icon(s,ic,.85,yy,.36,fill=PANEL);text(s,1.32,yy-.01,2.55,.38,t,12,SOFT,anchor='m',autofit=False)
 mx,mw=4.2,4.75
 card(s,mx,top,mw,1.05,fill=LIGHT,shadow=False)
 text(s,mx+.25,top+.12,mw-.5,.26,'TYPED',10,MUTED,bold=True,autofit=False)
 text(s,mx+.25,top+.42,mw-.5,.5,'“check meetings”',17,MUTED,font=MONO,autofit=False)
 card(s,mx,top+1.2,mw,bot-top-1.2)
 text(s,mx+.25,top+1.32,mw-.5,.26,'SPOKEN · TIDIED BY FLOW',10,TEAL,bold=True,autofit=False)
 text(s,mx+.25,top+1.62,mw-.5,1.55,'“Check this week’s Kopi Kaki meetings in Singapore time, flag anything that clashes with Thursday’s supplier tasting, and draft a reply to the outlet manager for me to approve.”',13.5,INK,font=SERIF,italic=True,minpt=11,lh=1.15)
 text(s,mx+.25,bot-.5,mw-.5,.36,'Talking, you give the goal, context and finish line agents need.',11,MUTED,minpt=9.5)
 rx,rw=9.2,3.5
 for i,(ti,de) in enumerate([('Get Flow','Download from wisprflow.ai and sign up; the free plan needs no card.'),
   ('Allow the mic','Grant microphone and accessibility access when asked.'),
   ('Hold, speak, release','Hold your Flow shortcut, say the prompt, let go. The text lands in Muse, ChatGPT or Hermes.')]):
  yy=top+i*1.24;circle(s,rx,yy+.04,.46,ACC)
  text(s,rx,yy+.04,.46,.46,str(i+1),15,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  text(s,rx+.6,yy-.02,rw-.6,.34,ti,14.5,INK,bold=True,font=SERIF,autofit=False)
  text(s,rx+.6,yy+.32,rw-.6,.85,de,11.5,MUTED,minpt=9.5)
 cta(D,'Download Wispr Flow  →  wisprflow.ai   ·   then speak every prompt in this course',WISPR,icon_name='chat')
 tag(D,'CASE',WISPR+' ; https://wisprflow.ai/pricing');return s

GENIC='https://www.genicsolutions.com/ai-agents-for-business-use-cases-and-implementation/'
AGENTSEA='https://www.straitstimes.com/tech/new-platform-to-create-ai-agents-available-to-all-public-healthcare-professionals'
def agentsea(D):
 """Singapore news: Synapxe AgentSea (Straits Times, 24 Aug 2026), straight after the AI history."""
 s=D.new();header(D,s,'Topic 1 · Singapore in the news','Singapore Healthcare: 12,000+ AI Agents in Three Months',
  'AgentSea, Synapxe’s agentic AI platform built with AWS, lets public healthcare staff build their own agents in plain language')
 for j,(big,lab,de) in enumerate([('12,000+','AI agents created','By healthcare professionals, from the end-May 2026 launch to 24 Aug 2026.'),
   ('80,000+','healthcare professionals','Everyone in Singapore’s public health sector can create agents, with little or no coding.'),
   ('300+','agents shared','Published for colleagues to reuse and adapt for their own work.')]):
  x=.6+j*4.1;card(s,x,2.3,3.9,1.95,fill=CHAR if j==0 else WHITE)
  text(s,x+.25,2.36,3.4,.85,big,40,ACC,bold=True,font=SERIF,autofit=False)
  text(s,x+.25,3.18,3.4,.32,lab,14,WHITE if j==0 else INK,bold=True,font=SERIF,minpt=11,autofit=False)
  text(s,x+.25,3.5,3.45,.7,de,11,SOFT if j==0 else MUTED,minpt=9)
 for j,(ic,ti,de) in enumerate([('user','Cardiologist, National Heart Centre','An agent summarises patient histories before clinic, halving 40+ minutes of daily pre-clerking. He still verifies and makes the clinical assessment.'),
   ('calendar','KK Women’s and Children’s Hospital','An agent generates daily staff rosters, cutting manual data entry and transcription errors.'),
   ('shield','Guardrails and governance','Rejects requests for card or ID numbers; MOH’s updated AI in Healthcare Guidelines keep professional judgment with people.')]):
  x=.6+j*4.1;card(s,x,4.45,3.9,1.8);icon(s,ic,x+.22,4.6,.42)
  text(s,x+.75,4.6,3.0,.42,ti,12.5,INK,bold=True,font=SERIF,minpt=10,anchor='m')
  text(s,x+.22,5.12,3.5,1.08,de,11,MUTED,minpt=9)
 tip(D,s,'The course pattern at national scale: agents prepare the work; clinicians verify and decide.',y=6.38)
 tag(D,'CASE',AGENTSEA);links(D,[('The Straits Times, 24 Aug 2026: New platform to create AI agents available to all public healthcare professionals · click',AGENTSEA)],step=12)
 return s

SCI_NEWS=[('Quanta Magazine · 8 Sep 2026','https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/'),
 ('Stanford Medicine · 17 Sep 2026','https://med.stanford.edu/news/all-news/2026/09/virtual-biotech-company.html'),
 ('Nature · 7 Oct 2026','https://www.nature.com/articles/d41586-026-03196-8'),
 ('Firstpost · 27 Oct 2026','https://www.firstpost.com/tech/openai-claims-three-new-ai-breakthroughs-in-math-physics-and-computer-science-14055633.html')]
def science_news(D):
 """2026 AI-for-science news: four results, each with its verification status."""
 s=D.new();header(D,s,'Topic 1 · AI for Science in the news','2026 Breakthroughs: Agents at Scale, Humans Verify',
  'Four reported results. Each shows what the agents did, and what still has to be checked before it counts as a discovery.')
 items=[('flask','Maths · a Millennium Prize problem','OpenAI ran about 10,000 autonomous agents to show the 3D Navier–Stokes fluid equations can “blow up”.','Checked in the Lean proof assistant; humans confirmed the formal statement. Priority dispute with two mathematicians.'),
  ('users','Drug discovery · a virtual biotech','Stanford’s 37,000 AI agents catalogued about 50,000 clinical trials in under a week and designed a lung-cancer antibody–drug conjugate.','A pharma company independently reached the same design; real-lab testing of other findings is next.'),
  ('file','Maths at volume · 700+ preprints','OpenAI posted more than 700 AI-generated maths preprints from an unreleased model.','Mathematicians call them a “messy first draft” and raise credit and pre-emption concerns.'),
  ('target','Maths, physics and computing claims','OpenAI claims proofs on Kakeya conjectures and 4D quantum field theory, and an algorithm that would disprove the Exponential Time Hypothesis.','Claims awaiting verification; expert panels are reviewing them.')]
 for j,(ic,ti,de,chk) in enumerate(items):
  x=.6+(j%2)*6.15;y=2.25+(j//2)*2.0;card(s,x,y,5.95,1.88)
  icon(s,ic,x+.2,y+.16,.42);text(s,x+.75,y+.12,4.95,.32,ti,13.5,INK,bold=True,font=SERIF,minpt=11,autofit=False)
  text(s,x+.75,y+.42,5.0,.36,SCI_NEWS[j][0],10,TEAL,bold=True,autofit=False)
  text(s,x+.2,y+.74,5.55,.56,de,11,MUTED,minpt=9)
  rich(s,x+.2,y+1.3,5.55,.55,[[('CHECK  ',dict(color=ACC,bold=True,size=10.5)),(chk,dict(color=INK,size=10.5))]])
 tip(D,s,'Agents now propose at massive scale. Proof checkers, laboratories and experts still decide what counts as a discovery.',y=6.3)
 tag(D,'CASE',' ; '.join(u for _,u in SCI_NEWS));links(D,[(t+' · click',u) for t,u in SCI_NEWS],step=3.05)
 return s

def analogy(D):
 """Visual analogy: Human = Brain + Body --food--> Work; AI agent = Model + Harness --tokens--> Work."""
 s=D.new();header(D,s,'Topic 1 · Under the hood','An AI Agent Works Like a Person','Brain + body need food to do work. Model + harness need tokens to do work.')
 rows_=[('HUMAN','user',PLUM,[('brain','Brain','Thinks, plans, decides'),('hand','Body','Hands, eyes and tools act')],('coffee','Food','Energy'),('briefcase','Work','The job gets done')),
        ('AI AGENT','robot',TEAL,[('sparkles','Model','Reasons, proposes next step'),('gear','Harness','Tools, memory, skills, controls')],('coins','Tokens','Fuel and cost'),('check','Work','Verified output'))]
 def node(x,ic,t,d,fill):
  circle(s,x-.55,cy-.55,1.1,fill);icon(s,ic,x-.42,cy-.42,.84,fill=fill)
  text(s,x-1.15,cy+.62,2.3,.4,t,19,INK,bold=True,font=SERIF,align='c',autofit=False)
  text(s,x-1.15,cy+.98,2.3,.36,d,11,MUTED,align='c',minpt=9)
 for r,(lab,lic,col,parts,fuel,work) in enumerate(rows_):
  y=2.2+r*2.08;cy=y+.72
  card(s,.6,y,12.1,1.95,fill=WHITE);box(s,.6,y,.12,1.95,fill=col)
  circle(s,1.0,cy-.42,.84,col);icon(s,lic,1.1,cy-.32,.64,fill=col)
  text(s,.75,cy+.5,1.35,.3,lab,12,col,bold=True,align='c',autofit=False)
  node(3.25,*parts[0],ACC);text(s,4.45,cy-.42,.6,.84,'+',40,ACC,bold=True,font=SERIF,align='c',anchor='m',autofit=False);node(6.25,*parts[1],ACC)
  box(s,7.4,cy-.08,2.15,.16,fill=col);box(s,9.45,cy-.3,.45,.6,fill=col,shape=MSO_SHAPE.ISOSCELES_TRIANGLE).rotation=90
  box(s,7.6,cy+.22,1.75,.62,fill=col,shape=MSO_SHAPE.ROUNDED_RECTANGLE)
  icon(s,fuel[0],7.66,cy+.28,.5,fill=col);text(s,8.18,cy+.22,1.15,.36,fuel[1],15,WHITE,bold=True,font=SERIF,autofit=False)
  text(s,8.18,cy+.52,1.15,.28,fuel[2],9.5,WHITE,autofit=False)
  node(10.85,*work,CHAR)
 tip(D,s,'No food, no work; no tokens, no work. Every read, reasoning step and reply spends tokens, so a token budget is the agent’s running cost.',y=6.4)
 tag(D,'MODEL','Trainer analogy: human brain/body/food vs model/harness/tokens')
 return s

def illustrated(D,k,title,steps,img,tipt,source):
 """Four numbered steps (left) beside a wide illustration (right)."""
 s=D.new();header(D,s,k,title)
 top,bot=1.95,6.15;card(s,.6,top,5.25,bot-top);rh=(bot-top-.2)/len(steps)
 for i,(ic,t,d) in enumerate(steps):
  y=top+.14+i*rh;circle(s,.82,y+.05,.42,ACC)
  text(s,.82,y+.05,.42,.42,str(i+1),13,WHITE,bold=True,font=SERIF,align='c',anchor='m',autofit=False)
  if i<len(steps)-1:line(s,1.03,y+.5,1.03,y+rh+.02,color=SOFT,w=1.25)
  text(s,1.42,y-.02,4.25,.34,t,14,INK,bold=True,font=SERIF,minpt=11,autofit=False)
  text(s,1.42,y+.31,4.25,rh-.34,d,11.5,MUTED,minpt=9)
 picture(s,t1a(img),6.1,top,frame=True,maxw=6.6,maxh=bot-top)
 tip(D,s,tipt,y=6.32);tag(D,'ARCH',source);return s

def topic1(D,C,mark):
 """Topic 1 narration: what agents are -> how they work -> where people decide -> where they are used
 -> the always-on agents (one briefing slide each) -> Lab 1 (1A Muse invite, 1B Dots) (the topic ends with its lab)."""
 mark('t1a')
 section(D,'Topic 1',C.TOPICS[0]['title'],['Brief history and what an agent is','Under the hood: how agents work','AI does the work; humans decide','Five collaboration scenarios','Use cases and the Big Five always-on agents','Activity 1 · Join Muse, set up a dot'])
 timeline(D,'Topic 1 · Brief history','From Rules to Learning to Action',[
 ('Rules','1950s–80s','Explicit rules and expert systems.'),('Learning','1990s–2010s','Patterns learned from examples.'),('Language','2017–2023','Transformers and chat interfaces.'),('Action','2024 onward','Tool use, feedback and goal-directed work.')],foot='These approaches coexist. A modern agent still uses ordinary software, rules and databases.');tag(D,'MODEL','Attention Is All You Need 2017; ReAct 2022')
 timeline(D,'Topic 1 · Brief history','2023 → 2026: Four Engineering Lenses',[
 ('Prompt Engineering','2023','Specify goal, audience and output.'),('Context Engineering','2024','Provide relevant facts and instructions.'),('Harness Engineering','2025','Connect tools, state and checks.'),('AI Agents','2026','Delegate outcomes and inspect results.')],foot='Course framing: overlapping priorities, not invention dates or exclusive eras.');tag(D,'MODEL','Trainer-requested teaching sequence; agent and context engineering literature')
 agentsea(D)
 compare(D,'Topic 1 · Agents and agentic AI','Agentic AI Is the System. An Agent Does the Work.',
 ('Agentic AI','network',['Goal-directed planning, action and feedback.','May contain one agent or a coordinated team.','The harness controls access, state and execution.']),
 ('Always-on agent · course focus','clock',['A persistent, 24/7-capable agentic system.','Can act between messages while runtime is available.','Examples: OpenClaw, Hermes, Muse and Dots.']),tipt='Always-on describes the deployment we study; it is not a universal definition of every AI agent or an uptime promise.');tag(D,'ARCH','Anthropic building effective agents; vendor agent documentation')
 # Under the hood (before Lab 1): analogy -> the model inside its harness -> tools and skills -> the loop.
 analogy(D)
 hub(D,'Topic 1 · Under the hood','What Makes an AI Agent: a Model Inside a Working System','AI agent',[
 ('brain','Model','Reasons and proposes the next action.'),('tool','Tools','Read, calculate, browse, render.'),('book','Skills','Reusable procedures and checks.'),('memory','Memory','Approved persistent facts.'),('folder','Knowledge base','Curated evidence and versions.'),('file','Instructions','Goal, policy and output contract.'),('shield','Runtime controls','Loop, permissions, limits and logs.')],foot='A more capable model cannot compensate for missing access, poor sources or an unverified action.');tag(D,'ARCH',HERMES)
 compare(D,'Topic 1 · Under the hood','Tools Execute. Skills Explain How.',
 ('Tool','tool',['The Gmail connector reads your inbox through a real API.','Python calculates a workbook total.','FFmpeg renders an actual MP4.']),
 ('Skill','book',['kopi-email-brief sets read limits and source checks.','professional-ppt defines a repeatable slide process.','launch-video defines scenes, render and QA.']),tipt='Installing a skill creates neither the executable nor Google permission. Verify all three separately.');tag(D,'ARCH',HERMES)
 loop(D,'Topic 1 · Under the hood','The Agentic Loop: Observe, Act, Verify',[
 ('target','Goal','Bounded outcome'),('search','Observe','Read permitted evidence'),('brain','Select','Choose next action'),('tool','Act','Execute tool'),('eyecheck','Verify','Inspect real result'),('hand','Decide','Repeat, ask or stop')],foot='Tool errors are observations. Never replace an unavailable result with an invented success.');tag(D,'ARCH','ReAct; Hermes documentation')
 # Where people stay in charge.
 compare(D,'Topic 1 · Human–AI work','AI Agents Do the Work. Humans Decide.',
 ('AI agent','robot',['Reads the permitted source records.','Uses tools to calculate, draft and produce.','Checks the result and reports exceptions.']),
 ('Human','user',['Chooses the goal and permitted access.','Exercises judgment when facts or values conflict.','Approves consequential actions and accepts work.']),tipt='Example: agent proposes a meeting time; you resolve a conflict and approve the message.');tag(D,'MODEL','IBM human-AI collaboration; classroom task contract')
 compare(D,'Topic 1 · Two collaboration modes','Personal Assistant or Digital Worker?',
 ('Personal assistant','calendar',['Organises YOUR day: email, schedule, travel.','Success: a source-checked brief and useful draft.','You decide priorities and approve commitments.']),
 ('Digital worker','briefcase',['Performs a BUSINESS role: analyst, coder, bookkeeper.','Success: verified work products and a review trail.','A named owner accepts the result and exceptions.']),tipt='These are work roles, not two different kinds of language model.');tag(D,'MODEL','IBM; BULDRR job-fit framing; course design')
 # Five collaboration scenarios (Scenario 2 is followed by a live WhatsApp try-it): from one person and one agent to agents working across companies.
 scenario(D,1,'One Human, One AI Agent','Your own chief of staff that never clocks off',
  'One person, one always-on agent. It works through your inbox and calendar overnight and is waiting with a brief, a clash and a draft before you wake up.',
  [('sparkles','Always-on personal assistants','OpenAI Dots, Meta Muse, Grok Bot, Claude Duet and Manus Cue: the Big Five you meet later today.'),
   ('server','A desktop agent on your own laptop','Hermes Desktop, the single office worker you run this afternoon.'),
   ('code','A coding partner for one developer','Claude Code or OpenAI Codex working through one person’s repository.')],
  'pattern1.jpg','p1-assistant-chat.png','Real example · names blurred',tipt='On the right: an assistant spots a weekend clash between two booked course days and a new teaching request.')
 scenario(D,2,'Multiple Humans, One AI Agent','One agent, a whole team asking it for help',
  'Drop one agent into the team chat and it becomes the colleague everyone pings. It updates systems, chases blockers and reports back to the whole group.',
  [('chat','A bot in the team group chat','An OpenClaw or Hermes agent in Telegram or WhatsApp, like the trainers’ chat on the right.'),
   ('users','An assistant the whole channel can call','Claude in Slack, or any bot a channel can @mention.'),
   ('inbox','A shared front desk','One agent triaging a shared support inbox for the whole service team.')],
  'pattern2.jpg','p2-group-chat.png','Real example · names blurred',tipt='The best shared agents say out loud what they verified and what is still unknown.')
 whatsapp_try(D)
 scenario(D,3,'One Human, Multiple AI Agents','Be the manager of your own AI department',
  'One person splits the goal and hands each piece to a specialist: a researcher, a writer, a producer and an auditor. The work runs in parallel while you approve the hand-offs.',
  [('kanban','Hermes profiles on a Kanban board','Your Day 2 video studio: research → script → video → audit.'),
   ('users','Several Grok Bots on one cloud computer','Each bot has its own screen while sharing files and logins.'),
   ('robot','A Manus Cue agent team','Agents share a group chat and a goal; you make the final call.')],
  'pattern3.jpg','p3-hermes-profiles.png','Real example · Hermes profiles',tipt='On the right: six Hermes profiles that run a YouTube channel from research to upload.')
 scenario(D,4,'Multiple Humans, Multiple AI Agents','When a whole organisation runs on agents',
  'Many people, each building and running their own agents, all pointed at shared goals. This is where agents stop being a gadget and become part of the workforce.',
  [('hospital','Singapore public healthcare','80,000+ staff have built 12,000+ AgentSea agents and shared 300+ for colleagues to reuse.'),
   ('flask','Stanford’s virtual biotech','A research team directs 37,000 AI scientist agents across drug-discovery divisions.'),
   ('kanban','Your department’s shared board','Every card has a human owner and an agent assignee: Day 2 at team scale.')],
  'pattern4.jpg',tipt='Scale needs governance: named owners, permissions for each role and an audit trail.')
 scenario(D,5,'Inter-Company Collaboration','Your agent negotiates with their agent',
  'Agents start working across the company wall. A buyer’s agent requests quotes, a supplier’s agent checks stock and replies, and people on both sides sign off.',
  [('network','Agent-to-agent protocols','Open standards such as Google’s Agent2Agent (A2A) let agents from different vendors talk to each other.'),
   ('cart','Personal agents meeting business services','Meta Muse working with Singapore partners such as Grab and Singapore Airlines as they roll out.'),
   ('phone','Agents with their own identity','Manus Cue agents with their own email, phone and wallet, calling and paying outside businesses.')],
  'pattern5.jpg',tipt='Treat anything from another company’s agent as untrusted until a person verifies it.')
 # Five business use cases (Genic Solutions, 30 Sep 2026); AI for Science and the humanoid task follow.
 cases=[
 ('Customer service operations','Incoming requests + account history','Classify, look up the account, draft a reply, suggest next step','Complex or sensitive cases; limits on what it may complete','Prepared response + next action','Less time spent searching for information','Digital worker · customer service'),
 ('IT service management','Access, account, device and software requests','Collect details, check known issues, create and route tickets','Technician fixes; approves access changes','Triage-ready ticket with details','Repeat requests routed to the right group','Digital worker · IT support'),
 ('Finance operations','Invoices, payment queries, internal records','Read documents, match records, flag missing details','Approves payments and high-risk actions','Items prepared for approval','Clear approval rules applied every time','Digital worker · finance'),
 ('Sales operations','Customer records + meeting notes','Update records, prepare notes, create follow-up tasks','Salesperson owns the customer relationship','Updated records + follow-up tasks','Less administration for sales staff','Digital worker · sales'),
 ('Procurement and supply chain','Orders, stock, supplier and delivery data','Monitor orders, flag delays, gather facts across systems','Operations manager decides the response','Delay alert with consolidated records','Delays flagged with supporting records','Digital worker · operations')]
 for i in range(0,len(cases),2):
  case_pair(D,'AI Agents for Business: Five Use Cases','handshake',cases[i:i+2],i+1,kick='Topic 1 · Use cases',sub='Business functions · what the agent does, what people decide, and the evidence to check')
  links(D,[('Genic Solutions, 30 Sep 2026: AI Agents for Business, Use Cases and Implementation · click',GENIC)],step=12);tag(D,'CASE',GENIC)
 illustrated(D,'Topic 1 · Scientific collaboration','AI for Science: Proposal → Experiment → Discovery',[
 ('user','Research goal','Scientist sets the question and constraints.'),('users','Hypotheses','An AI co-scientist proposes, critiques and ranks ideas.'),('flask','Experiment','Scientists test the selected hypotheses in the lab.'),('check','Validation','New evidence supports or rejects the claim.')],
 'ai-for-science.jpg','A plausible proposal is not a discovery. Record provenance and experimental results.','https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/')
 science_news(D)
 illustrated(D,'Topic 1 · Future collaboration','Humanoid + Human: A Bounded Physical Task',[
 ('eye','Sense','The robot observes the authorised room and the resident it is helping.'),('brain','Plan','It proposes one bounded task, such as handing over water or a walking aid.'),('user','Authorise','A caregiver confirms the task and keeps the stop control.'),('check','Verify','The caregiver checks the hand-off, the resident’s response and recovery behaviour.')],
 'humanoid-elderly-care.jpg','Prospective design for elderly care. Manufacturer demos are not proof of safe deployment in homes or care facilities.','https://deepmind.google/models/gemini-robotics/')
 mark('t1b')
 timeline(D,'Topic 1 · Deployment evolution','OpenClaw → Hermes → Hosted Personal Agents',[
 ('OpenClaw','Configurable harness','Local/server tools and channels.'),('Hermes Agent','Desktop + skills','Local workflow, memory and reusable procedures.'),('Hosted agents','Managed cloud','Dots, Muse, Duet, Grok Bot and Cue.'),('Your choice','Work + control','Access, oversight, cost and data boundaries.')],foot='A teaching progression in deployment choices, not corporate lineage or a claim one product replaced another.');tag(D,'ARCH','Official OpenClaw, Hermes, Meta, Anthropic, xAI and OpenAI docs')
 table(D,'Topic 1 · The Big Five','The Big Five: Same Always-On Idea, Different Jobs',
 ['Product','Useful starting job','Human control to inspect','Access checkpoint'],[
 ('Muse','Schedule, errands and personal email','Connector permissions + sensitive-action approval','Singapore since 27 Oct; free core use'),
 ('Dots','Persistent goals and delegated tasks','Connection permissions, custom rules and review','Pro, Business Premium; Enterprise beta'),
 ('Grok Bot','Named workers sharing ongoing work','Approval settings; shared cloud logins across bots','Check your plan’s access'),
 ('Duet','Work briefs and business follow-ups','Approval before sensitive actions; some actions disallowed','US Pro/Max waitlist preview'),
 ('Cue','Personal errands, bookings and calls','Per-agent permissions, wallet budget, review boundaries','Early access; free with invite code')],colw=[1.4,3.4,4.6,2.7],size=12.5,sub='Five hosted always-on agents; one briefing slide each follows, with its official source.',tipt='No universal winner. Verify your current account, region, connector and action controls before delegating.');tag(D,'MODEL',ARTICLE+' ; '+DUET+' ; '+NEWS+' ; '+GROK+' ; '+DOTS);source(D,ARTICLE,'Comparison reference: BULDRR · click to read')
 brief(D,'Meta Muse','Meta · available in Singapore since 27 Oct 2026 · Activity 1A: everyone joins with the trainer’s invite code',[
  ('check','Does the work','Manages email, coordinates schedules and turns long-term goals into action plans.'),
  ('plug','Connected apps','Gmail, Google Calendar and Instagram; Singapore partners such as Grab, Shopee and Singapore Airlines are rolling out.'),
  ('shield','Asks before acting','Checks with you before sending an email or making a purchase; retrieve-only connectors available.'),
  ('lock','Secure and mostly free','Muse Secure VM keeps passwords and payment methods out of the agent’s view; iOS, Android and muse.ai.')],
  [('Install','Muse from Meta (iOS / Android) or muse.ai.'),
   ('Sign in','Complete onboarding; link your Meta accounts.'),
   ('Connect Gmail','Settings → Connectors → Connect beside Gmail → Continue.'),
   ('Authorise','Finish the Google login in the browser; repeat for Google Calendar.'),
   ('Approvals','Keep retrieve-only where offered; approve every send or invite.')],
  'Shortcut: ask “Connect my Gmail”. Partner features roll out progressively; no bookings or purchases in class.',
  [('Meta Newsroom: Muse in SG · click',NEWS),('Meta Help: Connectors · click',METAHELP),('Muse iOS (SG) · click',IOS),('Muse Android (SG) · click',ANDROID),('YouTube: 10 ways to use Muse',MUSE_VIDEO)],logo='logo-muse.png',video=(MUSE_VIDEO,'video-muse.jpg'),step=2.44)
 brief(D,'OpenAI Dots','OpenAI · rolling out to ChatGPT Pro and Business Premium · Activity 1B if your plan has it',[
  ('target','Ongoing responsibilities','Give one dot several long-running jobs instead of one-off chats.'),
  ('server','Its own cloud computer','Works in its own browser; optionally on your computer while the ChatGPT app is open.'),
  ('puzzle','Plugins and channels','Email, calendar and files through plugins; Slack and other contact methods for messages.'),
  ('clock','Delegates and schedules','Hands parts to ChatGPT Work or Codex; fixed schedules, event triggers and an Activity view.')],
  [('Open dots','ChatGPT mobile app, desktop app or desktop browser (not mobile web).'),
   ('Create a dot','Follow the intro; name it and pick its look (changeable later).'),
   ('Plugins','Connect email, calendar and files plugins; authorise each one.'),
   ('Channels','Optional: profile → Add a contact method such as Slack.'),
   ('Assign work','Describe an ongoing responsibility, its sources and your decisions.')],
  'A messaging channel does not grant inbox access. Ending a chat does not stop assigned work: check Activity.',
  [('ChatGPT Learn: Get started with your dot · click',DOTS),('YouTube: How to set up your first dot (Short) · click',DOTS_VIDEO)],logo='logo-dots.png',video=(DOTS_VIDEO,'video-dots.jpg'),step=4.2)
 brief(D,'Grok Bot','xAI · Grok Bot documentation, updated 28 Oct 2026 · check your plan’s access',[
  ('server','Persistent cloud computer','Browser, command line and files; keeps working while your laptop is closed.'),
  ('users','Several bots, one computer','Each bot has its own screen; sessions, files and logins are shared across your bots.'),
  ('mail','Apps, MCP and its own email','Gmail, Calendar, Sheets, Slack and Notion; mail to name@mail.grokbot.com can start routines.'),
  ('eye','Watch, take over, review','Live computer view; take control for a sign-in or CAPTCHA; Auto Review gates sends.')],
  [('Install','Start at x.ai/bot; get the desktop or mobile app and sign in.'),
   ('Create a bot','Sidebar + → Create a Bot → name it → Create.'),
   ('Connect apps','Open Connect apps (mobile: avatar → Connect apps); add Gmail.'),
   ('Authorise','Finish the Google login in the browser; repeat for Google Calendar.'),
   ('Verify','Both show under Installed; “Added” is not signed in, so fix “Needs auth”.')],
  'All bots on one account share a cloud computer and logins. The bot’s @mail.grokbot.com inbox is not your Gmail.',
  [('xAI docs: Grok Bot computer and apps · click',GROK),('YouTube: 3 steps to set up Grok Bot (Short) · click',GROK_VIDEO)],logo='logo-grok.png',video=(GROK_VIDEO,'video-grok.jpg'),step=4.2)
 brief(D,'Claude Duet','Anthropic research preview · 21 Oct 2026 · US Pro/Max via waitlist · reference route',[
  ('calendar','Morning brief, then watching','A daily brief, then checks every few hours; messages you only when something needs you.'),
  ('server','Works while you are away','Its own virtual machine and browser: meetings, dashboards, forecasts, prototypes and web apps.'),
  ('puzzle','6,000+ connectors','Gmail, Slack, QuickBooks, Stripe, HubSpot, Docusign, Canva, Shopify and more.'),
  ('shield','You approve actions','Shows exactly what it will send, pay, sign or delete and waits; some actions stay off-limits.')],
  [('Get access','Pro or Max plan; join the Claude Duet waitlist on claude.com.'),
   ('Install','Open the Claude Duet app (iOS / Android) or claude.ai once invited.'),
   ('Carry context','Memory, skills and apps carry over from your Claude account.'),
   ('Connect apps','Add Gmail, Calendar, Slack or others from the Claude Marketplace.'),
   ('Set the brief','Tell it what to watch and how often; approve every send or payment.')],
  'Reference route, not assessed. Background checks use your plan limits; some actions stay off-limits even with approval.',
  [('Anthropic: Introducing Claude Duet · click',DUET),('YouTube: Claude Duet is here (Short) · click',DUET_VIDEO)],logo='logo-duet.png',video=(DUET_VIDEO,'video-duet.jpg'),step=4.2)
 brief(D,'Manus Cue','Manus · early access since 28 Sep 2026 · free with an invite code · reference route',[
  ('user','Agent identity','Each agent has its own email address, phone number, wallet and computer.'),
  ('phone','Calls, messages, payments','Takes forwarded calls, emails from its own address and pays within the budget you set.'),
  ('users','Agent teams','Agents share a group chat and a goal; you make the final call.'),
  ('puzzle','Connectors and routines','Gmail, Trip.com, Oura and more; routines repeat your steps; scan a QR code to create an agent.')],
  [('Get Cue','cue.im on the web, desktop or Android; iOS pending.'),
   ('Invite code','Sign up with an invite code from your trainer or a user.'),
   ('Create an agent','Give it one responsibility and the context it needs.'),
   ('Identity + limits','Choose its email, phone, wallet; set budgets and approvals.'),
   ('Connect + routines','Connect Gmail or other services, then define routines for repeat steps.')],
  'Reference route, not assessed. Keep wallet budgets small; require approval for payments, calls and messages.',
  [('Cue by Manus: cue.im · click',CUE),('YouTube: Meet Manus Cue (Short) · click',CUE_VIDEO)],logo='logo-cue.png',video=(CUE_VIDEO,'video-cue.jpg'),step=4.2)

def pp1_evidence(D,kick):
 """PP Task 1 evidence, shown inside Lab 1."""
 proof(D,kick,'PP Task 1 Has Two Images and Written Analysis',[
 ('camera','Image A · morning','Own chosen assistant request/result: real schedule check or email draft.'),('file','Image B · afternoon','Own Hermes-generated artifact: PPT, dashboard, analysis or video.'),('eyecheck','Keep working evidence','Source references, actual artifact and tool/run trace.'),('pen','Written analysis','Explain underlying LLM/agent loop, strengths and limitations for the paper’s client.')],'Current assessment v7; A1 and A3 unchanged')

def office_extra(D):
 units=[
 ('Install a Skill Only After Reviewing Its Source',[('search','Origin','Official or supplied reviewed source; record version.'),('book','Inspect','Read SKILL.md and any scripts it can run.'),('lock','Destination','Selected Desktop profile’s actual Skills folder.'),('check','Probe','Reload, list skill and run a harmless tool test.')]),
 ('Five Skills, One Hermes Agent',[('mail','gog-office','Read sources with bounds and provenance.'),('chart','office-analytics','Schema, formulas and reconciliation.'),('file','professional-ppt','Editable decision story and rendered check.'),('code','interactive-dashboard','Filters, sorting and CSV export, tested offline.'),('film','launch-video','Approved scenes, render and video QA.')]),
 ('Native Desktop and WSL Are Separate Runtimes',[('server','Native app','Uses native paths, PATH and credential store.'),('code','WSL','Linux paths and executables are separate.'),('alert','Symptom','Terminal works, Desktop cannot find gog.'),('check','Fix','Probe inside the selected Desktop runtime; restart only that gateway if needed.')]),
 ('Check Skill, Tool and Permission Separately',[('book','Skill','Does Hermes load the intended SOP?'),('tool','Tool','Does gog/FFmpeg execute in that runtime?'),('lock','Permission','Does the assigned account have the needed service grant?'),('file','Output','Can the real source/artifact be opened independently?')]),
 ('The Office Pack Has a Stable Data Contract',[('file','Brief','outputs/lab01/research-brief.md'),('chart','Analysis','outputs/lab02/analysis.json and analysis.xlsx'),('file','Artifacts','outputs/lab02/dashboard.html and management-brief.pptx'),('film','Videos','Day 1: outputs/single-video; Day 2: outputs/team/video')]),
 ('First Authorise Read-Only Gmail',[('login','Client','Trainer-supplied Desktop OAuth client.'),('user','Account','Assigned Google identity; browser consent.'),('lock','Scope','--services gmail,calendar,drive --gmail-scope readonly'),('shield','Runtime','--readonly and Gmail --gmail-no-send on reads.')]),
 ('One Test Send Is a Separate Procedure',[('pen','Prepare','Exact recipient, subject, body and attachments.'),('user','Approve','Trainer-approved training recipient; explicit SEND decision.'),('lock','Grant','Inspect installed help; preserve existing services when reauthorising write.'),('check','Read back','Send once; verify returned message ID and actual Sent record.')]),
 ('Read-Only Defaults Resume After the Test',[('shield','Default','gog-office remains the read-only SOP.'),('mail','Exception','Only the approved test-send procedure may send.'),('eyecheck','Inspect','One send result; no hidden follow-up automation.'),('check','Restore','Next reads again use --readonly and --gmail-no-send.')]),
 ('An Email Draft Is Not a Sent Message',[('pen','Draft text','Local text has no mailbox delivery state.'),('file','Server draft','Saved draft has an ID but has not been sent.'),('mail','Send result','Real send returns a message ID.'),('check','Verification','Inspect actual Sent record for To/Subject/body.')]),
 ('Make a Single-Agent Video Before a Team Video',[('book','Skill','launch-video supplies the procedure.'),('tool','Renderer','One Hermes agent invokes local FFmpeg tool.'),('film','Output','Real 15s 1080x1920 H.264 MP4.'),('user','Review','Watch full video; approve exact hash.')]),
 ('A Storyboard Is an Input, Not a Completed Video',[('pen','Script','Three approved five-second scenes.'),('code','Render','Run the actual reviewed local tool.'),('eye','Playback','Inspect all scenes and ffprobe metadata.'),('check','Accept','Store MP4, QA evidence and human decision.')]),
 ('Video Rights and Facts Need Checks',[('file','Facts','Approved price, launch date and offer terms.'),('image','Assets','Use supplied or appropriately licensed assets.'),('shield','Claims','No unsupported health/certification promises.'),('user','Decision','Human checks every scene before accepting.')]),
 ('A Small Video Change Invalidates Old Acceptance',[('file','Version 1','Watch, audit and hash actual MP4.'),('user','Revision','Human requests one concrete scene correction.'),('tool','Version 2','Re-render and repeat scene/metadata checks.'),('check','Accept','Log new hash; previous approval does not carry over.')]),
 ('Total Time Includes Setup and Human Review',[('clock','Setup','Installation, consent and source preparation.'),('robot','Run','Agent work and deterministic tool execution.'),('eyecheck','Review','Source checks, render inspection and corrections.'),('chart','Compare','Use total time per accepted artifact, not model speed alone.')]),
 ('Office Failures Should Stay Visible',[('alert','Missing service','Mark Calendar unavailable rather than empty.'),('chart','Mismatch','Stop when aggregates disagree with source rows.'),('file','Bad output','Open PPT/MP4; completion text is insufficient.'),('hand','Human decision','Repair or record incomplete; never manufacture evidence.')]),
 ('Create a Reusable Skill from a Real Correction',[('eyecheck','Observe','Find an actual calculation or layout defect.'),('book','Improve','Add a specific check to the reviewed skill.'),('loop','Repeat','Run a new bounded task from source.'),('check','Evaluate','Compare defect rate, review time and accepted output.')])]
 return {t:(lambda k,t=t,items=items:proof(D,k,t,items,HERMES)) for t,items in units}
