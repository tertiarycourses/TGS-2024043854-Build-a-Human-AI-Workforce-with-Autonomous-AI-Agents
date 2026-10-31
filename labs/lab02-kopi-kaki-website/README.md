# Lab 2 — Activity 2 — One Agent Builds the Kopi Kaki Website with UX Skills

**Day 1 · Topic 2 · 45 min · Single agent + installed UX skills · LO2**

> A startup without a website does not exist. Ask Mia to install two UX skills from skills.sh, then let her design, build and test your one-page site in 45 minutes.

## Goal
Install third-party UX skills after reviewing their source, use them to brief a single agent, and judge the result against the brand guide (LO2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. Customers who taste the cold brew at a pop-up search for you that evening — and find nothing. You need a one-page site before the flagship opens: hero, menu, the 1 Dec launch, pop-up locations and an app pre-order button. You have no designer, so you install design skills and brief Mia like an agency.

## You will deliver
- outputs/website/index.html — responsive one-page Kopi Kaki site (hero, menu, launch, pop-ups, pre-order CTA)
- outputs/website/review.md — your design review: what the skill changed, what you corrected
- Two screenshots: desktop and mobile widths

## Who does what
- **Agents:** 1 Hermes agent (Mia) with UX skills from skills.sh
- **You (the human):** Brief the site, review the design against the brand guide, request one revision

## Before you start
- Topic 2 setup done: Mia works in your kopi-kaki folder
- This lab's data/ dragged into Desktop/kopi-kaki

## Concepts in action
- A skill is reusable know-how in a SKILL.md: install it once, every task benefits
- Read a third-party skill before you install it
- Brief an agent like an agency: audience, sections, brand, constraints, definition of done

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `website-brief.md` | One-page website brief |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-02-Instructions.pdf`](LAB-02-Instructions.pdf).

## Steps

### 1. Copy the website brief into your company folder (2 min)
In Finder (Mac) or File Explorer (Windows), open this lab's data folder from the unzipped course files, select everything, and drag it into your Desktop/kopi-kaki folder. If asked about files that already exist, choose Skip (do not replace). The brief says who the site is for, the sections, the brand and the definition of done.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Read website-brief.md and tell me in three lines what you will build, for whom, and how we will know it is done.
```

✓ **Expected:** Three lines that match the brief.

### 2. Choose UX skills on skills.sh (5 min)
Open skills.sh in your browser and search 'frontend' and 'design'. The most installed design skills include Anthropic's frontend-design (about 1.1 million installs), Vercel's web-design-guidelines and ui-ux-pro-max. Open each skill's page and read its SKILL.md: what will it make the agent do, and does it run any scripts?

✓ **Expected:** You can explain in one sentence what each skill changes.

### 3. Ask Mia to install two UX skills (5 min)
No command line: Mia installs the skills for herself. Afterwards they appear in Capabilities → Skills.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Install these two skills from skills.sh for yourself: frontend-design from github.com/anthropics/skills and web-design-guidelines from github.com/vercel-labs/agent-skills. Read each SKILL.md first and tell me whether it runs any scripts. Then confirm both are installed and available.
```

✓ **Expected:** Both skills installed and listed in Capabilities → Skills.

### 4. Brief Mia like a design agency (15 min)
Start a New session in your kopi-kaki folder so the new skills load.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Use the frontend-design and web-design-guidelines skills. Build the Kopi Kaki Co. one-page website from website-brief.md.
- Sections: hero (Gula Melaka Cold Brew, SGD 6.80, from 1 Dec 2026), our story (a startup founded in 2026), menu from product-catalogue.csv, pop-ups and the Tiong Bahru flagship, three short taster quotes from customer-reviews.csv (no names), app pre-order button, footer.
- Brand: colours and voice from brand-guide.md; use assets/kopi-kaki-logo.png and assets/cold-brew-product-card.png.
- One self-contained outputs/website/index.html: inline CSS, no external libraries or fonts, responsive down to 375 px, accessible contrast.
- No health or halal claims. Every price and date must match the source files.
When done, open the page in my browser, then list which skill rules you applied and every fact with its source file.
```

✓ **Expected:** outputs/website/index.html opens in your browser, plus a list of applied rules and sourced facts.

### 5. Check it like a customer (5 min)
Look at the page Mia opened (or double-click outputs/website/index.html in your kopi-kaki folder). Narrow the browser window to phone width. Check the price, the date, the pop-up information and the button.

✓ **Expected:** The hero shows Gula Melaka Cold Brew, SGD 6.80 and 'Pouring from 1 Dec 2026'; the page still works at phone width.

### 6. Ask for one concrete revision (8 min)
Give feedback an agent can test, not 'make it nicer'.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Revise outputs/website/index.html: (1) move the pre-order button into the hero, visible without scrolling on a 375 px phone; (2) make the menu a two-column grid on desktop and one column on phone; (3) add the pop-up dates as a simple list. Then write outputs/website/review.md: what the skills changed, my requested fixes, and the checks you ran.
```

✓ **Expected:** Updated page and review.md.

### 7. Capture your website (2 min)
Save two screenshots — desktop and phone width — into outputs/website/. You will reuse the site's facts in the pitch deck and the social posts.

## Verification / checkpoint
- [ ] Two UX skills installed and listed in Capabilities → Skills
- [ ] index.html opens offline with the Kopi Kaki colours, logo and product card
- [ ] Every price and date matches the source files
- [ ] Works at 375 px; review.md records your revision

**Checkpoint:** index.html opens offline, uses the Kopi Kaki colours and facts, works at phone width, and review.md records your one requested change.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skill install fails | Ask Mia what failed and to try the Hermes skills hub instead; or search the skill in Capabilities → Skills and click Install. |
| Skill not used | Start a New session so newly installed skills load; name the skill in the prompt. |
| Images missing | Check assets/ was dragged into your kopi-kaki folder and ask Mia to use relative paths. |

## Stretch challenge
Ask Mia to install ui-ux-pro-max as a third skill and make a second design. Which design would you ship, and what did the extra skill actually change?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
