# Lab 31 — Add the Tavily Search API

## Objective
LO2: Wire live web search into the company via the Tavily Search API. A blog company needs **fresh information**. You will create a Tavily API key, store it as a company **Secret**, and bind it to the **`TAVILY_API_KEY`** runtime environment variable — Paperclip resolves the secret **server-side when a run starts**, so the key never sits in a prompt or a repo.

## Prerequisites
- **Lab 30 complete** — the six-task backlog exists, including 'Wire the research pipeline to live search'.
- An email account to register at [app.tavily.com](https://app.tavily.com) (free tier is fine).
- Paperclip running at `http://localhost:3100` with an enabled adaptor (Lab 29).

## Estimated Time
20–30 minutes

## Steps

### 1. Create a Tavily account and copy an API key from app.tavily.com
Sign up at [app.tavily.com](https://app.tavily.com), open the dashboard and copy an **API key** (it starts with `tvly-`). Keep it in your clipboard — you will paste it once, into a secret, and nowhere else.

### 2. Open Settings → Company settings → Secrets and click 'New secret'
In the Paperclip dashboard go to **Settings → Company settings → Secrets** and click **New secret**. Secrets are company-scoped: every agent the company hires can be granted them, but no agent ever reads them in plain text.

### 3. Store the key as a secret (e.g. name it tavily)
Name the secret (e.g. `tavily`), paste the API key as its value, and save. Secrets are **injected at run start, never shown to agents in plain text** — the value will not appear in prompts, task logs or the repo.

### 4. Bind it to TAVILY_API_KEY via an agent's Environment variables (or a project's Env field)
Now map the secret to the environment variable the Tavily SDK/CLI expects:

- Open an **agent's Environment variables** (or a **project's Env field**),
- add the key **`TAVILY_API_KEY`**,
- choose **Secret** as the value type, and
- select the stored `tavily` secret.

At run start Paperclip resolves the binding server-side and the agent's runtime sees `TAVILY_API_KEY` set — without the key ever passing through a prompt.

### 5. Verify with a live search task
Create a task for an agent with the binding:

> *Use Tavily to find today's three biggest AI announcements and list your sources*

The agent should return **fresh, cited results** — stories from today with source links, not stale training-data knowledge.

## Verification / Expected Output
- The **secret exists** under Settings → Company settings → Secrets.
- **`TAVILY_API_KEY` is bound** to the runtime env of an agent (or project) via the Secret value type.
- The **live-search task returns fresh cited results** — today's announcements with source URLs.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Agent reports "TAVILY_API_KEY not set" | The binding is missing or on the wrong agent — add the env var `TAVILY_API_KEY` with value type **Secret** on the agent (or project) actually running the task. |
| 401 / unauthorized from Tavily | The key was copied wrong or revoked — copy a fresh key from app.tavily.com and update the secret's value. |
| Binding added but runs still fail | Bindings resolve **at run start** — stop and restart the task so a new run picks up the env. |
| Agent echoes the key in its output | It shouldn't ever see it — check you chose value type **Secret** (not a plain-text value) in the env binding. |
| Results are stale / uncited | The agent answered from memory instead of calling Tavily — restate the task to require using Tavily and listing source URLs. |

## Exercise / Challenge
Ask the agent to *print the value of `TAVILY_API_KEY`* and observe what happens — then explain in two sentences why storing the key as a Secret (resolved server-side at run start) is safer than pasting it into the task description or committing a `.env` file. Finally, rotate the key: generate a new one at app.tavily.com, update only the secret's value, and confirm the live-search task still works with **no change** to any agent or task.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
