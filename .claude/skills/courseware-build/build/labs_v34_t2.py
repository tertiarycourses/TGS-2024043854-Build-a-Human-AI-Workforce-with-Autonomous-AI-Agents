"""Topic 2 guided setup + Activities 2 and 3 (v3.4). Commands checked against the Hermes docs (commit 5057eaa,
30 Oct 2026), platform.minimax.io, gogcli.sh / github.com/openclaw/gogcli, firecrawl.dev and skills.sh on 31 Oct 2026."""
from labs_v34_steps import S

MINIMAX_MODEL = "MiniMax-M3.1-Flash"
SOURCES = [
 ("Hermes Desktop", "https://hermes-agent.nousresearch.com/desktop"),
 ("Hermes docs — installation, providers, Telegram, tools, skills, cron, web search", "https://hermes-agent.nousresearch.com/docs/"),
 ("MiniMax — Hermes Agent setup (M Plan)", "https://platform.minimax.io/docs/m-plan/hermes-agent"),
 ("Firecrawl pricing (free 1,000 credits/month)", "https://www.firecrawl.dev/pricing"),
 ("gogcli — Google Workspace CLI", "https://github.com/openclaw/gogcli"),
 ("skills.sh — the open agent-skills directory", "https://skills.sh/"),
 ("Vercel skills CLI (supports Hermes Agent)", "https://github.com/vercel-labs/skills"),
 ("HyperFrames", "https://github.com/heygen-com/hyperframes"), ("Remotion agent skills", "https://github.com/remotion-dev/skills"),
 ("Manim Community", "https://www.manim.community/"), ("Paperclip", "https://github.com/paperclipai/paperclip"),
]

def setup(L, raw):
    L["prereq"] = ["Laptop: macOS 12+ on Apple Silicon (Intel Macs are not supported by the Desktop installer), Windows 10/11, or Linux",
                   "A Telegram account on your phone", "The trainer-assigned training Google account and OAuth client file (from Lab 1)",
                   "A model provider: a MiniMax account (demo) or the provider key your trainer assigns",
                   "A free Firecrawl account (firecrawl.dev — 1,000 free credits a month, no card)"]
    L["steps"] = [
     S("Create the Kopi Kaki workspace (5 min)",
       "Everything your agents do for the startup happens in one folder. AGENTS.md tells every agent who Kopi Kaki is and the rules; Hermes loads it automatically when it starts in that folder. The small Python environment is used by the PPT and image tools later.",
       cmd="mkdir -p ~/kopi-kaki && cp -Rn data/* ~/kopi-kaki/\ncd ~/kopi-kaki\npython3 -m venv .office-venv\n.office-venv/bin/python -m pip install python-pptx openpyxl Pillow\nls",
       expect="~/kopi-kaki holds AGENTS.md, brand-guide.md, campaign-brief.md, the reviews and competitor files and skills/."),
     S("Install Hermes Desktop (10 min)",
       "Download the installer for your laptop from the official page: Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows). On Linux install the CLI, then run `hermes desktop`. On first run, choose 'Choose provider later' — you connect the model in the next step — and pick the Basic layout. Data lives in ~/.hermes (Windows: %LOCALAPPDATA%\\hermes).",
       cmd="# Download: https://hermes-agent.nousresearch.com/desktop\n# CLI (macOS / Linux / WSL2):\ncurl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash\n# CLI (Windows PowerShell):\niex (irm https://hermes-agent.nousresearch.com/install.ps1)\nhermes --version\nhermes desktop",
       expect="Hermes Desktop opens; `hermes --version` prints a version."),
     S("Connect a model — demo with MiniMax (10 min)",
       f"The model is the agent's brain. Hermes has MiniMax built in. Run `hermes model`, choose MiniMax → MiniMax (OAuth) and sign in in the browser, or choose 'MiniMax (global endpoint)' and paste your M Plan subscription key. Then choose 'Enter custom model name' and type {MINIMAX_MODEL}. In Desktop the same setting is Settings → Providers, then Settings → Model → Main model → Apply. "
       "Trial offer: your trainer will confirm any current MiniMax free trial on the day (awaiting verification); MiniMax's published options are the M Plan and pay-as-you-go credits. Use the trainer-assigned provider if you have no MiniMax access.",
       cmd=f"hermes model                       # MiniMax → MiniMax (OAuth), or global endpoint + key\n# key alternative: add to ~/.hermes/.env\n#   MINIMAX_API_KEY=your-key\n# model name: {MINIMAX_MODEL}\nhermes chat -q \"Say hello in one line as Mia, Kopi Kaki's first AI employee.\"",
       expect="A one-line reply from the model."),
     S("Meet Mia: your first AI employee (5 min)",
       "Start a Desktop chat with the working folder set to ~/kopi-kaki so AGENTS.md is loaded, and check that Mia knows the company.",
       where="Hermes Desktop — new chat, folder ~/kopi-kaki",
       prompt="You are Mia, the first AI employee of Kopi Kaki Co. Read AGENTS.md and campaign-brief.md. In five bullets: who we are, what we launch and when, the price, our KPIs, and the three rules you must never break.",
       expect="Five correct bullets: startup, Gula Melaka Cold Brew on 1 Dec 2026, SGD 6.80, the KPIs and the rules."),
     S("Put Mia on Telegram (10 min)",
       "In Telegram open @BotFather → /newbot → choose a name (e.g. Mia Kopi Kaki) and a username ending in 'bot' → copy the token. Get your numeric user ID from @userinfobot. Only allow-listed users can talk to your agent. Desktop shortcut: Messaging → Telegram → Create with QR does all of this for you.",
       cmd="hermes gateway setup          # choose Telegram, paste the token and your user ID\n# or add to ~/.hermes/.env:\n#   TELEGRAM_BOT_TOKEN=...\n#   TELEGRAM_ALLOWED_USERS=123456789\nhermes gateway                # keep running (service: hermes gateway install && hermes gateway start; WSL: hermes gateway run)",
       expect="Send 'hi' to your bot — Mia replies. Then send /sethome in that chat so scheduled results arrive there."),
     S("Configure Mia's tools (5 min)",
       "Tools are what the agent can actually do: web, terminal, files, browser, images, voice, cron and more. Switch on only what the job needs (Principle 2: permission control).",
       cmd="hermes tools --summary\nhermes tools                  # tick or untick toolsets per platform\nhermes tools disable browser --platform telegram",
       expect="The summary lists the enabled toolsets for CLI and Telegram."),
     S("Review, then install skills (10 min)",
       "A skill is a SKILL.md folder of know-how the agent loads when a task matches it. Read every third-party skill before you install it. Start with the reviewed gog-office skill in this lab's data/, then browse the hub.",
       cmd="cat ~/kopi-kaki/skills/gog-office/SKILL.md\nmkdir -p ~/.hermes/skills/productivity && cp -R ~/kopi-kaki/skills/gog-office ~/.hermes/skills/productivity/\nhermes skills list\nhermes skills browse\nhermes skills search marketing",
       expect="gog-office appears in hermes skills list."),
     S("Give Mia web search with Firecrawl (5 min)",
       "Firecrawl is Hermes's default web backend. Create a free key at firecrawl.dev (1,000 credits a month, no card) and add it to Hermes. Then ask a real question.",
       cmd="echo 'FIRECRAWL_API_KEY=fc-your-key' >> ~/.hermes/.env\nhermes tools                  # confirm the web toolset is on",
       where="Hermes Desktop — Mia",
       prompt="Search the web for 3 news items from the last 90 days about cold brew or kopi trends in Singapore. For each: headline, date, URL and one takeaway for Kopi Kaki's launch. Mark anything you could not verify. Save it to outputs/research/trends.md.",
       expect="Three dated items with URLs in outputs/research/trends.md."),
     S("Connect gog: read Gmail and check Calendar (10 min)",
       "gog (gogcli) is a Google Workspace command-line tool Mia drives from the terminal. Sign in once with the trainer-assigned training account and its OAuth client. Read-only first.",
       cmd="brew install openclaw/tap/gogcli        # or: go install github.com/openclaw/gogcli/cmd/gog@latest\ngog auth credentials set ~/Downloads/training-oauth-client.json\nexport GOG_ACCOUNT=\"REPLACE_WITH_ASSIGNED_GOOGLE_EMAIL\"\ngog auth add \"$GOG_ACCOUNT\" --services gmail,calendar\ngog auth doctor --check\ngog --account \"$GOG_ACCOUNT\" gmail search 'is:unread newer_than:7d' --max 10 --json\ngog --account \"$GOG_ACCOUNT\" calendar events --today --json",
       where="Hermes Desktop — Mia",
       prompt="Use gog with the gog-office skill (account $GOG_ACCOUNT, read-only). List my unread Kopi Kaki emails from the last 7 days and today's calendar events in Asia/Singapore time. Flag any clash, any supplier or landlord email that needs a reply today, and anything that looks like phishing. Do not send or change anything.",
       expect="A short brief with message IDs, event times (+08:00) and flagged items."),
     S("Send ONE approved email (5 min)",
       "Sending is a separate permission. Mia drafts, you approve the exact text, then she sends once to the trainer-approved test address and shows the message ID. Re-authorise with send access only for this step if your account was added read-only.",
       where="Hermes Desktop — Mia",
       prompt="Draft a reply to the supplier tasting email confirming Thursday 3 pm at the Tiong Bahru flagship. Show me the exact To, Subject and Body. Wait for my SEND. After I say SEND, send it once with gog gmail send to the trainer-approved test address, show the message ID and confirm it is in Sent.",
       cmd="gog --account \"$GOG_ACCOUNT\" gmail send --to TRAINER_TEST_ADDRESS --subject \"Kopi Kaki tasting — Thursday 3 pm\" --body \"…approved text…\"",
       expect="One message ID and a Sent record — nothing sent before your SEND.", decide="Approve the exact recipient, subject and body."),
     S("Make Mia proactive: cron basics (5 min)",
       "Cron makes the agent start work without being asked. Jobs run inside the gateway, which checks for due jobs every minute — keep it running.",
       cmd="hermes cron list\nhermes cron status\n# a test job you can delete afterwards:\nhermes cron create \"every 2h\" \"Remind me to post the pop-up photo.\" --name test-reminder --deliver telegram\nhermes cron run <job_id>\nhermes cron remove <job_id>",
       expect="The test reminder arrives on Telegram, then the job is removed."),
     S("Schedule the daily 8:00 email summary (5 min)",
       "Your morning brief before you open the pop-up: Mia reads the inbox at 8:00 Singapore time and messages you on Telegram. Reading only — the cron job never sends email.",
       cmd="hermes cron create \"0 8 * * *\" \"Summarise my unread Kopi Kaki Gmail from the last 24 hours with gog (read-only): urgent items first, then replies needed, then FYI. Add today's calendar events and any clash. Never send or change anything.\" --skill gog-office --name \"Morning email brief\" --deliver telegram --timezone Asia/Singapore\nhermes cron list\nhermes cron run <job_id>",
       expect="Your test run delivers a structured email summary to Telegram; the job is listed for 08:00 daily."),
    ]
    L["verify"] = ["Desktop runs in ~/kopi-kaki with a working model", "Mia replies on Telegram only to your user ID",
                   "hermes tools --summary and hermes skills list show the expected tools and gog-office",
                   "trends.md has three dated items with URLs", "gog reads Gmail and Calendar; one approved email has a message ID",
                   "`hermes cron list` shows 'Morning email brief' at 08:00 Asia/Singapore"]
    L["trouble"] = [("`hermes: command not found`", "Open a new terminal or run `source ~/.zshrc` (macOS) / `source ~/.bashrc` (Linux/WSL2)."),
                    ("MiniMax sign-in works but replies fail", "Check the plan/credits on platform.minimax.io; re-run `hermes model` and type the model name exactly."),
                    ("Bot silent on Telegram", "Is the gateway running? `hermes gateway status`; check TELEGRAM_ALLOWED_USERS has your numeric ID."),
                    ("Cron never fires", "The gateway must be running; check `hermes cron status`. Results go to the /sethome chat."),
                    ("gog: access blocked", "Use the trainer's OAuth client and the assigned account; run `gog auth doctor --check`."),
                    ("Web search returns nothing", "Check FIRECRAWL_API_KEY in ~/.hermes/.env and that the web toolset is enabled.")]
    L["challenge"] = "Add a second cron at 18:00 that summarises the day's pre-orders and emails into three lines on Telegram. Which part of the job would you never let a cron do unattended?"

def act2(L):
    L["prereq"] = ["Topic 2 setup done: Mia works in ~/kopi-kaki", "Node.js 22.20+ for the skills CLI (`node --version`)", "This lab's data/ copied into ~/kopi-kaki"]
    L["steps"] = [
     S("Copy the website brief (2 min)", "The brief says who the site is for, the sections, the brand and the definition of done.",
       cmd="cp -Rn data/* ~/kopi-kaki/\nmkdir -p ~/kopi-kaki/outputs/website\ncat ~/kopi-kaki/website-brief.md"),
     S("Choose UX skills on skills.sh (5 min)",
       "Open skills.sh and search 'frontend' and 'design'. The most installed design skills include Anthropic's frontend-design (about 1.1 million installs), Vercel's web-design-guidelines and ui-ux-pro-max. Open each skill's page and read its SKILL.md: what will it make the agent do, and does it run any scripts?",
       cmd="# Browse: https://skills.sh/  (search: frontend, design)\nhermes skills search design --source skills-sh",
       expect="You can explain in one sentence what each skill changes."),
     S("Install two UX skills into Hermes (5 min)",
       "The skills.sh command-line tool installs straight into Hermes with -a hermes-agent (-g = for your user, into ~/.hermes/skills).",
       cmd="npx skills add https://github.com/anthropics/skills --skill frontend-design -a hermes-agent -g\nnpx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines -a hermes-agent -g\nhermes skills list | grep -i -E 'frontend-design|web-design'",
       expect="Both skills appear in hermes skills list."),
     S("Brief Mia like a design agency (15 min)",
       "Start a new Desktop chat in ~/kopi-kaki so the new skills load.",
       where="Hermes Desktop — Mia, folder ~/kopi-kaki",
       prompt="Use the frontend-design and web-design-guidelines skills. Build the Kopi Kaki Co. one-page website from website-brief.md.\n"
              "- Sections: hero (Gula Melaka Cold Brew, SGD 6.80, from 1 Dec 2026), our story (a startup founded in 2026), menu from product-catalogue.csv, pop-ups and the Tiong Bahru flagship, three short taster quotes from customer-reviews.csv (no names), app pre-order button, footer.\n"
              "- Brand: colours and voice from brand-guide.md; use assets/kopi-kaki-logo.png and assets/cold-brew-product-card.png.\n"
              "- One self-contained outputs/website/index.html: inline CSS, no external libraries or fonts, responsive down to 375 px, accessible contrast.\n"
              "- No health or halal claims. Every price and date must match the source files.\n"
              "When done, list which skill rules you applied and every fact with its source file.",
       expect="outputs/website/index.html and a list of applied rules and sourced facts."),
     S("Open it and check it like a customer (5 min)",
       "Open the page, then narrow the browser to phone width (or use the browser's device view). Check the price, the date, the pop-up information and the button.",
       cmd="open ~/kopi-kaki/outputs/website/index.html      # Windows: start  ·  Linux: xdg-open"),
     S("Ask for one concrete revision (8 min)", "Give feedback an agent can test, not 'make it nicer'.",
       where="Hermes Desktop — Mia",
       prompt="Revise outputs/website/index.html: (1) move the pre-order button into the hero, visible without scrolling on a 375 px phone; (2) make the menu a two-column grid on desktop and one column on phone; (3) add the pop-up dates as a simple list. Then write outputs/website/review.md: what the skills changed, my requested fixes, and the checks you ran.",
       expect="Updated page and review.md.", decide="Is it on-brand, true and usable on a phone?"),
     S("Capture your website (2 min)", "Save two screenshots — desktop and phone width — into outputs/website/. You will reuse the site's facts in the pitch deck and the social posts."),
    ]
    L["verify"] = ["Two UX skills installed and listed", "index.html opens offline with the Kopi Kaki colours, logo and product card",
                   "Every price and date matches the source files", "Works at 375 px; review.md records your revision"]
    L["trouble"] = [("`npx skills` fails", "Install Node.js 22.20+ and retry; or use `hermes skills install skills-sh/anthropics/skills/frontend-design`."),
                    ("Skill not used", "Start a new chat so newly installed skills load; name the skill in the prompt."),
                    ("Images missing", "Check assets/ was copied into ~/kopi-kaki and the paths in index.html are relative.")]
    L["challenge"] = "Install ui-ux-pro-max as a third skill and ask Mia for a second design. Which design would you ship, and what did the extra skill actually change?"

def act3(L):
    L["prereq"] = ["Topic 2 setup and Activity 2 done", "python-pptx in ~/kopi-kaki/.office-venv (from the setup step)",
                   "LibreOffice for the PDF render (`soffice --version`)", "This lab's data/ copied into ~/kopi-kaki"]
    L["steps"] = [
     S("Copy the deck skill and check the PPT tool (3 min)",
       "The tool writes the file (python-pptx); the skill says how to build a good deck. Hermes also ships a built-in microsoft-office skill (Word, PowerPoint, Excel via python-pptx); the reviewed kopi-pitch-deck skill adds your story, brand and checks.",
       cmd="cp -Rn data/* ~/kopi-kaki/\ncat ~/kopi-kaki/skills/kopi-pitch-deck/SKILL.md\nmkdir -p ~/.hermes/skills/office && cp -R ~/kopi-kaki/skills/kopi-pitch-deck ~/.hermes/skills/office/\n~/kopi-kaki/.office-venv/bin/python -c \"import pptx; print('python-pptx', pptx.__version__)\"\nhermes skills list | grep -i -E 'kopi-pitch-deck|microsoft-office'\nsoffice --version",
       expect="kopi-pitch-deck is listed; python-pptx prints its version."),
     S("Optional: add a hub PPT skill (3 min)", "For comparison, Hermes's optional pptx-author skill (adapted from Anthropic's) builds decks headless with python-pptx.",
       cmd="hermes skills install official/finance/pptx-author"),
     S("Brief the deck (15 min)", "Start a new Desktop chat in ~/kopi-kaki. This is the run you will screenshot for PP Task 2.",
       where="Hermes Desktop — Mia, folder ~/kopi-kaki",
       prompt="Use the kopi-pitch-deck skill and python-pptx (~/kopi-kaki/.office-venv/bin/python). Build the Kopi Kaki Co. pitch deck for Friday's meeting with a bank relationship manager.\n"
              "- 8-10 slides: title · the problem · Gula Melaka Cold Brew (SGD 6.80, from 1 Dec 2026) · proof from the 60 pop-up tasting reviews (average rating and top themes with review IDs) · market and the 6 competitors · launch plan 17 Nov-14 Dec #ShiokColdBrew · KPIs (2,500 pre-orders, 8% engagement, 40,000 views) · budget SGD 15,000 · the ask (I will fill in the amount).\n"
              "- One NATIVE editable chart (ratings distribution or KPI targets), brand colours from brand-guide.md, the logo on the title slide.\n"
              "- Speaker notes: the source file for every number.\n"
              "Save outputs/deck/kopi-kaki-pitch.pptx, render outputs/deck/kopi-kaki-pitch.pdf with soffice, check every page for clipping or overlap, and write outputs/deck/qa-report.md.",
       expect="kopi-kaki-pitch.pptx, the PDF and qa-report.md in outputs/deck/."),
     S("Check it: content errors and layout errors (8 min)",
       "Open the PDF and the PPTX. Content error = a wrong or unsourced number. Layout error = clipped, overlapping or unreadable text. Check three numbers against the source files yourself and click the chart to confirm it is editable.",
       cmd="open ~/kopi-kaki/outputs/deck/kopi-kaki-pitch.pdf\nopen ~/kopi-kaki/outputs/deck/kopi-kaki-pitch.pptx\ncat ~/kopi-kaki/outputs/deck/qa-report.md"),
     S("One revision, then approve (8 min)", "Ask for a concrete, testable change, then approve the deck.",
       where="Hermes Desktop — Mia",
       prompt="Revise the deck: (1) make slide 2's headline state the problem in one sentence; (2) on the reviews slide show the average rating as one big number with the review count; (3) the ask slide: 'SGD 50,000 working capital for the Tiong Bahru flagship'. Re-render the PDF, re-check every page, and add the changes to qa-report.md. Then summarise what changed.",
       expect="Updated PPTX, PDF and qa-report.md.", decide="Are the numbers right and the story convincing? Approve or ask for one more change."),
     S("Capture your PP Task 2 evidence (3 min)",
       "Take ONE readable screenshot of Hermes Desktop (or the Hermes dashboard) showing your request and the finished deck — for example the chat with the saved .pptx path and the slides open beside it. Hide keys and private data. Keep the .pptx, the PDF and qa-report.md."),
    ]
    L["verify"] = ["kopi-pitch-deck skill listed; python-pptx works", "8-10 editable slides with one native chart",
                   "Three numbers checked by you against the source files", "PDF has no clipped or overlapping text; qa-report.md lists fixes",
                   "PP Task 2: ONE Hermes Desktop/dashboard screenshot showing the PPT run and the deck"]
    L["trouble"] = [("`soffice: command not found`", "Install LibreOffice (macOS: brew install --cask libreoffice) or open the .pptx and export PDF yourself."),
                    ("Chart is a picture", "Ask Mia to use python-pptx chart_data / add_chart so the chart stays editable."),
                    ("Invented figures", "Point Mia at the source files and the skill rule 'never invent figures'; ask for a sourced revision.")]
    L["challenge"] = "Ask Mia to turn the same deck into a one-page investor memo (DOCX) with the microsoft-office skill. Which format would the bank manager read first?"
