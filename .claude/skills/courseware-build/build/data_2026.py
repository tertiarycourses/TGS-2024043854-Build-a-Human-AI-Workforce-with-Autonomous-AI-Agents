"""2026 update: shared, evidence-grounded collaboration cases and workshop content.
All CASE_GROUPS are proposed classroom designs, not claims of deployments.
"""
CHECKED = '29 October 2026'
SOURCES = [
 ('Hermes installation', 'https://hermes-agent.nousresearch.com/docs/'),
 ('Hermes Telegram gateway', 'https://hermes-agent.nousresearch.com/docs/user-guide/messaging'),
 ('Hermes skills', 'https://hermes-agent.nousresearch.com/docs/user-guide/features/skills'),
 ('gog installation and platform requirements', 'https://gogcli.sh/install.html'),
 ('gog OAuth and read commands', 'https://gogcli.sh/quickstart.html'),
 ('gog command policy and readonly flag', 'https://github.com/openclaw/gogcli'),
 ('OpenAI Dots: product demo reference', 'https://openai.com/index/introducing-dots/'),
 ('Google AI co-scientist: research case', 'https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/'),
 ('AlphaEvolve: evaluators and algorithm search', 'https://arxiv.org/abs/2506.13131'),
 ('Workflow, routing, parallelism and orchestrator patterns', 'https://www.anthropic.com/research/building-effective-agents'),
 ('Context engineering', 'https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents'),
 ('PptxGenJS: editable PowerPoint output', 'https://gitbrent.github.io/PptxGenJS/'),
 ('FFmpeg: local video rendering', 'https://ffmpeg.org/ffmpeg.html'),
 ('HyperFrames: optional AI video workflow', 'https://github.com/heygen-com/hyperframes'),
]
VIDEOS = ['OeAaTbzeNs4','-I23qhC0gSw','fZV5NlRpbC0','2TdhDKIH_FU','SJywU4UQryQ','jQxFsWxn5rQ']
# Case tuple: title, input, agent work, human decision, inspectable output, acceptance metric, pattern.
CASE_GROUPS = [
 ('Science & discovery','flask',[
 ('Hypothesis workshop','Research question + selected papers','Find claims; propose and critique hypotheses','Scientist selects experiment','Ranked hypotheses + source passages','Every hypothesis links evidence; novelty unproven','Multi-agent + expert gate'),
 ('Laboratory planning','Approved hypothesis + equipment limits','Draft protocol and resource schedule','Scientist approves safe protocol','Protocol + reagent checklist','No experiment before lab approval','Single agent + human gate'),
 ('Algorithm discovery','Seed program + evaluator','Propose code variants; run controlled tests','Engineer accepts validated candidate','Code diff + evaluation log','All correctness tests pass before speed comparison','Evaluator loop'),
 ('Literature evidence map','Topic + inclusion criteria','Extract study design and conflicting results','Researcher checks primary sources','Evidence matrix with DOI and limitations','All included studies satisfy criteria','Parallel extraction + synthesis')]),
 ('Healthcare & public service','heart',[
 ('Clinic inbox triage','De-identified messages + routing policy','Classify admin requests and urgent terms','Clinician reviews clinical escalation','Queue with reason and owner','Every urgent case escalated; no diagnosis','Router + human gate'),
 ('Discharge explanation','Approved discharge instructions','Draft plain-language and translated summary','Clinician verifies meaning','Side-by-side explanation','No new treatment advice; all doses match','Copilot'),
 ('Public-service enquiry','Published policy + synthetic query','Retrieve policy and draft cited response','Officer resolves ambiguous eligibility','Draft + policy section IDs','All eligibility claims trace to current policy','RAG single agent'),
 ('Service appointment plan','Service slots + accessibility needs','Find eligible slots and prepare options','Resident chooses; officer confirms','Proposed booking, no submission','No booking without explicit selection','Single agent + approval')]),
 ('Operations & logistics','route',[
 ('Delivery exception desk','Shipment events + service SLA','Flag late shipments; group causes','Dispatcher changes the route','Exception list + proposed action','Every flag cites shipment ID + timestamp','Single agent'),
 ('Route planning','Orders + vehicle constraints','Generate route candidates; run feasibility checks','Dispatcher accepts safe plan','Route table + constraint violations','No capacity or delivery-window violation','Planner + verifier'),
 ('Supplier delay response','Supplier email + purchase orders','Match order IDs; propose alternatives','Buyer approves change','Impact brief + draft reply','All affected orders matched; no duplicate action','Orchestrated workflow'),
 ('Shift handover','Open tickets + incident notes','Summarise unresolved items and owners','Shift lead accepts handover','Handover log with ticket IDs','No open critical ticket omitted','Single agent + review')]),
 ('Sales & customer care','handshake',[
 ('Lead research','Company URL + qualification rubric','Gather public evidence and score fit','Sales lead chooses contact strategy','Account brief + cited score','No invented contact or budget','Single research agent'),
 ('Proposal preparation','Approved brief + price catalogue','Build scope, timeline and assumptions','Commercial owner approves price','Proposal draft + source price IDs','Totals reconcile; no unapproved discount','Sequential workflow'),
 ('Support knowledge reply','Ticket + approved support articles','Retrieve fix and draft troubleshooting','Agent reviews unresolved cases','Reply draft + article links','Each suggested fix has a source','RAG + human gate'),
 ('Complaint escalation','Comment + escalation rules','Mask PII; classify and route','Manager handles health/legal/refund issues','Redacted escalation packet','All high-risk cases stop before posting','Router + approval')]),
 ('Finance & procurement','coins',[
 ('Invoice matching','Synthetic PO, receipt and invoice','Compare quantities, taxes and totals','Accounts officer accepts exceptions','Three-way match report','Zero unexplained variance; no payment execution','Single agent + rules'),
 ('Expense exception review','Claims + policy','Flag missing receipts or limits','Finance lead approves reimbursement','Exception report + evidence IDs','All flags trace to policy and receipt','Evaluator workflow'),
 ('Cash-flow brief','Approved receivables + due dates','Calculate overdue buckets and scenarios','Owner selects follow-up action','Ageing table + assumptions','Bucket totals equal source balance','Single agent'),
 ('Vendor comparison','Approved RFQ + supplier quotes','Normalise line items and compare trade-offs','Buyer awards contract','Comparison matrix with exclusions','Same specification and tax basis throughout','Parallel analysis + synthesis')]),
 ('HR & learning','grad',[
 ('Onboarding assistant','Role checklist + approved policies','Answer questions and track missing steps','HR handles exceptions','Checklist + policy links','No sensitive personnel records in prompts','RAG single agent'),
 ('Skills-gap plan','Anonymised role skills + target rubric','Map gaps and propose practice tasks','Learner and manager agree goals','Learning plan + evidence rubric','Every activity maps to one observable skill','Copilot'),
 ('Workshop material pack','Approved brief + learner profile','Build slides, worksheet and examples','Trainer checks accuracy and usability','PPTX + handout + QA report','No missing sources; readable projected slides','Single agent + skills'),
 ('Interview preparation','Job requirements + question rubric','Draft job-related questions and scoring anchors','HR validates fairness and selection','Question bank + rubric','No automated hiring decision','Human-led co-creation')]),
 ('Marketing & media','megaphone',[
 ('Campaign evidence brief','Reviews + approved product facts','Find themes and propose angles','Marketing lead selects angle','Research brief + review IDs','Every insight cites data; claims checked','Single agent'),
 ('Management pitch deck','Research brief + brand guide','Build editable slides and speaker notes','Manager approves narrative','PPTX + PDF + QA log','Six slides; verified prices; no overflow','Single agent + PPT skill'),
 ('Product micro-video','Approved copy + licensed assets','Storyboard, render and check duration','Owner watches full video','15-second MP4 + contact sheet','1080x1920; readable; no unlicensed audio','Single agent + video skill'),
 ('Creative testing','Approved variants + campaign metrics','Compare response and suggest one controlled test','Marketer chooses test and budget','Experiment plan + baseline','One changed variable; no fake causality','Analyst + human gate')]),
 ('Software & IT service','code',[
 ('Bug investigation','Issue + logs + repository','Reproduce, propose fix, run tests','Developer reviews diff','Patch + test evidence','Regression reproduced before acceptance','Single coding agent'),
 ('IT ticket routing','Ticket + service catalogue','Categorise and gather diagnostic data','Technician approves privileged action','Routed ticket + diagnostic log','No password or production change in output','Router'),
 ('Release preparation','Approved changes + release checklist','Compile notes; inspect checks and dependencies','Release owner authorises deployment','Release packet + test links','All required checks pass before release','Orchestrator + gate'),
 ('Security alert enrichment','Synthetic alert + approved telemetry','Correlate indicators and draft timeline','Analyst decides containment','Evidence timeline + uncertainty','No live containment by classroom agent','Parallel retrieval + analyst')]),
 ('Retail & manufacturing','store',[
 ('Demand replenishment','Sales history + stock + lead times','Calculate reorder candidates and explain drivers','Planner approves order','Suggested PO + assumptions','No order exceeds storage or budget limits','Single agent + forecast tool'),
 ('Visual defect triage','Labelled product images + defect taxonomy','Classify suspect units for inspection','Inspector confirms defect','Inspection queue + model confidence','False negatives checked on held-out sample','Vision + human gate'),
 ('Maintenance planning','Sensor trends + maintenance manuals','Summarise anomalies and retrieve safe checks','Engineer schedules intervention','Work-order draft + manual sections','No unsafe machine-control instruction','RAG + predictive tool'),
 ('Store performance review','Outlet sales + comparable periods','Compute changes and plausible explanations','Manager chooses field investigation','Variance table + questions','All percentages use stated baseline','Single analysis agent')]),
 ('Legal & governance','gavel',[
 ('Contract clause review','Synthetic contract + approved playbook','Flag missing or changed clauses','Counsel assesses legal significance','Clause diff + playbook references','No legal conclusion without qualified review','Copilot'),
 ('Policy consistency audit','Approved policy versions','Compare contradictions and stale references','Policy owner resolves conflict','Issue register with paragraph IDs','Every issue reproduces from source text','Parallel reviewer + synthesis'),
 ('Audit evidence assembly','Control checklist + sanitised records','Index evidence and mark missing items','Auditor judges adequacy','Evidence register + gaps','No fabricated evidence or completion claims','Single agent'),
 ('Privacy impact worksheet','Workflow data map + retention policy','Identify fields, recipients and retention gaps','Data owner approves design','Data-flow diagram + open decisions','All personal-data paths have an owner','Human-led design')]),
 ('Energy, built environment & research','building',[
 ('Energy efficiency review','Meter readings + operating hours','Find unusual loads and simulate options','Facilities engineer validates change','Baseline + scenario model','Savings labelled estimates; comfort preserved','Analysis + simulator'),
 ('Construction progress brief','Site notes + approved drawings','Match observations to work packages','Site lead verifies safety and progress','Progress report + unresolved issues','No safety sign-off by AI','Multimodal copilot'),
 ('Materials screening','Target properties + candidate dataset','Rank candidates under constraints','Scientist validates and tests','Candidate shortlist + provenance','Predictions distinguished from measurements','Model + expert experiment'),
 ('Grant proposal support','Call text + project evidence','Map requirements and draft work packages','Principal investigator owns commitments','Compliance matrix + proposal draft','All budget and capability claims verified','Sequential co-creation')]),
 ('Personal productivity & administration','calendar',[
 ('Morning work brief','Training Gmail + Calendar + Drive','Read bounded records; link evidence and conflicts','User prioritises the day','Brief with email, event and file IDs','Only assigned account; no sends or writes','Single Hermes + gog'),
 ('Meeting preparation','Agenda + related emails and documents','Extract decisions needed and propose questions','Chair sets agenda','Meeting pack + source references','Date/time and attendees checked','Single agent + skills'),
 ('Follow-up tracking','Approved meeting notes + action list','Detect overdue actions and draft reminders','Owner approves recipients and wording','Draft reminders + task IDs','No duplicate task or external send','Single agent + approval'),
 ('Travel planning','Policy + dates + public options','Compare feasible itinerary and costs','Traveller chooses and books','Options table + current source links','No booking; estimates time-stamped','Research agent + user gate')]),
]
PATTERNS = [
 ('Copilot: the person drives','Human selects each next step',[('user','Human task','Choose the decision or paragraph.'),('robot','AI proposal','Suggest alternatives using supplied context.'),('user','Human edit','Check and accept a specific change.')],'Example: trainer edits six-slide management pitch; evidence = tracked revisions.','No autonomous scheduling; do not imply the agent owns the outcome.'),
 ('Single agent: one accountable loop','One model can use many tools',[('target','Goal','Prepare a source-linked morning brief.'),('robot','Hermes loop','Read Gmail, Calendar and Drive using gog.'),('check','Verify','Reconcile records and save brief locally.')],'One agent + three services remains a single-agent design.','If a source fails, mark that section unavailable; never invent an empty inbox.'),
 ('Workflow: predefined sequence','Known path, explicit stage contract',[('file','Extract','Invoice -> {po_id, amount, tax}.'),('scale','Match','Compare against PO and receipt.'),('user','Review','Officer resolves mismatched amount.')],'Use when every invoice must pass the same controls.','A fixed workflow can use one agent; multiple stages do not prove multiple agents.'),
 ('Routing: send work to the right owner','Classification + confidence + fallback',[('inbox','Classify','Label FAQ / refund / food safety.'),('route','Route','FAQ to drafter; risks to manager.'),('user','Escalate','Unknown label or uncertainty -> human.')],'Output contract = {case_id, label, evidence, owner}.','A router must handle unknowns; do not force every case into a known category.'),
 ('Parallel specialists: divide independent work','Useful only for separable questions',[('users','Split','Review comments, sales and competitor notes.'),('file','Workers','Separate reports with source IDs.'),('check','Merge','Verifier reconciles shared totals.')],'Lab 5 compares independent analysis with one-agent baseline.','Parallel workers must not edit the same output file.'),
 ('Orchestrator-workers: dynamic delegation','Controller decomposes a changing task',[('target','Plan','Break video request into specialist roles.'),('kanban','Dispatch','Use tasks, owners and dependencies.'),('check','Synthesis','Combine outputs; surface failed stages.')],'Task contract = owner + input + output + done criterion.','More agents adds coordination cost; measure end-to-end quality and time.'),
 ('Evaluator-optimizer: revise against criteria','A reviewer needs independent evidence',[('pen','Produce','Draft caption or candidate program.'),('eyecheck','Evaluate','Check C1-C10 or executable tests.'),('loop','Revise','Fix explicit failures; stop at limit.')],'Lab 2 QA report records failure -> revision -> result.','Self-critique is not ground truth; prices come from catalogue, not a second opinion.'),
 ('Human-in-the-loop: block consequential actions','Approval is a state transition',[('file','Draft','Save exact artifact and intended audience.'),('pause','Await approval','Freeze version; record decision.'),('user','Release gate','Human authorises only that version.')],'States = draft -> reviewed -> approved -> released.','APPROVE text is policy; enforce the gate by withholding publication capability.'),
 ('Human-on-the-loop: monitor bounded work','Use for reversible internal outputs',[('clock','Trigger','Scheduled internal report.'),('robot','Run','Read-only fetch; bounded records.'),('eye','Monitor','Check errors, coverage and cost.')],'Evidence = run timestamp, coverage, output link and exception log.','An installed cron is not proof of a successful run.'),
 ('Hierarchical team: company-level ownership','Separate execution from budget authority',[('gavel','Board','Approve hiring and mission.'),('org','CEO','Assign goals and issue owners.'),('users','Specialists','Deliver artifacts within budgets.')],'Paperclip Lab 7 org chart becomes PP Task 3 evidence.','Role labels alone do not prove distinct running agents.'),
 ('Scientific collaboration: expert-led discovery','Evidence must survive external testing',[('flask','Research goal','Scientist specifies question and constraints.'),('brain','Generate + critique','Agents propose ranked hypotheses.'),('user','Experiment','Scientist tests and interprets results.')],'AI co-scientist generates research proposals; experiments validate claims.','A plausible hypothesis is not a discovery and a model prediction is not a measurement.'),
 ('Choose the smallest effective design','Select by dependency and risk',[('target','Scope','One coherent task -> one agent.'),('layers','Separate','Independent expertise -> specialists.'),('hand','Gate','Irreversible action -> human decision.')],'Compare against a one-agent baseline before introducing a team.','Measure verified output per cost/time; agent count is not a success metric.'),
]
