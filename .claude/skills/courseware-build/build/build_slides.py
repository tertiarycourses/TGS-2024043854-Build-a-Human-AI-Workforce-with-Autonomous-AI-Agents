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
tip(D, s, "Day 1 = Hermes Agent (single → multi-agent).  Day 2 = Paperclip (a governed company of agents).", y=6.5)

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
mark("t1a")
T1 = C.TOPICS[0]
section(D, "Topic 1", T1["title"], T1["items"])

timeline(D, "Topic 1 · History of AI", "A Brief History of AI — From Rules to Learning", [
    ("Turing test", "1950", "Turing asks \"Can machines think?\" and proposes the imitation game."),
    ("AI is named", "1956", "Dartmouth workshop coins \"artificial intelligence\"."),
    ("Expert systems", "1970s", "Hand-written rules (MYCIN, XCON) — brittle, costly to update."),
    ("Deep Blue", "1997", "IBM beats Kasparov at chess with brute-force search."),
    ("Deep learning", "2012", "AlexNet wins ImageNet — GPUs + big data."),
    ("AlphaGo", "2016", "Deep + reinforcement learning beats Lee Sedol 4–1."),
    ("Transformer", "2017", "\"Attention Is All You Need\" — the architecture behind every LLM.")],
    foot="Rules → Search → Learning → Language: each era moved more of the 'how' from humans into the machine.")
timeline(D, "Topic 1 · History of AI", "A Brief History of AI, 2022–2026 — From Chat to Agents", [
    ("ChatGPT", "2022", "Launches 30 Nov 2022 — LLMs go mainstream. ReAct shows LLMs can reason and act."),
    ("Prompt Engineering", "2023", "GPT-4 (Mar 2023); results depend on how you word the prompt."),
    ("Tools & MCP", "2024", "Model Context Protocol (Nov 2024) standardises how agents reach tools and data."),
    ("Context Engineering", "2025", "Claude Code & Codex coding agents; results depend on the context you curate."),
    ("Harness Engineering", "2026", "The environment around the model is engineered: loop, tools, memory, checks, guardrails."),
    ("AI Agents", "2026", "Always-on agents work 24/7 — OpenClaw, Hermes Agent, Paperclip, Dots, Muse.")],
    foot="From wording one prompt → curating context → engineering the harness → agents that work around the clock.")
cards(D, "Topic 1 · History of AI", "Prompt, Context & Harness Engineering", [
    ("Prompt engineering", "Craft the instruction. One request, one answer. Quality depends on wording.\nExample: \"Write a caption for our new drink.\"", "pen"),
    ("Context engineering", "Curate what the model sees: brand guide, brief, data, memory, tool results — and nothing that wastes the window.\nExample: AGENTS.md + campaign-brief.md loaded every session.", "layers"),
    ("Harness engineering", "Design the whole environment: the loop, tools, memory, skills, verification, guardrails and human gates — so the agent does reliable long-running work.\nExample: Lab 4's five-agent studio with an auditor and an approval gate.", "gear")],
    cols=3, hi=(2,), sub="Each layer contains the one before it.", desc_pt=13)

cards(D, "Topic 1 · History of AI", "The Range of AI Applications Today", [
    ("Generative AI / LLMs", "Chatbots, writing, coding and summarising. Capability: understand and generate natural language, code and images.", "chat"),
    ("Computer vision", "Defect detection, medical imaging, product search. Capability: recognise and classify what is in images and video.", "camera"),
    ("Predictive analytics & ML", "Demand forecasting, fraud scoring, recommendations. Capability: learn patterns in data to predict outcomes.", "trend"),
    ("Speech & multimodal", "Voice assistants, transcription, text-to-speech. Capability: convert between speech, text and other media.", "phone"),
    ("Scientific discovery", "AlphaFold, AI co-scientist, AlphaEvolve. Capability: generate and rank hypotheses and designs for experts to test.", "flask"),
    ("Autonomous AI agents", "Hermes, Paperclip, OpenAI Dots, AgentSea. Capability: pursue a goal with tools, memory and planning — with humans in the loop.", "robot")],
    cols=3, sub="Every industry uses several of these together — agents increasingly orchestrate the others.", desc_pt=13)
cards(D, "Topic 1 · AI agents vs agentic AI", "What Is an AI Agent?", [
    ("Goal-directed", "Given a goal, it decides the steps itself instead of waiting for each instruction.", "target"),
    ("Uses tools", "Searches the web, reads files, writes documents, calls APIs and MCP servers.", "tool"),
    ("Loops until done", "Acts, observes the result, checks it, and tries again.", "loop"),
    ("Remembers", "Keeps context in the session and long-term memory across sessions.", "memory"),
    ("Bounded", "Works inside permissions, budgets and approval gates set by humans.", "shield"),
    ("Accountable human", "A person owns the outcome — the agent recommends or acts on their behalf.", "user")],
    cols=3, sub="\"Autonomous software entities engineered for goal-directed task execution within bounded digital environments\" — Sapkota et al., 2025")
table(D, "Topic 1 · AI agents vs agentic AI", "AI Agents vs Agentic AI",
      ["Dimension", "AI Agent", "Agentic AI"],
      [("Scope", "One specific, well-defined task", "A complex, multi-step goal or workflow"),
       ("Architecture", "One LLM + tools: perceive → reason → act", "Several specialised agents + an orchestrator"),
       ("Flow", "User → Agent → Tool", "User → System → Agent 1 → Agent 2 → …"),
       ("Memory", "Session context, optional cache", "Shared, persistent memory across stages"),
       ("Planning", "Single-step, reactive", "Multi-step, proactive goal decomposition"),
       ("Coordination", "Works alone", "Hierarchical or decentralised hand-offs"),
       ("Examples", "Support bot, email triage, research agent (Lab 1)", "Video studio (Lab 4), AI company (Labs 6–10)"),
       ("Main risks", "Hallucination, brittle prompts", "Error propagation, misalignment, governance")],
      colw=[2.0, 5.0, 5.1], size=11.5, hi_col=2,
      sub="Source: Sapkota, Roumeliotis & Karkee, \"AI Agents vs. Agentic AI\", Information Fusion 2025 (arXiv 2505.10468).")
compare(D, "Topic 1 · AI agents vs agentic AI", "An Analogy: the Smart Home",
        ("AI Agent — a smart thermostat", "gauge", ["Holds the room at 21°C", "One goal, one device, clear rules",
                                                    "Reacts to the temperature it senses", "Kopi Kaki: Mia writes a research brief (Lab 1)"]),
        ("Agentic AI — the coordinated home", "network", ["Weather, energy-price, schedule, appliance and security agents work together",
                                                          "Pre-cools with solar before a heatwave hits at peak price",
                                                          "Plans ahead, hands off, adapts the goal",
                                                          "Kopi Kaki: a 5-agent studio ships a video (Lab 4)"]),
        tipt="Same LLMs underneath — the difference is orchestration, memory and coordination.")

loop(D, "Topic 1 · The agentic loop", "The Agentic Loop", [
    ("search", "1. Gather context", "Read files and memory, search the web, call tools to understand the task."),
    ("bolt", "2. Take action", "Write files, run commands, call MCP tools and APIs to make progress."),
    ("check", "3. Verify work", "Check the result — tests, a checklist, a screenshot, a second agent."),
    ("loop", "4. Repeat", "Feed results back as new context and loop until the goal is met.")],
    sub="Every agent task runs the same repeating cycle. ReAct (2022) calls it Thought → Action → Observation.",
    foot="Goal in → context → action → verification → repeat → goal met")
rows(D, "Topic 1 · The agentic loop", "The Loop in Action — Mia's Research Brief (Lab 1)", [
    ("target", "Goal", "\"Write a research brief with three evidence-backed campaign angles.\""),
    ("search", "Gather context", "Loads AGENTS.md and memory, reads 60 reviews, searches 2026 cold-brew trends."),
    ("brain", "Reason & plan", "Groups reviews into themes, compares competitors, drafts three angles."),
    ("bolt", "Act", "Writes review-insights.md and research-brief.md with citations."),
    ("check", "Verify", "Checks each claim has a review ID or URL; flags anything unverified."),
    ("user", "Human checkpoint", "You challenge a claim and choose the angle — Mia saves it to long-term memory.")], dark=True)
rows(D, "Topic 1 · The agentic loop", "Why the Loop Matters", [
    ("target", "Give direction, not micro-steps", "State the goal, constraints and definition of done; let the loop find the steps."),
    ("check", "Verification is everything", "An agent is only as good as its ability to check its own work — checklists, auditors, tests."),
    ("hand", "Steer mid-loop", "Review plans and drafts early; send work back with specific feedback rather than waiting for a wrong final answer."),
    ("layers", "Context is the fuel", "What the agent can see decides what it can do — that is why we give it AGENTS.md, skills and memory.")], dark=True)

s = D.new(); header(D, s, "Topic 1 · Harness engineering", "What Is Harness Engineering?",
                    "Agent = Model + Harness. The harness is everything around the model that turns it into a dependable worker.")
card(s, 0.6, 2.5, 6.4, 4.25)
text(s, 0.9, 2.7, 5.9, 0.45, "A harness provides", 17, INK, bold=True, font=SERIF)
text(s, 0.9, 3.25, 5.9, 3.4, "•  The agentic loop (gather → act → verify → repeat)\n•  Tools and MCP connections\n•  Context & memory management\n•  Skills (procedural know-how)\n•  Verification — checklists, tests, auditor agents\n•  Guardrails — permissions, budgets, approval gates\n•  Sub-agents and orchestration\n•  Observability — logs, costs, audit trail", 13.5, MUTED, lh=1.22)
card(s, 7.2, 2.5, 5.5, 4.25, fill=CHAR)
text(s, 7.5, 2.7, 5.0, 0.45, "Who named it", 17, WHITE, bold=True, font=SERIF)
text(s, 7.5, 3.25, 4.95, 3.4, "Nov 2025 — Anthropic: \"Effective harnesses for long-running agents\".\n\nFeb 2026 — Mitchell Hashimoto: \"Engineer the harness\" — every time an agent makes a mistake, fix the environment so it never happens again.\n\nFeb 2026 — OpenAI Codex team: ~1M lines of code, ~1,500 PRs, no hand-written code. \"Humans steer. Agents execute.\"", 12.5, SOFT, lh=1.2)
cards(D, "Topic 1 · Harness engineering", "The Harness in This Course", [
    ("Context: AGENTS.md", "Company facts and rules loaded every session (Lab 1).", "file"),
    ("Memory", "MEMORY.md / USER.md recall decisions across sessions (Lab 1).", "memory"),
    ("Skills", "kopi-brand-voice, campaign planner, compliance audit (Labs 2, 4).", "puzzle"),
    ("Verification", "Self-check tables, auditor agent, verifier in the swarm (Labs 2, 4, 5).", "eyecheck"),
    ("Guardrails", "APPROVE on Telegram, blocked publish task, Board gates (Labs 3, 4, 7–9).", "shield"),
    ("Orchestration", "Profiles + Kanban, swarms, Paperclip org chart (Labs 4–10).", "org"),
    ("Scheduling", "Cron jobs and Paperclip routines (Labs 3, 5, 9).", "clock"),
    ("Observability", "Kanban history, costs and the audit log (Labs 5, 10).", "history")],
    cols=4, tipt="When an agent gets it wrong, improve the harness (instructions, skills, gates) — don't just re-prompt.")

# ---- brain / perception / action
s = D.new(); header(D, s, "Topic 1 · How an agent works", "The Agent Framework: Perception · Brain · Action",
                    "From the survey \"The Rise and Potential of LLM-Based Agents\" (Xi et al., Fudan University, arXiv 2309.07864).")
cols = [(0.6, "Perception", "eye", "Sense the world", TEAL,
         ["Multimodal input — text, image, audio, video", "Environment interaction — tools, web, files", "Information retrieval — search, RAG, memory"],
         "From data to information"),
        (4.75, "Brain", "brain", "Core cognition & decisions", PLUM,
         ["Knowledge — pre-trained, domain, common sense", "Memory — short-term & long-term", "Reasoning — logic, reflection, self-correction", "Planning — decompose, set goals, adapt"],
         "From understanding to decisions"),
        (8.9, "Action", "hand", "Change the world", ACC_D,
         ["Task execution — code, tools, operations", "Environment feedback — results, rewards", "Behaviour optimisation — learn and evolve"],
         "From decisions to action")]
for x, t, ic, sub, col, items, foot in cols:
    card(s, x, 2.45, 3.85, 4.35)
    icon(s, ic, x + 0.25, 2.65, 0.66, fill=col)
    text(s, x + 1.05, 2.62, 2.7, 0.45, t, 20, INK, bold=True, font=SERIF)
    text(s, x + 1.05, 3.05, 2.7, 0.35, sub, 11.5, MUTED)
    text(s, x + 0.3, 3.6, 3.3, 2.5, "\n".join("•  " + it for it in items), 12.5, MUTED, lh=1.25)
    box(s, x + 0.25, 6.2, 3.35, 0.42, fill=col, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2)
    text(s, x + 0.25, 6.2, 3.35, 0.42, foot, 12, WHITE, bold=True, align="c", anchor="m", autofit=False)
for x in (4.47, 8.62):
    line(s, x, 4.6, x + 0.25, 4.6, ACC, 2.5, arrow=True)
cards(D, "Topic 1 · How an agent works", "Inside the Brain", [
    ("Knowledge", "Pre-trained and domain knowledge, common sense and self-knowledge. Can be stale → ground it with RAG.", "book"),
    ("Memory", "Short-term (the context window) and long-term (notes, history, skills). Retrieved when relevant.", "memory"),
    ("Reasoning", "Logical and step-by-step reasoning, reflection and self-correction on complex problems.", "brain"),
    ("Planning", "Break tasks into sub-goals, set targets, revise the plan after feedback, improve over time.", "list")],
    cols=4, sub="The LLM is the control centre: it turns what the agent perceives into decisions.",
    tipt="Hermes adds natural-language interaction and transfer: one agent, every channel, new skills learned on the job.")
s = D.new(dark=True); header(D, s, "Topic 1 · How an agent works", "Perception → Decision → Action: a Closed Loop")
left = [("eye", "Multimodal perception"), ("globe", "Environment interaction"), ("memory", "Information retrieval"), ("map", "World modelling")]
right = [("tool", "Task execution"), ("loop", "Environment feedback"), ("trend", "Behaviour optimisation"), ("sparkles", "Autonomous evolution")]
card(s, 0.6, 1.95, 4.9, 4.4, fill=K.PANEL, shadow=False); card(s, 7.8, 1.95, 4.9, 4.4, fill=K.PANEL, shadow=False)
text(s, 0.9, 2.1, 4.3, 0.45, "Perception", 18, ACC, bold=True, font=SERIF)
text(s, 8.1, 2.1, 4.3, 0.45, "Action", 18, ACC, bold=True, font=SERIF)
for i, ((ic1, t1), (ic2, t2)) in enumerate(zip(left, right)):
    y = 2.75 + i * 0.86
    icon(s, ic1, 0.95, y, 0.5, fill=TEAL); text(s, 1.6, y + 0.05, 3.7, 0.42, t1, 15, WHITE, font=SERIF, bold=True)
    icon(s, ic2, 8.15, y, 0.5); text(s, 8.8, y + 0.05, 3.7, 0.42, t2, 15, WHITE, font=SERIF, bold=True)
    line(s, 5.6, y + 0.25, 7.7, y + 0.25, ACC, 1.75, arrow=True)
circle(s, 5.85, 3.25, 1.6, PLUM); text(s, 5.85, 3.25, 1.6, 1.6, "Brain\ndecides", 15, WHITE, bold=True, font=SERIF, align="c", anchor="m", autofit=False)
text(s, 0.6, 6.5, 12.1, 0.42, "Perception → decision → action → feedback → new perception. In Lab 3 the feedback is your Telegram reply.", 13, SOFT, align="c")

table(D, "Topic 1 · Memory", "Memory: Short-Term and Long-Term",
      ["Memory type", "Human analogy", "What the agent keeps", "Where you will see it"],
      [("Short-term / working", "What you're thinking about now", "The context window: instructions, chat, tool results, current plan", "Every Hermes session; compaction when it fills"),
       ("Episodic (long-term)", "\"What happened\"", "Past sessions, actions and outcomes", "Hermes session search; Kanban & Paperclip history"),
       ("Semantic (long-term)", "\"Facts I know\"", "Facts about the company and user; knowledge bases (RAG)", "MEMORY.md / USER.md; brand guide in company knowledge"),
       ("Procedural (long-term)", "\"How to do things\"", "Skills, rules, workflows", "SKILL.md skills; AGENTS.md; agent instructions")],
      colw=[2.3, 2.4, 4.0, 3.4], size=11.5,
      sub="Framework: CoALA (Sumers et al., 2023). Short-term memory is limited and resets; long-term memory persists and is retrieved when relevant.",
      tipt="Hermes loads memory at session start — after it saves something, start a new session (/new) to see it recalled.")
cards(D, "Topic 1 · Memory", "How Agents Remember — Retrieval & Reflection", [
    ("Retrieve by relevance", "Pull the memories that score highest for recency, importance and relevance (Generative Agents, 2023).", "search"),
    ("RAG", "Retrieve from a curated, current knowledge base before answering — grounded, auditable answers.", "book"),
    ("Just-in-time context", "Keep pointers (file paths, links) and load the data only when needed — saves the window.", "file"),
    ("Reflection", "After a failure, write a lesson to memory and do better next time (Reflexion, 2023).", "lightbulb")],
    cols=2, tipt="Lab 2 challenge: turn your review feedback into a permanent skill update — reflection by design.")
compare(D, "Topic 1 · Memory", "RAG Agent vs a Standard LLM Assistant",
        ("RAG agent", "book", ["Retrieves from a curated, current corpus before generating", "Grounded answers with citations — less hallucination",
                                "Quality depends on corpus freshness, chunking and retrieval/memory configuration", "Needs a maintenance process: re-index, review sources"]),
        ("Standard LLM assistant", "chat", ["Answers from training data alone — fastest to deploy", "No live company data; knowledge can be stale",
                                             "Harder to audit where an answer came from", "Lower maintenance, higher risk on facts"]),
        tipt="Evaluate both on accuracy, relevance, latency, cost and maintenance effort.")

s = D.new(); header(D, s, "Topic 1 · World models", "World Models — Predicting the Next State of the World",
                    "LLMs predict the next word; world models predict how the world changes after an action — so an agent can plan before it acts.")
card(s, 0.6, 2.5, 4.6, 4.25, fill=CHAR)
text(s, 0.9, 2.7, 4.0, 0.45, "Why they matter", 17, WHITE, bold=True, font=SERIF)
text(s, 0.9, 3.25, 4.05, 3.4, "•  Plan and simulate \"what if I do X?\" before costly or irreversible actions\n•  Physical AI — robots and vehicles need intuitive physics\n•  Train agents safely in generated worlds\n•  Ground the agent in how the world really behaves", 13, SOFT, lh=1.25)
wm = [("NVIDIA Cosmos", "Jan 2025", "World foundation models for robots and autonomous vehicles."),
      ("Meta V-JEPA 2", "Jun 2025", "Video world model; zero-shot robot pick-and-place."),
      ("DeepMind Genie 3", "Aug 2025", "Interactive worlds from text at 24 fps, 720p."),
      ("World Labs Marble", "Nov 2025", "Persistent, editable 3D worlds from text or images."),
      ("AMI Labs (LeCun)", "Mar 2026", "US$1.03B raised to build JEPA-based world models.")]
for i, (t, d, desc) in enumerate(wm):
    y = 2.5 + i * 0.86; card(s, 5.45, y, 7.25, 0.76)
    text(s, 5.65, y + 0.08, 2.45, 0.6, t, 13.5, INK, bold=True, font=SERIF, anchor="m")
    text(s, 8.1, y + 0.08, 1.15, 0.6, d, 11.5, ACC, bold=True, anchor="m")
    text(s, 9.25, y + 0.08, 3.3, 0.62, desc, 11, MUTED, anchor="m", minpt=8.5)

# ---- paradigms
mark("t1b")
cards(D, "Topic 1 · Paradigms", "Three Paradigms: Single Agent → Multi-Agent → Human–Agent Collaboration", [
    ("Single agent", "One agent completes a task end to end.\n•  Task-oriented — follows instructions\n•  Innovation-oriented — research & discovery\n•  Lifecycle-oriented — learns skills over time\nLabs 1–2: Mia researches and runs a campaign.", "robot"),
    ("Multi-agent", "Several agents collaborate or compete.\n•  Cooperative — ordered (SOP pipeline) or disordered (discussion, voting)\n•  Adversarial — debate to improve answers\nLabs 4–5: video studio pipeline and analysis swarm.", "users"),
    ("Human–agent collaboration", "People and agents share the work.\n•  Instructor–executor — humans instruct and give feedback\n•  Equal partnership — agents as peers\nLab 3 and Day 2: APPROVE, review and Board gates.", "handshake")],
    cols=3, hi=(2,), sub="Xi et al. (2023): from individual agents to collaboration and agent society.", desc_pt=12.5)
hub(D, "Topic 1 · Paradigms", "Multi-Agent Patterns You Will Build", "Orchestrator\n(Kanban / CEO)", [
    ("search", "Researcher", "Finds facts and hooks, cites sources"),
    ("pen", "Scriptwriter", "Turns research into a script"),
    ("film", "Producer", "Renders the video"),
    ("eyecheck", "Auditor", "Checks rules; can send work back"),
    ("send", "Publisher", "Acts only after human approval"),
    ("user", "Human", "Sets goals, approves, owns the outcome")],
    sub="Ordered pipeline (Lab 4), parallel swarm with a verifier (Lab 5), and an org chart with a Board (Labs 6–10).",
    foot="Without rules, multi-agent chatter can amplify small hallucinations — add verifiers and human checkpoints.")
compare(D, "Topic 1 · Human–agent collaboration", "Two Ways Humans and Agents Work Together",
        ("Instructor–executor", "user", ["The human sets goals, gives instructions and feedback", "Feedback can be quantitative (scores) or qualitative (critique)",
                                          "Agent executes and improves from feedback", "Labs: APPROVE / EDIT on Telegram; Board revision requests"]),
        ("Equal partnership", "handshake", ["Agent participates as a peer — proposes, negotiates, challenges", "Empathetic communicator or human-level participant",
                                             "Human remains accountable for decisions", "Labs: the CEO agent proposes the team; you approve or push back"]),
        tipt="Why keep humans in? They fill gaps in privacy, ethics, judgement and data — and agents learn through interaction.")
table(D, "Topic 1 · Human–agent collaboration", "Levels of Autonomy — Pick Per Task, Not Per Agent",
      ["Level", "Your role", "What the agent does", "Example in this course"],
      [("L1", "Operator", "Acts only when you invoke it for a subtask", "Asking Mia a one-off question"),
       ("L2", "Collaborator", "Plans and works with you; you can take over anytime", "Lab 2 campaign drafting with your feedback"),
       ("L3", "Consultant", "Does most of the work; asks for your expertise", "Lab 1 research brief, Lab 7 hiring plan"),
       ("L4", "Approver", "Asks only at high-risk steps or required approvals", "Lab 3 APPROVE gate, Lab 9 weekly routine"),
       ("L5", "Observer", "Works on its own; you monitor with an off-switch", "Weekly report cron (Lab 5)")],
      colw=[0.9, 1.8, 4.6, 4.8], size=12,
      sub="Feng, McDonald & Zhang (2025): autonomy is a design decision, separate from capability.")
table(D, "Topic 1 · Human–agent collaboration", "Human-in-the-Loop vs Human-on-the-Loop",
      ["Pattern", "Definition", "Use it for", "Course example"],
      [("Human-in-the-loop", "A person approves BEFORE the action happens", "Irreversible, public, regulated actions — publishing, payments, refunds", "Telegram APPROVE (Lab 3), blocked publish task (Lab 4), Board gates"),
       ("Human-on-the-loop", "The agent acts; a person monitors and can intervene", "High-volume, reversible work — triage, drafts, analysis", "Weekly report cron (Lab 5), Paperclip costs & activity (Lab 10)"),
       ("Human-out-of-the-loop", "Fully autonomous, no real-time oversight", "Only low-risk, bounded, reversible tasks", "Scheduled data refresh")],
      colw=[2.2, 3.3, 3.4, 3.2], size=12,
      tipt="Keep humans IN the loop for irreversible actions and ON the loop for reversible volume. The human is always accountable.")
rows(D, "Topic 1 · Agent society", "From Individuals to an Agent Society", [
    ("user", "Individual behaviour", "Each agent learns and adapts — Hermes writes new skills after hard tasks."),
    ("users", "Group interaction", "Agents communicate and coordinate — Kanban hand-offs, swarms, CEO delegation."),
    ("star", "Personality", "Roles and values in SOUL.md and instructions shape how each agent behaves."),
    ("network", "Social emergence", "Collective intelligence and new behaviours appear at scale — plus new risks (groupthink, bias)."),
    ("building", "Agent-as-a-Service", "Agents offered as a workforce you hire and govern — the idea behind Paperclip.")], dark=True)

# ---- market
table(D, "Topic 1 · The 2026 agent market", "Autonomous Agents in the Market (Oct 2026) — 1/2",
      ["Product", "Vendor · launch", "Type", "Runs where", "Human-in-the-loop"],
      [("OpenClaw", "OpenClaw Foundation · Nov 2025 (renamed Jan 2026)", "Open source personal agent", "Your machine; chat apps", "DM pairing; optional sandbox"),
       ("Hermes Agent", "Nous Research · ~Feb 2026", "Open source, self-improving agent", "Local, VPS, desktop; 15+ channels", "Approval modes; allow-lists"),
       ("Paperclip", "Paperclip Labs · Mar 2026", "Open source company of agents", "Self-hosted (Node / Docker)", "Board approvals; budgets auto-pause"),
       ("OpenAI Dots", "OpenAI · 29 Sep 2026", "Always-on agent with its own cloud computer", "ChatGPT, Slack, Teams", "Custom rules: allow / approve / block"),
       ("Meta Muse", "Meta · 8 Sep 2026 (US)", "Personal agent for life admin", "App, web, WhatsApp", "Confirms sensitive actions; Sentinel guard"),
       ("Block Buzz", "Block · 21 Jul 2026", "Open workspace for humans + agents", "Self-host or buzz.xyz", "Agent identities & permissions"),
       ("Manus Cue", "Manus · 28 Sep 2026", "Agents with email, phone, wallet", "Web, desktop, mobile", "Budgets; you make the final call")],
      colw=[1.6, 3.0, 2.8, 2.4, 2.6], size=10.5, hi_col=0)
table(D, "Topic 1 · The 2026 agent market", "Autonomous Agents in the Market (Oct 2026) — 2/2",
      ["Product", "Vendor · launch", "Type", "Runs where", "Human-in-the-loop"],
      [("Claude Cowork / Claude Code", "Anthropic · 2025–2026", "Desktop & coding agents with sub-agents", "Desktop, terminal, cloud", "Manual / Auto / Skip permission modes"),
       ("OpenAI Codex", "OpenAI · May 2025; Cloud Sep 2026", "Parallel coding agents", "CLI, IDE, cloud", "Review before merge; sandboxes"),
       ("Gemini Enterprise agents", "Google · 8 Oct 2026", "Sub-agents + persistent 'coworker' agents", "Workspace, M365, Slack", "Agent identity, gateway, spend caps"),
       ("Microsoft Agent 365", "Microsoft · May 2026", "Governance control plane for many agents", "M365 admin, Entra, Purview", "Registry, access control, DLP"),
       ("Perplexity Computer", "Perplexity · Feb 2026", "Multi-model orchestrator", "Cloud", "Not confirmed")],
      colw=[2.3, 2.9, 2.9, 2.2, 2.1], size=11, hi_col=0,
      tipt="Sources: vendor announcements and repos (verified Oct 2026). Products move fast — check before you buy.")
cards(D, "Topic 1 · The 2026 agent market", "How to Read the Market", [
    ("Personal agents", "One agent working for one person — OpenClaw, Hermes Agent, Meta Muse, OpenAI Dots, Manus Cue.", "user"),
    ("Workspaces & companies", "Many agents and humans with roles — Paperclip, Block Buzz, Gemini coworker agents.", "building"),
    ("Governance layers", "Registries, identities, budgets and policy across agents — Microsoft Agent 365, Paperclip Board.", "shield"),
    ("Open vs closed", "Open source = self-host, inspect, own your data. Closed = convenience, managed security, vendor lock-in.", "scale")],
    cols=2, tipt="This course: Hermes Agent (an employee that learns) + Paperclip (the company you govern) — both open source.")
image(D, "Topic 1 · Singapore in focus", "Singapore: 12,000+ AI Agents in Public Healthcare", asset("screenshots", "st-agentsea.png"),
      side=[("hospital", "AgentSea", "Synapxe + AWS agentic AI platform for 80,000+ public healthcare professionals — launched end-May 2026."),
            ("users", "12,000+ agents", "Created by staff in natural language, little or no coding; 300+ shared for reuse."),
            ("heart", "Real impact", "NHCS cardiologist halved pre-consultation prep; KKH agent generates daily rosters."),
            ("shield", "Guardrails", "Patient-data protections built in — \"not replaced the need for verification or my own clinical assessment\".")],
      caption="\"We are moving from AI as assistant to AI as actor.\" — SMS Tan Kiat How, HIMSS26 APAC, 24 Aug 2026",
      src="Source: The Straits Times, \"New platform to create AI agents available to all public healthcare professionals\", Zhaki Abdullah, 24 Aug 2026.")
cards(D, "Topic 1 · Singapore in focus", "Singapore's Agentic AI Playbook", [
    ("IMDA framework", "Model AI Governance Framework for Agentic AI — launched 22 Jan 2026 (Davos); updated v1.5 May 2026.", "gavel"),
    ("Four dimensions", "Bound risks upfront · meaningful human accountability · technical controls · end-user responsibility.", "list"),
    ("Public service", "GovTech AI Assistant Desk with an agent registry (owner and purpose of each agent) for ~150,000 officers.", "building"),
    ("Healthcare", "AgentSea plus MOH's AI in Healthcare Guidelines (AIHGle 2.0) — healthcare is a national AI mission.", "hospital")],
    cols=2, tipt="Course link: approval gates, budgets and audit logs (Labs 3, 7–10) are the 'human accountability' dimension in practice.")

# ---- use cases
table(D, "Topic 1 · Human–AI collaboration in action", "AI for Science — Agents Propose, Humans Decide",
      ["Use case", "What the agent does", "What the human does", "Result"],
      [("Google AI co-scientist (2025)", "Multi-agent system generates, debates and ranks hypotheses", "Sets the goal, picks hypotheses, runs wet-lab tests", "3 of 5 lab-tested leukaemia drug ideas worked"),
       ("Edison Kosmos (2025)", "Reads ~1,500 papers, writes ~42,000 lines of analysis code per run", "Sets objective, judges which findings matter", "79% of statements judged accurate"),
       ("Sakana AI Scientist (2025–26)", "Idea → code → experiments → paper → review", "Chooses the field, checks work, runs ethics review", "1 of 3 papers passed a workshop review")],
      colw=[2.5, 3.6, 3.2, 2.8], size=11.5)
table(D, "Topic 1 · Human–AI collaboration in action", "AI for Mathematics",
      ["Use case", "What the agent does", "What the human does", "Result"],
      [("AlphaProof + AlphaGeometry (2024)", "Searches formal proofs in Lean", "Formalises problems; graders score", "IMO silver standard, 28/42"),
       ("Gemini Deep Think (2025)", "Writes natural-language proofs in 4.5 h", "IMO coordinators grade and certify", "IMO gold, 35/42 (certified)"),
       ("AlphaEvolve (2025)", "Evolves programs scored by an evaluator", "Defines the problem and WRITES the evaluator", "Improved best-known results in ~20% of 50+ problems"),
       ("Terence Tao + AI (2025–26)", "Searches constructions; proposes proofs (Erdős problems)", "Chooses problems, checks and generalises", "Real wins — mostly 'cheap wins', says Tao")],
      colw=[2.7, 3.3, 3.3, 2.8], size=11.5)
table(D, "Topic 1 · Human–AI collaboration in action", "Drug Discovery & Biology",
      ["Use case", "What the AI does", "What the human does", "Status"],
      [("AlphaFold 3 (2024)", "Predicts structures of proteins, DNA, RNA and ligands", "Forms hypotheses, chooses targets, validates in the lab", "2024 Nobel Prize in Chemistry (AlphaFold)"),
       ("Insilico rentosertib (2025)", "Found the TNIK target and designed the molecule", "Clinicians ran the Phase 2a trial; regulators approved", "Nature Medicine, Jun 2025 — safety met"),
       ("Isomorphic Labs (2026)", "In-house AI drug-design engine", "Chemists, pharma partners, clinical teams", "US$2.1B raised; first trials targeted end-2026")],
      colw=[2.5, 3.5, 3.4, 2.7], size=11.5,
      tipt="Agents shorten discovery; humans still design the experiment, validate, and carry the clinical and ethical responsibility.")
table(D, "Topic 1 · Human–AI collaboration in action", "Business Functions",
      ["Function", "Agent does", "Human does", "Evidence"],
      [("Healthcare", "MAI-DxO: virtual panel orders tests step by step", "Clinician owns diagnosis and treatment", "85.5% on 304 NEJM cases (benchmark only)"),
       ("Finance", "Claude agents for trade accounting and client onboarding", "Staff review exceptions and approve", "Goldman Sachs + Anthropic, Feb 2026"),
       ("Software", "Codex writes code, tests, CI and docs", "Engineers steer, review and build feedback loops", "~1M lines, no hand-written code (OpenAI)"),
       ("Customer service", "Handles routine chats in 35+ languages", "Takes complex and sensitive cases", "Klarna re-prioritised human access in 2025"),
       ("Marketing", "Drafts, designs, schedules and reports campaigns", "Sets strategy, approves everything public", "Labs 2–5 and 8–9 in this course")],
      colw=[1.8, 3.8, 3.3, 3.2], size=11.5)
compare(D, "Topic 1 · Human–AI collaboration in action", "The Pattern Behind Every Success",
        ("The agent", "robot", ["Searches, generates, runs and checks — at scale", "Works 24/7 and in parallel", "Follows the rules it is given — exactly",
                                "Never owns the consequence"]),
        ("The human", "user", ["Sets the goal and defines 'good' (rubric, evaluator, tests)", "Approves consequential actions",
                               "Interprets meaning and context", "Owns accountability — always"]),
        tipt="Counter-evidence matters: a 2025 METR trial found experienced developers 19% SLOWER with early AI tools. The harness and the human make the difference.")
cards(D, "Topic 1 · Risks & governance", "Five Challenges for Trustworthy Agents", [
    ("Hallucination", "Confident but false facts → require citations and verifiers.", "alert"),
    ("Security risks", "Prompt injection, poisoned skills, leaked keys → least privilege, secrets, sandboxes.", "lock"),
    ("Explainability", "Why did it do that? → logs, Kanban history, audit trail.", "eye"),
    ("Data & bias", "Fairness, diversity, privacy (PDPA) → mask personal data, review outputs.", "scale"),
    ("Efficiency & cost", "Tokens and runs add up → budgets, cheap models for simple roles.", "coins")],
    cols=5, sub="Toward agents that are trustworthy, controllable and sustainable.", desc_pt=14)
cards(D, "Topic 1 · Risks & governance", "Five Principles of AI Agent Security", [
    ("Data control", "WHAT AI CAN SEE — classify data; give the agent only what it needs.", "eye"),
    ("Permission control", "WHAT AI CAN DO — least privilege; read before write; approve before delete.", "lock"),
    ("Human approval", "WHEN AI MUST ASK — gates for public, financial or irreversible actions.", "hand"),
    ("Monitoring & audit", "WHAT AI DID — logs, costs, activity trail; review regularly.", "history"),
    ("Kill switch", "HOW TO STOP IT — pause agents, revoke keys, `hermes pause`, Paperclip pause.", "stop")],
    cols=5, desc_pt=14, tipt="Every lab applies at least one of these — look for them.")

s = D.new(); header(D, s, "Topic 1 · The platforms", "The Two Platforms You Will Use",
                    "\"If OpenClaw is an employee, Paperclip is the company.\" Hermes is the employee that learns.")
for i, (logo, t, sub, items, dark) in enumerate([
        ("hermes-agent.png", "Hermes Agent", "Day 1 · Labs 1–5", ["Open source (MIT), Nous Research", "Self-improving: memory + skills it writes itself",
                                                             "Telegram & 15+ channels, cron scheduler", "Profiles + Kanban for multi-agent teams"], False),
        ("paperclip.png", "Paperclip", "Day 2 · Labs 6–10", ["Open source (MIT), self-hosted", "Company: Board → CEO → specialists (org chart)",
                                                         "Issues, routines, heartbeats", "Budgets, approval gates, immutable audit log"], True)]):
    x = 0.6 + i * 6.15; card(s, x, 2.45, 5.95, 4.35, fill=CHAR if dark else WHITE)
    lp = asset("logos", logo)
    if os.path.exists(lp):
        box(s, x + 0.3, 2.7, 1.3, 1.3, fill=WHITE, line=K.RULE, shape=K.MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
        s.shapes.add_picture(lp, K.Inches(x + 0.4), K.Inches(2.8), K.Inches(1.1), K.Inches(1.1))
    text(s, x + 1.85, 2.75, 3.9, 0.55, t, 22, WHITE if dark else INK, bold=True, font=SERIF)
    text(s, x + 1.85, 3.32, 3.9, 0.4, sub, 13, ACC, bold=True)
    text(s, x + 0.35, 4.25, 5.3, 2.4, "\n".join("•  " + it for it in items), 14, SOFT if dark else MUTED, lh=1.3)

mark("activity")
s = D.new(dark=True); header(D, s, "Topic 1 · Activity", "Activity — Human–AI Workforce Canvas",
                             "In pairs, 15 minutes. Then start the Hermes Agent install so it is ready for Lab 1.")
steps_ = [("list", "List the work", "Write 8–10 tasks in Kopi Kaki's #ShiokColdBrew campaign (research, posts, video, replies, reporting …)."),
          ("robot", "Single agent?", "Mark tasks one Hermes agent can do end to end."),
          ("users", "Agent team?", "Mark tasks that need several specialised agents (pipeline or swarm)."),
          ("user", "Human?", "Mark decisions that must stay human — and why (risk, accountability, judgement)."),
          ("hand", "Checkpoints", "Draw where the human approves: before public posts, refunds, spend."),
          ("terminal", "Start Hermes", "Run the installer now (Lab 1 step 1) — it downloads while we debrief.")]
for i, (ic, t, d) in enumerate(steps_):
    r, c = divmod(i, 3); x = 0.6 + c * 4.1; y = 2.5 + r * 2.1
    card(s, x, y, 3.9, 1.92, fill=K.PANEL, shadow=False); icon(s, ic, x + 0.25, y + 0.25, 0.52)
    text(s, x + 0.9, y + 0.27, 2.85, 0.48, f"{i+1}. {t}", 15, WHITE, bold=True, font=SERIF, anchor="m")
    text(s, x + 0.25, y + 0.88, 3.45, 0.98, d, 12, SOFT, minpt=9)
prompt(D, "Topic 1 · Activity", "Optional — Ask Hermes to Critique Your Canvas",
       "Here is our Human-AI Workforce Canvas for Kopi Kaki Co.'s #ShiokColdBrew campaign:\n<paste your task list with SINGLE / TEAM / HUMAN labels and approval checkpoints>\n\nAct as an operations consultant. For each task:\n1. Agree or disagree with our label and say why (risk, reversibility, volume, judgement).\n2. Suggest the autonomy level (L1 Operator ... L5 Observer).\n3. Name one control (approval gate, budget, audit, verifier) we must add.\nEnd with the 3 biggest risks in our design.",
       side=[("robot", "Uses Hermes", "Once installed, paste this into the Hermes chat — your first agent conversation."),
             ("scale", "Compare", "Where does the agent disagree with you? Who is right?"),
             ("flag", "Keep it", "You will build this exact workforce in Labs 1–10.")])

# ====================================================================== TOPIC 2 · HERMES
mark("t2")
T2 = C.TOPICS[1]
section(D, "Topic 2", T2["title"], T2["items"], sub="Day 1 — from one AI employee to a supervised multi-agent team.")
cards(D, "Topic 2 · Hermes Agent", "What Is Hermes Agent?", [
    ("Open source, self-hosted", "MIT licence by Nous Research. Runs on your laptop, a VPS, Docker or the desktop app.", "server"),
    ("Grows with you", "Persistent memory and session search; writes and improves its own skills after hard tasks.", "sparkles"),
    ("Every channel", "One gateway: CLI, Telegram, WhatsApp, Slack, Discord, Signal, email …", "chat"),
    ("Tools & MCP", "Web search, files, terminal, browser, image generation, TTS and any MCP server.", "tool"),
    ("Proactive", "Built-in cron scheduler runs jobs and delivers results to your chat.", "clock"),
    ("Multi-agent", "Profiles (isolated agents) + a Kanban board with dependencies, reviews and swarms.", "kanban")],
    cols=3, sub="\"The agent that grows with you.\" — 255k+ GitHub stars, v0.22 (Oct 2026).")
hub(D, "Topic 2 · Hermes Agent", "Hermes Architecture — the Harness Around the Model", "Hermes agent loop\n+ your LLM", [
    ("file", "Context", "AGENTS.md, SOUL.md, USER.md"),
    ("memory", "Memory", "MEMORY.md + session search"),
    ("puzzle", "Skills", "SKILL.md, hub + self-written"),
    ("tool", "Tools & MCP", "web, files, terminal, images"),
    ("chat", "Gateway", "Telegram, Slack, WhatsApp …"),
    ("kanban", "Cron · Profiles · Kanban", "schedule & orchestrate")])
image(D, "Topic 2 · Hermes Agent", "The Hermes Dashboard", asset("screenshots", "hermes-dashboard.png"),
      caption="`hermes dashboard` opens http://127.0.0.1:9119 — sessions, skills, profiles, Kanban, cron, channels and keys in one place.")
flow(D, "Topic 2 · Day 1 journey", "Day 1: Single Agent → Multi-Agent → Human Gates", [
    ("user", "Lab 1", "First AI employee — research brief, memory."),
    ("megaphone", "Lab 2", "Social media campaign — skills + tools."),
    ("handshake", "Lab 3", "Human-in-the-loop on Telegram + cron."),
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
    lambda L, k: _cmd(L, k, "Install, Connect a Model, Start in the Workspace", 0,
                      [("download", "Install", "macOS / Linux / WSL2 one-liner; Windows PowerShell installer."),
                       ("gear", "hermes setup", "Pick a provider and a model with ≥ 64k context; `hermes doctor` to check."),
                       ("folder", "Start in ~/kopi-kaki", "AGENTS.md there is loaded automatically.")]),
    lambda L, k: table(D, k, "Context & Memory Files in Hermes", ["File", "Scope", "What goes in it", "Loaded"],
        [("AGENTS.md (project)", "This folder", "Company facts, rules, current priority", "Every session started in the folder"),
         ("SOUL.md", "~/.hermes/ (per profile)", "The agent's role, personality and standing rules", "Every session"),
         ("MEMORY.md", "~/.hermes/memories/", "Facts the agent decides to remember (~2,200 chars)", "Session start"),
         ("USER.md", "~/.hermes/memories/", "What it knows about you and your preferences", "Session start"),
         ("Session history", "state database", "Every past conversation — searchable", "On demand (session search)")],
        colw=[2.3, 2.4, 4.6, 2.8], size=12, tipt="Short-term = this session's context window. Long-term = the files and history above."),
]
LAB_EXTRAS[2] = [
    lambda L, k: image(D, k, "Skills on the Hermes Dashboard", asset("screenshots", "hermes-skills.png"),
                       caption="Skills are folders with a SKILL.md — bundled, from the hub (`hermes skills install`), your own, or written by the agent itself."),
    lambda L, k: prompt(D, k, "Anatomy of a Skill — kopi-brand-voice/SKILL.md",
                        "---\nname: kopi-brand-voice\ndescription: Write or rewrite public-facing copy in the\n  Kopi Kaki voice and check it against the compliance rules.\n---\n# Kopi Kaki brand voice\n## Steps\n1. Read brand-guide, campaign-brief, compliance-rules.\n2. Warm and sensory; max 1 Singlish word, max 2 emojis.\n3. Only facts and prices from the brief or catalogue.\n4. Promo code shown? Add its terms.\n5. Run the self-check; fix every FAIL.\n## Self-check: C1 health · C3 promo · C4 halal · C9 AI",
                        side=[("eye", "description", "Tells the agent WHEN to load the skill — costs no context until used."),
                              ("list", "steps", "An SOP the agent follows the same way every time."),
                              ("check", "self-check", "Verification built into the skill — the loop checks itself.")],
                        label="SKILL.md  ·  in labs/lab02-…/data/skills/"),
]
LAB_EXTRAS[3] = [
    lambda L, k: flow(D, k, "Connect Telegram in Five Steps", [
        ("chat", "@BotFather", "/newbot → name → copy the token (keep it secret)."),
        ("user", "@userinfobot", "Copy your numeric Telegram user ID."),
        ("gear", "hermes gateway setup", "Choose Telegram, paste token + your ID as the only allowed user."),
        ("server", "hermes gateway run", "Leave it running — it hosts chat, cron and Kanban dispatch."),
        ("megaphone", "Brand channel", "Create 'Kopi Kaki Feed (Training)'; add the bot as admin.")],
        tipt="Shortcut: Dashboard → Messaging → Telegram → 'Create with QR'. NEVER share the bot token."),
    lambda L, k: table(D, k, "Escalation Rules — Policy Becomes Agent Behaviour", ["Comment type", "Agent action", "Why"],
        [("FAQ (availability, oat milk, outlets)", "REPLY — draft in brand voice", "Low risk, high volume"),
         ("Spam", "IGNORE", "No value; don't engage"),
         ("Food safety / allergy (C06, C16)", "ESCALATE — no public reply", "Health and legal risk"),
         ("Legal threat / media (C18, C11)", "ESCALATE", "Needs a human spokesperson"),
         ("Billing / refund (C09)", "ESCALATE", "Money and policy decisions"),
         ("Halal / health questions (C03, C15)", "ESCALATE", "Claims we must not make (C1, C4)")],
        colw=[4.2, 4.1, 3.8], size=12.5, tipt="Personal data (names, phone numbers) is masked before anything reaches you or a public reply."),
    lambda L, k: _cmd(L, k, "Make It Proactive — the 09:00 Approval Cron", 5,
                      [("clock", "Schedule", "Cron syntax '0 9 * * *' = every day at 09:00."),
                       ("send", "--deliver telegram", "Results arrive in your Telegram chat."),
                       ("hand", "Still gated", "The job proposes; only your APPROVE publishes.")]),
]
LAB_EXTRAS[4] = [
    lambda L, k: hub(D, k, "Your Video Studio Team", "Kanban board\n(orchestrator)", [
        ("search", "researcher", "hooks + proof points → research.md"),
        ("pen", "scriptwriter", "25-s script + 6 scenes → script.md"),
        ("film", "producer", "HyperFrames → output/final.mp4"),
        ("eyecheck", "auditor", "V1–V9, C1–C10 → audit-report.md"),
        ("send", "publisher", "runs only after you unblock"),
        ("user", "You", "watch the cut · unblock or comment")],
        foot="The profile --description is the routing contract; SOUL.md holds each role's rules."),
    lambda L, k: image(D, k, "Profiles — Isolated Agents with Their Own Memory", asset("screenshots", "hermes-profiles.png"),
                       caption="`hermes profile create <name> --clone --description \"…\"` — each profile has its own SOUL.md, memory, skills and sessions."),
    lambda L, k: _cmd(L, k, "Build the Task Graph with a Human Gate", 3,
                      [("route", "--parent", "Each task waits for the one before — an ordered SOP."),
                       ("folder", "dir: workspace", "All stages share ~/kopi-kaki/video-studio."),
                       ("stop", "--initial-status blocked", "Publishing waits for your `hermes kanban unblock`.")]),
    lambda L, k: image(D, k, "Watch the Board", asset("screenshots", "hermes-kanban.png"),
                       caption="Lanes: triage → todo → ready → running → review → done. A FAIL goes back with `hermes kanban request-changes`."),
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

for L in LABS[:5]:
    lab_block(L)
mark("t2sum")
cards(D, "Topic 2 · Summary", "What You Built on Day 1", [
    ("Single agent", "Mia researched, remembered and ran a whole campaign with skills and tools.", "robot"),
    ("Human-in-the-loop", "Nothing went public without your APPROVE; risky comments came to you.", "handshake"),
    ("Multi-agent", "A five-role studio and a verified analysis swarm.", "users"),
    ("Harness", "Context, memory, skills, verification, gates, cron — the environment did the heavy lifting.", "gear")],
    cols=4, dark=True)

# ====================================================================== TOPIC 3 · PAPERCLIP
mark("t3")
T3 = C.TOPICS[2]
section(D, "Topic 3", T3["title"], T3["items"], sub="Day 2 — the same marketing work, run as a governed company.")
cards(D, "Topic 3 · Paperclip", "What Is Paperclip?", [
    ("The company as the harness", "Open-source orchestration for a company of agents — org chart, goals, budgets, governance.", "building"),
    ("You are the Board", "Approve hires and strategy; pause, override, reassign or terminate any agent.", "gavel"),
    ("Bring your own agent", "Adapters for Claude Code, Codex, Gemini CLI, OpenClaw, Hermes, Cursor …", "plug"),
    ("Issues & goals", "Mission → goals → projects → issues: every task traces to a goal.", "target"),
    ("Heartbeats & routines", "Agents wake on a schedule or when work is assigned; routines create recurring work.", "clock"),
    ("Budgets & audit", "Per-agent budgets warn at 80% and auto-pause at 100%; append-only activity log.", "coins")],
    cols=3, sub="\"If OpenClaw is an employee, Paperclip is the company.\" — 100k+ GitHub stars, self-hosted at http://localhost:3100.")
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
    ("rocket", "Lab 8", "Launch project: review, revise, release."),
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
for L in LABS[5:]:
    lab_block(L)
mark("t3sum")
cards(D, "Topic 3 · Summary", "What You Governed on Day 2", [
    ("A company", "Mission, goals, budget and a CEO you approved.", "building"),
    ("A team", "Specialists with mandates, budgets, secrets and an independent auditor.", "users"),
    ("Delivery", "A launch project and a weekly routine — all through Board review.", "rocket"),
    ("Governance", "Costs, audit trail, scorecard, interventions and a Board report.", "gavel")],
    cols=4, dark=True)

# ====================================================================== CLOSE
mark("wrap")
section(D, "Wrap-up", "Course Summary & Next Steps", ["Key takeaways", "Practice exam", "Assessment", "Digital attendance"])
cards(D, "Wrap-up", "Summary & Q&A", [
    ("Topic 1", "Agents loop through perception, reasoning and action; the harness and the human make them reliable.", "brain"),
    ("Topic 2", "Hermes took one AI employee to a supervised multi-agent team with skills, memory, cron and gates.", "robot"),
    ("Topic 3", "Paperclip ran the same work as a governed company — Board, budgets, routines, audit.", "building"),
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

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
D.save(OUT)
mark("end")
import json
json.dump(MARK, open(os.path.join(HERE, "slide_map.json"), "w"), indent=1)
print(f"Saved {OUT}  ({D.n} slides)")
