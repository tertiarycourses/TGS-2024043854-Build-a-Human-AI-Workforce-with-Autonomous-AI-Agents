# Lab 3 — Memory and Plugins

## Objective
LO2: Give the agent persistent memory and extend it with plugins. You will explore Hermes' three-layer memory (agent-curated notes, FTS5 cross-session recall, and Honcho user modelling), teach **Athena** a durable preference, recall it in a fresh session, and enable a plugin to extend behaviour.

## Prerequisites
- **Lab 1 and Lab 2 complete** — Hermes installed and the local deployment running.
- The TUI (`hermes --tui`) or Desktop app working and connected to your provider.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Memory and Plugins](https://www.youtube.com/watch?v=ZKZLko9kLm4&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=4)

## Steps

### 1. Watch the reference video
Watch the video to see how Hermes stores memory across the three layers and how plugins are enabled:

[https://www.youtube.com/watch?v=ZKZLko9kLm4&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=4](https://www.youtube.com/watch?v=ZKZLko9kLm4&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=4)

### 2. Teach Athena a durable preference
Start a session (`hermes --tui`) and give Athena a clear, memorable instruction that should persist. Explicitly asking it to *remember* nudges the agent to write the fact into its curated-notes memory layer:

```text
Remember I prefer concise, bulleted summaries.
```

Confirm the agent acknowledges (e.g. "Got it — I'll keep summaries concise and bulleted."). Then end the session.

### 3. Start a new session and confirm the preference is recalled
Resume the conversation in a fresh session. The `--continue` flag brings back prior context so you can test cross-session recall:

```bash
hermes --continue
```

Ask something like *"How do you format summaries for me?"* — Athena should recall the bulleted-summary preference **without you repeating it**. This proves the FTS5 cross-session recall / curated-notes memory is working.

### 4. Inspect stored memory / sessions
List the stored sessions so you can see the memory Hermes is persisting behind the scenes:

```bash
hermes sessions list
```

You should see your earlier session(s) listed with identifiers/timestamps. This is where cross-session recall draws context from.

### 5. Enable a plugin to extend the agent
Enable a plugin to add capability beyond the base agent. Plugins are toggled from the Hermes plugins UI or config:

```text
# enable a plugin from the Hermes plugins UI/config
```

Open the plugins panel (Desktop app or the plugins section of `~/.hermes/config.yaml`), turn on a plugin, and restart the agent if prompted. Verify it in the agent's capability list.

> If the exact plugin-enable command/flag differs in your build, verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

## Verification / Expected Output
- A preference taught in one session (bulleted summaries) is **recalled in a new session** started with `hermes --continue`, with no re-prompting.
- `hermes sessions list` shows your stored sessions.
- The enabled plugin appears as active in the agent's capabilities and can be invoked.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| New session doesn't recall the preference | Make sure you used `hermes --continue` (not a brand-new session); re-teach the preference and phrase it as "Remember …". |
| `hermes sessions list` is empty | You never completed a session, or sessions are stored under a different profile — confirm you're the same user and provider is configured. |
| Plugin doesn't appear after enabling | Restart the agent/gateway so the plugin loads; confirm it's toggled on in the plugins UI/config. |
| Preference recalled but ignored in output | Restate it once; some models need the recalled note reinforced in the active turn. |
| Not sure where plugins live | Check the plugins section of `~/.hermes/config.yaml` or the Desktop app's Plugins panel; see the docs link above. |

## Exercise / Challenge
Teach Athena three durable facts about yourself (timezone, preferred meeting length, and a "never schedule before 9am" rule). Close the TUI, reopen with `hermes --continue`, and ask Athena to draft your ideal weekday schedule. Confirm it honours all three remembered facts — this shows memory feeding real planning behaviour.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
