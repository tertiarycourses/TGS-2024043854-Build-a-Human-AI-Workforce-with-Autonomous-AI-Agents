"""
SINGLE SOURCE OF TRUTH for the "Build a Human-AI Workforce with Autonomous AI
Agents" courseware.

Every artifact — the slide deck (PPT), Lesson Plan (LP), Learner Guide (LG)
and the labs/ folder — is generated from (or aligned to) the data in this
module and the data_domainN.py files, so titles, topic numbering, activities,
learning outcomes and the schedule can never drift apart.

Edit here, then re-run the courseware-build engine.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Build a Human-AI Workforce with Autonomous AI Agents"
SHORT_TITLE  = "Human-AI Workforce with Autonomous AI Agents"   # used in output filenames
COURSE_CODE  = "TGS-2024043854"
VERSION      = "v1.10"
VERSION_DATE = "16 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

# ------------------------------------------------------------------ outcomes
# The 3 official WSQ learning outcomes for the TSC "Artificial Intelligence
# Application in Product Development" (ICT-TEM-4034-1.1), taken from the Course
# Proposal (CP). Delivered through the three autonomous-agent platform topics.
LEARNING_OUTCOMES = [
    "LO1: Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.",
    "LO2: Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.",
    "LO3: Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.",
]

# ------------------------------------------------------------------ topics (= platform domains)
# num, code, title, subtitle, weighting, concept bullets for the section
TOPICS = [
    dict(num=1, code="01",
         title="Hermes Agent — Your Autonomous Personal Chief-of-Staff",
         subtitle="Install & Setup · Deployment · Memory & Plugins · Skills · Providers & Model · MCP & Tools · Crons · Subagents · Profile & Kanban · Security",
         weighting="33%",
         concepts=[
            "Hermes Agent (Nous Research) installs on your own machine — via the install script or the Hermes Desktop app — and requires a model with a >=64,000-token context window.",
            "Memory and plugins make the agent stateful and extensible: a three-layer memory (agent-curated notes, FTS5 cross-session recall, Honcho user modelling) plus installable skills and MCP tools.",
            "Providers & models are swappable with no lock-in (Nous Portal, OpenRouter, OpenAI, any endpoint); MCP servers and the Tool Gateway (web search, image, TTS) give the agent real-world reach.",
            "Cron jobs automate recurring work; subagents & delegation split work across isolated backends; the profile and Kanban board let you supervise the agent's tasks — all under security controls.",
         ]),
    dict(num=2, code="02",
         title="OpenClaw — Automating a Business Back-Office",
         subtitle="Install · Providers · Channels · Skills · Tools · Commands · Crons · Memory · Dreaming · Security · Multi-Agent · Use Cases",
         weighting="33%",
         concepts=[
            "OpenClaw runs on Node.js 24 LTS as a long-running gateway daemon that hosts every channel, tool, cron and skill for the Nimbus Supplies back office.",
            "Providers are connected by OAuth sign-in (OpenAI Codex, MiniMax) or API key (Anthropic, DeepSeek, OpenRouter); skills from skills.sh and integrations such as Firecrawl and AgentMail extend the agent.",
            "'Dreaming' lets the agent reflect during idle time — reviewing memory and generating follow-ups — while profiles and allow/deny lists keep every channel least-privileged and audited.",
            "Crons schedule recurring work, a heartbeat auto-restarts the gateway, and a multi-agent capstone splits work across cooperating Sales, Research and Ops agents for real back-office use cases.",
         ]),
    dict(num=3, code="03",
         title="Paperclip — Running & Governing a Company of AI Agents",
         subtitle="Install (Windows & Mac) · Company, CEO & Mission · Adaptors · Task Backlog · Tavily Search API · Hire the Team",
         weighting="34%",
         concepts=[
            "Paperclip is an operating system for a company of AI agents, self-hosted with Docker Compose on Windows (WSL2) or macOS; you are the Board, a CEO agent reports to you, and specialists report to the CEO.",
            "Running use case: 'Tertiary AI News Research' — a zero-human news desk whose mission is a verified, cited daily AI-news briefing; the mission you write steers every agent the company hires.",
            "Model adaptors (built-in Claude Code, Codex and Gemini CLI) are the agents' engine; the Tavily Search API — stored as a Secret and bound to a runtime env var — gives researchers live web results.",
            "The company runs off a detailed task backlog (todo -> in_progress -> in_review -> done) whose core task is hiring; the CEO proposes the team and every hire pauses at a Board approval gate.",
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Hermes Agent (Topic 1) & OpenClaw (Topic 2)",
    2: "Paperclip (Topic 3) & Final Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on agent-building tasks that follow the course labs, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
