"""
SINGLE SOURCE OF TRUTH for the "Build a Human-AI Workforce with Autonomous AI
Agents" courseware (v2.0 — Claude Code course design, use-case labs).

course_data.py (metadata, topics, schedule) + data_labs.py (the ten labs) +
mock_data.py (the Kopi Kaki Co. scenario files) drive the slide deck, Lesson
Plan, Learner Guide, labs/ folder, lab PDFs and the Lab Prompts page.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Build a Human-AI Workforce with Autonomous AI Agents"
SHORT_TITLE  = "Human-AI Workforce with Autonomous AI Agents"   # used in output filenames
COURSE_CODE  = "TGS-2024043854"
VERSION      = "v2.5"
VERSION_DATE = "29 October 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
REPO_URL     = "https://github.com/tertiarycourses/TGS-2024043854-Build-a-Human-AI-Workforce-with-Autonomous-AI-Agents"
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-build-a-human-ai-workforce-with-autonomous-ai-agents.html"
SCENARIO     = "Kopi Kaki Co. — a fictional Singapore kopi chain launching the Gula Melaka Cold Brew (#ShiokColdBrew)"

# ------------------------------------------------------------------ outcomes (from the Course Proposal / TSC ICT-TEM-4034-1.1)
LEARNING_OUTCOMES = [
    "LO1: Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.",
    "LO2: Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.",
    "LO3: Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.",
]

# ------------------------------------------------------------------ topics
TOPICS = [
 dict(num=1,code="01",weighting="30%",title="Human–AI Collaboration & Always-On AI Agents",short="Landscape & Always-On",items=["Brief AI history and two human–AI work modes", "Big Five: Duet, Muse, Grok Bot, Dots and Manus Cue", "Activity 1 · Set up an always-on assistant", "Under the hood: harness, loop, context and human decisions"]),
 dict(num=2,code="02",weighting="35%",title="Hermes Agent — Single-Agent Office Automation, Tools & Skills",short="Hermes Agent",items=["Activity 2 · Hermes Desktop, tools, skills and source brief", "Activity 3 · gog: Gmail, Calendar, Drive and Excel", "Activity 4 · Dashboard, professional PPT and single-agent video", "Human review and one approved training email"]),
 dict(num=3,code="03",weighting="35%",title="Hermes Teams & OpenAI Dots — Kanban, Video & Human Oversight",short="Hermes Teams & Dots",items=["Activity 5 · Hermes bots and Kanban video studio", "Activity 6 · Source retrieval, verification and maintenance", "Activity 7 · Dots: supervised launch review", "Activity 8 · Team video revision, local release and evaluation"]),
]
DAY_THEMES = {1:"Human–AI overview → always-on assistants → Hermes single-agent office practice (Activities 1–4)",2:"Hermes multi-agent Kanban video team and OpenAI Dots (Activities 5–8), then assessment"}
CONTACT_TIME_NOTE = "9:30 am–6:30 pm both days. 16 scheduled course hours excluding lunch include 13 hours instruction/practice, 1 hour tea breaks and 2 hours assessment. Tea is included in the scheduled LU allocations; this is not a claim of 14 net instructional hours."

# ------------------------------------------------------------------ learning units (approved CP TPG-2024060313, TSC ICT-TEM-4034-1.1)
# LU durations and K/A are fixed by the CP: LU1 5 h, LU2 5 h, LU3 4 h (+ 2 h assessment) = 16 h.
LUS = [
    dict(lu="LU1", hours=5, codes=["K1", "K6", "A1", "A3"], lo=0,
         title="Foundations of autonomous AI agents and single-agent LLM applications",
         covers="Topic 1 history, collaboration, harness and Big Five + Activity 1 always-on setup + Activity 2A Hermes Desktop and company brief"),
    dict(lu="LU2", hours=5, codes=["K4", "K5", "A2", "A6"], lo=1,
         title="Agent and multi-agent design for efficiency, with humans in the loop",
         covers="Activity 2B skills/tools + Activities 3–5: Google/Excel, office/video artifacts, human approval and Kanban video studio"),
    dict(lu="LU3", hours=4, codes=["K2", "K3", "A4", "A5"], lo=2,
         title="Evaluate and improve the effectiveness of an AI-agent workforce in product development",
         covers="Activities 6–8: source assurance, Dots, video-team revision and evaluation"),
]

# ------------------------------------------------------------------ schedule (9:30–18:30, 8 training hours/day)
# (start, end, minutes, kind, text, LU)  kind: admin/topic/activity/lab/break/lunch/assess/recap
SCHEDULE = {
 1: [
  ("9:30","9:50",20,"admin","Welcome, attendance, outcomes and official SWDA AI subscription redemption steps","LU1"),
  ("9:50","11:05",75,"topic","Topic 1 (Part A) — brief AI history; agentic AI and always-on agents; human–AI roles, two work modes and use cases; Big Five features (Duet, Muse, Grok Bot, Dots, Manus and Cue), comparison and Singapore update","LU1"),
  ("11:05","11:20",15,"break","Tea break (included in scheduled LU time)","LU1"),
  ("11:20","12:35",75,"lab","Lab 1: Activity 1 — setup plan and walkthroughs (Muse, Dots, Grok Bot; Duet and Cue for reference); connect Gmail/Calendar, schedule check and email draft (PP Task 1 image A)","LU1"),
  ("12:35","12:50",15,"activity","Assistant results review — compare source accuracy, approval controls, limits and actual stop state","LU1"),
  ("12:50","13:30",40,"topic","Under the hood — how agents work: model in a harness, context, memory and RAG, tools and skills, the agentic loop, approvals and human-in/on-the-loop","LU1"),
  ("13:30","14:30",60,"lunch","Lunch break",""),
  ("14:30","15:30",60,"lab","Lab 2: Activity 2A — introduce Kopi Kaki; Hermes Desktop, features, tools and reviewed skills","LU1"),
  ("15:30","16:00",30,"lab","Lab 2: Activity 2B — install office/gog/video skills, verify tools and save the source brief","LU2"),
  ("16:00","16:15",15,"break","Tea break (included in scheduled LU time)","LU2"),
  ("16:15","17:05",50,"lab","Lab 3: Activity 3 — Hermes gog Gmail/Calendar/Drive and verified Excel analysis","LU2"),
  ("17:05","17:45",40,"lab","Lab 4: Activity 4A — interactive dashboard and professional PPT (PP Task 2; PP Task 1 image B)","LU2"),
  ("17:45","18:15",30,"lab","Lab 4: Activity 4B — single-agent video, exact-version review and one approved test email with Sent readback","LU2"),
  ("18:15","18:30",15,"recap","Day 1 recap, Q&A and PM digital attendance","LU2"),
 ],
 2: [
  ("9:30","9:45",15,"recap","Day 1 recap and AM attendance; prepare the multi-agent board","LU2"),
  ("9:45","10:35",50,"lab","Lab 5: Activity 5A — Hermes bots, Kanban roles, dependencies and video production","LU2"),
  ("10:35","11:10",35,"lab","Lab 5: Activity 5B — independent audit, human revision and video-team evidence","LU2"),
  ("11:10","11:25",15,"break","Tea break (included in scheduled LU time)","LU2"),
  ("11:25","11:30",5,"topic","Source assurance introduction — claims, passages, versions and owners","LU2"),
  ("11:30","12:15",45,"lab","Lab 6: Activity 6 — source retrieval, verification and RAG maintenance","LU3"),
  ("12:15","13:15",60,"lunch","Lunch break",""),
  ("13:15","13:50",35,"lab","Lab 7: Activity 7 — supervised OpenAI Dots launch review and Hermes comparison","LU3"),
  ("13:50","14:40",50,"lab","Lab 8: Activity 8A — multi-agent Kanban video revision with Hermes bots (PP Task 3)","LU3"),
  ("14:40","15:10",30,"lab","Lab 8: Activity 8B — repeat-run test, failed-source recovery and exact-version review","LU3"),
  ("15:10","15:25",15,"break","Tea break (included in scheduled LU time)","LU3"),
  ("15:25","16:00",35,"lab","Lab 8: Activity 8C — final local release, scorecard and team improvement","LU3"),
  ("16:00","16:15",15,"recap","Course recap, practice questions and Q&A","LU3"),
  ("16:15","16:30",15,"assess","Briefing for Assessment","LU3"),
  ("16:30","17:30",60,"assess","Written Assessment (WA) — 1 hour, open book","ASSESS"),
  ("17:30","18:30",60,"assess","Practical Performance (PP) — 1 hour, open book; TRAQOM survey and PM / assessment attendance","ASSESS"),
 ],
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — three tasks plus written analysis, 1 hour, open book. Task 1: TWO screenshots (Activity 1 chosen always-on assistant and Activity 4 Hermes-generated artifact). Task 2: ONE professional PPT screenshot using skills/tools (Activity 4). Task 3: ONE real multi-agent Kanban video-team screenshot with Hermes bots (Activity 5 or 8).",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
