#!/usr/bin/env python3
"""Deterministic 15s local baseline; the producer adapts the approved scene copy."""
import argparse,subprocess,json,hashlib
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

def font(size):
 for p in ['/System/Library/Fonts/Supplemental/Arial Bold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','C:/Windows/Fonts/arialbd.ttf']:
  if Path(p).exists():return ImageFont.truetype(p,size)
 raise RuntimeError('Install a scalable font or set a valid font path; do not render tiny fallback text.')
def render(out):
 out.mkdir(parents=True,exist_ok=True)
 scenes=[('Heritage kopi.','Modern craft.','Kopi Kaki Co.'),('Gula Melaka','Cold Brew','SGD 6.80'),('Visit Kopi Kaki','1 December 2026','#ShiokColdBrew')]
 for n,lines in enumerate(scenes):
  im=Image.new('RGB',(1080,1920),'#F6EBD9');d=ImageDraw.Draw(im)
  d.rounded_rectangle((100,120,980,1800),radius=60,fill='#5B3A29')
  d.ellipse((390,350,690,650),fill='#C7782A');d.rounded_rectangle((420,400,640,590),25,fill='#F6EBD9')
  for y,t in zip([840,980,1220],lines):
   f=font(72 if y<1200 else 52)
   if d.textlength(t,font=f)>780:f=font(54)
   d.text((540,y),t,anchor='mm',fill='#F6EBD9',font=f)
  d.text((540,1650),'AI-ASSISTED TRAINING VIDEO',anchor='mm',font=font(25),fill='#F6EBD9');im.save(out/f'frame-{n:02d}.png')
 cmd=['ffmpeg','-y','-framerate','1/5','-i',str(out/'frame-%02d.png'),'-c:v','libx264','-r','30','-pix_fmt','yuv420p','-t','15','-movflags','+faststart',str(out/'final.mp4')]
 subprocess.run(cmd,check=True,capture_output=True)
 probe=subprocess.run(['ffprobe','-v','error','-show_entries','stream=width,height','-show_entries','format=duration','-of','json',str(out/'final.mp4')],check=True,capture_output=True,text=True)
 (out/'metadata.json').write_text(probe.stdout);(out/'render-log.md').write_text('Command:\n'+repr(cmd)+'\n\nMP4 SHA256: '+hashlib.sha256((out/'final.mp4').read_bytes()).hexdigest()+'\n')
 (out/'description.md').write_text('AI-assisted training video for fictional Kopi Kaki Co. Visual frames were rendered locally with Pillow/FFmpeg; no voice-over or music is used. Human review is required before any release.\n')
 print(probe.stdout)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='outputs/team/video');a=ap.parse_args();render(Path(a.out))
