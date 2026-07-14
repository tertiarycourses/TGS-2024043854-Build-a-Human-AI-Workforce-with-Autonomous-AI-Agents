"""
Domain 3 — Paperclip (a company of AI agents). Labs 27-34, topic 3.

Running use case: found and run "Nimbus Coffee, Inc.", a zero-human company you
govern as the Board. Each lab follows a reference video from the Paperclip
playlist (PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC). The video is the first step of
each lab. This module is the single source of truth for the Paperclip slides / LP / LG.
"""

_PP = "https://www.youtube.com/watch?v={v}&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index={i}"
# Concept overview ("Explain Paperclip") — used as an intro reference on Lab 1.
_EXPLAIN = "https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31"

DOMAIN3 = [
    dict(
        num=27, topic=3,
        title="Setup Paperclip",
        objective="LO1: Install and self-host Paperclip, then found your company.",
        desc="Watch the Paperclip overview, then self-host Paperclip with Docker Compose and create the Nimbus Coffee company with a single goal and a monthly budget.",
        build="A running Paperclip at http://localhost:3100 with a company (goal + budget).",
        services="Paperclip, Docker Compose",
        steps=[
            ("Watch the Paperclip overview (Explain Paperclip)", _EXPLAIN),
            ("Watch the setup reference video for this lab", _PP.format(v="f2eian-bR_U", i=2)),
            ("Clone the Paperclip repository", "git clone https://github.com/paperclipai/paperclip.git"),
            ("Start Paperclip with the quickstart compose file", "docker compose -f docker-compose.quickstart.yml up --build"),
            ("Open the dashboard", "# http://localhost:3100"),
            ("Create the company with a single goal and a monthly budget", ""),
        ],
        test="The dashboard loads at http://localhost:3100 and a company exists with a goal and budget.",
    ),
    dict(
        num=28, topic=3,
        title="Connect OpenAI Codex to Paperclip",
        objective="LO2: Connect a coding model (OpenAI Codex) as the agents' engine.",
        desc="Give Paperclip's agents a brain by connecting the OpenAI Codex adapter, so the agents can reason and act. Confirm the adapter is detected and available.",
        build="Paperclip using the OpenAI Codex adapter as the agents' model.",
        services="Paperclip, OpenAI Codex",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="gU5BrKo_iHk", i=3)),
            ("Install/log in to the OpenAI Codex CLI so Paperclip can detect it", ""),
            ("Open Settings -> Agents / Adapters in the dashboard", ""),
            ("Confirm the OpenAI Codex adapter shows as 'available'", ""),
            ("Restart Paperclip if the adapter is not detected", "docker compose -f docker-compose.quickstart.yml restart"),
        ],
        test="The OpenAI Codex adapter is detected and shows as available in Settings.",
    ),
    dict(
        num=29, topic=3,
        title="Configure Paperclip",
        objective="LO2: Configure the company — settings, budget and workspace.",
        desc="Configure Nimbus Coffee: set the monthly budget, connect a workspace folder so agents write real files, and adjust company settings.",
        build="A configured company with a budget and a connected workspace folder.",
        services="Paperclip, workspace",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="WItGcCiQRKw", i=4)),
            ("Open the company's settings in the dashboard", ""),
            ("Set or adjust the monthly budget cap", ""),
            ("Connect a workspace folder so agents create real deliverables", "mkdir -p ~/paperclip-workspace/nimbus-coffee"),
            ("Save the configuration and confirm it persists", ""),
        ],
        test="The company shows the configured budget and a connected workspace folder.",
    ),
    dict(
        num=30, topic=3,
        title="Track AI Tasks",
        objective="LO3: Track AI work on the task board.",
        desc="Use Paperclip's task board to track work through its four states — todo, in_progress, in_review, done — giving you visibility and control over what the agents are doing.",
        build="A task board showing AI tasks moving across the four states.",
        services="Paperclip, task board",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="FrYvRd0KX_I", i=5)),
            ("Open the task board for the company", ""),
            ("Create or observe a task in the 'todo' column", ""),
            ("Watch a task move todo -> in_progress -> in_review", ""),
            ("Open a shell to review the task activity log", "docker compose -f docker-compose.quickstart.yml exec paperclip sh"),
        ],
        test="Tasks are visible on the board and move through todo -> in_progress -> in_review -> done.",
    ),
    dict(
        num=31, topic=3,
        title="Automate AI Hiring",
        objective="LO3: Automate hiring of the CEO and specialist agents behind approval gates.",
        desc="Hire your CEO agent and let it propose specialist hires, each passing a human approval gate. This is how the company staffs itself automatically while you stay in control.",
        build="An approved CEO agent and one or more approved specialist agents.",
        services="Paperclip, approval gates",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="tgqcHHxiwfk", i=6)),
            ("Hire the CEO agent from the company page", ""),
            ("Approve the CEO hire (you are the Board)", ""),
            ("Let the CEO propose specialist hires", ""),
            ("Review and approve each specialist at the approval gate", ""),
        ],
        test="The CEO and approved specialists are active; each hire is logged as an actor_type=user decision.",
    ),
    dict(
        num=32, topic=3,
        title="Setup AI Agents",
        objective="LO2: Set up and configure the AI agents and their capabilities.",
        desc="Configure the hired agents — their mandate, tools and per-agent budget caps — so each specialist can carry out the delegated work for Nimbus Coffee.",
        build="Configured agents with mandates, tools and per-agent budgets.",
        services="Paperclip, agents",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="JLnGSWK4bJY", i=7)),
            ("Open an agent's configuration", ""),
            ("Set the agent's mandate and the tools it may use", ""),
            ("Set a per-agent budget cap", ""),
            ("Save and confirm the agent is ready to receive tasks", ""),
        ],
        test="Each agent has a mandate, allowed tools and a budget cap, and is ready for tasks.",
    ),
    dict(
        num=33, topic=3,
        title="Security",
        objective="LO3: Secure the company with budgets, safety rails and approvals.",
        desc="Apply Paperclip's governance: company-wide and per-agent budget caps trigger an 80% warning and a 100% pause; approvals gate risky decisions; the audit trail records everything.",
        build="Budget caps with the 80% warning and 100% pause rails demonstrated, plus an audit review.",
        services="Paperclip, budgets, PostgreSQL audit",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="77uTzIqw8SQ", i=8)),
            ("Set a company and/or per-agent budget cap", ""),
            ("Trigger the 80% warning and 100% pause, then resume", ""),
            ("Audit actions and spend in the embedded PostgreSQL", "psql \"postgresql://postgres@localhost:5432/paperclip\""),
            ("Separate human vs agent actions with actor_type", "SELECT actor_type, COUNT(*) FROM activity_log GROUP BY actor_type;"),
        ],
        test="The 80% warning and 100% pause fire, resume works, and the audit shows actions by actor_type and total spend.",
    ),
    dict(
        num=34, topic=3,
        title="Assign Task",
        objective="LO3: Assign and delegate tasks to run the company end-to-end.",
        desc="Delegate real work: assign tasks to specialists, watch them execute and produce deliverables in the workspace, and review and accept the results to complete the Nimbus Coffee goal.",
        build="Assigned tasks executed by agents, producing real deliverables you review and accept.",
        services="Paperclip, task board, workspace",
        steps=[
            ("Watch the reference video for this lab", _PP.format(v="kAGzMnQ3_Cs", i=9)),
            ("Assign a task to a specialist agent", ""),
            ("Watch the agent execute and write output to the workspace", "ls -R ~/paperclip-workspace/nimbus-coffee"),
            ("Review the deliverable in the in_review state", ""),
            ("Approve to move it to done, or send it back for revision", ""),
        ],
        test="An assigned task is executed by an agent, produces a real file, and is reviewed and accepted to done.",
    ),
]
