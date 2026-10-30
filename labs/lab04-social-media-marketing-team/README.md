# Lab 4 — Activity 4 — Your Social Media Marketing Team

**Day 2 · Topic 3 · 60 min · Multi-agent team on a Kanban board · LO2**

> One researcher, three platform writers and an image creator work in parallel. In an hour you review a gallery of LinkedIn, Facebook and Instagram launch posts.

## Goal
Design a multi-agent team with profiles, a Kanban dependency graph and a human approval gate, and compare its output and effort with a single agent (LO2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. Two weeks to launch. LinkedIn needs a founder story for investors and corporate catering buyers, Facebook needs the neighbourhood and the pop-up dates, Instagram needs a scroll-stopping image. One agent writing all three sounds the same everywhere, so you build a team: each specialist owns one platform, and you approve every post before anything goes public.

## You will deliver
- Five Hermes profiles: researcher, linkedin-writer, facebook-writer, instagram-writer, image-creator
- A Kanban board (tenant kopi-social) with dependencies and an unassigned HUMAN approval card
- outputs/social/research.md, linkedin.md, facebook.md, instagram.md and images/*.png
- outputs/social/gallery.html — every post shown as it would appear on its platform
- outputs/social/approval-log.md — APPROVE / EDIT / REJECT per post

## Who does what
- **Agents:** 5 Hermes profiles shown as bots: researcher → 3 platform writers (in parallel) → image creator
- **You (the human):** Brief the campaign, approve or edit each post, nothing is posted publicly

## Before you start
- Topic 2 setup done: Hermes Desktop, a working model and Telegram (the gateway must be running for Kanban to dispatch work)
- Activity 2 website and Activity 3 deck saved — the team reuses their facts
- This lab's data/ copied into ~/kopi-kaki (souls/, tasks/ and tools/make_post_image.py are included)

## Concepts in action
- Profile = a separate agent: its own SOUL.md, memory, skills and model
- Kanban = the team's shared to-do list: assignee, parent dependency, status, history
- Parallel specialists + one human gate beat one generalist for multi-channel work
- Bots = profiles you can talk to by name

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
| `social-comments.csv` | 20 social comments incl. complaints, legal, PII, spam |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `souls/researcher.SOUL.md` | Role + rules for one studio profile |
| `souls/linkedin-writer.SOUL.md` | Role + rules for one studio profile |
| `souls/facebook-writer.SOUL.md` | Role + rules for one studio profile |
| `souls/instagram-writer.SOUL.md` | Role + rules for one studio profile |
| `souls/image-creator.SOUL.md` | Role + rules for one studio profile |
| `tasks/s1-research.md` | Task brief for one Kanban card |
| `tasks/s2-linkedin.md` | Task brief for one Kanban card |
| `tasks/s3-facebook.md` | Task brief for one Kanban card |
| `tasks/s4-instagram.md` | Task brief for one Kanban card |
| `tasks/s5-images.md` | Task brief for one Kanban card |
| `tools/make_post_image.py` | Offline on-brand image tool (Pillow) |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-04-Instructions.pdf`](LAB-04-Instructions.pdf).

## Steps

### 1. Copy the lab data and create the output folders (3 min)
Open a terminal in this lab folder. The data/ folder holds the five team role files (souls/), the task briefs (tasks/), the brand files and a small image tool. Copy it into your company workspace without overwriting your own AGENTS.md.

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/kopi-kaki/outputs/social/images
cd ~/kopi-kaki && ls souls tasks tools
```

✅ **Expected:** souls/ lists researcher, linkedin-writer, facebook-writer, instagram-writer and image-creator.

### 2. Staff the team: five profiles, one job each (8 min)
A profile is a separate Hermes agent with its own SOUL.md, memory, skills and settings. --clone copies your working model and keys from the default profile, so every specialist can think straight away. The description is how the board routes work to the right specialist.

```bash
hermes profile create researcher --clone --description "Finds launch angles, audience insights and facts for Kopi Kaki posts; cites the source file for every fact"
hermes profile create linkedin-writer --clone --description "Writes the founder's LinkedIn post: story, proof, call to action; professional Singapore English"
hermes profile create facebook-writer --clone --description "Writes the neighbourhood Facebook post: pop-up dates, launch day, friendly kopitiam voice"
hermes profile create instagram-writer --clone --description "Writes the Instagram caption, first-line hook and hashtags for a 1080x1350 image post"
hermes profile create image-creator --clone --description "Creates one on-brand 1080x1350 image per post with tools/make_post_image.py and builds the review gallery"
for p in researcher linkedin-writer facebook-writer instagram-writer image-creator; do cp ~/kopi-kaki/souls/$p.SOUL.md ~/.hermes/profiles/$p/SOUL.md; done
hermes profile list
```

✅ **Expected:** hermes profile list shows the five new profiles next to default.

### 3. Meet your team as bots (5 min)
Hermes Desktop's Bot Mode (the Bots tab, on by default) shows every profile as a named bot you can chat with directly. Say hello to two of them and check that each answers in its own role. Optional: give a profile its own Telegram bot token, then run `<profile> gateway install` and `<profile> gateway start`. A bot is how you talk to a profile; the work itself is tracked on the Kanban board.

**Prompt** — paste into *Hermes Desktop → Bots tab → researcher*:

```text
Hi, I'm the founder of Kopi Kaki Co. In two sentences: what is your job on my marketing team, and which files in ~/kopi-kaki will you read first?
```

✅ **Expected:** Each bot describes its own role and names AGENTS.md, campaign-brief.md and brand-guide.md.

### 4. Build the Kanban board with a human gate (10 min)
Ask your default agent (Mia) to build the board. Research runs first; the three writers run in parallel as soon as research is done; the image creator waits for all three; the last card is yours. Nothing is posted anywhere — the output is a review gallery.

**Prompt** — paste into *Hermes Desktop → default profile (Mia), started in ~/kopi-kaki*:

```text
Use the Kanban tools to build the board for tenant kopi-social, workspace ~/kopi-kaki.
1. Research launch angles - assignee researcher - body from tasks/s1-research.md.
2. LinkedIn post - assignee linkedin-writer - parent: card 1 - body from tasks/s2-linkedin.md.
3. Facebook post - assignee facebook-writer - parent: card 1 - body from tasks/s3-facebook.md.
4. Instagram post - assignee instagram-writer - parent: card 1 - body from tasks/s4-instagram.md.
5. Images and review gallery - assignee image-creator - parents: cards 2, 3 and 4 - body from tasks/s5-images.md.
6. HUMAN: approve the posts - unassigned, parent: card 5. Only I complete this card.
Show me the card IDs, assignees and parents as a table. Do not start anything outside this board and never post to a real account.
```

✅ **Expected:** A table of six cards; cards 2–4 depend on 1, card 5 on 2–4, card 6 on 5 and has no assignee.

### 5. Watch the team work (12 min)
Kanban dispatches each card to its profile as soon as its parents are done. Watch in the terminal or in the dashboard's Kanban view. Open a card to read its run history and output path.

```bash
hermes kanban watch --tenant kopi-social
# or the web view:
hermes dashboard          # then open Kanban
```

✅ **Expected:** Research finishes first, the three writers run side by side, then the image creator starts.

### 6. Open the posts gallery (5 min)
The image creator builds one page that shows every post the way it would look on its platform: LinkedIn text post, Facebook post with image, Instagram square with caption. Open it in your browser.

```bash
open ~/kopi-kaki/outputs/social/gallery.html      # Windows: start  ·  Linux: xdg-open
```

✅ **Expected:** Three platform cards, each with its image, copy and hashtags.

### 7. Review like the founder: APPROVE, EDIT or REJECT (10 min)
Check every post against brand-guide.md and compliance-rules.md: price SGD 6.80, launch 1 Dec 2026, SHIOK20 terms if the code appears, no health or halal claims, no competitor bashing. Send one post back with a concrete edit — the writer reworks it and the gallery updates.

```bash
hermes kanban list --tenant kopi-social
hermes kanban complete <human_card_id>     # after you have checked the refreshed gallery
```

**Prompt** — paste into *Hermes Desktop → default profile (Mia)*:

```text
My decisions for the kopi-social posts:
- LinkedIn: APPROVE
- Facebook: EDIT - put the first pop-up date in the first line and cut the post to 80 words
- Instagram: APPROVE
Create a rework card for the facebook-writer with my edit as its body and the image creator's card as parent, then a card for the image-creator to refresh the gallery. Record every decision with date and reason in outputs/social/approval-log.md. Leave my HUMAN card open: I complete it myself.
```

✅ **Expected:** A rework card runs; gallery.html shows the edited Facebook post; approval-log.md has three rows.

### 8. Reflect: team versus one agent (5 min)
Compare the team with Mia working alone on Day 1.

**Prompt** — paste into *Hermes Desktop → default profile (Mia)*:

```text
Compare today's five-profile team with you working alone: time to first draft, how different the three posts sound, number of my edits, and coordination overhead. Give me a 5-row table and one recommendation: when should Kopi Kaki use a team, and when one agent?
```

✅ **Expected:** A short evidence-based comparison you can discuss in class.

## Verification / checkpoint
- [ ] `hermes profile list` shows the five team profiles
- [ ] The board shows parents: writers ← research; images ← all three writers; HUMAN ← images
- [ ] gallery.html shows three platform posts with images
- [ ] approval-log.md records a decision for every post; nothing was posted publicly

**Checkpoint:** The board shows five owners, writers blocked on research, the image creator blocked on the writers, and every post in approval-log.md has your decision.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Cards stay in Ready and never run | The gateway dispatches Kanban work: run `hermes gateway status` and start it (`hermes gateway run`). |
| A profile cannot reach the model | Recreate it with --clone or run `hermes -p <profile> model` to pick the provider. |
| Image tool fails | Install Pillow in the workspace venv: `.office-venv/bin/python -m pip install Pillow`. |
| A writer invents a price or promo | Point it at product-catalogue.csv and campaign-brief.md in a rework card; add the rule to its SOUL.md. |

## Stretch challenge
Add a sixth profile, tiktok-writer, as a card that depends on research. What did the extra specialist cost in time and review effort, and was it worth it?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
