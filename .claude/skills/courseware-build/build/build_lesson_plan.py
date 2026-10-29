#!/usr/bin/env python3
"""Generate the Lesson Plan (LP) DOCX from course_data.SCHEDULE + data_labs + the deck's slide_map.json.

House format: WSQ cover page, Document Version Control Record, TOC field, Arial 11pt,
colour-coded day tables (9:30am–6:30pm, 8 training hours/day, 1h lunch) with the slide
numbers of the CURRENT deck on every row (read from slide_map.json written by build_slides.py).
"""
import json, os, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.table import WD_TABLE_ALIGNMENT

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS
import prodoc
from version_history import PRIOR, V20, V21, V22, V23, V24

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE); ASSETS = os.path.join(os.path.dirname(HERE), "assets")
MAP = json.load(open(os.path.join(HERE, "slide_map.json")))

BRAND = RGBColor(0x1F, 0x6F, 0xEB); GREY = RGBColor(0x55, 0x5B, 0x66)
HEADER_FILL = "1F6FEB"; TOPIC_FILL = "E8F0FE"; BREAK_FILL = "FFF4E5"; LUNCH_FILL = "FDE9D9"; ASSESS_FILL = "E8F7EE"
KIND_FILL = {"topic": TOPIC_FILL, "activity": TOPIC_FILL, "break": BREAK_FILL, "lunch": LUNCH_FILL, "assess": ASSESS_FILL,
             "admin": "F3F5F8", "recap": "F3F5F8", "lab": None}

def rng(a, b): return str(MAP[a]) if MAP[b] - 1 == MAP[a] else f"{MAP[a]}–{MAP[b] - 1}"
def slides_for(day, text):
    t = text
    if t.startswith("Welcome"): return rng("admin", "t1a")
    if t.startswith("Topic 1 (Part A)"): return rng("t1a", "lab1")
    if t.startswith("Assistant results"): return rng("activity", "consolidation")
    if t.startswith("Under the hood"): return rng("consolidation", "t2")
    if t.startswith("Lab 2: Activity 2A"): return rng("t2", "lab2i")
    if t.startswith("Lab 2: Activity 2B"): return rng("lab2i", "lab3")
    if t.startswith("Source assurance introduction"): return str(MAP["lab6"])
    if t.startswith("Lab 6:"): return f"{MAP['lab6'] + 1}–{MAP['lab7'] - 1}"
    for L in LABS:
        if t.startswith(f"Lab {L['num']}:"):
            nxt = {1: "lab1end", 4: "t2close", 8: "t3sum"}.get(L["num"], f"lab{L['num'] + 1}")
            return rng(f"lab{L['num']}", nxt)
    if t.startswith("Day 1 recap, Q&A"): return rng("t2close", "day2")
    if t.startswith("Day 1 recap and AM"): return rng("t2sum", "lab5")
    if t.startswith("Course recap"): return rng("t3sum", "assess")
    if t.startswith("Briefing"): return str(MAP["briefing"])
    if t.startswith("Written") or t.startswith("Practical"): return rng("assess", "end")
    return "—"

doc = Document()
normal = doc.styles["Normal"]; normal.font.name = "Arial"; normal.font.size = Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "LESSON PLAN", C.TITLE, C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"), course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, PRIOR + [V20, V21, V22, V23, V24])
prodoc.add_toc(doc)
H = lambda t, l=1: doc.add_heading(t, level=l)

def set_cell(cell, text, bold=False, size=9.5, color=None, fill=None):
    cell.text = ""; p = cell.paragraphs[0]
    r = p.add_run(text); r.bold = bold; r.font.size = Pt(size); r.font.name = "Arial"
    if color: r.font.color.rgb = color
    if fill: prodoc._shade_cell(cell, fill)

H("Course Information")
info = [("Course Title", C.TITLE), ("WSQ Course Reference", C.COURSE_CODE),
        ("Training Provider", f"{C.ORG}  ({C.UEN.replace('UEN: ', 'UEN ')})"),
        ("Duration", C.CONTACT_TIME_NOTE),
        ("Daily Timing", "9:30 am – 6:30 pm (1-hour lunch; tea breaks within training time)"),
        ("Mode", "Instructor-led; always-on assistant setup followed by Hermes Desktop office and team practice (learner laptop)"),
        ("Course scenario", C.SCENARIO + " — all company data is fictional"),
        ("Slide deck", f"{C.SHORT_TITLE}-{C.VERSION}.pptx ({MAP['end'] - 1} slides)"),
        ("Trainer", C.TRAINER)]
t = doc.add_table(rows=0, cols=2); t.style = "Table Grid"
for k, v in info:
    c = t.add_row().cells; set_cell(c[0], k, bold=True, size=10, fill=TOPIC_FILL); set_cell(c[1], v, size=10)
prodoc.set_widths(t, [1.8, 5.0])

H("Learning Outcomes")
doc.add_paragraph("On completion of this course, learners will be able to:")
for lo in C.LEARNING_OUTCOMES:
    doc.add_paragraph(style="List Bullet").add_run(lo).font.size = Pt(11)

H("Topics and Labs")
tt = doc.add_table(rows=0, cols=3); tt.style = "Table Grid"
hdr = tt.add_row().cells
for i, h in enumerate(["Topic", "Content / labs", "Slides"]):
    set_cell(hdr[i], h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
topic_slides = {1: rng("t1a", "t2"), 2: rng("t2", "t3"), 3: rng("t3", "wrap")}
for tp in C.TOPICS:
    c = tt.add_row().cells
    set_cell(c[0], f"Topic {tp['num']}: {tp['title']}", bold=True, fill=TOPIC_FILL)
    set_cell(c[1], "; ".join(tp["items"]) + (".  Activity 1: always-on assistant setup." if tp["num"] == 1 else "."))
    set_cell(c[2], topic_slides[tp["num"]])
prodoc.set_widths(tt, [2.3, 3.6, 0.9])

H("Learning Units (approved Course Proposal TPG-2024060313)")
lut = doc.add_table(rows=0, cols=5); lut.style = "Table Grid"
hdr = lut.add_row().cells
for i, h in enumerate(["LU", "Learning unit", "Delivered through", "K & A", "Duration"]):
    set_cell(hdr[i], h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
for u in C.LUS:
    mins = sum(r[2] for d in C.SCHEDULE for r in C.SCHEDULE[d] if r[5] == u["lu"] and r[3] != "lunch")
    assert mins == u["hours"] * 60, (u["lu"], mins)
    c = lut.add_row().cells
    set_cell(c[0], u["lu"], bold=True, fill=TOPIC_FILL); set_cell(c[1], u["title"]); set_cell(c[2], u["covers"])
    set_cell(c[3], ", ".join(u["codes"])); set_cell(c[4], f"{u['hours']} h")
c = lut.add_row().cells
set_cell(c[0], "Assessment", bold=True, fill=ASSESS_FILL); set_cell(c[1], "WA-SAQ (1 h) + PP (1 h)"); set_cell(c[2], "Day 2, 4:30–6:30 pm")
set_cell(c[3], "K1–K6, A1–A6"); set_cell(c[4], "2 h")
prodoc.set_widths(lut, [0.75, 1.9, 2.4, 1.05, 0.7])
p = doc.add_paragraph(); r = p.add_run("Scheduled LU allocations: 5 h + 5 h + 4 h, plus 2 h assessment; these include tea. Net instruction/practice is 13 h. Retained 9:30–18:30 timing was confirmed by the trainer."); r.italic = True; r.font.size = Pt(9.5)

# Avoid an isolated table heading/header at the bottom of a page.
for row in lut.rows[:2]:
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            paragraph.paragraph_format.keep_with_next = True
H("Assessment")
for a in [C.ASSESSMENT["written"], C.ASSESSMENT["practical"],
          "Format: Open Book — course slides, Learner Guide and approved materials only.",
          "Final assessment is conducted on Day 2 from 4:30 pm.", C.ASSESSMENT["note"]]:
    doc.add_paragraph(style="List Bullet").add_run(a).font.size = Pt(11)

H("Course Schedule")
for day in (1, 2):
    H(f"Day {day} — {C.DAY_THEMES[day]}", 2)
    tbl = doc.add_table(rows=0, cols=5); tbl.style = "Table Grid"; tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.add_row().cells
    for i, h in enumerate(["Time", "Duration", "Topic / Activity", "LU", "Slides"]):
        set_cell(hdr[i], h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    training = 0
    for start, end, mins, kind, text, lu in C.SCHEDULE[day]:
        cells = tbl.add_row().cells; fill = KIND_FILL.get(kind); bold = kind in ("topic", "assess", "activity")
        set_cell(cells[0], f"{start}–{end}", bold=bold, fill=fill); set_cell(cells[1], f"{mins} min", fill=fill)
        set_cell(cells[2], text, bold=bold, fill=fill)
        set_cell(cells[3], "Assessment" if lu == "ASSESS" else (lu or "—"), fill=fill)
        set_cell(cells[4], "—" if kind in ("break", "lunch") else slides_for(day, text), fill=fill)
        if kind != "lunch": training += mins
    prodoc.set_widths(tbl, [1.05, 0.75, 3.75, 0.6, 0.7])
    p = doc.add_paragraph(); r = p.add_run(f"Scheduled time excluding lunch: {training} minutes ({training // 60} hours), including tea and any assessment."); r.italic = True
    r.font.size = Pt(9.5); r.font.color.rgb = GREY
    assert training == 480, f"Day {day} training minutes = {training}, expected 480"

H("Lab Reference")
lt = doc.add_table(rows=0, cols=5); lt.style = "Table Grid"
hdr = lt.add_row().cells
for i, h in enumerate(["Lab", "Title", "Paradigm", "LO", "Slides"]):
    set_cell(hdr[i], h, bold=True, size=10, color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
for L in LABS:
    c = lt.add_row().cells
    nxt = {1: "lab1end", 4: "t2close", 8: "t3sum"}.get(L["num"], f"lab{L['num'] + 1}")
    set_cell(c[0], f"Lab {L['num']} (Day {L['day']})", bold=True); set_cell(c[1], L["title"])
    set_cell(c[2], L["paradigm"]); set_cell(c[3], L["lo"]); set_cell(c[4], rng(f"lab{L['num']}", nxt))
prodoc.set_widths(lt, [0.9, 3.4, 1.5, 0.5, 0.7])
doc.add_paragraph("Lab materials: labs/labNN-*/ (README, LAB-NN-Instructions.pdf, COPY-PROMPTS.txt, data/) and the "
                  "Lab Prompts page prompts/index.html in the course repository.").runs[0].font.size = Pt(10)

prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
OUT = os.path.join(REPO, "courseware", f"LP-{C.SHORT_TITLE}.docx")
doc.save(OUT); print("Saved", OUT)
