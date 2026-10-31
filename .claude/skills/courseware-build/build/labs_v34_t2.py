"""Topic 2 guided setup + Activities 2 and 3 (v3.5: Hermes Desktop only — no command lines for learners).
Every step is a click in Hermes Desktop or a prompt Mia carries out. Desktop screens match the trainer's
screenshots of Hermes Desktop v0.22.5 (31 Oct 2026); Nous Portal tiers and Bot Mode checked against
portal.nousresearch.com and the Hermes docs on 31 Oct 2026."""
from labs_v34_steps import S

MINIMAX_MODEL = "MiniMax-M3.1-Flash"   # kept for reference; v3.5 no longer demos MiniMax
WSF = "Desktop/kopi-kaki"              # the learner's company folder (a normal folder on the Desktop)
SOURCES = [
 ("Hermes Desktop", "https://hermes-agent.nousresearch.com/desktop"),
 ("Hermes docs — desktop, providers, messaging, tools, skills, cron, web search", "https://hermes-agent.nousresearch.com/docs/"),
 ("Nous Portal — Free tier (free models only, $0) and paid plans", "https://portal.nousresearch.com/"),
 ("Nous Portal — use your ChatGPT plan for inference", "https://portal.nousresearch.com/help/chatgpt-plan-sharing"),
 ("Hermes Bot Mode — bots, group chats, routines", "https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode"),
 ("Hermes connectors (managed apps such as Gmail, via a Nous sign-in)", "https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-search#connectors-remote-tools"),
 ("Firecrawl pricing (free 1,000 credits/month)", "https://www.firecrawl.dev/pricing"),
 ("skills.sh — the open agent-skills directory", "https://skills.sh/"),
 ("HyperFrames", "https://github.com/heygen-com/hyperframes"), ("Remotion agent skills", "https://github.com/remotion-dev/skills"),
 ("Manim Community", "https://www.manim.community/"), ("Paperclip", "https://github.com/paperclipai/paperclip"),
]

COPY_DATA = ("In Finder (Mac) or File Explorer (Windows), open this lab's data folder from the unzipped course files, select everything, "
             f"and drag it into your {WSF} folder. If asked about files that already exist, choose Skip (do not replace). "
             f"Then in Hermes Desktop click + (left of Ask anything) → Folder… and choose {WSF}: Mia now has this lab's files and AGENTS.md. "
             "Start the session with: 'Read AGENTS.md in the attached folder and follow it for this session.'")

def setup(L, raw):
    L["prereq"] = ["Laptop: macOS 12+ on Apple Silicon (Intel Macs are not supported by the Desktop installer) or Windows 10/11",
                   "A model: your ChatGPT Plus plan (sign up for it as your free AI subscription), or a free Nous Portal account (Upstage Solar Mini 4 is free)",
                   "A Telegram account on your phone", "The trainer-assigned training Google account (synthetic Kopi Kaki mail)",
                   "A free Firecrawl account (firecrawl.dev — 1,000 free credits a month, no card)"]
    L["steps"] = [
     S("Unzip the labs and create your Kopi Kaki folder (5 min)",
       "Download the course ZIP (the trainer shares the link), unzip it, and create a folder called kopi-kaki on your Desktop. "
       "Open labs/setup02-hermes-first-ai-employee/data, select everything and drag it into the new kopi-kaki folder. "
       "This folder is your company: AGENTS.md inside it tells every agent who Kopi Kaki is and the rules.",
       expect=f"{WSF} holds AGENTS.md, brand-guide.md, campaign-brief.md, the reviews and competitor files and skills/."),
     S("Install Hermes Desktop (10 min)",
       "Download the installer from hermes-agent.nousresearch.com/desktop: Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows), and run it like any app. "
       "On first run choose 'Choose provider later' (you pick the brain in the next step) and the Basic layout. "
       "Then open Settings → About → Version & updates: it should say you are running the latest version.",
       expect="Hermes Desktop opens; Version & updates shows 'You're running the latest version'."),
     S("Give Mia a brain: choose your model (10 min)",
       "The model is the agent's brain. Pick ONE route. "
       "This class (recommended): your ChatGPT Plus plan. Settings → Model → Main model → Provider: 'ChatGPT or Codex Subscription' → sign in with your ChatGPT account → pick the model → Apply. "
       "Free: click Sign in next to Nous in the status bar at the bottom of the window and create a free Nous Portal account, then Settings → Model → Provider: Nous Portal → Upstage Solar Mini 4 (FREE). "
       "Paid, if you want a stronger model later: Nous Portal Plus (USD 20 a month) or another provider's key in Settings → Providers.",
       where="Hermes Desktop — New session",
       prompt="Say hello in one line as Mia, Kopi Kaki's first AI employee, and tell me which model you are running on.",
       expect="A one-line reply that names the model."),
     S("Hand Mia the company rulebook and meet her (5 min)",
       f"Start a New session. In the chat box click + (left of Ask anything) → Folder… and choose {WSF}: that hands Mia the company files, including AGENTS.md, the company rulebook. "
       "Then send this prompt. Do the same in every new session: + → Folder… → kopi-kaki, then 'Read AGENTS.md in the attached folder and follow it for this session.' Tip: type @ to point at one file, e.g. @AGENTS.md.",
       where=f"Hermes Desktop — New session",
       prompt="You are Mia, the first AI employee of Kopi Kaki Co. Read AGENTS.md and campaign-brief.md in the attached folder and follow AGENTS.md for this session. In five bullets: who we are, what we launch and when, the price, our KPIs, and the three rules you must never break.",
       expect="Five correct bullets: startup, Gula Melaka Cold Brew on 1 Dec 2026, SGD 6.80, the KPIs and the rules."),
     S("Let Mia set up her own toolbox (3 min)",
       "Later labs need a few Python libraries (for slides, spreadsheets and images). You do not type any commands: Mia installs them for you and reports back.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Prepare this folder for the next labs: create a Python virtual environment called .office-venv here and install python-pptx, openpyxl and Pillow into it. Do not change anything outside this folder. Then tell me in two lines what you installed and whether it works.",
       expect="Mia confirms .office-venv exists with python-pptx, openpyxl and Pillow."),
     S("Put Mia on Telegram: the quick way (5 min)",
       "Left sidebar → Messaging → Telegram → Quick setup → Create with QR. Scan the code with the Telegram app on your phone, or open the link on this computer (it expires in 30 minutes), and confirm in Telegram. "
       "Hermes creates the bot and detects your Telegram user ID. Switch Telegram to Enabled and click Save changes.",
       expect="Telegram shows Connected and you are the only approved user. Send 'hi' to your bot — Mia replies. Then send /sethome in that chat so scheduled results arrive there."),
     S("Or the manual way: create the bot with BotFather (10 min)",
       "Use this if the QR code does not work, or to see what it does for you. "
       "Step 1 — talk to BotFather: open Telegram, search for BotFather (look for the blue verification tick), tap Start and send /newbot. "
       "Step 2 — name your bot: a display name (e.g. Mia · Kopi Kaki), then a unique username ending in bot or _bot (e.g. kopikaki_mia_bot); if it is taken, BotFather asks for another. "
       "Step 3 — get your API token: copy the token BotFather replies with and keep it safe; it is the password to your bot, so never paste it into a chat or a prompt. "
       "Step 4 — in Hermes Desktop, Messaging → Telegram: paste the token into Bot token, put your numeric user ID from @userinfobot under Allowed Telegram user IDs, then Enabled → Save changes.",
       expect="Telegram shows Connected with only you approved; your bot replies to 'hi'."),
     S("Talk to Mia with your voice (5 min)",
       "Settings → Voice. Speech to text: switch it on (Live Transcription shows your words as you speak). Text to speech: provider Edge (free, no key), pick a voice such as en-US-AriaNeural, and switch on Read Responses Aloud. "
       "Then use the microphone in the chat and ask Mia a question out loud. Wispr Flow from Activity 1C works here too.",
       expect="Mia hears your question and reads her answer aloud."),
     S("Check Mia's tools (5 min)",
       "Capabilities → Tools shows every toolset Mia can use: web, files, terminal, browser, images, voice, schedules and more. Switch on only what the job needs (Principle 2: permission control). "
       "Mia uses the terminal tool for you — that is how she installed the toolbox — so you never have to.",
       where="Hermes Desktop — Mia",
       prompt="List the toolsets you have switched on. Which ones do you need to read my email, search the web and make slides? Which would you switch off on Telegram, and why?",
       expect="A short list that matches Capabilities → Tools, with a reason for each."),
     S("Review, then install a skill (10 min)",
       "A skill is a SKILL.md folder of know-how Mia loads when a task matches it. Browse Capabilities → Skills (Discover Skills shows what is already installed). "
       "Then install the reviewed kopi-email-brief skill from your folder — by asking. Read every third-party skill before you install it.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Read skills/kopi-email-brief/SKILL.md in this folder. In three bullets, tell me what it makes you do and whether it runs any scripts. Then install it as one of your skills and confirm it is available.",
       expect="Mia reports 'Installed and verified' and kopi-email-brief appears in Capabilities → Skills."),
     S("Give Mia web search with Firecrawl (5 min)",
       "Firecrawl is Hermes's default web search. Create a free account at firecrawl.dev (1,000 credits a month, no card) and copy your API key. "
       "In Hermes Desktop open Settings → Tools & Keys, find Firecrawl, paste the key and save. Never paste keys into a chat.",
       where="Hermes Desktop — Mia",
       prompt="Search the web for 3 news items from the last 90 days about cold brew or kopi trends in Singapore. For each: headline, date, URL and one takeaway for Kopi Kaki's launch. Mark anything you could not verify. Save it to outputs/research/trends.md.",
       expect="Three dated items with URLs in outputs/research/trends.md."),
     S("Connect Gmail with a Google sign-in (10 min)",
       "No OAuth client and no command line: you sign in to Google the normal way. First make sure you are signed in to Nous (Sign in in the status bar; the free account is enough). "
       "Then Capabilities → Connectors → search 'Gmail' → Connect → choose the trainer-assigned training Google account → Allow. "
       "Add Google Calendar the same way if your Connectors list shows it. Connector access on the free Nous tier is awaiting verification: your trainer confirms it before class.",
       where="Hermes Desktop — Mia",
       prompt="Using the Gmail connector (read-only), list my unread Kopi Kaki emails from the last 7 days. Flag any supplier or landlord email that needs a reply today and anything that looks like phishing. Do not send, delete or change anything.",
       expect="A short brief with senders, subjects and flagged items. Nothing sent or changed."),
     S("Send ONE approved email (5 min)",
       "Sending is a separate permission. Mia drafts, you approve the exact text, then she sends once to the trainer-approved test address.",
       where="Hermes Desktop — Mia",
       prompt="Draft a reply to the supplier tasting email confirming Thursday 3 pm at the Tiong Bahru flagship. Show me the exact To, Subject and Body. Wait for my SEND. After I say SEND, send it once with the Gmail connector to the trainer-approved test address and confirm it is in Sent.",
       expect="One sent message — nothing sent before your SEND.", decide="Approve the exact recipient, subject and body."),
     S("Schedule the daily 8:00 email summary (10 min)",
       "A scheduled job (cron) makes Mia start work without being asked. Open Scheduled jobs and look at the Blueprints (Morning briefing, Important-mail monitor …). "
       "Then create your own by asking Mia. Finally open the job in Scheduled jobs and click Trigger now to test it — do not wait until tomorrow.",
       where="Hermes Desktop — Mia",
       prompt="Create a scheduled job called 'Morning email brief' that runs every day at 8:00 Asia/Singapore time and delivers to my Telegram. Job: use the kopi-email-brief skill and the Gmail connector to summarise my unread Kopi Kaki email from the last 24 hours: urgent first, then replies needed, then FYI. Read only — never send or change anything. Show me the job when it is saved.",
       expect="Scheduled jobs lists 'Morning email brief' (every day 8:00); Trigger now delivers a structured summary to Telegram."),
    ]
    L["verify"] = [f"Hermes Desktop works in {WSF} with a model you chose", "Mia replies on Telegram only to you, and reads answers aloud",
                   "Capabilities shows the expected tools and the kopi-email-brief skill",
                   "trends.md has three dated items with URLs", "Gmail is connected; one approved email sent",
                   "Scheduled jobs shows 'Morning email brief' at 08:00 and a successful Trigger now"]
    L["trouble"] = [("Mia does not reply / model error", "Settings → Model → Main model: check the provider, sign in again and click Apply. On the Nous free tier pick a free model."),
                    ("ChatGPT sign-in fails", "Use the account that has ChatGPT Plus; sign out and in again from Settings → Model. Use the free Nous route while you wait."),
                    ("Bot silent on Telegram", "Messaging → Telegram: is it Enabled and Connected? Did you click Save changes? Are you listed under Approved users?"),
                    ("Scheduled job never arrives", "Hermes Desktop must be running at that time. Send /sethome in your Telegram chat, then click Trigger now."),
                    ("Gmail not listed or Connect fails", "Sign in to Nous first (status bar). If Gmail still is not offered, tell your trainer — use the trainer's demo mailbox for this step."),
                    ("Web search returns nothing", "Settings → Tools & Keys: check the Firecrawl key is saved; Capabilities → Tools: is web on?")]
    L["challenge"] = "Add a second scheduled job at 18:00 that summarises the day's pre-orders and emails into three lines on Telegram. Which part of the job would you never let a cron do unattended?"

def act2(L):
    L["prereq"] = ["Topic 2 setup done: Mia works in your kopi-kaki folder", "This lab's data/ dragged into Desktop/kopi-kaki"]
    L["steps"] = [
     S("Copy the website brief into your company folder (2 min)", COPY_DATA + " The brief says who the site is for, the sections, the brand and the definition of done.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Read website-brief.md and tell me in three lines what you will build, for whom, and how we will know it is done.",
       expect="Three lines that match the brief."),
     S("Choose UX skills on skills.sh (5 min)",
       "Open skills.sh in your browser and search 'frontend' and 'design'. The most installed design skills include Anthropic's frontend-design (about 1.1 million installs), Vercel's web-design-guidelines and ui-ux-pro-max. "
       "Open each skill's page and read its SKILL.md: what will it make the agent do, and does it run any scripts?",
       expect="You can explain in one sentence what each skill changes."),
     S("Ask Mia to install two UX skills (5 min)",
       "No command line: Mia installs the skills for herself. Afterwards they appear in Capabilities → Skills.",
       where="Hermes Desktop — Mia",
       prompt="Install these two skills from skills.sh for yourself: frontend-design from github.com/anthropics/skills and web-design-guidelines from github.com/vercel-labs/agent-skills. Read each SKILL.md first and tell me whether it runs any scripts. Then confirm both are installed and available.",
       expect="Both skills installed and listed in Capabilities → Skills."),
     S("Brief Mia like a design agency (15 min)",
       "Start a New session in your kopi-kaki folder so the new skills load.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Use the frontend-design and web-design-guidelines skills. Build the Kopi Kaki Co. one-page website from website-brief.md.\n"
              "- Sections: hero (Gula Melaka Cold Brew, SGD 6.80, from 1 Dec 2026), our story (a startup founded in 2026), menu from product-catalogue.csv, pop-ups and the Tiong Bahru flagship, three short taster quotes from customer-reviews.csv (no names), app pre-order button, footer.\n"
              "- Brand: colours and voice from brand-guide.md; use assets/kopi-kaki-logo.png and assets/cold-brew-product-card.png.\n"
              "- One self-contained outputs/website/index.html: inline CSS, no external libraries or fonts, responsive down to 375 px, accessible contrast.\n"
              "- No health or halal claims. Every price and date must match the source files.\n"
              "When done, open the page in my browser, then list which skill rules you applied and every fact with its source file.",
       expect="outputs/website/index.html opens in your browser, plus a list of applied rules and sourced facts."),
     S("Check it like a customer (5 min)",
       "Look at the page Mia opened (or double-click outputs/website/index.html in your kopi-kaki folder). Narrow the browser window to phone width. Check the price, the date, the pop-up information and the button.",
       expect="The hero shows Gula Melaka Cold Brew, SGD 6.80 and 'Pouring from 1 Dec 2026'; the page still works at phone width."),
     S("Ask for one concrete revision (8 min)", "Give feedback an agent can test, not 'make it nicer'.",
       where="Hermes Desktop — Mia",
       prompt="Revise outputs/website/index.html: (1) move the pre-order button into the hero, visible without scrolling on a 375 px phone; (2) make the menu a two-column grid on desktop and one column on phone; (3) add the pop-up dates as a simple list. Then write outputs/website/review.md: what the skills changed, my requested fixes, and the checks you ran.",
       expect="Updated page and review.md.", decide="Is it on-brand, true and usable on a phone?"),
     S("Capture your website (2 min)", "Save two screenshots — desktop and phone width — into outputs/website/. You will reuse the site's facts in the pitch deck and the social posts."),
    ]
    L["verify"] = ["Two UX skills installed and listed in Capabilities → Skills", "index.html opens offline with the Kopi Kaki colours, logo and product card",
                   "Every price and date matches the source files", "Works at 375 px; review.md records your revision"]
    L["trouble"] = [("Skill install fails", "Ask Mia what failed and to try the Hermes skills hub instead; or search the skill in Capabilities → Skills and click Install."),
                    ("Skill not used", "Start a New session so newly installed skills load; name the skill in the prompt."),
                    ("Images missing", "Check assets/ was dragged into your kopi-kaki folder and ask Mia to use relative paths.")]
    L["challenge"] = "Ask Mia to install ui-ux-pro-max as a third skill and make a second design. Which design would you ship, and what did the extra skill actually change?"

def act3(L):
    L["prereq"] = ["Topic 2 setup and Activity 2 done (Mia's .office-venv toolbox exists)", "This lab's data/ dragged into Desktop/kopi-kaki",
                   "Optional: LibreOffice, so Mia can save a PDF copy of the deck"]
    L["steps"] = [
     S("Ask Mia to install the deck skill (3 min)",
       COPY_DATA + " The tool writes the file (python-pptx); the skill says how to build a good deck. You install the skill by asking — no command line.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="install the kopi pitch deck skill from skills/kopi-pitch-deck in this folder. Read its SKILL.md first and tell me in two lines what it makes you do. Then confirm it is available, and check that python-pptx works in .office-venv.",
       expect="'Installed and verified the kopi-pitch-deck skill … readiness status available' and python-pptx works."),
     S("Optional: compare with a hub PPT skill (3 min)", "Hermes's skills hub also has a general PowerPoint skill. Search 'pptx' in Capabilities → Skills, read it, and install it if you want to compare."),
     S("Brief the deck (15 min)", "Start a New session in your kopi-kaki folder. This is the run you will screenshot for PP Task 2.",
       where=f"Hermes Desktop — Mia, folder {WSF}",
       prompt="Use the kopi-pitch-deck skill and python-pptx (from .office-venv in this folder). Build the Kopi Kaki Co. pitch deck for Friday's meeting with a bank relationship manager.\n"
              "- 8-10 slides: title · the problem · Gula Melaka Cold Brew (SGD 6.80, from 1 Dec 2026) · proof from the 60 pop-up tasting reviews (average rating and top themes with review IDs) · market and the 6 competitors · launch plan 17 Nov-14 Dec #ShiokColdBrew · KPIs (2,500 pre-orders, 8% engagement, 40,000 views) · budget SGD 15,000 · the ask (I will fill in the amount).\n"
              "- One NATIVE editable chart (ratings distribution or KPI targets), brand colours from brand-guide.md, the logo on the title slide.\n"
              "- Speaker notes: the source file for every number.\n"
              "Save outputs/deck/kopi-kaki-pitch.pptx. If LibreOffice is installed, also save outputs/deck/kopi-kaki-pitch.pdf and check every page for clipping or overlap. Write outputs/deck/qa-report.md, then open the deck for me.",
       expect="kopi-kaki-pitch.pptx (and the PDF if LibreOffice is installed) and qa-report.md in outputs/deck/."),
     S("Check it: content errors and layout errors (8 min)",
       "Open the deck Mia opened (or double-click it in outputs/deck/). Content error = a wrong or unsourced number. Layout error = clipped, overlapping or unreadable text. "
       "Check three numbers against the source files yourself and click the chart to confirm it is editable."),
     S("One revision, then approve (8 min)", "Ask for a concrete, testable change, then approve the deck.",
       where="Hermes Desktop — Mia",
       prompt="Revise the deck: (1) make slide 2's headline state the problem in one sentence; (2) on the reviews slide show the average rating as one big number with the review count; (3) the ask slide: 'SGD 50,000 working capital for the Tiong Bahru flagship'. Re-check every slide, add the changes to qa-report.md, and summarise what changed.",
       expect="Updated PPTX and qa-report.md.", decide="Are the numbers right and the story convincing? Approve or ask for one more change."),
     S("Capture your PP Task 2 evidence (3 min)",
       "Take ONE readable screenshot of Hermes Desktop showing your request and the finished deck — for example the chat with the saved .pptx path and the slides open beside it. Hide keys and private data. Keep the .pptx and qa-report.md."),
    ]
    L["verify"] = ["kopi-pitch-deck skill installed and available", "8-10 editable slides with one native chart",
                   "Three numbers checked by you against the source files", "No clipped or overlapping text; qa-report.md lists fixes",
                   "PP Task 2: ONE Hermes Desktop screenshot showing the PPT run and the deck"]
    L["trouble"] = [("No PDF", "LibreOffice is not installed. That is fine: open the .pptx and use File → Export → PDF yourself."),
                    ("Chart is a picture", "Ask Mia to use a python-pptx chart (add_chart) so the chart stays editable."),
                    ("Invented figures", "Point Mia at the source files and the skill rule 'never invent figures'; ask for a sourced revision.")]
    L["challenge"] = "Ask Mia to turn the same deck into a one-page investor memo (Word). Which format would the bank manager read first?"
