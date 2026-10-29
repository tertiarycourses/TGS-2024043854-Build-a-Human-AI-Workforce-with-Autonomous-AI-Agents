"""Visual teaching units for v2.1, using the course's native-shape component library."""
import ccdeck as K
from data_2026 import CASE_GROUPS, PATTERNS, SOURCES
from ccdeck import *
SWDA='https://www.myskillsfuture.gov.sg/content/portal/en/career-resources/career-resources/education-career-personal-development/redeem-ai-subscription.html'
ANCHORS={}
def tag(D,kind,source='Classroom design; verify against supplied data'):
    s=D.prs.slides[-1]; s.notes_slide.notes_text_frame.text=f'Technical anchor: {kind}\nSource: {source}\nResearch checked: 29 October 2026.\nUse-case designs are teaching scenarios unless explicitly labelled research evidence.'
    ANCHORS[D.n]=(kind,source)
def trace(D,k,title,steps,evidence,source='Classroom workflow design',sub=None):
    flow(D,k,title,steps,sub=sub,tipt=evidence);tag(D,'ARCH',source)
def proof(D,k,title,items,source='Classroom verification model'):
    rows(D,k,title,items,dark=False);tag(D,'EVIDENCE',source)
def swda(D):
    trace(D,'Before we begin · SWDA','Free AI Subscription: Check, Attend, Redeem',[
      ('user','Eligibility','Singapore Citizen; age 18+.'),('search','Course label','Find the official “Free AI sub” label.'),('mail','Notification','After attending an eligible course.'),('check','Request + activate','Choose once; follow the official email.')],
      'One free six-month subscription per person. Eligible course end date: 16 Sep 2026 or later. Submit within 60 days of notification.',SWDA)
    proof(D,'Before we begin · SWDA','A Subscription Choice Is a Learning Decision',[
      ('check','Check eligibility','Verify the live MySkillsFuture course label and your own eligibility; a WSQ code alone is insufficient.'),
      ('clock','Wait for the official email','The request form arrives after eligible attendance; redemption is not a Day 1 prerequisite.'),
      ('hand','Choose carefully','Selection cannot be changed after submission. Compare the current official provider options first.'),
      ('tool','Separate lab access','A consumer AI subscription does not automatically include API credits, Dots access or API credits.')],SWDA)
    s=D.prs.slides[-1]; text(s,0.7,6.63,11.8,0.28,'Official redemption guide (click)',11,ACC_D).text_frame.paragraphs[0].runs[0].hyperlink.address=SWDA

def case_pair(D,group,ic,pair,index):
    s=D.new();header(D,s,'Topic 1 · 2026 opportunity gallery',group,'Proposed workflows · compare AI work, human decisions and observable evidence')
    for row,c in enumerate(pair):
      title,inp,work,human,out,metric,pattern=c;y=2.3+row*2.12
      icon(s,ic,.68,y+.01,.37);text(s,1.22,y,10.95,.38,f'{index+row:02d}  {title}',17,INK,bold=True,font=SERIF)
      text(s,1.24,y+.37,10.8,.22,pattern,11.5,TEAL,bold=True)
      nodes=[('INPUT',inp,'file'),('AGENT WORK',work,'robot'),('HUMAN DECISION',human,'user'),('EVIDENCE',out,'check')]
      for j,(label,body,glyph) in enumerate(nodes):
        x=.65+j*3.08;card(s,x,y+.68,2.87,1.02,fill=CHAR if j==2 else WHITE,shadow=False)
        text(s,x+.14,y+.77,2.59,.2,label,10.5,ACC if j==2 else TEAL,bold=True,autofit=False)
        text(s,x+.14,y+1.03,2.59,.57,body,13,SOFT if j==2 else MUTED,minpt=12)
        if j<3:line(s,x+2.90,y+1.18,x+3.05,y+1.18,ACC,1.7,arrow=True)
      text(s,.8,y+1.78,11.75,.31,'ACCEPT WHEN  '+metric,12,TEAL,bold=True,minpt=11.5)
    tag(D,'MODEL','Proposed classroom scenarios; not claims of actual deployments')

def topic1(D,C,mark):
    mark('t1a');section(D,'Topic 1','Humans + AI: The Collaboration Landscape',[
     'Who acts, who decides and who checks?','From AI history to agentic work','48 practical opportunities + future scenarios','Choose a collaboration design before a product'])
    trace(D,'Topic 1 · Opening landscape','One Launch, Four Ways to Share the Work',[
      ('user','Human + copilot','Manager directs every edit.'),('robot','Single agent','Hermes reads files and builds artifacts.'),('users','Agent team','Specialists own separate deliverables.'),('hand','Human approval','A person authorises public release.')],
      'Running case: Kopi Kaki’s product launch. We will compare outputs, verified quality, time and human effort.','IBM human-AI collaboration + Anthropic building effective agents')
    hub(D,'Topic 1 · Opening landscape','The 2026 Human–AI Workplace','Human owner\nGoal + judgement',[
     ('chat','Conversational copilots','Discuss, draft, revise with a person.'),('robot','Digital task agents','Operate files, email, calendar and tools.'),
     ('users','Multi-agent teams','Specialists coordinate and review work.'),('clock','Always-on assistants','Monitor bounded tasks and report exceptions.'),
     ('flask','Scientific collaborators','Propose hypotheses for expert testing.'),('building','Embodied agents','Sense and act in physical workspaces.')],foot='Different capabilities require different permissions, feedback and evidence; no product is best for every role.');tag(D,'ARCH','IBM; Google AI co-scientist; Gemini Robotics')
    compare(D,'Topic 1 · Opening landscape','Control and Capability Are Separate Choices',
     ('Capability axis','tool',['A chatbot can draft without tools.','An agent chooses tools and checks results.','Multiple agents add separate contexts and coordination.']),
     ('Human authority axis','hand',['Assist: a person directs each step.','Delegate: agent works within a bounded goal.','Approve: person controls consequential release.']),tipt='One agent can be highly autonomous; a team can still require human approval at every release.');tag(D,'MODEL','Anthropic building effective agents')
    timeline(D,'Topic 1 · History','From Rules to Models to Action',[
      ('Rules','1950s–80s','People encode explicit expert rules.'),('Learning','1990s–2010s','Models learn patterns from data.'),('Language','2017–2023','Transformers and chat interfaces scale generation.'),('Tool use','2024 onward','Models act, observe results and revise plans.')],foot='Different eras coexist: a 2026 agent still uses ordinary rules, databases and deterministic software.');tag(D,'MODEL','Vaswani et al., Attention Is All You Need; ReAct 2022')
    timeline(D,'Topic 1 · History','2023 → 2026: Four Engineering Lenses',[
     ('Prompt Engineering','2023','Instruction: “Write a launch brief.”'),('Context Engineering','2024','Supply catalogue, policy and source data.'),('Harness Engineering','2025','Add tools, state, checks and approval gates.'),('AI Agents','2026','Delegate work; inspect actions and results.')],foot='Course framing requested by the trainer: overlapping lenses, not invention dates or exclusive historical eras.');tag(D,'MODEL','Pedagogical framing; Anthropic context engineering 2025; agent workflows 2024')
    trace(D,'Topic 1 · History in practice','The Same Brief Gains Four Layers',[
      ('pen','Prompt','Goal + audience + format.'),('file','Context','Reviews + brand + approved price.'),('gear','Harness','Read tools + output checks + limits.'),('robot','Agent','Choose actions, verify, ask for a decision.')],
      'Observable output: research-brief.md with source IDs, limitations and a human decision log.','Course Lab 1')
    compare(D,'Topic 1 · Agents and agentic AI','A Digital Agent Can Run a Multi-Step Workflow',
      ('AI agent','robot',['One goal-directed loop with context, tools and state.','Reads Gmail, Calendar, Drive; writes a local brief.','Can plan many steps and use several tools.']),
      ('Agentic system','network',['System that plans and acts toward goals.','May use one agent or multiple coordinated agents.','A team adds separate roles, contexts and hand-offs.']),tipt='Vocabulary varies across sources. In this course always draw the runtime: number of agents, tools, state and decision owner.');tag(D,'ARCH','Anthropic building effective agents')
    trace(D,'Topic 1 · Practical mechanism','The Agentic Loop: Goal → Action → Evidence',[
      ('target','Receive goal','Produce a source-linked launch brief.'),('search','Gather context','Read reviews and approved files.'),('tool','Use a tool','Calculate totals; write an artifact.'),('eyecheck','Verify + decide','Check claims; revise or ask the human.')],
      'Stop when the acceptance criteria pass, a limit is reached, or a human decision is required.','ReAct; course Lab 1')
    for group,ic,cases in CASE_GROUPS:
      base=sum(len(cs) for g,i,cs in CASE_GROUPS[:CASE_GROUPS.index((group,ic,cases))])+1
      case_pair(D,group,ic,cases[:2],base);case_pair(D,group,ic,cases[2:],base+2)
    trace(D,'Topic 1 · Research evidence','AI for Science: Generate, Critique, Experiment',[
      ('user','Scientist','Sets research goal and constraints.'),('users','AI co-scientist','Generates, debates and ranks hypotheses.'),('flask','Experiment','Researchers test selected proposals.'),('check','Evidence','Compare results with the initial hypothesis.')],
      'Research case, not a classroom deployment. A generated hypothesis needs experimental validation.',SOURCES[7][1])
    trace(D,'Topic 1 · Research evidence','AlphaEvolve: Search Needs an Evaluator',[
      ('code','Seed solution','Working program + objective.'),('brain','Propose variants','Generate candidate algorithms.'),('gauge','Evaluate','Run correctness and performance checks.'),('loop','Keep + evolve','Retain useful candidates for another round.')],
      'Transfer to office work: supply a reliable check, such as totals that reconcile to a spreadsheet.',SOURCES[8][1])
    proof(D,'Topic 1 · Research evidence','Productivity Gains Can Hide Quality Trade-offs',[
      ('users','Study context','Pairit field experiment: 2,234 participants producing 11,024 advertisements.'),
      ('trend','Observed result','Human–AI teams produced more ads per worker and better text; human–human teams had better image quality.'),
      ('eye','Trade-off','Outputs were more homogeneous. Volume and average quality do not measure creative diversity.'),
      ('check','Lab implication','Score factual accuracy, visual quality and variety separately; do not assume the same benefit in every task.')],'https://arxiv.org/html/2503.18238v3')
    proof(D,'Topic 1 · Research evidence','Design Collaboration Around the Person',[
      ('user','Understand the user','Ask about goals, constraints and preferred involvement; do not infer sensitive traits from a few messages.'),
      ('handshake','Adapt collaboration','Offer drafts, explain changes, allow interruption and let the person choose the level of delegation.'),
      ('scale','Measure two outcomes','Evaluate task performance AND whether people can understand and steer the collaboration.'),
      ('check','Lab implication','Record one correction and show how the agent’s next output changed.')],'Columbia Building AI That Understands People; Mayer et al. 2026, doi:10.1186/s41235-026-00713-1')
    # Explicitly prospective: no fabricated rollout or claim of present capability.
    futures=[
     ('Humanoid + warehouse worker','Approved order + mapped work zone','Robot proposes pick-and-carry plan','Worker authorises task; supervisor controls stop','https://deepmind.google/models/gemini-robotics/'),
     ('Humanoid + manufacturing technician','Sensor anomaly + maintenance instruction','Robot brings tools and records inspection','Technician isolates machine and approves repair','https://www.figure.ai/'),
     ('Humanoid + hospital logistics staff','Approved non-clinical delivery request','Robot transports supplies in permitted areas','Staff verifies identity and route safety','https://deepmind.google/models/gemini-robotics/'),
     ('Humanoid + retail colleague','Stock task + customer nearby','Robot proposes replenishment or guidance','Employee handles accessibility and exceptions','https://www.figure.ai/'),
     ('Human + simulation team','Factory layout + operating constraints','Agents compare digital-twin scenarios','Engineer validates model before physical changes','Deloitte AI and VR: a model for human-AI collaboration'),
     ('Human + persistent research collective','Long-term goal + evolving evidence','Specialists monitor new findings and propose tests','Research owner sets budgets and accepts evidence','Google AI co-scientist; proposed future scenario'),
    ]
    for title,inp,act,gate,source in futures:
      trace(D,'Topic 1 · Future scenario · not a deployment claim',title,[('file','Sense / context',inp),('robot','Plan + act',act),('user','Human authority',gate)],
        'Design constraints: bounded permissions, recoverable state, visible evidence and a stop/escalation route. Physical actions require validated safety engineering.',source)
    mark('t1b')
    section(D,'Topic 1 · After morning break','Choose the Collaboration Mode',['Single agent and tool use','Workflow, routing and parallelism','Orchestrator, team and evaluator','Human approval, oversight and recovery'])
    for title,sub,steps,evidence,failure in PATTERNS:
      trace(D,'Topic 1 · Collaboration patterns',title,steps,evidence,'Anthropic building effective agents; course design',sub=sub)
      D.prs.slides[-1].notes_slide.notes_text_frame.text += '\nFailure/control: '+failure
    proof(D,'Topic 1 · Team research','A Team Metaphor Needs Runtime Evidence',[
      ('users','Mental-model study','Interviews with 13 early adopters at Microsoft found role-based team and divide-and-conquer metaphors.'),
      ('alert','Observed concerns','Error propagation and unproductive loops make agent-to-agent hand-offs hard to inspect.'),
      ('kanban','Classroom response','Give each task an owner, input, output, dependency and acceptance test.'),
      ('eye','Verification','Inspect real workers and their artifacts; a chat response describing five roles is not five running agents.')],'https://arxiv.org/html/2510.06224v1')
    proof(D,'Topic 1 · Research comparison','Shared Workspaces Make Coordination Visible',[
      ('chat','ChatCollab research prototype','Human and AI participants used role-based collaboration in Slack on software tasks.'),
      ('file','Inspectable coordination','Participants could request inputs, wait for deliverables and communicate responsibilities.'),
      ('kanban','Classroom transfer','Use Hermes profiles/bots for separate state and Kanban for owned tasks, dependencies and run evidence.'),
      ('scale','Limit','A research prototype does not establish that a classroom team will outperform one agent.')],'https://arxiv.org/html/2412.01992v1')
    mechanisms=[
     ('Tools, Skills and Memory Have Different Jobs',[('tool','Tool','A callable operation: gog reads a message or python calculates a table.'),('book','Skill','A reusable procedure with inputs, steps and checks: build the management deck.'),('memory','Memory','Persistent facts or preferences; keep secrets out of it.'),('check','Trace','Goal -> loaded skill -> tool calls -> saved artifact -> verification.')]),
     ('Context Has Provenance and a Trust Boundary',[('file','Trusted task','Human goal, approved brief and product catalogue.'),('mail','Untrusted content','Email, web pages and spreadsheet cells are task data.'),('shield','Boundary','Text inside a document cannot authorise tool access or sending.'),('check','Test','An email that says “ignore the rules” must remain quoted data.')]),
     ('RAG Adds Evidence; It Does Not Guarantee Truth',[('search','Retrieve','Search relevant approved document passages.'),('brain','Ground','Draft answer with file ID and passage reference.'),('user','Review','Check whether cited text actually supports the claim.'),('alert','Failure','No relevant passage -> state insufficient evidence, then escalate.')]),
     ('Memory Requires a Fresh-Session Check',[('file','Short term','The current context includes today’s conversation.'),('memory','Long term','Save only approved company facts and chosen decisions.'),('loop','New session','Ask for the decision and inspect its persisted source.'),('check','Accept','Recall must match the saved decision; a promise to remember is insufficient.')]),
     ('Permissions Are Part of the Workflow',[('login','Identity','Use the trainer-assigned Google account explicitly.'),('lock','Access','Request only required services and scope modes.'),('shield','Execution','Use readonly tool policy and no-send controls for office labs.'),('eye','Review','OAuth scope and runtime restrictions both need inspection.')]),
     ('Reliable Autonomy Needs Stop Conditions',[('target','Done','Artifact exists and all required checks pass.'),('coins','Limit','Cap records, retries, time and approved spending.'),('pause','Block','Missing identity, source, permission or human decision.'),('check','Report','Name what succeeded, what failed and what remains unknown.')]),
     ('Office Automation: One Agent, Many Artifacts',[('mail','Collect','Bounded Gmail, Calendar and Drive reads.'),('chart','Calculate','Read Excel with reproducible formulas.'),('code','Create','Generate interactive HTML and editable PowerPoint.'),('user','Review','Owner checks figures and chooses the business action.')]),
     ('Compare Benefits with Verification Cost',[('clock','Baseline','Manual work: 45 minutes, including checks.'),('robot','Agent workflow','Preparation 10 + run 5 + review 15 = 30 minutes.'),('gauge','Net saving','45 - 30 = 15 minutes, not the full generation time.'),('check','Quality gate','Reject a faster result if its evidence or calculations fail.')]),
    ]
    for title,items in mechanisms:proof(D,'Topic 1 · Agent mechanisms',title,items)
    trace(D,'Topic 1 · Model mechanism','The LLM Proposes Tokens; the Agent Executes Tools',[
      ('file','Tokenise context','Goal + source text + tool results become input tokens.'),
      ('brain','Transformer inference','Learned weights + attention estimate P(next token | context).'),
      ('tool','Tool boundary','Generated action request is checked and executed by the harness.'),
      ('loop','Observe + verify','Real tool result returns as context; model proposes the next step.')],
      'Training changes model weights; adding a skill, source file or memory changes runtime context. A plausible completion is not a verified fact.',
      'https://arxiv.org/abs/1706.03762 ; https://arxiv.org/abs/2210.03629')
    proof(D,'Topic 1 · Transfer to logistics','A Logistics Brief Needs Evidence at Each Step',[
      ('file','Perception','Read shipment IDs, promised dates and current event timestamps.'),
      ('brain','LLM work','Interpret free-text delay reports and propose an exception summary.'),
      ('tool','Strengths + limits','Tools compute exact delays; the LLM handles varied language. Missing events or unsupported causal stories still need review.'),
      ('check','Verification','Every late-shipment claim cites an ID/time; dispatcher approves route or customer action.')],
      'Classroom transfer scenario: inspectable task data and controls, not an assessment model answer')
    compare(D,'Topic 1 · RAG comparison','RAG and a Standard LLM Have Different Evidence Paths',
      ('Standard LLM assistant','chat',['Generates from learned weights and supplied context.','Fast setup; useful for drafts and general reasoning.','May miss private/current policy; unsupported facts need checking.']),
      ('Retrieval-augmented agent','search',['Retrieves authorised document passages before generating.','Can cite current internal evidence and use relevant tools.','Bad retrieval, stale sources or ignored access rules can still fail.']),
      tipt='Neither design guarantees correctness. Check the cited passage and choose based on freshness, privacy and maintenance needs.');tag(D,'ARCH','https://arxiv.org/abs/2005.11401')
    trace(D,'Topic 1 · RAG maintenance','Keeping RAG Useful Is an Operational Workflow',[
      ('folder','Ingest + control','Approved documents, ownership and access rules.'),
      ('layers','Prepare + index','Split passages; update search/vector index when sources change.'),
      ('search','Retrieve + answer','Filter by user access; return passages with source/version IDs.'),
      ('eyecheck','Maintain + test','Retire stale documents; re-index; test retrieval and answer support.')],
      'Budget for document curation, indexing, retrieval latency, model calls and evaluation. Compare that upkeep with the value of current internal evidence.',
      'https://arxiv.org/abs/2005.11401 ; course maintenance scenario')
    proof(D,'Topic 1 · Governance','People Need Authority, Feedback and Recourse',[
      ('user','Owner','Name the human accountable for each workflow and any affected colleague.'),('hand','Authority','State which actions the AI may take and which require approval.'),
      ('chat','Feedback','Give a reason for rejection and an opportunity to revise.'),('pause','Recovery','Pause the agent, restore the prior artifact and route unresolved cases.')],'UNSW BusinessThink workplace collaboration governance; IBM')
    proof(D,'Topic 1 · Governance','Trust Comes from Checkable Behaviour',[
      ('eye','Understand','Show source IDs, assumptions, uncertainty and pending actions.'),('handshake','Calibrate','Use bounded trials; avoid treating a friendly persona as evidence of competence.'),
      ('scale','Evaluate','Measure task quality, human control, correction effort and failure recovery.'),('user','Respect autonomy','Allow the person to change collaboration mode or stop the work.')],'Murthy et al. 2026, doi:10.1007/s00146-026-02977-z; Mayer et al. 2026')
    proof(D,'Topic 1 · Agent market','Compare Products by Workflow Fit',[
      ('robot','Hermes','Day 1: local agent, tools, skills, memory and Telegram; one model loop owns the office pack.'),
      ('chat','OpenAI Dots','Trainer demo: persistent assistant and tool actions; use only available account capabilities.'),
      ('users','Hermes teams','Day 2: actual separate profiles/bots, owned outputs, Kanban parent edges and run history.'),
      ('hand','Human oversight','Unassigned human gates, source verification and exact-version acceptance.')],'Official Hermes and OpenAI Dots documentation')
    mark('activity')
    trace(D,'Topic 1 · Canvas activity','Design the Launch Office Before Building It',[
      ('target','Pick the outcome','Prepare the launch manager’s office pack.'),('file','Map evidence','Email, events, Drive files and Excel source rows.'),('robot','Choose a mode','Single agent first; team only for separable work.'),('user','Name decisions','Manager chooses angle, accepts figures and approves release.')],
      'Canvas fields: task | input | AI action | human owner | mode | output | acceptance test | stop condition.')
    proof(D,'Topic 1 · Canvas activity','Turn an Opportunity into a Testable Brief',[
      ('mail','Workload','Find at most 10 launch emails, today’s events and 10 approved Drive files.'),
      ('chart','Analysis','Calculate outlet sales, revenue totals and review trends from the supplied workbook.'),
      ('file','Deliverables','Produce morning-brief.md, analysis.xlsx, dashboard.html and management-brief.pptx.'),
      ('check','Definition of done','Figures reconcile; sources are traceable; HTML works offline; slides are readable; nothing sent.')])
    proof(D,'Topic 1 · Before lunch','What You Will Build in Two Days',[
      ('robot','Day 1: single agent','Install Hermes Desktop + Telegram; connect gog; analyse Excel; build dashboard and professional slides.'),
      ('users','Day 2: agent team','Use Hermes bots with owned outputs, Kanban dependencies and independent video review.'),
      ('hand','Human role','Set goals, verify facts, challenge analysis, direct revisions and approve the exact release version.'),
      ('check','Assessment bridge','Keep Activity 1 Telegram, Activity 3 professional PPT and Activity 5/8 real Kanban video-team evidence.')])

def demo(D,mark):
    mark('demo')
    trace(D,'After lunch · Trainer demo','Watch a Digital Agent Complete Office Work',[
      ('user','Brief','Ask Dots to prepare a launch meeting pack.'),('tool','Observe','Inspect sources, tool actions and saved outputs.'),('hand','Intervene','Correct one fact and reject an unsupported claim.'),('check','Compare','Now repeat the pattern with one Hermes agent.')],
      '15-minute trainer demo. Use a prepared recording or Hermes if the trainer account lacks Dots access. No learner purchase required.',SOURCES[6][1])
    proof(D,'After lunch · Trainer demo','Watch the Work, Then Inspect the Result',[
      ('eye','Evidence','Which source supports each claimed meeting, email or product fact?'),('tool','Action','Did a tool actually run, or did the assistant only describe an intended action?'),
      ('hand','Human control','Which action is pending approval? Can the person interrupt and revise?'),('check','Transition to Activity 1','Download Hermes Desktop, verify Telegram and produce the Lab 1 brief for PP Task 1.')],SOURCES[6][1])

def office(D):
    """Day 1 Hermes concept slides keyed by title; build_slides places each before its lab."""
    R={}
    R['Hermes Desktop: Download → Configure → Connect']=lambda k:trace(D,k,'Hermes Desktop: Download → Configure → Connect',[
      ('download','Official installer','Mac: DMG. Windows: EXE. Linux: linked terminal route.'),
      ('login','Local profile','Select approved provider and verify a real reply.'),
      ('folder','Workspace','Open the launch folder and confirm source files.'),
      ('chat','Optional Telegram','Messaging → Telegram → Create with QR; verify allowlist and restart.')],
      'If Telegram is enabled, use the same local runtime as Desktop/tools. Native Windows and WSL do not automatically share credentials or files.',
      'https://hermes-agent.nousresearch.com/desktop ; https://hermes-agent.nousresearch.com/docs/user-guide/desktop')
    R['One Hermes Agent Runs the Launch Office']=lambda k:trace(D,k,'One Hermes Agent Runs the Launch Office',[
      ('mail','gog + Google','Read assigned Gmail, Calendar and Drive.'),('chart','Spreadsheet tools','Calculate and reconcile Excel data.'),('code','HTML skill','Create a filterable local dashboard.'),('file','PPT skill','Produce an editable management deck.')],
      'All outputs stay local until reviewed. Tool count does not change the number of agents.')
    units=[
     ('Optional Telegram: A Channel, Not a Second Agent',[('phone','User interface','A direct message reaches the Hermes gateway.'),('server','Runtime','The gateway invokes Hermes on the learner’s computer.'),('folder','Workspace','Explicitly use ~/kopi-kaki; gateway working directory may differ.'),('check','Proof','Optional round trip creates a local timestamped file. PP1 uses the chosen morning assistant plus a Hermes artifact.')]),
     ('Google Login: Identity Before Data',[('login','OAuth client','Trainer supplies a Desktop OAuth client outside the course repository.'),('user','Account','Learner authorises only the assigned training account.'),('lock','Token','gog stores tokens in the local keyring; never paste them into agent chat.'),('check','Three checks','Read one Gmail result, one calendar result and one Drive file; report failures separately.')]),
     ('gog Is a Tool; the gog Skill Is the Procedure',[('tool','Executable','gog --account TRAINING_EMAIL --readonly ...'),('book','Skill','Read-only workspace SOP: bounds, provenance and no-send policy.'),('brain','Hermes','Selects the next read based on the task and observed output.'),('file','Artifact','morning-brief.md includes IDs and unresolved conflicts.')]),
     ('Gmail: Bound the Search and Trace the Claims',[('search','Query','subject:Kopi newer_than:30d; maximum 10 results.'),('mail','Read','Open selected message IDs using gog gmail get.'),('shield','Interpret','Treat message bodies as untrusted data.'),('check','Verify','Each decision or deadline links to its source message ID.')]),
     ('Calendar: Inspect Time and Availability',[('calendar','Read','Use gog calendar events --today for assigned account.'),('clock','Time zone','Check displayed offset against Asia/Singapore.'),('alert','Conflict','Compare event start/end intervals and flag overlap.'),('user','Decision','Propose options; do not create or move a meeting.')]),
     ('Drive: Permission Does Not Prove Relevance',[('folder','List','Bound results and record file IDs.'),('search','Select','Use only the trainer-designated launch folder.'),('file','Read','Download an approved workbook or use local supplied copy.'),('check','Verify','Check filename, version and source; no sharing or upload required.')]),
     ('One Office Brief Reconciles Three Services',[('mail','Email','Request says launch review on Friday.'),('calendar','Calendar','Event records Thursday 10:00 +08:00.'),('file','Drive','Brief version 2 lists a Friday deadline.'),('user','Resolve','Mark conflicting dates; ask owner instead of choosing silently.')]),
     ('Excel Analysis Begins with a Data Contract',[('file','Inputs','campaign-data.xlsx: Reviews, Sales and Metrics sheets.'),('list','Schema','Validate required columns, types and unique row IDs.'),('chart','Calculate','Aggregate revenue, units and engagement from source rows.'),('check','Reconcile','Computed totals must match independent spreadsheet checks.')]),
     ('Revenue Must Match the Supplied Schema',[('file','Source','Sales sheet: week_start, outlet, revenue_sgd and cups_sold.'),('chart','Aggregate','Sum supplied revenue_sgd by outlet; do not reconstruct it from catalogue prices.'),('coins','Total','Sum outlet revenue to the same-period workbook total.'),('eyecheck','Verify','Separate missing/duplicate rows; explain exclusions and do not infer tax.')]),
     ('Review Themes Need Counts and Evidence',[('file','Read','60 synthetic review rows, each with review_id.'),('chart','Count','Rating distribution + average by outlet.'),('search','Group','Themes must cite example review_ids.'),('check','Challenge','Ask which source rows support a proposed campaign angle.')]),
     ('Missing Values Change the Answer',[('alert','Detect','Blank outlet, non-numeric units or duplicate IDs.'),('file','Log','Write data-quality.md with row IDs and counts.'),('user','Decide','Separate excluded rows and explain the rule.'),('check','Reconcile','Report raw rows, valid rows, excluded rows and aggregate totals.')]),
     ('Interactive Artifacts: A Local HTML Dashboard',[('code','Data','Embed only synthetic aggregate data in dashboard.html.'),('eye','Views','Outlet selector, KPI cards, bar chart and data table.'),('user','Interaction','Filter outlet; sort rows; reset to all outlets.'),('check','Test','Open offline and confirm filtered totals reconcile to Excel.')]),
     ('Interactivity Must Change the Evidence View',[('user','Action','Select an outlet and date range.'),('chart','Expected','KPIs and visible rows change together.'),('file','Cross-check','Exported CSV equals the visible table.'),('alert','Failure','A decorative button that changes nothing fails the lab.')]),
     ('A Professional PPT Needs a Decision Story',[('target','Audience','Operations manager choosing launch priorities.'),('file','Narrative','Problem -> evidence -> options -> recommendation.'),('chart','Visuals','Editable chart, workflow and comparison.'),('user','Decision','End with one choice and the evidence supporting it.')]),
     ('The PPT Skill Makes Quality Repeatable',[('book','Inputs','Approved brief, workbook totals and brand guide.'),('pen','Build','Six editable slides with readable labels and notes.'),('eyecheck','Render','Export PDF or inspect in PowerPoint; correct clipping.'),('check','Accept','Every figure traces to a row/table; all six slides readable.')]),
     ('Separate Content Errors from Layout Errors',[('file','Factual check','Prices and dates match approved sources.'),('chart','Numeric check','Chart data equals verified workbook totals.'),('eye','Visual check','No clipping, overlap or unreadable labels.'),('hand','Revision','Record one failure, fix it, render and inspect again.')]),
     ('One Agent, Four Office Skills',[('book','gog-office','Read assigned services and preserve source IDs.'),('chart','office-analytics','Validate workbook, compute and reconcile metrics.'),('file','professional-ppt','Turn approved findings into an editable deck.'),('code','interactive-dashboard','Build and test the local filterable artifact.')]),
     ('Skill Instructions Cannot Create Capabilities',[('book','Instruction','A skill describes how to perform the work.'),('tool','Dependencies','gog, Python packages and slide/video renderers must exist.'),('lock','Permissions','OAuth or paid provider access is configured separately.'),('check','Probe','Version + one real read/render is stronger evidence than skill installation.')]),
     ('Practice Checkpoint: Validate the Office Pack',[('mail','Brief','IDs from three services, with coverage and conflicts.'),('chart','Workbook','Totals reconcile; rejected rows documented.'),('code','Dashboard','Filters and CSV export work offline.'),('file','Deck','Six editable slides with sources and a checked PDF.')]),
     ('What Failed? Diagnose Before Retrying',[('login','OAuth error','Check account, client, enabled APIs and test-user eligibility.'),('server','Gateway error','Check running process, allowed ID and executable PATH.'),('chart','Data error','Inspect sheet names, numeric types and duplicates.'),('file','Artifact error','Open saved file; check actual output, not chat completion text.')]),
    ]
    for title,items in units:R[title]=lambda k,title=title,items=items:proof(D,k,title,items)
    return R
