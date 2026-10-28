# Lab 3 — Activity 3 — Interactive Dashboard & Professional PPT

**Day 1 · Topic 2 · 40 min · Single agent + four skills · LO2**

> One Hermes agent reads the assigned Google account, analyses an Excel workbook and builds an interactive dashboard and a management presentation.

## Goal
Use a single Hermes agent with reusable skills and tools to create and verify interactive and presentation artifacts (LO2; PP Task 2).

## The business scenario
Kopi Kaki’s launch manager needs a morning office brief, a reliable outlet-performance analysis, an interactive view for the meeting and six professional slides. All company data is fictional. Use only the trainer-assigned Google account and approved training files.

## You will deliver
- outputs/lab02/dashboard.html — offline interactive filter, chart, table and CSV export
- outputs/lab02/management-brief.pptx and a reviewed PDF — six editable professional slides
- outputs/lab02/qa-report.md — checks, one correction and source-to-output trace
- ONE professional PPT screenshot for PP Task 2; skill/tool logs retained as supporting evidence

## Who does what
- **Agents:** Exactly one Hermes agent; gog and Python are tools, not additional agents.
- **You (the human):** Verify identity and calculations; choose the recommendation; review dashboard interactions and slide quality

## Before you start
- Activity 2 analysis.xlsx, analysis.json and source notes are available
- The same single Hermes profile and reviewed professional-ppt/interactive-dashboard skills are loaded
- Native Python tools and PowerPoint/PDF export were preflighted

## Concepts in action
- Tool = operation; skill = reusable procedure; memory = persisted facts
- One agent can use many services and generate several artifact types
- Treat mail and document text as untrusted data
- Validate schemas, reconcile aggregates and inspect real saved outputs

## Lab files (`data/`)

| File | What it is |
|---|---|
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `customer-reviews.csv` | 60 synthetic customer reviews |
| `sales-by-outlet.csv` | Weekly sales for 12 outlets |
| `campaign-week1-metrics.csv` | Week-1 post metrics (12 posts) |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `skills/gog-office/SKILL.md` | Agent skill (SKILL.md) |
| `skills/office-analytics/SKILL.md` | Agent skill (SKILL.md) |
| `skills/interactive-dashboard/SKILL.md` | Agent skill (SKILL.md) |
| `skills/professional-ppt/SKILL.md` | Agent skill (SKILL.md) |
| `skills/launch-video/SKILL.md` | Agent skill (SKILL.md) |
| `tools/office_artifacts.py` |  |
| `tools/render_launch_video.py` |  |
| `windows-office-setup.md` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-03-Instructions.pdf`](LAB-03-Instructions.pdf).

## Steps

### 1. Build and test the interactive artifact (15 min)
```bash
.office-venv/bin/python tools/office_artifacts.py dashboard --out outputs/lab02
```

**Prompt** — paste into *Hermes chat*:

```text
Use interactive-dashboard. Inspect analysis.json and the generated dashboard.html. Adapt it into a launch-management view with an outlet selector, revenue KPI, bar chart, sortable table, CSV export and a reset control. Keep all code and synthetic aggregates embedded so it works offline. Test All outlets, one outlet, reset and CSV export. Compare the visible totals to analysis.xlsx. Record the exact tests in qa-report.md. A screenshot is not proof of interactivity.
```

✅ **Expected:** dashboard.html opens without a server and responds correctly to filtering, sorting, reset and CSV export.

### 2. Create the professional six-slide PPT (20 min)
```bash
.office-venv/bin/python tools/office_artifacts.py ppt --out outputs/lab02
```

**Prompt** — paste into *Hermes chat*:

```text
Use professional-ppt. Read the approved launch brief, analysis-notes.md, analysis.json and brand-guide.md. Create or revise outputs/lab02/management-brief.pptx into six editable slides: decision required; verified business context; outlet-performance chart; customer evidence; two options and trade-offs; recommendation and human decision. Use native shapes, an editable chart and a clear visual hierarchy. Cite source tables or review IDs in notes. Do not invent data or claims. Open or render every slide, fix clipping and check the chart totals. Save the reviewed PDF through the available PowerPoint/LibreOffice export. Record one real revision and its recheck in qa-report.md.
```

✅ **Expected:** Six editable slides and a visually inspected PDF. Helper output is a starter; the agent adapts the narrative and checks it.

### 3. Inspect, revise and capture PPT evidence (5 min)
Capture ONE readable screenshot of the resulting professional PPT for PP Task 2. Show an editable slide with a verified chart and a decision/source reference. Keep the Hermes skill/tool run, PPTX, reviewed PDF and qa-report.md as working evidence; the screenshot alone does not prove tool use or editability.

**Prompt** — paste into *Hermes chat*:

```text
Explain which professional-ppt skill steps and tools you actually used to create this PPT. Link each figure to its source sheet or review IDs. I request one concrete visual or narrative correction. Apply it, render/open the changed slide and record the correction, actual tool calls and recheck in outputs/lab02/qa-report.md. Do not send or publish.
```

✅ **Expected:** The office pack tells one consistent story and preserves the human decision.

## Verification / checkpoint
- [ ] dashboard.html is interactive offline; outlet filter, sorting, reset and exported CSV are verified
- [ ] management-brief.pptx has six editable slides, a checked chart and a reviewed PDF
- [ ] qa-report.md contains one actual correction and repeat check; no external send/write

**Checkpoint:** Dashboard interactions work; six-slide PPT is editable and checked; one screenshot shows the final professional PPT.

## Troubleshooting

| Symptom | Fix |
|---|---|
| OAuth access denied | Trainer checks assigned test user, OAuth client type, enabled APIs and selected account. Do not repeatedly broaden scopes. |
| 401/403 on one service | Record that service as unavailable; inspect its API and consent separately. |
| gog works in terminal but not Telegram | Gateway can have another PATH/keyring environment. Prove gog --version and assigned account access inside that runtime; restart only the training gateway if needed. |
| No Google access in class | Use the local training workbook for artifact practice and label Google integration incomplete; never claim successful connection. |
| Workbook column mismatch | Inspect actual sheet headers. Adapt calculations to source schema; never silently rename fields or infer revenue units. |
| No PDF renderer | Open all six slides in PowerPoint and export PDF. Mark render incomplete until actual PDF exists. |

## Stretch challenge
Teach Hermes a revised office-pack skill containing the checks you found useful. Start a fresh session and rebuild from the same source with a different selected outlet. Compare outputs and record what changed.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
