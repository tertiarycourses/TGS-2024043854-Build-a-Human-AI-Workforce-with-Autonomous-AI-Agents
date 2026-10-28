# Lab 8 — Activity 8 — Revise, Verify & Release the Team Video Locally

**Day 2 · Topic 3 · 115 min · Multi-agent team + human oversight · LO3**

> Use the existing Hermes team to revise the video, test a repeat run and accept a verified local release with evidence.

## Goal
Evaluate multi-agent video creation, compare strengths/limitations and assess a maintainable workflow (LO3; PP Task 3).

## The business scenario
The manager changes the launch angle. The team must identify stale downstream work, revise only owned files, re-render and re-audit the real video, then compare quality and effort against a single agent.

## You will deliver
- outputs/team/video/final.mp4 — revised playable video and metadata
- outputs/team/audit-report.md, decision-log.md and release-package.md — exact-version acceptance
- outputs/team/scorecard.csv and improvement-plan.md — quality, cost/time, maintenance and constraints
- ONE actual multi-agent Kanban video-creation screenshot with Hermes bots, output task and dependency/human gate — PP Task 3

## Who does what
- **Agents:** Distinct Hermes profiles: researcher, scriptwriter, producer, auditor and publisher
- **You (the human):** Own approval gates, inspect evidence and accept the exact version

## Before you start
- Activity 5 real Hermes video team is working
- Same approved launch workspace and original source files

## Concepts in action
- Separate agent state and output ownership
- Source provenance and independent verification
- Exact-version human decision and honest completion

## Lab files (`data/`)

| File | What it is |
|---|---|
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `DESIGN.md` | Visual identity for HyperFrames |
| `souls/researcher.SOUL.md` | Role + rules for one studio profile |
| `souls/scriptwriter.SOUL.md` | Role + rules for one studio profile |
| `souls/producer.SOUL.md` | Role + rules for one studio profile |
| `souls/auditor.SOUL.md` | Role + rules for one studio profile |
| `souls/publisher.SOUL.md` | Role + rules for one studio profile |
| `tasks/t1-research.md` | Task contract; use current Kanban tools or --body text |
| `tasks/t2-script.md` | Task contract; use current Kanban tools or --body text |
| `tasks/t3-produce.md` | Task contract; use current Kanban tools or --body text |
| `tasks/t4-audit.md` | Task contract; use current Kanban tools or --body text |
| `tasks/t5-package.md` | Task contract; use current Kanban tools or --body text |
| `tasks/t6-post.md` | Task contract; use current Kanban tools or --body text |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `skills/launch-video/SKILL.md` | Agent skill (SKILL.md) |
| `tools/render_launch_video.py` |  |
| `windows-office-setup.md` |  |
| `team-task-contracts.md` |  |
| `kanban-studio-runbook.md` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-08-Instructions.pdf`](LAB-08-Instructions.pdf).

## Steps

### 1. 8A: plan the change and gate stale work (10 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Inspect the current real kopi-video board, bots/profiles and artifact hashes. I request a more outlet-focused video using the verified Day 1 sales findings. Identify affected research, storyboard, render and audit outputs. Create new follow-up tasks with dependencies and separate owners; preserve completed run history. Verify Manual orchestration (kanban.auto_decompose=false) and create an UNASSIGNED human review card before dependent production can run. Do not change the approved product facts or start publication.
```

✅ **Expected:** New tasks identify stale artifacts; human gate exists before dependent work.

### 2. 8A: revise storyboard and produce (25 min)
```bash
python3 tools/render_launch_video.py --out outputs/team/video
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json outputs/team/video/final.mp4
```

**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Researcher cites verified outlet data and source passages. Scriptwriter revises three five-second scenes, keeping each headline within seven words. Pause for my exact-copy decision. After I complete the unassigned storyboard gate, producer copies the reviewed renderer into its owned outputs/team/video/ folder, adapts that copy and saves a new playable MP4 plus command/ffprobe metadata. Each worker owns its files. A tool-success message without an MP4 is incomplete.
```

✅ **Expected:** Revised 15-second 1080x1920 MP4 exists and plays.

### 3. 8A: independent review and evidence (15 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Auditor independently checks actual scene frames, source facts, approved storyboard, duration, dimensions, rights and readability. Save evidence for every PASS/FAIL. Keep final acceptance unassigned and pending. Show a Kanban/video task detail with real bot/profile names, parent dependencies, output path and review state so I can capture ONE screenshot for PP Task 3. Do not fabricate screenshots or mark unexecuted work done.
```

✅ **Expected:** Own real team/video screenshot plus saved audit; final human decision remains pending.

### 4. 8B: repeat-run and recovery test (30 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Create a local-only repeat-run checklist, not an unattended publication job. Test one repeat run against the same approved source versions. Seed a missing-source condition in an isolated test fixture; never delete original sources. Verify the affected task stops and reports the missing input, restore the fixture and retry only that stage. Record run IDs, elapsed time, changes, retry outcome and whether downstream approvals became stale. Limit to one deliberate test/retry; no provider purchases or external sends.
```

✅ **Expected:** A real stop/recovery trace exists; source changes invalidate dependent reviews.

### 5. 8C: watch and accept the exact version (15 min)
Human watches the whole final cut, verifies all visible copy and chooses ACCEPT or REVISE. Obtain the actual SHA256 using the local tool or native OS command; do not let the agent invent a hash.

**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Show final video path, actual SHA256, complete audit evidence and unresolved issues. Wait for my exact-version decision. Only after I accept and personally complete the unassigned final gate may publisher create release-package.md locally with MP4 path/hash, source/storyboard/audit links, AI-assisted description, CTA, rights and acceptance. No external posting is authorised.
```

✅ **Expected:** Local release package names the accepted file hash and human decision.

### 6. 8C: evaluate and improve the workflow (20 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Create scorecard.csv comparing the actual Day 1 single-agent office run and Day 2 video team without pretending they are identical tasks. Include setup, run and human review time; first-pass acceptance; defects/revisions; actual usage/cost if available; source coverage; unknowns. Explain when the team overhead is justified. Assess two improvements and their measurable expected effect. Write improvement-plan.md with owner, test, success threshold, rollback and source-maintenance schedule. Reuse rag-feasibility.md to explain how an advisory-content version would maintain retrieval sources.
```

✅ **Expected:** Evidence-based evaluation plus maintainable improvement plan; unknown cost is not zero.

## Verification / checkpoint
- [ ] Real independent Hermes bots/profiles and actual task history
- [ ] Playable revised MP4 with checked metadata and independent scene audit
- [ ] One stop/recovery test; source changes trigger downstream review
- [ ] Human acceptance binds exact hash; package is local only
- [ ] PP Task 3 screenshot shows actual video creation with Kanban team and Hermes bots

**Checkpoint:** A real revised video, independent audit, human acceptance, maintainable plan and PP evidence; no public release.

## Troubleshooting

| Symptom | Fix |
|---|---|
| One chat plays every role | Inspect assigned profiles and run history; do not count role-play as an executed team. |
| Renderer fails | Inspect native Python/Pillow/FFmpeg PATH; keep the task incomplete until a playable MP4 exists. |
| Source changes after approval | Invalidate dependent storyboard/render/audit approval and recheck. |
| No usage cost data | Record unavailable rather than estimating it as zero. |

## Stretch challenge
Transfer the checks to a different product while preserving source and decision ownership.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
