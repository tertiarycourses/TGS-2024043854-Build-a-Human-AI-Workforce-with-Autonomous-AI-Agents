# Lab 28 — Setup Company, CEO & Mission

## Objective
LO2: Found the company — name, mission and the CEO agent. You will found **'Altera AI Blogs'**: create the company, write its mission (research the AI landscape daily and publish AI-related blogs end to end), set the monthly budget, then hire the **CEO agent** — the Chief Officer who will run the blog operation and report to you, the **Board**.

## Prerequisites
- **Lab 27 complete** — Paperclip running at `http://localhost:3100` with your Board account created.
- The Docker Compose stack still up (leave the compose terminal running or run it detached).

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Setup Company, CEO & Mission](https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3)

## Steps

### 1. Watch the reference video for this lab
[https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3](https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3)

### 2. Create the company 'Altera AI Blogs' from the company switcher
In the dashboard open the **company switcher** (top of the sidebar) and choose **New company**. Name it exactly:

> **Altera AI Blogs**

This is the zero-human company you will govern for the rest of the topic.

### 3. Write the mission — it steers every agent the company hires
In the company setup (or **Company Settings → Mission**), write the mission statement:

> *Research the AI landscape daily and publish AI-related blogs end to end*

The mission is not decoration: every agent the company hires reads it and aligns its work to it, so a vague mission produces a vague company.

### 4. Set the monthly budget cap in Company Settings
Open **Company Settings** and set the **monthly budget** cap (e.g. $50/month to start). The budget is the hard ceiling on what the whole company may spend on model calls — agents cannot exceed it, which makes it your first governance lever as the Board.

### 5. Hire the CEO agent (Chief Officer) and approve the hire — you are the Board
Hire the company's first agent: the **CEO (Chief Officer)**. The hire pauses at an **approval gate** — as the Board, review the CEO's mandate and click **Approve**. The CEO is the only agent that reports directly to you; every later hire will report to the CEO.

### 6. Open the Org page and confirm the structure: Board above the CEO
Open the **Org** page and check the org chart: **Board (you)** at the top, the **CEO** directly beneath. This two-node chart is the seed of the whole workforce you will grow in Labs 30–33.

## Verification / Expected Output
- The company **Altera AI Blogs** exists and is selected in the company switcher.
- The mission and a monthly budget cap are saved in Company Settings.
- An **approved CEO agent** sits under the Board on the org chart.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| No "New company" option in the switcher | You are not signed in as the Board account — sign in with the account you created in Lab 27. |
| Mission field won't save | Save the company first, then edit **Company Settings → Mission**; refresh the page and retry. |
| CEO hire stuck on "pending" | It is waiting at the approval gate — open the hire and click **Approve** as the Board. |
| CEO shows but does nothing | Normal at this point — the CEO needs a model adaptor (Lab 29) and tasks (Lab 30) before it can work. |
| Org chart is empty | Confirm you are viewing the right company in the switcher, then reload the Org page after the hire is approved. |

## Exercise / Challenge
Rewrite the mission twice — once too vague (*"do AI blogs"*) and once over-specific (a full paragraph of rules) — and note in two or three bullets how each version would mis-steer the CEO's hiring and task decisions. Restore the original mission when done, and check the Org page still shows Board → CEO.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
