#!/usr/bin/env python3
"""Generate the Learner Guide as BOTH a Markdown mirror (LG-*.md at the repo root) and a DOCX
(courseware/LG-*.docx) from one block list, so the two never diverge.

Content: course_data (admin), TOPIC1 below (concept narrative matching the deck, with sources)
and data_labs.LABS (full step-by-step lab guides with prompts and commands).
"""
import os, re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS
import prodoc
from version_history import PRIOR, V20

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE); ASSETS = os.path.join(os.path.dirname(HERE), "assets")
SHOTS = os.path.join(REPO, "courseware", "assets")

B = []
def h1(t): B.append(("h1", t))
def h2(t): B.append(("h2", t))
def h3(t): B.append(("h3", t))
def p(t): B.append(("p", t))
def bullets(xs): B.append(("bullets", list(xs)))
def numbered(xs): B.append(("numbered", list(xs)))
def code(t, lang="bash"): B.append(("code", t, lang))
def note(t): B.append(("note", t))
def table(head, rows): B.append(("table", head, rows))
def img(path, caption, width=6.0): B.append(("img", path, caption, width))
def src(t): B.append(("src", t))

# ====================================================================== front matter
h1("About This Learner Guide")
p(f"This Learner Guide accompanies the WSQ course **{C.TITLE}** ({C.COURSE_CODE}). It explains the concepts of Topic 1 in "
  "depth and gives you detailed, step-by-step instructions for the ten hands-on labs. Use it during class and as an "
  "open-book reference in the assessment.")
table(["Item", "Details"], [("Course", C.TITLE), ("Course code", C.COURSE_CODE), ("Duration", "2 days (16 hours incl. assessment)"),
                            ("Provider", f"{C.ORG} ({C.UEN})"), ("Course scenario", C.SCENARIO + " — all company data is fictional"),
                            ("Course repository", C.REPO_URL)])
h2("Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)
h2("Course Structure")
table(["Topic", "Day", "What you do"], [
    ("1 · " + C.TOPICS[0]["title"], "Day 1 AM", "; ".join(C.TOPICS[0]["items"]) + "; Activity: Human–AI Workforce Canvas"),
    ("2 · " + C.TOPICS[1]["title"], "Day 1 PM", "Labs 1–5 on Hermes Agent"),
    ("3 · " + C.TOPICS[2]["title"], "Day 2", "Labs 6–10 on Paperclip, then the assessment")])
h2("How to Use the Lab Materials")
numbered(["Download the course repository (Code → Download ZIP) and unzip it.",
          "Open prompts/index.html in your browser. Pick a lab, click Copy and paste the prompt or command where the page says. It works offline.",
          "Each lab folder labs/labNN-…/ contains README.md, LAB-NN-Instructions.pdf (printable), COPY-PROMPTS.txt and data/ (mock company files, skills and brand assets).",
          "Create one workspace folder ~/kopi-kaki and copy each lab's data/ into it as you go. Outputs are saved to ~/kopi-kaki/outputs/labNN/.",
          "Finish each lab with its checkpoint: evidence, not vibes."])
img(os.path.join(SHOTS, "screenshots", "prompts-page.png"), "The Lab Prompts page (prompts/index.html)", 4.2)
note("Platforms change quickly. If a command differs on your version, run it with --help and check the official docs: "
     "https://hermes-agent.nousresearch.com/docs/ and https://docs.paperclip.ing.")

# ====================================================================== TOPIC 1
h1("Topic 1 — " + C.TOPICS[0]["title"])
h2("1.1 A Brief History of AI")
p("Artificial intelligence moved from hand-written rules to learning from data, then to language, and now to agents that act. "
  "Each era moved more of the 'how' from people into the machine.")
table(["Year", "Milestone", "Why it matters"], [
    ("1950", "Alan Turing proposes the imitation game (Turing test)", "Turns 'Can machines think?' into a behavioural test"),
    ("1956", "Dartmouth workshop coins 'artificial intelligence'", "AI becomes a field of study"),
    ("1970s–80s", "Expert systems (MYCIN, XCON)", "Rules + inference engine; brittle and costly to update"),
    ("1997", "IBM Deep Blue beats Garry Kasparov", "Brute-force search wins a narrow task"),
    ("2012", "AlexNet wins ImageNet", "Deep learning era: GPUs + big data"),
    ("2016", "AlphaGo beats Lee Sedol 4–1", "Deep + reinforcement learning"),
    ("2017", "'Attention Is All You Need' — the Transformer", "The architecture behind every LLM"),
    ("2022", "ChatGPT launches (30 Nov); ReAct paper", "LLMs go mainstream; LLMs can reason and act"),
    ("2023", "GPT-4; the prompt-engineering era", "Results depend on how the prompt is worded"),
    ("2024", "Model Context Protocol (25 Nov 2024)", "A standard way for agents to reach tools and data"),
    ("2025", "Coding agents (Claude Code, Codex); context engineering", "Results depend on the context you curate"),
    ("2026", "Harness engineering named; always-on agents (OpenClaw, Hermes Agent, Paperclip, OpenAI Dots, Meta Muse)", "Agents work 24/7 inside human-governed systems")])
p("**Prompt → context → harness engineering.** Prompt engineering crafts one instruction. Context engineering curates everything "
  "the model sees — brand guide, brief, data, memory, tool results. Harness engineering designs the whole environment around the "
  "model: the loop, tools, memory, skills, verification, guardrails and human gates. Each layer contains the one before it.")
h3("The range of AI applications today")
table(["Category", "Examples", "Key capability"], [
    ("Generative AI / LLMs", "Chatbots, writing, coding, summarising", "Understand and generate natural language, code and images"),
    ("Computer vision", "Defect detection, medical imaging, visual product search", "Recognise and classify what is in images and video"),
    ("Predictive analytics & machine learning", "Demand forecasting, fraud scoring, recommendations", "Learn patterns in historical data to predict outcomes"),
    ("Speech & multimodal", "Voice assistants, transcription, text-to-speech", "Convert between speech, text and other media"),
    ("Scientific discovery", "AlphaFold, AI co-scientist, AlphaEvolve", "Generate and rank hypotheses or designs for experts to test"),
    ("Autonomous AI agents", "Hermes Agent, Paperclip, OpenAI Dots, Synapxe AgentSea", "Pursue a goal with tools, memory and planning, with humans in the loop")])
src("Sources: Turing (1950); Vaswani et al. (2017); Anthropic, Model Context Protocol (Nov 2024); Anthropic, Effective context engineering for AI agents (Sep 2025).")

h2("1.2 AI Agents vs Agentic AI")
p("An **AI agent** is an autonomous software entity that executes a goal-directed task in a bounded digital environment: one LLM plus "
  "tools, cycling through perceive → reason → act. **Agentic AI** is a system of several specialised agents coordinated by an "
  "orchestrator, with dynamic task decomposition, persistent shared memory and coordinated autonomy.")
table(["Dimension", "AI Agent", "Agentic AI"], [
    ("Scope", "One specific, well-defined task", "A complex, multi-step goal or workflow"),
    ("Architecture", "One LLM + tools", "Several specialised agents + an orchestrator"),
    ("Flow", "User → Agent → Tool", "User → System → Agent 1 → Agent 2 → …"),
    ("Memory", "Session context, optional cache", "Shared, persistent memory across stages"),
    ("Planning", "Single-step, reactive", "Multi-step, proactive goal decomposition"),
    ("Coordination", "Works alone", "Hierarchical or decentralised hand-offs"),
    ("In this course", "Lab 1 research agent, Lab 2 campaign agent", "Lab 4 video studio, Lab 5 swarm, Labs 6–10 AI company"),
    ("Main risks", "Hallucination, brittle prompts", "Error propagation, misalignment, governance")])
p("Analogy: a smart thermostat that holds 21°C is an AI agent. A smart home whose weather, energy-price, schedule, appliance and "
  "security agents pre-cool the house with solar power before a heatwave hits at peak price is agentic AI.")
src("Source: Sapkota, Roumeliotis & Karkee, 'AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges', Information Fusion (2025), arXiv 2505.10468.")

h2("1.3 The Agentic Loop")
p("Every agent task runs the same repeating cycle: **gather context → take action → verify work → repeat** until the goal is met. "
  "ReAct (2022) describes the same idea as Thought → Action → Observation.")
table(["Step", "What the agent does", "Lab 1 example"], [
    ("Gather context", "Reads files and memory, searches, calls tools", "Loads AGENTS.md, reads 60 reviews, searches cold-brew trends"),
    ("Take action", "Writes files, runs commands, calls APIs/MCP tools", "Writes review-insights.md and research-brief.md"),
    ("Verify", "Checks results — checklist, test, screenshot, second agent", "Every claim needs a review ID or URL"),
    ("Repeat", "Feeds results back as new context", "Revises the brief after your challenge")])
bullets(["Give direction, not micro-steps — state the goal, constraints and definition of done.",
         "Verification is everything — an agent is only as good as its ability to check its work.",
         "Steer mid-loop — review plans and drafts early, send work back with specific feedback.",
         "Context is the fuel — what the agent can see decides what it can do."])
src("Sources: Anthropic, Building agents with the Claude Agent SDK (Sep 2025); Yao et al., ReAct (arXiv 2210.03629).")

h2("1.4 Harness Engineering")
p("**Agent = Model + Harness.** The harness is everything around the model that turns it into a dependable worker. Harness "
  "engineering is designing that environment — and treating every agent mistake as something to fix permanently in the "
  "environment rather than re-explaining it in chat. Anthropic described long-running agent harnesses in Nov 2025; Mitchell "
  "Hashimoto named 'engineer the harness' and OpenAI's Codex team popularised 'harness engineering' in Feb 2026 "
  "('Humans steer. Agents execute.' — ~1M lines of code with no hand-written code).")
table(["Harness component", "What it does", "Where you use it"], [
    ("Agent loop", "Runs gather → act → verify → repeat", "Every Hermes and Paperclip run"),
    ("Tools & MCP", "Lets the model act", "Web search, files, terminal, image generation"),
    ("Context management", "Keeps the right tokens in the window", "AGENTS.md, company instructions"),
    ("Memory", "Persists across sessions", "MEMORY.md / USER.md; Paperclip history"),
    ("Skills", "Procedural know-how on demand", "kopi-brand-voice, campaign planner, compliance audit"),
    ("Verification", "Checklists, auditors, verifiers", "Self-check tables, auditor profile, swarm verifier"),
    ("Guardrails", "Permissions, budgets, approval gates", "Telegram APPROVE, blocked tasks, Board approvals, budgets"),
    ("Sub-agents & orchestration", "Focused agents, coordinated", "Profiles + Kanban, swarms, Paperclip org chart"),
    ("Observability", "Logs, costs, audit trail", "Kanban history, Audit → Activity/Costs")])
src("Sources: Anthropic, Effective harnesses for long-running agents (Nov 2025); M. Hashimoto, My AI Adoption Journey (Feb 2026); OpenAI, Harness engineering (Feb 2026).")

h2("1.5 How an Agent Works: Perception · Brain · Action")
p("The survey 'The Rise and Potential of Large Language Model Based Agents' (Xi et al., Fudan University, arXiv 2309.07864) frames "
  "an LLM agent as three parts working in a closed loop with its environment.")
table(["Part", "Role", "Includes"], [
    ("Perception", "Sense the world — from data to information", "Multimodal input (text, image, audio, video); environment interaction (tools, web, files); information retrieval (search, RAG, memory); world modelling"),
    ("Brain", "Core cognition and decisions — from understanding to decisions", "Knowledge (pre-trained, domain, common sense); memory (short- and long-term); reasoning (logic, reflection, self-correction); planning (decompose, set goals, adapt)"),
    ("Action", "Change the world — from decisions to action", "Task execution (code, tools, operations); environment feedback (results, rewards); behaviour optimisation and autonomous evolution")])
p("Perception → decision → action → feedback → new perception. In Lab 3 the feedback is literally your APPROVE / EDIT / REJECT reply on Telegram.")

h2("1.6 Memory: Short-Term and Long-Term")
table(["Memory type", "Human analogy", "What the agent keeps", "Where you see it"], [
    ("Short-term / working", "What you are thinking about now", "The context window: instructions, chat, tool results, current plan", "Every session; compaction when it fills"),
    ("Episodic (long-term)", "'What happened'", "Past sessions, actions and outcomes", "Hermes session search; Kanban and Paperclip history"),
    ("Semantic (long-term)", "'Facts I know'", "Facts about the company and user; knowledge bases (RAG)", "MEMORY.md / USER.md; company knowledge"),
    ("Procedural (long-term)", "'How to do things'", "Skills, rules, workflows", "SKILL.md skills; AGENTS.md; agent instructions")])
p("Agents bring long-term memory back into context by **retrieval** (by recency, importance and relevance; RAG and vector search; "
  "just-in-time loading of files), and improve through **reflection** — writing lessons to memory after a failure. In Hermes, "
  "memory files load at session start, so after the agent saves something, start a new session to see it recalled.")
h3("RAG agent vs a standard LLM assistant")
table(["", "RAG agent", "Standard LLM assistant"], [
    ("How it answers", "Retrieves from a curated, current corpus, then generates", "From training data alone"),
    ("Strengths", "Grounded, cited, auditable; uses live company data", "Fast to deploy; low maintenance"),
    ("Limitations", "Quality depends on corpus freshness, chunking and retrieval settings", "Stale knowledge; hallucination; no provenance"),
    ("Maintenance", "Re-index and review sources regularly", "Minimal"),
    ("Evaluate on", "Accuracy, relevance, latency, cost, maintenance effort", "Same metrics")])
src("Sources: Sumers et al., CoALA (arXiv 2309.02427); Park et al., Generative Agents (2023); Shinn et al., Reflexion (2023).")

h2("1.7 World Models")
p("LLMs predict the next word; **world models** predict how the state of the world changes after an action, so an agent can "
  "simulate 'what if I do X?' before acting. They matter for planning, physical AI (robots, vehicles), safe training in generated "
  "worlds, and grounding.")
table(["Date", "System", "What it is"], [
    ("Jan 2025", "NVIDIA Cosmos", "World foundation models for robots and autonomous vehicles"),
    ("Jun 2025", "Meta V-JEPA 2", "Video world model; zero-shot robot pick-and-place"),
    ("Aug 2025", "Google DeepMind Genie 3", "Interactive worlds from text at 24 fps, 720p"),
    ("Nov 2025", "World Labs Marble", "Persistent, editable 3D worlds from text or images"),
    ("Mar 2026", "AMI Labs (Yann LeCun)", "US$1.03B raised to build JEPA-based world models")])

h2("1.8 From Single Agent to Human–Agent Collaboration")
table(["Paradigm", "Forms", "In this course"], [
    ("Single agent", "Task-oriented, innovation-oriented, lifecycle-oriented", "Labs 1–2: one agent researches and runs a campaign"),
    ("Multi-agent", "Cooperative — ordered (SOP pipeline) or disordered (discussion, voting); adversarial (debate)", "Lab 4 ordered pipeline; Lab 5 parallel swarm with a verifier"),
    ("Human–agent collaboration", "Instructor–executor (humans instruct and give feedback); equal partnership (agents as peers)", "Lab 3 APPROVE gate; Day 2 Board approvals; CEO proposes, you decide")])
p("Without rules, multi-agent conversation can amplify small hallucinations — add verifiers, cross-checks and human checkpoints. "
  "At scale, agents form an **agent society**: individual behaviour, group interaction, personality (SOUL.md, instructions) and "
  "social emergence — and 'Agent-as-a-Service', the idea behind Paperclip.")
h3("Levels of autonomy — pick per task, not per agent")
table(["Level", "Your role", "What the agent does", "Course example"], [
    ("L1", "Operator", "Acts only when invoked for a subtask", "A one-off question to Mia"),
    ("L2", "Collaborator", "Plans and works with you", "Lab 2 drafting with feedback"),
    ("L3", "Consultant", "Does most of the work; asks for expertise", "Lab 1 brief; Lab 7 hiring plan"),
    ("L4", "Approver", "Asks only at high-risk steps or approvals", "Lab 3 APPROVE; Lab 9 weekly routine"),
    ("L5", "Observer", "Works alone; you monitor with an off-switch", "Lab 5 weekly report cron")])
table(["Pattern", "Definition", "Use for"], [
    ("Human-in-the-loop", "A person approves BEFORE the action", "Irreversible, public, regulated actions"),
    ("Human-on-the-loop", "Agent acts; a person monitors and can intervene", "High-volume, reversible work"),
    ("Human-out-of-the-loop", "Fully autonomous", "Only low-risk, bounded, reversible tasks")])
src("Sources: Xi et al. (arXiv 2309.07864); Feng, McDonald & Zhang, Levels of Autonomy for AI Agents (arXiv 2506.12469).")

h2("1.9 The 2026 Agent Market")
table(["Product", "Vendor · launch", "Type", "Human-in-the-loop"], [
    ("OpenClaw", "OpenClaw Foundation · Nov 2025 (renamed Jan 2026)", "Open-source personal agent on your machine, via chat apps", "DM pairing; optional sandbox"),
    ("Hermes Agent", "Nous Research · ~Feb 2026", "Open-source, self-improving agent; memory, skills, cron, profiles, Kanban", "Approval modes; allow-lists"),
    ("Paperclip", "Paperclip Labs · Mar 2026", "Open-source company of agents (org chart, budgets)", "Board approvals; budgets auto-pause; audit log"),
    ("OpenAI Dots", "OpenAI · 29 Sep 2026", "Always-on agents with their own cloud computer (ChatGPT, Slack, Teams)", "Custom rules: allow / approve / block"),
    ("Meta Muse", "Meta · 8 Sep 2026 (US)", "Personal agent for life admin (app, web, WhatsApp)", "Confirms sensitive actions; Sentinel guard agent"),
    ("Block Buzz", "Block · 21 Jul 2026", "Open-source workspace for humans and agents (Nostr)", "Agent identities and permissions"),
    ("Manus Cue", "Manus · 28 Sep 2026", "Agents with their own email, phone, wallet and computer", "Budgets; you make the final call"),
    ("Claude Cowork / Claude Code", "Anthropic · 2025–2026", "Desktop and coding agents with sub-agents", "Manual / Auto / Skip permission modes"),
    ("OpenAI Codex", "OpenAI · 2025–2026", "Parallel coding agents", "Review before merge; sandboxes"),
    ("Gemini Enterprise agents", "Google · 8 Oct 2026", "Sub-agents and persistent 'coworker' agents", "Agent identity, gateway, spend caps"),
    ("Microsoft Agent 365", "Microsoft · May 2026", "Governance control plane for many agents", "Registry, access control, DLP")])
p("Read the market in four groups: **personal agents** (one agent for one person), **workspaces and companies** (many agents and "
  "humans with roles), **governance layers** (registries, identities, budgets) and **open vs closed** (self-host and own your data, "
  "or convenience and managed security). This course uses two open-source platforms: Hermes Agent — an employee that learns — and "
  "Paperclip — the company you govern.")
src("Sources: vendor announcements and repositories, verified Oct 2026. Products change quickly — check before you buy.")

h2("1.10 Singapore in Focus")
img(os.path.join(SHOTS, "screenshots", "st-agentsea.png"), "The Straits Times, 24 Aug 2026 — 'New platform to create AI agents available to all public healthcare professionals'", 3.6)
p("**AgentSea**, an agentic AI platform by national healthtech agency Synapxe and AWS, lets Singapore's 80,000+ public healthcare "
  "professionals create their own AI agents in natural language. Since its launch at the end of May 2026, more than **12,000 agents** "
  "have been created and 300+ shared for reuse. A National Heart Centre Singapore cardiologist halved his pre-consultation "
  "preparation, and KK Women's and Children's Hospital built an agent that generates daily rosters. Guardrails protect patient "
  "data, and clinicians still verify: the tool 'has not replaced the need for verification or my own clinical assessment'. "
  "Announcing it at HIMSS26 APAC, Senior Minister of State Tan Kiat How said: 'We are moving from AI as assistant to AI as actor.'")
p("Singapore's governance anchor is IMDA's **Model AI Governance Framework for Agentic AI** (launched 22 Jan 2026; updated May 2026), "
  "with four dimensions: assess and bound risks upfront, meaningful human accountability (including approval checkpoints), technical "
  "controls, and end-user responsibility. GovTech's AI Assistant Desk keeps a registry of each agent's owner and purpose.")
src("Sources: The Straits Times (Zhaki Abdullah, 24 Aug 2026); Synapxe and MOH releases (24 Aug 2026); IMDA (Jan/May 2026).")

h2("1.11 Human–AI Collaboration in Action")
table(["Domain", "Example", "What the agent does", "What the human does"], [
    ("Science", "Google AI co-scientist (2025)", "Generates, debates and ranks hypotheses", "Sets the goal, picks hypotheses, runs wet-lab tests (3 of 5 leukaemia ideas worked)"),
    ("Science", "Edison Kosmos (2025)", "Reads ~1,500 papers, writes ~42,000 lines of analysis per run", "Sets the objective, judges which findings matter"),
    ("Mathematics", "Gemini Deep Think (2025)", "Writes natural-language proofs", "IMO coordinators certify — gold, 35/42"),
    ("Mathematics", "AlphaEvolve + Terence Tao (2025–26)", "Evolves programs and constructions", "Defines the problem, WRITES the evaluator, proves and generalises"),
    ("Drug discovery", "AlphaFold 3 (2024)", "Predicts biomolecular structures", "Chooses targets, validates in the lab (2024 Nobel Prize)"),
    ("Drug discovery", "Insilico rentosertib (2025)", "Found the TNIK target and designed the molecule", "Clinicians ran the Phase 2a trial; regulators approved"),
    ("Healthcare", "Microsoft MAI-DxO (2025)", "Virtual panel orders tests step by step", "Clinician owns diagnosis (benchmark only)"),
    ("Finance", "Goldman Sachs + Anthropic (2026)", "Trade accounting, client onboarding", "Staff review exceptions and approve"),
    ("Software", "OpenAI Codex harness (2026)", "Writes code, tests, CI, docs", "Engineers steer, review, build feedback loops"),
    ("Customer service", "Klarna (2024–25)", "Handles routine chats", "Takes complex cases — human access re-prioritised in 2025"),
    ("Marketing", "This course", "Drafts, designs, schedules, reports", "Sets strategy, approves everything public")])
p("**The pattern:** the agent searches, generates, runs and checks at scale; the human sets the goal, defines 'good' (rubric, evaluator, "
  "tests), approves consequential actions, interprets meaning and owns accountability. Counter-evidence matters too: a 2025 METR trial "
  "found experienced developers 19% slower with early AI tools — the harness and the human make the difference.")

h2("1.12 Risks, Governance and Security")
table(["Challenge", "Mitigation"], [
    ("Hallucination", "Require citations; verifier agents; human spot-checks"),
    ("Security risks (prompt injection, poisoned skills, leaked keys)", "Least privilege, secrets, sandboxes, review skills before installing"),
    ("Explainability", "Logs, Kanban history, Paperclip audit trail"),
    ("Data and bias (PDPA)", "Mask personal data; review outputs"),
    ("Efficiency and cost", "Budgets; cheaper models for simple roles")])
table(["Security principle", "Question it answers", "Control in the labs"], [
    ("Data control", "What can the AI see?", "Only the workspace files it needs"),
    ("Permission control", "What can the AI do?", "Approval modes; allow-listed Telegram user"),
    ("Human approval", "When must it ask?", "APPROVE on Telegram; blocked publish task; Board approvals"),
    ("Monitoring & audit", "What did it do?", "Kanban history; Audit → Activity/Costs"),
    ("Kill switch", "How do I stop it?", "hermes pause; Paperclip Pause; disable routines")])

h2("1.13 Activity — Human–AI Workforce Canvas")
numbered(["In pairs, list 8–10 tasks in Kopi Kaki's #ShiokColdBrew campaign (research, posts, video, replies, reporting …).",
          "Mark the tasks one agent can do end to end (SINGLE).",
          "Mark the tasks that need several specialised agents — pipeline or swarm (TEAM).",
          "Mark the decisions that must stay human, and why — risk, accountability, judgement (HUMAN).",
          "Draw where the human approves: before public posts, refunds, spend.",
          "Start the Hermes Agent install now (Lab 1, step 1). Once installed, ask Hermes to critique your canvas:"])
code("Here is our Human-AI Workforce Canvas for Kopi Kaki Co.'s #ShiokColdBrew campaign:\n<paste your task list with SINGLE / TEAM / HUMAN labels and approval checkpoints>\n\nAct as an operations consultant. For each task:\n1. Agree or disagree with our label and say why (risk, reversibility, volume, judgement).\n2. Suggest the autonomy level (L1 Operator ... L5 Observer).\n3. Name one control (approval gate, budget, audit, verifier) we must add.\nEnd with the 3 biggest risks in our design.", "text")

# ====================================================================== labs
LAB_SHOTS = {
    1: ("screenshots/hermes-dashboard.png", "Lab 1 — the Hermes dashboard: sessions of your onboarded agent (hermes dashboard)"),
    2: ("screenshots/hermes-skills.png", "Lab 2 — the Skills page: your kopi-brand-voice and social-campaign-planner skills appear here"),
    3: ("screenshots/hermes-channels.png", "Lab 3 — the Channels page: Telegram connected to the gateway"),
    4: ("screenshots/hermes-kanban.png", "Lab 4 — the Kanban board: the video studio's tasks, dependencies and the blocked posting gate"),
    5: ("screenshots/hermes-profiles.png", "Lab 5 — Profiles: analyst, listener, strategist, researcher and auditor run the swarm"),
    6: ("paperclip/pc-adapters.png", "Lab 6 — Settings → Adapters: the runtime your CEO agent runs on"),
    7: ("paperclip/pc-org.png", "Lab 7 — the Agents org chart view: Board → CEO → specialists"),
    8: ("paperclip/pc-tasks.png", "Lab 8 — Tasks moving todo → in_progress → in_review → done"),
    9: ("paperclip/pc-routine-pipeline.png", "Lab 9 — a routine's generated task delegating each stage"),
    10: ("paperclip/pc-agents.png", "Lab 10 — agents with status and budgets: pause, re-budget, improve"),
}

def lab_section(L):
    h2(f"Lab {L['num']} — {L['title']}")
    p(f"**Day {L['day']} · {L['minutes']} min · {L['paradigm']} · {L['lo']}** — {L['hook']}")
    h3("Business scenario"); p(L["scenario"])
    h3("Goal"); p(L["objective"])
    if L.get("prereq"): h3("Before you start"); bullets(L["prereq"])
    shot = LAB_SHOTS.get(L["num"])
    if shot: img(os.path.join(SHOTS, *shot[0].split("/")), shot[1], 5.0)
    h3("You will deliver"); bullets(L["deliverables"])
    table(["Who", "Role"], [("Agents", L["agents"]), ("You (human)", L["human"])])
    h3("Concepts in action"); bullets(L["concepts"])
    h3("Lab files")
    p(f"labs/{L['slug']}/ — README.md, LAB-{L['num']:02d}-Instructions.pdf, COPY-PROMPTS.txt and data/. Copy data/ into ~/kopi-kaki.")
    h3("Step-by-step")
    for i, st in enumerate(L["steps"], 1):
        p(f"**Step {i} — {st['title']}**")
        if st.get("body"): p(st["body"])
        if st.get("cmd"): code(st["cmd"], "bash")
        if st.get("prompt"):
            p(f"Prompt — paste into *{st.get('where', 'Hermes chat')}*:"); code(st["prompt"], "text")
        if st.get("expect"): p(f"✓ Expected: {st['expect']}")
    h3("Test it"); B.append(("testit", L["check"], L["verify"]))
    h3("Troubleshooting"); table(["Symptom", "Fix"], L["trouble"])
    h3("Stretch challenge"); p(L["challenge"])

h1("Topic 2 — " + C.TOPICS[1]["title"])
p("Hermes Agent (Nous Research, MIT licence) is a self-hosted, self-improving agent with persistent memory, skills, tools and MCP, a "
  "messaging gateway (Telegram and 15+ channels), a cron scheduler, and profiles + a Kanban board for multi-agent teams. On Day 1 you "
  "take it from one AI employee to a supervised five-agent studio.")
img(os.path.join(SHOTS, "screenshots", "hermes-dashboard.png"), "The Hermes dashboard (hermes dashboard → http://127.0.0.1:9119)", 5.2)
table(["File / place", "What it holds", "Loaded"], [
    ("AGENTS.md (in the folder you start Hermes in)", "Company context and rules", "Every session in that folder"),
    ("~/.hermes/SOUL.md (per profile)", "The agent's role, personality, standing rules", "Every session"),
    ("~/.hermes/memories/MEMORY.md and USER.md", "What the agent chose to remember; what it knows about you", "Session start"),
    ("~/.hermes/skills/", "Skills (SKILL.md folders)", "On demand, by description"),
    ("Kanban board", "Tasks, dependencies, comments, history", "Dispatched by the running gateway")])
for L in LABS[:5]: lab_section(L)

h1("Topic 3 — " + C.TOPICS[2]["title"])
p("Paperclip (MIT licence) is open-source orchestration for a company of agents. You are the **Board**; a CEO agent reports to you and "
  "specialists report to the CEO. Agents run on adapters you already have (Claude Code, Codex, Gemini CLI, Hermes …). Goals, projects "
  "and tasks give every run a purpose; routines and heartbeats make work recurring; budgets (80% warning, 100% auto-pause), approval "
  "gates and an append-only activity log keep it governed.")
img(os.path.join(SHOTS, "paperclip", "pc-dashboard.png"), "The Paperclip dashboard (http://localhost:3100)", 5.2)
table(["", "Hermes Agent (Day 1)", "Paperclip (Day 2)"], [
    ("Unit", "An agent — or a team of profiles", "A company of agents"),
    ("Orchestration", "Kanban, dependencies, swarms", "Org chart, CEO delegation, projects and tasks"),
    ("Human control", "APPROVE prompts, approval modes, blocked tasks", "Hiring gate, Approvers on tasks, Board approvals"),
    ("Scheduling", "Cron jobs", "Routines + heartbeats"),
    ("Cost control", "Model choice per profile", "Budgets per agent / project / company"),
    ("Audit", "Sessions, Kanban history", "Audit → Activity, Runs, Costs, Budgets")])
for L in LABS[5:]: lab_section(L)

# ====================================================================== close
h1("Assessment Preparation")
bullets([C.ASSESSMENT["written"], C.ASSESSMENT["practical"],
         "Open book: slides, this Learner Guide and approved materials only.",
         "Practice at https://exams.tertiaryinfotech.com before the assessment.",
         "On the day: TRAQOM survey → Assessment digital attendance → WA then PP → submit on the LMS → sign the Assessment Summary Record."])
h1("Glossary")
table(["Term", "Meaning"], [
    ("AI agent", "An autonomous LLM-based program that pursues a goal with tools in a bounded environment"),
    ("Agentic AI", "A system of multiple specialised agents with orchestration, shared memory and coordinated autonomy"),
    ("Agentic loop", "Gather context → act → verify → repeat"),
    ("Harness", "Everything around the model: loop, tools, context, memory, skills, verification, guardrails, orchestration, observability"),
    ("Skill", "A SKILL.md folder of procedural know-how an agent loads on demand"),
    ("Profile (Hermes)", "An isolated agent with its own SOUL.md, memory, skills and sessions"),
    ("Kanban (Hermes)", "A durable task board with dependencies, comments, reviews and swarms shared by profiles"),
    ("Cron / routine", "A schedule that starts agent work without a human prompt"),
    ("Human-in-the-loop", "A person approves before an action happens"),
    ("Human-on-the-loop", "A person monitors and can intervene while the agent acts"),
    ("Board (Paperclip)", "The human owner who approves hires, strategy and gated work"),
    ("Adapter (Paperclip)", "The agent runtime an employee runs on (Claude Code, Codex, Gemini CLI, Hermes …)"),
    ("RAG", "Retrieval Augmented Generation — retrieve from a curated corpus, then generate"),
    ("World model", "A model that predicts how the world changes after an action"),
    ("MCP", "Model Context Protocol — an open standard for connecting agents to tools and data")])

# ====================================================================== renderers
def _anchor(t): return re.sub(r"[^a-z0-9 -]", "", t.lower()).replace(" ", "-")
def render_md():
    o = [f"# Learner Guide — {C.TITLE}", "", f"**{C.COURSE_CODE} · Version {C.VERSION.lstrip('v')} · {C.VERSION_DATE} · {C.ORG} ({C.UEN})**", "",
         "> Markdown mirror of `courseware/LG-" + C.SHORT_TITLE + ".docx` — generated from the same source.", "", "## Contents", ""]
    o += [f"- [{b[1]}](#{_anchor(b[1])})" for b in B if b[0] == "h1"] + [""]
    for b in B:
        k = b[0]
        if k == "h1": o += [f"## {b[1]}", ""]
        elif k == "h2": o += [f"### {b[1]}", ""]
        elif k == "h3": o += [f"#### {b[1]}", ""]
        elif k == "p": o += [b[1], ""]
        elif k == "bullets": o += [f"- {x}" for x in b[1]] + [""]
        elif k == "numbered": o += [f"{i}. {x}" for i, x in enumerate(b[1], 1)] + [""]
        elif k == "code": o += [f"```{b[2]}", b[1], "```", ""]
        elif k == "note": o += [f"> **Note:** {b[1]}", ""]
        elif k == "testit": o += [f"> **✅ Test it:** {b[1]}", ">"] + [f"> - [ ] {v}" for v in b[2]] + [""]
        elif k == "src": o += [f"<sub>{b[1]}</sub>", ""]
        elif k == "img":
            rel = os.path.relpath(b[1], REPO)
            o += [f"![{b[2]}]({rel.replace(' ', '%20')})", f"*{b[2]}*", ""]
        elif k == "table":
            o += ["| " + " | ".join(b[1]) + " |", "|" + "---|" * len(b[1])]
            o += ["| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |" for r in b[2]] + [""]
    return "\n".join(o)

with open(os.path.join(REPO, f"LG-{C.SHORT_TITLE}.md"), "w", encoding="utf-8") as f:
    f.write(render_md())

doc = Document()
normal = doc.styles["Normal"]; normal.font.name = "Arial"; normal.font.size = Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "Learner Guide", C.TITLE, C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"), course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, PRIOR + [V20])
prodoc.add_toc(doc)

def add_md_runs(par, text, size=None, color=None):
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text):
        if not part: continue
        if part.startswith("**"): r = par.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*"): r = par.add_run(part[1:-1]); r.italic = True
        else: r = par.add_run(part)
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color

def shade_par(par, hexc):
    pPr = par._p.get_or_add_pPr(); shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexc); pPr.append(shd)

for b in B:
    k = b[0]
    if k in ("h1", "h2", "h3"):
        doc.add_heading(b[1], level={"h1": 1, "h2": 2, "h3": 3}[k])
    elif k == "p":
        add_md_runs(doc.add_paragraph(), b[1])
    elif k == "bullets":
        for x in b[1]: add_md_runs(doc.add_paragraph(style="List Bullet"), x)
    elif k == "numbered":
        for x in b[1]: add_md_runs(doc.add_paragraph(style="List Number"), x)
    elif k == "code":
        for line in b[1].split("\n"):
            par = doc.add_paragraph(); par.paragraph_format.space_after = Pt(0); par.paragraph_format.left_indent = Inches(0.15)
            r = par.add_run(line if line else " "); r.font.name = "Consolas"; r.font.size = Pt(9)
            shade_par(par, "F3F1EB")
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    elif k == "note":
        par = doc.add_paragraph(); shade_par(par, "FDF0EA"); add_md_runs(par, "Note: " + b[1], size=10)
    elif k == "testit":
        t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"; c = t.rows[0].cells[0]
        prodoc._shade_cell(c, "E8F7EE"); c.text = ""
        r = c.paragraphs[0].add_run("✅ Test it — " + b[1]); r.bold = True; r.font.size = Pt(10.5)
        for v in b[2]:
            pp = c.add_paragraph(); rr = pp.add_run("☐  " + v); rr.font.size = Pt(10)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    elif k == "src":
        par = doc.add_paragraph(); add_md_runs(par, b[1], size=8.5, color=RGBColor(0x6B, 0x68, 0x62))
    elif k == "img":
        if os.path.exists(b[1]):
            par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            par.add_run().add_picture(b[1], width=Inches(b[3]))
            cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_md_runs(cap, b[2], size=9, color=RGBColor(0x6B, 0x68, 0x62))
    elif k == "table":
        head, rows = b[1], b[2]
        t = doc.add_table(rows=1, cols=len(head)); t.style = "Table Grid"
        for i, h in enumerate(head):
            c = t.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); prodoc._shade_cell(c, "1F6FEB")
        for row in rows:
            cells = t.add_row().cells
            for i, v in enumerate(row):
                cells[i].text = ""; r = cells[i].paragraphs[0].add_run(str(v)); r.font.size = Pt(9.5)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)

prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
OUT = os.path.join(REPO, "courseware", f"LG-{C.SHORT_TITLE}.docx")
doc.save(OUT); print("Saved", OUT, "and LG markdown")
