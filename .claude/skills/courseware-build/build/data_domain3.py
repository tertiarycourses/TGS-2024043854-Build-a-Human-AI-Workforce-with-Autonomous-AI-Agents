"""
Domain 3 — Paperclip (a company of AI agents). Labs 27-32, topic 3.

Running use case: found and govern "Tertiary AI News Research", a zero-human
AI-news-research company you direct as the Board. The labs mirror a real live
build (dashboard at http://localhost:3100): install on Windows & Mac, set up
the company + CEO + mission, wire a model adaptor, create a detailed task
backlog (whose core task is hiring the team), add the Tavily Search API, and
hire the members under the hiring task. Reference videos come from the
Paperclip playlist (PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC). This module is the
single source of truth for the Paperclip slides / LP / LG.
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
        desc="Found 'Tertiary AI News Research': create the company, write its mission (research and publish a reliable daily AI-news briefing), set the monthly budget, then hire the CEO agent — the Chief Officer who will run the news desk and report to you, the Board.",
        build="A company with a mission and budget, plus an approved CEO agent at the top of the org chart.",
        services="Paperclip, company settings, org chart",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="gU5BrKo_iHk", i=3)),
            ("Create the company 'Tertiary AI News Research' from the company switcher", ""),
            ("Write the mission: 'Research the AI landscape daily and publish a verified, cited AI-news briefing' — this steers every agent the company hires", ""),
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
        desc="Give the company's agents a brain. Paperclip ships three built-in adaptors — Claude Code (claude_local), Codex (codex_local) and Gemini CLI (gemini_local) — and supports installable external adaptors (alpha). Confirm your adaptor is detected so every hired agent can reason and act with it.",
        build="A detected, enabled model adaptor (Claude Code, Codex or Gemini CLI) powering the agents.",
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
        desc="Write the backlog that runs the news desk. Every task gets a precise title AND a detailed description — the description is the agent's brief, so vague tasks produce vague work. The core task is hiring the team; the rest build the news-research pipeline around it.",
        build="A Tasks board holding six well-specified tasks, with 'Hire the core team' as the core task.",
        services="Paperclip, Tasks board",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="FrYvRd0KX_I", i=5)),
            ("Create the CORE task — 'Hire the core team and create a hiring plan': 'Based on the coverage strategy, propose which agents to hire (research analyst, news writer, fact-checker, editor/publisher) with roles, budgets and reporting lines.' Assign it to the CEO", ""),
            ("Create 'Define the AI news coverage strategy and editorial plan': 'Pick the beats (models, chips, policy, funding), the daily cadence, the briefing format and the quality bar for every published story.'", ""),
            ("Create 'Scaffold the news-desk workspace & tooling foundation': 'Set up the workspace folder structure, briefing templates, style guide and source register the whole team will use.'", ""),
            ("Create 'Build the AI news sources watchlist': 'Assemble the RSS feeds, publication sites, X accounts, arXiv categories and company blogs to monitor, with priority tiers and de-duplication rules.'", ""),
            ("Create 'Produce the first daily AI news briefing': 'Pull the top stories from the watchlist, verify each against two independent sources, and draft a cited briefing for Board review.'", ""),
            ("Create 'Wire the research pipeline to live search': 'Integrate the Tavily Search API so researchers query the live web with fresh results (depends on the Tavily key from the next lab).'", ""),
        ],
        test="The Tasks board shows all six tasks, each with a detailed description, and the hiring task is assigned to the CEO.",
    ),
    dict(
        num=31, topic=3,
        title="Add the Tavily Search API",
        objective="LO2: Wire live web search into the company via the Tavily Search API.",
        desc="A news-research company needs fresh information. Create a Tavily API key, store it as a company Secret, and bind it to the TAVILY_API_KEY runtime environment variable — Paperclip resolves the secret server-side when a run starts, so the key never sits in a prompt or a repo.",
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
        desc="Let the company staff itself. The CEO works the core hiring task — proposing the specialist roles for the news desk (research analyst, news writer, fact-checker, editor/publisher) with budgets and reporting lines — and every hire pauses at an approval gate for you, the Board, to approve.",
        build="An approved core team under the CEO, visible in the Agents list and the org chart, ready to take the backlog.",
        services="Paperclip, hiring task, approval gates, org chart",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="tgqcHHxiwfk", i=6)),
            ("Open the core hiring task and move it to in_progress — the CEO drafts the hiring plan in the task", ""),
            ("Review the proposed roles, budgets and reporting lines in the task's hiring plan", ""),
            ("Approve each proposed hire at its approval gate (or reject and ask for a revised proposal)", ""),
            ("Confirm the new members appear under Agents and on the Org chart beneath the CEO", ""),
            ("Assign the rest of the backlog to the new team and watch tasks move todo → in_progress → in_review → done", ""),
        ],
        test="The hiring task reaches in_review/done, every hire was Board-approved, and the specialists appear on the org chart taking backlog tasks.",
    ),
]
