"""
Domain 3 — Paperclip (a company of AI agents). Labs 27-33, topic 3.

Running use case: found and govern "Altera AI Blogs", a zero-human company you
direct as the Board whose mission is to research the AI landscape and publish
AI-related blogs end to end. The labs mirror a real live build (dashboard at
http://localhost:3100): install on Windows & Mac, set up the company + CEO +
mission, wire a model adaptor, create a detailed task backlog whose core task
hires the agents to publish the blogs end to end, add the Tavily Search API,
hire the members under the hiring task, then automate publication with a
daily 3pm routine. Reference videos come from the Paperclip playlist
(PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC). This module is the single source of
truth for the Paperclip slides / LP / LG.
"""

_PP = "https://www.youtube.com/watch?v={v}&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index={i}"
# Concept overview ("Explain Paperclip") — used as an intro reference on the first lab.
_EXPLAIN = "https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31"

DOMAIN3 = [
    dict(
        num=27, topic=3,
        title="Install Paperclip on Windows & Mac",
        objective="LO1: Install and self-host Paperclip on Windows and macOS.",
        desc="Watch the Paperclip overview, then self-host Paperclip with Docker Compose on your own machine — Docker Desktop on macOS, or Docker Desktop + WSL2 on Windows — and open the dashboard at http://localhost:3100.",
        build="A running Paperclip instance at http://localhost:3100 on Windows or Mac.",
        services="Paperclip, Docker Desktop, Docker Compose",
        steps=[
            ("Watch the Paperclip overview (Explain Paperclip)", _EXPLAIN),
            ("Watch the setup reference video for this lab", _PP.format(v="f2eian-bR_U", i=2)),
            ("Install Docker Desktop — macOS: download from docker.com; Windows: enable WSL2 first, then install Docker Desktop with the WSL2 backend", "wsl --install"),
            ("Clone the Paperclip repository", "git clone https://github.com/paperclipai/paperclip.git"),
            ("Start Paperclip with the quickstart compose file (same command in the macOS Terminal or the Windows WSL2/PowerShell shell)", "docker compose -f docker-compose.quickstart.yml up --build"),
            ("Open the dashboard in your browser at http://localhost:3100 and create your Board account", ""),
        ],
        test="Docker shows the Paperclip containers running and the dashboard loads at http://localhost:3100 on your platform.",
    ),
    dict(
        num=28, topic=3,
        title="Setup Company, CEO & Mission",
        objective="LO2: Found the company — name, mission and the CEO agent.",
        desc="Found 'Altera AI Blogs': create the company, write its mission (research the AI landscape daily and publish AI-related blogs end to end), set the monthly budget, then hire the CEO agent — the Chief Officer who will run the blog operation and report to you, the Board.",
        build="A company with a mission and budget, plus an approved CEO agent at the top of the org chart.",
        services="Paperclip, company settings, org chart",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="gU5BrKo_iHk", i=3)),
            ("Create the company 'Altera AI Blogs' from the company switcher", ""),
            ("Write the mission: 'Research the AI landscape daily and publish AI-related blogs end to end' — this steers every agent the company hires", ""),
            ("Set the monthly budget cap in Company Settings", ""),
            ("Hire the CEO agent (Chief Officer) and approve the hire — you are the Board", ""),
            ("Open the Org page and confirm the structure: Board above the CEO", ""),
        ],
        test="The company exists with a mission and budget, and an approved CEO agent sits under the Board on the org chart.",
    ),
    dict(
        num=29, topic=3,
        title="Setup Adaptor",
        objective="LO2: Connect a model adaptor as the agents' engine.",
        desc="Give every Altera AI Blogs agent a brain. An adaptor is the bridge between Paperclip and the language model that does the reasoning: when any agent (the CEO or a specialist) picks up a task, Paperclip hands the work to the adaptor, which runs it on the underlying model and streams the result back to the task. Paperclip ships three BUILT-IN adaptors that piggyback on locally installed CLIs — Claude Code (claude_local, 9 models), Codex (codex_local, 10 models) and Gemini CLI (gemini_local, 8 models) — and supports installable EXTERNAL adaptor packages (alpha). You install/log in to the CLI on the host so Paperclip can detect it, confirm it shows as available under Settings → Instance settings → Adapters, use the power icon to hide adaptors you don't want agents to pick, and restart Paperclip if detection fails. Whatever adaptor you enable here powers every hire in Labs 30-33.",
        build="A detected, enabled model adaptor (Claude Code, Codex or Gemini CLI) powering every Altera AI Blogs agent.",
        services="Paperclip, model adaptors (Claude Code / Codex / Gemini CLI)",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="WItGcCiQRKw", i=4)),
            ("Install / log in to the adaptor CLI on the host so Paperclip can detect it (e.g. Claude Code or the OpenAI Codex CLI)", ""),
            ("Open Settings → Instance settings → Adapters in the dashboard", ""),
            ("Confirm the built-in adaptors are listed — Claude Code (9 models), Codex (10 models), Gemini CLI (8 models) — and yours shows as available", ""),
            ("Use the power icon to hide adaptors you don't want agents to pick; 'Install Adapter' adds external adaptor packages (alpha)", ""),
            ("Restart Paperclip if your adaptor is not detected", "docker compose -f docker-compose.quickstart.yml restart"),
        ],
        test="Settings → Adapters lists the built-in adaptors and your chosen adaptor is detected and enabled for agents.",
    ),
    dict(
        num=30, topic=3,
        title="Create the Task Backlog",
        objective="LO3: Create a detailed task backlog that drives the company.",
        desc="Write the backlog that runs Altera AI Blogs. Every task gets a precise title AND a detailed description — the description is the agent's brief, so vague tasks produce vague work. The CORE task is 'Hire the agents to publish the AI-related blogs end to end'; the rest build the blog pipeline around it.",
        build="A Tasks board holding six well-specified tasks, with the end-to-end blog-publishing hire as the core task.",
        services="Paperclip, Tasks board",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="FrYvRd0KX_I", i=5)),
            ("Create the CORE task — 'Hire the agents to publish the AI-related blogs end to end': 'Based on the content strategy, propose which agents to hire (research analyst, blog writer, editor/publisher, SEO/marketer) with roles, budgets and reporting lines, so the company can research, write, edit and publish AI blogs without human writers.' Assign it to the CEO", ""),
            ("Create 'Define the AI blog content strategy and editorial plan': 'Pick the beats (models, chips, policy, funding), the publishing cadence, the blog format and the quality bar for every published post.'", ""),
            ("Create 'Scaffold the blog workspace & tooling foundation': 'Set up the workspace folder structure, post templates, style guide and source register the whole team will use.'", ""),
            ("Create 'Build the AI news sources watchlist': 'Assemble the RSS feeds, publication sites, X accounts, arXiv categories and company blogs to monitor, with priority tiers and de-duplication rules.'", ""),
            ("Create 'Produce and publish the first AI blog post': 'Pull the top stories from the watchlist, verify each against two independent sources, draft a cited post and publish it for Board review.'", ""),
            ("Create 'Wire the research pipeline to live search': 'Integrate the Tavily Search API so researchers query the live web with fresh results (depends on the Tavily key from the next lab).'", ""),
        ],
        test="The Tasks board shows all six tasks, each with a detailed description, and the core hiring task is assigned to the CEO.",
    ),
    dict(
        num=31, topic=3,
        title="Add the Tavily Search API",
        objective="LO2: Wire live web search into the company via the Tavily Search API.",
        desc="A blog company needs fresh information. Create a Tavily API key, store it as a company Secret, and bind it to the TAVILY_API_KEY runtime environment variable — Paperclip resolves the secret server-side when a run starts, so the key never sits in a prompt or a repo.",
        build="A TAVILY_API_KEY secret bound to the agents' runtime environment, verified with a live search task.",
        services="Paperclip, Secrets, Tavily Search API",
        steps=[
            ("Create a Tavily account and copy an API key from app.tavily.com", ""),
            ("Open Settings → Company settings → Secrets and click 'New secret'", ""),
            ("Store the key as a secret (e.g. name it tavily) — secrets are injected at run start, never shown to agents in plain text", ""),
            ("Bind it: open an agent's Environment variables (or a project's Env field), add the key TAVILY_API_KEY, choose Secret, and select the stored secret", ""),
            ("Verify with a task: 'Use Tavily to find today's three biggest AI announcements and list your sources' — the agent should return fresh, cited results", ""),
        ],
        test="The secret exists, TAVILY_API_KEY is bound to the runtime env, and a live-search task returns fresh cited results.",
    ),
    dict(
        num=32, topic=3,
        title="Hire the Members Under the Hiring Task",
        objective="LO3: Staff the company through the hiring task, behind approval gates.",
        desc="Let Altera AI Blogs staff itself — all of it happening UNDER the core task from Lab 30, 'Hire the agents to publish the AI-related blogs end to end'. You move that task to in_progress and the CEO works it: inside the task it drafts a hiring plan proposing each specialist the blog pipeline needs — a research analyst (scans the watchlist and verifies stories), a blog writer (drafts cited posts), an editor/publisher (reviews, formats and publishes) and an SEO/marketer (titles, tags and distribution) — each with a mandate, a budget cap and a reporting line to the CEO. Every proposed hire pauses at an approval gate for you, the Board: approve it and the agent is created; reject it and the CEO revises the plan. When the gates clear, the new members appear in the Agents sidebar and on the Org chart beneath the CEO, and you assign them the rest of the backlog so the pipeline runs end to end — research → draft → edit → publish.",
        build="A Board-approved blog team (research analyst, blog writer, editor/publisher, SEO/marketer) hired under the core task, visible on the org chart and taking the backlog.",
        services="Paperclip, hiring task, approval gates, org chart",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="tgqcHHxiwfk", i=6)),
            ("Open the CORE task 'Hire the agents to publish the AI-related blogs end to end' and move it to in_progress — the CEO drafts the hiring plan inside this task", ""),
            ("Review the proposed roles in the task's hiring plan — research analyst, blog writer, editor/publisher, SEO/marketer — each with budget and reporting line", ""),
            ("Approve each proposed hire at its approval gate (or reject and ask for a revised proposal) — you are the Board", ""),
            ("Confirm the new members appear under Agents and on the Org chart beneath the CEO", ""),
            ("Assign the rest of the backlog to the new team and watch the pipeline run: research → draft → edit → publish, todo → in_progress → in_review → done", ""),
        ],
        test="The core hiring task reaches in_review/done, every hire was Board-approved under that task, and the specialists appear on the org chart publishing the first posts.",
    ),
    dict(
        num=33, topic=3,
        title="Routine & Trigger — Publish Daily at 3pm",
        objective="LO3: Automate the company with a scheduled routine and trigger.",
        desc="Put Altera AI Blogs on autopilot. Create a Routine with a daily 3:00pm trigger that generates and runs the blog-publishing task automatically — the routine fires, creates the day's 'Produce and publish today's AI blog post' task, the team executes the pipeline (research → draft → edit → publish), and the finished post lands in in_review for the Board. No human kicks it off.",
        build="A daily 3:00pm routine that generates and runs the blog-publishing task automatically.",
        services="Paperclip, Routines, triggers, Tasks board",
        steps=[
            ("Open the Routines page from the sidebar (Work → Routines)", ""),
            ("Create a new routine: 'Daily AI blog publish'", ""),
            ("Set the trigger: schedule, daily at 3:00pm (15:00)", ""),
            ("Define what the routine generates: the task 'Produce and publish today's AI blog post' — pull the top stories from the watchlist, verify against two sources, draft a cited post, publish for Board review — assigned to the team", ""),
            ("Save and enable the routine, then trigger it once manually to confirm it creates and runs the task", ""),
            ("At the next 3:00pm, confirm the task was generated and executed automatically and the post is in in_review", ""),
        ],
        test="The routine is enabled with a daily 15:00 trigger, a manual run creates and executes the publish task, and the next 3pm run happens without human action.",
    ),
]
