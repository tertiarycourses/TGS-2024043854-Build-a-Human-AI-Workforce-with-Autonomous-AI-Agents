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

s = D.new(); header(D, s, "Roadmap", "Course Outline", "You are the founder of Kopi Kaki Co. Three topics of agents help you start it; a bonus topic runs it as a one-person company.")
for i, tp in enumerate(C.TOPICS + [C.BONUS]):
    x = 0.6 + i * 3.08; bonus = tp is C.BONUS
    card(s, x, 2.45, 2.9, 4.35, fill=CHAR if bonus else WHITE)
    circle(s, x + 0.25, 2.65, 0.58, ACC); text(s, x + 0.25, 2.65, 0.58, 0.58, "B" if bonus else str(tp["num"]), 18, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
    text(s, x + 0.95, 2.72, 1.85, 0.45, "BONUS · OPTIONAL" if bonus else f"TOPIC {tp['num']}", 10, ACC, bold=True, autofit=False)
    text(s, x + 0.25, 3.35, 2.45, 1.05, tp["short"] if not bonus else "Paperclip one-person company", 15, WHITE if bonus else INK, bold=True, font=SERIF, minpt=11)
    text(s, x + 0.25, 4.4, 2.5, 2.3, "\n".join("•  " + it for it in tp["items"]), 10.5, SOFT if bonus else MUTED, lh=1.18, minpt=8.5)

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

s = D.new(); header(D, s, "Roadmap · Hands-on", "Six Activities and a Bonus, One Startup Story",
                    "Day 1: a CEO assistant, then one AI employee builds your website and deck. Day 2: bots, a Kanban team and crons — then an AI company.")
for i, L in enumerate(LABS):
    r, c = divmod(i, 4); x = 0.6 + c * 3.08; y = 2.3 + r * 2.07
    dark = L["day"] == 2
    card(s, x, y, 2.9, 1.97, fill=CHAR if dark else WHITE)
    text(s, x + 0.18, y + 0.14, 2.6, 0.3, f"{L['label'].upper()}  ·  DAY {L['day']}", 10, ACC, bold=True, autofit=False)
    icon(s, L["icon"], x + 0.18, y + 0.5, 0.48, fill=ACC if dark else TEAL)
    text(s, x + 0.8, y + 0.52, 1.95, 0.5, L["short"], 13.5, WHITE if dark else INK, bold=True, font=SERIF, minpt=10, lh=1.0)
    text(s, x + 0.18, y + 1.12, 2.55, 0.75, L["paradigm"], 10, SOFT if dark else MUTED, minpt=8, lh=1.05)
tip(D, s, "PP evidence: Task 1 = Lab 1 Muse/Dots · Task 2 = Lab 3 Hermes PPT · Task 3 = Lab 5 Kanban + video. The bonus is optional.", y=6.5)

s = D.new(); header(D, s, "Roadmap · Hands-on", "Lab Materials & the Lab Prompts Page",
                    "Everything you need is in the course repo: instructions PDF, mock data, skills and copy-ready prompts for every lab.")
shot = asset("screenshots", "prompts-page.png")
if os.path.exists(shot):
    picture(s, shot, 0.7, 2.5, maxw=6.6, maxh=4.25)
for i, (ic, t, d) in enumerate([
        ("download", "Get the labs", "github.com/tertiarycourses/TGS-2024043854-… → Code → Download ZIP. Unzip anywhere."),
        ("file", "Open the prompts page", "Double-click prompts/index.html — pick your lab, click Copy, paste into Hermes Desktop. No terminal needed."),
        ("folder", "Use the lab folder", "labs/labNN-…/ holds README, LAB-NN-Instructions.pdf, COPY-PROMPTS.txt and data/."),
        ("check", "Verify every result", "Each lab sheet ends with its checks — evidence, not vibes.")]):
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
                                 "You are the founder-CEO of this fictional Singapore kopi startup. Agents help you start it, from this activity to Day 2. All data is synthetic.")
    facts = [("store", "A startup, founded by you", "Heritage kopi, modern craft. Flagship in Tiong Bahru opens 1 Dec 2026; pop-ups and app pre-orders until then."),
             ("coffee", "Launch: Gula Melaka Cold Brew", "SGD 6.80 · 1 Dec 2026 · code SHIOK20 (20% off first app order, 1–14 Dec)."),
             ("target", "Campaign #ShiokColdBrew", "17 Nov – 14 Dec · SGD 15,000 · 2,500 pre-orders · 8% engagement · 40k views."),
             ("shield", "Rules that matter", "No health or halal claims · no competitor bashing · human APPROVE before anything is public.")]
    for i, (ic, t, d) in enumerate(facts):
        r, c = divmod(i, 2); x = 0.6 + c * 6.15; y = 2.55 + r * 2.05
        card(s, x, y, 5.95, 1.85, fill=K.PANEL, shadow=False); icon(s, ic, x + 0.28, y + 0.3, 0.6)
        text(s, x + 1.08, y + 0.28, 4.7, 0.5, t, 17, WHITE, bold=True, font=SERIF)
        text(s, x + 1.08, y + 0.82, 4.65, 0.95, d, 13, SOFT)

def _nb(t): return t.replace("`", "") if isinstance(t, str) else t
PROMPTS_URL = "https://tertiarycourses.github.io/TGS-2024043854-Build-a-Human-AI-Workforce-with-Autonomous-AI-Agents/prompts/"
def prompts_link(L): return f"{PROMPTS_URL}#lab-{L['code']}"
def prompts_button(s, L):
    """Orange 'Lab Prompts' button, top right of the lab slide; the whole button opens this lab on the prompts page."""
    from pptx.enum.shapes import MSO_SHAPE as _S
    b = K.box(s, 8.45, 0.14, 4.3, 0.56, fill=K.ACC_D, line=K.WHITE, lw=2.0, shape=_S.ROUNDED_RECTANGLE, radius=0.5, shadow=True)
    b.click_action.hyperlink.address = prompts_link(L)
    t = text(s, 8.45, 0.14, 4.3, 0.56, f"▶  COPY THE PROMPTS  ·  lab {L['code']}", 15, K.WHITE, bold=True, align="c", anchor="m", autofit=False)
    t.click_action.hyperlink.address = prompts_link(L)
def lab_block(L, n_prompts=2):
    kick = ("Bonus topic" if L["topic"] == 4 else f"Topic {L['topic']}") + f" · {L['label']}"
    k = "lab" + L["code"]
    if k not in MARK: mark(k)
    mark(k + "i")
    lab_intro(D, {k: _nb(v) if isinstance(v, str) else ([_nb(x) for x in v] if k == "deliverables" else v) for k, v in L.items()}, kick)
    s_i = D.prs.slides[-1]
    prompts_button(s_i, L)
    t = text(s_i, 0.6, 6.79, 12.1, 0.26, f"Copy every prompt for this lab ▸ {prompts_link(L)}", 11, K.TEAL, bold=True, autofit=False)
    t.click_action.hyperlink.address = prompts_link(L)   # shape-level link keeps the teal text colour
    if L["code"] == "01": meet_kopi(kick)   # Activity 1 runs on Kopi Kaki meetings
    lab_flow(D, dict(L, check=_nb(L["check"])), kick)
    for fn in LAB_EXTRAS.get(L["code"], []): fn(L, kick)
    pr = [st for st in L["steps"] if st.get("prompt")][:n_prompts]
    for st in pr:
        prompt(D, kick, st["title"], st["prompt"],
               side=[("chat", "Paste into", _nb(st.get("where", "Hermes chat"))),
                     ("check", "Expect", _nb(st.get("expect", "A saved output in your workspace."))),
                     ("hand", "You decide", _nb(st.get("decide") or L["human"]))],
               label=f"PROMPT  ·  click to copy it from the Lab Prompts page  ·  prompts/#lab-{L['code']}", url=prompts_link(L))
        prompts_button(D.prs.slides[-1], L)
    # No Checkpoint & Reflection slide: the trainer removed them from every lab (Lab 1 in v2.7, the rest in v3.5);
    # the checks stay in each lab's README/PDF and the Learner Guide.

def _cmd(L, kick, title, idx, side):
    st = L["steps"][idx]
    prompt(D, kick, title, st["cmd"], side=side, label="TERMINAL  ·  copy from the Lab Prompts page")

# --- Lab-specific concept / screenshot slides
LAB_EXTRAS["01"] = [lambda L,k: V23.muse_invite(D,k), lambda L,k: V23.dots_setup(D,k), lambda L,k: V23.wispr(D,k)]   # Activity 1A / 1B visual slides

U.swda(D)
V23.topic1(D,C,mark)
lab_block(LABS[0])   # Topic 1 ends with its lab (CEO assistant)
mark("lab1end")
for k in ("activity", "demo", "consolidation"): mark(k)   # legacy FG keys; v2.6 maps no slides to them

# ====================================================================== TOPIC 2 · YOUR FIRST AI EMPLOYEE
import slides_v34 as V34, slides_v34_t2 as T2
LAB = {L["code"]: L for L in LABS}
T2S = {**U.office(D), **V23.office_extra(D)}   # reuse two reviewed concept slides (skill correction; content vs layout errors)
mark("t2")
T2.open_(D, C)
table(D, "The course scenario", "The Kopi Kaki Company Pack (data/ in every lab)", ["File", "What it is", "Used in"],
      [("AGENTS.md", "Who Kopi Kaki is and the rules; Hermes loads it from the folder", "Every Hermes lab"),
       ("brand-guide.md · campaign-brief.md", "Voice, colours, formats · product, offer, KPIs, timeline", "Every Hermes lab"),
       ("compliance-rules.md · video-qa-checklist.md", "C1–C10 brand-safety rules · V1–V9 video checks", "Labs 2–5, bonus"),
       ("customer-reviews.csv · competitors.csv", "60 pop-up tasting reviews · 6 fictional competitors", "Setup, Labs 2–4"),
       ("product-catalogue.csv", "Menu and prices", "Labs 2–5"),
       ("skills/ · souls/ · tasks/ · tools/", "Reviewed skills, bot role files, Kanban task briefs, small tools", "Setup, Labs 3–6")],
      colw=[4.0, 5.6, 2.5], size=11.5)
# Topic 2 order (trainer, v3.6): what an agent is -> what Hermes is -> install -> provider and model -> Telegram
#   -> tools and skills (the difference; Gmail, web design, PPTX; Firecrawl kept for Topic 3) -> activities (website, PPT)
V23.agent_components(D, "Topic 2 · What is an AI agent?")   # moved from Topic 1
T2.what_is_hermes(D); T2.desktop(D); T2.folder(D); T2.model(D); T2.telegram(D)
mark("t2b"); T2.voice(D); V23.tools_vs_skills(D, "Topic 2 · Tools and skills")   # moved from Topic 1
T2.tools(D); T2.skills(D, T2S); T2.firecrawl(D)
mark("t2c"); T2.gmail(D); T2.cron(D); T2.web_skills(D); T2.pptx_skill(D)
lab_block(LAB["S2"], 2)
mark("lab02"); T2.website(D); lab_block(LAB["02"], 3)
mark("lab03"); T2.deck(D, T2S); lab_block(LAB["03"])
mark("t2close"); mark("day2")
# ====================================================================== TOPIC 3 · YOUR AI MARKETING TEAMS
mark("t3")
V34.topic3_open(D, C)
V34.multi_intro(D)   # general introduction to multiple agents + the five things every agent owns
V34.hub_spoke(D); V34.comm_flow(D)   # trainer screenshots (v3.5 hand edit): hub-and-spoke
V34.each_can(D); V34.handoff(D)   # trainer-added v3.3 slides, recreated natively
V34.decomposition(D); V34.framework(D); V34.subagents(D)   # trainer screenshots (v3.5): task decomposition, subagents
V34.bots_and_groups(D)   # Part A: hire bots with New Agent; group chats (LP row)
mark("lab04"); V34.social_team(D); V34.activity4_team(D); lab_block(LAB["04"], 3)
mark("lab05"); V34.video_tools(D); V34.kanban_board(D); V34.video_team(D); lab_block(LAB["05"], 3)
mark("lab06"); V34.crons_week(D); lab_block(LAB["06"], 2)
mark("t3b"); V34.security(D); V34.grounding(D); V34.evaluation(D)   # Part B: security, RAG, metrics (LP row)
mark("t3sum")
# ====================================================================== BONUS · PAPERCLIP (optional)
V34.bonus(D, C, mark); lab_block(LAB["B"], 3)
mark("bonusend")

mark("wrap")
section(D, "Wrap-up", "Course Summary & Next Steps", ["What you can now do", "Assessment", "Digital attendance"])
cards(D, "Wrap-up", "Summary & Q&A", [
    ("Topic 1", "An always-on CEO assistant checked your schedule and drafted your email; the harness and the human make agents reliable.", "brain"),
    ("Topic 2", "One Hermes agent — Mia — got a model, Telegram, voice, tools, skills, web search, Gmail and a schedule, all from one app, then built the website and the pitch deck.", "robot"),
    ("Topic 3", "Five bots in a group chat wrote the posts, a Kanban team made the video, and crons now start both every week; you approved everything. Bonus: Paperclip ran it as a company.", "building"),
    ("Your workforce", "Decide per task: agent, agent team or human — and where the human approves.", "handshake")],
    cols=4)
rows(D, "Wrap-up", "Continue Building Your Human–AI Workforce", [
    ("server", "Run 24/7", "Paid Nous Portal plans include one cloud-hosted agent, so scheduled jobs and Telegram keep running when your laptop sleeps."),
    ("puzzle", "Codify your SOPs", "Turn your team's checklists into SKILL.md skills and agent instructions."),
    ("shield", "Govern from day one", "Budgets, approval gates, audit trail — follow IMDA's agentic AI framework."),
    ("chart", "Measure", "Track cycle time, revisions, cost per deliverable and quality before you scale.")], dark=True)
# Practice Exam slide removed at the trainer’s request (v3.6, 1 Nov 2026).
mark("assess")
s = D.new(); header(D, s, "Assessment", "Final Assessment")
for i, (ic, t, d, dark) in enumerate([
        ("pen", "Written Assessment (WA)", "Short-Answer Questions — 1 hour, open book. Six questions on the knowledge from Topics 1–3.", False),
        ("tool", "Practical Performance (PP)", "Three tasks — Task 1: ONE Muse or Dots screenshot (Activity 1). Task 2: ONE Hermes PPT screenshot (Activity 3). Task 3: TWO screenshots, the Kanban board and the video (Activity 5). Written analysis; 1 hour, open book.", True)]):
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
