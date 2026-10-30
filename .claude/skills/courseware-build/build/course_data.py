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
VERSION      = "v3.4"
VERSION_DATE = "31 October 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
REPO_URL     = "https://github.com/tertiarycourses/TGS-2024043854-Build-a-Human-AI-Workforce-with-Autonomous-AI-Agents"
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-build-a-human-ai-workforce-with-autonomous-ai-agents.html"
SCENARIO     = "Kopi Kaki Co. — a fictional Singapore kopi startup you found, launching the Gula Melaka Cold Brew at its Tiong Bahru flagship on 1 Dec 2026 (#ShiokColdBrew)"

# ------------------------------------------------------------------ outcomes (from the Course Proposal / TSC ICT-TEM-4034-1.1)
LEARNING_OUTCOMES = [
    "LO1: Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.",
    "LO2: Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.",
    "LO3: Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.",
]

# ------------------------------------------------------------------ topics
TOPICS = [
 dict(num=1,code="01",weighting="30%",title="Human–AI Collaboration & Always-On AI Agents",short="Landscape & Always-On",items=["Brief AI history and what agentic AI is", "Under the hood: the model in a harness, tools, skills and the agentic loop; humans decide", "Two work modes, five collaboration scenarios, use cases and the Big Five always-on agents", "Activity 1 · Join Meta Muse (invite code) and set up an OpenAI Dot"]),
 dict(num=2,code="02",weighting="35%",title="Hermes Agent — Your First AI Employee: Setup, Tools, Skills & Schedules",short="Hermes Agent",items=["What Hermes Agent is; set up Hermes Desktop and connect a model (MiniMax demo)", "Telegram, tools, skills and cron schedules", "gog for Gmail and Calendar; a daily email-summary cron; Firecrawl web search", "Activity 2 · UX skills from skills.sh build the Kopi Kaki website", "Activity 3 · PPT tool + skill build a professional Kopi Kaki deck (PP Task 2)"]),
 dict(num=3,code="03",weighting="35%",title="Hermes Teams — Marketing & Video Production with Profiles, Kanban & Bots",short="Hermes Teams",items=["Multiple agents: own tools, skills, model, instructions and context window; how agents talk (ACP)", "Video tools (HyperFrames, Remotion, Manim); profiles, Kanban and bots", "Activity 4 · Social media marketing team: LinkedIn, Facebook and Instagram posts with images", "Activity 5 · Video production team: research → script → video → voice-over → review → your approval (PP Task 3)", "Five principles of AI security"]),
]
BONUS = dict(num=4,code="B",title="Bonus (optional) — Paperclip: Kopi Kaki as a One-Person Company",short="Bonus · Paperclip",items=["What Paperclip is; install it", "Set up the company and the CEO (with instructions)", "CEO hires a Chief of Staff; the Chief of Staff hires the marketing team", "Org chart, then the team produces the video", "Compare Paperclip with the Hermes Kanban team"])
DAY_THEMES = {1:"Human–AI overview → always-on assistants → Hermes Agent setup, tools, skills and schedules (Activities 1–3)",2:"Hermes marketing and video teams with profiles, Kanban and bots (Activities 4–5), AI security, optional Paperclip bonus, then assessment"}
CONTACT_TIME_NOTE = "9:30 am–6:30 pm both days. 16 scheduled course hours excluding lunch include 13 hours instruction/practice, 1 hour tea breaks and 2 hours assessment. Tea is included in the scheduled LU allocations; this is not a claim of 14 net instructional hours."

# ------------------------------------------------------------------ learning units (approved CP TPG-2024060313, TSC ICT-TEM-4034-1.1)
# LU durations and K/A are fixed by the CP: LU1 5 h, LU2 5 h, LU3 4 h (+ 2 h assessment) = 16 h.
LUS = [
    dict(lu="LU1", hours=5, codes=["K1", "K6", "A1", "A3"], lo=0,
         title="Foundations of autonomous AI agents and single-agent LLM applications",
         covers="Topic 1 history, collaboration, harness and Big Five + Activity 1 always-on assistant + Topic 2 Part A: Hermes Agent, Desktop, model (MiniMax) and Telegram"),
    dict(lu="LU2", hours=5, codes=["K4", "K5", "A2", "A6"], lo=1,
         title="Agent and multi-agent design for efficiency, with humans in the loop",
         covers="Topic 2 Part B: tools, skills, Firecrawl, gog and cron schedules + Activities 2–3 (Kopi website, professional PPT) + Topic 3 team set-up + Activity 4 social media marketing team"),
    dict(lu="LU3", hours=4, codes=["K2", "K3", "A4", "A5"], lo=2,
         title="Evaluate and improve the effectiveness of an AI-agent workforce in product development",
         covers="Activity 5 video production team (researcher source checks, review and human approval), five principles of AI security, evaluation metrics and the optional Paperclip comparison"),
]

# ------------------------------------------------------------------ schedule (9:30–18:30, 8 training hours/day)
# (start, end, minutes, kind, text, LU)  kind: admin/topic/activity/lab/break/lunch/assess/recap
SCHEDULE = {
 1: [
  ("9:30", "9:50", 20, "admin", "Welcome, attendance, outcomes and official SWDA AI subscription redemption steps", "LU1"),
  ("9:50", "11:05", 75, "topic", "Topic 1 (Part A) — AI history; what agentic AI is; under the hood (model, harness, tools, skills, loop); humans decide; assistant vs digital worker; five collaboration scenarios (Scenario 2 tried live on WhatsApp); use cases, AI for Science, humanoid elderly care", "LU1"),
  ("11:05", "11:20", 15, "break", "Tea break (included in scheduled LU time)", "LU1"),
  ("11:20", "12:00", 40, "topic", "Topic 1 (Part B) — deployment evolution (OpenClaw → Hermes → hosted agents); the Big Five and one briefing slide each (Muse, Dots, Grok Bot, Duet, Cue) with embedded setup videos", "LU1"),
  ("12:00", "13:15", 75, "lab", "Lab 1: Activity 1 — 1A join Meta Muse with the trainer’s invite code; 1B set up an OpenAI Dot (Pro/Business Premium); 1C speak prompts with Wispr Flow; Kopi Kaki schedule check and email draft (PP Task 1)", "LU1"),
  ("13:15", "13:30", 15, "activity", "Activity 1 checkpoint and results review — source accuracy, approval controls, limits and actual stop state", "LU1"),
  ("13:30", "14:30", 60, "lunch", "Lunch break", ""),
  ("14:30", "15:30", 60, "topic", "Topic 2 (Part A) — meet Kopi Kaki Co.; what Hermes Agent is; set up Hermes Desktop; connect a model (MiniMax demo); connect Telegram", "LU1"),
  ("15:30", "16:00", 30, "topic", "Topic 2 (Part B) — configure tools; review and install skills; Firecrawl web search", "LU2"),
  ("16:00", "16:15", 15, "break", "Tea break (included in scheduled LU time)", "LU2"),
  ("16:15", "16:45", 30, "topic", "Topic 2 (Part C) — gog: read and send Gmail, check Calendar; cron schedules; a daily email-summary cron to Telegram", "LU2"),
  ("16:45", "17:30", 45, "lab", "Lab 2: Activity 2 — install UX skills from skills.sh; Hermes builds the Kopi Kaki website", "LU2"),
  ("17:30", "18:15", 45, "lab", "Lab 3: Activity 3 — PPT tool + skill: Hermes builds a professional Kopi Kaki deck (PP Task 2)", "LU2"),
  ("18:15", "18:30", 15, "recap", "Day 1 recap, Q&A and PM digital attendance", "LU2"),
 ],
 2: [
  ("9:30", "9:45", 15, "recap", "Day 1 recap and AM attendance", "LU2"),
  ("9:45", "10:15", 30, "topic", "Topic 3 (Part A) — introduction to multiple agents (each with its own tools, skills, model, instructions and context window); how agents talk (ACP); video skills and tools (HyperFrames, Remotion, Manim); Hermes profiles, the Kanban board and bots", "LU2"),
  ("10:15", "11:15", 60, "lab", "Lab 4: Activity 4 — social media marketing team: researcher, LinkedIn/Facebook/Instagram writers and image creator; review the posts gallery", "LU2"),
  ("11:15", "11:30", 15, "break", "Tea break (included in scheduled LU time)", "LU2"),
  ("11:30", "12:15", 45, "lab", "Lab 5: Activity 5A — video production team: profiles, Kanban board and bots; researcher source checks and script", "LU3"),
  ("12:15", "13:15", 60, "lunch", "Lunch break", ""),
  ("13:15", "14:40", 85, "lab", "Lab 5: Activity 5B — video production, voice-over and review; human approval of the exact video via its review link (PP Task 3)", "LU3"),
  ("14:40", "15:10", 30, "topic", "Topic 3 (Part B) — five principles of AI security; RAG vs a standard LLM; four metrics to evaluate and improve the team", "LU3"),
  ("15:10", "15:25", 15, "break", "Tea break (included in scheduled LU time)", "LU3"),
  ("15:25", "16:00", 35, "topic", "Bonus (optional) — Paperclip: Kopi Kaki as a one-person company (trainer demo; full lab self-paced) and comparison with the Hermes Kanban team", "LU3"),
  ("16:00", "16:15", 15, "recap", "Course recap, practice questions and Q&A", "LU3"),
  ("16:15", "16:30", 15, "assess", "Briefing for Assessment", "LU3"),
  ("16:30", "17:30", 60, "assess", "Written Assessment (WA) — 1 hour, open book; TRAQOM survey and assessment attendance first", "ASSESS"),
  ("17:30", "18:30", 60, "assess", "Practical Performance (PP) — 1 hour, open book; submit answers on the LMS and take PM attendance", "ASSESS"),
 ],
}

ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — three tasks plus written analysis, 1 hour, open book. Task 1: ONE Meta Muse or OpenAI Dots screenshot (Activity 1). Task 2: ONE Hermes Desktop/dashboard screenshot of the professional PPT (Activity 3). Task 3: TWO screenshots — the Hermes Kanban board and the video it produced (Activity 5).",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
