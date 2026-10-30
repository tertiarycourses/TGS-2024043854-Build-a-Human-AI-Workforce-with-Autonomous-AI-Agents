"""Detailed steps, copy-ready prompts and commands for the v3.4 labs (one Kopi Kaki startup story).
Every step has a body; most have a `cmd` (terminal) and/or a `prompt` (paste into the named place).
Vendor facts were checked against official docs on 31 Oct 2026 (labs_v34.SOURCES)."""
from labs_v22 import step

def S(title, body="", cmd=None, prompt=None, where=None, expect=None, decide=None):
    d = step(title, body=body, expect=expect) if expect else step(title, body=body)
    if cmd: d["cmd"] = cmd
    if prompt: d["prompt"] = prompt
    if where: d["where"] = where
    if decide: d["decide"] = decide
    return d

# ---------------------------------------------------------------- Activity 4 · social media marketing team
def act4(L):
    L["prereq"] = ["Topic 2 setup done: Hermes Desktop, a working model and Telegram (the gateway must be running for Kanban to dispatch work)",
                   "Activity 2 website and Activity 3 deck saved — the team reuses their facts",
                   "This lab's data/ copied into ~/kopi-kaki (souls/, tasks/ and tools/make_post_image.py are included)"]
    L["steps"] = [
     S("Copy the lab data and create the output folders (3 min)",
       "Open a terminal in this lab folder. The data/ folder holds the five team role files (souls/), the task briefs (tasks/), the brand files and a small image tool. Copy it into your company workspace without overwriting your own AGENTS.md.",
       cmd="cp -Rn data/* ~/kopi-kaki/\nmkdir -p ~/kopi-kaki/outputs/social/images\ncd ~/kopi-kaki && ls souls tasks tools",
       expect="souls/ lists researcher, linkedin-writer, facebook-writer, instagram-writer and image-creator."),
     S("Staff the team: five profiles, one job each (8 min)",
       "A profile is a separate Hermes agent with its own SOUL.md, memory, skills and settings. --clone copies your working model and keys from the default profile, so every specialist can think straight away. The description is how the board routes work to the right specialist.",
       cmd='hermes profile create researcher --clone --description "Finds launch angles, audience insights and facts for Kopi Kaki posts; cites the source file for every fact"\n'
           'hermes profile create linkedin-writer --clone --description "Writes the founder\'s LinkedIn post: story, proof, call to action; professional Singapore English"\n'
           'hermes profile create facebook-writer --clone --description "Writes the neighbourhood Facebook post: pop-up dates, launch day, friendly kopitiam voice"\n'
           'hermes profile create instagram-writer --clone --description "Writes the Instagram caption, first-line hook and hashtags for a 1080x1350 image post"\n'
           'hermes profile create image-creator --clone --description "Creates one on-brand 1080x1350 image per post with tools/make_post_image.py and builds the review gallery"\n'
           'for p in researcher linkedin-writer facebook-writer instagram-writer image-creator; do cp ~/kopi-kaki/souls/$p.SOUL.md ~/.hermes/profiles/$p/SOUL.md; done\n'
           'hermes profile list',
       expect="hermes profile list shows the five new profiles next to default."),
     S("Meet your team as bots (5 min)",
       "Hermes Desktop's Bot Mode (the Bots tab, on by default) shows every profile as a named bot you can chat with directly. Say hello to two of them and check that each answers in its own role. Optional: give a profile its own Telegram bot token, then run `<profile> gateway install` and `<profile> gateway start`. A bot is how you talk to a profile; the work itself is tracked on the Kanban board.",
       where="Hermes Desktop → Bots tab → researcher",
       prompt="Hi, I'm the founder of Kopi Kaki Co. In two sentences: what is your job on my marketing team, and which files in ~/kopi-kaki will you read first?",
       expect="Each bot describes its own role and names AGENTS.md, campaign-brief.md and brand-guide.md."),
     S("Build the Kanban board with a human gate (10 min)",
       "Ask your default agent (Mia) to build the board. Research runs first; the three writers run in parallel as soon as research is done; the image creator waits for all three; the last card is yours. Nothing is posted anywhere — the output is a review gallery.",
       where="Hermes Desktop → default profile (Mia), started in ~/kopi-kaki",
       prompt="Use the Kanban tools to build the board for tenant kopi-social, workspace ~/kopi-kaki.\n"
              "1. Research launch angles - assignee researcher - body from tasks/s1-research.md.\n"
              "2. LinkedIn post - assignee linkedin-writer - parent: card 1 - body from tasks/s2-linkedin.md.\n"
              "3. Facebook post - assignee facebook-writer - parent: card 1 - body from tasks/s3-facebook.md.\n"
              "4. Instagram post - assignee instagram-writer - parent: card 1 - body from tasks/s4-instagram.md.\n"
              "5. Images and review gallery - assignee image-creator - parents: cards 2, 3 and 4 - body from tasks/s5-images.md.\n"
              "6. HUMAN: approve the posts - unassigned, parent: card 5. Only I complete this card.\n"
              "Show me the card IDs, assignees and parents as a table. Do not start anything outside this board and never post to a real account.",
       expect="A table of six cards; cards 2–4 depend on 1, card 5 on 2–4, card 6 on 5 and has no assignee."),
     S("Watch the team work (12 min)",
       "Kanban dispatches each card to its profile as soon as its parents are done. Watch in the terminal or in the dashboard's Kanban view. Open a card to read its run history and output path.",
       cmd="hermes kanban watch --tenant kopi-social\n# or the web view:\nhermes dashboard          # then open Kanban",
       expect="Research finishes first, the three writers run side by side, then the image creator starts."),
     S("Open the posts gallery (5 min)",
       "The image creator builds one page that shows every post the way it would look on its platform: LinkedIn text post, Facebook post with image, Instagram square with caption. Open it in your browser.",
       cmd="open ~/kopi-kaki/outputs/social/gallery.html      # Windows: start  ·  Linux: xdg-open",
       expect="Three platform cards, each with its image, copy and hashtags."),
     S("Review like the founder: APPROVE, EDIT or REJECT (10 min)",
       "Check every post against brand-guide.md and compliance-rules.md: price SGD 6.80, launch 1 Dec 2026, SHIOK20 terms if the code appears, no health or halal claims, no competitor bashing. Send one post back with a concrete edit — the writer reworks it and the gallery updates.",
       where="Hermes Desktop → default profile (Mia)",
       prompt="My decisions for the kopi-social posts:\n- LinkedIn: APPROVE\n- Facebook: EDIT - put the first pop-up date in the first line and cut the post to 80 words\n- Instagram: APPROVE\n"
              "Create a rework card for the facebook-writer with my edit as its body and the image creator's card as parent, then a card for the image-creator to refresh the gallery. "
              "Record every decision with date and reason in outputs/social/approval-log.md. Leave my HUMAN card open: I complete it myself.",
       cmd="hermes kanban list --tenant kopi-social\nhermes kanban complete <human_card_id>     # after you have checked the refreshed gallery",
       expect="A rework card runs; gallery.html shows the edited Facebook post; approval-log.md has three rows.",
       decide="Which posts are ready, which need a concrete change; nothing is published."),
     S("Reflect: team versus one agent (5 min)",
       "Compare the team with Mia working alone on Day 1.",
       where="Hermes Desktop → default profile (Mia)",
       prompt="Compare today's five-profile team with you working alone: time to first draft, how different the three posts sound, number of my edits, and coordination overhead. Give me a 5-row table and one recommendation: when should Kopi Kaki use a team, and when one agent?",
       expect="A short evidence-based comparison you can discuss in class."),
    ]
    L["verify"] = ["`hermes profile list` shows the five team profiles", "The board shows parents: writers ← research; images ← all three writers; HUMAN ← images",
                   "gallery.html shows three platform posts with images", "approval-log.md records a decision for every post; nothing was posted publicly"]
    L["trouble"] = [("Cards stay in Ready and never run", "The gateway dispatches Kanban work: run `hermes gateway status` and start it (`hermes gateway run`)."),
                    ("A profile cannot reach the model", "Recreate it with --clone or run `hermes -p <profile> model` to pick the provider."),
                    ("Image tool fails", "Install Pillow in the workspace venv: `.office-venv/bin/python -m pip install Pillow`."),
                    ("A writer invents a price or promo", "Point it at product-catalogue.csv and campaign-brief.md in a rework card; add the rule to its SOUL.md.")]
    L["challenge"] = "Add a sixth profile, tiktok-writer, as a card that depends on research. What did the extra specialist cost in time and review effort, and was it worth it?"

# ---------------------------------------------------------------- Activity 5 · video production team (PP Task 3)
def act5(L):
    L["prereq"] = ["Activity 4 done: profiles, Kanban and the running gateway work", "Node.js 22+ and FFmpeg for HyperFrames; Python 3.10+ for the local voice (Kokoro)",
                   "This lab's data/ copied into ~/kopi-kaki (souls/, tasks/, DESIGN.md and video-qa-checklist.md are included)"]
    L["steps"] = [
     S("Copy the lab data (2 min)", "Copy the video team's role files, task briefs, design rules and QA checklist into your workspace.",
       cmd="cp -Rn data/* ~/kopi-kaki/\nmkdir -p ~/kopi-kaki/outputs/video\nls ~/kopi-kaki/souls ~/kopi-kaki/tasks",
       expect="souls/ now also lists scriptwriter, video-producer, voice-over and video-reviewer."),
     S("Install the video skills and tools: HyperFrames, Remotion, Manim (10 min)",
       "HyperFrames (HeyGen) writes videos as HTML and renders them to MP4 — the team's main renderer (Node.js 22+ and FFmpeg). Remotion (React) and Manim (Python maths animation; Hermes ships a manim-video skill, Manim itself needs Python 3.10+ and LaTeX) are alternatives worth knowing. Read each SKILL.md before you trust it.",
       cmd="hermes skills install official/creative/hyperframes\nnpx hyperframes doctor\nnpx skills add remotion-dev/skills -a hermes-agent -g\nhermes skills list | grep -i -E 'hyperframes|remotion|manim'\n# optional, for Manim: python3 -m pip install manim && manim --version",
       expect="hyperframes doctor reports Node, FFmpeg and a browser OK; the skills appear in hermes skills list."),
     S("Give the team a voice: local text-to-speech (5 min)",
       "HyperFrames can narrate locally with the free Kokoro voice model — no account and no cost. Test it once.",
       cmd='python3 -m pip install kokoro-onnx soundfile\nnpx hyperframes tts "Gula Melaka Cold Brew. A taste of the kopitiam, slow-brewed cold." --voice af_heart --output ~/kopi-kaki/outputs/video/voice-test.wav',
       expect="voice-test.wav plays a clear English voice."),
     S("Staff the production line: five profiles (6 min)",
       "One researcher grounds every fact; the reviewer is independent of the producer. Each SOUL.md says what the role owns and what it must never do.",
       cmd='hermes profile create scriptwriter --clone --description "Turns research.md into a 20-second, 4-scene script with on-screen text and narration"\n'
           'hermes profile create video-producer --clone --description "Renders the approved script into a 1080x1920 MP4 with HyperFrames; owns outputs/video/final.mp4"\n'
           'hermes profile create voice-over --clone --description "Writes narration.txt from the approved script and records narration.wav with hyperframes tts"\n'
           'hermes profile create video-reviewer --clone --description "Independently checks the video against video-qa-checklist.md and the sources; sends the founder a review link"\n'
           'for p in scriptwriter video-producer voice-over video-reviewer; do cp ~/kopi-kaki/souls/$p.SOUL.md ~/.hermes/profiles/$p/SOUL.md; done\n'
           'cp ~/kopi-kaki/souls/video-researcher.SOUL.md ~/.hermes/profiles/researcher/SOUL.md\nhermes profile list',
       expect="researcher (now the video researcher), scriptwriter, video-producer, voice-over and video-reviewer are listed."),
     S("Build the production board with two human gates (8 min)",
       "Two cards are yours: approve the script before anything is rendered, and approve the exact final file. The producer and voice-over both depend on your script approval; the reviewer waits for both.",
       where="Hermes Desktop → default profile (Mia), started in ~/kopi-kaki",
       prompt="Use the Kanban tools to build the board for tenant kopi-video, workspace ~/kopi-kaki.\n"
              "1. Research the launch video - assignee researcher - body from tasks/v1-research.md.\n"
              "2. Write the 20-second script - assignee scriptwriter - parent: 1 - body from tasks/v2-script.md.\n"
              "3. HUMAN: approve the script - unassigned - parent: 2. Only I complete it.\n"
              "4. Record the voice-over - assignee voice-over - parent: 3 - body from tasks/v3-voice.md.\n"
              "5. Render the video - assignee video-producer - parents: 3 and 4 - skill hyperframes - body from tasks/v4-produce.md.\n"
              "6. Review and send me the link - assignee video-reviewer - parent: 5 - body from tasks/v5-review.md.\n"
              "7. HUMAN: approve the exact video - unassigned - parent: 6. Only I complete it.\n"
              "Show the card IDs, assignees and parents as a table. Never publish or post the video anywhere.",
       expect="A seven-card table with two unassigned HUMAN cards."),
     S("Research with source checks (8 min)",
       "The researcher may only use facts it can point to in a source file: this is grounding, the same idea as retrieval-augmented generation (RAG). Open research.md when the card is done and check two claims yourself.",
       cmd="hermes kanban watch --tenant kopi-video\ncat ~/kopi-kaki/outputs/video/research.md",
       expect="Every claim in research.md names its source file and line (e.g. campaign-brief.md); unsupported ideas are marked UNVERIFIED."),
     S("Approve the script — your first gate (5 min)",
       "Read script.md: four scenes, 20 seconds, on-screen text of seven words or fewer per scene, price SGD 6.80, launch 1 Dec 2026, no health or halal claims. Approve it, or ask for one change first.",
       where="Hermes Desktop → default profile (Mia)",
       cmd="hermes kanban list --tenant kopi-video          # find the 'HUMAN: approve the script' card id\nhermes kanban complete <card_id>",
       prompt="I have read outputs/video/script.md and APPROVE it as written. Note my approval with today's date in outputs/video/approvals.md. I have completed the HUMAN script card myself.",
       expect="The voice-over and render cards start.", decide="Is every word on screen true, on-brand and allowed?"),
     S("Production and voice-over (20 min)",
       "The voice-over profile records narration.wav; the producer builds the HyperFrames composition, adds the narration and renders. Check the real file, not the success message.",
       cmd="ls -la ~/kopi-kaki/outputs/video/\nffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json ~/kopi-kaki/outputs/video/final.mp4",
       expect="final.mp4 exists, 1080×1920, about 20 seconds, with an audio stream."),
     S("Independent review and the review link (10 min)",
       "The reviewer checks every scene against video-qa-checklist.md (V1–V9) and the sources, writes review.md, computes the file's SHA-256 and sends you a link on Telegram. The link serves the file from your laptop only.",
       cmd="cd ~/kopi-kaki/outputs/video && python3 -m http.server 8765\n# review link: http://localhost:8765/final.mp4\nshasum -a 256 final.mp4      # Windows: certutil -hashfile final.mp4 SHA256",
       expect="A Telegram message with the review link, PASS/FAIL per check and the SHA-256."),
     S("Approve the exact video — your final gate (10 min)",
       "Watch the whole video from the link. If anything is wrong, request one revision: the producer re-renders, the reviewer re-checks, and the new file gets a new hash — your old approval does not carry over.",
       where="Hermes Desktop → default profile (Mia)",
       prompt="I watched http://localhost:8765/final.mp4 to the end. Check that its SHA-256 matches review.md. If it matches, record 'APPROVE <sha256>' with today's date in outputs/video/approvals.md. Do not post or publish the video anywhere.",
       cmd="shasum -a 256 ~/kopi-kaki/outputs/video/final.mp4\nhermes kanban complete <human_video_card_id>      # only after the hashes match",
       expect="approvals.md shows APPROVE with the same hash as review.md.", decide="Accept this exact file, or request one revision."),
     S("Capture your PP Task 3 evidence (5 min)",
       "Take TWO readable screenshots of your own work: (A) the Kanban board (dashboard Kanban view) showing the profile/bot names, a dependency or HUMAN gate and the video task; (B) final.mp4 playing in a media player. Hide keys and private data. Keep final.mp4, research.md, review.md and approvals.md."),
     S("Reflect: what did the team buy you? (5 min)", "Compare effort, cost and quality.",
       where="Hermes Desktop → default profile (Mia)",
       prompt="Summarise the kopi-video run: total time, number of runs per card, what the reviewer caught, my revisions and an estimated model cost. Compare with an agency quote of SGD 3,000 and two weeks. What would you change in one SOUL.md to cut my review time next week?",
       expect="An honest summary including what failed."),
    ]
    L["verify"] = ["Video skills installed and `npx hyperframes doctor` passes", "research.md links every claim to a source file",
                   "final.mp4 is 1080×1920, ~20 s, with narration", "review.md passes V1–V9 with evidence; approvals.md hash = file hash",
                   "PP Task 3: two screenshots — Kanban board and the video playing"]
    L["trouble"] = [("`hyperframes doctor` fails on FFmpeg", "Install FFmpeg (macOS `brew install ffmpeg`, Windows `winget install ffmpeg`) and reopen the terminal."),
                    ("Render card runs before script approval", "The render card was created without the HUMAN card as parent — block it, fix the parent, re-run."),
                    ("No audio in final.mp4", "Check narration.wav exists and the composition references it; ask the producer to re-render."),
                    ("Review link does not open", "Keep the http.server terminal open; open the link on the same laptop.")]
    L["challenge"] = "Ask the producer for a 9:16 and a 1:1 cut from the same composition. How much extra review does a second format cost you?"

# ---------------------------------------------------------------- Bonus · Paperclip one-person company
def bonus(L, raw):
    pc = {st["title"]: st for st in raw[5]["steps"] + raw[6]["steps"]}
    L["prereq"] = ["Node.js 24.11+ (or Docker Desktop)", "One agent CLI signed in on this laptop — Claude Code, Codex, Gemini CLI or the Hermes Agent from Topic 2",
                   "This lab's data/ copied into ~/kopi-kaki"]
    L["steps"] = [
     S("What Paperclip is (5 min)",
       "Paperclip (open source, github.com/paperclipai/paperclip) runs a company of AI agents: an org chart, job titles, reporting lines, budgets, tasks and an approval inbox. You are the Board. Hermes Kanban organised tasks for your team; Paperclip organises the people — who reports to whom, who may hire, and what each agent may spend. Watch the overview first.",
       cmd="# Overview video: https://www.youtube.com/watch?v=WNYe5mD4fY8\nnode --version          # v24.11.0 or higher\nhermes --version        # or: claude --version / codex --version",
       expect="Node ≥ 24.11 and at least one signed-in agent CLI."),
     S("Install and start Paperclip (10 min)", pc["Install and start Paperclip"]["body"], cmd=pc["Install and start Paperclip"]["cmd"],
       expect="'Server running at http://localhost:3100' — open it in your browser."),
     S("Set up the company: Kopi Kaki Co. (5 min)",
       "In the onboarding wizard name the organization Kopi Kaki Co. Create the first agent and name her Ava. Connect a model (the same CLI you checked). Then set the mission in the organization description and a training budget cap. Leave the onboarding task waiting — hiring rules come first.",
       cmd="npx paperclipai company list                 # copy the company id\nnpx paperclipai budget company:update -C <company-id> --payload-json '{\"budgetMonthlyCents\":6000}'",
       expect="Kopi Kaki Co. exists with a USD 60/month cap under Audit → Budgets."),
     S("Set up the CEO and write her instructions (8 min)",
       "Make Ava the CEO with the CLI, then replace the starter text in Agents → Ava → Instructions → AGENTS.md with the CEO instructions below. Upload brand-guide.md, campaign-brief.md and compliance-rules.md with + (Add agent file). Finally switch ON Settings → General → Hiring → 'Require board approval for new hires'.",
       where="Paperclip → Agents → Ava → Instructions → AGENTS.md",
       cmd="npx paperclipai agent list -C <company-id>    # copy Ava's agent id\nnpx paperclipai agent update <ava-id> --payload-json '{\"role\":\"ceo\",\"title\":\"CEO\"}'",
       prompt="You are Ava, CEO of Kopi Kaki Co., a Singapore kopi startup run as a one-person company: the founder is the Board and the only human.\n"
              "Mission: launch the Gula Melaka Cold Brew on 1 Dec 2026 - 2,500 app pre-orders, one approved short video every week, AI spend under USD 60/month, zero compliance breaches.\n"
              "How you work:\n- You do not do the marketing work yourself. You hire and manage.\n- Your first hire is a Chief of Staff who runs the marketing team for you.\n"
              "- Every hire needs a mandate, a reporting line and a monthly budget, and waits for Board approval.\n"
              "- Every public item passes an independent reviewer and then the Board. Never publish anything yourself.\n"
              "- Source of truth: brand-guide.md, campaign-brief.md, compliance-rules.md.\n- Report weekly to the Board: progress, spend vs budget, risks, decisions needed.",
       expect="Ava's role is CEO, her instructions show the mandate and three files, and the hiring gate is ON."),
     S("CEO task: hire a Chief of Staff (5 min)",
       "Give Ava her first task. She proposes the hire; it lands in your approval inbox.",
       where="Paperclip → New Task (assign to Ava)",
       prompt="Hire a Chief of Staff for Kopi Kaki Co.\nMandate (3 bullets): turn my goals into weekly plans, hire and manage the marketing team, report progress and risks to you every Friday.\n"
              "Reports to: you (CEO). Monthly budget: USD 10. Use the same adapter as you.\nSubmit the hire for Board approval and tell me when it is waiting.",
       expect="A 'Hire Agent' card in Pending Approvals."),
     S("Approve the hire from the Board seat (3 min)",
       "Dashboard → Pending Approvals → View details → See full request. Check mandate, budget and reporting line, then approve. CLI alternative:",
       cmd="npx paperclipai approval list -C <company-id> --status pending\nnpx paperclipai approval approve <approval-id> --decision-note \"Approved: Chief of Staff, USD 10/month\"",
       expect="The Chief of Staff is active and reports to Ava.", decide="Does the mandate and budget make sense for a startup?"),
     S("Chief of Staff task: hire the marketing team (8 min)",
       "Now the Chief of Staff staffs the same team you built by hand in Activities 4 and 5. Approve the hires that fit; send one back with Request revision.",
       where="Paperclip → New Task (assign to the Chief of Staff)",
       prompt="Hire the Kopi Kaki marketing team. All report to you.\n- Market Researcher (finds facts with sources)\n- Social Copywriter (LinkedIn, Facebook and Instagram posts)\n- Image Creator\n- Video Producer (HyperFrames)\n- Voice-over Artist\n- Content Reviewer (independent: checks posts and videos against compliance-rules.md and video-qa-checklist.md; can block release)\n"
              "Give each a 3-bullet mandate and a monthly budget. The whole company must stay under USD 60/month including Ava and you. Submit every hire for Board approval.",
       cmd="npx paperclipai approval list -C <company-id> --status pending\nnpx paperclipai approval approve <approval-id> --decision-note \"Approved\"\nnpx paperclipai approval request-revision <approval-id> --decision-note \"Cap the Video Producer at USD 8/month\"",
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
    L["trouble"] = list(raw[5]["trouble"]) + [("Hires joined without approval", "The hiring gate was OFF — Settings → General → Hiring. Pause the agent and re-hire.")]
    L["challenge"] = "Add a weekly routine (Routines → Create) that asks the Chief of Staff for one new video every Monday at 10:00, still behind your approval. What would you need to trust it to run unattended?"


def fill(labs, raw):
    import labs_v34_t2
    by = {L["code"]: L for L in labs}
    labs_v34_t2.setup(by["S2"], raw); labs_v34_t2.act2(by["02"]); labs_v34_t2.act3(by["03"])
    act4(by["04"]); act5(by["05"]); bonus(by["B"], raw)
