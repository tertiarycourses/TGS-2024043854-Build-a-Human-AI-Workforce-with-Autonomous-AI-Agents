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
from version_history import PRIOR, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37

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
    ("1 · " + C.TOPICS[0]["title"], "Day 1 AM", "; ".join(C.TOPICS[0]["items"]) + "; Activity 1: join Meta Muse with the trainer’s invite code and set up an OpenAI Dot"),
    ("2 · " + C.TOPICS[1]["title"], "Day 1 PM", "Topic 2 setup in Hermes Desktop (model, Telegram QR, voice, tools, skills, Firecrawl, Gmail connector, scheduled jobs) + Activity 2 website + Activity 3 pitch deck, each by a single agent (PP Task 2)"),
    ("3 · " + C.TOPICS[2]["title"], "Day 2", "Activity 4 five bots in a group chat + Activity 5 Kanban video team (PP Task 3) + Activity 6 content crons, AI security; bonus: Paperclip one-person company")])
h2("How to Use the Lab Materials")
numbered(["Download the course repository (Code → Download ZIP) and unzip it.",
          "Open prompts/index.html in your browser. Pick a lab, click Copy and paste the prompt into Hermes Desktop (or the app the page names). It works offline.",
          "Each lab folder labs/labNN-…/ contains README.md, LAB-NN-Instructions.pdf (printable), COPY-PROMPTS.txt and data/ (mock company files, skills and brand assets).",
          "Morning Activity 1 introduces Kopi Kaki Co.: your assistant checks any of the company's meetings and drafts a reply. In the Topic 2 setup, create one kopi-kaki folder on your Desktop for the company labs; Day 2 reuses its outputs.",
          "Finish each lab with its checkpoint: evidence, not vibes."])
img(os.path.join(SHOTS, "screenshots", "prompts-page.png"), "The Lab Prompts page (prompts/index.html)", 4.2)
note("Preferred surface: Hermes Desktop. macOS/Windows learners use the official Desktop installer: download it from https://hermes-agent.nousresearch.com/desktop . On native Windows use the supplied PowerShell setup file and the same local profile for tools and Telegram; WSL is a separate runtime.\nPlatforms change quickly. If a command differs on your version, run it with --help and check the official docs: "
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
h3("AI application categories: different inputs, different work")
p("Organisations use several categories of AI application side by side. Each takes a different input, performs a different operation and needs a different human check.")
table(["Category","Typical input → operation → output","Key capability","Human check"],[("LLM / generative","Text brief → generate draft → proposed reply","Understand and produce natural language","Facts, tone and intent"),("Computer vision","Images → detect patterns → defect flags","Analyse images and video for inspection and classification","Validated inspection labels"),("Predictive analytics","Historical rows → fit/forecast → demand estimate","Forecast outcomes from historical data","Error against held-out actuals"),("Autonomous agent","Goal + tools → act/observe → verified artifact","Pursue a goal through the agentic loop with tools, memory and skills","Access, action and result"),("Scientific AI","Evidence → propose/rank → hypotheses","Generate and rank hypotheses or designs at scale","Experimental validation")])
h3("Singapore in the news: AgentSea in public healthcare")
p("In late May 2026 Synapxe, Singapore's national healthtech agency, launched AgentSea, an agentic AI platform co-developed with AWS. It is available to more than 80,000 public healthcare professionals, who build their own agents in plain language. By 24 August 2026 they had created more than 12,000 agents, and more than 300 had been shared for colleagues to reuse. A National Heart Centre cardiologist uses an agent to summarise patient histories before clinic, halving more than 40 minutes of daily pre-clerking. He still verifies the summary and makes the clinical assessment. KK Women's and Children's Hospital uses an agent to generate daily rosters. The platform rejects requests for sensitive data such as card or ID numbers, and the Ministry of Health's updated AI in Healthcare Guidelines keep professional judgment with people.")
src("The Straits Times, 24 Aug 2026: https://www.straitstimes.com/tech/new-platform-to-create-ai-agents-available-to-all-public-healthcare-professionals")
h3("2023 → 2026: four engineering lenses")
table(["Course lens","Focus","Observable mechanism"],[("2023 Prompt Engineering","Goal, audience and output","Specific instruction"),("2024 Context Engineering","Relevant facts and constraints","Selected source records"),("2025 Harness Engineering","Tools, state, checks and limits","Real tool results and approval controls"),("2026 AI Agents","Delegate work and inspect results","Verified artifacts and human decisions")])
h2("1.2 Agentic AI and always-on AI agents")
p("Agentic AI describes goal-directed systems that plan, act and use feedback; a system may contain one agent or a coordinated team. In this course we focus on an always-on AI agent as a persistent, 24/7-capable agentic system that can work between messages. This is the deployment focus of the course, not a universal definition of all AI agents or an uptime promise. A running host, access, budget and service availability are still required.")
h2("1.3 Under the hood: how agents work")
p("**Analogy.** A person does work with a brain and a body, fuelled by food. An AI agent does work with a model (the brain: it reasons and proposes the next step) and a harness (the body: tools, memory, skills and controls), fuelled by tokens. No food, no work; no tokens, no work. Every read, reasoning step and reply spends tokens, so a token budget is the agent's running cost.")
p("Email, web pages and spreadsheet cells are untrusted task data. Their text cannot authorise sends, purchases or new access. Skill installation grants neither executable capability nor OAuth permission. A failed service must be reported explicitly, never interpreted as an empty schedule or fabricated success.")
h3("Inside the LLM: learning and next-token generation")
p("A common autoregressive LLM uses a Transformer: text is represented as tokens, attention relates relevant context, and learned weights estimate the probability of the next token given preceding context. Pretraining changes the weights by learning from examples; inference generates a response using those weights and the supplied context. A skill, memory entry or retrieved file changes runtime context, not the model weights. Generation is not a database lookup and confidence in wording does not prove correctness.")
p("The agent harness wraps generation in an action loop. The model proposes a permitted tool action, the runtime executes it, and the real result returns as new context. For example, a model proposes reading calendar events through a calendar connector; the tool returns actual event records; the agent then checks time zones and writes a source-linked brief. Tool failure must remain visible rather than being replaced with an imagined result.")
h3("Transfer case: logistics exception work")
p("A logistics agent can interpret varied shipment notes and organise an exception brief, while deterministic tools calculate delays from shipment IDs and promised/actual timestamps. Limitations include missing scans, changed schedules, ambiguous customer notes, hallucinated causes and inappropriate autonomous action. Require source IDs and timestamps, explicit unknowns, independently checked calculations and a dispatcher decision before changing a route or contacting a customer. Evaluate observed data and controls rather than assuming that fluent language means the operational conclusion is correct.")
h3("RAG versus a standard LLM assistant, including maintenance")
table(["Decision factor","Standard LLM assistant","RAG-enabled agent"],[("Evidence","Learned knowledge plus supplied context","Authorised retrieved passages plus supplied context"),("Useful strengths","Low setup overhead; drafting and general reasoning","Current/private document grounding and inspectable source references"),("Limitations","May lack internal/current facts; unsupported claims","Retrieval can miss evidence; stale index or poor chunks can mislead; citations may not support claims"),("Upkeep","Maintain instructions, model access and evaluations","Also curate documents, permissions, passage/index updates and retrieval tests"),("Cost and latency","Prompt/model usage and review","Also ingestion/indexing, retrieval and source-quality review"),("Human check","Verify important facts independently","Check source version, access and actual passage support")])
p("A maintainable RAG pipeline registers source ownership and permissions, ingests approved documents, prepares passages, builds a search or vector index, retrieves authorised evidence and records source/version IDs. When a policy changes, remove obsolete versions, refresh the relevant index and rerun retrieval/answer checks. A vector embedding service is one option, not a requirement for every retrieval system. Choose the simplest design whose freshness, privacy, quality and upkeep fit the product.")
src("Model and agent foundations: https://arxiv.org/abs/1706.03762 ; https://arxiv.org/abs/2210.03629 ; retrieval-augmented generation: https://arxiv.org/abs/2005.11401")
p("Compare observed source accuracy, setup/run/review time, actual approval and stop controls, and explicit failures. Distinguish model weights from runtime context, memory from a managed knowledge base, human-in-the-loop approval from human-on-the-loop monitoring. Keep the task bounded and record unknowns.")
h2("1.4 AI agents do the work; humans decide")
p("Human-in-the-loop means the agent waits for an owner's approval before a consequential action; human-on-the-loop means a named owner monitors bounded, reversible work and can pause or correct it. The agent reads permitted sources, selects tools, calculates, drafts and produces work. The human sets the goal and access, exercises judgment when facts or values conflict, approves consequential commitments and accepts the result. Capability and human authority should be explicit in the task, rather than inferred from a product label.")
table(["Two work modes","AI work","Human judgment","Evidence"],[("Personal assistant","Email, calendar, travel options and daily brief","Priorities, conflicting commitments and exact sends/purchases","Source-checked schedule and reviewed draft"),("Digital worker","Coding, accounting, analysis and content production","Business decision, exceptions, release and quality acceptance","Patch, reconciliation, deck or video plus verified checks")])
h2("1.5 Five collaboration scenarios")
p("People and agents team up in five scenarios. Each step down the list adds more people or more agents, and with them more hand-offs, permissions and ownership to get right.")
img(os.path.join(SHOTS, "topic1", "patterns-strip.jpg"), "The five collaboration scenarios, from one human with one agent (left) to inter-company collaboration (right)", 6.3)
table(["Scenario","How it works","Where you see it today"],[
 ("1 · One human, one AI agent","Your own chief of staff that never clocks off. It works through your inbox and calendar overnight and has a brief, a clash and a draft ready by morning.","Always-on assistants: OpenAI Dots, Meta Muse, Grok Bot, Claude Duet, Manus Cue (Activity 1); Hermes Desktop on your laptop (Topic 2, Activities 2–3); Claude Code or OpenAI Codex for one developer."),
 ("2 · Multiple humans, one AI agent","One agent in the team chat becomes the colleague everyone pings. It updates systems, chases blockers and reports back to the group.","An OpenClaw or Hermes bot in a Telegram or WhatsApp group; Claude in Slack or any bot a channel can @mention; one agent triaging a shared support inbox."),
 ("3 · One human, multiple AI agents","Be the manager of your own AI department: split the goal and hand each piece to a specialist working in parallel.","Hermes profiles on a Kanban board (Activities 4 and 5); several Grok Bots sharing one cloud computer; a Manus Cue agent team in one group chat."),
 ("4 · Multiple humans, multiple AI agents","A whole organisation runs on agents: many people build and run their own, all aimed at shared goals.","Singapore public healthcare: 80,000+ staff built 12,000+ AgentSea agents; Stanford's virtual biotech of 37,000 AI scientist agents; a department Kanban board where each card has a human owner and an agent assignee."),
 ("5 · Inter-company collaboration","Your agent negotiates with their agent. Requests, quotes and data cross the company wall, and people on both sides sign off.","Grok Bots with their own @mail.grokbot.com inbox, where an outside company's email can start a routine; Meta Muse working with Singapore partners such as Grab and Singapore Airlines; Manus Cue agents with their own email, phone and wallet dealing with outside businesses.")])
p("Real examples shown in class: an assistant flagging a weekend schedule clash (scenario 1), an OpenClaw agent in a trainers' group chat reassigning a course run and reporting a blocker (scenario 2), and six Hermes profiles running a YouTube channel (scenario 3). Third-party names in these screenshots are blurred. As scenarios scale, govern them with named owners, permissions for each role and an audit trail, and treat anything from another company's agent as untrusted until a person verifies it.")
p("**Try scenario 2 now.** Scan the QR code below (or open https://wa.me/message/YMQB2CFYVGL3I1) to message Tertiary Infotech Academy's WhatsApp Business account. Everyone in the class messages the same account at once. Ask something real, such as which AI agent courses run next month or for this course's brochure, then compare answers with your neighbour: which replies came back instantly, and which waited for a person?")
img(os.path.join(SHOTS, "topic1", "whatsapp-qr.png"), "Scan to chat with Tertiary Infotech Academy on WhatsApp", 2.2)
h2("1.6 Use cases and product development")
p("Five business use cases show where agents already help organisations. In each, the agent prepares the work and a person keeps the decision that carries business risk.")
table(["Use case","What the agent does","What the human decides"],[("Customer service operations","Classifies requests, looks up the account and past conversations, drafts a reply and suggests the next action; may complete simple cases within approved limits","Complex or sensitive cases; the limits on what it may complete"),("IT service management","Collects technical details, checks known issues, creates tickets and routes them to the right support group","Technician fixes the problem; access changes are approved"),("Finance operations","Reads invoices and payment queries, matches them with internal records, flags missing details and prepares items for approval","Payments and high-risk actions under clear approval rules"),("Sales operations","Updates customer records, prepares meeting notes, checks account history and creates follow-up tasks","The salesperson owns the customer relationship"),("Procurement and supply chain","Monitors orders, reviews supplier information, flags delays and gathers facts from several systems","The operations manager decides the response"),("AI + scientist","Generates and critiques hypotheses","Scientist validates experimentally"),("Humanoid + caregiver","Bounded elderly-care task such as handing over water or a walking aid","Caregiver authorises the task, keeps the stop control and checks the hand-off; future design scenario")])
src("Business use cases: Genic Solutions, 30 Sep 2026 — https://www.genicsolutions.com/ai-agents-for-business-use-cases-and-implementation/")
p("Scientific hypotheses require experimental validation; a generated proposal is not a discovery. Embodied systems add sensing and physical action: manufacturer demos, controlled pilots and validated deployments are different levels of evidence. The elderly-care humanoid scenario is prospective: sense the authorised room, plan one bounded task, have a caregiver authorise it and keep the stop control, then verify the hand-off and recovery. It is not a claim of readiness for homes or care facilities.")
h3("AI for Science in the news (2026)")
table(["Result","What the agents did","What still has to be checked"],[
 ("Maths: a Millennium Prize problem (Quanta Magazine, 8 Sep 2026)","OpenAI ran about 10,000 autonomous agents to show that the 3D Navier–Stokes fluid equations can 'blow up'.","Checked in the Lean proof assistant, with humans confirming the formal statement; a priority dispute with two mathematicians continues."),
 ("Drug discovery: a virtual biotech (Stanford Medicine, 17 Sep 2026)","37,000 AI agents catalogued about 50,000 clinical trials in under a week and designed a lung-cancer antibody–drug conjugate.","A pharmaceutical company independently reached the same design; the team's next step is real-lab testing."),
 ("Maths at volume (Nature, 7 Oct 2026)","OpenAI posted more than 700 AI-generated maths preprints from an unreleased model.","Mathematicians describe them as a 'messy first draft' and raise credit and pre-emption concerns."),
 ("Maths, physics and computing claims (Firstpost, 27 Oct 2026)","OpenAI claims proofs on Kakeya conjectures and 4D quantum field theory, and an algorithm that would disprove the Exponential Time Hypothesis.","Claims awaiting verification by expert panels.")])
p("Agents can now propose results at massive scale, but proof checkers, laboratories and experts still decide what counts as a discovery.")
src("Sources: https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/ ; https://med.stanford.edu/news/all-news/2026/09/virtual-biotech-company.html ; https://www.nature.com/articles/d41586-026-03196-8 ; https://www.firstpost.com/tech/openai-claims-three-new-ai-breakthroughs-in-math-physics-and-computer-science-14055633.html")
h3("Product development: agents across the lifecycle")
p("Worked example: Kopi Kaki Co. launches a new iced oat latte. At every stage the agent does the work and a person makes the decision that carries business risk.")
table(["Stage","What the agent does","What the human decides"],[("1 Discovery","Reads 200 customer reviews and competitor menus; lists the top requests with review IDs.","Which customer problem to solve."),("2 Design + build","Drafts the drink spec, menu card, poster and a short launch video script.","Recipe, price and brand wording."),("3 Test + QA","Auditor agent re-checks prices, allergens and claims against the source sheet.","Fix flagged errors; sign off release."),("4 Launch","Posts the approved content and sorts incoming feedback into a queue.","Complaints and anything sensitive."),("5 Measure + improve","Compares week-1 sales with the target and suggests what to change.","Keep, change or stop the product.")])
h2("1.7 Always-on agents: the Big Five")
p("OpenClaw → Hermes → hosted agents such as Dots, Muse, Duet, Grok Bot and Cue is a teaching progression through deployment/work choices, not corporate lineage. Local agents stop when their runtime stops; a managed cloud agent can keep working while your device is off, within its current limits. A list of avatars is not proof of multi-agent execution; verify actual worker runs, owned outputs and hand-offs.")
p("Compare the agents with a job-fit, control, access and limits framework (BULDRR). It was updated on 22 October 2026; newer official vendor information takes precedence. This is a task-selection framework, not an independent performance benchmark or a universal ranking.")
p("**The Big Five side by side.** The model decides how the agent thinks; the use case decides whether it fits your job. Models below were checked on 31 October 2026 against each maker's own announcement; vendors change models without notice, so check again before you rely on one.")
table(["Agent (maker)","Model inside","Use it for","At Kopi Kaki"],[("Meta Muse (Meta)","Muse Spark; Meta says Muse Wonder will power Muse soon, subscribers first","Personal email, schedules and goals; errands with Singapore partners such as Grab, Shopee and Singapore Airlines as they roll out","Sort your inbox and calendar before the Saturday pop-up"),("OpenAI Dots (OpenAI)","GPT-6 Astra","Ongoing goals inside ChatGPT, Slack and Teams; hands coding work to Codex","Check pre-orders every morning and flag a dip"),("Grok Bot (xAI)","Launched on Grok 4.6; Grok 4.7 (21 Sep 2026) is trained for the Grok Bot harness","A team of named bots (Research, Sales, Ops) sharing one cloud computer","A Research bot and a Sales bot working from one supplier list"),("Claude Duet (Anthropic)","Claude Opus 5.5","A morning brief, business inbox, invoices and follow-ups; asks before it sends, pays, signs or deletes","A 7 am brief: overdue invoices and supplier emails that need you"),("Manus Cue (Manus)","Runs on the Manus 2.0 Cascade agent harness; Manus does not publish the model","Agents with their own email, phone and wallet: calls, bookings and payments within a budget","Call three venues and shortlist the launch party")])
src("Models: Meta — https://ai.meta.com/blog/introducing-muse-spark-msl/ and https://research.meta.ai/blog/muse-wonder ; OpenAI — https://openai.com/index/introducing-dots/ ; xAI — https://x.ai/news/grok-4-7 ; Anthropic — https://claude.com/resources/articles/claude-duet ; Manus — https://manus.im/blog/introducing-manus-2-0")
table(["Agent","Human control to inspect","Access checkpoint"],[("Meta Muse","Connector permissions + sensitive-action approval","Singapore since 27 Oct; free core use"),("OpenAI Dots","Connection permissions, custom rules and review","Pro, Business Premium; Enterprise beta"),("Grok Bot","Approval settings; shared cloud logins across bots","Check your plan's access"),("Claude Duet","Approval before sensitive actions; some actions disallowed","US Pro/Max waitlist preview"),("Manus Cue","Per-agent permissions, wallet budget, review boundaries","Early access; free with invite code")])
p("Activity 1 has three parts. **1A, everyone:** join Meta Muse at muse.ai with your Facebook account and redeem your trainer’s invite code. **1B, if your ChatGPT plan includes dots:** set up an OpenAI Dot and give it a standing job. **1C, everyone:** install Wispr Flow and speak your prompts instead of typing them. Grok Bot, Claude Duet (US Pro/Max research preview) and Manus Cue (early access, invite code) are shown for reference. Use only the trainer-assigned Google account and connect Gmail and Google Calendar separately.")
h3("Meta Muse (Activity 1A: everyone)")
p("**What it can do** (Singapore since 27 Oct 2026; free for most needs): Manages email, schedules and goals; Gmail, Google Calendar and Instagram connectors; Singapore partners (Shopee, Lazada, Grab, Singapore Airlines, Agoda, Klook, Trip.com, ShopBack) rolling out; checks before sending or buying; Muse Secure VM keeps passwords and payment methods out of the agent's view.")
p("**How to set it up:**")
bullets(['Step 1 — Install Muse from Meta (iOS / Android) or open muse.ai; confirm the developer is Meta Platforms, Inc.', 'Step 2 — Complete sign-in and onboarding; Facebook, Instagram and Threads link automatically through Accounts Center.', 'Step 3 — Go to Settings → Connectors → Connect beside Gmail → Continue.', 'Step 4 — Finish the Google login in the browser; repeat for Google Calendar.', 'Step 5 — Keep retrieve-only where offered and approve sends and invites. Shortcut: ask “Connect my Gmail”; disconnect anytime in Settings → Connectors.'])
p("**Activity 1C — speak, don't type.** Install Wispr Flow (https://wisprflow.ai; Mac, Windows, iPhone and Android; free for 2,000 words a week) and speak your prompts to Muse, Dots and Hermes instead of typing. Hold the Flow shortcut, talk, release: the tidied text lands in the app you are using. Talking makes it natural to give the goal, context, constraints and what done looks like, which is exactly what an agent needs. Wispr says Flow is 4x faster than typing (a vendor claim). Do not dictate passwords or personal data.")
p("**Your trainer’s invite code: H1KWDZ.** Within 48 hours of joining, go to Settings → General → Usage → Redeem invite code and key it in. You and your trainer each receive 1 billion Muse tokens. Happy learning and collaborating with AI.")
src("Muse connector steps: https://www.meta.com/help/superintelligence/1687253048996149/")
src("Video (YouTube Short): 10 ways to use Muse — https://www.youtube.com/shorts/zuAAjV5dNMA")
p("Meta's announcement of 27 October 2026 confirms Singapore availability, Gmail/Google Calendar/Instagram connections, sensitive-action approval and free core use with optional subscriptions. Local partner features roll out progressively.")
src("Meta Singapore launch: https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/")
src("Official iOS Singapore listing: https://apps.apple.com/sg/app/muse-from-meta/id6760173601 ; Android Singapore listing: https://play.google.com/store/apps/details?gl=sg&id=com.facebook.aura")
h3("OpenAI Dots (Activity 1B: Pro or Business Premium)")
p("**What it can do** (rolling out to ChatGPT Pro and Business Premium; Enterprise, Edu and Healthcare beta once the workspace admin enables it. Free, Go and Plus are not in the launch rollout): Several ongoing responsibilities per dot; its own cloud computer, optionally your computer; plugins for email, calendar and files; contact methods such as Slack; delegates to ChatGPT Work or Codex; schedules, event triggers and an Activity view.")
p("**How to set it up:**")
bullets(['Step 1 — Open dots in the ChatGPT mobile app, desktop app or a desktop browser (mobile web is not supported) and follow the introduction.', 'Step 2 — Name your dot and choose its appearance; both can change later.', 'Step 3 — Connect plugins for email, calendar and files, authorising each one.', 'Step 4 — Optional: open the dot’s profile and select Add to connect a contact method such as Slack. A messaging channel does not grant inbox or computer access.', 'Step 5 — Describe an ongoing responsibility, its sources and which decisions need you. Ending a conversation does not necessarily stop assigned work; check Activity.'])
src("Dots getting started: https://learn.chatgpt.com/docs/dots/getting-started ; plans: https://openai.com/index/introducing-dots/")
src("Video (YouTube Short): How to set up your first OpenAI dot — https://www.youtube.com/shorts/gdHwOn2kvT8")
h3("Grok Bot (reference — eligible account)")
p("**What it can do** (Check your plan's access): Persistent cloud computer (browser, command line, files) shared by your bots; watch live or take over for sign-ins; Gmail, Calendar, Sheets, Slack, Notion and MCP servers; its own @mail.grokbot.com address; Vault/1Password sign-ins and Auto Review.")
p("**How to set it up:**")
bullets(['Step 1 — Start at x.ai/bot; install the desktop or mobile app and sign in.', 'Step 2 — Create a bot: sidebar + → Create a Bot → name it → Create.', 'Step 3 — Open Connect apps (mobile: avatar → Connect apps) and add Gmail.', 'Step 4 — Finish the Google login in the browser; repeat for Google Calendar.', 'Step 5 — Confirm both appear under Installed. “Added” does not mean signed in; choose Authenticate if an app shows Needs auth.'])
p("All bots on one account share a cloud computer, browser logins and connected apps. A @mail.grokbot.com address is the bot’s own inbox, not your Gmail.")
src("Grok Bot computer and apps: https://docs.x.ai/grok-bot/computer-and-apps")
src("Video (YouTube Short): 3 steps to set up Grok Bot — https://www.youtube.com/shorts/Gm_dlNAVOGI")
h3("Claude Duet (reference — US research preview)")
p("**What it can do** (Research preview, US Pro/Max via waitlist): Morning brief across connected apps; checks accounts every few hours and messages only when something needs you; own virtual machine and browser; 6,000+ connectors (Gmail, Slack, QuickBooks, Stripe, HubSpot, Docusign…); shows exactly what it will send, pay, sign or delete and waits for approval.")
p("**How to set it up:**")
bullets(['Step 1 — Have a Pro or Max plan and join the Claude Duet waitlist on claude.com.', 'Step 2 — Once invited, open the Claude Duet app (iOS / Android) or claude.ai.', 'Step 3 — Memory, skills and connected apps carry over from your Claude account.', 'Step 4 — Add connectors such as Gmail, Calendar or Slack from the Claude Marketplace.', 'Step 5 — Tell it what to watch and how often. It asks before it sends, pays, signs or deletes; some actions stay off-limits even with approval.'])
src("Introducing Claude Duet: https://claude.com/resources/articles/claude-duet")
src("Video (YouTube Short): Claude Duet is here — https://www.youtube.com/shorts/7G5hOD6oF4M")
h3("Manus Cue (reference — early access)")
p("**What it can do** (Early access, free with an invite code): Each agent has its own email, phone number, wallet and computer; takes forwarded calls; pays within budgets you set; agents collaborate in a group chat; connectors (Gmail, Trip.com…) and routines; scan a QR code to create an agent.")
p("**How to set it up:**")
bullets(['Step 1 — Use cue.im on the web, the desktop app or Android; the iOS app is pending review.', 'Step 2 — Sign up with an invite code from your trainer or an existing user during early access.', 'Step 3 — Create an agent and give it one responsibility and the context it needs.', 'Step 4 — Choose its email, phone, wallet and computer; set wallet budgets and which actions need your approval.', 'Step 5 — Connect Gmail or other services, then define routines for steps you repeat. Keep budgets small and require approval for payments, calls and messages.'])
src("Cue by Manus: https://cue.im/")
src("Video (YouTube Short): Meet Manus Cue — https://www.youtube.com/shorts/ZW7gCKTLtpo")
src("Requested comparison: https://buldrr.com/claude-duet-vs-muse-vs-grokbot-vs-dots")
src("Official product checks: https://claude.com/resources/articles/claude-duet ; https://docs.x.ai/grok-bot/computer-and-apps ; https://learn.chatgpt.com/docs/dots/getting-started")
h2("1.8 Activity 1 checks and PP Task 1 evidence")
p("Check the schedule in Asia/Singapore against actual source events, draft a reply, correct one detail and inspect the real task stop/pause state. Closing a chat need not stop an ongoing responsibility. A store/install screen, generic chatbot or trainer demonstration is not your executed work. PP Task 1 needs ONE readable screenshot of your own Meta Muse or OpenAI Dots request and its result (a schedule check or a drafted email), with credentials and unrelated private data hidden.")


# ====================================================================== labs
LAB_SHOTS = {"01": ("workflows/activity-01.png", "Activity 1 workflow model — design diagram, not executed learner evidence"),
             "S2": ("screenshots/desktop/telegram-setup.png", "Hermes Desktop → Messaging → Telegram → Create with QR"),
             "02": ("screenshots/desktop/kopi-website.png", "The trainer's Activity 2 result: one agent, two UX skills, one brief — your version will differ"),
             "03": ("screenshots/desktop/install-skill-by-asking.png", "Install a skill by asking: “install the kopi pitch deck skill”"),
             "04": ("screenshots/desktop/bot-group-chat.png", "A bot group chat in Hermes Desktop (trainer's test room); yours is the Kopi Social Team"),
             "06": ("screenshots/desktop/scheduled-jobs.png", "Scheduled jobs: frequency, next run, prompt, Pause and Trigger now"),
             "05": ("screenshots/hermes-kanban.png", "Reference Kanban interface; PP Task 3 uses your own board and video"),
             "B": ("paperclip/org-chart.png", "Paperclip org chart (trainer's demo company); yours shows Board → CEO → Chief of Staff → team")}


def lab_section(L):
    h2(f"{L['label']} — {L['title']}")
    p(f"**Day {L['day']} · {L['minutes']} min · {L['paradigm']} · {L['lo']}** — {L['hook']}")
    h3("Business scenario"); p(L["scenario"])
    h3("Goal"); p(L["objective"])
    if L.get("prereq"): h3("Before you start"); bullets(L["prereq"])
    shot = LAB_SHOTS.get(L["code"])
    if shot: img(os.path.join(SHOTS, *shot[0].split("/")), shot[1], 5.0)
    h3("You will deliver"); bullets(L["deliverables"])
    table(["Who", "Role"], [("Agents", L["agents"]), ("You (human)", L["human"])])
    h3("Concepts in action"); bullets(L["concepts"])
    h3("Lab files")
    p(f"labs/{L['slug']}/ — README.md, LAB-{L['code']}-Instructions.pdf, COPY-PROMPTS.txt and data/. Every prompt below is also on the Lab Prompts page with a Copy button. Use the training account for Activity 1; from the Topic 2 setup on, drag each lab's data/ into your Desktop/kopi-kaki folder (Finder or File Explorer). No step needs a terminal: everything is a click in Hermes Desktop or a prompt Mia carries out.")
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

lab_section(LABS[0])   # Topic 1 ends with its lab
h2("1.9 Sources and further reading")
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
LAB = {L["code"]: L for L in LABS}
import labs_v34_t2 as T2SRC
h1("Topic 2 — " + C.TOPICS[1]["title"])
p(C.SCENARIO + ". You are the founder-CEO; all company data is fictional. "
  "In Topic 1 an always-on assistant handled your schedule. In Topic 2 you hire your first AI employee — a Hermes agent called Mia — and give her, step by step, everything an employee needs.")
h2("2.1 What an AI agent is")
p("Before using an agent, open the system it runs in. The model sits inside a harness; the harness assembles context, calls tools, applies skills and limits, and stops for human decisions.")
table(["Component","Function","What to inspect"],[("Model","Proposes next tokens and actions","Model access and observed limitations"),("Tools","Execute reads, calculations, browsing and rendering","Actual executable/API result"),("Skills","Reusable procedures and verification checks","Reviewed SKILL.md, scripts and source"),("Memory","Persist approved preferences and decisions","Saved entry and fresh-session recall"),("Knowledge base","Curated evidence with owners and versions","Source access, freshness and passage support"),("Instructions","Goal, policies and output contract","Authority and stop conditions"),("Context","Selected instructions, memory, retrieved knowledge and recent tool results","Relevant material fits the finite context window"),("Agentic loop","Observe → select → act → verify → repeat/ask/stop","Real state changes and error handling"),("Security","Identity, permissions, approvals, budgets and logs","OAuth and runtime policy checked separately")])
h2("2.2 What Hermes Agent is")
p("Hermes Agent (Nous Research, MIT licence) is an open-source agent: a model inside a harness of tools, skills, memory and channels. "
  "In this course you use it only through Hermes Desktop — an app you install like any other. Mia remembers across sessions, learns skills, talks to you on Telegram, "
  "runs scheduled jobs, and — in Topic 3 — works in teams of bots and on a Kanban board. Whenever a technical step is needed, Mia does it for you with her terminal tool; you never type commands.")
table(["Part", "What it is for Mia", "Where you set it in Hermes Desktop"], [
    ("Model", "The brain — your ChatGPT Plus plan, Nous free models or a paid model", "Settings → Model → Main model"),
    ("Context", "Who Kopi Kaki is and the rules", "AGENTS.md in your Desktop/kopi-kaki folder"),
    ("Memory", "What she chose to remember about you and the work", "Settings → Memory & Context"),
    ("Tools & connectors", "What she can do: web, files, browser, images, voice, schedules; apps such as Gmail", "Capabilities → Tools / Connectors"),
    ("Skills", "How to do a job well: steps, rules and checks in a SKILL.md", "Capabilities → Skills, or ask Mia to install one"),
    ("Messaging + schedules", "How she reaches you, and when she starts work by herself", "Messaging · Scheduled jobs")])
img(os.path.join(SHOTS, "screenshots", "desktop", "skills.png"), "Hermes Desktop: the left sidebar (New session, Capabilities, Messaging, Scheduled jobs, Kanban) is your control panel", 5.2)
h2("2.3 Install Hermes Desktop and point it at your company folder")
p("Download Hermes-Setup.dmg (Mac, Apple Silicon only) or Hermes-Setup.exe (Windows) from hermes-agent.nousresearch.com/desktop and install it like any app. "
  "On first run choose 'Choose provider later' and the Basic layout. Check Settings → About → Version & updates: it should say you are running the latest version. "
  "Create a folder called kopi-kaki on your Desktop and drag the lab's data/ into it; AGENTS.md sits at the top of that folder.")
p("**Hand Mia the company rulebook: + → Folder….** AGENTS.md is Kopi Kaki's rulebook: who the company is and the rules every agent follows. It comes with every Hermes lab's data/ files. "
  "In Hermes Desktop: (1) drag the lab's data/ files into Desktop/kopi-kaki; (2) in the chat box click + (left of 'Ask anything') → Folder… and choose kopi-kaki; "
  "(3) send 'Read AGENTS.md in the attached folder and follow it for this session' and check her answer matches the rules. Do this at the start of every lab. Type @ to point Mia at a single file, e.g. @AGENTS.md.")
src("Context files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files")
img(os.path.join(SHOTS, "screenshots", "desktop", "version.png"), "Settings → About → Version & updates", 4.6)
h2("2.4 Provider and model")
p("The provider serves the model; the model is the brain. Pick one route:")
table(["Route", "How", "Cost"], [
    ("Paid, this class: ChatGPT Plus", "Settings → Model → Main model → Provider 'ChatGPT or Codex Subscription' → sign in → pick the model → Apply", "Your ChatGPT Plus plan (sign up for it as your free AI subscription); no Nous subscription needed"),
    ("Free: Upstage Solar Mini 4", "Status bar → Sign in next to Nous → free Nous Portal account → Settings → Model → Provider: Nous Portal → Solar Mini 4", "$0 — free models only, standard rate limits; Solar Mini 4 is the most-used free model on Nous Portal (31 Oct 2026)"),
    ("Paid", "Nous Portal Plus, or another provider's key in Settings → Providers", "Nous Plus USD 20/month (Super USD 100, Ultra USD 200)")])
p("'Applies to' at the top of the Model page chooses which bot you are setting: each bot can have its own brain. Right-sized models (Security Principle 5): a small, fast model is often enough for inbox triage.")
src("Nous Portal plans and free models (checked 31 Oct 2026): https://portal.nousresearch.com/ ; https://portal.nousresearch.com/models")
img(os.path.join(SHOTS, "screenshots", "desktop", "model.png"), "Settings → Model → Main model with the ChatGPT or Codex Subscription provider", 5.0)
h2("2.5 Telegram messaging and voice")
p("Give Mia a phone number. Left sidebar → Messaging → Telegram offers two ways to create her bot.")
p("**Quick way (recommended): Create with QR.** Quick setup → Create with QR. Scan the code with the Telegram app on your phone, or open the link on this computer (the code expires in 30 minutes), and confirm in Telegram. Hermes creates the bot and detects your Telegram user ID automatically. Switch on Enabled and click Save changes.")
p("**Manual way: BotFather.** Use it if the QR code does not work, or to see what the quick way does for you.")
bullets(["Step 1 — Talk to BotFather. Open Telegram and search for BotFather (look for the official blue verification tick). Tap Start, then send /newbot.",
         "Step 2 — Name your bot. Choose a display name (e.g. Mia · Kopi Kaki), then a unique username that ends in bot or _bot (e.g. kopikaki_mia_bot). If the name is taken, BotFather asks you to pick another.",
         "Step 3 — Get your API token. BotFather generates an API token. Copy it and keep it safe: it is the password to your bot. Never paste it into a chat, a prompt or a slide.",
         "Step 4 — Connect it in Hermes. Messaging → Telegram: paste the token into Bot token and add your numeric user ID (message @userinfobot in Telegram to get it) under Allowed Telegram user IDs. Without it, anyone can message your bot. Switch on Enabled and click Save changes."])
p("Either way: send 'hi' to your bot, then /sethome so scheduled results arrive in that chat.")
img(os.path.join(SHOTS, "screenshots", "desktop", "telegram-setup.png"), "Messaging → Telegram: Quick setup, Get your credentials and the Bot token field", 5.0)
src("Telegram bots and BotFather: https://core.telegram.org/bots/features#botfather ; Hermes Telegram: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram")
bullets(["Voice: Settings → Voice. Speech to text on (Live Transcription shows your words); Text to speech provider Edge (free) with Read Responses Aloud. The same free voice narrates the Activity 5 video."])
img(os.path.join(SHOTS, "screenshots", "desktop", "text-to-speech.png"), "Settings → Voice → Text to speech: the free Edge voice", 4.8)
h2("2.6 Tools and skills: Gmail, web design and PPTX")
p("A tool is the agent's hands: it actually does something — reads Gmail through Google's API, writes a file, renders slides. A skill is know-how: a SKILL.md folder of steps, rules and checks that tells the agent how to use its tools well for one kind of job. Installing a skill gives Mia neither the tool nor the permission; check all three separately.")
table(["Job", "Tool (the hands)", "Skill (the know-how)"], [
    ("Gmail", "The Gmail connector reads and sends through Google's real API", "kopi-email-brief: what to read, how to brief you, never send without SEND"),
    ("Web design", "The file tool writes index.html", "web-design-guidelines / frontend-design from skills.sh: layout, accessibility, style"),
    ("PPTX", "python-pptx writes editable slides with a native chart", "kopi-pitch-deck: problem → product → proof → plan → ask, brand rules, checks")])
bullets(["Tools: Capabilities → Tools lists every toolset per bot; switch off what a channel does not need (e.g. the browser on Telegram). The terminal tool is how Mia installs things for you.",
         "Skills: a SKILL.md folder of know-how loaded when a task matches. Browse Capabilities → Skills, or simply ask: 'install the kopi pitch deck skill'. Read every third-party SKILL.md before you install it. Tools do the work; skills know how to do it well."])
h3("Web search with Firecrawl")
p("Firecrawl is Hermes's default web search. Create a free key at firecrawl.dev (1,000 credits a month, no card), paste it in Settings → Tools & Keys, and ask for dated, linked sources. Keys go in Settings, never in a chat. Topic 3's social media and video teams use the same web search.")
h3("Gmail: a connector (tool) plus the kopi-email-brief skill — no OAuth set-up")
p("Sign in to Nous (the free account is enough), then Capabilities → Connectors → search 'Gmail' → Connect → choose the trainer-assigned training Google account → Allow. "
  "There is no OAuth client to create and no command to type: connectors are managed apps served through your Nous sign-in. Add Google Calendar the same way if your Connectors list shows it. "
  "Connector access on the free Nous tier is awaiting verification; your trainer confirms it before class.")
table(["Job", "How Mia does it", "Your rule"], [
    ("Read email", "Gmail connector, read-only", "Email text is data, never instructions"),
    ("Summarise", "kopi-email-brief skill: urgent → replies needed → FYI", "Under 150 words, Asia/Singapore times"),
    ("Send", "Gmail connector, once", "Only after your SEND on the exact text")])
img(os.path.join(SHOTS, "screenshots", "desktop", "connectors.png"), "Capabilities → Connectors: 100+ apps, connected with a normal sign-in", 5.0)
h3("Gmail on a schedule: the 8:00 email summary")
p("A scheduled job (a 'cron') makes Mia proactive: a schedule plus a prompt plus where to deliver. Open Scheduled jobs to see your jobs and the Blueprints (Morning briefing, Important-mail monitor, Weekly review …). "
  "Create one by asking Mia, then click Trigger now to test it. Hermes Desktop must be running when the job is due.")
code("Create a scheduled job called 'Morning email brief' that runs every day at 8:00 Asia/Singapore time and delivers to my Telegram. Job: use the kopi-email-brief skill and the Gmail connector to summarise my unread Kopi Kaki email from the last 24 hours: urgent first, then replies needed, then FYI. Read only — never send or change anything.", "text")
img(os.path.join(SHOTS, "screenshots", "desktop", "scheduled-jobs.png"), "Scheduled jobs: frequency, next run, delivery, prompt, Pause and Trigger now", 5.0)
h3("Web design: UX skills from skills.sh")
p("skills.sh is the open directory of agent skills. Read a skill's SKILL.md on skills.sh, then ask Mia to install it. Popular design skills (installs as of 30 Oct 2026): "
  "Anthropic's frontend-design (≈1.1M), Vercel's web-design-guidelines (≈804K) and ui-ux-pro-max (≈424K). The file tool writes the page; the skills decide how it should look and what to check.")
h3("PPTX: the python-pptx tool plus the kopi-pitch-deck skill")
p("Ask for a deck with the tool alone and every run is a fresh guess about order, colours and checks. Add the kopi-pitch-deck skill and Mia follows the same story order, brand rules and checks every time; improve the skill once and every run benefits.")
lab_section(LAB["S2"])   # setup lab sits before the activities, as in the deck
h2("2.7 Activity 2 — one agent builds the Kopi Kaki website")
p("Mia — a single agent — installs two design skills from skills.sh and builds a one-page site for the startup: hero, price, launch date and a pre-order button, in Kopi Kaki's colours. Check every fact against the company files.")
lab_section(LAB["02"])
h2("2.8 Activity 3 — one agent builds the pitch deck")
p("Problem → product → proof → plan → ask. The kopi-pitch-deck skill gives Mia this order, the brand rules and the checks; python-pptx (the tool) writes editable slides with a native chart. "
  "Check content errors (a wrong or unsourced number) separately from layout errors (clipped or overlapping text). PP Task 2 needs ONE Hermes Desktop screenshot showing your request and the finished deck.")
for title, url in T2SRC.SOURCES[:7]: src(title + ": " + url)
lab_section(LAB["03"])

h1("Topic 3 — " + C.TOPICS[2]["title"])
h2("3.1 From one employee to a team of agents")
p("A multi-agent system splits one big goal into specialist jobs that hand work to each other, with a human in charge. One agent fills one context window with every task and uses one set of "
  "instructions for every voice; a team gives each job its own agent and runs independent jobs in parallel. More agents also mean more hand-offs to check, so use a team when the jobs are truly different.")
table(["Every agent has its own…", "What it means", "Kopi Kaki example"], [
    ("Tools", "What it can do", "Pixel has the image tool; Rafi has web search"),
    ("Unique skills", "How it does the job well", "video-producer has the hyperframes skill"),
    ("Model", "How it thinks — big or small, any provider", "a careful model for Rafi, a fast one for drafts"),
    ("Instructions", "Who it is and its rules (SOUL.md + AGENTS.md)", "the reviewer never approves on your behalf"),
    ("Context window", "What it is holding in mind — its own memory and session", "each bot keeps its own chat and memory")])
h2("3.2 How agents work together: hub-and-spoke, hand-offs and subagents")
p("**Hub-and-spoke.** Rather than giving every responsibility to one agent, a multi-agent system divides the work among specialist agents that work toward one goal. A coordinator (the hub) hands out the pieces and collects the results; the specialists (the spokes) each do one piece. In Activity 4 you are the hub, @mentioning Rafi, Lin, Farah, Ivy and Pixel in the Kopi Social Team group. In Activity 5 Mia is the hub: one prompt, five video agents, one board.")
img(os.path.join(SHOTS, "workflows", "hub-and-spoke.png"), "The hub-and-spoke model: one coordinator (hub) hands work to specialists (spokes) and combines what comes back", 6.0)
p("**How a request travels.** (1) Your request enters the coordinator; (2) the coordinator splits it into tasks; (3) the tasks move out to the subagents; (4) the results return to the coordinator; (5) one final response comes back to you. In Activity 5: you ask Mia for a 20-second launch video; she creates seven cards on the kopi-video board; the researcher, scriptwriter, voice-over, producer and reviewer each work their card; their files (research.md, script.md, the narration, the MP4, the review) come back; and Mia reports to you. Nothing ships until you approve the exact video.")
p("**Hand-offs in practice.** “My order arrived damaged. I need a replacement.” A support agent understands the complaint and opens a case; a logistics agent reserves a replacement; a shipping agent books the courier and returns a tracking number; "
  "a customer agent confirms the fix. Each hands a structured message to the next. At Kopi Kaki the same four hand-offs handle “My cold brew pre-order arrived spilled”, with refunds above SGD 20 waiting for you.")
p("**Task decomposition** turns one large objective into smaller, specialised tasks that subagents can do on their own: understand the request, identify logical subtasks, assign responsibilities, and make sure the outputs can be combined later. Ask five questions in order:")
table(["Step", "Question", "Answered for Kopi Kaki (Activity 5)"], [
    ("1 · Understand the primary objective", "What is the user actually asking for?", "A 20-second cold brew launch video you can post on 1 Dec"),
    ("2 · Identify independent subtasks", "Which parts can be separated cleanly?", "Research, script, voice-over, render and review"),
    ("3 · Assign specialisation", "Which subagent is best suited for each task?", "video-researcher, scriptwriter, voice-over, video-producer, video-reviewer"),
    ("4 · Define expected outputs", "What should each subagent return?", "research.md, script.md, the narration, the MP4, review notes"),
    ("5 · Plan aggregation", "How will the coordinator combine the results?", "Mia follows the board; your two HUMAN cards close each stage")])
p("**Subagents.** A coordinator spawns a subagent through a task tool; in Hermes that tool is delegate_task. The subagent starts with a completely fresh conversation: it knows only the goal and context the coordinator writes, it inherits the coordinator's enabled tools, and only its final summary comes back. Hermes runs up to 10 subagents at once by default. Subagents are temporary helpers for one job; your named bots (Rafi and the team) and the video agents are profiles that stay, with their own role, memory and chat.")
src("Hermes subagent delegation (checked 31 Oct 2026): https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation")
h2("3.3 Bots and group chats")
bullets(["Bot — a Hermes agent with a name you can @mention: its own role, model, memory and skills, and one permanent Bot Chat. Hire one in the Bots tab → New Agent: Name, Title, Description; Advanced takes its role file as Custom SOUL.md. Right-click → Edit Profile gives it an avatar.",
         "Group chat — right-click a bot → Manage groups → create a room for 2–6 bots. Your message starts up to three rounds of bot turns; bots hand work to each other with @name and ask you with @user. Built-in caps (3 rounds, 10 messages per send) stop a room from spinning; Stop, Rename and Disband are in the room header.",
         "Activity 4 team: Rafi (Market Researcher), Lin (LinkedIn Writer), Farah (Facebook Writer), Ivy (Instagram Writer) and Pixel (Image Creator), in the group 'Kopi Social Team'. You approve every post."])
src("Hermes Bot Mode (checked 31 Oct 2026): https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode")
img(os.path.join(SHOTS, "screenshots", "desktop", "bot-edit-profile.png"), "Edit Profile: avatar (Bot, Generate, Upload, Pet), title and description", 4.4)
lab_section(LAB["04"])
h2("3.4 Video skills and tools, and the Kanban board")
table(["Tool", "How it makes video", "How to install"], [
    ("HyperFrames (HeyGen)", "HTML/CSS + GSAP timing → MP4; lint, snapshot, preview, render", "Ask Mia to install the official hyperframes skill and check what it needs"),
    ("Remotion", "React components → MP4; strong for templated videos at scale", "Capabilities → Skills → search 'remotion'"),
    ("Manim", "Python maths animation (3Blue1Brown style)", "Built-in manim-video skill; Mia installs Manim if you ask")])
bullets(["Kanban — the team's shared to-do list: assignee, parent dependencies, status and run history. A card runs only when every parent is done. HUMAN cards are unassigned and only you complete them (or tell Mia 'I approve — complete the card for me').",
         "Prompt method — in Activity 5 one prompt to Mia creates the five video agents (they also appear in the Bots tab) and the seven-card board with your two HUMAN gates. Open Kanban in the sidebar to watch it run.",
         "Group chat or board? Bots in a group talk their way to a result; a board makes the order explicit. Use a board when the steps are known and the stakes are high."])
img(os.path.join(SHOTS, "screenshots", "hermes-kanban.png"), "Reference Hermes Kanban board", 5.2)
h2("3.5 Grounding: RAG versus a standard LLM")
p("A standard LLM answers from what it learned: fluent and cheap, but it does not know your price, dates or latest policy and can state a wrong fact confidently. A retrieval-augmented (RAG) system answers from passages it retrieved, "
  "quotes the approved source and its version, and says INSUFFICIENT EVIDENCE when nothing supports a claim — but it needs source owners, indexing, access control and refresh. "
  "In Activity 5 the researcher writes claim | source file | exact quote: that table is your RAG audit trail.")
table(["Test", "Example question", "Correct behaviour"], [
    ("Supported", "What does the cold brew cost?", "Quote the catalogue line: SGD 6.80"),
    ("Partial", "What is the SHIOK20 offer?", "Give the discount AND its terms, or mark incomplete"),
    ("Unsupported", "Is it healthier than soft drinks?", "INSUFFICIENT EVIDENCE — no source, no claim"),
    ("Conflicting", "Two files disagree on the launch date", "Stop and ask the source owner")])
p("Maintenance is part of feasibility: when a source changes, refresh the index, retire the obsolete version, re-run the four tests and re-review everything that quoted it. Evaluate retrieval by relevance, support, latency and cost — not fluency. "
  "A regulated business (bank, insurer, clinic) adds a named source owner, per-document access control and an audit log of every refresh.")
lab_section(LAB["05"])
h2("3.6 Activity 6 — crons make next week's content")
p("A cron (scheduled job) starts the team's work without you: every Monday at 9:00 the week's three social drafts, every Friday at 10:00 a new video run on the Kanban board. "
  "Automate the start of the work, never the approval: drafts wait for your APPROVE, the video still stops at both HUMAN gates. Test every job with Trigger now, pause what you cannot watch, and log what each job produced in cron-log.md.")
lab_section(LAB["06"])
h2("3.7 Evaluate and improve the team")
table(["Metric", "What to measure"], [("Cycle time", "Brief to accepted output, including reviews and retries"), ("First-pass acceptance", "Share of outputs approved without revision"),
      ("Cost per accepted item", "Model and tool spend plus review minutes"), ("Defect rate", "Fact, brand and video-quality failures, counted separately")])
p("Measure the same four numbers before and after any change to a skill, a SOUL.md or the team; keep a change only when the measured benefit exceeds its overhead. Compare the team with the agency quote (SGD 3,000 and two weeks) including your own review time.")
h2("3.8 Five principles of AI security")
table(["Principle", "Question", "Rule"], [
    ("Data Control", "What AI can see", "Classify your data (public, internal, confidential) and decide exactly which data the AI may access."),
    ("Permission Control", "What AI can do", "Grant only the rights needed — read, write, edit, delete. Ask before anything destructive."),
    ("Human in the Loop", "Who approves", "A person reviews and approves high-impact actions — sends, posts, payments, deletions."),
    ("Traceability", "What happened", "Log every prompt, tool call and change so actions can be audited, explained and rolled back."),
    ("Right-Sized Models", "Not the most powerful", "The smallest model that does the job has less autonomy and risk.")])
p("In Hermes: a read-only Gmail connector, the Telegram approved-users list, @user questions in group chats, HUMAN Kanban cards, run history and file fingerprints, and a smaller model per bot.")

h1("Bonus Topic (optional) — Paperclip: Kopi Kaki as a One-Person Company")
p("Kopi Kaki Co. decides to run as a one-person company (OPC): you are the founder, the Board and the only human. Paperclip (open source, github.com/paperclipai/paperclip) runs a company of AI agents — org chart, job titles, "
  "reporting lines, budgets, tasks and an approval inbox. Hermes Kanban organises tasks; Paperclip organises people. Its agents run on CLIs you already have (Hermes, Claude Code, Codex or Gemini CLI) as adapters.")
bullets(["Install: ask Mia to install and start Paperclip (she runs its one-line onboarder for you), then open http://localhost:3100. Node.js 24.11+ must be on the laptop.",
         "Set up the company: Kopi Kaki Co., the mission, a USD 60/month training budget, and Settings → General → Hiring → 'Require board approval for new hires' ON.",
         "Set up the CEO (Ava): ask Mia to set her role to CEO (Paperclip has no Role field), then paste her written instructions into AGENTS.md; her first task is to hire a Chief of Staff.",
         "The Chief of Staff hires the marketing team — researcher, social copywriter, image creator, video producer, voice-over artist and an independent content reviewer — each through your Board approval.",
         "Show the org chart: Board → CEO → Chief of Staff → team. Then give the team the Activity 5 video brief and compare the result with your Hermes Kanban team."])
img(os.path.join(SHOTS, "paperclip", "dashboard.png"), "Paperclip dashboard at http://localhost:3100 (trainer's demo company)", 5.2)
table(["", "Hermes Kanban team (Activity 5)", "Paperclip company (bonus)"], [
    ("Who breaks down the work", "You create every card and parent", "The CEO and Chief of Staff create tasks"),
    ("Who decides the team", "You (one prompt to Mia) create the agents", "Managers propose hires; you approve"),
    ("Control", "HUMAN cards on the board", "Approval inbox, budgets, hiring gate"),
    ("Best for", "A known pipeline you want to run exactly", "An ongoing operation you want to delegate and govern")])
lab_section(LAB["B"])

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
        elif k == "testit": o += [f"> **✓ Test it:** {b[1]}", ">"] + [f"> - [ ] {v}" for v in b[2]] + [""]
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
prodoc.add_version_control(doc, PRIOR + [V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37])
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
        doc.add_heading(b[1], level={"h1": 1, "h2": 2, "h3": 3}[k]).paragraph_format.keep_with_next = True
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
        r = c.paragraphs[0].add_run("✓ Test it — " + b[1]); r.bold = True; r.font.size = Pt(10.5)
        for v in b[2]:
            pp = c.add_paragraph(); rr = pp.add_run("☐  " + v); rr.font.size = Pt(10)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    elif k == "src":
        par = doc.add_paragraph(); add_md_runs(par, b[1], size=8.5, color=RGBColor(0x6B, 0x68, 0x62))
    elif k == "img":
        if os.path.exists(b[1]):
            if doc.paragraphs: doc.paragraphs[-1].paragraph_format.keep_with_next = True   # lead-in stays with its image
            par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER; par.paragraph_format.keep_with_next = True
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
