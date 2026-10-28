# Lab 5 — Activity 5 — Hermes Bots & Kanban Video Studio

**Day 2 · Topic 3 · 85 min · Multi-agent (ordered pipeline) · LO2**

> Coordinate five distinct Hermes profiles on a Kanban board to create a local 15-second video and a reviewed release package.

## Goal
Coordinate actual independent Hermes profiles/bots through source research, storyboard, production and independent audit; preserve human control (LO2; PP Task 3 preparation).

## The business scenario
Use the verified Day 1 launch-office evidence. The team must turn one approved campaign angle into a short video while making ownership, dependencies, review and the human release gate visible.

## You will deliver
- outputs/team/research.md and storyboard.md — source references and approved scenes
- outputs/team/video/final.mp4 — real playable 15-second 1080x1920 MP4
- outputs/team/audit-report.md and release-package.md — independent checks and human decision
- Actual Hermes bots/profiles + Kanban task IDs, parent edges, run history and human gate; ONE video-team screenshot for PP Task 3

## Who does what
- **Agents:** Five distinct Hermes profiles: researcher, scriptwriter, producer, auditor and publisher; publisher packages locally only
- **You (the human):** Approve storyboard, watch the actual video, request a correction and decide whether the exact version is accepted

## Before you start
- Day 1 approved office pack and source files available
- Trainer preflights distinct researcher, scriptwriter, producer, auditor and publisher profiles; provider access, native Python/Pillow and FFmpeg/ffprobe
- Desktop Bot Mode roster may expose those profiles as named bots; do not confuse Desktop bots with Telegram bot accounts
- Each worker owns different output files; a trainer-prepared board is inspected and exercised by each learner

## Concepts in action
- Separate profile/context and output ownership for each specialist
- Kanban task contracts and dependencies
- Producer result must pass independent audit
- Human gate is visible; classroom release means a local package, not public posting

## Lab files (`data/`)

| File | What it is |
|---|---|
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `skills/brand-compliance-audit/SKILL.md` | Agent skill (SKILL.md) |
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

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-05-Instructions.pdf`](LAB-05-Instructions.pdf).

## Steps

### 1. Inspect actual profiles, bots and runtime (10 min)
In Desktop inspect the Bot Mode roster and each profile’s identity, model, skills and workspace. A Desktop bot is a roster presentation of a profile; a Telegram bot is a messaging account. Use distinct profiles for concurrently running workers. Provider configuration is preflighted privately. Inspect installed help before using version-specific controls.

```bash
hermes --version
hermes profile list
hermes profile create --help
hermes kanban create --help
hermes gateway status
ffprobe -version
```

✅ **Expected:** The learner can inspect actual profile/task state; gateway and renderer are available.

### 2. Create safe task contracts and dependencies (15 min)
Use the supplied kanban-studio-runbook.md. In the selected training gateway switch Orchestration to Manual (kanban.auto_decompose=false), restart if required and verify the saved setting. Create human approval cards UNASSIGNED and --triage before dependent tasks exist. Human completes only the gate whose exact artifact they reviewed. No worker has authority to complete a human gate. Create producer and package tasks with the gate as parent at creation; do not dispatch first and link later. There is no assumed native approval-permission system: human supervision and withholding external posting tools enforce the classroom boundary.

**Prompt** — paste into *Hermes lead chat in ~/kopi-kaki*:

```text
Use the Kanban tools to inspect or build my real kopi-video task graph in the explicit launch workspace. Actual profiles: researcher, scriptwriter, producer, auditor, publisher. First verify Manual orchestration, kanban.auto_decompose=false, in the selected gateway configuration. Create unassigned triage cards for HUMAN storyboard approval and HUMAN final acceptance; only I may complete them. Research -> storyboard -> HUMAN storyboard approval -> render -> audit -> HUMAN final acceptance -> local package. Put every parent edge in place before a task becomes runnable. Each task gets a unique owned output, acceptance criteria and source path. Producer owns only outputs/team/video; auditor owns audit-report.md; publisher packages locally only. Never revert another worker or complete a human gate. Verify both human cards remain unassigned and in triage across a dispatcher tick before creating dependent work. Show actual task IDs, owners and states. Stop if the installed runtime cannot enforce or expose the dependencies.
```

✅ **Expected:** A real Kanban board shows owners, dependencies and the human gate.

### 3. Run research and storyboard; human approves exact text (15 min)
**Prompt** — paste into *Hermes lead chat*:

```text
Dispatch the researcher to extract approved launch facts and source IDs from the Day 1 office pack into outputs/team/research.md. Scriptwriter writes three five-second scenes into storyboard.md. Pause for my exact-copy approval. No health, halal or unsupported market claims. Use only approved product facts and supplied/licensed assets.
```

✅ **Expected:** Research and storyboard files exist. Human checks the scene copy before production.

### 4. Produce a playable video with the reviewed tool (15 min)
The producer inspects and adapts the supplied local renderer to the approved copy, then runs it. No paid video API is required. The real output is the MP4, not a tool-success message.

```bash
python3 tools/render_launch_video.py --out outputs/team/video
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json outputs/team/video/final.mp4
```

**Prompt** — paste into *Hermes lead chat*:

```text
My reviewed storyboard is approved for local production. Dispatch the producer to adapt the reviewed render_launch_video.py scene copy and create outputs/team/video/final.mp4. Preserve the verified facts. Save the render command and metadata; do not advance to release before audit and my decision.
```

✅ **Expected:** A playable MP4 exists, 1080x1920, approximately 15 seconds, with saved metadata.

### 5. Independent audit, real revision and acceptance (20 min)
**Prompt** — paste into *Hermes lead chat*:

```text
Dispatch the independent auditor to inspect every scene and the real ffprobe output. Check facts, brand, readability, duration, dimensions and rights. Save audit-report.md with evidence. I will watch the whole cut and request one correction. Re-render and re-audit it. Keep release blocked until my exact-version ACCEPT. Publisher then creates only release-package.md with file hash and audit reference; no external posting.
```

✅ **Expected:** Independent evidence, one corrected defect or human-directed revision, and a human-reviewed local release pack.

### 6. Capture the real team evidence (10 min)
For PP Task 3 capture ONE readable Kanban/video-creation screenshot showing actual assigned Hermes bot/profile names, a dependency or human gate, and the video render/output task. A task drawer can show output path and parent IDs while board owners remain visible. Keep MP4, runs, source references, audit and exact-version decision as working evidence. Do not submit a role diagram, sample board or one-agent role-play.

**Prompt** — paste into *Hermes lead chat*:

```text
Summarise the real profile/task state, artifact paths, human decision and what failed or needed correction. Compare team coordination effort with Day 1’s single agent. Do not mark blocked or unfinished tasks as completed.
```

✅ **Expected:** PP evidence is from a real board; limitations are accurately stated.

## Verification / checkpoint
- [ ] Actual distinct profiles/bots execute assigned tasks; task IDs and run history exist
- [ ] Producer remains gated until a human completes the unassigned storyboard approval card
- [ ] Real MP4 plays, metadata matches specification and auditor checks every scene
- [ ] Human directs one change, reviewer rechecks it, and final acceptance identifies the exact hash

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
