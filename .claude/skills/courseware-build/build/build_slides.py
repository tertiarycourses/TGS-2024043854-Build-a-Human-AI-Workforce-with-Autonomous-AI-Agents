#!/usr/bin/env python3
"""Generate the v2 slide deck for "Build a Human-AI Workforce with Autonomous AI Agents"
in the house design of "Agentic AI Applications with Claude Code" (TGS-2025052468):
ivory/charcoal canvases, terracotta accent, Cambria headings, icon cards.

Content: course_data.py (admin, topics, schedule) + data_labs.py (ten labs) + the
Topic 1 concept slides below (sources cited on the slides / in the LG).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS
import ccdeck as K
from ccdeck import (cover, section, cards, rows, timeline, loop, compare, table, image, statement,
                    prompt, lab_intro, lab_flow, hub, trainer, flow, tip, header, card, text, rich, icon,
                    line, circle, box, picture, ACC, ACC_D, TEAL, PLUM, CHAR, PANEL, WHITE, INK, MUTED,
                    SOFT, LIGHT, IVORY, SERIF)

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
A = os.path.join(REPO, "courseware", "assets")
def asset(*p): return os.path.join(A, *p)

D = K.Deck(C.TITLE, C.COURSE_CODE, C.SHORT_TITLE)
VER = C.VERSION.lstrip("v")
MARK = {}
def mark(k): MARK[k] = D.n + 1

# ====================================================================== ADMIN
mark("admin")
cover(D, f"WSQ Course Code: {C.COURSE_CODE}", "Build a Human–AI Workforce\nwith Autonomous AI Agents",
      f"Version {VER}  ·  {C.VERSION_DATE}",
      f"{C.ORG}\n{C.UEN}",
      "www.tertiarycourses.com.sg   |   enquiry@tertiaryinfotech.com   |   +65 6100 0613",
      logo=os.path.join(os.path.dirname(HERE), "assets", "tertiary-infotech-logo.png"))

s = D.new(); header(D, s, "Housekeeping", "Digital Attendance")
card(s, 0.6, 1.95, 7.6, 3.6); icon(s, "phone", 0.95, 2.25, 0.62)
text(s, 1.8, 2.3, 6.2, 0.5, "Attendance is mandatory for SSG funding.", 17, INK, bold=True, font=SERIF)
text(s, 0.95, 3.1, 7.0, 2.3, "Take AM, PM and Assessment digital attendance for every session.\nScan the SSG digital attendance QR code shown by your trainer with your phone camera.\nThe TRAQOM survey and Assessment attendance are taken on assessment day.", 15, MUTED, lh=1.3)
card(s, 8.6, 1.95, 4.1, 3.6, fill=CHAR)
text(s, 8.6, 2.35, 4.1, 0.5, "Minimum", 20, SOFT, font=SERIF, align="c", autofit=False)
text(s, 8.6, 2.85, 4.1, 1.2, "75%", 60, ACC, bold=True, font=SERIF, align="c", autofit=False)
text(s, 8.6, 4.2, 4.1, 0.6, "attendance required", 18, SOFT, font=SERIF, align="c", autofit=False)

trainer(D, "Introduction", "[ Trainer Name ]", "[ Title / Role ]",
        [("grad", "Qualifications", ""), ("star", "Expertise", ""), ("briefcase", "Experience", ""), ("mail", "Contact / Profile", "")], template=True)
trainer(D, "Introduction", "Dr. Alfred Ang", "AI Trainer & Engineer\nTertiary Infotech Academy",
        [("grad", "Qualifications", "PhD-qualified trainer specialising in AI, automation and software engineering."),
         ("robot", "Expertise", "Builds autonomous AI agents and multi-agent workflows with Hermes Agent and OpenAI Dots."),
         ("users", "Experience", "Trains professionals across Singapore on practical, project-based AI skills."),
         ("medal", "Certifications", "Claude Certified Associate (Foundations), PMP, AWS, Microsoft, CompTIA, CKA, CKAD."),
         ("linkedin", "Profile", "linkedin.com/in/angchewhoe   ·   github.com/alfredang")],
        badge=asset("claude-certified-associate.png"))

s = D.new(dark=True); header(D, s, "Introduction", "Let's Know Each Other", "Take a minute to introduce yourself to the class:")
for i, (ic, t) in enumerate([("user", "Your name & role"), ("briefcase", "What you do day to day"),
                             ("robot", "Your experience with AI or agents"), ("target", "One task you want an AI agent to take off your plate")]):
    x = 0.6 + i * 3.08; card(s, x, 2.7, 2.9, 2.6, fill=K.PANEL, shadow=False)
    icon(s, ic, x + 1.12, 3.0, 0.66); text(s, x + 0.2, 3.9, 2.5, 1.2, t, 15, WHITE, bold=True, font=SERIF, align="c")

cards(D, "Housekeeping", "Ground Rules", [
    ("Phones on silent", "Step out quietly for calls or breaks.", "phone"),
    ("Participate actively", "No question is too small — ask freely.", "chat"),
    ("Mutual respect", "Agree to disagree; one conversation at a time.", "handshake"),
    ("Be punctual", "Return from breaks on time.", "clock"),
    ("75% attendance", "Required for funding eligibility.", "check"),
    ("Stay hands-on", "Follow along with every lab.", "tool")], cols=3, bottom=5.9)

s = D.new(); header(D, s, "Roadmap", "Course Outline", "Day 1: overview → always-on assistants → Hermes office practice. Day 2: Hermes teams and video.")
for i, tp in enumerate(C.TOPICS):
    x = 0.6 + i * 4.1; card(s, x, 2.45, 3.9, 4.35)
    circle(s, x + 0.3, 2.7, 0.62, ACC); text(s, x + 0.3, 2.7, 0.62, 0.62, str(tp["num"]), 20, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    text(s, x + 0.3, 3.45, 3.35, 0.95, tp["title"], 16, INK, bold=True, font=SERIF)
    text(s, x + 0.3, 4.45, 3.35, 2.25, "\n".join("•  " + it for it in tp["items"]), 12, MUTED, lh=1.25)

cards(D, "What you'll achieve", "Learning Outcomes", [
    ("LO1 · Analyse AI applications", C.LEARNING_OUTCOMES[0].split(": ", 1)[1], "search"),
    ("LO2 · Agent design and efficiency", C.LEARNING_OUTCOMES[1].split(": ", 1)[1], "gear"),
    ("LO3 · Evaluate & improve", C.LEARNING_OUTCOMES[2].split(": ", 1)[1], "trend")],
    cols=3, sub="Mapped to the TSC Artificial Intelligence Application in Product Development (ICT-TEM-4034-1.1).", desc_pt=14)

table(D, "What you'll achieve", "Learning Units, Topics and Labs", ["LU", "Learning unit", "Delivered through", "K & A", "Hours"],
      [(u["lu"], u["title"], u["covers"], ", ".join(u["codes"]), f"{u['hours']} h") for u in C.LUS] +
      [("Assess", "WA-SAQ (1 h) + Practical Performance (1 h)", "Day 2, 4:30–6:30 PM", "K1–K6 · A1–A6", "2 h")],
      colw=[0.9, 3.6, 4.6, 1.8, 0.9], size=12, sub="Approved Course Proposal: TSC ICT-TEM-4034-1.1 Artificial Intelligence Application in Product Development — 16 hours.")
for day in (1, 2):
    rows_ = [(f"{a}–{b}", t, "Assess" if lu == "ASSESS" else (lu or "—")) for a, b, m, k, t, lu in C.SCHEDULE[day]]
    table(D, "Roadmap", f"Lesson Plan — Day {day} (9:30 AM – 6:30 PM)", ["Time", "Session", "LU"], rows_,
          colw=[1.5, 9.7, 0.9], size=10.5 if day == 1 else 11)

s = D.new(); header(D, s, "Roadmap · Hands-on", "Eight Activities Across Two Days",
                    "Four activities per day: personal assistant setup, Hermes office work, then a supervised video team.")
for i, L in enumerate(LABS):
    r, c = divmod(i, 4); x = 0.6 + c * 3.08; y = 2.3 + r * 2.07
    dark = L["day"] == 2
    card(s, x, y, 2.3, 1.97, fill=CHAR if dark else WHITE)
    text(s, x + 0.18, y + 0.14, 2.0, 0.3, f"LAB {L['num']}  ·  DAY {L['day']}", 10, ACC, bold=True, autofit=False)
    icon(s, L["icon"], x + 0.18, y + 0.5, 0.48, fill=ACC if dark else TEAL)
    text(s, x + 0.18, y + 1.02, 1.98, 0.5, L["short"], 13.5, WHITE if dark else INK, bold=True, font=SERIF, minpt=10, lh=1.0)
    text(s, x + 0.18, y + 1.53, 1.98, 0.4, L["paradigm"], 9.5, SOFT if dark else MUTED, minpt=8, lh=1.0)
tip(D, s, "Day 1: always-on assistant, then Hermes office worker. Day 2: Hermes Kanban team, video and governance.", y=6.5)

s = D.new(); header(D, s, "Roadmap · Hands-on", "Lab Materials & the Lab Prompts Page",
                    "Everything you need is in the course repo: instructions PDF, mock data, skills and copy-ready prompts for every lab.")
shot = asset("screenshots", "prompts-page.png")
if os.path.exists(shot):
    picture(s, shot, 0.7, 2.5, maxw=6.6, maxh=4.25)
for i, (ic, t, d) in enumerate([
        ("download", "Get the labs", "github.com/tertiarycourses/TGS-2024043854-… → Code → Download ZIP. Unzip anywhere."),
        ("file", "Open the prompts page", "Double-click prompts/index.html — pick your lab, click Copy, paste into your chosen assistant or Hermes Desktop, as specified."),
        ("folder", "Use the lab folder", "labs/labNN-…/ holds README, LAB-NN-Instructions.pdf, COPY-PROMPTS.txt and data/."),
        ("check", "Verify every result", "Each lab ends with a checkpoint — evidence, not vibes.")]):
    y = 2.5 + i * 1.08; icon(s, ic, 7.7, y, 0.52)
    text(s, 8.38, y - 0.04, 4.4, 0.38, t, 15, INK, bold=True, font=SERIF)
    text(s, 8.38, y + 0.34, 4.4, 0.7, d, 11.5, MUTED, minpt=9)

image(D, "Course Portal", "Login to LMS and Download Course Material", asset("screenshots", "lms-login.png"),
      caption="Log in at lms-tms.tertiaryinfotech.com with your registered email and the OTP sent to your inbox, "
              "then open this course to download the slides and Learner Guide.")
flow(D, "Learning Management System", "Download Course Material", [
    ("globe", "Open the LMS", "Go to lms-tms.tertiaryinfotech.com"),
    ("mail", "Send OTP", "Enter your registered email and click Send OTP."),
    ("lock", "Verify", "Key in the one-time password from your inbox."),
    ("folder", "Open the course", "Select Build a Human-AI Workforce with Autonomous AI Agents."),
    ("download", "Download", "Slides PDF + Learner Guide — keep them for the open-book assessment.")])

mark("briefing")
cards(D, "Assessment", "Briefing for Assessment", [
    ("Clear your space", "Phones and other materials under the table or on the floor.", "inbox"),
    ("No recording", "No photos or recording of assessment scripts.", "camera"),
    ("Open book", "Slides, Learner Guide and approved materials only.", "book"),
    ("Work individually", "No discussion during the assessment.", "user"),
    ("Manage your time", "WA (1 hour) then PP (1 hour).", "clock"),
    ("Appeals", "An appeal process is available if you disagree with the outcome.", "scale")], cols=3, bottom=5.9)

s = D.new(); header(D, s, "Assessment", "Assessment & Funding")
card(s, 0.6, 1.95, 6.0, 4.6); icon(s, "clipboard", 0.9, 2.25, 0.6)
text(s, 1.65, 2.3, 4.7, 0.5, "Final Assessment", 19, INK, bold=True, font=SERIF)
text(s, 0.95, 3.15, 5.4, 3.2, "•  " + C.ASSESSMENT["written"] + "\n•  " + C.ASSESSMENT["practical"] +
     "\n•  Day 2, from 4:30 PM — open book\n•  Allowed: slides, Learner Guide, approved materials\n•  Appeal process available", 13.5, MUTED, lh=1.25)
card(s, 6.85, 1.95, 5.85, 4.6, fill=CHAR); icon(s, "coins", 7.15, 2.25, 0.6)
text(s, 7.9, 2.3, 4.6, 0.5, "Criteria for Funding", 19, WHITE, bold=True, font=SERIF)
text(s, 7.2, 3.15, 5.3, 3.2, "Minimum 75% attendance\nBased on SSG digital attendance records.\n\nAssessed as 'Competent'\nComplete and pass both assessment components (WA and PP).", 14, SOFT, lh=1.25)

ASSESS_FLOW = [("clipboard", "TRAQOM", "Scan the TRAQOM QR code on the LMS and complete the survey."),
               ("phone", "Attendance", "Take the Assessment digital attendance (SSG QR)."),
               ("pen", "Assessment", "Sit the WA (SAQ), then the PP — open book."),
               ("send", "Submit", "Upload your answers on the LMS."),
               ("check", "Sign the record", "Sign the Assessment Summary Record.")]
flow(D, "Assessment", "Assessment Flow", ASSESS_FLOW, sub="On assessment day, follow these five steps in order.")

# ====================================================================== TOPIC 1
import slides_2026 as U
import slides_v23 as V23
LAB_EXTRAS = {}
def meet_kopi(kick):
    """The course company, introduced at the start of Activity 1 (its meetings drive the Lab 1 schedule check)."""
    s = D.new(dark=True); header(D, s, kick + " · Your company", "Meet Kopi Kaki Co.",
                                 "The fictional Singapore kopi chain you work for from this activity to Day 2. Its meetings are your Activity 1 calendar. All data is synthetic.")
    facts = [("store", "12 outlets · 140 staff", "Heritage kopi, modern craft — Tiong Bahru to Changi T3."),
             ("coffee", "Launch: Gula Melaka Cold Brew", "SGD 6.80 · 1 Dec 2026 · code SHIOK20 (20% off first app order, 1–14 Dec)."),
             ("target", "Campaign #ShiokColdBrew", "17 Nov – 14 Dec · SGD 15,000 · 2,500 pre-orders · 8% engagement · 40k views."),
             ("shield", "Rules that matter", "No health or halal claims · no competitor bashing · human APPROVE before anything is public.")]
    for i, (ic, t, d) in enumerate(facts):
        r, c = divmod(i, 2); x = 0.6 + c * 6.15; y = 2.55 + r * 2.05
        card(s, x, y, 5.95, 1.85, fill=K.PANEL, shadow=False); icon(s, ic, x + 0.28, y + 0.3, 0.6)
        text(s, x + 1.08, y + 0.28, 4.7, 0.5, t, 17, WHITE, bold=True, font=SERIF)
        text(s, x + 1.08, y + 0.82, 4.65, 0.95, d, 13, SOFT)

def lab_block(L):
    kick = f"Topic {L['topic']} · Lab {L['num']}"
    if f"lab{L['num']}" not in MARK: mark(f"lab{L['num']}")
    mark(f"lab{L['num']}i")
    lab_intro(D, L, kick)
    if L["num"] == 1: meet_kopi(kick)   # Activity 1 runs on Kopi Kaki meetings
    lab_flow(D, L, kick)
    for fn in LAB_EXTRAS.get(L["num"], []): fn(L, kick)
    pr = [st for st in L["steps"] if st.get("prompt")]
    key = pr[:1] if L["num"] in (6, 9) else (pr if L["num"] == 4 else pr[:2])
    for st in key:
        prompt(D, kick, st["title"], st["prompt"],
               side=[("chat", "Paste into", st.get("where", "Hermes chat")),
                     ("check", "Expect", st.get("expect", "A saved output in your workspace.")),
                     ("hand", "You decide", st.get("decide", L["human"]))])
    if L["num"] == 1: return   # Lab 1 ends on its last task slide (checkpoint slide removed in v2.7)
    rows(D, kick, f"Lab {L['num']} — Checkpoint & Reflection",
         [("check", "Verify", v) for v in L["verify"][:3]] + [("lightbulb", "Concepts in action", "  ·  ".join(L["concepts"][:2])),
                                                              ("rocket", "Stretch challenge", L["challenge"])], dark=True)

def _cmd(L, kick, title, idx, side):
    st = L["steps"][idx]
    prompt(D, kick, title, st["cmd"], side=side, label="TERMINAL  ·  copy from the Lab Prompts page")

# --- Lab-specific concept / screenshot slides
LAB_EXTRAS[1] = [lambda L,k: V23.muse_invite(D,k), lambda L,k: V23.dots_setup(D,k), lambda L,k: V23.wispr(D,k)]   # Activity 1A / 1B visual slides
LAB_EXTRAS[5] = [lambda L,k: hub(D,k,"Five Hermes Profiles, Distinct Owned Outputs","Kanban parents\n+ human gates",[("search","researcher","Source facts -> research.md"),("pen","scriptwriter","Three scenes -> storyboard.md"),("film","producer","Local renderer -> final.mp4"),("eyecheck","auditor","Independent evidence -> audit-report.md"),("file","publisher","Accepted local package only"),("user","Human owner","Unassigned gates; exact-version decisions")]),lambda L,k:image(D,k,"Inspect Your Actual Kanban Video Team",asset("screenshots","hermes-kanban.png"),caption="Reference UI only. Capture your own bot/profile owners, dependency state, video task/output and human gate.")]

U.swda(D)
V23.topic1(D,C,mark)
lab_block(LABS[0])   # Topic 1 ends with its lab
mark("lab1end")
for k in ("activity", "demo", "consolidation"): mark(k)   # legacy FG keys; v2.6 maps no slides to them

# ====================================================================== TOPIC 2 · HERMES
mark("t2")
T2 = C.TOPICS[1]
section(D, "Topic 2", T2["title"], T2["items"], sub="After lunch: one Hermes office worker for Kopi Kaki Co.")
table(D, "The course scenario", "The Kopi Kaki Company Pack (data/ in every lab)",
      ["File", "What it is", "Used in"],
      [("AGENTS.md", "Company context Hermes loads automatically from the folder", "Activities 2–8"),
       ("brand-guide.md · campaign-brief.md", "Voice, colours, formats · product, offer, KPIs, timeline", "Activities 2–8"),
       ("compliance-rules.md · video-qa-checklist.md", "C1–C10 brand-safety rules · V1–V9 video checks", "Activities 2–6, 8"),
       ("customer-reviews.csv · competitors.csv", "60 synthetic reviews · 6 fictional competitors", "Activities 2, 5"),
       ("social-comments.csv", "20 comments incl. complaints, legal, PII, spam", "Activities 4, 5"),
       ("campaign-week1-metrics.csv · sales-by-outlet.csv", "Post metrics and outlet sales for week 1", "Activities 2, 5, 8"),
       ("skills/ · souls/ · tasks/ · DESIGN.md", "Ready-made skills, agent roles, task briefs, visual identity", "Activities 2–5, 8")],
      colw=[4.0, 5.6, 2.5], size=11.5)


cards(D, "Topic 2 · Hermes Agent", "What Is Hermes Agent?", [
    ("Open source, self-hosted", "MIT licence by Nous Research. Runs on your laptop, a VPS, Docker or the desktop app.", "server"),
    ("Grows with you", "Persistent memory and session search; writes and improves its own skills after hard tasks.", "sparkles"),
    ("Every channel", "One gateway: CLI, Telegram, WhatsApp, Slack, Discord, Signal, email …", "chat"),
    ("Tools & MCP", "Web search, files, terminal, browser, image generation, TTS and any MCP server.", "tool"),
    ("Proactive", "Built-in cron scheduler runs jobs and delivers results to your chat.", "clock"),
    ("Multi-agent", "Profiles (isolated agents) + a Kanban board with dependencies, reviews and swarms.", "kanban")],
    cols=3, sub="Inspect the current installed version and verify each required tool before practice.")
hub(D, "Topic 2 · Hermes Agent", "Hermes Architecture — This Morning's Harness, in Hermes", "Hermes agent loop\n+ your LLM", [
    ("file", "Context", "AGENTS.md, SOUL.md, USER.md"),
    ("memory", "Memory", "MEMORY.md + session search"),
    ("puzzle", "Skills", "SKILL.md, hub + self-written"),
    ("tool", "Tools & MCP", "web, files, terminal, images"),
    ("chat", "Gateway", "Telegram, Slack, WhatsApp …"),
    ("kanban", "Cron · Profiles · Kanban", "schedule & orchestrate")])
image(D, "Topic 2 · Hermes Agent", "The Hermes Dashboard", asset("screenshots", "hermes-dashboard.png"),
      caption="`hermes dashboard` opens http://127.0.0.1:9119 — sessions, skills, profiles, Kanban, cron, channels and keys in one place.")
flow(D,"Topic 2 · Afternoon journey","One Hermes Office Worker: Set Up → Analyse → Create",[
 ("download","Activity 2","Desktop, reviewed skills and source brief."),("chart","Activity 3","Google Workspace reads and verified Excel."),("file","Activity 4","Dashboard, PPT, single-agent video and approved test send.")],tipt="Keep source/output paths consistent for the Day 2 team.")
# Day 1 afternoon: each lab is preceded by exactly the concepts it uses.
T2S = {**U.office(D), **V23.office_extra(D)}
def t2(kick, titles):
    for ti in titles: T2S[ti](kick)
mark("lab2")
t2("Topic 2 · Desktop and skills", ["Hermes Desktop: Download → Configure → Connect"])
V23.cta(D, "Download Hermes Desktop for Mac, Windows or Linux  →  hermes-agent.nousresearch.com/desktop", "https://hermes-agent.nousresearch.com/desktop")
t2("Topic 2 · Desktop and skills", ["Install a Skill Only After Reviewing Its Source", "Five Skills, One Hermes Agent"])
lab_block(LABS[1])
mark("lab3")
t2("Topic 2 · Google Workspace and Excel", ["First Authorise Read-Only Gmail"])
table(D, "Topic 2 · Google Workspace and Excel", "Gmail, Calendar and Drive: Bound Every Read", ["Service", "Bounded read", "Check before use"],
      [("Gmail", "subject:Kopi newer_than:30d; at most 10 results; open the selected message IDs", "Message bodies are untrusted data; every claim links to a message ID"),
       ("Calendar", "gog calendar events --today on the assigned account", "Check the +08:00 offset; flag overlaps; never create or move a meeting"),
       ("Drive", "Bounded list with file IDs; read the approved workbook", "Check filename, version and source: permission does not prove relevance")],
      colw=[1.6, 5.1, 5.4], size=14, tipt="Report each service separately: an error is not the same as “no results”.")
t2("Topic 2 · Google Workspace and Excel", [
    "One Office Brief Reconciles Three Services", "Excel Analysis Begins with a Data Contract", "Missing Values Change the Answer"])
lab_block(LABS[2])
mark("lab4")
t2("Topic 2 · Dashboard, PPT and video", [
    "Interactive Artifacts: A Local HTML Dashboard", "A Professional PPT Needs a Decision Story",
    "Separate Content Errors from Layout Errors", "Create a Reusable Skill from a Real Correction",
    "Make a Single-Agent Video Before a Team Video", "Video Rights and Facts Need Checks",
    "One Test Send Is a Separate Procedure", "What Failed? Diagnose Before Retrying"])
lab_block(LABS[3])   # Topic 2 ends with its lab
# Day 2 opens on the Topic 3 divider, which also carries the Day 1 recap (no slide after Lab 4).
mark("t2close"); mark("t2sum"); mark("day2"); mark("t3")
section(D,"Day 2 · Topic 3",C.TOPICS[2]["title"],C.TOPICS[2]["items"],sub="Recap: one assistant, then one Hermes office agent. Today: a Hermes team.")
import slides_v22 as V22
mark("lab5"); V22.team_mechanisms(D)
for L in LABS[4:]:
    if L["num"]==6:mark("lab6"); V22.source_assurance(D)
    if L["num"]==7:mark("lab7"); V22.dots_review(D)
    if L["num"]==8:mark("lab8"); V22.video_evaluation(D)
    lab_block(L)   # Topic 3 ends with Lab 8
mark("t3sum")

mark("wrap")
section(D, "Wrap-up", "Course Summary & Next Steps", ["What you can now do", "Practice exam", "Assessment", "Digital attendance"])
cards(D, "Wrap-up", "Summary & Q&A", [
    ("Topic 1", "Agents loop through perception, reasoning and action; the harness and the human make them reliable.", "brain"),
    ("Topic 2", "One Hermes Desktop agent produced the Google brief, Excel analysis, dashboard and PPT; Kanban extended it on Day 2.", "robot"),
    ("Topic 3", "Hermes bots produced and audited the video; Dots supplied a supervised comparison; source checks and human gates remained visible.", "building"),
    ("Your workforce", "Decide per task: agent, agent team or human — and where the human approves.", "handshake")],
    cols=4)
rows(D, "Wrap-up", "Continue Building Your Human–AI Workforce", [
    ("server", "Run 24/7", "Move Hermes to a small VPS or Docker host so cron and Telegram keep running."),
    ("puzzle", "Codify your SOPs", "Turn your team's checklists into SKILL.md skills and agent instructions."),
    ("shield", "Govern from day one", "Budgets, approval gates, audit trail — follow IMDA's agentic AI framework."),
    ("chart", "Measure", "Track cycle time, revisions, cost per deliverable and quality before you scale.")], dark=True)
s = D.new(); header(D, s, "Test yourself", "Practice Exam", "Sharpen your readiness before the final assessment.")
pe = asset("screenshots", "practice-exam.png")
if os.path.exists(pe):
    picture(s, pe, 0.7, 2.45, maxw=7.2, maxh=4.3)
for i, (ic, t, d) in enumerate([("globe", "Open the portal", "https://exams.tertiaryinfotech.com"),
                                ("clock", "Time yourself", "Attempt it under exam conditions."),
                                ("book", "Review", "Read every explanation; revisit the matching lab.")]):
    y = 2.6 + i * 1.35; icon(s, ic, 8.3, y, 0.55)
    text(s, 9.0, y - 0.02, 3.7, 0.42, t, 16, INK, bold=True, font=SERIF)
    text(s, 9.0, y + 0.42, 3.7, 0.8, d, 13, MUTED)
mark("assess")
s = D.new(); header(D, s, "Assessment", "Final Assessment")
for i, (ic, t, d, dark) in enumerate([
        ("pen", "Written Assessment (WA)", "Short-Answer Questions — 1 hour, open book. Six questions on the knowledge from Topics 1–3.", False),
        ("tool", "Practical Performance (PP)", "Three tasks — Task 1 TWO images: chosen assistant (Activity 1) + Hermes artifact (Activity 4); Task 2 ONE PPT image (Activity 4); Task 3 ONE real Hermes Kanban video-team image (Activity 5/8). Written analysis; 1 hour, open book.", True)]):
    x = 0.6 + i * 6.15; card(s, x, 1.95, 5.95, 3.4, fill=CHAR if dark else WHITE)
    icon(s, ic, x + 0.3, 2.25, 0.6)
    text(s, x + 1.05, 2.3, 4.7, 0.5, t, 19, WHITE if dark else INK, bold=True, font=SERIF)
    text(s, x + 0.35, 3.1, 5.3, 2.1, d, 14.5, SOFT if dark else MUTED, lh=1.25)
tip(D, s, "Take the Assessment digital attendance and submit your answers on the LMS at https://lms-tms.tertiaryinfotech.com/.", y=5.7)
flow(D, "Assessment", "Assessment Flow", ASSESS_FLOW, sub="On assessment day, follow these five steps in order.")
s = D.new(dark=True); header(D, s, "Before you go", "Certification, TRAQOM Survey & Digital Attendance")
card(s, 0.6, 1.95, 6.0, 4.3, fill=K.PANEL, shadow=False); icon(s, "clipboard", 0.9, 2.25, 0.6)
text(s, 1.65, 2.3, 4.7, 0.5, "TRAQOM Survey (mandatory)", 18, WHITE, bold=True, font=SERIF)
text(s, 0.95, 3.15, 5.4, 2.9, "Complete the certification & TRAQOM survey to receive your certificate.\n\nScan the TRAQOM QR code on the LMS.", 15, SOFT, lh=1.25)
card(s, 6.85, 1.95, 5.85, 4.3, fill=K.PANEL, shadow=False); icon(s, "phone", 7.15, 2.25, 0.6)
text(s, 7.9, 2.3, 4.6, 0.5, "Digital Attendance", 18, WHITE, bold=True, font=SERIF)
text(s, 7.2, 3.15, 5.3, 2.9, "Take the AM, PM and Assessment digital attendance — scan the SSG QR code.\n\nMinimum 75% attendance is required for funding.", 15, SOFT, lh=1.25)
s = D.new(dark=True)
circle(s, 10.4, -1.6, 4.6, ACC); circle(s, 11.6, 4.3, 2.6, TEAL)
text(s, 0.9, 2.4, 10, 1.2, "Thank You!", 54, WHITE, bold=True, font=SERIF, autofit=False)
text(s, 0.9, 3.75, 10, 0.6, "Questions? We're here to help — during and after class.", 18, SOFT, autofit=False)
text(s, 0.9, 6.6, 11, 0.4, "enquiry@tertiaryinfotech.com   |   +65 6100 0613   |   www.tertiarycourses.com.sg", 13, K.DIM, autofit=False)

K.footer(D, s)

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
D.save(OUT)
mark("end")
import json
json.dump(MARK, open(os.path.join(HERE, "slide_map.json"), "w"), indent=1)
print(f"Saved {OUT}  ({D.n} slides)")
