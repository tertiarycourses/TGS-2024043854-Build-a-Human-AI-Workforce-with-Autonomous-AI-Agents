"""Detailed steps and copy-ready prompts for the Day 2 labs (v3.5: Hermes Desktop only — no command lines for learners).
Activity 4: five named bots in one group chat. Activity 5: one prompt builds the video team and its Kanban board.
Activity 6: scheduled jobs auto-generate next week's content. Bot Mode facts checked against the Hermes docs
(user-guide/bot-mode) on 31 Oct 2026; Desktop screens match the trainer's Hermes Desktop v0.22.5 screenshots."""
from labs_v22 import step

def S(title, body="", cmd=None, prompt=None, where=None, expect=None, decide=None):
    d = step(title, body=body, expect=expect) if expect else step(title, body=body)
    if cmd: d["cmd"] = cmd
    if prompt: d["prompt"] = prompt
    if where: d["where"] = where
    if decide: d["decide"] = decide
    return d

WSF = "Desktop/kopi-kaki"
COPY = ("In Finder (Mac) or File Explorer (Windows), open this lab's data folder from the unzipped course files, select everything and drag it "
        f"into your {WSF} folder. Choose Skip (do not replace) for files that already exist. "
        f"Then in Hermes Desktop click + (left of Ask anything) → Folder… and choose {WSF}: Mia now has this lab's files and AGENTS.md. "
        "Start the session with: 'Read AGENTS.md in the attached folder and follow it for this session.'")

# The Activity 4 team: name, title, one-line description (pasted into New Agent), soul file
SOCIAL_TEAM = [
 ("Rafi", "Market Researcher", "Finds launch angles, audience insights and facts for Kopi Kaki posts; cites the source file for every fact.", "rafi"),
 ("Lin", "LinkedIn Writer", "Writes the founder's LinkedIn post: story, one proof point, call to action; professional Singapore English.", "lin"),
 ("Farah", "Facebook Writer", "Writes the neighbourhood Facebook post: pop-up dates, the 1 Dec opening, friendly kopitiam voice.", "farah"),
 ("Ivy", "Instagram Writer", "Writes the Instagram hook, caption and hashtags, plus a one-line image brief.", "ivy"),
 ("Pixel", "Image Creator", "Makes one on-brand 1080x1350 image per post and the review gallery that shows every post as it will look.", "pixel"),
]
VIDEO_TEAM = [("video-researcher", "Extracts the facts the video may use: claim | source file | exact quote"),
              ("scriptwriter", "Turns research.md into a 20-second, 4-scene script, then waits for the founder"),
              ("voice-over", "Records the narration from the APPROVED script with Hermes text-to-speech"),
              ("video-producer", "Renders the APPROVED script into a 1080x1920 MP4 with HyperFrames"),
              ("video-reviewer", "Independently checks the video against the QA checklist and sends the founder a review link")]

# ---------------------------------------------------------------- Activity 4 · five named bots in one group chat
def act4(L):
    L["prereq"] = ["Topic 2 setup done: Hermes Desktop with a working model; Telegram connected",
                   "Activity 2 website and Activity 3 deck saved — the team reuses their facts",
                   f"This lab's data/ dragged into {WSF} (souls/ holds the five role files; tools/make_post_image.py makes the images)"]
    hire = "\n".join(f"- {n} · {t} · {d}" for n, t, d, _ in SOCIAL_TEAM)
    L["steps"] = [
     S("Copy the team files into your company folder (3 min)", COPY + " souls/ holds one role file per bot: who it is, what it writes and the rules it must never break.",
       expect="souls/ lists rafi, lin, farah, ivy and pixel .SOUL.md files."),
     S("Hire five bots with New Agent (12 min)",
       "Open the Bots tab (next to Sessions) and click New Agent. For each bot fill in Name, Title and Description below, open Advanced → Custom SOUL.md and paste the text of its souls/<name>.SOUL.md file, then create it. "
       "Each bot introduces itself in its own Bot Chat. Right-click a bot → Edit Profile to give it an avatar (Bot, Generate, Upload or a Pet).\n" + hire,
       expect="Rafi, Lin, Farah, Ivy and Pixel appear in the Bots roster, each with its own title."),
     S("Meet your team (5 min)",
       "Click each bot to open its Bot Chat and check that it answers in its own role. If a bot says it has no model, open Settings → Model, pick that bot under 'Applies to', choose your provider, sign in and Apply.",
       where="Hermes Desktop → Bots tab → Rafi (then Lin)",
       prompt="Hi, I'm the founder of Kopi Kaki Co. In two sentences: what is your job on my marketing team, and which files in my Desktop/kopi-kaki folder will you read first?",
       expect="Each bot describes its own role and names AGENTS.md, campaign-brief.md and brand-guide.md."),
     S("Put the team in one group chat (5 min)",
       "Right-click Rafi → Manage groups → create a group called 'Kopi Social Team' inline, then add Lin, Farah, Ivy and Pixel the same way (a group holds 2–6 bots). Click the group row → Open chat. "
       "In a group, your message starts up to three rounds of bot turns; bots hand work to each other with @name and ask you with @user.",
       expect="The roster shows 'Kopi Social Team · 5 bots'; the room opens with all five members."),
     S("Post the brief and watch them hand off (15 min)",
       "One message briefs the whole team. Rafi researches first; the three writers start when Rafi hands off. Watch the room: who speaks, who passes, who asks you.",
       where="Hermes Desktop → Kopi Social Team (group chat)",
       prompt="Team, we launch the Gula Melaka Cold Brew on 1 Dec 2026. Work in Desktop/kopi-kaki and follow AGENTS.md, brand-guide.md and compliance-rules.md.\n"
              "@rafi research first: write outputs/social/research.md with 3 launch angles, the top 3 things tasters loved (with review IDs) and 5 approved facts with their source file. Then hand off to @lin @farah @ivy.\n"
              "@lin write outputs/social/linkedin.md, @farah write outputs/social/facebook.md, @ivy write outputs/social/instagram.md — each from research.md and your own role file.\n"
              "Never post anything. If you are unsure about a fact, ask me with @user.",
       expect="research.md first, then three platform drafts; anything uncertain comes to you as an @user question."),
     S("Ask Pixel for the images and the gallery (8 min)",
       "Pixel makes one image per post with the small image tool in your folder and builds one page that shows every post the way it would look on its platform.",
       where="Hermes Desktop → Kopi Social Team",
       prompt="@pixel make one 1080x1350 image for each of linkedin.md, facebook.md and instagram.md with tools/make_post_image.py (Python from .office-venv), save them in outputs/social/images/, then build outputs/social/gallery.html with one card per platform and open it for me.",
       expect="gallery.html opens: three platform cards, each with its image, copy and hashtags."),
     S("Review like the founder: APPROVE, EDIT or REJECT (8 min)",
       "Check every post against brand-guide.md and compliance-rules.md: price SGD 6.80, launch 1 Dec 2026, SHIOK20 terms if the code appears, no health or halal claims, no competitor bashing. Send one post back with a concrete edit.",
       where="Hermes Desktop → Kopi Social Team",
       prompt="My decisions:\n- LinkedIn: APPROVE\n- Facebook: EDIT — @farah put the first pop-up date in the first line and cut the post to 80 words\n- Instagram: APPROVE\n"
              "@pixel when Farah is done, refresh the gallery and record every decision with today's date and my reason in outputs/social/approval-log.md.",
       expect="Farah revises; the gallery shows the edited Facebook post; approval-log.md has three rows.",
       decide="Which posts are ready, which need a concrete change; nothing is published."),
     S("Reflect: team versus one agent (4 min)", "Compare the bots with Mia working alone in Activities 2 and 3.",
       where="Hermes Desktop → Mia (your first session)",
       prompt="Compare today's five-bot group chat with you working alone on Day 1: time to first draft, how different the three posts sound, number of my edits, and coordination overhead. Give me a 5-row table and one recommendation: when should Kopi Kaki use a group of bots, and when one agent?",
       expect="A short evidence-based comparison you can discuss in class."),
    ]
    L["verify"] = ["Five bots in the roster with names, titles and role files", "The group 'Kopi Social Team' shows the hand-off: research → three writers → images",
                   "gallery.html shows three platform posts with images", "approval-log.md records a decision for every post; nothing was posted publicly"]
    L["trouble"] = [("A bot has no model", "Settings → Model → pick the bot under 'Applies to' → choose the provider, sign in, Apply."),
                    ("Nobody answers in the group", "@mention the bot you want (@rafi …). A message with no mention lets each bot decide whether to speak."),
                    ("The room stops after three rounds", "That is the safety cap. Send a short follow-up: '@lin @farah @ivy please continue from research.md'."),
                    ("Image tool fails", "Ask Mia in your own session: 'Install Pillow into .office-venv in Desktop/kopi-kaki.'"),
                    ("A writer invents a price or promo", "Reply '@<writer> use only product-catalogue.csv and campaign-brief.md' and add the rule to its role file (Edit Profile → SOUL.md).")]
    L["challenge"] = "Hire a sixth bot, Tash the TikTok Writer, add her to the group and ask for a 15-second script. What did the extra specialist cost in time and review effort, and was it worth it?"

# ---------------------------------------------------------------- Activity 5 · Kanban video team built by prompt (PP Task 3)
def act5(L):
    L["prereq"] = ["Activity 4 done", f"This lab's data/ dragged into {WSF} (souls/, tasks/, DESIGN.md and video-qa-checklist.md)",
                   "Lab laptops: Node.js 22+ and FFmpeg for HyperFrames — Mia checks them for you; the trainer installs anything missing before class",
                   "Settings → Voice → Text to speech set to Edge (free) from the Topic 2 setup"]
    team = "\n".join(f"- {n}: {d} (role file souls/{n}.SOUL.md)" for n, d in VIDEO_TEAM)
    L["steps"] = [
     S("Copy the video team files (2 min)", COPY,
       expect="souls/ now also lists video-researcher, scriptwriter, voice-over, video-producer and video-reviewer; tasks/ has v1–v5."),
     S("Install the video skill — by asking (8 min)",
       "HyperFrames (HeyGen) writes each scene as HTML and renders an MP4 — the team's renderer. Remotion (React) and Manim (maths animation) are alternatives worth knowing. "
       "You can also search 'hyperframes' in Capabilities → Skills and click Install.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Install the official hyperframes skill from the Hermes skills hub. Read its SKILL.md first and tell me what it needs. Then check that this laptop has what it needs (Node.js 22 or newer, FFmpeg, a browser) and run its health check. If anything is missing, tell me exactly what to ask the trainer to install. Do not change system settings.",
       expect="'hyperframes' appears in Capabilities → Skills and the health check passes (or Mia names what is missing)."),
     S("One prompt: hire the video team and build its Kanban board (10 min)",
       "This is the prompt method: you describe the team and the work; Mia creates the five agents (they also appear in the Bots tab) and the Kanban board with your two HUMAN gates.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Build my video production team and its Kanban board. Workspace: Desktop/kopi-kaki.\n"
              "1. Create these five agents (Hermes profiles) by cloning your settings, each with its role file as SOUL.md and the description shown:\n" + team + "\n"
              "2. Create a Kanban board for tenant kopi-video with these cards:\n"
              "   1 Research the launch video · video-researcher · body tasks/v1-research.md\n"
              "   2 Write the 20-second script · scriptwriter · parent 1 · body tasks/v2-script.md\n"
              "   3 HUMAN: approve the script · unassigned · parent 2 · only I complete it\n"
              "   4 Record the voice-over · voice-over · parent 3 · body tasks/v3-voice.md\n"
              "   5 Render the video · video-producer · parents 3 and 4 · skill hyperframes · body tasks/v4-produce.md\n"
              "   6 Review and send me the link · video-reviewer · parent 5 · body tasks/v5-review.md\n"
              "   7 HUMAN: approve the exact video · unassigned · parent 6 · only I complete it\n"
              "3. Show me the agents and the cards (ID, assignee, parents) as two tables. Never publish or post the video anywhere.",
       expect="Two tables: five agents, seven cards with two unassigned HUMAN cards. The agents appear in the Bots tab."),
     S("Watch the board work (8 min)",
       "Open Kanban in the left sidebar and choose the kopi-video board. A card runs only when every parent is done; your HUMAN card holds everything after it. Open a card to read its run history and output.",
       expect="Research runs first, then the script; card 3 (yours) waits."),
     S("Check the research — grounding (5 min)",
       "The researcher may only use facts it can point to in a source file: this is grounding, the same idea as retrieval-augmented generation (RAG). Check two claims yourself.",
       where="Hermes Desktop — Mia",
       prompt="Open outputs/video/research.md for me and pick two claims. For each, show me the exact line in the source file that supports it.",
       expect="Every claim names its source file and quote; unsupported ideas are marked UNVERIFIED."),
     S("Approve the script — your first gate (5 min)",
       "Read script.md: four scenes, 20 seconds, on-screen text of seven words or fewer per scene, price SGD 6.80, launch 1 Dec 2026, no health or halal claims. Approve it, or ask for one change first.",
       where="Hermes Desktop — Mia",
       prompt="I have read outputs/video/script.md and APPROVE it as written. Record my approval with today's date in outputs/video/approvals.md, then complete the 'HUMAN: approve the script' card on the kopi-video board for me.",
       expect="The voice-over and render cards start.", decide="Is every word on screen true, on-brand and allowed?"),
     S("Production and voice-over (20 min)",
       "The voice-over agent records the narration with Hermes's free text-to-speech; the producer builds the HyperFrames video and adds the narration. Check the real file, not the success message.",
       where="Hermes Desktop — Mia",
       prompt="Check outputs/video/final.mp4 for me: does it exist, what are its width, height and duration, and does it have an audio track? Answer in one line per check.",
       expect="final.mp4 exists, 1080×1920, about 20 seconds, with audio."),
     S("Independent review and the review link (10 min)",
       "The reviewer checks every scene against video-qa-checklist.md (V1–V9) and the sources, writes review.md with the file's SHA-256 fingerprint, starts a local link and messages you on Telegram. The link works on your laptop only.",
       expect="A Telegram message with the review link (http://localhost:8765/final.mp4), PASS/FAIL per check and the SHA-256."),
     S("Approve the exact video — your final gate (10 min)",
       "Watch the whole video from the link. If anything is wrong, request one revision: the producer re-renders, the reviewer re-checks, and the new file gets a new fingerprint — your old approval does not carry over.",
       where="Hermes Desktop — Mia",
       prompt="I watched http://localhost:8765/final.mp4 to the end. Check that its SHA-256 matches review.md. If it matches, record 'APPROVE <sha256>' with today's date in outputs/video/approvals.md and complete the 'HUMAN: approve the exact video' card for me. Do not post or publish the video anywhere.",
       expect="approvals.md shows APPROVE with the same fingerprint as review.md.", decide="Accept this exact file, or request one revision."),
     S("Capture your PP Task 3 evidence (5 min)",
       "Take TWO readable screenshots of your own work: (A) the Kanban view in Hermes Desktop showing the agent names, a dependency or HUMAN gate and the video task; (B) final.mp4 playing in a media player. Hide keys and private data. Keep final.mp4, research.md, review.md and approvals.md."),
     S("Reflect: what did the team buy you? (5 min)", "Compare effort, cost and quality.",
       where="Hermes Desktop — Mia",
       prompt="Summarise the kopi-video run: total time, number of runs per card, what the reviewer caught, my revisions and an estimated model cost. Compare with an agency quote of SGD 3,000 and two weeks. What would you change in one role file to cut my review time next week?",
       expect="An honest summary including what failed."),
    ]
    L["verify"] = ["hyperframes installed and its health check passes", "Five video agents and a seven-card board with two HUMAN gates, created by one prompt",
                   "research.md links every claim to a source file", "final.mp4 is 1080×1920, ~20 s, with narration",
                   "review.md passes V1–V9 with evidence; approvals.md fingerprint = file fingerprint", "PP Task 3: two screenshots — Kanban board and the video playing"]
    L["trouble"] = [("Cards stay waiting and never run", "Keep Hermes Desktop open. Ask Mia: 'Why is card <n> on kopi-video not running?'"),
                    ("HyperFrames health check fails", "Node.js or FFmpeg is missing: ask the trainer; Mia tells you exactly which one."),
                    ("Render card ran before your approval", "The card was created without the HUMAN card as parent. Ask Mia to block it, fix the parent and re-run."),
                    ("No audio in final.mp4", "Ask Mia to check the narration file exists and to have the producer re-render with it."),
                    ("Review link does not open", "Open it on the same laptop; ask the reviewer to start the link again.")]
    L["challenge"] = "Ask Mia to add a second cut: a 1:1 square version from the same script. How much extra review does a second format cost you?"

# ---------------------------------------------------------------- Activity 6 · scheduled jobs auto-generate content
def act6(L):
    L["prereq"] = ["Activities 4 and 5 done (bots, role files and the kopi-video board exist)", "Telegram connected with /sethome from the Topic 2 setup",
                   "Hermes Desktop stays open while a job runs (on a laptop that sleeps, nothing runs)"]
    L["steps"] = [
     S("Read a scheduled job like a recipe (3 min)",
       "Open Scheduled jobs in the left sidebar and click your Morning email brief. Every job has the same parts: a name, a frequency, the next run, where it delivers, and the prompt it runs. "
       "Pause stops it; Trigger now runs it immediately. The Blueprints list shows ready-made jobs (Weekly review, Competitor news watch, Topic news digest …).",
       expect="You can point to the frequency, the delivery target, the prompt, Pause and Trigger now."),
     S("Monday 9:00: the week's social drafts (7 min)",
       "The job starts the work; you still approve. It writes drafts into a dated folder and tells you on Telegram — it never posts.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Create a scheduled job called 'Weekly social drafts' that runs every Monday at 9:00 Asia/Singapore time and delivers to my Telegram.\n"
              "Job: in Desktop/kopi-kaki, read campaign-brief.md, research.md and last week's approval-log.md. Following the rules in souls/lin.SOUL.md, souls/farah.SOUL.md and souls/ivy.SOUL.md, draft this week's LinkedIn, Facebook and Instagram posts into outputs/social/weekly/<date>/, "
              "make one image per post with tools/make_post_image.py and a gallery.html. Then message me: 'Drafts ready — reply APPROVE, EDIT or REJECT per post'. Never post or publish anything.\n"
              "Show me the job when it is saved.",
       expect="'Weekly social drafts' appears in Scheduled jobs: every Monday 9:00, delivered to Telegram."),
     S("Friday 10:00: a new video draft on the board (7 min)",
       "This job does not make the video itself: it starts a new run on the Kanban board, so your two HUMAN gates still hold.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Create a scheduled job called 'Weekly video draft' that runs every Friday at 10:00 Asia/Singapore time and delivers to my Telegram.\n"
              "Job: on the kopi-video Kanban board, create a new run for a 15-second clip about this week's best-performing angle from outputs/social/approval-log.md: the same seven cards as Activity 5 with both HUMAN gates (approve the script, approve the exact video). "
              "Message me when the script is waiting for my approval. Nothing is rendered before I approve the script; nothing is published.\n"
              "Show me the job when it is saved.",
       expect="'Weekly video draft' appears in Scheduled jobs: every Friday 10:00."),
     S("Test both now with Trigger now (8 min)",
       "Do not wait until Monday. In Scheduled jobs open each job and click Trigger now. Check Telegram, the new dated folder in outputs/social/weekly/ and the new cards on the kopi-video board.",
       expect="Two Telegram messages; a dated drafts folder with three posts and a gallery; new kopi-video cards waiting at your HUMAN gate."),
     S("Log it and stay in control (5 min)",
       "Automation you cannot see is automation you cannot trust. Record what each job does, then pause the video job after class so it does not spend model credits while nobody is watching.",
       where="Hermes Desktop — Mia",
       prompt="Write outputs/automation/cron-log.md: one row per scheduled job with name, schedule, what the test run produced, model time used, and what still needs my approval. Then list my scheduled jobs with their next run time.",
       expect="cron-log.md with three rows (morning brief, social drafts, video draft); you paused 'Weekly video draft' in Scheduled jobs.",
       decide="Which jobs keep running after class, and which do you pause?"),
    ]
    L["verify"] = ["Scheduled jobs lists 'Weekly social drafts' (Mon 9:00) and 'Weekly video draft' (Fri 10:00)",
                   "Trigger now produced dated drafts, a gallery and new kopi-video cards", "Telegram received both notifications",
                   "Nothing was posted or rendered without your approval", "cron-log.md records every job; the video job is paused after class"]
    L["trouble"] = [("Job never runs", "Hermes Desktop must be open and the laptop awake at that time. Use Trigger now to test."),
                    ("No Telegram message", "Send /sethome in your Telegram chat with Mia, then Trigger now again."),
                    ("Wrong time", "Ask Mia to set the job's timezone to Asia/Singapore, or edit the frequency in Scheduled jobs."),
                    ("The job did more than asked", "Pause it, then tell Mia exactly what to remove from its prompt. Approval steps never move into a cron.")]
    L["challenge"] = "Use the Competitor news watch blueprint for Kopi Kaki's six competitors. What should the job do when it finds a price cut: alert you, or draft a response for your approval?"

# ---------------------------------------------------------------- Bonus · Paperclip one-person company
def bonus(L, raw):
    L["prereq"] = ["Hermes Desktop with Mia working (Topic 2) — Mia installs and starts Paperclip for you",
                   "Node.js 24.11+ on the laptop (Mia checks; the trainer installs it if missing)", f"This lab's data/ dragged into {WSF}"]
    L["steps"] = [
     S("What Paperclip is (5 min)",
       "Paperclip (open source, github.com/paperclipai/paperclip) runs a company of AI agents: an org chart, job titles, reporting lines, budgets, tasks and an approval inbox. You are the Board. "
       "Hermes Kanban organised tasks for your team; Paperclip organises the people — who reports to whom, who may hire, and what each agent may spend. Watch the overview first: https://www.youtube.com/watch?v=WNYe5mD4fY8"),
     S("Ask Mia to install and start Paperclip (10 min)", "No terminal for you: Mia runs the installer and keeps it running.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Install Paperclip for me with its one-line onboarder (npx paperclipai onboard --yes) and keep it running. Check first that Node.js is 24.11 or newer; if not, stop and tell me what the trainer must install. When it is up, give me the link to open.",
       expect="Mia reports 'Server running at http://localhost:3100' — open it in your browser."),
     S("Set up the company: Kopi Kaki Co. (5 min)",
       "In the onboarding wizard name the organization Kopi Kaki Co. Create the first agent and name her Ava. Connect a model. Then open Company settings: put the mission in the description and set the monthly budget to USD 60. "
       "Leave the onboarding task waiting — hiring rules come first.",
       expect="Kopi Kaki Co. exists with a USD 60/month budget."),
     S("Make Ava the CEO and write her instructions (8 min)",
       "Paperclip's screen has no Role field, so ask Mia to set it. Then paste the CEO instructions below into Agents → Ava → Instructions → AGENTS.md, upload brand-guide.md, campaign-brief.md and compliance-rules.md with + (Add agent file), "
       "and switch ON Settings → General → Hiring → 'Require board approval for new hires'.",
       where="Paperclip → Agents → Ava → Instructions → AGENTS.md (after asking Mia: 'In Paperclip, set Ava's role to CEO and her title to CEO for me.')",
       prompt="You are Ava, CEO of Kopi Kaki Co., a Singapore kopi startup run as a one-person company: the founder is the Board and the only human.\n"
              "Mission: launch the Gula Melaka Cold Brew on 1 Dec 2026 - 2,500 app pre-orders, one approved short video every week, AI spend under USD 60/month, zero compliance breaches.\n"
              "How you work:\n- You do not do the marketing work yourself. You hire and manage.\n- Your first hire is a Chief of Staff who runs the marketing team for you.\n"
              "- Every hire needs a mandate, a reporting line and a monthly budget, and waits for Board approval.\n"
              "- Every public item passes an independent reviewer and then the Board. Never publish anything yourself.\n"
              "- Source of truth: brand-guide.md, campaign-brief.md, compliance-rules.md.\n- Report weekly to the Board: progress, spend vs budget, risks, decisions needed.",
       expect="Ava's role is CEO, her instructions show the mandate and three files, and the hiring gate is ON."),
     S("CEO task: hire a Chief of Staff (5 min)", "Give Ava her first task. She proposes the hire; it lands in your approval inbox.",
       where="Paperclip → New Task (assign to Ava)",
       prompt="Hire a Chief of Staff for Kopi Kaki Co.\nMandate (3 bullets): turn my goals into weekly plans, hire and manage the marketing team, report progress and risks to you every Friday.\n"
              "Reports to: you (CEO). Monthly budget: USD 10. Use the same adapter as you.\nSubmit the hire for Board approval and tell me when it is waiting.",
       expect="A 'Hire Agent' card in Pending Approvals."),
     S("Approve the hire from the Board seat (3 min)",
       "Dashboard → Pending Approvals → View details → See full request. Check mandate, budget and reporting line, then click Approve.",
       expect="The Chief of Staff is active and reports to Ava.", decide="Does the mandate and budget make sense for a startup?"),
     S("Chief of Staff task: hire the marketing team (8 min)",
       "Now the Chief of Staff staffs the same team you built in Activities 4 and 5. In Pending Approvals approve the hires that fit; send one back with Request revision.",
       where="Paperclip → New Task (assign to the Chief of Staff)",
       prompt="Hire the Kopi Kaki marketing team. All report to you.\n- Market Researcher (finds facts with sources)\n- Social Copywriter (LinkedIn, Facebook and Instagram posts)\n- Image Creator\n- Video Producer (HyperFrames)\n- Voice-over Artist\n- Content Reviewer (independent: checks posts and videos against compliance-rules.md and video-qa-checklist.md; can block release)\n"
              "Give each a 3-bullet mandate and a monthly budget. The whole company must stay under USD 60/month including Ava and you. Submit every hire for Board approval.",
       expect="Six hire requests; after your decisions the team is active.", decide="Approve, revise or reject each hire."),
     S("Show the organization chart (3 min)",
       "Open Agents → Org chart view (icon next to New Agent). Expected: Board (you) → Ava (CEO) → Chief of Staff → six marketing agents. Take a screenshot: this is your one-person company."),
     S("Get the team to produce the launch video (10 min)",
       "Give the Chief of Staff the same brief as Activity 5 so you can compare like with like. Watch the tasks the Chief of Staff creates and assigns.",
       where="Paperclip → New Task (assign to the Chief of Staff)",
       prompt="Produce the Gula Melaka Cold Brew launch video: 20 seconds, 1080x1920, 4 scenes, narration, facts only from campaign-brief.md and product-catalogue.csv, SGD 6.80, launch 1 Dec 2026, no health or halal claims.\n"
              "Split it into tasks for the team, with the Content Reviewer checking the final file against video-qa-checklist.md. Ask me to approve the script before rendering and the exact final file before anything is used. Never publish.",
       expect="Sub-tasks assigned across the team, a script approval request, then a final-file approval request."),
     S("Compare Paperclip with the Hermes Kanban team (8 min)", "Write down what each approach gave you.",
       where="Paperclip → New Task (assign to Ava)",
       prompt="Write comparison.md for the Board: Paperclip company vs the Hermes Kanban team from Activity 5 for the same launch video.\n"
              "Rows: set-up time, who decides the task breakdown, approvals and hiring control, budget control, visibility (org chart, audit), output quality, my review effort, cost.\n"
              "End with a recommendation: when should a one-person company use a Kanban team, and when a Paperclip company?",
       expect="A table and a clear recommendation."),
    ]
    L["verify"] = ["http://localhost:3100 shows Kopi Kaki Co.; the hiring gate is ON", "Ava is CEO with written instructions",
                   "Chief of Staff and six marketing agents hired through Board approvals", "Org chart: Board → CEO → Chief of Staff → team",
                   "The video task ran with script and final-file approvals; comparison.md written"]
    L["trouble"] = [("Node.js too old", "Ask the trainer to install Node.js 24.11+ (nodejs.org), then ask Mia to try again."),
                    ("Port 3100 busy", "Paperclip picks another port — ask Mia for the link it printed."),
                    ("Run test fails", "The agent's model is not signed in: connect a model in the agent's Harness / Runtime page."),
                    ("Hires joined without approval", "The hiring gate was OFF — Settings → General → Hiring. Pause the agent and re-hire.")]
    L["challenge"] = "Add a weekly routine (Routines → Create) that asks the Chief of Staff for one new video every Monday at 10:00, still behind your approval. What would you need to trust it to run unattended?"


def fill(labs, raw):
    import labs_v34_t2
    by = {L["code"]: L for L in labs}
    labs_v34_t2.setup(by["S2"], raw); labs_v34_t2.act2(by["02"]); labs_v34_t2.act3(by["03"])
    act4(by["04"]); act5(by["05"]); act6(by["06"]); bonus(by["B"], raw)
