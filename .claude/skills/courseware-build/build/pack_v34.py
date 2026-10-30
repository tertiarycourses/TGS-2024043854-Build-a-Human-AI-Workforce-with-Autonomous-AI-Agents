"""v3.4 lab data packs: team role files (souls/), task briefs (tasks/), skills and small tools, keyed by lab code.
Everything here is synthetic Kopi Kaki Co. training material."""
from pathlib import Path
import shutil
import pack_2026

RULES = ("Rules: read AGENTS.md, campaign-brief.md, brand-guide.md and compliance-rules.md first. Use only facts you can point to in a "
         "source file (price SGD 6.80, launch 1 Dec 2026, flagship in Tiong Bahru, SHIOK20 terms only if the code is used). No health, "
         "halal or competitor claims. Never post, send or publish anything. Write only the files your task names.")

SOULS = {
 # Activity 4 · social media marketing team
 "researcher": "You are the Kopi Kaki marketing researcher. Find launch angles, audience insights and proof points for the Gula Melaka Cold Brew launch. "
               "Cite the source file for every fact; mark anything you cannot source as UNVERIFIED. " + RULES,
 "linkedin-writer": "You write the founder's LinkedIn posts for Kopi Kaki Co.: a short founder story, one proof point, a clear call to action. "
                    "Professional Singapore English, 120-180 words, at most 3 hashtags. " + RULES,
 "facebook-writer": "You write Kopi Kaki's neighbourhood Facebook posts: friendly kopitiam voice, pop-up dates and the 1 Dec flagship opening first, 60-100 words. " + RULES,
 "instagram-writer": "You write Kopi Kaki's Instagram captions: a first line that stops the scroll, 40-80 words, 5-8 hashtags including #ShiokColdBrew, and a one-line image brief. " + RULES,
 "image-creator": "You create one 1080x1350 on-brand image per post with tools/make_post_image.py (brand colours, product card, short headline) and build "
                  "outputs/social/gallery.html showing every post as it would appear on its platform. No people, no stock photos, no logos except Kopi Kaki. " + RULES,
 # Activity 5 · video production team
 "video-researcher": "You are the video researcher. Extract the facts the launch video may use into outputs/video/research.md as a table: claim | source file | exact quote. "
                     "Propose one hook. Anything without a source is UNVERIFIED and must not be used. " + RULES,
 "scriptwriter": "You turn research.md into outputs/video/script.md: a 20-second, 4-scene vertical video. Per scene: duration, on-screen text (max 7 words), narration line, visual. "
                 "Then stop and wait for the founder's approval. " + RULES,
 "voice-over": "You write outputs/video/narration.txt from the APPROVED script only and record outputs/video/narration.wav with "
               "`npx hyperframes tts outputs/video/narration.txt --voice af_heart --output outputs/video/narration.wav`. Check the length fits 20 seconds. " + RULES,
 "video-producer": "You render the APPROVED script with HyperFrames into outputs/video/final.mp4: 1080x1920, about 20 seconds, Kopi Kaki colours from DESIGN.md, narration.wav as the audio track. "
                   "Run `npx hyperframes check` before rendering and ffprobe after. The MP4 is the output, not a success message. " + RULES,
 "video-reviewer": "You are independent of the producer. Watch every scene of final.mp4, check it against video-qa-checklist.md (V1-V9) and research.md, and write outputs/video/review.md "
                   "with PASS/FAIL and evidence per check plus the file's SHA-256. Then send the founder the review link http://localhost:8765/final.mp4 and your verdict. "
                   "Send failures back to the producer. You never approve on the founder's behalf. " + RULES,
}
TASKS = {
 "s1-research.md": "# Research launch angles\nRead the brief, the 60 pop-up tasting reviews (customer-reviews.csv) and competitors.csv. Write outputs/social/research.md: "
                   "3 launch angles, the top 3 things tasters loved (with review IDs), 5 approved facts with their source file, and one angle per platform (LinkedIn, Facebook, Instagram).",
 "s2-linkedin.md": "# LinkedIn post\nUsing research.md, write outputs/social/linkedin.md: the founder's story of starting Kopi Kaki, one proof point from the tasting reviews, the 1 Dec opening, a call to action. 120-180 words.",
 "s3-facebook.md": "# Facebook post\nUsing research.md, write outputs/social/facebook.md for neighbours near Tiong Bahru: pop-up dates, the 1 Dec flagship opening, SGD 6.80, app pre-order. 60-100 words.",
 "s4-instagram.md": "# Instagram post\nUsing research.md, write outputs/social/instagram.md: hook line, caption (40-80 words), 5-8 hashtags incl. #ShiokColdBrew, and a one-line image brief.",
 "s5-images.md": "# Images and review gallery\nFor each of linkedin.md, facebook.md and instagram.md make one image with\n"
                 "`.office-venv/bin/python tools/make_post_image.py --headline \"<max 6 words>\" --sub \"<max 10 words>\" --out outputs/social/images/<platform>.png`\n"
                 "(Windows: .office-venv\\Scripts\\python.exe). Then build outputs/social/gallery.html: one card per platform styled like that platform, with image, copy and hashtags. Offline, no external libraries.",
 "v1-research.md": "# Research the launch video\nExtract the facts the video may use into outputs/video/research.md (claim | source file | exact quote) from campaign-brief.md, product-catalogue.csv, brand-guide.md and the tasting reviews. Propose one hook.",
 "v2-script.md": "# Write the 20-second script\nFrom research.md write outputs/video/script.md: 4 scenes x 5 s; on-screen text max 7 words; narration line; visual. End card: Gula Melaka Cold Brew · SGD 6.80 · from 1 Dec 2026 · Tiong Bahru. Wait for the founder's approval.",
 "v3-voice.md": "# Record the voice-over\nFrom the APPROVED script write outputs/video/narration.txt and record outputs/video/narration.wav with hyperframes tts (voice af_heart). Report its duration.",
 "v4-produce.md": "# Render the video\nBuild a HyperFrames composition in outputs/video/project from the APPROVED script and DESIGN.md, add narration.wav, run `npx hyperframes check`, render "
                  "`npx hyperframes render --quality delivery --output outputs/video/final.mp4`, then save the ffprobe output to outputs/video/metadata.json.",
 "v5-review.md": "# Review and send the founder the link\nCheck final.mp4 against video-qa-checklist.md and research.md. Write outputs/video/review.md (PASS/FAIL + evidence per V1-V9, SHA-256). "
                 "Message the founder: the review link http://localhost:8765/final.mp4, the verdict and the hash. On FAIL, create a rework card for the video-producer instead.",
}
PPT_SKILL = ("kopi-pitch-deck", "Build a professional, editable investor/launch pitch deck for Kopi Kaki Co. from the source files with python-pptx.", """1. Read AGENTS.md, campaign-brief.md, brand-guide.md, product-catalogue.csv, competitors.csv and customer-reviews.csv.
2. Story (8-10 slides): title · the problem · the product (Gula Melaka Cold Brew, SGD 6.80) · proof from 60 tasting reviews (average rating, top themes with review IDs) · market and 6 competitors · launch plan (17 Nov-14 Dec, #ShiokColdBrew) · KPIs (2,500 pre-orders, 8% engagement, 40,000 views) · budget SGD 15,000 · the ask.
3. Design: 16:9, brand colours Kopi Brown #5B3A29, Pandan Green #4E8A3E, Cream #F6EBD9, Amber #C7782A; one idea per slide; headline that states the point; at most 5 short bullets; readable 18 pt+ body text.
4. Use a NATIVE editable chart (python-pptx chart, not an image) for the review ratings or KPI targets. Put the source file in the speaker notes of every slide with a number.
5. Never invent figures, awards, partners or a loan amount the founder did not give. Mark assumptions.
6. Save outputs/deck/kopi-kaki-pitch.pptx, render outputs/deck/kopi-kaki-pitch.pdf (soffice --headless --convert-to pdf), open every page and fix clipping or overlap.
7. Write outputs/deck/qa-report.md: each number → source file, each fix you made. Do not send or publish.""")

MAKE_IMAGE = r'''#!/usr/bin/env python3
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
'''

OPC_SETUP = """# Paperclip set-up sheet — Kopi Kaki Co. as a one-person company (OPC)

| Field | Value to enter |
|---|---|
| Organization name | Kopi Kaki Co. |
| Board | You — the founder and the only human |
| First agent | Ava — set role to CEO with the CLI |
| Adapter | Whichever agent CLI is signed in: Hermes (hermes_local), Claude Code, Codex or Gemini CLI |
| Hiring gate | Settings → General → Hiring → "Require board approval for new hires" = ON |
| Company budget | USD 60 / month → `budgetMonthlyCents: 6000` (training cap) |
| Mission | Launch the Gula Melaka Cold Brew on 1 Dec 2026: 2,500 app pre-orders, one approved short video every week, AI spend under USD 60/month, zero compliance breaches |

## Target org chart

| Role | Reports to | Hired by | Budget / month |
|---|---|---|---|
| CEO (Ava) | Board | Board | USD 15 |
| Chief of Staff | CEO | CEO, Board-approved | USD 10 |
| Market Researcher | Chief of Staff | Chief of Staff, Board-approved | USD 6 |
| Social Copywriter | Chief of Staff | Chief of Staff, Board-approved | USD 6 |
| Image Creator | Chief of Staff | Chief of Staff, Board-approved | USD 5 |
| Video Producer | Chief of Staff | Chief of Staff, Board-approved | USD 8 |
| Voice-over Artist | Chief of Staff | Chief of Staff, Board-approved | USD 4 |
| Content Reviewer | Chief of Staff (independent: can block release) | Chief of Staff, Board-approved | USD 4 |

Rule: nothing public without the Board; the reviewer never reviews its own work.
"""

WEBSITE_BRIEF = """# Website brief — Kopi Kaki Co. (one page)

- Audience: office workers 25-40 and students 18-24 who tasted us at a pop-up and search for us that evening.
- Sections: hero (Gula Melaka Cold Brew, SGD 6.80, from 1 Dec 2026) · our story (a startup founded in 2026) · menu (from product-catalogue.csv) ·
  pop-up dates and the Tiong Bahru flagship · what tasters say (3 short quotes from customer-reviews.csv, no names) · app pre-order button · footer.
- Brand: brand-guide.md colours and voice; assets/kopi-kaki-logo.png and assets/cold-brew-product-card.png.
- Constraints: one self-contained index.html (inline CSS, no external libraries or fonts), responsive to 375 px, accessible contrast, no health or halal claims.
- Definition of done: opens offline; every price and date matches the source files; works on a phone width; review.md lists checks and fixes.
"""

def assets(L, ddir):
    root = Path(ddir); root.mkdir(parents=True, exist_ok=True); files = []
    code = L["code"]
    def put(rel, text):
        p = root / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8"); files.append(rel)
    if code == "01":
        files += pack_2026.assets(dict(L, num=1), ddir)
    if code == "S2":
        name = "gog-office"; desc, steps = pack_2026.SKILLS[name]
        put(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: {desc}\n---\n# {name}\n\n{steps}\n")
        put("approved-test-send.md", pack_2026.TEST_SEND)
    if code == "02":
        put("website-brief.md", WEBSITE_BRIEF)
    if code == "03":
        name, desc, steps = PPT_SKILL
        put(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: {desc}\n---\n# {name}\n\n{steps}\n")
    if code == "04":
        for k in ("researcher", "linkedin-writer", "facebook-writer", "instagram-writer", "image-creator"):
            put(f"souls/{k}.SOUL.md", f"# {k} — SOUL.md\n\n{SOULS[k]}\n")
        for k in ("s1-research.md", "s2-linkedin.md", "s3-facebook.md", "s4-instagram.md", "s5-images.md"):
            put(f"tasks/{k}", TASKS[k] + "\n")
        put("tools/make_post_image.py", MAKE_IMAGE)
    if code == "05":
        for k in ("video-researcher", "scriptwriter", "voice-over", "video-producer", "video-reviewer"):
            put(f"souls/{k}.SOUL.md", f"# {k} — SOUL.md\n\n{SOULS[k]}\n")
        for k in ("v1-research.md", "v2-script.md", "v3-voice.md", "v4-produce.md", "v5-review.md"):
            put(f"tasks/{k}", TASKS[k] + "\n")
    if code == "B":
        put("paperclip-opc-setup.md", OPC_SETUP)
    return files
