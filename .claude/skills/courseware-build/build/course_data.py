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
VERSION      = "v2.1"
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
    dict(num=1, code="01", weighting="30%",
         title="Human–AI Collaboration: Landscape, Agents, Use Cases & Futures",
         short="Foundations",
         items=["Current human–AI interaction landscape", "2023 prompt → 2024 context → 2025 harness → 2026 agents",
                "48 practical workflows, scientific discovery and humanoid futures", "Single agents, teams, orchestration and human control",
                "Agent mechanisms, evidence, permissions and governance"]),
    dict(num=2, code="02", weighting="35%",
         title="Hermes Agent — Single-Agent Office Automation, Tools & Skills",
         short="Hermes Agent",
         items=["Lab 1 · Install Hermes, Telegram and an evidence brief", "Lab 2 · Gmail, Calendar, Drive, Excel, dashboard and PowerPoint",
                "Lab 3 · Office approval and exception handling", "Day 2 bridge · Labs 4–5 Kanban and multi-agent work"]),
    dict(num=3, code="03", weighting="35%",
         title="Multi-Agent Teams — Kanban, Claude Code & Governance",
         short="Paperclip",
         items=["Labs 4–5 · Kanban video studio and analysis team", "Labs 6–7 · Company and org-chart governance",
                "Lab 8 · Claude Code multi-agent video team", "Labs 9–10 · Repeatable work, evaluation and improvement"]),
]

DAY_THEMES = {
    1: "Human–AI landscape and single Hermes agent: office automation, tools, skills and practice (Labs 1–3)",
    2: "Multi-agent teams: Kanban, Claude Code video studio, governance (Labs 4–10), then assessment",
}
CONTACT_TIME_NOTE = "9:30 am–6:30 pm both days. 16 scheduled course hours excluding lunch include 13 hours instruction/practice, 1 hour tea breaks and 2 hours assessment. Tea is included in the scheduled LU allocations; this is not a claim of 14 net instructional hours."

# ------------------------------------------------------------------ learning units (approved CP TPG-2024060313, TSC ICT-TEM-4034-1.1)
# LU durations and K/A are fixed by the CP: LU1 5 h, LU2 5 h, LU3 4 h (+ 2 h assessment) = 16 h.
LUS = [
    dict(lu="LU1", hours=5, codes=["K1", "K6", "A1", "A3"], lo=0,
         title="Foundations of autonomous AI agents and single-agent LLM applications",
         covers="Topic 1 landscape, canvas and office design clinic + demo + Lab 1A installation and evidence brief"),
    dict(lu="LU2", hours=5, codes=["K4", "K5", "A2", "A6"], lo=1,
         title="Agent and multi-agent design for efficiency, with humans in the loop",
         covers="Lab 1B + Labs 2–5 tools/skills, human gates, Kanban studio and parallel team; governance introduction"),
    dict(lu="LU3", hours=4, codes=["K2", "K3", "A4", "A5"], lo=2,
         title="Evaluate and improve the effectiveness of an AI-agent workforce in product development",
         covers="Labs 6–10 company governance, Claude video team, repeatable work and evaluation"),
]

# ------------------------------------------------------------------ schedule (9:30–18:30, 8 training hours/day)
# (start, end, minutes, kind, text, LU)  kind: admin/topic/activity/lab/break/lunch/assess/recap
SCHEDULE = {
 1: [
  ("9:30","9:50",20,"admin","Welcome, attendance, learning outcomes and official SWDA AI subscription redemption steps","LU1"),
  ("9:50","11:05",75,"topic","Topic 1 (Part A) — current human–AI landscape; history; agents and agentic AI; practical use-case gallery; science; future humanoid collaboration","LU1"),
  ("11:05","11:20",15,"break","Tea break (included in scheduled LU time)","LU1"),
  ("11:20","12:40",80,"topic","Topic 1 (Part B) — collaboration modes; single and multi-agent patterns; orchestration; tools, skills, memory, RAG, permissions, governance and evidence","LU1"),
  ("12:40","13:00",20,"activity","Activity — design the Kopi Kaki launch-office canvas, inputs, outputs and human decisions","LU1"),
  ("13:00","13:30",30,"activity","Office workflow design clinic — analyse task ownership, tool contracts and acceptance tests","LU1"),
  ("13:30","14:30",60,"lunch","Lunch break",""),
  ("14:30","14:45",15,"topic","Trainer demo — OpenAI Dots office workflow, tool evidence and human control; Hermes fallback","LU1"),
  ("14:45","15:30",45,"lab","Lab 1: Activity 1A — install Hermes, connect Telegram and produce the source-linked brief (PP Q1 preparation)","LU1"),
  ("15:30","16:00",30,"lab","Lab 1: Activity 1B — test tools, memory recall and evidence; analyse the agent design","LU2"),
  ("16:00","16:15",15,"break","Tea break (included in scheduled LU time)","LU2"),
  ("16:15","17:45",90,"lab","Lab 2: Single-agent launch office — gog Gmail/Calendar/Drive, Excel analysis, interactive dashboard and professional PowerPoint","LU2"),
  ("17:45","18:15",30,"lab","Lab 3: Human approval, office exceptions and safe internal reporting","LU2"),
  ("18:15","18:30",15,"recap","Day 1 recap, Q&A and PM digital attendance","LU2"),
 ],
 2: [
  ("9:30","9:45",15,"recap","Day 1 recap and AM attendance; prepare the multi-agent board","LU2"),
  ("9:45","10:35",50,"lab","Lab 4: Multi-Agent Video Studio — Kanban roles, dependencies, production, audit and human release gate","LU2"),
  ("10:35","11:10",35,"lab","Lab 5: Multi-Agent Campaign Command Centre — parallel analysis, verifier and synthesis","LU2"),
  ("11:10","11:25",15,"break","Tea break (included in scheduled LU time)","LU2"),
  ("11:25","11:30",5,"topic","Topic 3 — company-level governance and team accountability","LU2"),
  ("11:30","12:15",45,"lab","Lab 6: Found Kopi Kaki Growth Studio — mission, company and governed CEO","LU3"),
  ("12:15","13:15",60,"lunch","Lunch break",""),
  ("13:15","13:50",35,"lab","Lab 7: Hire the Marketing Team through the Board gate — org-chart evidence for PP Q3","LU3"),
  ("13:50","14:40",50,"lab","Lab 8: Claude Code Agent Team — create and audit a launch video with independent teammates","LU3"),
  ("14:40","15:10",30,"lab","Lab 9: Repeatable Weekly Video Pipeline — routine, verification and Board review","LU3"),
  ("15:10","15:25",15,"break","Tea break (included in scheduled LU time)","LU3"),
  ("15:25","16:00",35,"lab","Lab 10: Govern, Measure and Improve — compare single-agent and team workflows","LU3"),
  ("16:00","16:15",15,"recap","Course recap, practice questions and Q&A","LU3"),
  ("16:15","16:30",15,"assess","Briefing for Assessment","LU3"),
  ("16:30","17:30",60,"assess","Written Assessment (WA) — 1 hour, open book","ASSESS"),
  ("17:30","18:30",60,"assess","Practical Performance (PP) — 1 hour, open book; TRAQOM survey and PM / assessment attendance","ASSESS"),
 ],
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — three tasks, each with ONE screenshot from a lab (Lab 1 Hermes agent, Lab 4 multi-agent studio, Lab 7 Paperclip org chart) plus written analysis, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
