# Lab 25 — Dreaming — Idle Reflection & Self-Improvement

## Objective
Enable OpenClaw's **dreaming** feature so your **Nimbus Supplies** back-office agent uses idle time to reflect on its memory, consolidate what it has learned, and propose useful follow-up actions and skill improvements — then inspect and accept what it produced. By the end you will have an agent that turns downtime into self-improvement instead of sitting idle.

> The `openclaw dreaming` / `openclaw dream` commands below are best-guess syntax. **Verify the exact syntax in the reference video and docs (<https://docs.openclaw.ai/>)** before relying on them in production.

## Prerequisites
- A working OpenClaw install with a running gateway (Labs 15–24). Confirm with `openclaw gateway status`.
- At least one configured model provider (Lab 16) — dreaming needs a model to reflect with.
- Some accumulated agent **memory** to reflect on: run a few Nimbus Supplies conversations/tasks first (Labs 17–24) so there is material to "dream" about.
- A terminal with the `openclaw` CLI on your `PATH`.

## Estimated Time
20–30 minutes

## 📺 Reference Video
[OpenClaw functions reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Watch the OpenClaw functions reference video.** Open the playlist and watch the segment on the dreaming / idle-reflection feature. Note how the presenter enables it and where the produced insights appear — the on-screen command names are your ground truth for the steps below.

   [https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

2. **Enable the dreaming feature in OpenClaw config.** This flips the setting that lets the gateway schedule reflection cycles when the agent is idle:

   ```bash
   openclaw config set dreaming.enabled true
   ```

   This writes the flag into your OpenClaw config (under `~/.openclaw/`). After it returns, the gateway will begin scheduling dream cycles during idle windows.

   > Verify syntax in the video/docs (<https://docs.openclaw.ai/>) — the exact config key may differ by version.

3. **Let the agent sit idle so a dream cycle runs — or trigger one manually.** Rather than wait for a natural idle window, force a cycle now so you can observe it immediately:

   ```bash
   openclaw dream run
   ```

   This kicks off one reflection pass: the agent reads its recent memory, consolidates recurring themes (e.g. repeated Nimbus Supplies supplier questions), and drafts follow-ups and skill tweaks. You will see log lines as the cycle progresses.

   > Verify syntax in the video/docs (<https://docs.openclaw.ai/>).

4. **Review what the dream produced.** List the insights, follow-ups, and skill suggestions the cycle generated:

   ```bash
   openclaw dream list
   ```

   You should see one or more entries — for example, a proposal to create a reusable "supplier price check" skill, or a follow-up to email a customer who was waiting on a quote. Each entry is a *proposal*, not an action already taken.

   > Verify syntax in the video/docs (<https://docs.openclaw.ai/>).

5. **Accept a useful follow-up the agent proposed.** In the dashboard (or via the CLI shown in the video), open one proposal that genuinely helps Nimbus Supplies and approve it. Accepting promotes the proposal into a real action or a saved skill; declining discards it. This human review step keeps you in control of what the agent's downtime actually changes.

## Verification / Expected Output
- `openclaw config set dreaming.enabled true` returns without error and the flag is persisted (re-reading the config shows `dreaming.enabled = true`).
- A dream cycle runs during idle time (or when triggered) and produces **reviewable insights / follow-ups drawn from the agent's memory**.
- `openclaw dream list` shows at least one entry describing a consolidation, a proposed follow-up, or a skill improvement tied to your Nimbus Supplies history.
- After you accept a proposal, it disappears from the pending list and appears as an action taken or a new saved skill.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `unknown command: dream` | The CLI verb differs in your version. Check the exact command in the reference video and <https://docs.openclaw.ai/>, then re-run. |
| Dream cycle produces nothing | The agent has no memory to reflect on. Run a few Nimbus Supplies conversations/tasks first, then re-run `openclaw dream run`. |
| `no model provider configured` | Dreaming needs a model. Configure a provider (Lab 16) and re-run `openclaw doctor`. |
| Config flag does not persist | You may lack write access to `~/.openclaw/`. Check permissions, or set the key via the dashboard settings shown in the video. |
| Cycles never fire on their own | The idle threshold may be long. Trigger manually with `openclaw dream run`, or lower the idle window in config (verify key in docs). |

## Exercise / Challenge
Seed the agent's memory with three realistic Nimbus Supplies interactions (a supplier price question, a late-quote complaint, and a repeat reorder). Trigger a dream cycle, then read `openclaw dream list` and write one sentence for each proposal saying whether you would accept or decline it and why. Accept the single most valuable one and confirm it becomes a saved skill or a scheduled follow-up — this is how you let idle time quietly harden your back office.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
