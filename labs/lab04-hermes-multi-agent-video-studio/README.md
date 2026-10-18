# Lab 4 — Multi-Agent Video Studio — Research → Script → Production → Audit → Publish

**Day 1 · Topic 2 · 60 min · Multi-agent (ordered pipeline) · LO2**

> Build a five-agent production team on the Kanban board, render a real 25-second vertical video with HyperFrames, let an auditor agent check it, and approve it yourself before it publishes.

## Goal
Orchestrate a multi-agent team with role specialisation, dependencies and a human approval gate, and correlate the team design with quality, cost and speed (LO2).

## The business scenario
The campaign needs a 25-second TikTok/Reels launch video. One agent doing everything is slow, expensive and hard to review, so you staff a studio: a researcher finds the hook, a scriptwriter writes it, a producer renders it, an auditor checks it against the brand and compliance rules, and a publisher prepares and posts it — but only after you approve the cut.

## You will deliver
- 5 Hermes profiles with routing descriptions (researcher, scriptwriter, producer, auditor, publisher)
- A Kanban task graph with dependencies and a human gate before publishing
- video-studio/research.md, script.md (scene list), output/final.mp4 (9:16)
- video-studio/audit-report.md — PASS/FAIL on V1–V9 and C1–C10
- video-studio/publish-package.md, reviewed by you, then the video posted once to your Telegram channel

## Who does what
- **Agents:** 5 Hermes profiles coordinated by the Kanban board
- **You (the human):** Review the cut and the publish package, then release the posting task (or send it back with comments)

## Before you start
- Lab 3 complete: Telegram bot connected, the gateway running (it dispatches Kanban tasks) and your channel ID from `hermes send --list telegram`
- Node.js 22+ and FFmpeg (installed with Hermes) for video rendering

## Concepts in action
- Agentic AI = several specialised agents + orchestration (vs one AI agent)
- Profile description = routing contract; SOUL.md = role + rules
- Dependencies (--parent) make an ordered SOP pipeline
- Auditor agent = verification; blocked task = human gate

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

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-04-Instructions.pdf`](LAB-04-Instructions.pdf).

## Steps

### 1. Install the HyperFrames video skill
HyperFrames (open source, no API key) renders MP4 videos from HTML + animation using headless Chrome and FFmpeg. Install the official optional skill and run its setup script once.

```bash
hermes skills install official/creative/hyperframes --yes
bash "$(dirname "$(find ~/.hermes/skills -path '*/hyperframes/SKILL.md' | head -1)")/scripts/setup.sh"
npx hyperframes doctor
```

✅ **Expected:** `npx hyperframes doctor` reports Node ≥ 22, FFmpeg and Chrome OK.

### 2. Create the shared studio workspace
All five agents share one folder so each stage can read the previous stage's output. Copy this lab's data — it includes DESIGN.md (the visual identity HyperFrames asks for), a SOUL.md per role and the auditor's skill. Install the skill BEFORE creating the profiles, because `--clone` copies your skills into each new profile.

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/.hermes/skills/marketing && cp -R ~/kopi-kaki/skills/brand-compliance-audit ~/.hermes/skills/marketing/
mkdir -p ~/kopi-kaki/video-studio/output
# put YOUR channel id (from Lab 3: hermes send --list telegram) into the posting brief
CH="telegram:-100XXXXXXXXXX"
perl -pi -e "s/telegram:<channel_id>/$CH/" ~/kopi-kaki/tasks/t6-post.md
cp ~/kopi-kaki/DESIGN.md ~/kopi-kaki/brand-guide.md ~/kopi-kaki/campaign-brief.md ~/kopi-kaki/compliance-rules.md ~/kopi-kaki/video-qa-checklist.md ~/kopi-kaki/video-studio/
```

### 3. Staff the studio — five profiles with routing descriptions
Each profile is an isolated agent with its own memory and SOUL.md. The `--description` is the routing contract the Kanban orchestrator reads, so say exactly what the role takes in and hands off. `--clone` copies your model and keys.

```bash
hermes profile create researcher --clone --description "Finds hooks, trends and proof points for a short video; writes research.md with cited sources"
hermes profile create scriptwriter --clone --description "Turns research.md into a 25-second script and 6-scene list in script.md"
hermes profile create producer --clone --description "Renders script.md into a 9:16 MP4 with HyperFrames; writes output/final.mp4"
hermes profile create auditor --clone --description "Audits a video and its copy against video-qa-checklist.md and compliance-rules.md; PASS or FAIL with fixes"
hermes profile create publisher --clone --description "Builds the publish package and posts an approved video to the Telegram channel"
for p in researcher scriptwriter producer auditor publisher; do cp ~/kopi-kaki/souls/$p.SOUL.md ~/.hermes/profiles/$p/SOUL.md; done
hermes profile list
```

✅ **Expected:** Five profiles listed (also visible on the dashboard's Profiles page).

### 4. Build the task graph with a human gate
Create the six tasks in order. Each `--parent` makes a task wait for the previous one. The publisher first only BUILDS the publish package (T5); the task that actually POSTS (T6) starts BLOCKED — only you can release it, after you have reviewed both the cut and the package. Copy each printed task ID into the next command (shown as <T1>, <T2> …).

```bash
S=dir:$HOME/kopi-kaki/video-studio
hermes kanban create "Research hooks for the Gula Melaka Cold Brew launch short" --assignee researcher --workspace $S --tenant kopi-video --body-file ~/kopi-kaki/tasks/t1-research.md
hermes kanban create "Write the 25-second script and scene list" --assignee scriptwriter --parent <T1> --workspace $S --tenant kopi-video --body-file ~/kopi-kaki/tasks/t2-script.md
hermes kanban create "Render the 9:16 launch video with HyperFrames" --assignee producer --parent <T2> --workspace $S --tenant kopi-video --skill hyperframes --max-runtime 45m --body-file ~/kopi-kaki/tasks/t3-produce.md
hermes kanban create "Audit the video and copy (V1-V9, C1-C10)" --assignee auditor --parent <T3> --workspace $S --tenant kopi-video --skill brand-compliance-audit --body-file ~/kopi-kaki/tasks/t4-audit.md
hermes kanban create "Build the publish package (do not post)" --assignee publisher --parent <T4> --workspace $S --tenant kopi-video --body-file ~/kopi-kaki/tasks/t5-package.md
hermes kanban create "Post the approved video to the channel" --assignee publisher --parent <T5> --workspace $S --tenant kopi-video --initial-status blocked --body-file ~/kopi-kaki/tasks/t6-post.md
```

✅ **Expected:** `hermes kanban list --tenant kopi-video` shows 6 tasks; T6 is blocked.

### 5. Watch the studio work
The gateway from Lab 3 dispatches ready tasks to the right profile. Watch the lanes move (todo → ready → running → done) in the terminal or on the dashboard Kanban page. Open each task to read its comments and outputs.

```bash
hermes kanban watch --tenant kopi-video
# or open the web dashboard:
hermes dashboard
```

✅ **Expected:** research.md → script.md → output/final.mp4 → audit-report.md → publish-package.md appear in ~/kopi-kaki/video-studio.

### 6. If the auditor says FAIL — rework, don't restart
A FAIL is the system working. The auditor's brief tells it to create a rework card for the producer and a re-audit card for itself. If it did not, add them yourself — the fix list comes from audit-report.md. The package and posting tasks wait until a PASS.

```bash
hermes kanban create "Rework the video: apply the audit-report.md fixes" --assignee producer --parent <T4> --workspace $S --tenant kopi-video --skill hyperframes --body "Fix V5: show SHIOK20 terms on the end card. Fix C9: AI voice-over disclosure. Re-render output/final.mp4."
hermes kanban create "Re-audit the reworked video" --assignee auditor --parent <rework_id> --workspace $S --tenant kopi-video --skill brand-compliance-audit --body-file ~/kopi-kaki/tasks/t4-audit.md
```

### 7. Human gate — review the cut AND the package, then release
Open output/final.mp4 and publish-package.md. Check them against the brief yourself: does the hook land in 2 seconds, are the price and SHIOK20 terms right, is the AI disclosure in the description, are the hashtags on-brand? If yes, unblock T6. If not, comment on T5 (or create a rework card) and keep T6 blocked.

```bash
open ~/kopi-kaki/video-studio/output/final.mp4     # Windows/WSL: explorer.exe, Linux: xdg-open
cat ~/kopi-kaki/video-studio/publish-package.md
hermes kanban unblock <T6>
```

✅ **Expected:** T6 moves to ready and the publisher posts once.

### 8. Confirm the post and close the loop
The publisher posts the video with its caption to your channel exactly once and records the result in publish-package.md. Do not post it again yourself — check the channel and the board instead.

```bash
hermes kanban list --tenant kopi-video
hermes kanban show <T6>
```

✅ **Expected:** The video is in your Telegram channel; all tasks are done.

### 9. Reflect — why a team beats one big agent
**Prompt** — paste into *Hermes chat*:

```text
Read the Kanban history for tenant kopi-video (hermes kanban show for each task). Report per stage: which profile ran it, how long it took, how many retries or change requests it needed, and what was handed to the next stage. Then compare this five-agent design with a single agent doing everything: quality, cost, speed, reviewability.
```

✅ **Expected:** A stage-by-stage table you can use in the assessment.

## Verification / checkpoint
- [ ] `hermes profile list` shows the five roles
- [ ] final.mp4 is 1080×1920, 20–30 s (`ffprobe` or the auditor's report)
- [ ] audit-report.md is PASS (or shows a FAIL that was fixed via request-changes)
- [ ] The posting task (T6) completed only after your `unblock`, and the video was posted once
- [ ] PP evidence: take ONE screenshot now of the Kanban board showing the tasks, dependencies and the posting gate — Task 2 of the Practical Performance uses it

**Checkpoint:** final.mp4 is 9:16 and 20–30 s, the audit is PASS, and the posting task only ran after you reviewed the package and unblocked it.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Tasks never start | The dispatcher runs inside the gateway — `hermes gateway status`; restart with `hermes gateway restart`. |
| Render fails | Run `npx hyperframes doctor`; the producer needs Node ≥ 22 and FFmpeg. Allow `--max-runtime 45m`. |
| Stages can't see each other's files | Every task must use the same `--workspace dir:` path (not scratch/worktree). |
| Publisher doesn't know where to post | Check t6-post.md contains your real channel id (step 2), not <channel_id>. |
| Wrong profile picked a task | Sharpen the profile description: `hermes profile describe <name> "…"`. |
| Rendering too slow on your laptop | Ask the producer for `--quality draft`, or accept a 6-frame storyboard (PNG) for the audit. |

## Stretch challenge
Shortcut: install `official/creative/kanban-video-orchestrator`, give it the brief, and compare the team it designs with yours. Which roles did it add or merge?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
