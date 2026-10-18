# Lab 2 — End-to-End Social Media Campaign with One Agent

**Day 1 · Topic 2 · 60 min · Single agent + skills · LO1**

> Give the agent two company skills and one tool chain, and turn the brief into a complete, dated, on-brand multi-platform campaign — then improve it with your feedback.

## Goal
Analyse the capabilities and limitations of an LLM agent on an end-to-end marketing workflow, and how skills, tools and instructions shape its output (LO1).

## The business scenario
With the angle chosen, you need a campaign: strategy, a 14-day content calendar across Instagram, TikTok, Facebook and LinkedIn, captions in the Kopi Kaki voice, visuals and tracking links. Instead of a long prompt you give Mia two skills — the company's brand-voice skill and a campaign-planner skill — so the work is repeatable and self-checked.

## You will deliver
- outputs/lab02/campaign-plan.md — strategy, pillars, phases, KPIs, budget split
- outputs/lab02/content-calendar.csv — ≥ 16 dated posts with UTM links
- outputs/lab02/captions.md — captions with a compliance self-check per post
- outputs/lab02/images/ — 3 hero visuals (or image prompts if no image tool)
- A revised v2 after your feedback

## Who does what
- **Agents:** 1 Hermes agent (Mia) + 2 custom skills + image tool
- **You (the human):** Review the draft, give concrete feedback, accept v2

## Before you start
- Lab 1 complete: Hermes installed, ~/kopi-kaki workspace, the angle you chose saved in memory
- Optional: an image-generation backend (paid Nous Portal plan or a FAL_KEY)

## Concepts in action
- Skills = procedural memory: a SKILL.md the agent loads on demand
- Tools = actions: file write, web search, image generation
- Self-check inside the skill = built-in verification step of the agentic loop
- Human feedback → revision = instructor–executor collaboration

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `templates/content-calendar-template.csv` | Template |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `skills/social-campaign-planner/SKILL.md` | Agent skill (SKILL.md) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-02-Instructions.pdf`](LAB-02-Instructions.pdf).

## Steps

### 1. Install the two company skills
Skills live in `~/.hermes/skills/`. Copy the two skill folders from this lab's data into a `marketing` category, then confirm Hermes can see them. (Optional: also install the official social-media-content-calendar skill.)

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/kopi-kaki/outputs/lab02/images ~/.hermes/skills/marketing
cp -R ~/kopi-kaki/skills/* ~/.hermes/skills/marketing/
hermes skills list | grep -E "kopi-brand-voice|social-campaign-planner"
# optional: hermes skills install official/creative/social-media-content-calendar
```

✅ **Expected:** Both skills appear in the list.

### 2. Read a skill before you trust it
Open `~/.hermes/skills/marketing/kopi-brand-voice/SKILL.md`. Notice the frontmatter `description` (when the agent should load it), the steps, and the self-check table. A skill is a contract you can review — like an SOP for a new hire.

```bash
cat ~/.hermes/skills/marketing/kopi-brand-voice/SKILL.md
```

### 3. Build the campaign plan and calendar
**Prompt** — paste into *Hermes chat in ~/kopi-kaki*:

```text
Use the social-campaign-planner skill to build the #ShiokColdBrew campaign from campaign-brief.md, using the angle I chose in Lab 1 (check your memory).
Scope: teaser (17-23 Nov) and pre-order push (24-30 Nov) phases, Instagram, TikTok, Facebook and LinkedIn.
Deliver:
- outputs/lab02/campaign-plan.md
- outputs/lab02/content-calendar.csv with at least 16 posts (use the columns in the skill)
- outputs/lab02/captions.md with every caption checked by the kopi-brand-voice skill
End with a 5-line summary of decisions you need from me.
```

✅ **Expected:** Three files in outputs/lab02 and a decisions summary.

### 4. Create the hero visuals
**Prompt** — paste into *Hermes chat*:

```text
Create 3 hero visuals for the teaser posts using your image generation tool: square 1:1, brand colours (kopi brown #5B3A29, pandan green #4E8A3E, cream #F6EBD9, gula melaka amber #C7782A), natural light, a glass of iced cold brew with a gula melaka drizzle, kopitiam tiles, no people's faces, no text in the image. Save them to outputs/lab02/images/ and add the file names to content-calendar.csv. If you have no image tool, write the 3 prompts to outputs/lab02/images/prompts.md instead.
```

✅ **Expected:** 3 PNGs (or a prompts file) linked from the calendar.

### 5. Human review — give concrete, testable feedback
Open the calendar in a spreadsheet and the captions in a viewer. Vague feedback ('make it better') produces vague revisions. Give specific, checkable changes — for example:

**Prompt** — paste into *Hermes chat*:

```text
Review feedback for v2:
1. TikTok hooks are weak - rewrite every TikTok caption to open with a question in under 8 words.
2. LinkedIn must not mention SHIOK20 - make the LinkedIn posts about our roasting team and heritage.
3. Add one post per phase aimed at students (18-24).
Apply the changes, re-run the kopi-brand-voice self-check on every changed caption, save as content-calendar-v2.csv and captions-v2.md, and list exactly what changed.
```

✅ **Expected:** v2 files plus a change log; changed captions all PASS.

### 6. Measure efficiency — what did the skills save?
Ask the agent to report its own work so you can relate design to efficiency (this is the LO2 analysis you will use in the assessment).

**Prompt** — paste into *Hermes chat*:

```text
Report: how many posts, captions and images you produced; how many self-check FAILs you found and fixed before showing me; and which parts of the work the two skills standardised. Then estimate how long the same work would take one human marketer.
```

✅ **Expected:** A short efficiency report you can quote.

## Verification / checkpoint
- [ ] campaign-plan.md, content-calendar(-v2).csv and captions(-v2).md exist in outputs/lab02
- [ ] ≥ 16 posts across 4 platforms with UTM links; LinkedIn has no promo code
- [ ] Each caption has a PASS self-check table

**Checkpoint:** Every caption carries a PASS self-check; no health/halal claims; SHIOK20 always shows its terms.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skill not listed | Check the path is ~/.hermes/skills/marketing/<skill>/SKILL.md and start a new session (`/new`) — skills and memory load at session start. |
| No images generated | Image generation runs through FAL.ai: either a paid Nous Portal plan (Tool Gateway) or your own FAL_KEY (`hermes config set FAL_KEY ...`), selected in `hermes tools`. The prompts.md fallback is acceptable. |
| CSV columns shift | Ask the agent to quote every caption field and re-save with UTF-8 encoding. |

## Stretch challenge
Ask Mia to turn your three review comments into permanent rules by patching the kopi-brand-voice skill ("update the skill so this mistake never happens again") — that is harness engineering in one sentence.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
