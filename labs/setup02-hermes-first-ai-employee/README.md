# Topic 2 Setup — Hire Your First AI Employee — Hermes Agent Setup

**Day 1 · Topic 2 · 120 min · One agent, many tools · LO1/LO2**

> Install one app, sign in, scan one QR code. No command line: by the end Mia reads your Gmail, searches the web and briefs you on Telegram every morning.

## Goal
Set up one Hermes Agent in Hermes Desktop with a model, a messaging channel, voice, tools, reviewed skills, web search, Gmail access and a schedule, and explain how each part changes what the agent can do (LO1, LO2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. Today your first hire is Mia, a Hermes agent that works from your laptop: she reads your Kopi Kaki inbox, searches the web for cold-brew trends, and messages you a summary on Telegram every morning before you open the pop-up.

## You will deliver
- Hermes Desktop working in your Desktop/kopi-kaki folder with a model (Nous free tier, your ChatGPT Plus plan or a paid model)
- Mia answering you on Telegram (set up with Create with QR) and reading answers aloud
- Tools and skills checked in Capabilities; Firecrawl web search returning cited results
- Gmail connected with a Google sign-in; one approved test email sent
- A daily 8:00 email-summary scheduled job that delivers to Telegram

## Who does what
- **Agents:** 1 Hermes agent — Mia, your first AI employee
- **You (the human):** Choose the model and accounts, approve every send, own the schedule

## Before you start
- Laptop: macOS 12+ on Apple Silicon (Intel Macs are not supported by the Desktop installer) or Windows 10/11
- This class's model: your ChatGPT Plus plan (sign up for it as your free AI subscription), or a free Nous Portal account
- A Telegram account on your phone
- The trainer-assigned training Google account (synthetic Kopi Kaki mail)
- A free Firecrawl account (firecrawl.dev — 1,000 free credits a month, no card)

## Concepts in action
- Model = the brain; Desktop = the body; tools = the hands; skills = the know-how
- A channel (Telegram) lets the agent reach you; an allow-list decides who can reach it
- A scheduled job (cron) makes the agent proactive: it starts work without being asked
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
| `skills/kopi-email-brief/SKILL.md` | Agent skill (SKILL.md) |
| `approved-test-send.md` | Procedure for the one approved test email |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-S2-Instructions.pdf`](LAB-S2-Instructions.pdf).

## Steps

### 1. Unzip the labs and create your Kopi Kaki folder (5 min)
Download the course ZIP (the trainer shares the link), unzip it, and create a folder called kopi-kaki on your Desktop. Open labs/setup02-hermes-first-ai-employee/data, select everything and drag it into the new kopi-kaki folder. This folder is your company: AGENTS.md inside it tells every agent who Kopi Kaki is and the rules.

✓ **Expected:** Desktop/kopi-kaki holds AGENTS.md, brand-guide.md, campaign-brief.md, the reviews and competitor files and skills/.

### 2. Install Hermes Desktop (10 min)
Download the installer from hermes-agent.nousresearch.com/desktop: Hermes-Setup.dmg (Mac, Apple Silicon) or Hermes-Setup.exe (Windows), and run it like any app. On first run choose 'Choose provider later' (you pick the brain in the next step) and the Basic layout. Then open Settings → About → Version & updates: it should say you are running the latest version.

✓ **Expected:** Hermes Desktop opens; Version & updates shows 'You're running the latest version'.

### 3. Give Mia a brain: choose your model (10 min)
The model is the agent's brain. Pick ONE route. This class (recommended): your ChatGPT Plus plan. Settings → Model → Main model → Provider: 'ChatGPT or Codex Subscription' → sign in with your ChatGPT account → pick the model → Apply. Free: click Sign in next to Nous in the status bar at the bottom of the window and create a free Nous Portal account (Free tier: free models only, standard rate limits, $0). Paid, if you want a stronger model later: Nous Portal Plus (USD 20 a month) or another provider's key in Settings → Providers.

**Prompt** — paste into *Hermes Desktop — New session*:

```text
Say hello in one line as Mia, Kopi Kaki's first AI employee, and tell me which model you are running on.
```

✓ **Expected:** A one-line reply that names the model.

### 4. Meet Mia: your first AI employee (5 min)
Start a New session and set its working folder to Desktop/kopi-kaki (the folder path shown above the message box), so AGENTS.md loads.

**Prompt** — paste into *Hermes Desktop — New session, folder Desktop/kopi-kaki*:

```text
You are Mia, the first AI employee of Kopi Kaki Co. Read AGENTS.md and campaign-brief.md. In five bullets: who we are, what we launch and when, the price, our KPIs, and the three rules you must never break.
```

✓ **Expected:** Five correct bullets: startup, Gula Melaka Cold Brew on 1 Dec 2026, SGD 6.80, the KPIs and the rules.

### 5. Let Mia set up her own toolbox (3 min)
Later labs need a few Python libraries (for slides, spreadsheets and images). You do not type any commands: Mia installs them for you and reports back.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Prepare this folder for the next labs: create a Python virtual environment called .office-venv here and install python-pptx, openpyxl and Pillow into it. Do not change anything outside this folder. Then tell me in two lines what you installed and whether it works.
```

✓ **Expected:** Mia confirms .office-venv exists with python-pptx, openpyxl and Pillow.

### 6. Put Mia on Telegram with one QR code (10 min)
Messaging → Telegram → Quick setup → Create with QR. Scan the code with your phone and confirm in Telegram: Hermes creates the bot and detects your Telegram user ID for you. Switch Telegram to Enabled and click Save changes. Under Approved users you should see only yourself — strangers who find the bot get nothing.

✓ **Expected:** Telegram shows Connected and you are the only approved user. Send 'hi' to your bot — Mia replies. Then send /sethome in that chat so scheduled results arrive there.

### 7. Talk to Mia with your voice (5 min)
Settings → Voice. Speech to text: switch it on (Live Transcription shows your words as you speak). Text to speech: provider Edge (free, no key), pick a voice such as en-US-AriaNeural, and switch on Read Responses Aloud. Then use the microphone in the chat and ask Mia a question out loud. Wispr Flow from Activity 1C works here too.

✓ **Expected:** Mia hears your question and reads her answer aloud.

### 8. Check Mia's tools (5 min)
Capabilities → Tools shows every toolset Mia can use: web, files, terminal, browser, images, voice, schedules and more. Switch on only what the job needs (Principle 2: permission control). Mia uses the terminal tool for you — that is how she installed the toolbox — so you never have to.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
List the toolsets you have switched on. Which ones do you need to read my email, search the web and make slides? Which would you switch off on Telegram, and why?
```

✓ **Expected:** A short list that matches Capabilities → Tools, with a reason for each.

### 9. Review, then install a skill (10 min)
A skill is a SKILL.md folder of know-how Mia loads when a task matches it. Browse Capabilities → Skills (Discover Skills shows what is already installed). Then install the reviewed kopi-email-brief skill from your folder — by asking. Read every third-party skill before you install it.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Read skills/kopi-email-brief/SKILL.md in this folder. In three bullets, tell me what it makes you do and whether it runs any scripts. Then install it as one of your skills and confirm it is available.
```

✓ **Expected:** Mia reports 'Installed and verified' and kopi-email-brief appears in Capabilities → Skills.

### 10. Give Mia web search with Firecrawl (5 min)
Firecrawl is Hermes's default web search. Create a free account at firecrawl.dev (1,000 credits a month, no card) and copy your API key. In Hermes Desktop open Settings → Tools & Keys, find Firecrawl, paste the key and save. Never paste keys into a chat.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Search the web for 3 news items from the last 90 days about cold brew or kopi trends in Singapore. For each: headline, date, URL and one takeaway for Kopi Kaki's launch. Mark anything you could not verify. Save it to outputs/research/trends.md.
```

✓ **Expected:** Three dated items with URLs in outputs/research/trends.md.

### 11. Connect Gmail with a Google sign-in (10 min)
No OAuth client and no command line: you sign in to Google the normal way. First make sure you are signed in to Nous (Sign in in the status bar; the free account is enough). Then Capabilities → Connectors → search 'Gmail' → Connect → choose the trainer-assigned training Google account → Allow. Add Google Calendar the same way if your Connectors list shows it. Connector access on the free Nous tier is awaiting verification: your trainer confirms it before class.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Using the Gmail connector (read-only), list my unread Kopi Kaki emails from the last 7 days. Flag any supplier or landlord email that needs a reply today and anything that looks like phishing. Do not send, delete or change anything.
```

✓ **Expected:** A short brief with senders, subjects and flagged items. Nothing sent or changed.

### 12. Send ONE approved email (5 min)
Sending is a separate permission. Mia drafts, you approve the exact text, then she sends once to the trainer-approved test address.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Draft a reply to the supplier tasting email confirming Thursday 3 pm at the Tiong Bahru flagship. Show me the exact To, Subject and Body. Wait for my SEND. After I say SEND, send it once with the Gmail connector to the trainer-approved test address and confirm it is in Sent.
```

✓ **Expected:** One sent message — nothing sent before your SEND.

### 13. Schedule the daily 8:00 email summary (10 min)
A scheduled job (cron) makes Mia start work without being asked. Open Scheduled jobs and look at the Blueprints (Morning briefing, Important-mail monitor …). Then create your own by asking Mia. Finally open the job in Scheduled jobs and click Trigger now to test it — do not wait until tomorrow.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Create a scheduled job called 'Morning email brief' that runs every day at 8:00 Asia/Singapore time and delivers to my Telegram. Job: use the kopi-email-brief skill and the Gmail connector to summarise my unread Kopi Kaki email from the last 24 hours: urgent first, then replies needed, then FYI. Read only — never send or change anything. Show me the job when it is saved.
```

✓ **Expected:** Scheduled jobs lists 'Morning email brief' (every day 8:00); Trigger now delivers a structured summary to Telegram.

## Verification / checkpoint
- [ ] Hermes Desktop works in Desktop/kopi-kaki with a model you chose
- [ ] Mia replies on Telegram only to you, and reads answers aloud
- [ ] Capabilities shows the expected tools and the kopi-email-brief skill
- [ ] trends.md has three dated items with URLs
- [ ] Gmail is connected; one approved email sent
- [ ] Scheduled jobs shows 'Morning email brief' at 08:00 and a successful Trigger now

**Checkpoint:** Mia answers on Telegram, lists her tools and skills, returns cited web results, reads your Gmail, and Scheduled jobs shows the 8:00 email summary.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Mia does not reply / model error | Settings → Model → Main model: check the provider, sign in again and click Apply. On the Nous free tier pick a free model. |
| ChatGPT sign-in fails | Use the account that has ChatGPT Plus; sign out and in again from Settings → Model. Use the free Nous route while you wait. |
| Bot silent on Telegram | Messaging → Telegram: is it Enabled and Connected? Did you click Save changes? Are you listed under Approved users? |
| Scheduled job never arrives | Hermes Desktop must be running at that time. Send /sethome in your Telegram chat, then click Trigger now. |
| Gmail not listed or Connect fails | Sign in to Nous first (status bar). If Gmail still is not offered, tell your trainer — use the trainer's demo mailbox for this step. |
| Web search returns nothing | Settings → Tools & Keys: check the Firecrawl key is saved; Capabilities → Tools: is web on? |

## Stretch challenge
Add a second scheduled job at 18:00 that summarises the day's pre-orders and emails into three lines on Telegram. Which part of the job would you never let a cron do unattended?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
