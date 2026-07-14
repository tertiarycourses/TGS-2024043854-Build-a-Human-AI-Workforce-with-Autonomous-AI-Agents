# Lab 28 — Connect OpenAI Codex to Paperclip

## Objective
Give Paperclip's agents a **brain** by connecting the **OpenAI Codex** adapter, so the agents can reason, write code, and act. By the end the Codex adapter will show as **available** in Settings, and your Nimbus Coffee company will be ready to hire agents that can actually do work.

## Prerequisites
- **Lab 27 complete**: Paperclip running at `http://localhost:3100` with the Nimbus Coffee company created.
- An **OpenAI account** with access to the Codex CLI / model, and any required API key or login credentials.
- The **OpenAI Codex CLI** installable on the same machine (or wherever Paperclip can detect it).
- Terminal access to the machine running the Paperclip containers.

## Estimated Time
20–30 minutes

## 📺 Reference Video
[Connect OpenAI Codex to Paperclip](https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3)

## Steps

1. **Watch the reference video for this lab.** It shows exactly where Paperclip looks for the Codex adapter and what "available" looks like in Settings.

   [https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3](https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3)

2. **Install / log in to the OpenAI Codex CLI so Paperclip can detect it.** Follow the video's instructions to install the Codex CLI and authenticate (log in or supply your API key). Paperclip detects the adapter by finding this working Codex CLI/credentials on the host — so getting the login right here is the whole ballgame.

   > The exact install/login command is version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

3. **Open Settings → Agents / Adapters in the dashboard.** In Paperclip at `http://localhost:3100`, go to **Settings**, then the **Agents / Adapters** section. This is where Paperclip lists every model engine it can use to power agents.

4. **Confirm the OpenAI Codex adapter shows as "available".** Look for the **OpenAI Codex** entry and check its status reads **available** (not "not detected" / "unavailable"). Available means Paperclip successfully found and authenticated the Codex CLI and can route agent reasoning through it.

5. **Restart Paperclip if the adapter is not detected.** If Codex still shows unavailable after you have logged in, restart the stack so Paperclip re-scans for the adapter:

   ```bash
   docker compose -f docker-compose.quickstart.yml restart
   ```

   Then reload Settings → Agents / Adapters and re-check the status.

## Verification / Expected Output
- In **Settings → Agents / Adapters**, the **OpenAI Codex adapter is detected and shows as available**.
- The status persists after a page reload (and, if you restarted, after the containers come back up).
- No "no model configured" warning remains on the company page.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Codex adapter shows "not detected" | Confirm the Codex CLI is installed and logged in on the host, then `docker compose -f docker-compose.quickstart.yml restart`. |
| Adapter detected but "unauthorized" | Your OpenAI credentials/API key are invalid or expired. Re-authenticate the Codex CLI and restart. |
| Container can't see the host CLI | Paperclip may need the credentials mounted/passed into the container — verify the required mount/env in the video / docs (<https://docs.paperclip.ing>). |
| Settings section named differently | UI wording is version-specific — locate the Adapters/Models area per the video / docs (<https://docs.paperclip.ing>). |
| Adapter drops to unavailable intermittently | Rate limit or expired session. Check your OpenAI usage/limits and re-login. |

## Exercise / Challenge
After Codex shows available, open the company page for Nimbus Coffee and confirm the "no model" warning is gone. Then write two sentences: one explaining what the adapter actually does for an agent (reasoning + acting), and one predicting what would break in Lab 31 (hiring) if the adapter were unavailable — proving you understand why the brain must be connected before you staff the company.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
