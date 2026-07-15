# Lab 4 — Skills

## Objective
LO3: Extend the agent with installable, self-improving skills. You will browse and install open-standard skills (agentskills.io / Skills Hub) so **Athena** can perform new tasks. Skills are portable and can self-improve as the agent uses them.

## Prerequisites
- **Lab 1–3 complete** — Hermes installed, deployed, and with memory working.
- A model/provider connected (so the agent can actually invoke a skill).

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Skills](https://www.youtube.com/watch?v=L3WdVeMaYZM&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=5)

## Steps

### 1. Watch the reference video
See how skills are discovered, installed, and invoked, and what "self-improving" means in practice:

[https://www.youtube.com/watch?v=L3WdVeMaYZM&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=5](https://www.youtube.com/watch?v=L3WdVeMaYZM&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=5)

### 2. Browse the skills hub
Open the skills catalogue to see what's available to install:

```bash
hermes skills browse
```
Or just ask the agent: "Show me what skills are available on the skills hub"


This opens the Skills Hub (backed by agentskills.io). Scroll through the categories to get a feel for the open-standard skills on offer.

### 3. Search for a skill by keyword
Narrow the catalogue to something useful for a chief-of-staff agent — for example `calendar`, `email`, `research`, or `pdf`:

```bash
hermes skills search <keyword>
```
Or just ask the agent: "Search the skills hub for <keyword> skills"


Replace `<keyword>` with your term. The results list each skill's `owner/skills/name` identifier — you'll need that exact identifier to install.

### 4. Install a skill
Install a skill by its full identifier (copy it from the search results). The pattern is `owner/skills/name`:

```bash
hermes skills install <owner/skills/name>
```
Or just ask the agent: "Install the <name> skill from the skills hub and confirm it loaded"


For example, if the search returned a skill identified as `acme/skills/summarize`, you would run `hermes skills install acme/skills/summarize`. Confirm the install reports success.

### 5. Ask the agent to use the new skill and observe self-improvement
Open the TUI and ask Athena to perform a task that the new skill enables. Watch it select and run the skill:

> This step is conversational — no fixed command. Phrase a request that maps to the skill (e.g. for a summarize skill: *"Summarize this article for me: <paste text>"*). As the agent uses the skill repeatedly, it refines how it invokes it — that's the self-improvement aspect.

### 6. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Learn the slide-deck skill from agentskills.io and confirm it is installed"*.

## Verification / Expected Output
- The installed skill appears in the agent's toolset (visible in the skills list / when the agent picks it).
- When you make a request that matches the skill, the agent **invokes it and returns the expected result**.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `hermes skills install` fails with "not found" | Use the **exact** `owner/skills/name` identifier from the search results, not the display name. |
| Skill installs but agent never uses it | Phrase your request to clearly match the skill's purpose; check the skill is enabled in the agent's toolset. |
| `hermes skills browse` shows nothing | Check connectivity to agentskills.io / Skills Hub; retry, or browse the hub in a browser. |
| Installed skill errors when invoked | Some skills need credentials or a provider — read the skill's README/requirements and configure them. |
| Want to remove a skill | Use the corresponding uninstall command shown in `hermes skills --help` (verify in docs: https://hermes-agent.nousresearch.com/docs/). |

## Exercise / Challenge
Install two complementary skills (e.g. a research/search skill and a summarize skill), then ask Athena a single task that requires both — such as *"Research the top 3 AI agent frameworks and give me a bulleted summary."* Observe the agent chain the skills together. Note in your own words how this differs from a plugin (Lab 3).

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
