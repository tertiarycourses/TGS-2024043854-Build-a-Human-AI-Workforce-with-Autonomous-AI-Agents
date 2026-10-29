#!/usr/bin/env python3
"""Generate the labs/ folder, the lab PDFs and the local Lab Prompts page from data_labs.py.

For every lab  -> labs/labNN-slug/README.md, COPY-PROMPTS.txt, LAB-NN-Instructions.pdf, data/
Index          -> labs/README.md
Prompts page   -> prompts/index.html  (self-contained; works offline from file://)

PDFs are printed from generated HTML with headless Google Chrome.
"""
import html, os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
import mock_data as M
from data_labs import LABS, SOULS, TASKS, DESIGN_MD
import pack_2026

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    raise SystemExit("course repo not found")
REPO = _find_repo(HERE)
LABS_DIR = os.path.join(REPO, "labs")
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
FOOT = f"Part of the WSQ course <b>{C.TITLE}</b> ({C.COURSE_CODE}) · © 2026 {C.ORG} · www.tertiarycourses.com.sg"
SYNTH = "All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training."

# ------------------------------------------------------------------ brand images
def brand_images(dst):
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs(dst, exist_ok=True)
    def font(sz, bold=True):
        for f in ["/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                  "/Library/Fonts/Arial Bold.ttf", "DejaVuSans-Bold.ttf"]:
            try: return ImageFont.truetype(f, sz)
            except Exception: pass
        return ImageFont.load_default()
    BROWN, GREEN, CREAM, AMBER = (91, 58, 41), (78, 138, 62), (246, 235, 217), (199, 120, 42)
    # logo
    im = Image.new("RGBA", (800, 800), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((20, 20, 780, 780), fill=BROWN)
    d.rounded_rectangle((250, 300, 520, 560), 40, fill=CREAM)            # cup
    d.arc((480, 350, 600, 480), -90, 90, fill=CREAM, width=26)           # handle
    d.rectangle((230, 560, 540, 590), fill=CREAM)                        # saucer
    for x in (310, 385, 460):
        d.arc((x - 25, 190, x + 25, 290), 100, 260, fill=AMBER, width=14)  # steam
    f = font(70); t = "KOPI KAKI"; w = d.textlength(t, font=f); d.text(((800 - w) / 2, 625), t, font=f, fill=CREAM)
    im.save(os.path.join(dst, "kopi-kaki-logo.png"))
    # palette
    im = Image.new("RGB", (1200, 360), CREAM); d = ImageDraw.Draw(im)
    for i, (c, n, h) in enumerate([(BROWN, "Kopi Brown", "#5B3A29"), (GREEN, "Pandan Green", "#4E8A3E"),
                                   ((246, 235, 217), "Condensed-Milk Cream", "#F6EBD9"), (AMBER, "Gula Melaka Amber", "#C7782A")]):
        x = 30 + i * 292; d.rounded_rectangle((x, 30, x + 270, 230), 24, fill=c, outline=(91, 58, 41), width=3)
        d.text((x, 250), n, font=font(26), fill=BROWN); d.text((x, 292), h, font=font(26, False), fill=BROWN)
    im.save(os.path.join(dst, "brand-palette.png"))
    # product card (placeholder visual — no people, no claims)
    im = Image.new("RGB", (1080, 1080), CREAM); d = ImageDraw.Draw(im)
    for r in range(0, 1080, 90):
        for c in range(0, 1080, 90):
            if (r // 90 + c // 90) % 2 == 0: d.rectangle((c, r + 760, c + 90, r + 850), fill=(232, 240, 230))
    d.polygon([(390, 260), (690, 260), (650, 760), (430, 760)], fill=(255, 255, 255), outline=BROWN)
    d.polygon([(400, 330), (680, 330), (648, 740), (432, 740)], fill=(120, 72, 40))
    d.polygon([(405, 330), (675, 330), (670, 400), (410, 400)], fill=(236, 222, 200))
    for y in (450, 520, 590): d.line((440, y, 640, y + 30), fill=AMBER, width=10)
    d.text((80, 840), "Gula Melaka Cold Brew", font=font(60), fill=BROWN)
    d.text((80, 920), "SGD 6.80 · from 1 Dec 2026 · #ShiokColdBrew", font=font(36, False), fill=BROWN)
    im.save(os.path.join(dst, "cold-brew-product-card.png"))

# ------------------------------------------------------------------ data packs
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.basename(path) == "AGENTS.md" and os.path.exists(path): return
    with open(path, "w", encoding="utf-8") as f: f.write(content)

def data_pack(L, ddir, assets_src):
    files = []
    for key in L["data"]:
        rel, fn = M.FILES[key]; write(os.path.join(ddir, rel), fn()); files.append(rel)
    if L["num"] in (5,8):
        write(os.path.join(ddir, "DESIGN.md"), DESIGN_MD); files.append("DESIGN.md")
        for k, v in SOULS.items():
            write(os.path.join(ddir, "souls", f"{k}.SOUL.md"), f"# {k} — SOUL.md\n\n{v}\n"); files.append(f"souls/{k}.SOUL.md")
        for k in ("t1-research.md", "t2-script.md", "t3-produce.md", "t4-audit.md", "t5-package.md", "t6-post.md"):
            write(os.path.join(ddir, "tasks", k), TASKS[k] + "\n"); files.append(f"tasks/{k}")
    if L["num"] != 1:
        shutil.copytree(assets_src, os.path.join(ddir, "assets"), dirs_exist_ok=True)
        files += [f"assets/{f}" for f in sorted(os.listdir(assets_src))]
    files += pack_2026.assets(L, ddir)
    return files

DESCR = {
 "AGENTS.md": "Company context Hermes loads automatically", "brand-guide.md": "Brand voice, colours, platform formats",
 "campaign-brief.md": "Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline)", "compliance-rules.md": "C1–C10 brand-safety and escalation rules",
 "product-catalogue.csv": "12 products and prices", "competitors.csv": "6 fictional competitors", "customer-reviews.csv": "60 synthetic customer reviews",
 "social-comments.csv": "20 social comments incl. complaints, legal, PII, spam", "campaign-week1-metrics.csv": "Week-1 post metrics (12 posts)",
 "sales-by-outlet.csv": "Weekly sales for 12 outlets", "video-qa-checklist.md": "V1–V9 video QA checks", "DESIGN.md": "Visual identity for HyperFrames",
 "paperclip-company-setup.md": "Values for the Paperclip company set-up", "paperclip-org-plan.md": "Reference hiring plan",
 "paperclip-backlog.csv": "7 launch issues with dependencies", "paperclip-routine-weekly-kopi-short.md": "Routine spec", "agent-scorecard.csv": "Month-1 agent scorecard (mock)",
}
def describe(rel):
    b = os.path.basename(rel)
    if rel.startswith("skills/"): return "Agent skill (SKILL.md)"
    if rel.startswith("souls/"): return "Role + rules for one studio profile"
    if rel.startswith("tasks/"): return "Task contract; use current Kanban tools or --body text"
    if rel.startswith("templates/"): return "Template"
    if rel.startswith("assets/"): return "Brand image asset"
    return DESCR.get(b, "")

# ------------------------------------------------------------------ README.md
def readme(L, files):
    o = [f"# Lab {L['num']} — {L['title']}", "",
         f"**Day {L['day']} · Topic {L['topic']} · {L['minutes']} min · {L['paradigm']} · {L['lo']}**", "",
         f"> {L['hook']}", "", "## Goal", L["objective"], "", "## The business scenario", L["scenario"], "",
         "## You will deliver"] + [f"- {d}" for d in L["deliverables"]] + ["",
         "## Who does what", f"- **Agents:** {L['agents']}", f"- **You (the human):** {L['human']}", "",
         "## Before you start"] + [f"- {x}" for x in L.get("prereq", [])] + ["",
         "## Concepts in action"] + [f"- {c}" for c in L["concepts"]] + ["",
         "## Lab files (`data/`)", "", "| File | What it is |", "|---|---|"] + \
        [f"| `{f}` | {describe(f)} |" for f in files] + ["", f"_{SYNTH}_", "",
         "Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). "
         f"Printable instructions: [`LAB-{L['num']:02d}-Instructions.pdf`](LAB-{L['num']:02d}-Instructions.pdf).", "", "## Steps", ""]
    for i, st in enumerate(L["steps"], 1):
        o.append(f"### {i}. {st['title']}")
        if st.get("body"): o += [st["body"], ""]
        if st.get("cmd"): o += ["```bash", st["cmd"], "```", ""]
        if st.get("prompt"):
            o += [f"**Prompt** — paste into *{st.get('where', 'Hermes chat')}*:", "", "```text", st["prompt"], "```", ""]
        if st.get("expect"): o += [f"✅ **Expected:** {st['expect']}", ""]
    o += ["## Verification / checkpoint"] + [f"- [ ] {v}" for v in L["verify"]] + ["", f"**Checkpoint:** {L['check']}", "",
          "## Troubleshooting", "", "| Symptom | Fix |", "|---|---|"] + [f"| {a} | {b} |" for a, b in L["trouble"]] + ["",
          "## Stretch challenge", L["challenge"], "", f"<sub>{FOOT.replace('<b>', '**').replace('</b>', '**')}</sub>", ""]
    return "\n".join(o)

def copy_prompts(L):
    o = [f"LAB {L['num']} — {L['title']}", f"{C.TITLE} ({C.COURSE_CODE})", "=" * 72, ""]
    n = 0
    for st in L["steps"]:
        if st.get("prompt") or st.get("cmd"):
            if st.get("cmd"):
                n += 1; o += [f"[{n}] TERMINAL — {st['title']}", "-" * 72, st["cmd"], ""]
            if st.get("prompt"):
                n += 1; o += [f"[{n}] PROMPT — {st['title']}  (paste into: {st.get('where', 'Hermes chat')})", "-" * 72, st["prompt"], ""]
    return "\n".join(o)

# ------------------------------------------------------------------ HTML (shared by PDF + prompts page)
CSS = """
:root{--bg:#FAF9F5;--panel:#fff;--ink:#21201C;--muted:#6B6862;--acc:#D97757;--accd:#C2603F;--rule:#E3DFD6;--code:#2B2924;--codefg:#F1EDE4;--teal:#3A7D7B}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#21201C;--panel:#2E2C26;--ink:#F1EDE4;--muted:#C9C4B9;--rule:#45423B}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Calibri,Carlito,-apple-system,"Segoe UI",sans-serif}
h1,h2,h3{font-family:Cambria,Caladea,Georgia,serif;line-height:1.2}h1{font-size:30px;margin:6px 0 10px}h2{font-size:22px;margin:26px 0 10px}h3{font-size:17px;margin:20px 0 6px}
.k{color:var(--acc);font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin:0}
.meta{color:var(--muted)}.hook{border-left:4px solid var(--acc);padding:8px 14px;background:var(--panel);border-radius:8px}
.card{background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:14px 18px;margin:12px 0}
.dark{background:#21201C;color:#E8E5DE;border:0}.dark h3{color:#fff}
pre{background:var(--code);color:var(--codefg);padding:12px 14px;border-radius:10px;white-space:pre-wrap;overflow-wrap:anywhere;font:13.5px/1.5 ui-monospace,Menlo,Consolas,monospace;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0}th{background:#21201C;color:#fff;text-align:left}th,td{border:1px solid var(--rule);padding:6px 8px;vertical-align:top}
.exp{color:var(--teal);font-weight:600}.foot{color:var(--muted);font-size:12px;border-top:1px solid var(--rule);margin-top:30px;padding-top:10px}
a{color:var(--accd)}
"""
PRINT_CSS = """@page{size:A4;margin:16mm 15mm 18mm}body{background:#fff;font-size:12.5px}.wrap{max-width:none}pre{font-size:11px;break-inside:avoid}
h2{break-after:avoid}.step{break-inside:avoid}.cover{background:#21201C;color:#fff;padding:22px 26px;border-radius:14px;margin-bottom:14px}
.cover h1{color:#fff}.cover .meta{color:#C9C4B9}"""

def e(t): return html.escape(str(t))

def lab_html(L, files):
    p = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Lab {L['num']} — {e(L['title'])}</title>",
         f"<style>{CSS}{PRINT_CSS}</style></head><body><div class='wrap'>",
         f"<div class='cover'><p class='k'>{C.COURSE_CODE} · Day {L['day']} · Lab {L['num']} · {L['minutes']} min</p>",
         f"<h1>{e(L['title'])}</h1><p class='meta'>{e(C.TITLE)} · {e(L['paradigm'])} · {L['lo']}</p></div>",
         f"<p class='hook'>{e(L['hook'])}</p>",
         f"<h2>The business scenario</h2><p>{e(L['scenario'])}</p>",
         "<h2>You will deliver</h2><ul>" + "".join(f"<li>{e(d)}</li>" for d in L["deliverables"]) + "</ul>",
         f"<div class='card'><b>Agents:</b> {e(L['agents'])}<br><b>You (the human):</b> {e(L['human'])}<br><b>Goal:</b> {e(L['objective'])}</div>",
         "<h2>Before you start</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in L.get("prereq", [])) + "</ul>",
         "<h2>Lab files (data/)</h2><table><tr><th>File</th><th>What it is</th></tr>" +
         "".join(f"<tr><td><code>{e(f)}</code></td><td>{e(describe(f))}</td></tr>" for f in files) + "</table>",
         f"<p class='meta'><i>{e(SYNTH)}</i></p><h2>Steps</h2>"]
    for i, st in enumerate(L["steps"], 1):
        p.append(f"<div class='step'><h3>{i}. {e(st['title'])}</h3>")
        if st.get("body"): p.append(f"<p>{e(st['body'])}</p>")
        if st.get("cmd"): p.append(f"<p class='k'>Terminal</p><pre>{e(st['cmd'])}</pre>")
        if st.get("prompt"): p.append(f"<p class='k'>Prompt — paste into {e(st.get('where', 'Hermes chat'))}</p><pre>{e(st['prompt'])}</pre>")
        if st.get("expect"): p.append(f"<p class='exp'>✓ Expected: {e(st['expect'])}</p>")
        p.append("</div>")
    p += ["<h2>Verification / checkpoint</h2><ul>" + "".join(f"<li>☐ {e(v)}</li>" for v in L["verify"]) + "</ul>",
          f"<div class='card dark'><b>Checkpoint:</b> {e(L['check'])}</div>",
          "<h2>Troubleshooting</h2><table><tr><th>Symptom</th><th>Fix</th></tr>" +
          "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in L["trouble"]) + "</table>",
          f"<h2>Stretch challenge</h2><p>{e(L['challenge'])}</p><p class='foot'>{FOOT}</p></div></body></html>"]
    return "".join(p)

def to_pdf(html_text, out_pdf):
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "page.html"); open(src, "w", encoding="utf-8").write(html_text)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={out_pdf}", "file://" + src], check=True, capture_output=True)

# ------------------------------------------------------------------ prompts page
def prompts_page():
    nav = "".join(f"<a href='#lab-{L['num']}'>Lab {L['num']}</a>" for L in LABS)
    picks = ""
    for day, name in ((1, "Day 1 · Always-on assistant, then Hermes office automation"), (2, "Day 2 · Multi-agent video studio — Hermes bots, Kanban and Dots")):
        picks += f"<h3>{e(name)}</h3><ul>" + "".join(
            f"<li><a href='#lab-{L['num']}'>Lab {L['num']} · {e(L['title'])}</a> <span class='meta'>· {L['minutes']} min</span></li>"
            for L in LABS if L["day"] == day) + "</ul>"
    secs = []
    for L in LABS:
        rel = f"../labs/{L['slug']}"
        blocks = []
        n = 0
        for step_number, st in enumerate(L["steps"], 1):
            blocks.append(f"<h3>{step_number}. {e(st['title'])}</h3>")
            if st.get("body"): blocks.append(f"<p class='step-explanation'>{e(st['body'])}</p>")
            for kind in ("cmd", "prompt"):
                if not st.get(kind): continue
                n += 1; label = "Terminal" if kind == "cmd" else "Prompt"
                where = "your terminal" if kind == "cmd" else st.get("where", "Hermes chat")
                blocks.append(f"<div class='prompt'><header><div><b>{n}. {e(st['title'])}</b><span class='ptool'>{label} · paste into {e(where)}</span></div>"
                              f"<button class='copy' type='button'>Copy</button></header><pre>{e(st[kind])}</pre>"
                              + (f"<p class='exp'>✓ {e(st['expect'])}</p>" if st.get("expect") and kind == ("prompt" if st.get("prompt") else "cmd") else "") + "</div>")
        secs.append(f"<section class='lab' id='lab-{L['num']}'><p class='k'>Lab {L['num']} · Day {L['day']} · Topic {L['topic']} · {L['minutes']} min · {e(L['paradigm'])}</p>"
                    f"<h2>{e(L['title'])}</h2><p class='hook'>{e(L['hook'])}</p>"
                    f"<p class='files'><a href='{rel}/LAB-{L['num']:02d}-Instructions.pdf'>Instructions PDF</a> · <a href='{rel}/README.md'>README</a> · "
                    f"<a href='{rel}/COPY-PROMPTS.txt'>All prompts (.txt)</a> · <a href='{rel}/data/'>Data folder</a></p>"
                    f"<details><summary>Scenario & deliverables</summary><p>{e(L['scenario'])}</p><ul>" +
                    "".join(f"<li>{e(d)}</li>" for d in L["deliverables"]) + f"</ul><p><b>You:</b> {e(L['human'])}</p></details>" +
                    "".join(blocks) + f"<p class='check'><b>Checkpoint:</b> {e(L['check'])}</p><p><a href='#top'>↑ Back to labs</a></p></section>")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lab Prompts | {e(C.TITLE)}</title><style>{CSS}
.wrap{{max-width:900px;margin:auto;padding:24px 16px 70px}}nav{{position:sticky;top:0;z-index:2;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--rule);display:flex;gap:6px;flex-wrap:wrap}}
nav a{{padding:7px 12px;border:1.5px solid var(--rule);border-radius:22px;text-decoration:none;font-weight:600;color:var(--ink)}}nav a:hover{{border-color:var(--acc)}}
.pick{{margin:22px 0;padding:16px 20px;border:2px dashed var(--acc);border-radius:12px}}.lab{{padding-top:26px}}.files{{font-size:15px}}
details{{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:10px 14px;margin:12px 0}}summary{{cursor:pointer;font-weight:600}}
.prompt{{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--acc);border-radius:10px;margin:0 0 14px;overflow:hidden}}
.prompt header{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 14px}}.ptool{{display:block;font-size:13px;color:var(--muted)}}
.prompt pre{{margin:0 14px 12px}}.prompt .exp{{margin:0 14px 12px;font-size:14px}}
.copy{{font:inherit;font-weight:700;padding:8px 18px;min-height:40px;border:0;border-radius:8px;background:var(--acc);color:#fff;cursor:pointer;flex:none}}.copy.done{{background:#3A7D7B}}
.check{{background:#21201C;color:#E8E5DE;padding:10px 14px;border-radius:10px}}
#status{{position:fixed;bottom:16px;right:16px;background:#21201C;color:#fff;padding:8px 14px;border-radius:8px;opacity:0;transition:opacity .2s}}#status.on{{opacity:1}}
@media(max-width:600px){{nav{{flex-wrap:nowrap;overflow:auto}}nav a{{flex:none}}h1{{font-size:26px}}pre{{font-size:12.5px}}}}
</style></head><body><main class="wrap" id="top">
<p class="k">{C.COURSE_CODE} · {e(C.SHORT_TITLE)} · {C.VERSION}</p><h1>Lab Steps & Copyable Prompts</h1>
<p class="meta">{e(C.TITLE)} — two days, eight activities. Start with a personal-assistant exercise; begin the fictional company scenario after lunch. Pick your lab, click <b>Copy</b>, paste into the named place, and verify every result.
This page works offline: open <code>prompts/index.html</code> from the downloaded course folder.</p>
<div class="pick"><b>One connected project: the Kopi Kaki launch</b><p>Day 1: always-on assistant → Hermes Desktop and skills → Google/Excel → dashboard/PPT and single-agent video.<br>Day 2: Kanban specialists → video production → independent audit → human decision.</p><p><a href="https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/redeem-ai-subscription.html">Official SWDA free AI subscription steps</a> · <a href="resources.html">Sources and further reading</a> · <a href="{C.REPO_URL}/archive/refs/heads/main.zip">Download course ZIP</a></p></div>
<nav aria-label="Labs">{nav}</nav>
<div class="pick"><b>Before Lab 1:</b> set up one accessible always-on assistant with the assigned training Google account. After lunch, Activity 2 introduces the company workspace <code>~/kopi-kaki</code> and copy each lab's <code>data/</code> folder into it as you go. Outputs go to <code>~/kopi-kaki/outputs/labNN/</code>.{picks}</div>
{''.join(secs)}
<p class="foot">{FOOT}<br>{e(SYNTH)}<br>Powered by <a href="https://www.tertiaryinfotech.com/">Tertiary Infotech Academy Pte Ltd</a></p></main><div id="status" role="status" aria-live="polite"></div>
<script>
function flash(m){{var s=document.getElementById('status');s.textContent=m;s.classList.add('on');setTimeout(function(){{s.classList.remove('on')}},1400)}}
function fallback(t){{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();var ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}a.remove();return ok}}
document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{
  var t=b.closest('.prompt').querySelector('pre').innerText;
  var done=function(){{b.textContent='Copied';b.classList.add('done');flash('Copied to clipboard');setTimeout(function(){{b.textContent='Copy';b.classList.remove('done')}},1500)}};
  if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(t).then(done,function(){{if(fallback(t)){{done()}}else{{flash('Copy unavailable: select the text and copy manually')}}}})}}else{{if(fallback(t)){{done()}}else{{flash('Copy unavailable: select the text and copy manually')}}}}
}})}});
</script></body></html>"""
    return page

def labs_index():
    o = [f"# Labs — {C.TITLE}", "",
         f"Eight activities: morning personal-assistant practice, then the **{C.SCENARIO}** company scenario from Activity 2. The Day 1 office pack is saved under `outputs/lab02/`; the video team uses `outputs/team/`; follow each named artifact path.", "",
         "**Copy-ready prompts:** open [`../prompts/index.html`](../prompts/index.html) in your browser (works offline) — pick a lab, click **Copy**.", "",
         "Each lab folder contains `README.md`, `LAB-NN-Instructions.pdf` (printable), `COPY-PROMPTS.txt` and `data/` (mock company files, skills and brand assets).", ""]
    for day, name in ((1, "Day 1 — Always-on assistant, then Hermes office tools and skills"), (2, "Day 2 — Hermes bots, Kanban video, source assurance and Dots")):
        o += [f"## {name}", "", "| # | Lab | Paradigm | Time | Instructions |", "|---|---|---|---|---|"]
        for L in LABS:
            if L["day"] == day:
                o.append(f"| {L['num']} | [{L['title']}]({L['slug']}/README.md) | {L['paradigm']} | {L['minutes']} min | [PDF]({L['slug']}/LAB-{L['num']:02d}-Instructions.pdf) |")
        o.append("")
    o += ["## Topic 1 activity", "Activity 1: set up one accessible Muse, Dots or Grok Bot; check schedule and draft a reply. Activity 2 begins the company scenario and Hermes Desktop after lunch.", "",
          "## Conventions", "- Prompts are plain English; terminal commands are marked `bash`.",
          "- Hermes: start `hermes` inside `~/kopi-kaki` so `AGENTS.md` is loaded. OpenAI Dots: https://chatgpt.com/dots (verify entitlement).",
          "- Nothing public is ever published without a human APPROVE / Board approval.",
          "- Platforms move fast — if a command differs on your version, check `--help` and the official docs "
          "([Hermes](https://hermes-agent.nousresearch.com/docs/) · [OpenAI Dots](https://learn.chatgpt.com/docs/dots/getting-started)).", "",
          f"<sub>{FOOT.replace('<b>', '**').replace('</b>', '**')}</sub>", ""]
    return "\n".join(o)

def main():
    tmp_assets = os.path.join(HERE, "brand_assets"); brand_images(tmp_assets)   # cached, overwritten each build
    for L in LABS:
        ld = os.path.join(LABS_DIR, L["slug"])
        os.makedirs(ld, exist_ok=True)
        files = data_pack(L, os.path.join(ld, "data"), tmp_assets)
        data_links = "".join(f"<li><a href=\"{e(f)}\">{e(f)}</a> — {e(describe(f))}</li>" for f in files)
        write(os.path.join(ld,"data","index.html"),f"<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Lab {L['num']} data files</title><body style=\"font:18px system-ui;max-width:900px;margin:40px auto;padding:20px\"><h1>Lab {L['num']}: Data and tools</h1><p>Download the course ZIP for the full folder structure. These files contain synthetic training data only.</p><ul>{data_links}</ul><a href=\"../../../prompts/index.html#lab-{L['num']}\">Back to lab steps</a></body></html>")
        write(os.path.join(ld, "README.md"), readme(L, files))
        write(os.path.join(ld, "COPY-PROMPTS.txt"), copy_prompts(L))
        to_pdf(lab_html(L, files), os.path.join(ld, f"LAB-{L['num']:02d}-Instructions.pdf"))
        print("lab", L["num"], "->", L["slug"], f"({len(files)} data files)")
    write(os.path.join(LABS_DIR, "README.md"), labs_index())
    write(os.path.join(REPO, "prompts", "index.html"), prompts_page())
    shutil.copy(os.path.join(tmp_assets, "kopi-kaki-logo.png"), os.path.join(REPO, "courseware", "assets", "logos", "kopi-kaki.png"))
    print("labs/README.md + prompts/index.html written")

if __name__ == "__main__":
    main()
