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
VERSION      = "v2.0"
VERSION_DATE = "18 October 2026"
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
    dict(num=1, code="01", weighting="30%",
         title="Foundations of Autonomous AI Agents & the Human–AI Workforce",
         short="Foundations",
         items=["A brief history of AI", "AI agents vs agentic AI", "The agentic loop & harness engineering",
                "Brain · perception · action, memory & world models", "From single agent to human–AI collaboration",
                "The 2026 agent market, use cases & governance"]),
    dict(num=2, code="02", weighting="35%",
         title="Hermes Agent — From a Single AI Employee to a Multi-Agent Team",
         short="Hermes Agent",
         items=["Lab 1 · Your first AI employee", "Lab 2 · End-to-end social media campaign",
                "Lab 3 · Human-in-the-loop publishing", "Lab 4 · Multi-agent video studio",
                "Lab 5 · Campaign command centre"]),
    dict(num=3, code="03", weighting="35%",
         title="Paperclip — Running & Governing a Company of AI Agents",
         short="Paperclip",
         items=["Lab 6 · Found the AI company", "Lab 7 · Hire the team", "Lab 8 · Launch campaign project",
                "Lab 9 · Weekly video routine", "Lab 10 · Govern, measure & improve"]),
]

DAY_THEMES = {
    1: "Foundations (Topic 1) & Hermes Agent — single to multi-agent (Topic 2, Labs 1–5)",
    2: "Paperclip — a governed company of agents (Topic 3, Labs 6–10) & Final Assessment",
}

# ------------------------------------------------------------------ learning units (approved CP TPG-2024060313, TSC ICT-TEM-4034-1.1)
# LU durations and K/A are fixed by the CP: LU1 5 h, LU2 5 h, LU3 4 h (+ 2 h assessment) = 16 h.
LUS = [
    dict(lu="LU1", hours=5, codes=["K1", "K6", "A1", "A3"], lo=0,
         title="Foundations of autonomous AI agents and single-agent LLM applications",
         covers="Topic 1 (Foundations) + Topic 2 Labs 1–2 (single Hermes agent)"),
    dict(lu="LU2", hours=5, codes=["K4", "K5", "A2", "A6"], lo=1,
         title="Agent and multi-agent design for efficiency, with humans in the loop",
         covers="Topic 2 Labs 3–5 (human-in-the-loop, multi-agent studio, swarm) + Topic 3 Lab 6 (designing a governed agent company)"),
    dict(lu="LU3", hours=4, codes=["K2", "K3", "A4", "A5"], lo=2,
         title="Evaluate and improve the effectiveness of an AI-agent workforce in product development",
         covers="Topic 3 Labs 7–10 (team, launch project, routine, governance and improvement)"),
]

# ------------------------------------------------------------------ schedule (9:30–18:30, 8 training hours/day)
# (start, end, minutes, kind, text, LU)  kind: admin/topic/activity/lab/break/lunch/assess/recap
SCHEDULE = {
 1: [
  ("9:30", "9:50", 20, "admin", "Welcome, housekeeping, trainer introduction, learning outcomes and AM digital attendance", "LU1"),
  ("9:50", "11:05", 75, "topic", "Topic 1 (Part A) — history of AI; AI agents vs agentic AI; the agentic loop; harness engineering; brain–perception–action; short- and long-term memory; RAG; world models", "LU1"),
  ("11:05", "11:20", 15, "break", "Tea break", "LU1"),
  ("11:20", "12:10", 50, "topic", "Topic 1 (Part B) — single agent → multi-agent → human–agent collaboration; levels of autonomy; agent society; the 2026 agent market (OpenClaw, Hermes, Paperclip, OpenAI Dots, Meta Muse, Block Buzz, Manus Cue …); Singapore's AgentSea; human–AI use cases in science, maths, drug discovery and business; risks and governance", "LU1"),
  ("12:10", "12:35", 25, "activity", "Activity — Human–AI Workforce Canvas for Kopi Kaki Co., and start the Hermes Agent install", "LU1"),
  ("12:35", "13:30", 55, "lab", "Topic 2 — Lab 1: Hire Your First AI Employee (Hermes) — customer & market research brief", "LU1"),
  ("13:30", "14:30", 60, "lunch", "Lunch break", ""),
  ("14:30", "15:30", 60, "lab", "Lab 2: End-to-End Social Media Campaign with one agent (skills + tools)", "LU1"),
  ("15:30", "16:15", 45, "lab", "Lab 3: Human-in-the-Loop Publishing & Community Care (Telegram + cron)", "LU2"),
  ("16:15", "16:30", 15, "break", "Tea break", "LU2"),
  ("16:30", "17:30", 60, "lab", "Lab 4: Multi-Agent Video Studio — research → script → production → audit → publish", "LU2"),
  ("17:30", "18:15", 45, "lab", "Lab 5: Multi-Agent Campaign Command Centre — measure, optimise & report", "LU2"),
  ("18:15", "18:30", 15, "recap", "Day 1 recap, Q&A and PM digital attendance", "LU2"),
 ],
 2: [
  ("9:30", "9:45", 15, "recap", "Day 1 recap and AM digital attendance", "LU2"),
  ("9:45", "10:15", 30, "topic", "Topic 3 — Paperclip: the company as the agent harness; Board, CEO and org chart; adapters; goals, projects and tasks; routines and heartbeats; budgets, approvals and the audit trail", "LU2"),
  ("10:15", "11:15", 60, "lab", "Lab 6: Found Kopi Kaki Growth Studio — an AI company you govern", "LU2"),
  ("11:15", "11:30", 15, "break", "Tea break", "LU2"),
  ("11:30", "12:15", 45, "lab", "Lab 7: Hire the Marketing Team through the Board approval gate", "LU3"),
  ("12:15", "13:15", 60, "lunch", "Lunch break", ""),
  ("13:15", "14:10", 55, "lab", "Lab 8: Run the #ShiokColdBrew launch as a project — review, revise, release", "LU3"),
  ("14:10", "14:55", 45, "lab", "Lab 9: Automate the weekly video pipeline with a routine and a Board gate", "LU3"),
  ("14:55", "15:10", 15, "break", "Tea break", "LU3"),
  ("15:10", "15:55", 45, "lab", "Lab 10: Govern, measure & improve your human–AI workforce", "LU3"),
  ("15:55", "16:15", 20, "recap", "Course recap, practice exam and Q&A", "LU3"),
  ("16:15", "16:30", 15, "assess", "Briefing for Assessment", "LU3"),
  ("16:30", "17:30", 60, "assess", "Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book", "ASSESS"),
  ("17:30", "18:30", 60, "assess", "Practical Performance (PP) — 1 hour, open book; TRAQOM survey and PM / assessment digital attendance", "ASSESS"),
 ],
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — three tasks, each with ONE screenshot from a lab (Lab 1 Hermes agent, Lab 4 multi-agent studio, Lab 7 Paperclip org chart) plus written analysis, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
