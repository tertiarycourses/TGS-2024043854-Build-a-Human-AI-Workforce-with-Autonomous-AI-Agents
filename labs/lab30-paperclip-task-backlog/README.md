# Lab 30 — Create the Task Backlog

## Objective
LO3: Create a detailed task backlog that drives the company. You will write the backlog that runs the news desk for **Tertiary AI News Research**. Every task gets a precise **title AND a detailed description** — the description is the agent's brief, so vague tasks produce vague work. The core task is **hiring the team**; the rest build the news-research pipeline around it.

## Prerequisites
- **Lab 29 complete** — a detected, enabled model adaptor.
- Company, mission, budget and approved CEO in place (Lab 28).
- Paperclip running at `http://localhost:3100`.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Create the Task Backlog](https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5)

## Steps

### 1. Watch the reference video for this lab
[https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5](https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5)

Then open the **Tasks** board and create the six tasks below. For each one, paste the title and the full description — the description is the brief the assigned agent will actually work from.

### 2. Create the CORE task — 'Hire the core team and create a hiring plan' — and assign it to the CEO
Title:

> **Hire the core team and create a hiring plan**

Description:

> *Based on the coverage strategy, propose which agents to hire (research analyst, news writer, fact-checker, editor/publisher) with roles, budgets and reporting lines.*

**Assign it to the CEO.** This is the core task of the whole topic — in Lab 32 the CEO works it to staff the company.

### 3. Create 'Define the AI news coverage strategy and editorial plan'
Title:

> **Define the AI news coverage strategy and editorial plan**

Description:

> *Pick the beats (models, chips, policy, funding), the daily cadence, the briefing format and the quality bar for every published story.*

### 4. Create 'Scaffold the news-desk workspace & tooling foundation'
Title:

> **Scaffold the news-desk workspace & tooling foundation**

Description:

> *Set up the workspace folder structure, briefing templates, style guide and source register the whole team will use.*

### 5. Create 'Build the AI news sources watchlist'
Title:

> **Build the AI news sources watchlist**

Description:

> *Assemble the RSS feeds, publication sites, X accounts, arXiv categories and company blogs to monitor, with priority tiers and de-duplication rules.*

### 6. Create 'Produce the first daily AI news briefing'
Title:

> **Produce the first daily AI news briefing**

Description:

> *Pull the top stories from the watchlist, verify each against two independent sources, and draft a cited briefing for Board review.*

### 7. Create 'Wire the research pipeline to live search'
Title:

> **Wire the research pipeline to live search**

Description:

> *Integrate the Tavily Search API so researchers query the live web with fresh results (depends on the Tavily key from the next lab).*

## Verification / Expected Output
- The **Tasks board shows all six tasks**, each with a detailed description (open each card and confirm the brief is there, not just a title).
- The **hiring task is assigned to the CEO**.
- Tasks sit in **todo**, ready to move todo → in_progress → in_review → done once the team exists.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Tasks board is empty / missing | Confirm the company switcher shows **Tertiary AI News Research** — each company has its own board. |
| Can't assign the hiring task to the CEO | The CEO hire wasn't approved (Lab 28) — approve it, refresh, then assign. |
| An agent starts a task immediately | Paperclip may auto-start assigned work — pause it or leave the other five tasks **unassigned** until the team is hired in Lab 32. |
| Description lost after saving | Save the card fully before closing (some fields save on blur) — reopen the card to confirm the brief persisted. |
| Agent's work misses the point of a task | The description is the brief — sharpen it with concrete deliverables and constraints, exactly as written above. |

## Exercise / Challenge
Pick one of the six tasks and strip its description down to just the title, then compare: list three concrete decisions the agent would have to guess at without the brief (format? sources? quality bar?). Restore the full description, and add one extra acceptance criterion of your own to the 'Produce the first daily AI news briefing' task (e.g. "maximum 10 stories, each with 2 source links").

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
