# Lab 29 — Configure Paperclip

## Objective
Configure **Nimbus Coffee, Inc.** so its agents can do real work: set the **monthly budget cap**, connect a **workspace folder** where agents write actual files, and adjust company settings. By the end the company will show a configured budget and a connected workspace ready to hold real deliverables.

## Prerequisites
- **Lab 28 complete**: the OpenAI Codex adapter shows as available in Settings.
- Paperclip running at `http://localhost:3100` with the Nimbus Coffee company created (Lab 27).
- Write access to a folder in your home directory for the workspace.

## Estimated Time
20–30 minutes

## 📺 Reference Video
[Configure Paperclip](https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4)

## Steps

1. **Watch the reference video for this lab.** It walks through the company settings screen — budget cap, workspace connection, and the other company options.

   [https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4](https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4)

2. **Open the company's settings in the dashboard.** At `http://localhost:3100`, open **Nimbus Coffee, Inc.** and go to its **Settings**. This is the per-company control panel (distinct from the app-wide Settings you used for adapters in Lab 28).

3. **Set or adjust the monthly budget cap.** Enter the maximum the company may spend per month. This cap is the governance rail you will exercise in Lab 33 (an 80% warning and a 100% pause). Set a deliberate figure you are comfortable letting agents spend against.

   > Field name/units are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

4. **Connect a workspace folder so agents create real deliverables.** First create the folder on your machine:

   ```bash
   mkdir -p ~/paperclip-workspace/nimbus-coffee
   ```

   Then, in the company settings, connect this folder as the company's **workspace**. This is where agents will write real files — landing-page code, marketing copy, spreadsheets — instead of just talking about them. (If Paperclip runs in Docker, confirm this path is mounted into the container as shown in the video.)

5. **Save the configuration and confirm it persists.** Save the settings, reload the page, and confirm the budget and the connected workspace path are still shown. Persistence matters — it proves the config was written to the database, not just held in the browser.

## Verification / Expected Output
- The company shows the **configured monthly budget**.
- The company shows a **connected workspace folder** pointing at `~/paperclip-workspace/nimbus-coffee`.
- Both values survive a page reload.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Workspace path not accepted | The folder must exist and be readable/writable. Re-run the `mkdir -p` command and re-enter the path. |
| Agents later can't write to the workspace | If Paperclip is containerised, the host folder must be mounted into the container — verify the mount in the video / docs (<https://docs.paperclip.ing>). |
| Budget field rejects your value | Check the expected units/format (per-month amount) shown in the video; re-enter. |
| Settings revert after reload | The save didn't reach the database. Confirm the stack is healthy and re-save; check the compose logs for errors. |
| Can't find the workspace setting | UI wording is version-specific — locate the workspace/folder option per the video / docs (<https://docs.paperclip.ing>). |

## Exercise / Challenge
Set the Nimbus Coffee monthly budget to a deliberately small figure (something you expect a busy company to approach), then note the exact 80% and 100% amounts it implies. You will use these in Lab 33 to trigger the warning and pause rails on purpose — so record them now alongside the workspace path.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
