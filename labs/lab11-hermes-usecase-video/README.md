# Lab 11 — Use Case — Make a Video with Hyperframe

## Objective
LO5: Apply the agent to a real creative use case — produce a video with Hyperframe. You will put **Athena** to work on an end-to-end creative task: use the agent to drive the Hyperframe tool and generate a short video from a concept brief, then review and refine the result.

## Prerequisites
- **Lab 1–10 complete** — Hermes running with a provider and tools/MCP configured.
- Access to the Hyperframe video tool (account/credentials if required).

## Estimated Time
40–50 minutes

## 📺 Reference Video
[Use Case — Make a Video with Hyperframe](https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)

## Steps

### 1. Watch the reference video
See the full workflow of driving Hyperframe through the agent to produce a video:

[https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3](https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)

### 2. Connect / set up the Hyperframe video tool for the agent
Wire the Hyperframe tool into Athena so the agent can invoke it.

> This may be an MCP server, a skill, or a Tool Gateway integration depending on your build. Add Hyperframe the same way you added tools in Lab 6, supplying any required API key via `hermes config set`. Verify the exact integration path in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 3. Brief the agent with a short video concept
Give Athena a clear, concise creative brief — topic, style, and length:

> Conversational step. For example: *"Make a 30-second explainer video introducing 'Athena, my AI chief of staff'. Clean, modern style, upbeat tone, with on-screen captions."* A tight brief yields a better first result.

### 4. Have the agent generate the video with Hyperframe
Ask Athena to generate the video. The agent calls Hyperframe with your brief and waits for the render:

> Confirm the agent invokes Hyperframe and reports back with a link/file to the rendered video. Rendering may take a few minutes.

### 5. Review the output and refine the brief to regenerate if needed
Play the video, then refine the brief (pacing, style, wording) and ask Athena to regenerate. Iterate until it meets your bar.

## Verification / Expected Output
- The agent **produces a playable video** from your brief using Hyperframe.
- You can iterate: a refined brief produces an updated video.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Agent can't find Hyperframe | The tool isn't connected — add it (as MCP/skill/Tool Gateway) and set any required key; see docs. |
| Generation fails / errors | Check the Hyperframe credential and that your brief isn't violating length/content limits. |
| Video renders but ignores the brief | Make the brief more specific (style, length, tone); regenerate. |
| Render takes very long | Large/long videos take time; shorten the length in the brief for faster iteration. |
| Unsure how Hyperframe integrates | The integration path is build-specific — verify in the video / docs link above. |

## Exercise / Challenge
Produce a **15-second promo** for Athena in two different visual styles (e.g. "corporate" vs "playful") by changing only the style words in the brief. Compare the two outputs and write one sentence on which better fits a "personal chief of staff" brand — practising prompt-driven creative iteration.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
