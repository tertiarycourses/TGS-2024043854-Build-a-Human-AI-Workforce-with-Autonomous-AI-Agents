"""Render compact learner-guide workflow models, labelled as design diagrams."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import textwrap
ROOT=Path(__file__).resolve().parents[4]/'courseware'/'assets'/'workflows'
FONTP='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
MODELS={
2:[('1  Confirm identity','Assigned Google account'),('2  Read sources','Gmail / Calendar / Drive'),('3  Analyse Excel','Schema + formulas + totals'),('4  Human checks','Sources + recommendations')],
4:[('1  Inspect sources','Email text stays data'),('2  Surface conflict','Two deadlines + source IDs'),('3  Human decision','Owner chooses correction'),('4  Recheck version','File hash + approval log')],
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
 return ROOT
if __name__=='__main__':build()
