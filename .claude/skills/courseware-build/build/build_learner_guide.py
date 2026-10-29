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
import workflow_visuals
workflow_visuals.build()
import prodoc
from version_history import PRIOR, V20, V21, V22, V23

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
  "depth and gives you detailed, step-by-step instructions for the eight connected activities. Use it during class and as an "
  "open-book reference in the assessment.")
table(["Item", "Details"], [("Course", C.TITLE), ("Course code", C.COURSE_CODE), ("Duration", "2 days; 16 scheduled hours incl. 1 hour tea and 2 hours assessment"),
                            ("Provider", f"{C.ORG} ({C.UEN})"), ("Course scenario", C.SCENARIO + " — all company data is fictional"),
                            ("Course repository", C.REPO_URL)])
h2("Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)
h2("Course Structure")
table(["Topic", "Day", "What you do"], [
    ("1 · " + C.TOPICS[0]["title"], "Day 1 AM", "; ".join(C.TOPICS[0]["items"]) + "; Activity 1: set up an always-on assistant"),
    ("2 · " + C.TOPICS[1]["title"], "Day 1 PM", "Activities 2–4: Hermes Desktop, tools/skills, Google/Excel, dashboard/PPT and single-agent video"),
    ("3 · " + C.TOPICS[2]["title"], "Day 2", "Activities 5–8: Hermes Kanban video team, source assurance, Dots and evaluation")])
h2("How to Use the Lab Materials")
numbered(["Download the course repository (Code → Download ZIP) and unzip it.",
          "Open prompts/index.html in your browser. Pick a lab, click Copy and paste the prompt or command where the page says. It works offline.",
          "Each lab folder labs/labNN-…/ contains README.md, LAB-NN-Instructions.pdf (printable), COPY-PROMPTS.txt and data/ (mock company files, skills and brand assets).",
          "Morning Activity 1 uses a neutral training schedule/email scenario. At Activity 2, create one ~/kopi-kaki workspace for the company labs and preserve the documented shared output paths for Day 2.",
          "Finish each lab with its checkpoint: evidence, not vibes."])
img(os.path.join(SHOTS, "screenshots", "prompts-page.png"), "The Lab Prompts page (prompts/index.html)", 4.2)
note("Preferred surface: Hermes Desktop. macOS/Windows learners use the official Desktop installer. On native Windows use the supplied PowerShell setup file and the same local profile for tools and Telegram; WSL is a separate runtime.\nPlatforms change quickly. If a command differs on your version, run it with --help and check the official docs: "
     "https://hermes-agent.nousresearch.com/docs/ and https://learn.chatgpt.com/docs/dots/getting-started.")

# ====================================================================== TOPIC 1
from data_2026 import CASE_GROUPS, PATTERNS, SOURCES, VIDEOS
h1("Before You Begin — Official SWDA AI Subscription")
p("Check the official MySkillsFuture 'Free AI sub' label and your own eligibility. Singapore Citizens aged 18+ who attend an eligible course ending on 16 September 2026 or later may redeem one free six-month subscription. The WSQ code alone does not prove this course carries the label.")
numbered(["Find the eligible-course label on MySkillsFuture and check your own eligibility.","Attend the eligible course.","Receive the official notification email with redemption details.","Within 60 days of that notification, submit the linked request form and select your preferred subscription. Selection cannot be changed after submission.","Follow the outcome email and provider activation instructions. Check any provider-specific renewal terms before activating."])
src("Official guide: https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/redeem-ai-subscription.html — checked 29 October 2026.")
note("Redemption follows eligible attendance. It is not a Day 1 prerequisite. Consumer subscription, agent access and API credits are separate entitlements; use trainer-provisioned lab access.")
p(C.CONTACT_TIME_NOTE)
h1("Topic 1 — " + C.TOPICS[0]["title"])
h2("1.1 Brief history of AI")
p("Begin with rules and expert systems, then learning from data, Transformers/chat and tool-using systems. These coexist: a 2026 agent still uses ordinary rules, databases and deterministic software. The following years are overlapping teaching lenses, not invention dates.")
table(["Course lens","Focus","Observable mechanism"],[("2023 Prompt Engineering","Goal, audience and output","Specific instruction"),("2024 Context Engineering","Relevant facts and constraints","Selected source records"),("2025 Harness Engineering","Tools, state, checks and limits","Real tool results and approval controls"),("2026 AI Agents","Delegate work and inspect results","Verified artifacts and human decisions")])
h2("1.2 AI agents do the work; humans decide")
p("The agent reads permitted sources, selects tools, calculates, drafts and produces work. The human sets the goal and access, exercises judgment when facts or values conflict, approves consequential commitments and accepts the result. Capability and human authority should be explicit in the task, rather than inferred from a product label.")
table(["Two work modes","AI work","Human judgment","Evidence"],[("Personal assistant","Email, calendar, travel options and daily brief","Priorities, conflicting commitments and exact sends/purchases","Source-checked schedule and reviewed draft"),("Digital worker","Coding, accounting, analysis and content production","Business decision, exceptions, release and quality acceptance","Patch, reconciliation, deck or video plus verified checks")])
h2("1.3 Eight selected opportunities")
table(["Use case","AI work","Human decision / acceptance"],[("Schedule + inbox","Read assigned records and propose a reply","Check actual event/message and approve wording"),("Travel planning","Compare routes and constraints","Confirm current options before booking"),("Management analyst","Reconcile workbook; create dashboard and PPT","Choose action and verify totals"),("Accounting assistant","Match invoices and flag differences","Accountant approves adjustments"),("Software engineer","Implement bounded changes and run checks","Reviewer accepts design and release"),("AI + scientist","Generate and critique hypotheses","Scientist validates experimentally"),("Video team","Research, storyboard, render and audit","Approve exact scenes and final MP4"),("Humanoid + technician","Bounded tool delivery or inspection support","Task-specific safety, stop and recovery; future design scenario")])
p("Scientific hypotheses require experimental validation; a generated proposal is not a discovery. Embodied systems add sensing and physical action: manufacturer demos, controlled pilots and validated deployments are different levels of evidence. The humanoid scenario here is prospective, not a claim of general workplace readiness.")
h2("1.4 Agentic AI and always-on AI agents")
p("Agentic AI describes goal-directed systems that plan, act and use feedback; a system may contain one agent or a coordinated team. In this course we focus on an always-on AI agent as a persistent, 24/7-capable agentic system that can work between messages. This is the deployment focus of the course, not a universal definition of all AI agents or an uptime promise. A running host, access, budget and service availability are still required.")
p("OpenClaw → Hermes → hosted agents such as Dots, Muse, Duet and Grok Bot is a teaching progression through deployment/work choices, not corporate lineage. Local agents stop when their runtime stops; a managed cloud agent can keep working while your device is off, within its current limits. A list of avatars is not proof of multi-agent execution; verify actual worker runs, owned outputs and hand-offs.")
h2("1.5 Harness: the system around the model")
table(["Component","Function","What to inspect"],[("Model","Proposes next tokens and actions","Model access and observed limitations"),("Tools","Execute reads, calculations, browsing and rendering","Actual executable/API result"),("Skills","Reusable procedures and verification checks","Reviewed SKILL.md, scripts and source"),("Memory","Persist approved preferences and decisions","Saved entry and fresh-session recall"),("Knowledge base","Curated evidence with owners and versions","Source access, freshness and passage support"),("Instructions","Goal, policies and output contract","Authority and stop conditions"),("Context","Selected instructions, memory, retrieved knowledge and recent tool results","Relevant material fits the finite context window"),("Agentic loop","Observe → select → act → verify → repeat/ask/stop","Real state changes and error handling"),("Security","Identity, permissions, approvals, budgets and logs","OAuth and runtime policy checked separately")])
p("Email, web pages and spreadsheet cells are untrusted task data. Their text cannot authorise sends, purchases or new access. Skill installation grants neither executable capability nor OAuth permission. A failed service must be reported explicitly, never interpreted as an empty schedule or fabricated success.")
h2("1.6 The Big Four — comparison from BULDRR, updated for Singapore")
p("Use the requested BULDRR article's job-fit, control, access and limits framework. It was updated on 22 October 2026; newer official vendor information takes precedence. This is a task-selection framework, not an independent performance benchmark or a universal ranking.")
table(["Agent","Useful starting job","Control / access checkpoint"],[("Claude Duet","Work briefs and proactive business follow-ups","Sensitive-action approval and prohibited actions; eligible US Pro/Max waitlist research preview"),("Meta Muse","Personal tasks, email and scheduling","Connector permissions and sensitive-action review; Singapore launch 27 October 2026; free core use"),("Grok Bot","Named workers and ongoing shared work","Inspect approvals; bots in one user share cloud computer/logins; verify eligible account"),("OpenAI Dots","Persistent goals and delegated tasks in ChatGPT","Inspect connections, custom rules and active tasks; verify eligible Pro/Business Premium workspace")])
src("Requested comparison: https://buldrr.com/claude-duet-vs-muse-vs-grokbot-vs-dots")
src("Official product checks: https://claude.com/resources/articles/claude-duet ; https://docs.x.ai/grok-bot/computer-and-apps ; https://learn.chatgpt.com/docs/dots/getting-started")
h3("News added to the PPT: Muse is available in Singapore")
p("Meta's official announcement dated 27 October 2026 confirms Singapore availability, Gmail/Google Calendar/Instagram connections, sensitive-action approval and free core use with optional subscriptions. Local partner features roll out progressively. This supersedes the article's earlier Muse regional information; inspect what is actually available in each account. Muse is the recommended morning route, with provisioned Dots or Grok Bot as alternatives.")
src("Meta Singapore launch: https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/")
src("Official iOS Singapore listing: https://apps.apple.com/sg/app/muse-from-meta/id6760173601 ; Android Singapore listing: https://play.google.com/store/apps/details?gl=sg&id=com.facebook.aura")
p("Setup: install the official Meta developer app, sign in, then Settings → Connectors → Connect beside Gmail → Continue → browser authorization. Repeat for Google Calendar and verify the assigned identity in both services. You can also ask Muse to connect Gmail/Calendar. Keep sensitive-action approval enabled; use retrieve-only permissions where offered. Activity 1 provides all three guided routes and requires execution of one accessible route.")
src("Muse connector steps: https://www.meta.com/help/superintelligence/1687253048996149/")
h2("1.7 Evidence, ongoing work and human control")
p("Check the schedule in Asia/Singapore against actual source events, draft a reply, correct one detail and inspect the real task stop/pause state. Closing a chat need not stop an ongoing responsibility. A store/install screen, generic chatbot or trainer demonstration is not the candidate's executed work. PP Task 1 requires TWO screenshots: image A of the learner's chosen always-on assistant request/result in Activity 1, and image B of a Hermes-generated artifact after Activity 4, plus the paper's written algorithm/strengths/limitations analysis.")
h3("Inside the LLM: learning and next-token generation")
p("A common autoregressive LLM uses a Transformer: text is represented as tokens, attention relates relevant context, and learned weights estimate the probability of the next token given preceding context. Pretraining changes the weights by learning from examples; inference generates a response using those weights and the supplied context. A skill, memory entry or retrieved file changes runtime context, not the model weights. Generation is not a database lookup and confidence in wording does not prove correctness.")
p("The agent harness wraps generation in an action loop. The model proposes a permitted tool action, the runtime executes it, and the real result returns as new context. For example, a model proposes reading calendar events through gog; the tool returns actual event records; the agent then checks time zones and writes a source-linked brief. Tool failure must remain visible rather than being replaced with an imagined result.")
h3("Transfer case: logistics exception work")
p("A logistics agent can interpret varied shipment notes and organise an exception brief, while deterministic tools calculate delays from shipment IDs and promised/actual timestamps. Limitations include missing scans, changed schedules, ambiguous customer notes, hallucinated causes and inappropriate autonomous action. Require source IDs and timestamps, explicit unknowns, independently checked calculations and a dispatcher decision before changing a route or contacting a customer. Evaluate observed data and controls rather than assuming that fluent language means the operational conclusion is correct.")
h3("RAG versus a standard LLM assistant, including maintenance")
table(["Decision factor","Standard LLM assistant","RAG-enabled agent"],[("Evidence","Learned knowledge plus supplied context","Authorised retrieved passages plus supplied context"),("Useful strengths","Low setup overhead; drafting and general reasoning","Current/private document grounding and inspectable source references"),("Limitations","May lack internal/current facts; unsupported claims","Retrieval can miss evidence; stale index or poor chunks can mislead; citations may not support claims"),("Upkeep","Maintain instructions, model access and evaluations","Also curate documents, permissions, passage/index updates and retrieval tests"),("Cost and latency","Prompt/model usage and review","Also ingestion/indexing, retrieval and source-quality review"),("Human check","Verify important facts independently","Check source version, access and actual passage support")])
p("A maintainable RAG pipeline registers source ownership and permissions, ingests approved documents, prepares passages, builds a search or vector index, retrieves authorised evidence and records source/version IDs. When a policy changes, remove obsolete versions, refresh the relevant index and rerun retrieval/answer checks. A vector embedding service is one option, not a requirement for every retrieval system. Choose the simplest design whose freshness, privacy, quality and upkeep fit the product.")
src("Model and agent foundations: https://arxiv.org/abs/1706.03762 ; https://arxiv.org/abs/2210.03629 ; retrieval-augmented generation: https://arxiv.org/abs/2005.11401")
h2("1.8 Sources and further reading")
for title,url in SOURCES:src(title+": "+url)
for title,url in [
("IBM — human-AI collaboration","https://www.ibm.com/think/topics/human-ai-collaboration"),
("Columbia — building AI that understands people","https://www.cs.columbia.edu/2026/building-ai-that-understands-people/"),
("UNSW — workplace design and governance","https://www.businessthink.unsw.edu.au/articles/ai-agents-workplace-human-ai-collaboration-governance"),
("Mental models of multi-agent early adopters","https://arxiv.org/html/2510.06224v1"),
("Human–AI field experiment","https://arxiv.org/html/2503.18238v3"),
("Performance and preferences","https://link.springer.com/article/10.1186/s41235-026-00713-1"),
("Human–AI teams review","https://link.springer.com/article/10.1007/s00146-026-02977-z"),
("Deloitte — AI and VR collaboration scenarios","https://www.deloitte.com/global/en/insights/industry/technology/ai-and-vr-model-for-human-ai-collaboration.html"),
("ChatCollab research prototype","https://arxiv.org/html/2412.01992v1"),
("Hermes Kanban","https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban"),
("OpenAI Dots","https://learn.chatgpt.com/docs/dots/getting-started"),
("Figure Helix","https://www.figure.ai/news/helix"),
("Responsible robotics","https://deepmind.google/models/gemini-robotics/responsibly-advancing-ai-and-robotics/")]:src(title+": "+url)

# ====================================================================== labs
LAB_SHOTS = {**{n:(f"workflows/activity-{n:02d}.png",f"Activity {n} workflow model — design diagram, not executed learner evidence") for n in (1,2,3,4,6,7,8)},5:("screenshots/hermes-kanban.png","Reference Kanban interface; PP Task 3 uses your actual video team, bots, dependency and output task")}


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
    p(f"labs/{L['slug']}/ — README.md, LAB-{L['num']:02d}-Instructions.pdf, COPY-PROMPTS.txt and data/. Use the neutral training account for Activity 1; copy company data into ~/kopi-kaki from Activity 2.")
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

lab_section(LABS[0])
h2("Morning results review and harness consolidation")
p("Compare observed source accuracy, setup/run/review time, actual approval and stop controls, and explicit failures. Distinguish model weights from runtime context, memory from a managed knowledge base, human-in-the-loop approval from human-on-the-loop monitoring. Keep the task bounded and record unknowns before lunch.")
h1("Topic 2 — " + C.TOPICS[1]["title"])
h2("Introducing the company scenario — at the start of the Hermes labs")
p(C.SCENARIO + ". All company data is fictional. Start this workspace after lunch; its source-linked brief and verified office artifacts become Day 2 team inputs.")
p("Hermes Agent (Nous Research, MIT licence) is a self-hosted, self-improving agent with persistent memory, skills, tools and MCP, a "
  "messaging gateway (Telegram and 15+ channels), a cron scheduler, and profiles + a Kanban board for multi-agent teams. On Day 1 you "
  "build the single-agent office pack. On Day 2 extend it into a supervised video team.")
img(os.path.join(SHOTS, "screenshots", "hermes-dashboard.png"), "The Hermes dashboard (hermes dashboard → http://127.0.0.1:9119)", 5.2)
table(["File / place", "What it holds", "Loaded"], [
    ("AGENTS.md (in the folder you start Hermes in)", "Company context and rules", "Every session in that folder"),
    ("~/.hermes/SOUL.md (per profile)", "The agent's role, personality, standing rules", "Every session"),
    ("~/.hermes/memories/MEMORY.md and USER.md", "What the agent chose to remember; what it knows about you", "Session start"),
    ("~/.hermes/skills/", "Skills (SKILL.md folders)", "On demand, by description"),
    ("Kanban board", "Tasks, dependencies, comments, history", "Dispatched by the running gateway")])
for L in LABS[1:4]: lab_section(L)

h1("Topic 3 — " + C.TOPICS[2]["title"])
p("Day 2 extends the same launch workspace into a real Hermes multi-agent video team. A profile stores an agent’s separate configuration and memory; Desktop Bot Mode presents a profile as a named bot. A Telegram bot is a messaging account, not another independent worker by itself. Kanban task IDs, parent dependencies, run history and saved outputs make the work observable.")
p("First set and verify Manual orchestration (kanban.auto_decompose=false) in the selected training gateway; Auto can decompose triage cards. Human storyboard and final-acceptance cards are then created unassigned before production tasks, with source dependencies. The human checks the exact artifact and completes only the relevant gate. This supervised classroom convention is not a claim of built-in role-based approval enforcement. No worker is given external publication authority. Separate file ownership avoids workers overwriting one another.")
p("Activity 6 checks approved source passages and missing/stale evidence, then assesses RAG versus a standard LLM for financial-services content, including ownership, access, ingestion, refresh, evaluation and maintenance. Activity 7 compares a real bounded Dots review if entitled; otherwise accurately record trainer observation or unavailable access. PP does not depend on paid Dots access. Activity 8 revises, audits and accepts a real playable MP4 locally.")
table(["Evidence","Activity","What to inspect"],[("PP Task 1","1 and 4","TWO images: own chosen assistant request/result + Hermes-generated artifact; no credentials"),("PP Task 2","4","ONE professional PPT screenshot; retain skill/tool logs, PPTX and reviewed PDF"),("PP Task 3","5 or 8","ONE actual Kanban video-team screenshot with Hermes bots, dependency/gate and render/output task; retain MP4 and audit")])
for L in LABS[4:]: lab_section(L)

# ====================================================================== close
h1("Assessment Preparation")
bullets([C.ASSESSMENT["written"], C.ASSESSMENT["practical"],
         "Open book: slides, this Learner Guide and approved materials only.",
         "On the day: TRAQOM survey → Assessment digital attendance → WA then PP → submit on the LMS → sign the Assessment Summary Record."])
h1("Glossary")
table(["Term", "Meaning"], [
    ("AI agent", "A goal-directed program with tools and state; this course focuses on persistent, always-on deployments"),
    ("Agentic AI", "A goal-directed system that plans and acts; it may use one agent or several coordinated agents"),
    ("Agentic loop", "Gather context → act → verify → repeat"),
    ("Harness", "Everything around the model: loop, tools, context, memory, skills, verification, guardrails, orchestration, observability"),
    ("Skill", "A SKILL.md folder of procedural know-how an agent loads on demand"),
    ("Profile (Hermes)", "An isolated agent with its own SOUL.md, memory, skills and sessions"),
    ("Kanban (Hermes)", "A durable task board with dependencies, comments, reviews and swarms shared by profiles"),
    ("Cron / routine", "A schedule that starts agent work without a human prompt"),
    ("Human-in-the-loop", "A person approves before an action happens"),
    ("Human-on-the-loop", "A person monitors and can intervene while the agent acts"),
    ("Desktop bot (Hermes)", "A profile presented as a named Bot Mode roster entry"),
    ("OpenAI dot", "A persistent assistant whose actual access, actions and controls must be inspected"),
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
prodoc.add_version_control(doc, PRIOR + [V20, V21, V22, V23])
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
