# Lab 4 — Multi-Agent Video Studio — Kanban, Production & Human Review

**Day 2 · Topic 2 · 50 min · Multi-agent (ordered pipeline) · LO2**

> Coordinate five distinct Hermes profiles on a Kanban board to create a local 15-second video and a reviewed release package.

## Goal
Orchestrate a multi-agent team with role specialisation, dependencies and a human approval gate, and correlate the team design with quality, cost and speed (LO2).

## The business scenario
Use the verified Day 1 launch-office evidence. The team must turn one approved campaign angle into a short video while making ownership, dependencies, review and the human release gate visible.

## You will deliver
- outputs/lab04/research.md and storyboard.md
- outputs/lab04/video/final.mp4 — playable 15-second 1080x1920 local video
- outputs/lab04/audit-report.md and release-package.md
- Real Kanban task/profile state with dependency and blocked human-release gate for PP Q2

## Who does what
- **Agents:** Five distinct Hermes profiles: researcher, scriptwriter, producer, auditor and publisher; publisher packages locally only
- **You (the human):** Approve storyboard, watch the actual video, request a correction and decide whether the exact version is accepted

## Before you start
- Trainer preflights five distinct Hermes profiles, model access and the gateway before Day 2; learners inspect and run them, rather than spending the 50-minute unit installing everything
- Day 1 launch office pack; supplied brand assets and local render_launch_video.py
- Python + Pillow, ffmpeg and ffprobe are installed and tested

## Concepts in action
- Separate profile/context and output ownership for each specialist
- Kanban task contracts and dependencies
- Producer result must pass independent audit
- Human gate is visible; classroom release means a local package, not public posting

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `templates/video-brief-template.md` | Template |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `skills/brand-compliance-audit/SKILL.md` | Agent skill (SKILL.md) |
| `DESIGN.md` | Visual identity for HyperFrames |
| `souls/researcher.SOUL.md` | Role + rules for one studio profile |
| `souls/scriptwriter.SOUL.md` | Role + rules for one studio profile |
| `souls/producer.SOUL.md` | Role + rules for one studio profile |
| `souls/auditor.SOUL.md` | Role + rules for one studio profile |
| `souls/publisher.SOUL.md` | Role + rules for one studio profile |
| `tasks/t1-research.md` | Task brief (used with --body-file) |
| `tasks/t2-script.md` | Task brief (used with --body-file) |
| `tasks/t3-produce.md` | Task brief (used with --body-file) |
| `tasks/t4-audit.md` | Task brief (used with --body-file) |
| `tasks/t5-package.md` | Task brief (used with --body-file) |
| `tasks/t6-post.md` | Task brief (used with --body-file) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `skills/launch-video/SKILL.md` | Agent skill (SKILL.md) |
| `tools/render_launch_video.py` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-04-Instructions.pdf`](LAB-04-Instructions.pdf).

## Steps

### 1. Inspect the preflighted studio (5 min)
Copy this lab’s tools and skills into the same workspace without overwriting AGENTS.md. The trainer has prepared the distinct profiles and provider access. If that preflight is missing, record setup time and complete the core run under trainer guidance; do not claim a role-play is a real team.

```bash
hermes --version
hermes profile --help
hermes kanban --help
hermes gateway status
ffmpeg -version
ffprobe -version
```

✅ **Expected:** The learner can inspect actual profile/task state; gateway and renderer are available.

### 2. Create or inspect the actual Kanban contracts (10 min)
**Prompt** — paste into *Hermes lead chat in ~/kopi-kaki*:

```text
Inspect current Hermes profile and Kanban help. Use distinct profiles researcher, scriptwriter, producer, auditor and publisher. Create or inspect a real launch-video board: research -> storyboard -> human storyboard review -> render -> independent audit -> human release gate -> local package. Each task needs one owner, source input, unique output path and done criteria. Do not revert another worker’s files. Keep the release/package task blocked until my decision. Publisher may only prepare a local package; never post to Telegram channels, social media, email or the web. Show the real task/profile state and dependency links.
```

✅ **Expected:** A real Kanban board shows owners, dependencies and the human gate.

### 3. Research, write and approve the scenes (10 min)
**Prompt** — paste into *Hermes lead chat*:

```text
Dispatch the researcher to extract approved launch facts and source IDs from the Day 1 office pack into outputs/lab04/research.md. Scriptwriter writes three five-second scenes into storyboard.md. Pause for my exact-copy approval. No health, halal or unsupported market claims. Use only approved product facts and supplied/licensed assets.
```

✅ **Expected:** Research and storyboard files exist. Human checks the scene copy before production.

### 4. Render a real video (10 min)
The producer inspects and adapts the supplied local renderer to the approved copy, then runs it. No paid video API is required. The real output is the MP4, not a tool-success message.

```bash
python3 tools/render_launch_video.py --out outputs/lab04/video
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json outputs/lab04/video/final.mp4
```

**Prompt** — paste into *Hermes lead chat*:

```text
My reviewed storyboard is approved for local production. Dispatch the producer to adapt the reviewed render_launch_video.py scene copy and create outputs/lab04/video/final.mp4. Preserve the verified facts. Save the render command and metadata; do not advance to release before audit and my decision.
```

✅ **Expected:** A playable MP4 exists, 1080x1920, approximately 15 seconds, with saved metadata.

### 5. Audit, revise and keep the release gate visible (10 min)
**Prompt** — paste into *Hermes lead chat*:

```text
Dispatch the independent auditor to inspect every scene and the real ffprobe output. Check facts, brand, readability, duration, dimensions and rights. Save audit-report.md with evidence. I will watch the whole cut and request one correction. Re-render and re-audit it. Keep release blocked until my exact-version ACCEPT. Publisher then creates only release-package.md with file hash and audit reference; no external posting.
```

✅ **Expected:** Independent evidence, one corrected defect or human-directed revision, and a human-reviewed local release pack.

### 6. Capture evidence and reflect (5 min)
Take one screenshot of the actual Kanban board showing multiple assigned profiles, a dependency and the human release gate. This supports PP Task 2; read the actual candidate paper for the written analysis requirements. Save source artifacts as supporting working files.

**Prompt** — paste into *Hermes lead chat*:

```text
Summarise the real profile/task state, artifact paths, human decision and what failed or needed correction. Compare team coordination effort with Day 1’s single agent. Do not mark blocked or unfinished tasks as completed.
```

✅ **Expected:** PP evidence is from a real board; limitations are accurately stated.

## Verification / checkpoint
- [ ] Actual profiles and assigned Kanban tasks are visible
- [ ] Dependencies block downstream work and the human gate controls local release
- [ ] A playable 15-second 1080x1920 video has independent audit evidence
- [ ] One screenshot shows the real team, dependency and human gate for PP Q2

**Checkpoint:** Real distinct profiles + real Kanban dependencies + playable reviewed video + visible human release gate. No external publishing.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Only one agent acts all roles | Inspect profile/task runtime; a role-play response is not a team. Use the trainer-preflighted real profiles. |
| Tasks do not dispatch | Check gateway status, assigned profile, dependency state and provider access. |
| Video renderer fails | Inspect ffmpeg error and dependencies; a storyboard is partial work and cannot be called completed video. |
| Gate is bypassed | Stop dispatch, restore blocked release state and inspect whether any external action occurred. |

## Stretch challenge
Re-run one stage after changing the approved angle. Show which downstream artifacts become stale and require re-review.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
