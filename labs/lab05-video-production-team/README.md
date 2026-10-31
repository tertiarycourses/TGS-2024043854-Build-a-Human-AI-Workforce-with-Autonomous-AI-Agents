# Lab 5 — Activity 5 — Your Video Team on a Kanban Board

**Day 2 · Topic 3 · 115 min · Agent team on a Kanban board + human gates · LO3**

> One prompt hires a video team and builds its Kanban board. Research, script, voice-over, render, review: the board runs it; nothing ships until you approve.

## Goal
Run a multi-agent video team with Kanban dependencies, source checks and an independent review, and accept only the exact video version you have watched (LO3; PP Task 3).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. The launch video is your biggest bet: 40,000 views is the campaign target. Agencies quoted SGD 3,000 and two weeks. You build a production line instead: a researcher grounds every claim in your source files, a scriptwriter writes the scenes, a producer renders with HyperFrames, a voice-over artist narrates, and a reviewer checks the cut and sends you a link to watch.

## You will deliver
- Video skill installed from Capabilities → Skills: HyperFrames (Remotion, Manim for reference)
- A video team created by prompt: video-researcher, scriptwriter, voice-over, video-producer, video-reviewer
- outputs/video/: research.md, script.md, narration audio, final.mp4, review.md
- Review link on Telegram; your APPROVE with the video's SHA-256
- PP Task 3: TWO screenshots — Kanban board + video playing

## Who does what
- **Agents:** 5 agents created by Mia from one prompt, working on a Kanban board
- **You (the human):** Approve the script, watch the exact cut, approve or request one revision

## Before you start
- Activity 4 done
- This lab's data/ dragged into Desktop/kopi-kaki (souls/, tasks/, DESIGN.md and video-qa-checklist.md)
- Lab laptops: Node.js 22+ and FFmpeg for HyperFrames — Mia checks them for you; the trainer installs anything missing before class
- Settings → Voice → Text to speech set to Edge (free) from the Topic 2 setup

## Concepts in action
- Grounding: the researcher may only use facts it can point to in a source file (the RAG idea)
- An independent reviewer catches what the maker misses
- A changed video needs a new review: approval belongs to one exact file
- Human gates are Kanban cards only you can complete

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `skills/brand-compliance-audit/SKILL.md` | Agent skill (SKILL.md) |
| `DESIGN.md` | Visual identity for HyperFrames |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `souls/video-researcher.SOUL.md` | Role + rules for one studio profile |
| `souls/scriptwriter.SOUL.md` | Role + rules for one studio profile |
| `souls/voice-over.SOUL.md` | Role + rules for one studio profile |
| `souls/video-producer.SOUL.md` | Role + rules for one studio profile |
| `souls/video-reviewer.SOUL.md` | Role + rules for one studio profile |
| `tasks/v1-research.md` | Task brief for one Kanban card |
| `tasks/v2-script.md` | Task brief for one Kanban card |
| `tasks/v3-voice.md` | Task brief for one Kanban card |
| `tasks/v4-produce.md` | Task brief for one Kanban card |
| `tasks/v5-review.md` | Task brief for one Kanban card |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-05-Instructions.pdf`](LAB-05-Instructions.pdf).

## Steps

### 1. Copy the video team files (2 min)
In Finder (Mac) or File Explorer (Windows), open this lab's data folder from the unzipped course files, select everything and drag it into your Desktop/kopi-kaki folder. Choose Skip (do not replace) for files that already exist.

✓ **Expected:** souls/ now also lists video-researcher, scriptwriter, voice-over, video-producer and video-reviewer; tasks/ has v1–v5.

### 2. Install the video skill — by asking (8 min)
HyperFrames (HeyGen) writes each scene as HTML and renders an MP4 — the team's renderer. Remotion (React) and Manim (maths animation) are alternatives worth knowing. You can also search 'hyperframes' in Capabilities → Skills and click Install.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Install the official hyperframes skill from the Hermes skills hub. Read its SKILL.md first and tell me what it needs. Then check that this laptop has what it needs (Node.js 22 or newer, FFmpeg, a browser) and run its health check. If anything is missing, tell me exactly what to ask the trainer to install. Do not change system settings.
```

✓ **Expected:** 'hyperframes' appears in Capabilities → Skills and the health check passes (or Mia names what is missing).

### 3. One prompt: hire the video team and build its Kanban board (10 min)
This is the prompt method: you describe the team and the work; Mia creates the five agents (they also appear in the Bots tab) and the Kanban board with your two HUMAN gates.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Build my video production team and its Kanban board. Workspace: Desktop/kopi-kaki.
1. Create these five agents (Hermes profiles) by cloning your settings, each with its role file as SOUL.md and the description shown:
- video-researcher: Extracts the facts the video may use: claim | source file | exact quote (role file souls/video-researcher.SOUL.md)
- scriptwriter: Turns research.md into a 20-second, 4-scene script, then waits for the founder (role file souls/scriptwriter.SOUL.md)
- voice-over: Records the narration from the APPROVED script with Hermes text-to-speech (role file souls/voice-over.SOUL.md)
- video-producer: Renders the APPROVED script into a 1080x1920 MP4 with HyperFrames (role file souls/video-producer.SOUL.md)
- video-reviewer: Independently checks the video against the QA checklist and sends the founder a review link (role file souls/video-reviewer.SOUL.md)
2. Create a Kanban board for tenant kopi-video with these cards:
   1 Research the launch video · video-researcher · body tasks/v1-research.md
   2 Write the 20-second script · scriptwriter · parent 1 · body tasks/v2-script.md
   3 HUMAN: approve the script · unassigned · parent 2 · only I complete it
   4 Record the voice-over · voice-over · parent 3 · body tasks/v3-voice.md
   5 Render the video · video-producer · parents 3 and 4 · skill hyperframes · body tasks/v4-produce.md
   6 Review and send me the link · video-reviewer · parent 5 · body tasks/v5-review.md
   7 HUMAN: approve the exact video · unassigned · parent 6 · only I complete it
3. Show me the agents and the cards (ID, assignee, parents) as two tables. Never publish or post the video anywhere.
```

✓ **Expected:** Two tables: five agents, seven cards with two unassigned HUMAN cards. The agents appear in the Bots tab.

### 4. Watch the board work (8 min)
Open Kanban in the left sidebar and choose the kopi-video board. A card runs only when every parent is done; your HUMAN card holds everything after it. Open a card to read its run history and output.

✓ **Expected:** Research runs first, then the script; card 3 (yours) waits.

### 5. Check the research — grounding (5 min)
The researcher may only use facts it can point to in a source file: this is grounding, the same idea as retrieval-augmented generation (RAG). Check two claims yourself.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Open outputs/video/research.md for me and pick two claims. For each, show me the exact line in the source file that supports it.
```

✓ **Expected:** Every claim names its source file and quote; unsupported ideas are marked UNVERIFIED.

### 6. Approve the script — your first gate (5 min)
Read script.md: four scenes, 20 seconds, on-screen text of seven words or fewer per scene, price SGD 6.80, launch 1 Dec 2026, no health or halal claims. Approve it, or ask for one change first.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
I have read outputs/video/script.md and APPROVE it as written. Record my approval with today's date in outputs/video/approvals.md, then complete the 'HUMAN: approve the script' card on the kopi-video board for me.
```

✓ **Expected:** The voice-over and render cards start.

### 7. Production and voice-over (20 min)
The voice-over agent records the narration with Hermes's free text-to-speech; the producer builds the HyperFrames video and adds the narration. Check the real file, not the success message.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Check outputs/video/final.mp4 for me: does it exist, what are its width, height and duration, and does it have an audio track? Answer in one line per check.
```

✓ **Expected:** final.mp4 exists, 1080×1920, about 20 seconds, with audio.

### 8. Independent review and the review link (10 min)
The reviewer checks every scene against video-qa-checklist.md (V1–V9) and the sources, writes review.md with the file's SHA-256 fingerprint, starts a local link and messages you on Telegram. The link works on your laptop only.

✓ **Expected:** A Telegram message with the review link (http://localhost:8765/final.mp4), PASS/FAIL per check and the SHA-256.

### 9. Approve the exact video — your final gate (10 min)
Watch the whole video from the link. If anything is wrong, request one revision: the producer re-renders, the reviewer re-checks, and the new file gets a new fingerprint — your old approval does not carry over.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
I watched http://localhost:8765/final.mp4 to the end. Check that its SHA-256 matches review.md. If it matches, record 'APPROVE <sha256>' with today's date in outputs/video/approvals.md and complete the 'HUMAN: approve the exact video' card for me. Do not post or publish the video anywhere.
```

✓ **Expected:** approvals.md shows APPROVE with the same fingerprint as review.md.

### 10. Capture your PP Task 3 evidence (5 min)
Take TWO readable screenshots of your own work: (A) the Kanban view in Hermes Desktop showing the agent names, a dependency or HUMAN gate and the video task; (B) final.mp4 playing in a media player. Hide keys and private data. Keep final.mp4, research.md, review.md and approvals.md.

### 11. Reflect: what did the team buy you? (5 min)
Compare effort, cost and quality.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Summarise the kopi-video run: total time, number of runs per card, what the reviewer caught, my revisions and an estimated model cost. Compare with an agency quote of SGD 3,000 and two weeks. What would you change in one role file to cut my review time next week?
```

✓ **Expected:** An honest summary including what failed.

## Verification / checkpoint
- [ ] hyperframes installed and its health check passes
- [ ] Five video agents and a seven-card board with two HUMAN gates, created by one prompt
- [ ] research.md links every claim to a source file
- [ ] final.mp4 is 1080×1920, ~20 s, with narration
- [ ] review.md passes V1–V9 with evidence; approvals.md fingerprint = file fingerprint
- [ ] PP Task 3: two screenshots — Kanban board and the video playing

**Checkpoint:** final.mp4 plays at 1080×1920, review.md passes V1–V9 with evidence, and your APPROVE names the same SHA-256 as the file you watched.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Cards stay waiting and never run | Keep Hermes Desktop open. Ask Mia: 'Why is card <n> on kopi-video not running?' |
| HyperFrames health check fails | Node.js or FFmpeg is missing: ask the trainer; Mia tells you exactly which one. |
| Render card ran before your approval | The card was created without the HUMAN card as parent. Ask Mia to block it, fix the parent and re-run. |
| No audio in final.mp4 | Ask Mia to check the narration file exists and to have the producer re-render with it. |
| Review link does not open | Open it on the same laptop; ask the reviewer to start the link again. |

## Stretch challenge
Ask Mia to add a second cut: a 1:1 square version from the same script. How much extra review does a second format cost you?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
