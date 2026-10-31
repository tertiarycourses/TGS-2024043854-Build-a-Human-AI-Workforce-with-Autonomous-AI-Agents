# Lab 4 — Activity 4 — Your Social Media Team: Five Bots in One Group Chat

**Day 2 · Topic 3 · 60 min · Multiple named bots in one group chat · LO2**

> Hire five bots with names and job titles, put them in one group chat, and post one brief. They hand off by @mention; you approve every post.

## Goal
Design a multi-agent team of named bots with clear roles, coordinate them in a group chat with a human approval step, and compare its output and effort with a single agent (LO2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. Two weeks to launch. LinkedIn needs a founder story for investors and corporate catering buyers, Facebook needs the neighbourhood and the pop-up dates, Instagram needs a scroll-stopping image. One agent writing all three sounds the same everywhere, so you hire a team of bots: each specialist owns one platform, they talk in one group chat, and you approve every post before anything goes public.

## You will deliver
- Five bots created with New Agent: Rafi (researcher), Lin (LinkedIn), Farah (Facebook), Ivy (Instagram), Pixel (images)
- A group chat 'Kopi Social Team' where the bots hand off by @mention and ask you (@user) for decisions
- outputs/social/research.md, linkedin.md, facebook.md, instagram.md and images/*.png
- outputs/social/gallery.html — every post shown as it would appear on its platform
- outputs/social/approval-log.md — APPROVE / EDIT / REJECT per post

## Who does what
- **Agents:** 5 named bots in one group chat: Rafi → Lin, Farah, Ivy → Pixel
- **You (the human):** Post the brief, approve or edit each post; nothing is posted publicly

## Before you start
- Topic 2 setup done: Hermes Desktop with a working model; Telegram connected
- Activity 2 website and Activity 3 deck saved — the team reuses their facts
- This lab's data/ dragged into Desktop/kopi-kaki (souls/ holds the five role files; tools/make_post_image.py makes the images)

## Concepts in action
- A bot = a separate agent with its own name, role, instructions, memory and skills
- A group chat lets bots talk to each other: @mention hands work to a teammate, @user asks you
- Specialists + one human decision beat one generalist for multi-channel work
- Hard caps (3 rounds, 10 messages per send) keep a room from spinning

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company rulebook: attach this folder with + → Folder… and tell Mia to follow it |
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
| `souls/rafi.SOUL.md` | Role + rules for one studio profile |
| `souls/lin.SOUL.md` | Role + rules for one studio profile |
| `souls/farah.SOUL.md` | Role + rules for one studio profile |
| `souls/ivy.SOUL.md` | Role + rules for one studio profile |
| `souls/pixel.SOUL.md` | Role + rules for one studio profile |
| `tools/make_post_image.py` | Offline on-brand image tool (Pillow) |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-04-Instructions.pdf`](LAB-04-Instructions.pdf).

## Steps

### 1. Copy the team files into your company folder (3 min)
In Finder (Mac) or File Explorer (Windows), open this lab's data folder from the unzipped course files, select everything and drag it into your Desktop/kopi-kaki folder. Choose Skip (do not replace) for files that already exist. Then in Hermes Desktop click + (left of Ask anything) → Folder… and choose Desktop/kopi-kaki: Mia now has this lab's files and AGENTS.md. Start the session with: 'Read AGENTS.md in the attached folder and follow it for this session.' souls/ holds one role file per bot: who it is, what it writes and the rules it must never break.

✓ **Expected:** souls/ lists rafi, lin, farah, ivy and pixel .SOUL.md files.

### 2. Hire five bots with New Agent (12 min)
Open the Bots tab (next to Sessions) and click New Agent. For each bot fill in Name, Title and Description below, open Advanced → Custom SOUL.md and paste the text of its souls/<name>.SOUL.md file, then create it. Each bot introduces itself in its own Bot Chat. Right-click a bot → Edit Profile to give it an avatar (Bot, Generate, Upload or a Pet).
- Rafi · Market Researcher · Finds launch angles, audience insights and facts for Kopi Kaki posts; cites the source file for every fact.
- Lin · LinkedIn Writer · Writes the founder's LinkedIn post: story, one proof point, call to action; professional Singapore English.
- Farah · Facebook Writer · Writes the neighbourhood Facebook post: pop-up dates, the 1 Dec opening, friendly kopitiam voice.
- Ivy · Instagram Writer · Writes the Instagram hook, caption and hashtags, plus a one-line image brief.
- Pixel · Image Creator · Makes one on-brand 1080x1350 image per post and the review gallery that shows every post as it will look.

✓ **Expected:** Rafi, Lin, Farah, Ivy and Pixel appear in the Bots roster, each with its own title.

### 3. Meet your team (5 min)
Click each bot to open its Bot Chat and check that it answers in its own role. If a bot says it has no model, open Settings → Model, pick that bot under 'Applies to', choose your provider, sign in and Apply.

**Prompt** — paste into *Hermes Desktop → Bots tab → Rafi (then Lin)*:

```text
Hi, I'm the founder of Kopi Kaki Co. In two sentences: what is your job on my marketing team, and which files in my Desktop/kopi-kaki folder will you read first?
```

✓ **Expected:** Each bot describes its own role and names AGENTS.md, campaign-brief.md and brand-guide.md.

### 4. Put the team in one group chat (5 min)
Right-click Rafi → Manage groups → create a group called 'Kopi Social Team' inline, then add Lin, Farah, Ivy and Pixel the same way (a group holds 2–6 bots). Click the group row → Open chat. In a group, your message starts up to three rounds of bot turns; bots hand work to each other with @name and ask you with @user.

✓ **Expected:** The roster shows 'Kopi Social Team · 5 bots'; the room opens with all five members.

### 5. Post the brief and watch them hand off (15 min)
One message briefs the whole team. Rafi researches first; the three writers start when Rafi hands off. Watch the room: who speaks, who passes, who asks you.

**Prompt** — paste into *Hermes Desktop → Kopi Social Team (group chat)*:

```text
Team, we launch the Gula Melaka Cold Brew on 1 Dec 2026. Work in Desktop/kopi-kaki and follow AGENTS.md, brand-guide.md and compliance-rules.md.
@rafi research first: write outputs/social/research.md with 3 launch angles, the top 3 things tasters loved (with review IDs) and 5 approved facts with their source file. Then hand off to @lin @farah @ivy.
@lin write outputs/social/linkedin.md, @farah write outputs/social/facebook.md, @ivy write outputs/social/instagram.md — each from research.md and your own role file.
Never post anything. If you are unsure about a fact, ask me with @user.
```

✓ **Expected:** research.md first, then three platform drafts; anything uncertain comes to you as an @user question.

### 6. Ask Pixel for the images and the gallery (8 min)
Pixel makes one image per post with the small image tool in your folder and builds one page that shows every post the way it would look on its platform.

**Prompt** — paste into *Hermes Desktop → Kopi Social Team*:

```text
@pixel make one 1080x1350 image for each of linkedin.md, facebook.md and instagram.md with tools/make_post_image.py (Python from .office-venv), save them in outputs/social/images/, then build outputs/social/gallery.html with one card per platform and open it for me.
```

✓ **Expected:** gallery.html opens: three platform cards, each with its image, copy and hashtags.

### 7. Review like the founder: APPROVE, EDIT or REJECT (8 min)
Check every post against brand-guide.md and compliance-rules.md: price SGD 6.80, launch 1 Dec 2026, SHIOK20 terms if the code appears, no health or halal claims, no competitor bashing. Send one post back with a concrete edit.

**Prompt** — paste into *Hermes Desktop → Kopi Social Team*:

```text
My decisions:
- LinkedIn: APPROVE
- Facebook: EDIT — @farah put the first pop-up date in the first line and cut the post to 80 words
- Instagram: APPROVE
@pixel when Farah is done, refresh the gallery and record every decision with today's date and my reason in outputs/social/approval-log.md.
```

✓ **Expected:** Farah revises; the gallery shows the edited Facebook post; approval-log.md has three rows.

### 8. Reflect: team versus one agent (4 min)
Compare the bots with Mia working alone in Activities 2 and 3.

**Prompt** — paste into *Hermes Desktop → Mia (your first session)*:

```text
Compare today's five-bot group chat with you working alone on Day 1: time to first draft, how different the three posts sound, number of my edits, and coordination overhead. Give me a 5-row table and one recommendation: when should Kopi Kaki use a group of bots, and when one agent?
```

✓ **Expected:** A short evidence-based comparison you can discuss in class.

## Verification / checkpoint
- [ ] Five bots in the roster with names, titles and role files
- [ ] The group 'Kopi Social Team' shows the hand-off: research → three writers → images
- [ ] gallery.html shows three platform posts with images
- [ ] approval-log.md records a decision for every post; nothing was posted publicly

**Checkpoint:** The group chat shows Rafi's research first, three platform drafts, Pixel's gallery, and every post in approval-log.md has your decision.

## Troubleshooting

| Symptom | Fix |
|---|---|
| A bot has no model | Settings → Model → pick the bot under 'Applies to' → choose the provider, sign in, Apply. |
| Nobody answers in the group | @mention the bot you want (@rafi …). A message with no mention lets each bot decide whether to speak. |
| The room stops after three rounds | That is the safety cap. Send a short follow-up: '@lin @farah @ivy please continue from research.md'. |
| Image tool fails | Ask Mia in your own session: 'Install Pillow into .office-venv in Desktop/kopi-kaki.' |
| A writer invents a price or promo | Reply '@<writer> use only product-catalogue.csv and campaign-brief.md' and add the rule to its role file (Edit Profile → SOUL.md). |

## Stretch challenge
Hire a sixth bot, Tash the TikTok Writer, add her to the group and ask for a 15-second script. What did the extra specialist cost in time and review effort, and was it worth it?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
