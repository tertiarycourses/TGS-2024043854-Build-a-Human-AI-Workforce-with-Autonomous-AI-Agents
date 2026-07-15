# Lab 11 — Use Case — Make a Video with Hyperframe

## Objective
LO5: Apply the agent to a real creative use case — produce a video with Hyperframe. You will put **Athena** to work on an end-to-end creative task: set up the Hyperframe video tool, write a concrete creative brief, have the agent generate a short video, iterate once on feedback, and export the finished file.

## Prerequisites
- **Lab 1–10 complete** — Hermes running with a provider and tools/MCP configured.
- Access to the Hyperframe video tool (account/credentials if required).

## Estimated Time
40–50 minutes

## 📺 Reference Video
[Use Case — Make a Video with Hyperframe](https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)

## Steps

### 1. Watch the reference video
Before touching the keyboard, watch the full workflow once so you know what "good" looks like: the presenter connects Hyperframe, writes a brief, generates, reviews, and iterates. Note the exact way the tool is invoked in your Hermes version — that is the part most likely to differ between builds.

[https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3](https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)

### 2. Install / verify the Hyperframe video skill
Wire Hyperframe into Athena the same way you added skills in Lab 4. In a terminal, search the skills hub for the Hyperframe (video) skill and install the match; if your build integrates Hyperframe as an MCP server or Tool Gateway tool instead, add it the way you added tools in Lab 6.

```bash
hermes skills search hyperframe
hermes skills install <owner/skills/hyperframe>
```
Or just ask the agent: "Find the Hyperframe video skill on the skills hub and install it"


> The exact skill/tool name is version-specific — verify in the video / docs (https://hermes-agent.nousresearch.com/docs/).

### 3. Set the Hyperframe credential via config
If Hyperframe needs an API key or account token, store it through Hermes config so it never sits in plain text. Get the key from your Hyperframe account page, then set it and confirm no error is printed.

```bash
hermes config set HYPERFRAME_API_KEY <your-key>
```
Or just ask the agent: "Save my Hyperframe API key securely in your config"


### 4. Confirm the tool is loaded, then start a session
Run the health check and confirm it reports green with the new skill/tool listed. Then open a chat session (TUI or Desktop app) and ask Athena *"What video tools do you have?"* — it should name Hyperframe in its reply. If it doesn't, restart Hermes so the new tool is picked up.

```bash
hermes doctor
hermes --tui
```
Or just ask the agent: "Run a health check and confirm the Hyperframe skill is loaded"


### 5. Brief the agent with a concrete 3-sentence brief
Type a tight, three-sentence creative brief covering **topic**, **style/tone**, and **length + extras**. A concrete brief is the single biggest lever on output quality — vague briefs produce generic videos. For example:

> *"Make a 30-second explainer video introducing 'Athena, my AI chief of staff'. Clean, modern visual style with an upbeat tone. Keep it to 30 seconds and add on-screen captions."*

### 6. Have the agent generate the video and wait for the render
Ask Athena to generate the video now. You should see the agent invoke the Hyperframe tool in the session transcript (a tool-call entry), then wait — rendering typically takes a few minutes for a 30-second clip. When it finishes, Athena reports back with a link or file path to the rendered video; if the tool call errors, check the credential from step 3.

### 7. Play the result, give one round of feedback, and regenerate
Open and play the video end-to-end. Then give Athena one specific round of feedback — change exactly the things that bothered you, e.g. *"Slow the pacing, make the captions larger, and warm up the colour palette"* — and ask it to regenerate. Compare the two versions; you should see your feedback reflected in version 2.

### 8. Export / save the final video and note where the file lands
Ask Athena to save/export the final cut and tell you the exact file path. Outputs typically land in the session's workspace under your Hermes home directory — open it and confirm the file plays from disk:

```bash
open ~/.hermes/
```
Or just ask the agent: "Where did you save the final video? Give me the file path"


> The exact output folder is version-specific — verify in the video / docs (https://hermes-agent.nousresearch.com/docs/). Copy the file somewhere permanent; session workspaces can be cleaned up.

## Verification / Expected Output
- The agent **produces a playable video** from your 3-sentence brief using Hyperframe.
- One round of feedback produces a **visibly updated version 2**.
- You can **locate the exported file on disk** and play it outside Hermes.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Agent can't find Hyperframe | The tool isn't connected — install the skill (or add it as MCP/Tool Gateway), restart, and re-run `hermes doctor`. |
| Generation fails / errors | Check `HYPERFRAME_API_KEY` is set and valid, and that the brief isn't violating length/content limits. |
| Video renders but ignores the brief | Make the brief more specific (style, length, tone) and regenerate — one change per sentence. |
| Render takes very long | Long/large videos take time; shorten to 15–30 seconds for faster iteration loops. |
| Can't find the output file | Ask Athena for the exact path; check the session workspace under `~/.hermes/`. |
| Unsure how Hyperframe integrates | The integration path is build-specific — verify in the video / docs link above. |

## Exercise / Challenge
Produce a **15-second promo** for Athena in two different visual styles (e.g. "corporate" vs "playful") by changing only the style words in the brief. Compare the two outputs and write one sentence on which better fits a "personal chief of staff" brand — practising prompt-driven creative iteration.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
