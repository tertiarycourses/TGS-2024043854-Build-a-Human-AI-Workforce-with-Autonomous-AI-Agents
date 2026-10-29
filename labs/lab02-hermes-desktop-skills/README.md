# Lab 2 — Activity 2 — Hermes Desktop, Tools, Skills & the Company Brief

**Day 1 · Topic 2 · 90 min · Single agent · LO1**

> Meet Kopi Kaki at the start of the company labs; onboard one Hermes office worker.

## Goal
Install Hermes Desktop, load reviewed office/video skills, verify tools and produce the source-linked company brief (LO1/LO2).

## The business scenario
You are Kopi Kaki Co.'s Marketing Lead. The Gula Melaka Cold Brew launches on 1 Dec and you have 60 unread customer reviews, a competitor list and no analyst. You 'hire' Mia — a Hermes Agent marketing analyst — onboard her with the company context, and ask for a research brief that tells you which campaign angle to run.

## You will deliver
- outputs/lab01/review-insights.md — ratings, themes and evidence (review IDs)
- outputs/lab01/research-brief.md — trends, competitors, 3 campaign angles with evidence
- Mia's long-term memory holds the brand facts and YOUR chosen angle (recalled in a new session)
- Skill installation and tool-version evidence for gog-office, office-analytics, interactive-dashboard, professional-ppt and launch-video

## Who does what
- **Agents:** 1 Hermes agent — 'Mia', AI marketing analyst
- **You (the human):** Set the goal, challenge the evidence, choose the campaign angle

## Before you start
- Download the official Hermes Desktop installer for your OS: https://hermes-agent.nousresearch.com/desktop
- Trainer-approved model access, preflighted native Python, gog, FFmpeg and PPT/PDF renderer
- Approved course skills/data downloaded; preserve existing AGENTS.md; do not copy credentials into the workspace

## Concepts in action
- Perception (files + web) → Brain (LLM reasoning, memory) → Action (write files)
- AGENTS.md = context the agent loads automatically (context engineering)
- Short-term memory (this session) vs long-term memory (MEMORY.md, recalled next session)
- Human-in-the-loop: the agent recommends, the human decides

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `customer-reviews.csv` | 60 synthetic customer reviews |
| `competitors.csv` | 6 fictional competitors |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `campaign-data.xlsx` |  |
| `skills/gog-office/SKILL.md` | Agent skill (SKILL.md) |
| `skills/office-analytics/SKILL.md` | Agent skill (SKILL.md) |
| `skills/interactive-dashboard/SKILL.md` | Agent skill (SKILL.md) |
| `skills/professional-ppt/SKILL.md` | Agent skill (SKILL.md) |
| `skills/launch-video/SKILL.md` | Agent skill (SKILL.md) |
| `tools/office_artifacts.py` |  |
| `tools/render_launch_video.py` |  |
| `windows-office-setup.md` |  |
| `mac-linux-office-setup.md` |  |
| `approved-test-send.md` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-02-Instructions.pdf`](LAB-02-Instructions.pdf).

## Steps

### 1. Download and install Hermes Desktop (preferred)
Open https://hermes-agent.nousresearch.com/desktop in your browser. On macOS choose the Mac download and open the DMG, then install and launch Hermes. On Windows choose the Windows download, run Hermes-Setup.exe and launch Hermes. Follow normal OS installation prompts. Linux learners use the official terminal installation route linked on the page. Record the app/backend version shown by the installed app; do not install a second CLI checkout unless the trainer identifies a real need.

✅ **Expected:** The native Hermes Desktop app opens on the learner computer. The selected connection/profile is local and its version is recorded.

### 2. Connect a model in the desktop app
Use the Desktop provider/account configuration and the trainer-approved provider to complete sign-in. Choose the model provided for class and send a short test message. Verify a real model response and inspect visible tool activity. A free app download does not guarantee free model/API usage.

✅ **Expected:** The selected local profile gives a real model-backed reply; credentials stay in the app's configuration.

### 3. Open the launch workspace in Desktop
Create the kopi-kaki workspace in your own user folder and copy the lab data into it. Preserve any existing AGENTS.md. Use the Desktop file browser/workspace context or explicitly give the full folder path in chat, then ask Hermes to list the approved files before analysing them. On Windows stay in the native Desktop runtime; WSL has a different filesystem, PATH and credential store unless explicitly connected. On macOS/Linux, after copying this activity’s data contents into the confirmed workspace, use data/mac-linux-office-setup.md to create the per-workspace .office-venv required below. Windows uses data/windows-office-setup.md. Verify imports in this exact environment before running any office/video helper.

```bash
cd ~/kopi-kaki
python3 -m venv .office-venv
.office-venv/bin/python -m pip install openpyxl python-pptx Pillow
.office-venv/bin/python -c "import openpyxl, pptx, PIL"
gog --version
ffprobe -version
```

**Prompt** — paste into *Hermes Desktop chat*:

```text
Work in my kopi-kaki workspace at <replace with its full local path>. List campaign-brief.md, brand-guide.md and customer-reviews.csv. Confirm the workspace path and selected local profile before doing any analysis. Do not open or print credentials.
```

✅ **Expected:** The Desktop agent can actually read the three files in the intended local workspace.

### 4. Inspect and install reviewed skills (15 min)
In Desktop open Skills for the selected local profile. Inspect the source and SKILL.md of each supplied course skill: gog-office, office-analytics, interactive-dashboard, professional-ppt and launch-video. Review commands, dependencies, permissions and output paths. Use the current app’s local-folder install/import control; if using CLI, inspect hermes skills --help and the profile Skills path first, then copy each reviewed folder there. Do not assume every profile uses ~/.hermes/skills. Reload and confirm the five skills are listed. Source-qualified Hub installs are an optional alternative only after source review and scan. Skills instruct; gog/Python/FFmpeg execute; OAuth grants access.

**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Inspect only the five reviewed course skills in my explicit workspace. Report each purpose, required executable, allowed reads/writes and output. Run harmless version/import probes for installed tools and report missing dependencies. Do not install arbitrary packages, run unreviewed scripts or print credentials.
```

✅ **Expected:** Five reviewed skills visible in the selected profile; actual dependencies and capabilities checked.

### 5. Create the source brief and human decision (25 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Work in the confirmed Kopi Kaki workspace. Read brand-guide.md, campaign-brief.md, compliance-rules.md, customer-reviews.csv and competitors.csv (fictional internal notes). Use tools to calculate rating counts and identify top praise/complaint themes with counts and review_ids. Save outputs/lab01/review-insights.md. Write outputs/lab01/research-brief.md with a short summary, three campaign angles, evidence IDs, a risk for each and Decision needed. Do not invent market statistics. Ask me to select an angle; save my choice and reason in the brief and only the approved decision in persistent memory.
```

✅ **Expected:** The shared Day 2 source brief exists and ends with an explicit human decision.

### 6. Verify persistence and native runtime (10 min)
Inspect the approved memory entry, then start a fresh chat with the same local profile and explicit workspace. Ask which angle you chose and why, and whether the answer used persisted memory or source/session search. Optional extension: Messaging → Telegram → Create with QR; verify numeric allowlist, restart if requested and use the existing gateway for one private round trip. Telegram is optional in v2.3; it does not replace the morning assistant screenshot.

✅ **Expected:** Fresh-session recall checked; source IDs and decision agree.

## Verification / checkpoint
- [ ] Desktop uses the intended native local profile and approved provider
- [ ] Five reviewed skills and actual required tools verified; installation alone does not prove output
- [ ] review-insights.md and research-brief.md cite source IDs and contain the human decision
- [ ] Approved decision is verified in persistence and a fresh session

**Checkpoint:** One native Hermes agent, five reviewed skills and a source-linked company brief; human decision persists.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `hermes: command not found` | Open a new terminal or run `source ~/.zshrc` (macOS) / `source ~/.bashrc` (Linux/WSL2). |
| Model errors / context too small | Re-run `hermes setup` (or `hermes model`) and choose a model with ≥ 64k context. |
| Web search not available | Run `hermes tools` and enable the web toolset. Keyless search works for light use; for reliability add a free key, e.g. `hermes config set TAVILY_API_KEY tvly-...` (you reuse it on Day 2). |
| Windows paths | On native Windows Hermes keeps its data in %LOCALAPPDATA%\hermes instead of ~/.hermes — or run the labs inside WSL2. |
| Mia ignores the brand rules | Make sure you started `hermes` inside ~/kopi-kaki so AGENTS.md is loaded. |
| Bot is silent | Check allowed numeric ID, bot token entry, gateway status and network. Ensure no second gateway is polling this bot. |
| Telegram cannot find files | Use the full ~/kopi-kaki workspace path; gateway session directory can differ from the CLI session. |
| Desktop, CLI and Telegram see different files | Check selected connection/profile, workspace and runtime. Native Windows and WSL do not automatically share tokens, skills or paths. |

## Stretch challenge
Ask Mia: "Save the review-analysis procedure you just used as a reusable skill called review-insights." Then run `hermes skills list` — a self-improving agent turns experience into procedural memory.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
