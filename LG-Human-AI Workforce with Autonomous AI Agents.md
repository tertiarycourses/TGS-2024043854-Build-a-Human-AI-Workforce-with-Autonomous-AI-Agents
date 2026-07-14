# Build a Human-AI Workforce with Autonomous AI Agents — Learner Guide

**WSQ Course Code:** TGS-2024043854  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.1 · 14 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Environment Setup](#before-you-start--environment-setup)
- [Topic 01 — Hermes Agent — Your Autonomous Personal Chief-of-Staff  (33%)](#topic-01--hermes-agent--your-autonomous-personal-chief-of-staff--33)
  - [Lab 1 — Install and Setup Hermes](#lab-1--install-and-setup-hermes)
  - [Lab 2 — Deployment — Local Install & Hermes Desktop App](#lab-2--deployment--local-install--hermes-desktop-app)
  - [Lab 3 — Memory and Plugins](#lab-3--memory-and-plugins)
  - [Lab 4 — Skills](#lab-4--skills)
  - [Lab 5 — Providers & Model](#lab-5--providers--model)
  - [Lab 6 — MCP and Tools](#lab-6--mcp-and-tools)
  - [Lab 7 — Cron Jobs & Automation](#lab-7--cron-jobs--automation)
  - [Lab 8 — Subagents & Delegation](#lab-8--subagents--delegation)
  - [Lab 9 — Profile and Kanban](#lab-9--profile-and-kanban)
  - [Lab 10 — Security](#lab-10--security)
  - [Lab 11 — Use Case — Make a Video with Hyperframe](#lab-11--use-case--make-a-video-with-hyperframe)
  - [Lab 12 — Visualization](#lab-12--visualization)
  - [Lab 13 — Build a Multi-Agent Workflow](#lab-13--build-a-multi-agent-workflow)
  - [Lab 14 — Webhook](#lab-14--webhook)
- [Topic 02 — OpenClaw — Automating a Business Back-Office  (33%)](#topic-02--openclaw--automating-a-business-back-office--33)
  - [Lab 15 — Install OpenClaw](#lab-15--install-openclaw)
  - [Lab 16 — Models & Providers](#lab-16--models--providers)
  - [Lab 17 — Channels](#lab-17--channels)
  - [Lab 18 — Skills](#lab-18--skills)
  - [Lab 19 — Tools & Integrations](#lab-19--tools--integrations)
  - [Lab 20 — Commands](#lab-20--commands)
  - [Lab 21 — Cron Jobs & Heartbeat](#lab-21--cron-jobs--heartbeat)
  - [Lab 22 — Memory & Context](#lab-22--memory--context)
  - [Lab 23 — Security](#lab-23--security)
  - [Lab 24 — Multi-Agent Workforce](#lab-24--multi-agent-workforce)
  - [Lab 25 — Dreaming — Idle Reflection & Self-Improvement](#lab-25--dreaming--idle-reflection--self-improvement)
  - [Lab 26 — Use Cases & Key Functions](#lab-26--use-cases--key-functions)
- [Topic 03 — Paperclip — Running & Governing a Company of AI Agents  (34%)](#topic-03--paperclip--running--governing-a-company-of-ai-agents--34)
  - [Lab 27 — Setup Paperclip](#lab-27--setup-paperclip)
  - [Lab 28 — Connect OpenAI Codex to Paperclip](#lab-28--connect-openai-codex-to-paperclip)
  - [Lab 29 — Configure Paperclip](#lab-29--configure-paperclip)
  - [Lab 30 — Track AI Tasks](#lab-30--track-ai-tasks)
  - [Lab 31 — Automate AI Hiring](#lab-31--automate-ai-hiring)
  - [Lab 32 — Setup AI Agents](#lab-32--setup-ai-agents)
  - [Lab 33 — Security](#lab-33--security)
  - [Lab 34 — Assign Task](#lab-34--assign-task)
- [Wrap-Up — The Agent Build Arc and Governance](#wrap-up--the-agent-build-arc-and-governance)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the WSQ course Build a Human-AI Workforce with Autonomous AI Agents (TGS-2024043854), conducted by Tertiary Infotech Academy Pte Ltd. It provides step-by-step instructions for all 34 hands-on labs across three autonomous-AI-agent platforms — Hermes Agent, OpenClaw and Paperclip — organised into three topics. Each platform builds on the same skillset: install the runtime, connect models and channels, give the agent memory, extend it with skills and tools, automate it with schedules, secure it with governance, and finally orchestrate multiple agents to deliver a realistic business outcome.

Use this guide alongside the course slides and the lab files in the labs/ folder of the course repository. The labs run on your own laptop and in Docker; where a lab connects to an external service (an LLM provider, a messaging channel, a VPS) use only accounts and credentials you own, and keep API keys and tokens out of prompts and out of version control.


## Course Learning Outcomes

- LO1: Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.
- LO2: Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.
- LO3: Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.


## Before You Start — Environment Setup

**What you need**

- A laptop you have administrator rights on — Windows 10/11, macOS 12+ or Ubuntu 22.04+ — with a terminal.
- Node.js 24 LTS (required to run the OpenClaw gateway daemon).
- Docker Desktop (required to self-host Paperclip with Docker Compose, and used for isolated agent sandboxes).
- At least one LLM provider login or API key — Claude (Anthropic), OpenAI, OpenRouter, MiniMax or DeepSeek.
- A free Telegram account for the messaging-channel labs (you will create a bot via BotFather).
- Optional: a VPS (e.g. Hostinger or exe.dev) if you want to run an agent 24/7 beyond the classroom.

**Verify your toolchain**

Open a terminal and confirm the core prerequisites are present before you begin. Each platform's installer (Hermes, OpenClaw, Paperclip) is run in its own lab; here you only confirm the building blocks.

```bash
$ node --version     # Node.js 24.x for OpenClaw
$ docker --version   # Docker Desktop for Paperclip and sandboxes
$ docker compose version
$ git --version      # to clone the course labs repository
```

**Conventions used in every lab**

- Commands are run from your terminal; a leading sudo is used only where elevated rights are required.
- Placeholders such as <API_KEY>, <BOT_TOKEN> and <HOST> are replaced with your own values.
- Store provider keys and channel tokens in each platform's config (never in prompts or in git).
- Keep approval prompts, budgets and sandboxing on so agents act under human oversight.
- Each capstone orchestrates multiple agents — start the single-agent labs first so the pieces are familiar.


## Topic 01 — Hermes Agent — Your Autonomous Personal Chief-of-Staff  (33%)

Install & Setup · Deployment · Memory & Plugins · Skills · Providers & Model · MCP & Tools · Crons · Subagents · Profile & Kanban · Security

**Key concepts**

- Hermes Agent (Nous Research) installs on your own machine — via the install script or the Hermes Desktop app — and requires a model with a >=64,000-token context window.
- Memory and plugins make the agent stateful and extensible: a three-layer memory (agent-curated notes, FTS5 cross-session recall, Honcho user modelling) plus installable skills and MCP tools.
- Providers & models are swappable with no lock-in (Nous Portal, OpenRouter, OpenAI, any endpoint); MCP servers and the Tool Gateway (web search, image, TTS) give the agent real-world reach.
- Cron jobs automate recurring work; subagents & delegation split work across isolated backends; the profile and Kanban board let you supervise the agent's tasks — all under security controls.


### Lab 1 — Install and Setup Hermes

Learning outcome: LO1: Install and configure Hermes Agent on a local machine..

Goal: Install Hermes Agent on your laptop, run the first-time setup wizard, and confirm a healthy install. This is the foundation for the Athena chief-of-staff agent you build across the track.

**What you'll build**

A working Hermes Agent install that passes 'hermes doctor' and opens the TUI.   (Tools: Hermes Agent, Nous Portal, terminal.)

**Step-by-step**

1. Watch the reference video Before touching the terminal, watch the reference video end to end so you know what a healthy install looks like and can spot where the UI differs from these written steps: https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11 (https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)
2. Install Hermes (macOS / Linux / WSL2) Run the official one-line installer. It downloads the Hermes binary, places it under your user directory, and wires up the hermes command:

   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```

3. Reload your shell so the hermes command is on PATH The installer adds Hermes to your PATH via your shell profile, but your current terminal session hasn't re-read that file yet. Reload it:

   ```bash
   source ~/.zshrc
   ```

4. Run the first-time setup wizard Launch the interactive setup wizard and connect Hermes to your Nous Portal account. This is where you sign in, pick defaults, and let Hermes provision a model provider:

   ```bash
   hermes setup --portal
   ```

5. Check the install is healthy Run the built-in diagnostic. It checks the binary, config, PATH, provider connectivity, and the local runtime:

   ```bash
   hermes doctor
   ```

6. Launch the agent and say hello Open the terminal UI (TUI) and start your first conversation with the agent — this is Athena's very first session:

   ```bash
   hermes --tui
   ```


**Test it**

'hermes doctor' reports all green and the TUI opens and replies to a message.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 2 — Deployment — Local Install & Hermes Desktop App

Learning outcome: LO1: Deploy Hermes locally and run it through the Hermes Desktop app..

Goal: Run Hermes as a persistent local deployment (preferred) and also install the Hermes Desktop app for a GUI experience. Confirm the local gateway is serving and keep the runtime up to date.

**What you'll build**

A local Hermes deployment plus the Desktop app, both talking to the same agent.   (Tools: Hermes Agent, Hermes Desktop, terminal.)

**Step-by-step**

1. Watch the reference video for this lab

   ```bash
   https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3
   ```

2. Watch the reference videos Watch both videos above. The primary shows the local deployment; the additional walkthrough covers the Desktop app in more depth. Note any UI screens that differ from the steps below.
3. Confirm the local install runs (preferred deployment) Verify the CLI runtime you installed in Lab 1 is present and check its version. The local install is the preferred deployment — it keeps the agent runtime on your machine:

   ```bash
   hermes --version
   ```

4. Download and install the Hermes Desktop app Download the Desktop app for your OS from the official site and install it like any normal application:
5. Open the Desktop app and sign in Launch the Hermes Desktop app and sign in with the same Nous Portal account you used for the CLI in Lab 1. Signing in with the same account is what makes the Desktop app and the CLI drive the same agent. > This step is UI-only — there is no terminal command. In the app, choose Sign in with Nous Portal and complete the browser/authentication prompt.
6. Verify the local gateway is serving The gateway is the local service that both the CLI and Desktop app connect to. Confirm it is up and healthy:

   ```bash
   hermes gateway status
   ```

7. Keep the runtime up to date Update Hermes to the latest release so the CLI and Desktop app stay compatible:

   ```bash
   hermes update
   ```


**Test it**

Both the local CLI and the Desktop app drive the same agent; 'hermes gateway status' is healthy.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 3 — Memory and Plugins

Learning outcome: LO2: Give the agent persistent memory and extend it with plugins..

Goal: Explore Hermes' three-layer memory (agent-curated notes, FTS5 cross-session recall, Honcho user modelling). Teach Athena a preference, recall it in a fresh session, and enable a plugin to extend behaviour.

**What you'll build**

Athena remembers a stated preference across sessions and runs an enabled plugin.   (Tools: Hermes Agent, memory, plugins.)

**Step-by-step**

1. Watch the reference video Watch the video to see how Hermes stores memory across the three layers and how plugins are enabled: https://www.youtube.com/watch?v=ZKZLko9kLm4&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=4 (https://www.youtube.com/watch?v=ZKZLko9kLm4&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=4)
2. Teach Athena a durable preference Start a session (hermes --tui) and give Athena a clear, memorable instruction that should persist. Explicitly asking it to remember nudges the agent to write the fact into its curated-notes memory layer:

   ```bash
   Remember I prefer concise, bulleted summaries.
   ```

3. Start a new session and confirm the preference is recalled Resume the conversation in a fresh session. The --continue flag brings back prior context so you can test cross-session recall:

   ```bash
   hermes --continue
   ```

4. Inspect stored memory / sessions List the stored sessions so you can see the memory Hermes is persisting behind the scenes:

   ```bash
   hermes sessions list
   ```

5. Enable a plugin to extend the agent Enable a plugin to add capability beyond the base agent. Plugins are toggled from the Hermes plugins UI or config:

**Test it**

A preference taught in one session is recalled in a new session, and the enabled plugin is active.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 4 — Skills

Learning outcome: LO3: Extend the agent with installable, self-improving skills..

Goal: Browse and install open-standard skills (agentskills.io / Skills Hub) so Athena can perform new tasks. Skills are portable and can self-improve as the agent uses them.

**What you'll build**

Athena equipped with at least one installed skill that it can invoke on request.   (Tools: Hermes Agent, agentskills.io, Skills Hub.)

**Step-by-step**

1. Watch the reference video See how skills are discovered, installed, and invoked, and what "self-improving" means in practice: https://www.youtube.com/watch?v=L3WdVeMaYZM&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=5 (https://www.youtube.com/watch?v=L3WdVeMaYZM&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=5)
2. Browse the skills hub Open the skills catalogue to see what's available to install:

   ```bash
   hermes skills browse
   ```

3. Search for a skill by keyword Narrow the catalogue to something useful for a chief-of-staff agent — for example calendar, email, research, or pdf:

   ```bash
   hermes skills search <keyword>
   ```

4. Install a skill Install a skill by its full identifier (copy it from the search results). The pattern is owner/skills/name:

   ```bash
   hermes skills install <owner/skills/name>
   ```

5. Ask the agent to use the new skill and observe self-improvement Open the TUI and ask Athena to perform a task that the new skill enables. Watch it select and run the skill: > This step is conversational — no fixed command. Phrase a request that maps to the skill (e.g. for a summarize skill: "Summarize this article for me: <paste text>"). As the agent uses the skill repeatedly, it refines how it invokes it — that's the self-improvement aspect.

**Test it**

The installed skill appears in the agent's toolset and runs when invoked.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 5 — Providers & Model

Learning outcome: LO2: Connect an LLM provider and switch models with no lock-in..

Goal: Connect a model provider (Nous Portal, OpenRouter, OpenAI or any endpoint) and select a model that meets the >=64,000-token context requirement. Switch providers to compare speed and quality.

**What you'll build**

Athena running on a chosen provider/model, with the ability to switch on demand.   (Tools: Hermes Agent, Nous Portal, OpenRouter.)

**Step-by-step**

1. Watch the reference video See how providers are connected and how to switch models on demand: https://www.youtube.com/watch?v=1oaaOWy7wSI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=6 (https://www.youtube.com/watch?v=1oaaOWy7wSI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=6)
2. Open the interactive provider/model picker Launch the interactive picker to see available providers and models and select one:

   ```bash
   hermes model
   ```

3. Set a model explicitly Instead of (or in addition to) the picker, set the active model directly in config:

   ```bash
   hermes config set model anthropic/claude-opus-4.6
   ```

4. Add a provider key if using a cloud endpoint If your chosen model runs on a cloud endpoint (e.g. OpenRouter), store the API key in config so Hermes can authenticate:

   ```bash
   hermes config set OPENROUTER_API_KEY sk-or-...
   ```

5. Confirm the active model meets the ≥64k context rule Reopen the picker to confirm the active model and its context window:

   ```bash
   hermes model
   ```


**Test it**

The agent starts on the selected model and can be switched to another provider without reinstalling.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 6 — MCP and Tools

Learning outcome: LO3: Give the agent real-world reach with MCP servers and the Tool Gateway..

Goal: Add Model Context Protocol (MCP) servers in the Hermes config and use the bundled Tool Gateway (web search, image generation, TTS) so Athena can act on the outside world.

**What you'll build**

Athena wired to an MCP server (e.g. GitHub) and able to use a Tool Gateway tool.   (Tools: Hermes Agent, MCP, Tool Gateway.)

**Step-by-step**

1. Watch the reference video See how MCP servers are declared in config and how the Tool Gateway tools are called from chat: https://www.youtube.com/watch?v=U140gP-1bEI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=7 (https://www.youtube.com/watch?v=U140gP-1bEI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=7)
2. Open the Hermes config to add an MCP server Edit your Hermes config file and locate (or create) the mcp_servers: section:
3. Add a GitHub MCP server entry Add an entry that launches the official GitHub MCP server via npx. A typical block looks like this:

   ```bash
   mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_your_token_here"
   ```

4. Restart so the MCP server is picked up, then verify Restart Hermes (close and reopen the TUI, or restart the gateway) so it reads the new config, then run the diagnostic:

   ```bash
   hermes doctor
   ```

5. Use a Tool Gateway tool from a chat Open the TUI and ask Athena to use a bundled Tool Gateway capability — web search, image generation, or text-to-speech: > This step is conversational. For example: "Search the web for today's top AI agent news and list 3 headlines," or "Generate an image of a friendly robot assistant." Confirm the agent invokes the tool and returns the result.

**Test it**

The agent lists the new MCP server's tools and completes a task using a Tool Gateway tool.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 7 — Cron Jobs & Automation

Learning outcome: LO4: Automate recurring agent work on a schedule..

Goal: Schedule Athena to run recurring jobs — for example an 8am daily briefing sent to your messaging app — and verify the scheduled run fires and produces output.

**What you'll build**

A scheduled job (e.g. a daily briefing) that runs automatically and delivers a result.   (Tools: Hermes Agent, scheduler/crons.)

**Step-by-step**

1. Watch the reference video Watch how recurring jobs (crons/automations) are defined and triggered in Hermes. The exact syntax is version-specific, so follow the video closely: https://www.youtube.com/watch?v=grMNnzCv2gY&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=8 (https://www.youtube.com/watch?v=grMNnzCv2gY&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=8)
2. Define a recurring job (daily 8am briefing) Create a recurring automation in the Hermes automations/crons section — for example a daily 8am briefing:
3. Confirm the automation is registered Run the diagnostic to confirm Hermes has picked up the new scheduled job:

   ```bash
   hermes doctor
   ```

4. Trigger the job once to confirm it produces output Manually run the job once (rather than waiting for 8am) to confirm it produces the expected briefing. > This is typically a "run now" action in the automations UI, or a trigger command shown in the docs. Confirm the briefing is generated and delivered to your chosen destination.
5. Confirm the next scheduled run is queued Check that after the manual run, the next run is still scheduled for its normal time (08:00 tomorrow), so the automation keeps recurring.

**Test it**

The scheduled job runs at its time (or on manual trigger) and delivers the expected briefing.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 8 — Subagents & Delegation

Learning outcome: LO5: Delegate work to isolated subagents across backends..

Goal: Turn Athena into a coordinator that delegates tasks to worker subagents running on isolated terminal backends (local, docker, ssh, modal), then aggregates their results.

**What you'll build**

A coordinator agent that delegates a task to one or more worker subagents and combines the output.   (Tools: Hermes Agent, terminal backends (docker/ssh/modal).)

**Step-by-step**

1. Watch the reference video See how a coordinator agent spawns worker subagents on isolated backends and combines their output: https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10 (https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)
2. Choose an isolated backend for worker agents Set the terminal backend that worker subagents will run on. docker gives each worker an isolated container:

   ```bash
   hermes config set terminal.backend docker
   ```

3. Ask the coordinator to delegate a multi-part task Open the TUI and give Athena (the coordinator) a task with clearly separable parts so it delegates each to a worker subagent: > Conversational step. For example: "Delegate this: subagent A researches competitor pricing, subagent B drafts a comparison table, subagent C writes a one-paragraph recommendation. Then combine their work." Watch the coordinator spin up workers.
4. Observe each subagent run in isolation and report back Watch each worker subagent execute on the isolated backend and return its portion of the result. Confirm they run separately (each in its own container/environment when using docker) rather than in the coordinator's session.
5. Review the coordinator's aggregated result Confirm the coordinator combines the workers' outputs into one coherent deliverable — the research, the table, and the recommendation merged into a single response.

**Test it**

The coordinator delegates to worker subagents on an isolated backend and returns a combined result.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 9 — Profile and Kanban

Learning outcome: LO5: Supervise the agent through its profile and Kanban board..

Goal: Configure the agent's profile and use the Hermes Kanban board to watch tasks move through todo -> in progress -> done, giving you human oversight of what Athena is working on.

**What you'll build**

A configured agent profile and a Kanban board tracking the agent's live tasks.   (Tools: Hermes Agent, profile, Kanban board.)

**Step-by-step**

1. Watch the reference video This lab shares the video with Lab 8. Focus on the portions covering the agent profile and the Kanban board view: https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10 (https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)
2. Set up the agent profile (identity, defaults, preferences) Configure Athena's profile — its identity, default model/backend, and behavioural preferences. > Open the profile settings in the Desktop app (or the profile section of ~/.hermes/config.yaml). Set the name to Athena, role to personal chief of staff, and default preferences (concise bulleted output, timezone, working hours). The exact profile fields are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).
3. Open the Kanban board view Open the Kanban board that visualizes the agent's tasks. > In the Desktop app, open the Kanban / Tasks view. You should see columns such as Todo, In Progress, and Done.
4. Assign a task and watch it move todo → in progress → done Give Athena a task and watch the corresponding card move across the board: > Assign a task (e.g. "Draft my weekly team update"). A card appears in Todo, moves to In Progress as the agent works, and lands in Done when finished. This is your live oversight of what the agent is doing.
5. Use the board to review and accept completed work When a card reaches Done, open it, review the agent's output, and accept (or send it back with feedback). This human-in-the-loop review is the point of the board.

**Test it**

The profile is set and the Kanban board shows tasks progressing across its columns.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 10 — Security

Learning outcome: LO4: Secure the agent with isolation, secrets and approvals..

Goal: Harden Athena: run risky work in an isolated terminal backend, manage secrets safely, and require approval before sensitive actions — applying least privilege throughout.

**What you'll build**

A hardened agent that sandboxes execution, protects secrets and prompts for approval on risky actions.   (Tools: Hermes Agent, terminal backends, secrets management.)

**Step-by-step**

1. Watch the reference video This lab shares the video with Lab 1. Focus on the sections covering isolation, secrets, and approvals: https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11 (https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)
2. Isolate execution in a sandboxed backend Set the terminal backend to a sandboxed container so risky commands never run directly on your host:

   ```bash
   hermes config set terminal.backend docker
   ```

3. Store provider/tool secrets via config rather than plain text Store API keys through the Hermes config mechanism instead of pasting them into prompts or scripts:

   ```bash
   hermes config set <PROVIDER>_API_KEY <value>
   ```

4. Require approval before the agent runs risky actions Enable approval prompts so the agent pauses and asks you before executing sensitive actions (shell commands, file deletions, external posts):
5. Apply least privilege — grant only the tools/skills the task needs Review the tools, skills, and MCP servers Athena has access to and disable anything not needed for the current work. > Conversational/config step: trim the enabled skills (Lab 4) and MCP servers (Lab 6) to the minimum. Least privilege means the agent can only do what the task actually requires.

**Test it**

Risky actions run only in the sandbox and only after approval; secrets are not stored in plain text.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 11 — Use Case — Make a Video with Hyperframe

Learning outcome: LO5: Apply the agent to a real creative use case — produce a video with Hyperframe..

Goal: Put Athena to work on an end-to-end creative task: use the agent to drive the Hyperframe tool and generate a short video from a concept brief, then review and refine the result.

**What you'll build**

A short video generated end-to-end by the agent using Hyperframe.   (Tools: Hermes Agent, Hyperframe.)

**Step-by-step**

1. Watch the reference video See the full workflow of driving Hyperframe through the agent to produce a video: https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3 (https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)
2. Connect / set up the Hyperframe video tool for the agent Wire the Hyperframe tool into Athena so the agent can invoke it. > This may be an MCP server, a skill, or a Tool Gateway integration depending on your build. Add Hyperframe the same way you added tools in Lab 6, supplying any required API key via hermes config set. Verify the exact integration path in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).
3. Brief the agent with a short video concept Give Athena a clear, concise creative brief — topic, style, and length: > Conversational step. For example: "Make a 30-second explainer video introducing 'Athena, my AI chief of staff'. Clean, modern style, upbeat tone, with on-screen captions." A tight brief yields a better first result.
4. Have the agent generate the video with Hyperframe Ask Athena to generate the video. The agent calls Hyperframe with your brief and waits for the render: > Confirm the agent invokes Hyperframe and reports back with a link/file to the rendered video. Rendering may take a few minutes.
5. Review the output and refine the brief to regenerate if needed Play the video, then refine the brief (pacing, style, wording) and ask Athena to regenerate. Iterate until it meets your bar.

**Test it**

The agent produces a playable video from your brief using Hyperframe.

> **Note:** Full commands and screenshots are in labs/lab-11-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 12 — Visualization

Learning outcome: LO5: Visualize agent activity and workflow data..

Goal: Use Hermes' visualization capability to see the agent's workflow, task flow and data at a glance, making the agent's behaviour transparent and easier to supervise.

**What you'll build**

A visualization of the agent's workflow / activity you can read and interpret.   (Tools: Hermes Agent, visualization.)

**Step-by-step**

1. Watch the reference video See how Hermes renders workflows/activity visually and how to read the output: https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27 (https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27)
2. Open the visualization view for the agent's activity Open the visualization panel that shows Athena's activity. > In the Desktop app, open the Visualization / Activity view. It surfaces the agent's task flow, tool calls, and data. Verify the exact location in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).
3. Generate a visualization of a workflow or dataset Ask Athena to produce a visualization of a workflow or a dataset: > Conversational step. For example: "Visualize the steps you took to produce this morning's briefing," or "Chart my task completion over the last week." The agent generates a diagram/chart of the workflow or data.
4. Interpret the visualization to understand what the agent did Read the visualization: which steps ran, in what order, which tools/subagents were involved, and where time was spent. Use it to confirm the agent did what you expected.

**Test it**

A visualization of the agent's workflow/data renders and communicates the agent's activity.

> **Note:** Full commands and screenshots are in labs/lab-12-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 13 — Build a Multi-Agent Workflow

Learning outcome: LO5: Compose multiple agents into a coordinated workflow..

Goal: Design a multi-agent workflow in which several agents take on distinct roles and hand off tasks to one another to complete a larger goal, building on the subagents and delegation concepts from earlier labs.

**What you'll build**

A working multi-agent workflow where agents hand off tasks to complete a goal.   (Tools: Hermes Agent, subagents, workflow.)

**Step-by-step**

1. Watch the reference video See a full multi-agent workflow composed and run end-to-end, with hand-offs between roles: https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19 (https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19)
2. Define the agents and their roles in the workflow Design the workflow by naming each agent and its distinct responsibility. > Conversational/design step. For a chief-of-staff use case, define roles such as: Researcher (gathers facts), Writer (drafts content), Reviewer (checks quality), with Athena as coordinator. Write the roles down before wiring anything.
3. Connect the agents so outputs hand off between them Wire the agents so each one's output becomes the next one's input (Researcher → Writer → Reviewer). > Use the subagent/delegation mechanism from Lab 8. Instruct Athena that the Researcher's findings feed the Writer, and the Writer's draft feeds the Reviewer. Verify the exact multi-agent wiring in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).
4. Run the workflow end-to-end on a sample goal Give the workflow a real goal and run it start to finish: > For example: "Produce a one-page competitor brief on the top 3 AI agent platforms." Watch Researcher → Writer → Reviewer hand off in sequence and produce the final brief.
5. Verify each stage completed and the final result is correct Check that every stage ran, each hand-off delivered usable input to the next, and the final output is coherent and correct.

**Test it**

The multi-agent workflow runs end-to-end with each agent handing off to the next and producing the final result.

> **Note:** Full commands and screenshots are in labs/lab-13-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 14 — Webhook

Learning outcome: LO3: Integrate the agent with external systems via webhooks..

Goal: Wire the agent to the outside world with webhooks: trigger the agent from an incoming webhook payload and/or have it call an outgoing webhook, then secure the endpoint.

**What you'll build**

A webhook that triggers the agent (or that the agent calls), verified end-to-end.   (Tools: Hermes Agent, webhooks.)

**Step-by-step**

1. Watch the reference video See how a webhook endpoint is configured for the agent and how an incoming payload triggers it: https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31 (https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)
2. Configure a webhook trigger/endpoint for the agent Set up a webhook endpoint that Athena listens on. > Configure the webhook in the Hermes automation/integration settings (Desktop app or the webhook section of ~/.hermes/config.yaml), mapping an incoming URL to an agent action. The exact config keys and the endpoint URL are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/). Note the endpoint URL served by your local gateway (from hermes gateway status).
3. Send a test payload to the webhook Send a test HTTP POST to the endpoint to simulate an external event:

   ```bash
   curl -X POST <your-webhook-endpoint-url> \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"Trigger Athena briefing"}'
   ```

4. Confirm the agent receives the event and responds/acts Check that the incoming payload triggered Athena — e.g. it ran the mapped action (a briefing, a reply, a message to a channel). Confirm the action's output where you expect it (chat, channel, or logs).
5. Secure the webhook (secret/token, allowlist) Lock the endpoint down so only authorized callers can trigger the agent: > Add a shared secret/token that callers must include (e.g. an Authorization header or a signing secret), and/or an IP allowlist. Re-send the test with and without the secret to confirm unauthorized calls are rejected. Verify the exact security options in the video / docs link above.

**Test it**

A test payload to the webhook triggers the agent and produces the expected action, with the endpoint secured.

> **Note:** Full commands and screenshots are in labs/lab-14-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


## Topic 02 — OpenClaw — Automating a Business Back-Office  (33%)

Install · Providers · Channels · Skills · Tools · Commands · Crons · Memory · Dreaming · Security · Multi-Agent · Use Cases

**Key concepts**

- OpenClaw runs on Node.js 24 LTS as a long-running gateway daemon that hosts every channel, tool, cron and skill for the Nimbus Supplies back office.
- Providers are connected by OAuth sign-in (OpenAI Codex, MiniMax) or API key (Anthropic, DeepSeek, OpenRouter); skills from skills.sh and integrations such as Firecrawl and AgentMail extend the agent.
- 'Dreaming' lets the agent reflect during idle time — reviewing memory and generating follow-ups — while profiles and allow/deny lists keep every channel least-privileged and audited.
- Crons schedule recurring work, a heartbeat auto-restarts the gateway, and a multi-agent capstone splits work across cooperating Sales, Research and Ops agents for real back-office use cases.


### Lab 15 — Install OpenClaw

Learning outcome: LO1: Install and configure an autonomous AI agent platform locally and on a container/VPS..

Goal: The learner installs the OpenClaw platform on their own machine (or a cloud VPS) by first installing Node.js 24 LTS, then installing OpenClaw via npm and running the onboarding wizard, and verifies the install with doctor and gateway status. This gateway becomes the back-office brain of the Nimbus Supplies running example.

**What you'll build**

A running OpenClaw gateway daemon (local or VPS) verified with openclaw doctor   (Tools: OpenClaw, Node.js 24 LTS, npm, openclaw gateway.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. Install Node.js 24 LTS (24 recommended; 22.16+ minimum). OpenClaw runs on Node. Windows — download the Node 24 LTS installer from <https://nodejs.org/> and run the .msi (WSL2 is recommended for stability), then check:

   ```bash
   node -v
   npm -v
   ```

3. Install OpenClaw — Option A (npm, recommended, cross-platform). After Node is installed:

   ```bash
   npm install -g openclaw@latest
   openclaw onboard
   ```

4. Install OpenClaw — Option B (installer script, fallback if npm fails). macOS / Linux / WSL2:

   ```bash
   curl -fsSL https://openclaw.ai/install.sh | bash
   ```

5. Install OpenClaw — Option C (from source, advanced). Requires git and pnpm:

   ```bash
   git clone https://github.com/openclaw/openclaw.git
   cd openclaw
   pnpm install && pnpm build && pnpm ui:build
   pnpm link --global
   openclaw onboard --install-daemon
   ```

6. (Optional) Install on a VPS so Nimbus Supplies runs 24/7. The same three-step flow works on any Ubuntu host — a Hostinger KVM VPS or an exe.dev sandbox. SSH in first (ssh root@<your-vps-ip>), then run:

   ```bash
   # Step 1 — Node.js 24
   curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
   sudo apt-get install -y nodejs
   node -v && npm -v

   # Step 2 — OpenClaw (note: sudo for a global install on a fresh VPS)
   sudo npm install -g openclaw@latest

   # Step 3 — onboarding wizard
   openclaw onboard
   ```

7. Verify the installation.

   ```bash
   openclaw --version
   openclaw doctor
   openclaw gateway status
   ```

8. Confirm the gateway is running (and set to auto-start). The gateway is the long-running daemon that will host every channel, tool, and cron for Nimbus Supplies:

   ```bash
   openclaw gateway status
   openclaw gateway start   # if it is not already running
   ```


**Test it**

openclaw --version prints a version, openclaw doctor shows green checks for Node 24 and the gateway daemon (provider/channel checks pending until Labs 16-17), and openclaw gateway status reports running.

> **Note:** Full commands and screenshots are in labs/lab-15-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 16 — Models & Providers

Learning outcome: LO2: Connect an LLM model/provider to an agent via OAuth or API key..

Goal: The learner connects a language model to OpenClaw, trying the supported provider options — OAuth sign-ins (OpenAI Codex, MiniMax) and API-key providers (Anthropic, DeepSeek, OpenRouter) — learns where credentials are stored under ~/.openclaw/auth/, hot-swaps between models, and runs a Nimbus Supplies smoke test.

**What you'll build**

A Nimbus Supplies agent wired to a working model provider that passes openclaw model test   (Tools: OpenClaw, OpenAI Codex / MiniMax (OAuth), Anthropic / DeepSeek / OpenRouter (API key).)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. See what is available and what is currently selected.

   ```bash
   openclaw models list
   openclaw model current
   ```

3. Option A — OpenAI Codex (OAuth, GPT-5.5). OAuth uses the openai-codex provider so you sign in with your ChatGPT Plus / Pro subscription instead of paying per token. Credentials are stored in ~/.openclaw/auth/ (profile at ~/.openclaw/auth-profiles/openai-codex.json); refresh is automatic.

   ```bash
   openclaw models auth login --provider openai-codex
   ```

4. Option B — MiniMax (OAuth, MiniMax-M2.7). Enable the OAuth plugin, restart the gateway, then log in and set it as default:

   ```bash
   openclaw plugins enable minimax-portal-auth
   openclaw gateway restart
   openclaw models auth login --provider minimax-portal --set-default
   ```

5. Option C — Anthropic (API key, Claude Opus 4.7). Get a key from <https://console.anthropic.com/settings/keys>:

   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   openclaw config set provider anthropic
   openclaw config set model anthropic/claude-opus-4-7
   openclaw model test
   ```

6. Option D — DeepSeek (API key, V4). Get a key from <https://platform.deepseek.com/api_keys>:

   ```bash
   export DEEPSEEK_API_KEY="sk-..."
   openclaw config set provider deepseek
   openclaw config set model deepseek/deepseek-v4
   openclaw model test
   ```

7. Option E — OpenRouter (API key, routes to Claude Opus 4.7). Get a key from <https://openrouter.ai/keys>:

   ```bash
   export OPENROUTER_API_KEY="sk-or-..."
   openclaw config set provider openrouter
   openclaw config set model openrouter/anthropic/claude-opus-4.7
   openclaw model test
   ```

8. Persist API keys so they survive reboots. For the API-key providers, add the export line to your shell profile (~/.zshrc on macOS, ~/.bashrc on Linux). OAuth tokens are persisted automatically in ~/.openclaw/auth/ and do not need this.

   ```bash
   echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
   source ~/.zshrc
   ```

9. Switch models and confirm the active one. You can hot-swap the global default at any time:

   ```bash
   openclaw model use deepseek/deepseek-v4
   openclaw model current
   openclaw model test
   ```

10. Give the agent a Nimbus Supplies smoke test. With any model active, from the CLI chat (openclaw) ask: > You are the back-office assistant for Nimbus Supplies, a small office-supplies reseller. In two sentences, introduce yourself to a customer. A sensible reply confirms the model is wired up.

**Test it**

openclaw models list shows the connected models, openclaw model current prints the active one, openclaw model test returns a short successful completion with no auth error, and OAuth credentials appear under ~/.openclaw/auth/.

> **Note:** Full commands and screenshots are in labs/lab-16-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 17 — Channels

Learning outcome: LO2: Connect multiple messaging channels to one agent gateway..

Goal: The learner gives customers a way to reach the Nimbus Supplies agent by creating a Telegram bot end-to-end via BotFather, registering it with a token, pairing a WhatsApp number by scanning a QR code, and running both channels at once through a single OpenClaw gateway so the same agent answers on either platform.

**What you'll build**

Telegram and WhatsApp both live on one OpenClaw gateway, answered by the same Nimbus Supplies agent   (Tools: OpenClaw, Telegram (BotFather), WhatsApp, openclaw channel.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. Create a Telegram bot with BotFather. 1. Open Telegram and search for @BotFather. 2. Send /newbot. 3. Enter a display name (e.g. Nimbus Supplies Assistant). 4. Enter a username — must be unique and end in _bot (e.g. nimbus_supplies_bot). 5. BotFather replies with an HTTP API token like 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11. Copy it.
3. Register and start the Telegram channel.

   ```bash
   openclaw channel add telegram --token 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   openclaw channel start telegram
   ```

4. Test Telegram. In Telegram, search for your bot's username and send: > Hi, do you supply recycled A4 paper for Nimbus Supplies? The agent should reply using the model you connected in Lab 16.
5. Add and start the WhatsApp channel.

   ```bash
   openclaw channel add whatsapp
   openclaw channel start whatsapp
   ```

6. Pair WhatsApp by scanning the QR. On your phone: WhatsApp → Settings → Linked Devices → Link a Device, then scan the QR code shown in the terminal. Wait for whatsapp: connected in the OpenClaw log. > WhatsApp keeps a stateful session on disk at ~/.openclaw/whatsapp/. Do not delete that folder unless you intend to re-pair.
7. Confirm both channels are running at the same time. One gateway hosts many channels — the same Nimbus Supplies agent now answers on both.

   ```bash
   openclaw channel list
   openclaw gateway status
   ```

8. Inspect and manage a channel. Useful day-to-day commands:

   ```bash
   openclaw channel show telegram
   openclaw channel restart whatsapp   # e.g. after the QR expires
   ```


**Test it**

openclaw channel list shows telegram and whatsapp both running, a message to the Telegram bot gets an agent reply, a message to the linked WhatsApp account gets an agent reply, and openclaw gateway status shows both connected.

> **Note:** Full commands and screenshots are in labs/lab-17-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 18 — Skills

Learning outcome: LO3: Extend an agent with registry and custom skills..

Goal: The learner installs and removes skills from the skills.sh registry, invokes them from chat, and builds a custom Nimbus Supplies skill (nimbus-quote) under ~/.openclaw/skills/ so the agent handles a recurring back-office task — drafting an itemised customer quote with GST — the same way every time.

**What you'll build**

Registry skills plus a custom nimbus-quote skill that produces itemised, GST-inclusive quotes   (Tools: OpenClaw, skills.sh registry, ~/.openclaw/skills/, openclaw skills.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. List the skills currently installed.

   ```bash
   openclaw skills list
   ```

3. Install a few useful skills from the registry. Skills come from <https://skills.sh/>:

   ```bash
   openclaw skills add web-research --source skills.sh
   openclaw skills add self-improvement --source skills.sh
   ```

4. Invoke a skill from chat. In your Telegram or WhatsApp channel, send:

   ```bash
   /skill web-research "Who are the main office-supplies wholesalers in Singapore?"
   ```

5. Remove a skill you do not need (keeps the agent focused and safe):

   ```bash
   openclaw skills remove self-improvement
   ```

6. Refresh the registry index if a skill you expect is missing:

   ```bash
   openclaw skills update
   ```

7. Build a custom Nimbus Supplies skill. Skills live under ~/.openclaw/skills/. Create a folder and a skill definition. (File layout is shown here as a documented example — confirm the exact schema for your version at <https://docs.openclaw.ai/> before relying on advanced fields.)

   ```bash
   mkdir -p ~/.openclaw/skills/nimbus-quote
   ```

8. Register and test the custom skill.

   ```bash
   openclaw skills list                 # confirm nimbus-quote appears
   openclaw gateway restart             # reload skills if it is not picked up
   ```


**Test it**

openclaw skills list shows the registry skills plus the custom nimbus-quote, /skill web-research runs end-to-end, and /skill nimbus-quote produces an itemised quote with a 9% GST line and standard terms, marking any unknown price as TBC instead of guessing.

> **Note:** Full commands and screenshots are in labs/lab-18-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 19 — Tools & Integrations

Learning outcome: LO3: Extend an agent with third-party tool integrations..

Goal: The learner extends the Nimbus Supplies agent with two real integrations — Firecrawl (JS-rendered web scraping) and AgentMail (its own inbox/outbox) — then runs an end-to-end back-office task: research a supplier's website prices, draft an itemised quote with the Lab 18 skill, and email it to a customer. Tool profiles and allow/deny lists scope tools per channel.

**What you'll build**

A Firecrawl + AgentMail integrated agent that scrapes supplier prices and emails an itemised quote   (Tools: OpenClaw, Firecrawl, AgentMail, openclaw tools.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. Inspect the built-in tools first.

   ```bash
   openclaw tools list
   ```

3. Enable Firecrawl. Sign up at <https://www.firecrawl.dev/>, then Dashboard → API Keys → copy the fc-... key:

   ```bash
   export FIRECRAWL_API_KEY="fc-..."
   openclaw tools enable firecrawl --api-key "$FIRECRAWL_API_KEY"
   openclaw tools status firecrawl
   ```

4. Smoke-test Firecrawl from chat. In Telegram or WhatsApp: > Use Firecrawl to fetch the products page of a stationery supplier's website and list their A4 paper options with prices in 5 bullets.
5. Enable AgentMail. Create an inbox at <https://agentmail.to/>, copy the API key and inbox address:

   ```bash
   export AGENTMAIL_API_KEY="..."
   openclaw tools enable agentmail \
     --api-key "$AGENTMAIL_API_KEY" \
     --inbox bot@yourname.agentmail.to
   openclaw tools status agentmail
   ```

6. Smoke-test AgentMail. From chat: > Send an email from my AgentMail inbox to <your-personal-email> with subject "Hello from Nimbus Supplies" and a friendly one-paragraph body. Check your inbox, reply to it, then ask: > Check my AgentMail inbox and summarise the latest reply.
7. Run the real end-to-end task (research → quote → email). From a channel, send one instruction that chains both tools plus the skill from Lab 18: > A customer, Acme Cafe, wants 10 reams of recycled A4 paper and 5 boxes of black pens. Use Firecrawl to check current prices on our supplier's site, then use the nimbus-quote skill to draft an itemised quote, and email it from my AgentMail inbox to orders@acmecafe.example with subject "Your Nimbus Supplies quote".
8. Scope tools per channel with profiles and allow/deny lists. Public channels should not run shell exec. Apply the safe messaging preset and lock down a public channel:

   ```bash
   openclaw channel set telegram --profile messaging
   openclaw channel set telegram --deny exec
   openclaw channel set telegram --allow group:web
   openclaw channel show telegram
   ```

9. (Optional) Add one more integration of your choice. Pick one from <https://docs.openclaw.ai/tools> and enable it (exact name/flags per the docs), e.g.:

   ```bash
   openclaw tools enable <tool-name> --api-key <KEY>
   ```


**Test it**

openclaw tools list --enabled shows firecrawl and agentmail, the agent scrapes a supplier URL and returns structured prices, an AgentMail send arrives in a real inbox, the end-to-end task produces an itemised quote email, and a channel set to --deny exec refuses shell-exec requests.

> **Note:** Full commands and screenshots are in labs/lab-19-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 20 — Commands

Learning outcome: LO4: Operate an agent through its CLI and in-chat command surface..

Goal: The learner becomes fluent in the two ways to drive OpenClaw daily: the CLI commands (config, model, doctor, gateway, channel, tools, skills, cron) and the in-chat slash commands operators and customers use inside a channel, building a personal quick-reference table for running the Nimbus Supplies back office and streaming live gateway logs.

**What you'll build**

A personal quick-reference of the CLI and slash commands used to run Nimbus Supplies day to day   (Tools: OpenClaw, openclaw CLI, in-chat slash commands.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. openclaw config — read and change settings.

   ```bash
   openclaw config list                        # show all settings
   openclaw config get model                   # get one setting
   openclaw config set model anthropic/claude-opus-4-7
   openclaw config edit                         # open the config file in $EDITOR
   ```

3. openclaw model — manage the brain.

   ```bash
   openclaw model list
   openclaw model current
   openclaw model use deepseek/deepseek-v4
   openclaw model test
   ```

4. openclaw doctor — health check (with auto-fix).

   ```bash
   openclaw doctor
   openclaw doctor --fix
   ```

5. openclaw gateway — control the daemon that runs everything.

   ```bash
   openclaw gateway status
   openclaw gateway start
   openclaw gateway stop
   openclaw gateway restart
   openclaw gateway logs --tail 50
   openclaw gateway install     # install daemon (LaunchAgent / systemd / Task Scheduler)
   ```

6. openclaw channel — manage the front doors.

   ```bash
   openclaw channel list
   openclaw channel add telegram --token <TOKEN>
   openclaw channel start whatsapp
   openclaw channel show telegram
   openclaw channel restart whatsapp
   openclaw channel remove telegram
   ```

7. openclaw tools and openclaw skills — capabilities.

   ```bash
   openclaw tools list
   openclaw tools list --enabled
   openclaw tools status agentmail

   openclaw skills list
   openclaw skills add web-research --source skills.sh
   openclaw skills remove web-research
   ```

8. In-chat slash commands. These work inside any channel (Telegram, WhatsApp, CLI chat). Try each from your Nimbus Supplies bot: | Slash Command | Purpose | | --- | --- | | /help | List all available slash commands | | /model <name> | Switch model for this conversation only | | /skill <name> [args] | Run an installed skill (e.g. /skill nimbus-quote "…") | | /tools | List tools the agent may use in this channel | | /clear | Clear the conversation history | | /memory | View / edit the agent's memory for this user | | /whoami | Show your user ID, channel, profile, and current model | | /stop | Cancel the current generation |
9. Watch it work live. In one terminal, follow the logs; in the channel, send a message and observe the corresponding lines:

   ```bash
   openclaw gateway logs --follow
   ```


**Test it**

You can switch the model both from chat (/model, per-conversation) and globally from the CLI (openclaw model use), /whoami returns your platform user ID, openclaw gateway logs --follow streams live activity, and /help lists the available slash commands.

> **Note:** Full commands and screenshots are in labs/lab-20-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 21 — Cron Jobs & Heartbeat

Learning outcome: LO4: Automate agent work with scheduled crons and a monitoring heartbeat..

Goal: The learner makes Nimbus Supplies run unattended by scheduling recurring tasks with cron (a nightly sales report and a weekly supplier price-check using Firecrawl) and monitoring uptime with the heartbeat, so the gateway self-checks, auto-restarts on failure, and can page an external monitor if it dies.

**What you'll build**

A nightly sales-report cron, a weekly price-check cron, and an enabled self-healing heartbeat   (Tools: OpenClaw, openclaw cron, gateway heartbeat, Firecrawl + AgentMail.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. Create the nightly sales-report cron. Cron syntax is <min> <hour> <day> <month> <weekday>.

   ```bash
   # Every day at 21:00 — post a Nimbus Supplies end-of-day summary to Telegram
   openclaw cron create \
     --schedule "0 21 * * *" \
     --prompt "Summarise today's Nimbus Supplies customer chats and any quotes sent. List open questions that still need a human." \
     --channel telegram \
     --name nightly-sales-report
   ```

3. Create a weekly supplier price-check cron (uses Firecrawl from Lab 19):

   ```bash
   # Every Monday at 08:00 — check supplier prices and email me
   openclaw cron create \
     --schedule "0 8 * * 1" \
     --prompt "Use Firecrawl to fetch our main supplier's A4 paper price and email me the current price via AgentMail with subject 'Weekly supplier price'." \
     --channel telegram \
     --name weekly-price-check
   ```

4. List and inspect your crons.

   ```bash
   openclaw cron list
   openclaw cron show nightly-sales-report
   openclaw cron logs nightly-sales-report --tail 20
   ```

5. Fire a cron on demand to test it now (ignores the schedule):

   ```bash
   openclaw cron run nightly-sales-report
   ```

6. Disable / enable / delete crons as your needs change:

   ```bash
   openclaw cron disable weekly-price-check
   openclaw cron enable  weekly-price-check
   openclaw cron delete  weekly-price-check   # only if you no longer need it
   ```

7. Enable the heartbeat. The heartbeat is a periodic self-check that verifies the gateway is alive, the model responds, and channels are connected; on failure the daemon attempts auto-restart and logs the incident.

   ```bash
   openclaw gateway heartbeat enable --interval 60s
   openclaw gateway heartbeat status
   openclaw gateway heartbeat logs --tail 20
   ```

8. (Optional) Push a heartbeat ping to an external monitor so you are paged if Nimbus Supplies goes dark (e.g. a free <https://healthchecks.io/> check):

   ```bash
   openclaw gateway heartbeat webhook \
     --url https://hc-ping.com/<your-uuid> \
     --interval 5m
   ```

9. Confirm auto-restart works. Ensure the daemon is installed to auto-start, then simulate a crash:

   ```bash
   openclaw gateway status        # expect "running" + "auto-start: yes"
   openclaw gateway stop
   # wait ~60s for the service manager to restart it
   openclaw gateway status        # expect "running" again
   ```


**Test it**

openclaw cron list shows nightly-sales-report and weekly-price-check, openclaw cron run delivers a summary to Telegram immediately, openclaw gateway heartbeat status reports healthy, and after openclaw gateway stop the service manager restarts the gateway within about a minute.

> **Note:** Full commands and screenshots are in labs/lab-21-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 22 — Memory & Context

Learning outcome: LO2: Give an agent persistent, user-scoped memory..

Goal: The learner gives the Nimbus Supplies agent durable memory so it recalls customer preferences across conversations: using the in-chat /memory command, inspecting where OpenClaw persists state under ~/.openclaw/, teaching a customer's standing preference, clearing the conversation to prove it is real memory, and confirming recall in a later separate chat.

**What you'll build**

An agent that persistently remembers a customer's standing preferences and applies them in a fresh conversation   (Tools: OpenClaw, /memory, /clear, ~/.openclaw/ state.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. See what OpenClaw stores on disk.

   ```bash
   ls -la ~/.openclaw/
   ```

3. Inspect your current memory from chat. In your Telegram or WhatsApp bot:

   ```bash
   /memory
   ```

4. Teach the agent a durable customer preference. Still in chat, send a plain-language instruction: > Remember this for future chats: our customer Acme Cafe always wants recycled A4 paper (never standard), delivery on Tuesdays only, and quotes addressed to Mei from Acme. Then confirm it was captured:

   ```bash
   /memory
   ```

5. Clear the conversation to prove it is real memory, not just context.

   ```bash
   /clear
   ```

6. Recall in a fresh conversation. In the now-cleared chat, ask something that requires the remembered facts: > Draft a quote for Acme Cafe: 10 reams of A4 paper and 5 boxes of black pens. A correct agent should automatically choose recycled A4, note Tuesday delivery, and address the quote to Mei — without you repeating any of it. (This pairs perfectly with the nimbus-quote skill from Lab 18.)
7. Edit or correct a memory. If a preference changes, update it in natural language and re-check: > Update your memory: Acme Cafe now accepts delivery on Tuesdays or Thursdays.

   ```bash
   /memory
   ```

8. Back up memory before major changes (memory lives under ~/.openclaw/, so the Lab 15 backup habit applies):

   ```bash
   mkdir -p ~/openclaw-backup-$(date +%F)
   cp -R ~/.openclaw/ ~/openclaw-backup-$(date +%F)/openclaw-state 2>/dev/null || true
   ```


**Test it**

/memory shows the customer preferences after you teach them, after /clear the /memory list still shows them (short-term context cleared, long-term memory retained), and a fresh quote request for the customer automatically applies recycled paper, Tuesday delivery and the correct recipient name without repetition.

> **Note:** Full commands and screenshots are in labs/lab-22-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 23 — Security

Learning outcome: LO4: Secure an agent with key management, allowlists, sandboxing and audit..

Goal: The learner hardens the Nimbus Supplies deployment before real customers: storing API keys as environment variables (never in cleartext config), restricting who can DM the bot with allowlists, applying per-channel tool deny lists, tightening the code-execution sandbox (timeout/memory/network), reviewing the audit log, and rotating provider keys.

**What you'll build**

A hardened agent with keys in env, DM allowlists, per-channel deny lists, a capped sandbox and an exported audit log   (Tools: OpenClaw, allowlists, tool deny lists, exec/python sandbox, gateway logs.)

**Step-by-step**

1. Watch the OpenClaw reference playlist

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J
   ```

2. Secure API keys — never hardcode or commit them. Store keys once as environment variables. macOS / Linux — append to ~/.zshrc or ~/.bashrc:

   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   export FIRECRAWL_API_KEY="fc-..."
   export AGENTMAIL_API_KEY="..."
   ```

3. Restrict who can DM the bot (allowlists). By default anyone who finds your Telegram bot can message it. Lock it to known users:

   ```bash
   openclaw channel set telegram \
     --allow-users 12345678,87654321 \
     --pair-mode allowlist
   ```

4. Apply tool deny lists (least privilege per channel). A customer-facing channel has no business running shell commands or deleting files:

   ```bash
   openclaw channel set telegram --deny exec,fs.write,fs.delete
   openclaw channel set telegram --allow group:web
   openclaw channel set telegram --profile messaging
   openclaw channel show telegram | grep -E "(allow|deny|profile)"
   ```

5. Tighten the code-execution sandbox. The exec / Python tools run sandboxed — cap time, memory, and network:

   ```bash
   openclaw tools config exec \
     --timeout 10s \
     --memory 256mb \
     --network deny

   openclaw tools config python \
     --timeout 30s \
     --memory 512mb \
     --network deny
   ```

6. Review the audit log. Every tool call, model call, and channel event is logged:

   ```bash
   openclaw gateway logs --tail 100
   openclaw gateway logs --filter tool=exec
   openclaw gateway logs --since 1h --filter level=warn
   openclaw gateway logs --export ~/openclaw-audit-$(date +%F).log
   ```

7. Rotate provider keys on a schedule (e.g. every 90 days). 1. Generate a new key in the provider dashboard. 2. Update the environment variable. 3. Restart the gateway: openclaw gateway restart. 4. Confirm openclaw model test still works. 5. Revoke the old key in the provider dashboard.

**Test it**

cat ~/.openclaw/config.toml does not contain raw API keys, a user not on the Telegram allowlist gets a not-authorized response, openclaw channel show telegram lists the deny list and messaging profile, and the audit log shows blocked exec attempts on a locked channel.

> **Note:** Full commands and screenshots are in labs/lab-23-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 24 — Multi-Agent Workforce

Learning outcome: LO5: Orchestrate cooperating multi-agent teams to deliver a business outcome..

Goal: In the OpenClaw capstone the learner splits the single agent into three cooperating agents — Sales (customer-facing on Telegram/WhatsApp), Research (supplier scouting with Firecrawl), and Ops (email, quotes, nightly crons) — each with least-privilege tools, and runs one end-to-end business scenario across all three, with a verified fallback using isolated OPENCLAW_HOME instances that cooperate via AgentMail and a shared folder.

**What you'll build**

A three-agent Sales/Research/Ops workforce that runs a customer order end-to-end into a real quote email   (Tools: OpenClaw, openclaw agent (or isolated OPENCLAW_HOME instances), Firecrawl, AgentMail.)

**Step-by-step**

1. Watch the OpenClaw multi-agent setup reference video

   ```bash
   https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=1
   ```

2. Create three named agents. Attempt the native multi-agent path first (confirm exact syntax in the docs):

   ```bash
   openclaw agent create sales
   openclaw agent create research
   openclaw agent create ops
   openclaw agent list
   ```

3. Give each agent least-privilege tools (mirrors Lab 19/23 allow-deny, applied per agent):

   ```bash
   # Sales — web + quoting only, no shell, no filesystem writes
   openclaw agent set sales --allow group:web --deny exec,fs.write,fs.delete

   # Research — scraping only
   openclaw agent set research --allow firecrawl,web_search,browser --deny exec,fs.write

   # Ops — email + files, no public channel exposure
   openclaw agent set ops --allow agentmail,group:fs
   ```

4. Attach channels to the right agents.

   ```bash
   # Customer traffic goes to Sales
   openclaw channel set telegram --agent sales
   openclaw channel set whatsapp --agent sales

   # A private research bot for the operator (see Lab 17 for creating a 2nd bot)
   openclaw channel add telegram --token <RESEARCH_BOT_TOKEN>
   openclaw channel set <research-bot> --agent research
   ```

5. Give each agent the right skill/memory. Sales uses nimbus-quote and the customer memory from Lab 22; Research uses nimbus-supplier-brief (Lab 18 exercise). Install/enable as needed:

   ```bash
   openclaw skills list
   ```

6. Wire cooperation between agents. The simplest, robust hand-off uses the tools you already have: - Sales → Ops: when Sales captures an order, it asks Ops (via a shared note file or an AgentMail message) to produce and send the quote. - Ops → Research: when a price is unknown ("TBC"), Ops asks Research to look it up with Firecrawl. - Research → Ops: Research replies with the price; Ops finalises the quote email.

   ```bash
   # Ops nightly consolidation cron (from Lab 21, now owned by Ops)
   openclaw cron create \
     --schedule "0 21 * * *" \
     --prompt "Compile today's Nimbus Supplies orders and quotes sent, and list anything waiting on Research." \
     --channel telegram \
     --name ops-nightly-report
   ```

7. Fallback (fully verified) — run agents as separate profiles/instances. If native multi-agent commands are not in your build, model each agent as its own OpenClaw configuration using only Lab 15–19 primitives: - Sales = your main instance with Telegram/WhatsApp, --profile messaging, deny exec,fs.write (Lab 23). - Research = a second instance pointed at a separate config dir with only Firecrawl/web tools enabled:

   ```bash
   OPENCLAW_HOME=~/.openclaw-research openclaw onboard
     OPENCLAW_HOME=~/.openclaw-research openclaw tools enable firecrawl --api-key "$FIRECRAWL_API_KEY"
   ```

8. Run the end-to-end capstone scenario. From a customer's Telegram, trigger the whole workflow: > Hi Nimbus Supplies — I'm Mei from Acme Cafe. I need 10 reams of recycled A4 paper and 5 boxes of black pens. What's your best price and when can you deliver? Expected chain: 1. Sales greets Mei, recalls Acme's preferences from memory (recycled paper, Tuesday delivery — Lab 22), and captures the order. 2. Sales hands the order to Ops, which starts the nimbus-quote. The pen price is unknown → marked TBC. 3. Ops asks Research to fetch the current pen price via Firecrawl. 4. Research replies with the price; Ops finalises the itemised quote (with GST) and emails it to Acme via AgentMail. 5. That night, the ops-nightly-report cron summarises the day, including Mei's order.

**Test it**

Three agents (or isolated instances) each have a distinct least-privilege tool set (Sales cannot exec, Research cannot write files, Ops is not on a public channel), a customer Telegram message produces a real quote email combining memory, the nimbus-quote skill, a Firecrawl price lookup and AgentMail delivery, and the nightly cron posts a summary referencing the same order.

> **Note:** Full commands and screenshots are in labs/lab-24-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 25 — Dreaming — Idle Reflection & Self-Improvement

Learning outcome: LO3: Use OpenClaw 'dreaming' so the agent reflects during idle time..

Goal: Enable OpenClaw's 'dreaming' feature so the Nimbus Supplies agent uses idle time to review its memory, consolidate what it has learned, and generate useful follow-up actions and skill improvements — then inspect what it produced. Reference the OpenClaw functions playlist for the walkthrough.

**What you'll build**

An agent that, when idle, 'dreams' — reflecting on memory and proposing follow-ups you can review.   (Tools: OpenClaw, dreaming, memory.)

**Step-by-step**

1. Watch the OpenClaw functions reference video. Open the playlist and watch the segment on the dreaming / idle-reflection feature. Note how the presenter enables it and where the produced insights appear — the on-screen command names are your ground truth for the steps below. https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J (https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)
2. Enable the dreaming feature in OpenClaw config. This flips the setting that lets the gateway schedule reflection cycles when the agent is idle:

   ```bash
   openclaw config set dreaming.enabled true
   ```

3. Let the agent sit idle so a dream cycle runs — or trigger one manually. Rather than wait for a natural idle window, force a cycle now so you can observe it immediately:

   ```bash
   openclaw dream run
   ```

4. Review what the dream produced. List the insights, follow-ups, and skill suggestions the cycle generated:

   ```bash
   openclaw dream list
   ```

5. Accept a useful follow-up the agent proposed. In the dashboard (or via the CLI shown in the video), open one proposal that genuinely helps Nimbus Supplies and approve it. Accepting promotes the proposal into a real action or a saved skill; declining discards it. This human review step keeps you in control of what the agent's downtime actually changes.

**Test it**

A dream cycle runs during idle time and produces reviewable insights/follow-ups from the agent's memory.

> **Note:** Full commands and screenshots are in labs/lab-25-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 26 — Use Cases & Key Functions

Learning outcome: LO3: Apply OpenClaw's key functions to real back-office use cases..

Goal: Tie the OpenClaw track together with practical use cases for Nimbus Supplies — a Google Workspace CLI assistant, a data-analytics agent, and a social-media-marketing agent — combining channels, skills, tools, memory, dreaming and crons into end-to-end automations. Each use case has its own reference video.

**What you'll build**

One or more end-to-end OpenClaw automations (Workspace, analytics or social media) solving a real use case.   (Tools: OpenClaw, skills, tools, Google Workspace, crons, memory.)

**Step-by-step**

1. Use case A — Google Workspace CLI assistant (reference video)

   ```bash
   https://www.youtube.com/watch?v=_ssB1YXRRtk&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=9
   ```

2. Watch one of the use-case videos above and study how the presenter composes several functions into one automation — which channel triggers the flow, which skills and tools it calls, and how memory and crons fit in. Good starting points: a Google Workspace CLI assistant (Docs/Sheets/Gmail), a Data Analytics agent, or a Social Media Marketing agent.
3. Pick a back-office use case. Choose one concrete Nimbus Supplies workflow to implement end-to-end. A strong default is "research a supplier, then email a quote": a customer asks for a price, the agent looks up current supplier pricing, applies a margin, and emails a formatted quote. Other options: customer FAQ Q&A on Telegram, or an automated nightly orders-and-quotes report.
4. Compose the channels, skills and tools needed for it. Wire the pieces together for your chosen use case. For research-to-quote that means: the customer channel (e.g. Telegram) as the trigger, the skill that formats a quote (e.g. nimbus-quote from Lab 18), a research tool (Firecrawl / web_search) for live pricing, and a delivery tool (AgentMail) to send the email. Confirm the agent has permission to call each one.
5. Run the automation end-to-end and verify the outcome. Send a real trigger — e.g. message the agent "What's your price for 50 kg of arabica beans?" on the customer channel — and watch the full chain fire: the agent recalls context from memory, runs the price lookup tool, builds the quote with the skill, and delivers it via email. Confirm the actual deliverable (the sent quote email) is correct, not just that the logs look busy.
6. Schedule it or hand it to the multi-agent team from Lab 24. Make the automation ongoing. Either attach it to a cron (e.g. a nightly consolidation report) so it runs unattended, or delegate the use case to the Sales / Research / Ops agents you built in Lab 24 so the right specialist owns each step. This is what turns a one-off demo into part of an always-on Nimbus Supplies back office.

**Test it**

A real use case (Google Workspace, data analytics or social media) runs end-to-end using OpenClaw's channels, skills, tools and crons.

> **Note:** Full commands and screenshots are in labs/lab-26-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


## Topic 03 — Paperclip — Running & Governing a Company of AI Agents  (34%)

Setup · Connect OpenAI Codex · Configure · Track Tasks · Automate Hiring · Setup Agents · Security · Assign Tasks

**Key concepts**

- Paperclip is an operating system for a company of AI agents, self-hosted with Docker Compose; you are the Board, a CEO agent reports to you, and specialists report to the CEO.
- You connect a coding model such as OpenAI Codex as the agents' engine, configure the company, and track AI tasks on a board: todo -> in_progress -> in_review -> done.
- Hiring is automated behind human approval gates; all durable state lives in an embedded PostgreSQL database whose activity_log (tagged by actor_type) and cost_events tables give a CFO-style audit trail.
- Security is enforced with budget caps (an 80% warning and a 100% pause rail) and approvals; you set up agents and assign tasks to deliver the company goal.


### Lab 27 — Setup Paperclip

Learning outcome: LO1: Install and self-host Paperclip, then found your company..

Goal: Watch the Paperclip overview, then self-host Paperclip with Docker Compose and create the Nimbus Coffee company with a single goal and a monthly budget.

**What you'll build**

A running Paperclip at http://localhost:3100 with a company (goal + budget).   (Tools: Paperclip, Docker Compose.)

**Step-by-step**

1. Watch the Paperclip overview (Explain Paperclip). This introduces the mental model: Paperclip runs an entire company of AI agents (a CEO who hires specialists), and you sit above them as the Board, approving hires and spend. Keep that framing in mind — every later lab maps to a real corporate function. https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31 (https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)
2. Watch the setup reference video for this lab. This is the exact self-hosting walkthrough for the steps below — follow along so the on-screen dashboard matches yours. https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2 (https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2)
3. Clone the Paperclip repository. This pulls the source and the Docker Compose files you need to run it locally:

   ```bash
   git clone https://github.com/paperclipai/paperclip.git
   cd paperclip
   ```

4. Start Paperclip with the quickstart compose file. This builds the image and brings up the full stack (the app plus its embedded PostgreSQL):

   ```bash
   docker compose -f docker-compose.quickstart.yml up --build
   ```

5. Open the dashboard. In your browser, go to:
6. Create the company with a single goal and a monthly budget. In the dashboard, start a new company. Name it Nimbus Coffee, Inc., give it one clear goal (e.g. "Launch a direct-to-consumer specialty coffee brand and make the first sale"), and set a monthly budget cap (your spend ceiling). Save. This company is the entity the CEO and specialist agents will work inside for every remaining Paperclip lab. > The exact wording of the "Create company" / goal / budget fields is version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

**Test it**

The dashboard loads at http://localhost:3100 and a company exists with a goal and budget.

> **Note:** Full commands and screenshots are in labs/lab-27-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 28 — Connect OpenAI Codex to Paperclip

Learning outcome: LO2: Connect a coding model (OpenAI Codex) as the agents' engine..

Goal: Give Paperclip's agents a brain by connecting the OpenAI Codex adapter, so the agents can reason and act. Confirm the adapter is detected and available.

**What you'll build**

Paperclip using the OpenAI Codex adapter as the agents' model.   (Tools: Paperclip, OpenAI Codex.)

**Step-by-step**

1. Watch the reference video for this lab. It shows exactly where Paperclip looks for the Codex adapter and what "available" looks like in Settings. https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3 (https://www.youtube.com/watch?v=gU5BrKo_iHk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=3)
2. Install / log in to the OpenAI Codex CLI so Paperclip can detect it. Follow the video's instructions to install the Codex CLI and authenticate (log in or supply your API key). Paperclip detects the adapter by finding this working Codex CLI/credentials on the host — so getting the login right here is the whole ballgame. > The exact install/login command is version-specific — verify in the video / docs (<https://docs.paperclip.ing>).
3. Open Settings → Agents / Adapters in the dashboard. In Paperclip at http://localhost:3100, go to Settings, then the Agents / Adapters section. This is where Paperclip lists every model engine it can use to power agents.
4. Confirm the OpenAI Codex adapter shows as "available". Look for the OpenAI Codex entry and check its status reads available (not "not detected" / "unavailable"). Available means Paperclip successfully found and authenticated the Codex CLI and can route agent reasoning through it.
5. Restart Paperclip if the adapter is not detected. If Codex still shows unavailable after you have logged in, restart the stack so Paperclip re-scans for the adapter:

   ```bash
   docker compose -f docker-compose.quickstart.yml restart
   ```


**Test it**

The OpenAI Codex adapter is detected and shows as available in Settings.

> **Note:** Full commands and screenshots are in labs/lab-28-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 29 — Configure Paperclip

Learning outcome: LO2: Configure the company — settings, budget and workspace..

Goal: Configure Nimbus Coffee: set the monthly budget, connect a workspace folder so agents write real files, and adjust company settings.

**What you'll build**

A configured company with a budget and a connected workspace folder.   (Tools: Paperclip, workspace.)

**Step-by-step**

1. Watch the reference video for this lab. It walks through the company settings screen — budget cap, workspace connection, and the other company options. https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4 (https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4)
2. Open the company's settings in the dashboard. At http://localhost:3100, open Nimbus Coffee, Inc. and go to its Settings. This is the per-company control panel (distinct from the app-wide Settings you used for adapters in Lab 28).
3. Set or adjust the monthly budget cap. Enter the maximum the company may spend per month. This cap is the governance rail you will exercise in Lab 33 (an 80% warning and a 100% pause). Set a deliberate figure you are comfortable letting agents spend against. > Field name/units are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).
4. Connect a workspace folder so agents create real deliverables. First create the folder on your machine:

   ```bash
   mkdir -p ~/paperclip-workspace/nimbus-coffee
   ```

5. Save the configuration and confirm it persists. Save the settings, reload the page, and confirm the budget and the connected workspace path are still shown. Persistence matters — it proves the config was written to the database, not just held in the browser.

**Test it**

The company shows the configured budget and a connected workspace folder.

> **Note:** Full commands and screenshots are in labs/lab-29-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 30 — Track AI Tasks

Learning outcome: LO3: Track AI work on the task board..

Goal: Use Paperclip's task board to track work through its four states — todo, in_progress, in_review, done — giving you visibility and control over what the agents are doing.

**What you'll build**

A task board showing AI tasks moving across the four states.   (Tools: Paperclip, task board.)

**Step-by-step**

1. Watch the reference video for this lab. It shows the task board layout and how tasks flow through the four columns. https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5 (https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5)
2. Open the task board for the company. In the dashboard, open Nimbus Coffee, Inc. and go to its task board. You'll see four columns — todo, in_progress, in_review, done — the single source of truth for everything the company is working on.
3. Create or observe a task in the "todo" column. Either create a task yourself (e.g. "Draft the Nimbus Coffee brand tagline") or watch one the CEO/agents have already queued. A task in todo is committed work that has not started yet.
4. Watch a task move todo → in_progress → in_review. As an agent picks up the task, it moves to in_progress; when the agent finishes and produces a deliverable, it moves to in_review, waiting for your judgement. Observing this flow is how you supervise a company of agents without micromanaging each action.
5. Open a shell to review the task activity log. For a deeper view than the UI, open a shell inside the running Paperclip container:

   ```bash
   docker compose -f docker-compose.quickstart.yml exec paperclip sh
   ```


**Test it**

Tasks are visible on the board and move through todo -> in_progress -> in_review -> done.

> **Note:** Full commands and screenshots are in labs/lab-30-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 31 — Automate AI Hiring

Learning outcome: LO3: Automate hiring of the CEO and specialist agents behind approval gates..

Goal: Hire your CEO agent and let it propose specialist hires, each passing a human approval gate. This is how the company staffs itself automatically while you stay in control.

**What you'll build**

An approved CEO agent and one or more approved specialist agents.   (Tools: Paperclip, approval gates.)

**Step-by-step**

1. Watch the reference video for this lab. It shows the hiring flow: hiring the CEO, the CEO proposing specialists, and the approval gate you control. https://www.youtube.com/watch?v=tgqcHHxiwfk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=6 (https://www.youtube.com/watch?v=tgqcHHxiwfk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=6)
2. Hire the CEO agent from the company page. On the Nimbus Coffee, Inc. page, choose to hire the CEO. The CEO is the top agent that reads the company goal and works out what roles the company needs to achieve it.
3. Approve the CEO hire (you are the Board). The hire pauses at an approval gate. Review it and approve — as the Board, nothing joins the company without your sign-off. This is the core governance pattern: agents propose, humans approve.
4. Let the CEO propose specialist hires. Once active, the CEO analyses the goal and proposes specialists it needs (for a coffee brand, perhaps a Marketer, an Engineer for the storefront, and an Operations agent). Each proposal explains the role and why it helps reach the goal.
5. Review and approve each specialist at the approval gate. For every proposed hire, review the role and approve or reject it at the gate. Approve the ones that genuinely serve the Nimbus Coffee goal; reject any that don't. Each approval is recorded as a human decision — an actor_type=user entry in the audit trail you'll inspect in Lab 33.

**Test it**

The CEO and approved specialists are active; each hire is logged as an actor_type=user decision.

> **Note:** Full commands and screenshots are in labs/lab-31-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 32 — Setup AI Agents

Learning outcome: LO2: Set up and configure the AI agents and their capabilities..

Goal: Configure the hired agents — their mandate, tools and per-agent budget caps — so each specialist can carry out the delegated work for Nimbus Coffee.

**What you'll build**

Configured agents with mandates, tools and per-agent budgets.   (Tools: Paperclip, agents.)

**Step-by-step**

1. Watch the reference video for this lab. It shows an agent's configuration screen — mandate, tools, and per-agent budget. https://www.youtube.com/watch?v=JLnGSWK4bJY&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=7 (https://www.youtube.com/watch?v=JLnGSWK4bJY&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=7)
2. Open an agent's configuration. On the Nimbus Coffee page, pick one specialist (e.g. the Marketer) and open its configuration. This is where you turn a generic hire into a purpose-built role.
3. Set the agent's mandate and the tools it may use. Write a crisp mandate — one or two sentences on exactly what this agent is responsible for (e.g. "Own Nimbus Coffee's brand voice and launch marketing copy"). Then grant only the tools it needs (e.g. file-write to the workspace, web research) and withhold the rest. Least privilege here prevents an agent from straying outside its lane. > Tool names and the mandate field are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).
4. Set a per-agent budget cap. Give this agent its own spend ceiling, carved out of the company budget. Per-agent caps mean one runaway agent can't drain the whole company — a key safety rail you'll exercise in Lab 33.
5. Save and confirm the agent is ready to receive tasks. Save the configuration, reload, and confirm the mandate, tools, and budget persist and the agent's status shows it is ready for work. Repeat steps 2–5 for each specialist you approved.

**Test it**

Each agent has a mandate, allowed tools and a budget cap, and is ready for tasks.

> **Note:** Full commands and screenshots are in labs/lab-32-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 33 — Security

Learning outcome: LO3: Secure the company with budgets, safety rails and approvals..

Goal: Apply Paperclip's governance: company-wide and per-agent budget caps trigger an 80% warning and a 100% pause; approvals gate risky decisions; the audit trail records everything.

**What you'll build**

Budget caps with the 80% warning and 100% pause rails demonstrated, plus an audit review.   (Tools: Paperclip, budgets, PostgreSQL audit.)

**Step-by-step**

1. Watch the reference video for this lab. It demonstrates the budget rails (80% warning, 100% pause), resuming, and the audit trail. https://www.youtube.com/watch?v=77uTzIqw8SQ&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=8 (https://www.youtube.com/watch?v=77uTzIqw8SQ&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=8)
2. Set a company and/or per-agent budget cap. In the company settings (Lab 29) and/or an agent's config (Lab 32), set a deliberately small cap so ongoing agent work will approach it during this lab. This is what lets you observe the safety rails fire instead of waiting days.
3. Trigger the 80% warning and 100% pause, then resume. Let the agents keep working (assign a task or two). As spend crosses 80% of the cap, Paperclip raises a warning; at 100% it pauses the company/agent so nothing can overspend. Review the pause, then resume (e.g. by raising the cap or explicitly resuming) and confirm work continues. You have now seen both the soft and hard money rails in action.
4. Audit actions and spend in the embedded PostgreSQL. Connect to Paperclip's database to inspect the ground-truth record:

   ```bash
   psql "postgresql://postgres@localhost:5432/paperclip"
   ```

5. Separate human vs agent actions with actor_type. Run the audit query to see how much of the company's activity was human decisions versus agent actions:

   ```bash
   SELECT actor_type, COUNT(*) FROM activity_log GROUP BY actor_type;
   ```


**Test it**

The 80% warning and 100% pause fire, resume works, and the audit shows actions by actor_type and total spend.

> **Note:** Full commands and screenshots are in labs/lab-33-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


### Lab 34 — Assign Task

Learning outcome: LO3: Assign and delegate tasks to run the company end-to-end..

Goal: Delegate real work: assign tasks to specialists, watch them execute and produce deliverables in the workspace, and review and accept the results to complete the Nimbus Coffee goal.

**What you'll build**

Assigned tasks executed by agents, producing real deliverables you review and accept.   (Tools: Paperclip, task board, workspace.)

**Step-by-step**

1. Watch the reference video for this lab. It shows assigning a task, the agent executing it, and reviewing the deliverable. https://www.youtube.com/watch?v=kAGzMnQ3_Cs&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=9 (https://www.youtube.com/watch?v=kAGzMnQ3_Cs&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=9)
2. Assign a task to a specialist agent. On the task board (Lab 30), create a concrete task and assign it to the right specialist — e.g. give the Engineer "Build a one-page Nimbus Coffee landing page in the workspace", or the Marketer "Write the launch tagline and hero copy". Match the task to the mandate you set in Lab 32.
3. Watch the agent execute and write output to the workspace. The task moves todo → in_progress as the agent works. When it finishes, check that a real file appeared in your workspace:

   ```bash
   ls -R ~/paperclip-workspace/nimbus-coffee
   ```

4. Review the deliverable in the in_review state. The task is now in in_review, waiting on you. Open the produced file and judge it against the task and the company goal. As the Board, you are the quality gate.
5. Approve to move it to done, or send it back for revision. If the deliverable is good, approve it — the task moves to done and that slice of the Nimbus Coffee goal is complete. If it falls short, send it back for revision with feedback, and the agent iterates. Either way, you stayed in control end-to-end.

**Test it**

An assigned task is executed by an agent, produces a real file, and is reviewed and accepted to done.

> **Note:** Full commands and screenshots are in labs/lab-34-*.md. Use only accounts, keys and hosts you own, and keep agents under human oversight.

---


## Wrap-Up — The Agent Build Arc and Governance

These cross-cutting themes run through every platform in the course. Study this section alongside the labs so the same skillset transfers from Hermes to OpenClaw to Paperclip and into your own production agents.

**The agent build arc**

Every platform follows the same progression — the order in which you built each agent in the labs:

- Install — set up the runtime (Hermes CLI/TUI, the OpenClaw Node.js gateway daemon, or Paperclip via Docker Compose).
- Models — connect an LLM provider (Claude, OpenAI, OpenRouter, MiniMax or DeepSeek) and pick a capable model.
- Channels — reach the agent where work happens (Telegram, WhatsApp, Discord, Slack and more).
- Memory — give the agent durable, user- or company-scoped recall across sessions and surfaces.
- Skills & tools — extend the agent with reusable skills and third-party tool/integration calls.
- Crons & heartbeat — schedule recurring work and let a heartbeat keep the agent running.
- Security — isolate execution in sandboxes, store secrets in config, and gate risky actions with approvals.
- Multi-agent — orchestrate a coordinator plus specialist workers to deliver an end-to-end business outcome.

**Human-in-the-loop governance**

- Approvals — important or destructive actions pause for explicit human sign-off before they run.
- Budgets — company- and per-agent spend caps warn at 80% and pause at 100% so costs never run away.
- Sandboxing — agents execute in isolated backends (Docker, SSH, or a remote host) so the host stays safe.
- Audit — an activity log and cost-events trail record who did what, giving you a CFO-style view of the workforce.
- Least privilege — scope each channel, skill and tool with allow/deny lists so agents can only do their job.

---


## Next Steps

- First pass: complete every lab on your own machine, following the commands in each lab file.
- Second pass: redo the labs from memory until installing, connecting and securing an agent is automatic.
- Extend the labs with your own skills, tools and integrations for a workflow you care about.
- Deploy an agent on a VPS or cloud backend for 24/7 operation, with budgets, approvals and audit turned on.
- Explore multi-agent orchestration — a coordinator plus specialists — for a realistic end-to-end business task.
- Review each lab's detailed steps in this guide and re-run the labs on your own machine.


## Glossary

- **Autonomous AI agent** — An LLM-driven system that perceives, reasons, acts with tools and remembers, running under human oversight.
- **Agent stack** — The layers that make an agent work: model, memory, skills, tools, channels and a scheduler/security layer.
- **Model / provider** — The LLM (and the vendor serving it) that gives the agent its reasoning — e.g. Claude, OpenAI, OpenRouter.
- **Channel** — A messaging surface the agent is reachable on, such as Telegram, WhatsApp, Discord or Slack.
- **Memory** — Durable, user- or company-scoped storage that lets the agent recall context across sessions and surfaces.
- **Skill** — A reusable, named capability an agent can install or create and invoke on demand.
- **Tool / integration** — An external action or service the agent can call — web search, image generation, email, GitHub via MCP.
- **MCP** — Model Context Protocol — a standard way to connect an agent to external tool servers.
- **Cron / heartbeat** — A schedule that triggers recurring agent work; a heartbeat self-checks and keeps the agent running.
- **Sandbox** — An isolated execution backend (Docker, SSH, remote host) that contains what an agent's commands can touch.
- **Approval gate** — A human sign-off required before an agent performs an important or destructive action.
- **Budget cap** — A spend limit at company or per-agent level that warns at 80% and pauses work at 100%.
- **Multi-agent orchestration** — A coordinator agent delegating to specialist worker agents to deliver an end-to-end outcome.
