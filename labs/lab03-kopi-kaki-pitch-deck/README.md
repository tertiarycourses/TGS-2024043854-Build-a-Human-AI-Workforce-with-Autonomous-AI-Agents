# Lab 3 — Activity 3 — PPT Tool + Skill Build the Kopi Kaki Pitch Deck

**Day 1 · Topic 2 · 45 min · One agent + PPT tool and skill · LO2**

> On Friday you pitch the bank for a SGD 50,000 loan. Mia turns your brief, reviews and competitors into a professional, editable deck — with a real chart.

## Goal
Use a presentation tool and a reviewed skill with one agent to produce a professional, editable deck; verify its facts and design before you accept it (LO2; PP Task 2).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. To open the flagship you need working capital, so you are pitching a bank relationship manager on Friday. You give Mia the campaign brief, the 60 tasting reviews from the pop-ups and the competitor list, plus a PPT tool and a presentation skill. She builds the deck; you check every number and approve it.

## You will deliver
- outputs/deck/kopi-kaki-pitch.pptx — 8–10 editable slides with one native chart
- outputs/deck/kopi-kaki-pitch.pdf — rendered copy you reviewed slide by slide
- outputs/deck/qa-report.md — facts checked against the source files, fixes made
- PP Task 2 evidence: ONE screenshot of Hermes Desktop/dashboard showing the PPT run and the deck

## Who does what
- **Agents:** 1 Hermes agent (Mia) with the PPT tool and presentation skill
- **You (the human):** Set the story, check every figure, approve the final deck

## Before you start
- Topic 2 setup and Activity 2 done
- python-pptx in ~/kopi-kaki/.office-venv (from the setup step)
- LibreOffice for the PDF render (`soffice --version`)
- This lab's data/ copied into ~/kopi-kaki

## Concepts in action
- Tool = does the work (python-pptx writes the file); skill = how to do it well (structure, design rules)
- A deck is a decision story: problem → product → proof → plan → ask
- Content errors and layout errors are different defects: check both

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
| `skills/kopi-pitch-deck/SKILL.md` | Agent skill (SKILL.md) |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-03-Instructions.pdf`](LAB-03-Instructions.pdf).

## Steps

### 1. Copy the deck skill and check the PPT tool (3 min)
The tool writes the file (python-pptx); the skill says how to build a good deck. Hermes also ships a built-in microsoft-office skill (Word, PowerPoint, Excel via python-pptx); the reviewed kopi-pitch-deck skill adds your story, brand and checks.

```bash
cp -Rn data/* ~/kopi-kaki/
cat ~/kopi-kaki/skills/kopi-pitch-deck/SKILL.md
mkdir -p ~/.hermes/skills/office && cp -R ~/kopi-kaki/skills/kopi-pitch-deck ~/.hermes/skills/office/
~/kopi-kaki/.office-venv/bin/python -c "import pptx; print('python-pptx', pptx.__version__)"
hermes skills list | grep -i -E 'kopi-pitch-deck|microsoft-office'
soffice --version
```

✅ **Expected:** kopi-pitch-deck is listed; python-pptx prints its version.

### 2. Optional: add a hub PPT skill (3 min)
For comparison, Hermes's optional pptx-author skill (adapted from Anthropic's) builds decks headless with python-pptx.

```bash
hermes skills install official/finance/pptx-author
```

### 3. Brief the deck (15 min)
Start a new Desktop chat in ~/kopi-kaki. This is the run you will screenshot for PP Task 2.

**Prompt** — paste into *Hermes Desktop — Mia, folder ~/kopi-kaki*:

```text
Use the kopi-pitch-deck skill and python-pptx (~/kopi-kaki/.office-venv/bin/python). Build the Kopi Kaki Co. pitch deck for Friday's meeting with a bank relationship manager.
- 8-10 slides: title · the problem · Gula Melaka Cold Brew (SGD 6.80, from 1 Dec 2026) · proof from the 60 pop-up tasting reviews (average rating and top themes with review IDs) · market and the 6 competitors · launch plan 17 Nov-14 Dec #ShiokColdBrew · KPIs (2,500 pre-orders, 8% engagement, 40,000 views) · budget SGD 15,000 · the ask (I will fill in the amount).
- One NATIVE editable chart (ratings distribution or KPI targets), brand colours from brand-guide.md, the logo on the title slide.
- Speaker notes: the source file for every number.
Save outputs/deck/kopi-kaki-pitch.pptx, render outputs/deck/kopi-kaki-pitch.pdf with soffice, check every page for clipping or overlap, and write outputs/deck/qa-report.md.
```

✅ **Expected:** kopi-kaki-pitch.pptx, the PDF and qa-report.md in outputs/deck/.

### 4. Check it: content errors and layout errors (8 min)
Open the PDF and the PPTX. Content error = a wrong or unsourced number. Layout error = clipped, overlapping or unreadable text. Check three numbers against the source files yourself and click the chart to confirm it is editable.

```bash
open ~/kopi-kaki/outputs/deck/kopi-kaki-pitch.pdf
open ~/kopi-kaki/outputs/deck/kopi-kaki-pitch.pptx
cat ~/kopi-kaki/outputs/deck/qa-report.md
```

### 5. One revision, then approve (8 min)
Ask for a concrete, testable change, then approve the deck.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Revise the deck: (1) make slide 2's headline state the problem in one sentence; (2) on the reviews slide show the average rating as one big number with the review count; (3) the ask slide: 'SGD 50,000 working capital for the Tiong Bahru flagship'. Re-render the PDF, re-check every page, and add the changes to qa-report.md. Then summarise what changed.
```

✅ **Expected:** Updated PPTX, PDF and qa-report.md.

### 6. Capture your PP Task 2 evidence (3 min)
Take ONE readable screenshot of Hermes Desktop (or the Hermes dashboard) showing your request and the finished deck — for example the chat with the saved .pptx path and the slides open beside it. Hide keys and private data. Keep the .pptx, the PDF and qa-report.md.

## Verification / checkpoint
- [ ] kopi-pitch-deck skill listed; python-pptx works
- [ ] 8-10 editable slides with one native chart
- [ ] Three numbers checked by you against the source files
- [ ] PDF has no clipped or overlapping text; qa-report.md lists fixes
- [ ] PP Task 2: ONE Hermes Desktop/dashboard screenshot showing the PPT run and the deck

**Checkpoint:** The .pptx opens and is editable, the chart is a native chart, every number matches the source files, and your PP Task 2 screenshot is saved.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `soffice: command not found` | Install LibreOffice (macOS: brew install --cask libreoffice) or open the .pptx and export PDF yourself. |
| Chart is a picture | Ask Mia to use python-pptx chart_data / add_chart so the chart stays editable. |
| Invented figures | Point Mia at the source files and the skill rule 'never invent figures'; ask for a sourced revision. |

## Stretch challenge
Ask Mia to turn the same deck into a one-page investor memo (DOCX) with the microsoft-office skill. Which format would the bank manager read first?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
