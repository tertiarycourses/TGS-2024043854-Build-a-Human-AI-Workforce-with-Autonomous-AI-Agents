# Lab 5 — Activity 5 — Your Video Production Team

**Day 2 · Topic 3 · 130 min · Multi-agent production line + human review · LO3**

> Research, script, render, voice-over, review — five Hermes bots make the 20-second launch video, then send you a link. Nothing ships until you approve it.

## Goal
Run a multi-agent video team with Kanban dependencies, source checks and an independent review, and accept only the exact video version you have watched (LO3; PP Task 3).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. The launch video is your biggest bet: 40,000 views is the campaign target. Agencies quoted SGD 3,000 and two weeks. You build a production line instead: a researcher grounds every claim in your source files, a scriptwriter writes the scenes, a producer renders with HyperFrames, a voice-over artist narrates, and a reviewer checks the cut and sends you a link to watch.

## You will deliver
- Video skills installed: HyperFrames (Remotion, Manim for reference)
- Five profiles: researcher, scriptwriter, video-producer, voice-over, video-reviewer
- outputs/video/: research.md, script.md, narration.wav, final.mp4, review.md
- Review link on Telegram; your APPROVE with the video's SHA-256
- PP Task 3: TWO screenshots — Kanban board + video playing

## Who does what
- **Agents:** 5 Hermes profiles shown as bots on a Kanban board
- **You (the human):** Approve the script, watch the exact cut, approve or request one revision

## Before you start
- Activity 4 done: profiles, Kanban and the running gateway work
- Node.js 22+ and FFmpeg for HyperFrames; Python 3.10+ for the local voice (Kokoro)
- This lab's data/ copied into ~/kopi-kaki (souls/, tasks/, DESIGN.md and video-qa-checklist.md are included)

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

### 1. Copy the lab data (2 min)
Copy the video team's role files, task briefs, design rules and QA checklist into your workspace.

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/kopi-kaki/outputs/video
ls ~/kopi-kaki/souls ~/kopi-kaki/tasks
```

✅ **Expected:** souls/ now also lists scriptwriter, video-producer, voice-over and video-reviewer.

### 2. Install the video skills and tools: HyperFrames, Remotion, Manim (10 min)
HyperFrames (HeyGen) writes videos as HTML and renders them to MP4 — the team's main renderer (Node.js 22+ and FFmpeg). Remotion (React) and Manim (Python maths animation; Hermes ships a manim-video skill, Manim itself needs Python 3.10+ and LaTeX) are alternatives worth knowing. Read each SKILL.md before you trust it.

```bash
hermes skills install official/creative/hyperframes
npx hyperframes doctor
npx skills add remotion-dev/skills -a hermes-agent -g
hermes skills list | grep -i -E 'hyperframes|remotion|manim'
# optional, for Manim: python3 -m pip install manim && manim --version
```

✅ **Expected:** hyperframes doctor reports Node, FFmpeg and a browser OK; the skills appear in hermes skills list.

### 3. Give the team a voice: local text-to-speech (5 min)
HyperFrames can narrate locally with the free Kokoro voice model — no account and no cost. Test it once.

```bash
python3 -m pip install kokoro-onnx soundfile
npx hyperframes tts "Gula Melaka Cold Brew. A taste of the kopitiam, slow-brewed cold." --voice af_heart --output ~/kopi-kaki/outputs/video/voice-test.wav
```

✅ **Expected:** voice-test.wav plays a clear English voice.

### 4. Staff the production line: five profiles (6 min)
One researcher grounds every fact; the reviewer is independent of the producer. Each SOUL.md says what the role owns and what it must never do.

```bash
hermes profile create scriptwriter --clone --description "Turns research.md into a 20-second, 4-scene script with on-screen text and narration"
hermes profile create video-producer --clone --description "Renders the approved script into a 1080x1920 MP4 with HyperFrames; owns outputs/video/final.mp4"
hermes profile create voice-over --clone --description "Writes narration.txt from the approved script and records narration.wav with hyperframes tts"
hermes profile create video-reviewer --clone --description "Independently checks the video against video-qa-checklist.md and the sources; sends the founder a review link"
for p in scriptwriter video-producer voice-over video-reviewer; do cp ~/kopi-kaki/souls/$p.SOUL.md ~/.hermes/profiles/$p/SOUL.md; done
cp ~/kopi-kaki/souls/video-researcher.SOUL.md ~/.hermes/profiles/researcher/SOUL.md
hermes profile list
```

✅ **Expected:** researcher (now the video researcher), scriptwriter, video-producer, voice-over and video-reviewer are listed.

### 5. Build the production board with two human gates (8 min)
Two cards are yours: approve the script before anything is rendered, and approve the exact final file. The producer and voice-over both depend on your script approval; the reviewer waits for both.

**Prompt** — paste into *Hermes Desktop → default profile (Mia), started in ~/kopi-kaki*:

```text
Use the Kanban tools to build the board for tenant kopi-video, workspace ~/kopi-kaki.
1. Research the launch video - assignee researcher - body from tasks/v1-research.md.
2. Write the 20-second script - assignee scriptwriter - parent: 1 - body from tasks/v2-script.md.
3. HUMAN: approve the script - unassigned - parent: 2. Only I complete it.
4. Record the voice-over - assignee voice-over - parent: 3 - body from tasks/v3-voice.md.
5. Render the video - assignee video-producer - parents: 3 and 4 - skill hyperframes - body from tasks/v4-produce.md.
6. Review and send me the link - assignee video-reviewer - parent: 5 - body from tasks/v5-review.md.
7. HUMAN: approve the exact video - unassigned - parent: 6. Only I complete it.
Show the card IDs, assignees and parents as a table. Never publish or post the video anywhere.
```

✅ **Expected:** A seven-card table with two unassigned HUMAN cards.

### 6. Research with source checks (8 min)
The researcher may only use facts it can point to in a source file: this is grounding, the same idea as retrieval-augmented generation (RAG). Open research.md when the card is done and check two claims yourself.

```bash
hermes kanban watch --tenant kopi-video
cat ~/kopi-kaki/outputs/video/research.md
```

✅ **Expected:** Every claim in research.md names its source file and line (e.g. campaign-brief.md); unsupported ideas are marked UNVERIFIED.

### 7. Approve the script — your first gate (5 min)
Read script.md: four scenes, 20 seconds, on-screen text of seven words or fewer per scene, price SGD 6.80, launch 1 Dec 2026, no health or halal claims. Approve it, or ask for one change first.

```bash
hermes kanban list --tenant kopi-video          # find the 'HUMAN: approve the script' card id
hermes kanban complete <card_id>
```

**Prompt** — paste into *Hermes Desktop → default profile (Mia)*:

```text
I have read outputs/video/script.md and APPROVE it as written. Note my approval with today's date in outputs/video/approvals.md. I have completed the HUMAN script card myself.
```

✅ **Expected:** The voice-over and render cards start.

### 8. Production and voice-over (20 min)
The voice-over profile records narration.wav; the producer builds the HyperFrames composition, adds the narration and renders. Check the real file, not the success message.

```bash
ls -la ~/kopi-kaki/outputs/video/
ffprobe -v error -show_entries stream=width,height -show_entries format=duration -of json ~/kopi-kaki/outputs/video/final.mp4
```

✅ **Expected:** final.mp4 exists, 1080×1920, about 20 seconds, with an audio stream.

### 9. Independent review and the review link (10 min)
The reviewer checks every scene against video-qa-checklist.md (V1–V9) and the sources, writes review.md, computes the file's SHA-256 and sends you a link on Telegram. The link serves the file from your laptop only.

```bash
cd ~/kopi-kaki/outputs/video && python3 -m http.server 8765
# review link: http://localhost:8765/final.mp4
shasum -a 256 final.mp4      # Windows: certutil -hashfile final.mp4 SHA256
```

✅ **Expected:** A Telegram message with the review link, PASS/FAIL per check and the SHA-256.

### 10. Approve the exact video — your final gate (10 min)
Watch the whole video from the link. If anything is wrong, request one revision: the producer re-renders, the reviewer re-checks, and the new file gets a new hash — your old approval does not carry over.

```bash
shasum -a 256 ~/kopi-kaki/outputs/video/final.mp4
hermes kanban complete <human_video_card_id>      # only after the hashes match
```

**Prompt** — paste into *Hermes Desktop → default profile (Mia)*:

```text
I watched http://localhost:8765/final.mp4 to the end. Check that its SHA-256 matches review.md. If it matches, record 'APPROVE <sha256>' with today's date in outputs/video/approvals.md. Do not post or publish the video anywhere.
```

✅ **Expected:** approvals.md shows APPROVE with the same hash as review.md.

### 11. Capture your PP Task 3 evidence (5 min)
Take TWO readable screenshots of your own work: (A) the Kanban board (dashboard Kanban view) showing the profile/bot names, a dependency or HUMAN gate and the video task; (B) final.mp4 playing in a media player. Hide keys and private data. Keep final.mp4, research.md, review.md and approvals.md.

### 12. Reflect: what did the team buy you? (5 min)
Compare effort, cost and quality.

**Prompt** — paste into *Hermes Desktop → default profile (Mia)*:

```text
Summarise the kopi-video run: total time, number of runs per card, what the reviewer caught, my revisions and an estimated model cost. Compare with an agency quote of SGD 3,000 and two weeks. What would you change in one SOUL.md to cut my review time next week?
```

✅ **Expected:** An honest summary including what failed.

## Verification / checkpoint
- [ ] Video skills installed and `npx hyperframes doctor` passes
- [ ] research.md links every claim to a source file
- [ ] final.mp4 is 1080×1920, ~20 s, with narration
- [ ] review.md passes V1–V9 with evidence; approvals.md hash = file hash
- [ ] PP Task 3: two screenshots — Kanban board and the video playing

**Checkpoint:** final.mp4 plays at 1080×1920, review.md passes V1–V9 with evidence, and your APPROVE names the same SHA-256 as the file you watched.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `hyperframes doctor` fails on FFmpeg | Install FFmpeg (macOS `brew install ffmpeg`, Windows `winget install ffmpeg`) and reopen the terminal. |
| Render card runs before script approval | The render card was created without the HUMAN card as parent — block it, fix the parent, re-run. |
| No audio in final.mp4 | Check narration.wav exists and the composition references it; ask the producer to re-render. |
| Review link does not open | Keep the http.server terminal open; open the link on the same laptop. |

## Stretch challenge
Ask the producer for a 9:16 and a 1:1 cut from the same composition. How much extra review does a second format cost you?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
