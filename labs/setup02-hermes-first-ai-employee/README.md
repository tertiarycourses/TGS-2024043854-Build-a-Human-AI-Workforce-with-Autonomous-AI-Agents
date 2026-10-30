# Topic 2 Setup — Hire Your First AI Employee — Hermes Agent Setup

**Day 1 · Topic 2 · 120 min · One agent, many tools · LO1/LO2**

> Install Hermes Desktop, give it a brain, put it on Telegram, arm it with tools and skills, then let it read your inbox and brief you every morning.

## Goal
Set up one Hermes Agent with a model, a messaging channel, tools, reviewed skills, web search, Google Workspace access and a schedule, and explain how each part changes what the agent can do (LO1, LO2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. Today your first hire is Mia, a Hermes agent that works from your laptop: she reads your Kopi Kaki inbox and calendar, searches the web for cold-brew trends, and messages you a summary on Telegram every morning before you open the pop-up.

## You will deliver
- Hermes Desktop running in ~/kopi-kaki with a working model (MiniMax demo or the trainer-assigned provider)
- Mia answering you on Telegram from your allow-listed user ID
- Tools and skills listed and tested; Firecrawl web search returning cited results
- gog reading Gmail and Calendar; one approved test email sent
- A daily 8:00 email-summary cron that delivers to Telegram

## Who does what
- **Agents:** 1 Hermes agent — Mia, your first AI employee
- **You (the human):** Choose the model and accounts, approve every send, own the schedule

## Before you start
- Laptop: macOS 12+ on Apple Silicon (Intel Macs are not supported by the Desktop installer), Windows 10/11, or Linux
- A Telegram account on your phone
- The trainer-assigned training Google account and OAuth client file (from Lab 1)
- A model provider: a MiniMax account (demo) or the provider key your trainer assigns
- A free Firecrawl account (firecrawl.dev — 1,000 free credits a month, no card)

## Concepts in action
- Model = the brain; Desktop/gateway = the body; tools = the hands; skills = the know-how
- A channel (Telegram) lets the agent reach you; an allow-list decides who can reach it
- Cron makes the agent proactive: it starts work without being asked
- Read and send are different permissions: approve every send

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `competitors.csv` | 6 fictional competitors |
| `customer-reviews.csv` | 60 synthetic customer reviews |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `skills/gog-office/SKILL.md` | Agent skill (SKILL.md) |
| `approved-test-send.md` | Procedure for the one approved test email |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-S2-Instructions.pdf`](LAB-S2-Instructions.pdf).

## Steps

### 1. Create the Kopi Kaki workspace (5 min)
Everything your agents do for the startup happens in one folder. AGENTS.md tells every agent who Kopi Kaki is and the rules; Hermes loads it automatically when it starts in that folder. The small Python environment is used by the PPT and image tools later.

```bash
mkdir -p ~/kopi-kaki && cp -Rn data/* ~/kopi-kaki/
cd ~/kopi-kaki
python3 -m venv .office-venv
.office-venv/bin/python -m pip install python-pptx openpyxl Pillow
ls
```

✅ **Expected:** ~/kopi-kaki holds AGENTS.md, brand-guide.md, campaign-brief.md, the reviews and competitor files and skills/.

### 2. Install Hermes Desktop (10 min)
Download the installer for your laptop from the official page: Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows). On Linux install the CLI, then run `hermes desktop`. On first run, choose 'Choose provider later' — you connect the model in the next step — and pick the Basic layout. Data lives in ~/.hermes (Windows: %LOCALAPPDATA%\hermes).

```bash
# Download: https://hermes-agent.nousresearch.com/desktop
# CLI (macOS / Linux / WSL2):
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# CLI (Windows PowerShell):
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
hermes --version
hermes desktop
```

✅ **Expected:** Hermes Desktop opens; `hermes --version` prints a version.

### 3. Connect a model — demo with MiniMax (10 min)
The model is the agent's brain. Hermes has MiniMax built in. Run `hermes model`, choose MiniMax → MiniMax (OAuth) and sign in in the browser, or choose 'MiniMax (global endpoint)' and paste your M Plan subscription key. Then choose 'Enter custom model name' and type MiniMax-M3.1-Flash. In Desktop the same setting is Settings → Providers, then Settings → Model → Main model → Apply. Trial offer: your trainer will confirm any current MiniMax free trial on the day (awaiting verification); MiniMax's published options are the M Plan and pay-as-you-go credits. Use the trainer-assigned provider if you have no MiniMax access.

```bash
hermes model                       # MiniMax → MiniMax (OAuth), or global endpoint + key
# key alternative: add to ~/.hermes/.env
#   MINIMAX_API_KEY=your-key
# model name: MiniMax-M3.1-Flash
hermes chat -q "Say hello in one line as Mia, Kopi Kaki's first AI employee."
```

✅ **Expected:** A one-line reply from the model.

### 4. Meet Mia: your first AI employee (5 min)
Start a Desktop chat with the working folder set to ~/kopi-kaki so AGENTS.md is loaded, and check that Mia knows the company.

**Prompt** — paste into *Hermes Desktop — new chat, folder ~/kopi-kaki*:

```text
You are Mia, the first AI employee of Kopi Kaki Co. Read AGENTS.md and campaign-brief.md. In five bullets: who we are, what we launch and when, the price, our KPIs, and the three rules you must never break.
```

✅ **Expected:** Five correct bullets: startup, Gula Melaka Cold Brew on 1 Dec 2026, SGD 6.80, the KPIs and the rules.

### 5. Put Mia on Telegram (10 min)
In Telegram open @BotFather → /newbot → choose a name (e.g. Mia Kopi Kaki) and a username ending in 'bot' → copy the token. Get your numeric user ID from @userinfobot. Only allow-listed users can talk to your agent. Desktop shortcut: Messaging → Telegram → Create with QR does all of this for you.

```bash
hermes gateway setup          # choose Telegram, paste the token and your user ID
# or add to ~/.hermes/.env:
#   TELEGRAM_BOT_TOKEN=...
#   TELEGRAM_ALLOWED_USERS=123456789
hermes gateway                # keep running (service: hermes gateway install && hermes gateway start; WSL: hermes gateway run)
```

✅ **Expected:** Send 'hi' to your bot — Mia replies. Then send /sethome in that chat so scheduled results arrive there.

### 6. Configure Mia's tools (5 min)
Tools are what the agent can actually do: web, terminal, files, browser, images, voice, cron and more. Switch on only what the job needs (Principle 2: permission control).

```bash
hermes tools --summary
hermes tools                  # tick or untick toolsets per platform
hermes tools disable browser --platform telegram
```

✅ **Expected:** The summary lists the enabled toolsets for CLI and Telegram.

### 7. Review, then install skills (10 min)
A skill is a SKILL.md folder of know-how the agent loads when a task matches it. Read every third-party skill before you install it. Start with the reviewed gog-office skill in this lab's data/, then browse the hub.

```bash
cat ~/kopi-kaki/skills/gog-office/SKILL.md
mkdir -p ~/.hermes/skills/productivity && cp -R ~/kopi-kaki/skills/gog-office ~/.hermes/skills/productivity/
hermes skills list
hermes skills browse
hermes skills search marketing
```

✅ **Expected:** gog-office appears in hermes skills list.

### 8. Give Mia web search with Firecrawl (5 min)
Firecrawl is Hermes's default web backend. Create a free key at firecrawl.dev (1,000 credits a month, no card) and add it to Hermes. Then ask a real question.

```bash
echo 'FIRECRAWL_API_KEY=fc-your-key' >> ~/.hermes/.env
hermes tools                  # confirm the web toolset is on
```

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Search the web for 3 news items from the last 90 days about cold brew or kopi trends in Singapore. For each: headline, date, URL and one takeaway for Kopi Kaki's launch. Mark anything you could not verify. Save it to outputs/research/trends.md.
```

✅ **Expected:** Three dated items with URLs in outputs/research/trends.md.

### 9. Connect gog: read Gmail and check Calendar (10 min)
gog (gogcli) is a Google Workspace command-line tool Mia drives from the terminal. Sign in once with the trainer-assigned training account and its OAuth client. Read-only first.

```bash
brew install openclaw/tap/gogcli        # or: go install github.com/openclaw/gogcli/cmd/gog@latest
gog auth credentials set ~/Downloads/training-oauth-client.json
export GOG_ACCOUNT="REPLACE_WITH_ASSIGNED_GOOGLE_EMAIL"
gog auth add "$GOG_ACCOUNT" --services gmail,calendar
gog auth doctor --check
gog --account "$GOG_ACCOUNT" gmail search 'is:unread newer_than:7d' --max 10 --json
gog --account "$GOG_ACCOUNT" calendar events --today --json
```

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Use gog with the gog-office skill (account $GOG_ACCOUNT, read-only). List my unread Kopi Kaki emails from the last 7 days and today's calendar events in Asia/Singapore time. Flag any clash, any supplier or landlord email that needs a reply today, and anything that looks like phishing. Do not send or change anything.
```

✅ **Expected:** A short brief with message IDs, event times (+08:00) and flagged items.

### 10. Send ONE approved email (5 min)
Sending is a separate permission. Mia drafts, you approve the exact text, then she sends once to the trainer-approved test address and shows the message ID. Re-authorise with send access only for this step if your account was added read-only.

```bash
gog --account "$GOG_ACCOUNT" gmail send --to TRAINER_TEST_ADDRESS --subject "Kopi Kaki tasting — Thursday 3 pm" --body "…approved text…"
```

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Draft a reply to the supplier tasting email confirming Thursday 3 pm at the Tiong Bahru flagship. Show me the exact To, Subject and Body. Wait for my SEND. After I say SEND, send it once with gog gmail send to the trainer-approved test address, show the message ID and confirm it is in Sent.
```

✅ **Expected:** One message ID and a Sent record — nothing sent before your SEND.

### 11. Make Mia proactive: cron basics (5 min)
Cron makes the agent start work without being asked. Jobs run inside the gateway, which checks for due jobs every minute — keep it running.

```bash
hermes cron list
hermes cron status
# a test job you can delete afterwards:
hermes cron create "every 2h" "Remind me to post the pop-up photo." --name test-reminder --deliver telegram
hermes cron run <job_id>
hermes cron remove <job_id>
```

✅ **Expected:** The test reminder arrives on Telegram, then the job is removed.

### 12. Schedule the daily 8:00 email summary (5 min)
Your morning brief before you open the pop-up: Mia reads the inbox at 8:00 Singapore time and messages you on Telegram. Reading only — the cron job never sends email.

```bash
hermes cron create "0 8 * * *" "Summarise my unread Kopi Kaki Gmail from the last 24 hours with gog (read-only): urgent items first, then replies needed, then FYI. Add today's calendar events and any clash. Never send or change anything." --skill gog-office --name "Morning email brief" --deliver telegram --timezone Asia/Singapore
hermes cron list
hermes cron run <job_id>
```

✅ **Expected:** Your test run delivers a structured email summary to Telegram; the job is listed for 08:00 daily.

## Verification / checkpoint
- [ ] Desktop runs in ~/kopi-kaki with a working model
- [ ] Mia replies on Telegram only to your user ID
- [ ] hermes tools --summary and hermes skills list show the expected tools and gog-office
- [ ] trends.md has three dated items with URLs
- [ ] gog reads Gmail and Calendar; one approved email has a message ID
- [ ] `hermes cron list` shows 'Morning email brief' at 08:00 Asia/Singapore

**Checkpoint:** Mia answers on Telegram, lists her tools and skills, returns cited web results, reads your inbox and calendar, and `hermes cron list` shows the 8:00 email summary.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `hermes: command not found` | Open a new terminal or run `source ~/.zshrc` (macOS) / `source ~/.bashrc` (Linux/WSL2). |
| MiniMax sign-in works but replies fail | Check the plan/credits on platform.minimax.io; re-run `hermes model` and type the model name exactly. |
| Bot silent on Telegram | Is the gateway running? `hermes gateway status`; check TELEGRAM_ALLOWED_USERS has your numeric ID. |
| Cron never fires | The gateway must be running; check `hermes cron status`. Results go to the /sethome chat. |
| gog: access blocked | Use the trainer's OAuth client and the assigned account; run `gog auth doctor --check`. |
| Web search returns nothing | Check FIRECRAWL_API_KEY in ~/.hermes/.env and that the web toolset is enabled. |

## Stretch challenge
Add a second cron at 18:00 that summarises the day's pre-orders and emails into three lines on Telegram. Which part of the job would you never let a cron do unattended?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
