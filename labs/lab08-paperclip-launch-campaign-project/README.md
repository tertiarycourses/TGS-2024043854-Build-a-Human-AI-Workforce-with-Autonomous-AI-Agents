# Lab 8 — Claude Code Agent Team — Produce the Launch Video

**Day 2 · Topic 3 · 50 min · Claude team + human gate · LO3**

> Use the Day 1 evidence pack and Kanban contracts to make a reviewed launch video with a real Claude Code agent team.

## Goal
Coordinate independent agents, test their outputs and evaluate whether teamwork improves a product artifact (LO3).

## The business scenario
The launch manager has accepted the office pack. A team must now produce one 15-second vertical launch video using verified product facts and supplied brand assets. Compare the team’s coordination and review effort with the Day 1 single-agent workflow.

## You will deliver
- outputs/team/research.md and storyboard.md — sources and scene contracts
- outputs/team/video/final.mp4 — playable 15-second 1080x1920 video
- outputs/team/audit-report.md — technical, factual, brand and rights checks
- outputs/team/decision-log.md — exact artifact version, human revision and final decision

## Who does what
- **Agents:** Claude Code lead plus researcher, scriptwriter, producer and reviewer teammates; distinct contexts and file ownership
- **You (the human):** Approve storyboard, watch the whole cut, request one revision and accept only the reviewed version

## Before you start
- Day 1 office pack and Day 2 Lab 4 Kanban studio complete
- Trainer-provisioned Claude Code access with usage budget; a free consumer chat account is not sufficient
- Python + Pillow and FFmpeg/ffprobe preinstalled; supplied local video renderer works before class

## Concepts in action
- Independent teammate contexts and direct messages
- Shared task list with separate file ownership
- Dependencies, human storyboard approval and independent audit
- Compare verified quality, usage and review effort against one agent

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
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `skills/launch-video/SKILL.md` | Agent skill (SKILL.md) |
| `tools/render_launch_video.py` |  |
| `team-task-contracts.md` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-08-Instructions.pdf`](LAB-08-Instructions.pdf).

## Steps

### 1. Install/check Claude Code and sign in (preflight)
Use approved access supplied by the trainer or your own authorised Claude Code account. Model usage is separate from SWDA subscription redemption. On Windows use the official PowerShell installer or WSL2. Do not print API keys.

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
# Windows PowerShell alternative: irm https://claude.ai/install.ps1 | iex
ffmpeg -version
ffprobe -version
```

✅ **Expected:** Claude Code, FFmpeg and ffprobe versions are recorded and the trainer confirms available usage budget.

### 2. Start the team in the existing launch workspace
```bash
cd ~/kopi-kaki
mkdir -p outputs/team/video
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

✅ **Expected:** Claude Code opens with agent teams enabled. This is an experimental feature; check current official docs if behaviour differs.

### 3. Create real teammates and a task list (10 min)
**Prompt** — paste into *Claude Code lead session*:

```text
Create an agent team for Kopi Kaki’s launch video. Use four actual teammates: researcher owns outputs/team/research.md; scriptwriter owns outputs/team/storyboard.md; producer owns outputs/team/video/; reviewer owns outputs/team/audit-report.md. You are not alone in the workspace: do not revert anyone’s edits; never have two workers edit the same file. Read the Day 1 approved office pack and brand rules. Use a shared task list with owner, input, output, dependency and acceptance criteria. Research precedes storyboard; human storyboard approval precedes render; render precedes audit. No external posting, purchases or new providers. Ask teammates to plan first and stop at the human gates. Show the actual running teammate and task state; do not role-play all roles in one response.
```

✅ **Expected:** Distinct teammate sessions and real tasks are visible; output ownership and dependencies are explicit.

### 4. Research and approve the storyboard (10 min)
**Prompt** — paste into *Claude Code lead session*:

```text
Have the researcher extract only approved facts with source file and row/review IDs. Have the scriptwriter create three 5-second scenes for a 15-second 1080x1920 silent launch video. No health, halal or invented market claims. Include the approved price and date; if using a promo, include the exact terms. Pause for my storyboard approval before asking the producer to render.
```

✅ **Expected:** research.md and storyboard.md exist. Human reviews the exact scene text before production.

### 5. Produce the real MP4 (10 min)
Copy this lab’s reviewed video tool into ~/kopi-kaki/tools if it is not already there. The helper is a deterministic baseline: after approval the producer may revise the frame layout while preserving verified copy. No paid generation API is needed.

```bash
python3 tools/render_launch_video.py --out outputs/team/video
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json outputs/team/video/final.mp4
```

**Prompt** — paste into *Claude Code lead session*:

```text
The storyboard text I reviewed is approved for local production only. Ask the producer to inspect tools/render_launch_video.py, adapt its three scene texts/layouts to the approved storyboard and render a real MP4. Never use unlicensed music or a real-person likeness. Save the exact command and ffprobe metadata to render-log.md. Report render errors honestly; a storyboard is not a completed video.
```

✅ **Expected:** A playable MP4 exists with 1080x1920 dimensions and approximately 15 seconds duration; render command and metadata are recorded.

### 6. Independent review and human revision (10 min)
**Prompt** — paste into *Claude Code lead session*:

```text
Have the reviewer independently inspect the saved video metadata and every scene frame against the approved storyboard, price/date, brand rules and readability. Write audit-report.md with PASS/FAIL and evidence for each check. Do not assume a successful render means the copy is correct. I will watch the full video and request one concrete change. Re-render and re-audit the changed version. Save my decision and the final MP4 SHA256 hash in decision-log.md. Do not publish.
```

✅ **Expected:** Reviewer evidence and one human-directed revision are recorded. Human watches the entire final cut.

### 7. Compare and close the team (10 min)
**Prompt** — paste into *Claude Code lead session*:

```text
Compare this team with Day 1’s single agent: setup time, run time, review effort, quality defects and provider usage. State where extra coordination helped and where it cost more. Confirm every teammate’s task state and shut down teammates cleanly after saving outputs. Do not describe unfinished or blocked tasks as done.
```

✅ **Expected:** A factual comparison and saved task/artifact evidence; teammates shut down cleanly.

## Verification / checkpoint
- [ ] Actual teammate sessions and task states prove a team ran
- [ ] Research/storyboard/video/audit files respect ownership and dependencies
- [ ] ffprobe and playback prove real MP4 output and correct duration/dimensions
- [ ] One human-requested change was re-rendered and independently reviewed
- [ ] Final decision names the exact video hash; usage and limitations recorded

**Checkpoint:** Actual independent teammates produced a playable reviewed video, one human revision and an exact-version decision log; no external publication.

## Troubleshooting

| Symptom | Fix |
|---|---|
| No teammates appear | Check the experimental environment variable in the process that launched Claude; verify current docs and account/tool availability. |
| Access or usage blocked | Use trainer-led demonstration of the real team and record your participation accurately. Do not label a role-play as an executed team. |
| Teammates overwrite files | Stop them, restore separate ownership and reconcile artifacts before resuming. |
| FFmpeg missing | Use trainer-preinstalled FFmpeg or official install instructions before class. A frame pack is a partial output, not video completion. |
| Text clipped or too small | Revise frame layout, re-render and watch the final cut on the target display. |

## Stretch challenge
Compare optional HyperFrames or Remotion production against the deterministic local renderer. Require actual MP4, provenance, review and cost evidence for either path.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
