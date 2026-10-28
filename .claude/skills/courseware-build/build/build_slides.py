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
         ("robot", "Expertise", "Builds autonomous AI agents and multi-agent workflows with Hermes Agent, Paperclip and Claude Code."),
         ("users", "Experience", "Trains professionals across Singapore on practical, project-based AI skills."),
         ("medal", "Certifications", "PMP, AWS, Microsoft, CompTIA, CKA, CKAD."),
         ("linkedin", "Profile", "linkedin.com/in/angchewhoe   ·   github.com/alfredang")])

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

s = D.new(); header(D, s, "Roadmap", "Course Outline", "Three topics, ten connected use-case labs, one company: " + C.SCENARIO.split(" — ")[0] + ".")
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

s = D.new(); header(D, s, "Roadmap · Hands-on", "Ten Labs, One Company",
                    "Every lab builds on the last — the same Kopi Kaki campaign grows from one agent to a governed AI company.")
for i, L in enumerate(LABS):
    r, c = divmod(i, 5); x = 0.6 + c * 2.46; y = 2.4 + r * 2.02
    dark = L["day"] == 2
    card(s, x, y, 2.3, 1.88, fill=CHAR if dark else WHITE)
    text(s, x + 0.18, y + 0.14, 2.0, 0.3, f"LAB {L['num']}  ·  DAY {L['day']}", 10, ACC, bold=True, autofit=False)
    icon(s, L["icon"], x + 0.18, y + 0.5, 0.48, fill=ACC if dark else TEAL)
    text(s, x + 0.18, y + 1.05, 1.98, 0.6, L["short"], 13.5, WHITE if dark else INK, bold=True, font=SERIF, minpt=10)
    text(s, x + 0.18, y + 1.6, 1.98, 0.35, L["paradigm"], 9.5, SOFT if dark else MUTED, minpt=8)
tip(D, s, "Day 1: single Hermes agent and office automation. Day 2: Kanban, agent teams, video production and governance.", y=6.5)

s = D.new(); header(D, s, "Roadmap · Hands-on", "Lab Materials & the Lab Prompts Page",
                    "Everything you need is in the course repo: instructions PDF, mock data, skills and copy-ready prompts for every lab.")
shot = asset("screenshots", "prompts-page.png")
if os.path.exists(shot):
    picture(s, shot, 0.7, 2.5, maxw=6.6, maxh=4.25)
for i, (ic, t, d) in enumerate([
        ("download", "Get the labs", "github.com/tertiarycourses/TGS-2024043854-… → Code → Download ZIP. Unzip anywhere."),
        ("file", "Open the prompts page", "Double-click prompts/index.html — pick your lab, click Copy, paste into Hermes, Telegram or Paperclip."),
        ("folder", "Use the lab folder", "labs/labNN-…/ holds README, LAB-NN-Instructions.pdf, COPY-PROMPTS.txt and data/."),
        ("check", "Verify every result", "Each lab ends with a checkpoint — evidence, not vibes.")]):
    y = 2.5 + i * 1.08; icon(s, ic, 7.7, y, 0.52)
    text(s, 8.38, y - 0.04, 4.4, 0.38, t, 15, INK, bold=True, font=SERIF)
    text(s, 8.38, y + 0.34, 4.4, 0.7, d, 11.5, MUTED, minpt=9)

s = D.new(dark=True); header(D, s, "The course scenario", "Meet Kopi Kaki Co.",
                             "A fictional Singapore kopi chain — the company every lab works for. All data is synthetic.")
facts = [("store", "12 outlets · 140 staff", "Heritage kopi, modern craft — Tiong Bahru to Changi T3."),
         ("coffee", "Launch: Gula Melaka Cold Brew", "SGD 6.80 · 1 Dec 2026 · code SHIOK20 (20% off first app order, 1–14 Dec)."),
         ("target", "Campaign #ShiokColdBrew", "17 Nov – 14 Dec · SGD 15,000 · 2,500 pre-orders · 8% engagement · 40k views."),
         ("shield", "Rules that matter", "No health or halal claims · no competitor bashing · human APPROVE before anything is public.")]
for i, (ic, t, d) in enumerate(facts):
    r, c = divmod(i, 2); x = 0.6 + c * 6.15; y = 2.55 + r * 2.05
    card(s, x, y, 5.95, 1.85, fill=K.PANEL, shadow=False); icon(s, ic, x + 0.28, y + 0.3, 0.6)
    text(s, x + 1.08, y + 0.28, 4.7, 0.5, t, 17, WHITE, bold=True, font=SERIF)
    text(s, x + 1.08, y + 0.82, 4.65, 0.95, d, 13, SOFT)

image(D, "Learning Management System", "Courseware & Assessment on the LMS", asset("screenshots", "lms-portal.png"),
      side=[("login", "Log in", "lms-tms.tertiaryinfotech.com with your registered email + OTP."),
            ("download", "Download the courseware", "Slides, Learner Guide and Lesson Plan for the open-book assessment."),
            ("clipboard", "Take the assessment", "Complete the WA and PP and upload your answers on the LMS.")],
      caption="LMS: https://lms-tms.tertiaryinfotech.com/  →  open this course  →  Courseware tab.")
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
U.swda(D)
U.topic1(D, C, mark)
U.demo(D, mark)

# ====================================================================== TOPIC 2 · HERMES
mark("t2")
T2 = C.TOPICS[1]
section(D, "Topic 2", T2["title"], T2["items"], sub="Day 1 — one Hermes agent for the launch office. Day 2 — Kanban team extension.")
cards(D, "Topic 2 · Hermes Agent", "What Is Hermes Agent?", [
    ("Open source, self-hosted", "MIT licence by Nous Research. Runs on your laptop, a VPS, Docker or the desktop app.", "server"),
    ("Grows with you", "Persistent memory and session search; writes and improves its own skills after hard tasks.", "sparkles"),
    ("Every channel", "One gateway: CLI, Telegram, WhatsApp, Slack, Discord, Signal, email …", "chat"),
    ("Tools & MCP", "Web search, files, terminal, browser, image generation, TTS and any MCP server.", "tool"),
    ("Proactive", "Built-in cron scheduler runs jobs and delivers results to your chat.", "clock"),
    ("Multi-agent", "Profiles (isolated agents) + a Kanban board with dependencies, reviews and swarms.", "kanban")],
    cols=3, sub="Inspect the current installed version and verify each required tool before practice.")
hub(D, "Topic 2 · Hermes Agent", "Hermes Architecture — the Harness Around the Model", "Hermes agent loop\n+ your LLM", [
    ("file", "Context", "AGENTS.md, SOUL.md, USER.md"),
    ("memory", "Memory", "MEMORY.md + session search"),
    ("puzzle", "Skills", "SKILL.md, hub + self-written"),
    ("tool", "Tools & MCP", "web, files, terminal, images"),
    ("chat", "Gateway", "Telegram, Slack, WhatsApp …"),
    ("kanban", "Cron · Profiles · Kanban", "schedule & orchestrate")])
image(D, "Topic 2 · Hermes Agent", "The Hermes Dashboard", asset("screenshots", "hermes-dashboard.png"),
      caption="`hermes dashboard` opens http://127.0.0.1:9119 — sessions, skills, profiles, Kanban, cron, channels and keys in one place.")
flow(D, "Topic 2 · Day 1 journey", "Two Days: Office Agent → Kanban Team → Human Gates", [
    ("user", "Lab 1", "First AI employee — research brief, memory."),
    ("megaphone", "Lab 2", "Google, Excel, interactive HTML and professional PPT."),
    ("handshake", "Lab 3", "Office exceptions, source boundaries and exact-version review."),
    ("video", "Lab 4", "5-agent video studio with a human gate."),
    ("chart", "Lab 5", "Swarm analysis, dashboard, decisions.")],
    tipt="Each lab saves to ~/kopi-kaki/outputs/labNN — the next lab builds on it.")
table(D, "Topic 2 · Day 1 journey", "The Kopi Kaki Company Pack (data/ in every lab)",
      ["File", "What it is", "Used in"],
      [("AGENTS.md", "Company context Hermes loads automatically from the folder", "All labs"),
       ("brand-guide.md · campaign-brief.md", "Voice, colours, formats · product, offer, KPIs, timeline", "All labs"),
       ("compliance-rules.md · video-qa-checklist.md", "C1–C10 brand-safety rules · V1–V9 video checks", "Labs 2–5, 8–9"),
       ("customer-reviews.csv · competitors.csv", "60 synthetic reviews · 6 fictional competitors", "Labs 1, 5"),
       ("social-comments.csv", "20 comments incl. complaints, legal, PII, spam", "Labs 3, 5"),
       ("campaign-week1-metrics.csv · sales-by-outlet.csv", "Post metrics and outlet sales for week 1", "Lab 5"),
       ("skills/ · souls/ · tasks/ · DESIGN.md", "Ready-made skills, agent roles, task briefs, visual identity", "Labs 2, 4, 5")],
      colw=[4.0, 5.6, 2.5], size=11.5)

LAB_EXTRAS = {}
def lab_block(L):
    kick = f"Topic {L['topic']} · Lab {L['num']}"
    mark(f"lab{L['num']}")
    lab_intro(D, L, kick)
    lab_flow(D, L, kick)
    for fn in LAB_EXTRAS.get(L["num"], []): fn(L, kick)
    pr = [st for st in L["steps"] if st.get("prompt")]
    key = pr[:2] if L["num"] not in (6, 9) else pr[:1]
    for st in key:
        prompt(D, kick, st["title"], st["prompt"],
               side=[("chat", "Paste into", st.get("where", "Hermes chat")),
                     ("check", "Expect", st.get("expect", "A saved output in your workspace.")),
                     ("hand", "You decide", L["human"])])
    rows(D, kick, f"Lab {L['num']} — Checkpoint & Reflection",
         [("check", "Verify", v) for v in L["verify"][:3]] + [("lightbulb", "Concepts in action", "  ·  ".join(L["concepts"][:2])),
                                                              ("rocket", "Stretch challenge", L["challenge"])], dark=True)

def _cmd(L, kick, title, idx, side):
    st = L["steps"][idx]
    prompt(D, kick, title, st["cmd"], side=side, label="TERMINAL  ·  copy from the Lab Prompts page")

# --- Lab-specific concept / screenshot slides
LAB_EXTRAS[1] = [
    lambda L, k: table(D, k, "Context & Memory Files in Hermes", ["File", "Scope", "What goes in it", "Loaded"],
        [("AGENTS.md (project)", "This folder", "Company facts, rules, current priority", "Every session started in the folder"),
         ("SOUL.md", "~/.hermes/ (per profile)", "The agent's role, personality and standing rules", "Every session"),
         ("MEMORY.md", "~/.hermes/memories/", "Facts the agent decides to remember (~2,200 chars)", "Session start"),
         ("USER.md", "~/.hermes/memories/", "What it knows about you and your preferences", "Session start"),
         ("Session history", "state database", "Every past conversation — searchable", "On demand (session search)")],
        colw=[2.3, 2.4, 4.6, 2.8], size=12, tipt="Short-term = this session's context window. Long-term = the files and history above."),
]
LAB_EXTRAS[2] = [
    lambda L,k: U.proof(D,k,"The Office Skill Contract",[
        ("login","gog-office","Assigned identity, bounded reads, source IDs and separate service failures."),
        ("chart","office-analytics","Actual workbook schema, reproducible calculations and reconciled totals."),
        ("code","interactive-dashboard","Outlet filter, sorting, reset and CSV export; works offline."),
        ("file","professional-ppt","Six editable slides, source notes, rendered checks and a real revision.")])
]
LAB_EXTRAS[3] = [
    lambda L,k: U.trace(D,k,"The Office Review Gate",[
        ("file","Draft","Name exact artifact and source IDs."),("alert","Challenge","Resolve conflict and reject untrusted instructions."),
        ("user","Human decision","ACCEPT or REVISE for the exact file hash."),("check","Recheck","Verify changed output and record decision.")],
        "An approval is specific to an artifact version; it does not grant future sending or publishing permission.")
]
LAB_EXTRAS[4] = [
    lambda L,k: hub(D,k,"Five Profiles, One Observable Video Workflow","Kanban dependencies\n+ human gates",[
        ("search","researcher","verified sources -> research.md"),("pen","scriptwriter","three scenes -> storyboard.md"),
        ("film","producer","local renderer -> final.mp4"),("eyecheck","auditor","independent checks -> audit-report.md"),
        ("file","publisher","local release-package.md only"),("user","Human owner","approve storyboard and exact final cut")]),
    lambda L,k: image(D,k,"Inspect the Real Kanban Board",asset("screenshots","hermes-kanban.png"),
        caption="Reference interface: inspect your own live owners, dependencies and blocked human gate. Capture your own PP evidence.")
]
LAB_EXTRAS[5] = [
    lambda L, k: hub(D, k, "Parallel Swarm with a Verifier", "Swarm root:\nweek-1 review", [
        ("chart", "analyst", "KPIs vs targets (CSV)"),
        ("chat", "listener", "sentiment & risks"),
        ("search", "researcher", "competitor & trend watch"),
        ("check", "auditor = verifier", "re-computes the numbers"),
        ("layers", "strategist = synthesiser", "dashboard + plan"),
        ("user", "You", "spot-check, approve 1–2 changes")]),
    lambda L, k: table(D, k, "The KPIs You Will Check", ["KPI", "Formula", "Target"],
        [("App pre-orders", "Σ app_preorders", "2,500 by 30 Nov"),
         ("Engagement rate", "(likes + comments + shares) ÷ reach", "≥ 8% (IG + TikTok)"),
         ("Click-through rate", "link_clicks ÷ reach", "Trend up week on week"),
         ("Cost per pre-order", "paid_spend_sgd ÷ app_preorders", "Lower is better"),
         ("Video views", "Σ video_views (TikTok + Reels)", "40,000")],
        colw=[3.0, 5.6, 3.5], size=13, tipt="Never forward a number you have not checked: verify at least one by hand."),
    lambda L, k: _cmd(L, k, "Launch the Swarm", 1,
                      [("users", "--worker", "Parallel cards: profile:title."),
                       ("check", "--verifier", "Waits for all workers, re-checks."),
                       ("layers", "--synthesizer", "Builds the dashboard and plan.")]),
]

U.office(D)
for L in LABS[:5]:
    if L["num"] == 4:
        mark("day2")
        section(D,"Day 2","From One Office Agent to a Video Team",["Kanban contracts and dependencies","Specialist workers and independent review","Human approval of the exact output"])
    lab_block(L)
mark("t2sum")
cards(D, "Topic 2 · Summary", "Hermes: From Office Work to Team Coordination", [
    ("Single agent", "Mia produced a Google brief, Excel analysis, interactive dashboard and professional deck.", "robot"),
    ("Human-in-the-loop", "Nothing went public without your APPROVE; risky comments came to you.", "handshake"),
    ("Multi-agent", "A five-role studio and a verified analysis swarm.", "users"),
    ("Harness", "Context, memory, skills, verification, gates, cron — the environment did the heavy lifting.", "gear")],
    cols=4, dark=True)

# ====================================================================== TOPIC 3 · PAPERCLIP
mark("t3")
T3 = C.TOPICS[2]
section(D, "Topic 3", T3["title"], T3["items"], sub="Day 2 — compare a governed company with a Claude Code multi-agent video team.")
cards(D, "Topic 3 · Paperclip", "What Is Paperclip?", [
    ("The company as the harness", "Open-source orchestration for a company of agents — org chart, goals, budgets, governance.", "building"),
    ("You are the Board", "Approve hires and strategy; pause, override, reassign or terminate any agent.", "gavel"),
    ("Bring your own agent", "Adapters for Claude Code, Codex, Gemini CLI, OpenClaw, Hermes, Cursor …", "plug"),
    ("Issues & goals", "Mission → goals → projects → issues: every task traces to a goal.", "target"),
    ("Heartbeats & routines", "Agents wake on a schedule or when work is assigned; routines create recurring work.", "clock"),
    ("Budgets & audit", "Per-agent budgets warn at 80% and auto-pause at 100%; append-only activity log.", "coins")],
    cols=3, sub="\"If OpenClaw is an employee, Paperclip is the company.\" — self-hosted at http://localhost:3100.")
image(D, "Topic 3 · Paperclip", "The Paperclip Dashboard", asset("paperclip", "pc-dashboard.png"),
      caption="Agents, issues, costs and approvals for the whole company — the Board's control room.")
table(D, "Topic 3 · Paperclip", "Hermes Agent vs Paperclip", ["", "Hermes Agent (Day 1)", "Paperclip (Day 2)"],
      [("Unit", "An agent (employee) — or a team of profiles", "A company of agents"),
       ("Orchestration", "Kanban board, dependencies, swarms", "Org chart, CEO delegation, projects & issues"),
       ("Human control", "APPROVE prompts, approval modes, blocked tasks", "Board approvals for hires & strategy; in_review gates"),
       ("Scheduling", "Cron jobs", "Routines + heartbeats"),
       ("Cost control", "Model choice per profile", "Budgets per agent / project / company, auto-pause"),
       ("Audit", "Sessions, Kanban history", "Immutable activity log, tool-call tracing"),
       ("Best for", "A personal or team agent that learns", "Running recurring business functions with governance")],
      colw=[2.0, 5.0, 5.1], size=12, hi_col=2)
flow(D, "Topic 3 · Day 2 journey", "Day 2: Found → Hire → Deliver → Automate → Govern", [
    ("building", "Lab 6", "Company, mission, budget, CEO."),
    ("users", "Lab 7", "Hire the team at the approval gate."),
    ("rocket", "Lab 8", "Claude Code team: research, storyboard, video and review."),
    ("clock", "Lab 9", "Weekly video routine with a Board gate."),
    ("gauge", "Lab 10", "Costs, audit, scorecard, improve.")],
    tipt="Same Kopi Kaki campaign as Day 1 — compare what changes when the work is run as a company.")

LAB_EXTRAS[6] = [
    lambda L, k: _cmd(L, k, "Install and Start Paperclip", 1,
                      [("terminal", "Option A", "npx paperclipai onboard --yes — Node.js 24.11+, local, no login."),
                       ("box", "Option B", "Docker: set BETTER_AUTH_SECRET + signing secret, then compose up."),
                       ("globe", "Open", "http://localhost:3100 → name the organization, create Ava.")]),
    lambda L, k: _cmd(L, k, "Guard Rails: CEO Role and Hard Budgets", 7,
                      [("briefcase", "Ava = CEO", "`agent update … role ceo` — the UI has no Role field."),
                       ("gavel", "Hiring gate", "Settings → General → Hiring → require Board approval (default OFF)."),
                       ("coins", "Budgets", "80% warning, 100% auto-pause — see Audit → Budgets.")]),
    lambda L, k: image(D, k, "Adapters — the Agents' Engine", asset("paperclip", "pc-adapters.png"),
                       caption="Enable the runtime you already have — Claude Code, Codex, Gemini CLI or Hermes — and test the connection."),
]
LAB_EXTRAS[7] = [
    lambda L, k: table(D, k, "A Good Hiring Plan (reference)", ["Role", "Reports to", "Mandate", "Budget / mo"],
        [("Market Researcher", "CEO", "Live trend, competitor and audience research with Tavily; cites sources", "USD 8"),
         ("Content Strategist", "CEO", "Campaign plan, calendar and briefs", "USD 8"),
         ("Copywriter", "Content Strategist", "Captions, scripts, replies in brand voice", "USD 8"),
         ("Video Producer", "Content Strategist", "Storyboards, renders, publish package", "USD 10"),
         ("Compliance Auditor", "CEO", "Audits every public item (C1–C10, V1–V9); can block release", "USD 5")],
        colw=[2.6, 2.4, 5.4, 1.7], size=12, tipt="Separation of duties: the auditor must not report to the people whose work it audits."),
    lambda L, k: image(D, k, "The Org Chart", asset("paperclip", "pc-org.png"),
                       caption="Board → CEO → specialists. Every hire passed an explicit Board decision."),
    lambda L, k: image(D, k, "Secrets — Tools Without Exposing Keys", asset("paperclip", "pc-secrets.png"),
                       caption="Store TAVILY_API_KEY as a company Secret and bind it to the researcher's runtime — it never appears in prompts or issues."),
]
LAB_EXTRAS[8] = [
    lambda L, k: table(D, k, "The Launch Backlog (paperclip-backlog.csv)", ["#", "Issue", "Owner", "Blocked by"],
        [("1", "Research SG cold-brew trends & competitor moves", "Market Researcher", "—"),
         ("2", "Campaign plan + 4-week content calendar", "Content Strategist", "1"),
         ("3", "Teaser-week captions (7 posts)", "Copywriter", "2"),
         ("4", "Script & storyboard the 25-s launch video", "Video Producer", "2"),
         ("5", "Render video + publish package", "Video Producer", "4"),
         ("6", "Compliance audit of captions and video", "Compliance Auditor", "3, 5"),
         ("7", "Board review & release pack", "CEO", "6")],
        colw=[0.6, 6.4, 3.2, 1.9], size=12),
    lambda L, k: image(D, k, "Issues Flow to the Board", asset("paperclip", "pc-tasks.png"),
                       caption="todo → in_progress → in_review → done. in_review is your quality gate: approve, or request changes with specific comments."),
]
LAB_EXTRAS[9] = [
    lambda L, k: image(D, k, "A Routine Fires the Pipeline", asset("paperclip", "pc-routine-pipeline.png"),
                       caption="Work → Routines: a schedule trigger (Monday 10:00, Asia/Singapore) generates the issue; the CEO delegates each stage."),
    lambda L, k: image(D, k, "Run Now — Test Before You Trust", asset("paperclip", "pc-routine-run.png"),
                       caption="Trigger the routine manually once and follow every stage before relying on the schedule."),
]
LAB_EXTRAS[10] = [
    lambda L, k: table(D, k, "Month-1 Agent Scorecard (agent-scorecard.csv)",
        ["Agent", "Issues done", "Audit FAILs", "Revisions", "Spend / budget (USD)", "Status"],
        [("Ava (CEO)", "13 / 14", "0", "1", "11.20 / 15", "Green"),
         ("Market Researcher", "9 / 9", "0", "0", "6.10 / 8", "Green"),
         ("Content Strategist", "6 / 7", "1", "1", "7.90 / 8", "Amber — 99% of budget"),
         ("Copywriter", "18 / 22", "4", "3", "5.30 / 8", "Amber — quality"),
         ("Video Producer", "3 / 5", "2", "2", "10.40 / 10", "Red — over budget"),
         ("Compliance Auditor", "27 / 27", "0", "0", "2.20 / 5", "Green")],
        colw=[2.6, 1.6, 1.6, 1.5, 2.4, 2.4], size=12, hi_col=5),
    lambda L, k: image(D, k, "Agents, Budgets and Status", asset("paperclip", "pc-agents.png"),
                       caption="Pause is reversible; terminate is not. Fix the instructions that caused rework — improve the harness."),
]
# Lab 8 uses actual Claude Code teammates, not the legacy Paperclip project flow.
LAB_EXTRAS[8] = []
for L in LABS[5:]:
    if L["num"] == 8: U.claude_team(D)
    lab_block(L)
mark("t3sum")
cards(D, "Topic 3 · Summary", "Day 2: Video Team, Coordination and Governance", [
    ("A company", "Mission, goals, budget and a CEO you approved.", "building"),
    ("A team", "Specialists with mandates, budgets, secrets and an independent auditor.", "users"),
    ("Delivery", "A Claude Code video team and a repeatable routine, independently audited.", "rocket"),
    ("Governance", "Costs, audit trail, scorecard, interventions and a Board report.", "gavel")],
    cols=4, dark=True)

# ====================================================================== CLOSE
mark("wrap")
section(D, "Wrap-up", "Course Summary & Next Steps", ["Key takeaways", "Practice exam", "Assessment", "Digital attendance"])
cards(D, "Wrap-up", "Summary & Q&A", [
    ("Topic 1", "Agents loop through perception, reasoning and action; the harness and the human make them reliable.", "brain"),
    ("Topic 2", "One Hermes Desktop agent produced the Google brief, Excel analysis, dashboard and PPT; Kanban extended it on Day 2.", "robot"),
    ("Topic 3", "Claude teammates produced the video; company governance exposed budgets, accountability and human gates.", "building"),
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
        ("tool", "Practical Performance (PP)", "Three tasks — ONE screenshot each from Lab 1 (Hermes agent), Lab 4 (multi-agent studio with its human gate) and Lab 7 (Paperclip org chart), plus written analysis. 1 hour, open book.", True)]):
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
circle(s, 10.4, -1.6, 4.6, ACC); circle(s, 11.2, 5.2, 3.2, TEAL)
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
