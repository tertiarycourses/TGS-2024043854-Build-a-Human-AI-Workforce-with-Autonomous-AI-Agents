#!/usr/bin/env python3
"""Make one 1080x1350 on-brand Kopi Kaki social image (offline, Pillow only).
Usage: python tools/make_post_image.py --headline "Slow-brewed. Shiok cold." --sub "Gula Melaka Cold Brew · from 1 Dec" --out outputs/social/images/instagram.png"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont
BROWN, GREEN, CREAM, AMBER = (91, 58, 41), (78, 138, 62), (246, 235, 217), (199, 120, 42)
def font(sz):
    for f in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf", "DejaVuSans-Bold.ttf"]:
        try: return ImageFont.truetype(f, sz)
        except Exception: pass
    return ImageFont.load_default()
def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur] if cur else lines
ap = argparse.ArgumentParser(); ap.add_argument("--headline", required=True); ap.add_argument("--sub", default="")
ap.add_argument("--out", required=True); ap.add_argument("--card", default="assets/cold-brew-product-card.png"); a = ap.parse_args()
im = Image.new("RGB", (1080, 1350), CREAM); d = ImageDraw.Draw(im)
d.rectangle((0, 0, 1080, 120), fill=BROWN); d.text((60, 38), "KOPI KAKI CO.", font=font(44), fill=CREAM)
if os.path.exists(a.card):
    card = Image.open(a.card).convert("RGB").resize((760, 760)); im.paste(card, (160, 150))
y = 940
for line in wrap(d, a.headline, font(72), 960): d.text((60, y), line, font=font(72), fill=BROWN); y += 84
for line in wrap(d, a.sub, font(40), 960): d.text((60, y + 10), line, font=font(40), fill=GREEN); y += 50
d.rectangle((0, 1290, 1080, 1350), fill=AMBER); d.text((60, 1300), "#ShiokColdBrew", font=font(36), fill=CREAM)
os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True); im.save(a.out); print("saved", a.out)
