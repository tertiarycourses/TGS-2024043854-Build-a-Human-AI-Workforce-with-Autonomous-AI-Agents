# Learner Guide — Building a Human-AI Workforce with Paperclip

**Course:** Build a Human-AI Workforce with Autonomous AI Agents (TGS-2024043854)
**Module:** Install Paperclip and run a company of AI agents (Labs 1–5)

This guide walks you, click-by-click and command-by-command, from an empty laptop to a
running **AI company** that you govern. You will:

1. Install **Paperclip** locally with **Docker Compose**.
2. Create a company with a goal and a budget.
3. Hire a **CEO agent**, approve its **strategy**, and staff a **team** of specialists.
4. Let the team produce **real files**.
5. Govern everything with **budgets, safety rails and a full audit trail**.

> **What is Paperclip?** "An operating system for running a company of AI agents." You are
> **the Board**. A **CEO agent** reports to you and proposes strategy; **specialist agents**
> report to the CEO and do the work. Every important decision — hiring, strategy, budget —
> passes through a **human approval gate**. Work moves across a board:
> `todo → in_progress → in_review → done`.

Reference crash course: <https://agentfactory.panaversity.org/docs/workforce-with-paperclip-crash-course>
Official docs: <https://docs.paperclip.ing>

---

## Table of Contents

- [Part 0 — Prepare your machine](#part-0--prepare-your-machine)
- [Part 1 — Install Paperclip with Docker Compose (Lab 1a)](#part-1--install-paperclip-with-docker-compose-lab-1a)
- [Lab 1b — Create your company](#lab-1b--create-your-company)
- [Lab 2 — Hire your CEO agent](#lab-2--hire-your-ceo-agent)
- [Lab 3 — Approve the company strategy](#lab-3--approve-the-company-strategy)
- [Lab 4 — Build the team & execute real work](#lab-4--build-the-team--execute-real-work)
- [Lab 5 — Govern: budgets, safety rails & audit](#lab-5--govern-budgets-safety-rails--audit)
- [Troubleshooting](#troubleshooting)
- [Command cheat-sheet](#command-cheat-sheet)

---

## Part 0 — Prepare your machine

Complete all four checks **before** the labs. Budget ~15 minutes.

### 0.1 Install Docker Desktop

Paperclip runs in a container, so you need Docker.

1. Download **Docker Desktop**: <https://www.docker.com/products/docker-desktop/>
2. Install and **launch** it. Wait until the whale icon says *Docker Desktop is running*.
3. Verify in a terminal:

   ```bash
   docker --version
   docker compose version
   ```

   You should see version numbers (Docker 20+ and Compose v2). If `docker compose` is not
   found, update Docker Desktop — older installs used `docker-compose` (with a hyphen).

### 0.2 Install Git

Used to download Paperclip's source code.

```bash
git --version
```

If missing: macOS → `xcode-select --install`; Windows → <https://git-scm.com/download/win>;
Linux → `sudo apt install git`.

### 0.3 Install an AI agent CLI (the agent's "brain")

Paperclip drives real AI models through a **local adapter** — a coding CLI you already have
logged in. Install **at least one** of these and sign in:

| CLI | Install | Sign in |
|-----|---------|---------|
| **Claude Code** (recommended) | <https://claude.com/claude-code> | run `claude` and follow login |
| OpenCode | <https://opencode.ai> | run `opencode` |
| Codex CLI | <https://developers.openai.com/codex/cli> | run `codex` |
| Gemini CLI | <https://github.com/google-gemini/gemini-cli> | run `gemini` |

Verify your choice runs, e.g.:

```bash
claude --version
```

> **Good news:** agents reuse this existing CLI login, so **you do not need extra API keys**
> to complete the labs. (Cloud keys like `ANTHROPIC_API_KEY` are optional — see 1.4.)

### 0.4 Pre-flight checklist

- [ ] `docker --version` and `docker compose version` both work, Docker Desktop is running.
- [ ] `git --version` works.
- [ ] At least one agent CLI installed and **logged in** (e.g. `claude --version`).
- [ ] ~2 GB free disk and a stable internet connection.

---

## Part 1 — Install Paperclip with Docker Compose (Lab 1a)

**Goal:** Get the Paperclip dashboard running at `http://localhost:3100`.
**Time:** ~15 min.

### 1.1 Download the Paperclip source

Pick a working folder and clone the repo:

```bash
cd ~/projects            # or anywhere you like
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
```

You are now inside the `paperclip/` repo, which contains the Docker Compose file.

### 1.2 Start Paperclip with Docker Compose

Run the **quickstart** compose file. `--build` builds the image on first run:

```bash
docker compose -f docker-compose.quickstart.yml up --build
```

> **Can't find the file?** Some versions place it in a `docker/` sub-folder. Locate it with
> `find . -name "docker-compose.quickstart.yml"` and use that path, e.g.
> `docker compose -f docker/docker-compose.quickstart.yml up --build`.

First run downloads base images and builds — this can take a few minutes. Leave the terminal
open. When you see log lines indicating the server is listening, it's ready.

To run it **in the background** instead, add `-d`:

```bash
docker compose -f docker-compose.quickstart.yml up --build -d
```

### 1.3 Open the dashboard

Open your browser at:

**<http://localhost:3100>**

You should see the Paperclip onboarding screen. If the page doesn't load, wait ~30 seconds
for startup and refresh; then see [Troubleshooting](#troubleshooting).

### 1.4 (Optional) Change port / data folder / add cloud keys

Override the defaults with environment variables **before** the command:

```bash
# run on port 3200 and store data in ./data/pc
PAPERCLIP_PORT=3200 PAPERCLIP_DATA_DIR=./data/pc \
  docker compose -f docker-compose.quickstart.yml up --build
```

- **Default port:** `3100`.
- **Default data directory:** `./data/docker-paperclip` — a single bind mount that holds
  **everything** that must survive a restart: the embedded PostgreSQL database, uploaded
  assets, the secrets key, and the agent workspace. **Delete this folder to reset Paperclip
  to a factory-fresh state.**

To enable **cloud** LLM adapters (optional — local CLIs are enough), supply keys, e.g.
`ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GEMINI_API_KEY` as environment variables.

### 1.5 Everyday container commands

Run these from the `paperclip/` folder:

| Task | Command |
|------|---------|
| View logs (follow) | `docker compose -f docker-compose.quickstart.yml logs -f` |
| Stop (keep data) | `docker compose -f docker-compose.quickstart.yml down` |
| Start again | `docker compose -f docker-compose.quickstart.yml up -d` |
| Open a shell in the container | `docker compose -f docker-compose.quickstart.yml exec paperclip sh` |
| **Reset everything** | `down`, then delete the data folder (`rm -rf data/docker-paperclip`) |

> **Even simpler (no Docker):** Paperclip also offers `npx paperclipai onboard --yes`
> (needs Node.js 20+). This course uses the Docker route because it is self-contained and
> identical on every machine.

### ✅ Lab 1a checklist

- [ ] Repo cloned; you are inside `paperclip/`.
- [ ] `docker compose -f docker-compose.quickstart.yml up --build` ran without errors.
- [ ] Dashboard loads at **http://localhost:3100**.

---

## Lab 1b — Create your company

**Goal:** Define one clear goal and a monthly budget. **Time:** ~10 min.
**Maps to:** Crash-course Scenario 1.

We'll use a running example throughout the labs — a fictional coffee brand, **"Nimbus
Coffee."** Use it, or invent your own goal.

### Steps

1. On the dashboard, click **Create company** (first-run setup).
2. Enter a **single, concrete goal**. A good goal is specific and achievable. Example:

   > *"Launch a simple one-page marketing website for a fictional coffee brand, 'Nimbus
   > Coffee', and draft its first three social media posts."*

3. Set a **monthly budget** — a hard spending ceiling. Start small: **$20**. You'll wire the
   safety rails to this number in Lab 5.
4. Click **Confirm / Create**.

### What just happened

Paperclip wrote a row to its **`activity_log`** table, tagged **`actor_type = user`** —
because *you*, the Board, made this decision. Later you'll query this log yourself.

> **Why only one goal?** Paperclip is deliberately opinionated: a single objective keeps the
> CEO and the whole team pulling in one direction. You can revise it any time.

### ✅ Lab 1b checklist

- [ ] A **company** exists with a one-line **goal**.
- [ ] A **monthly budget** is set.
- [ ] The creation shows in the activity log.

---

## Lab 2 — Hire your CEO agent

**Goal:** Connect your agent adapter and make your first hire — a **CEO** — through an
**approval gate**. **Time:** ~15 min. **Maps to:** Scenario 2.

### 2.1 Confirm your adapter is detected

1. In the dashboard open **Settings → Agents / Adapters** (wording varies by version).
2. Confirm at least one adapter shows **available / detected** (e.g. *Claude Code — detected*).
3. If none show, verify the CLI works and is logged in:

   ```bash
   claude --version     # or opencode / codex / gemini
   ```

   Then restart Paperclip so it re-scans:

   ```bash
   docker compose -f docker-compose.quickstart.yml restart
   ```

> **How adapters work:** Paperclip finds supported CLIs on your machine and maps each to a
> *local adapter*. A **heartbeat** then wakes agents on a schedule to pick up work.

### 2.2 Propose the CEO hire

1. From your company page click **Hire CEO** (or **Add agent → CEO**).
2. Choose the **adapter/model** the CEO will use (e.g. Claude Code).
3. Optionally give a short **mandate**:

   > *"You are the CEO. Deliver the company goal on time and under budget. Propose strategy
   > and delegate to specialists. Escalate anything needing Board approval."*

4. Submit. The hire is now **proposed** — it sits in an **approval gate**, not yet active.

### 2.3 Approve the hire (you are the Board)

1. Review the proposed CEO: adapter, mandate, and any per-agent budget cap.
2. Click **Approve**.
3. The CEO becomes **active**. Paperclip logs the decision as `actor_type = user`.

> **Why a gate?** Hiring, strategy, and budgets are the three decisions Paperclip reserves
> for humans. Everything else agents can do on their own.

### ✅ Lab 2 checklist

- [ ] An **adapter** is detected.
- [ ] A **CEO** was **proposed** (entered the gate) and then **approved**.
- [ ] The CEO is **active** and the hire is in the activity log as a `user` action.

---

## Lab 3 — Approve the company strategy

**Goal:** The CEO drafts a strategy; you review it at the `in_review` gate and move it to
`done`. **Time:** ~15 min. **Maps to:** Scenario 3.

### 3.1 The task board & its four states

Every unit of work flows through:

```
todo  →  in_progress  →  in_review  →  done
```

- **todo** — created, not started.
- **in_progress** — an agent is working it.
- **in_review** — finished; **waiting for a human** to accept.
- **done** — you approved it.

A **strategy** is simply the first, most important task — and it *stops* at `in_review`
until **you** advance it.

### 3.2 Ask the CEO to draft a strategy

1. Open the **CEO agent**.
2. Click **Draft strategy**, or message the CEO:

   > *"Draft a strategy to achieve our company goal within budget. Break it into phases and
   > list the specialist roles you'll need to hire."*

3. The task moves to **in_progress**. On the next **heartbeat**, the CEO's adapter runs,
   produces the strategy, and the task moves itself to **in_review**.

> **Nothing happening?** Wait for the heartbeat, or use **Run now / Nudge** if available.
> Watch progress with
> `docker compose -f docker-compose.quickstart.yml logs -f`.

### 3.3 Review the strategy (Board decision)

1. Open the strategy task in **in_review** and read it. Ask:
   - Does it serve the **goal** from Lab 1?
   - Are the proposed hires reasonable for the **budget**?
2. Choose:
   - **Approve** → moves to **done** (do this to continue).
   - **Request changes / Send back** → returns to the CEO; iterate, then approve.
3. On approval the decision is logged as `actor_type = user`.

> **Governance point:** No hiring or spending proceeds on an *unapproved* strategy. The
> `in_review` gate is where you keep control.

### ✅ Lab 3 checklist

- [ ] Strategy task moved `todo → in_progress → in_review`.
- [ ] You **read** it, then **approved** (or iterated) → state **done**.
- [ ] Approval recorded in the activity log.

---

## Lab 4 — Build the team & execute real work

**Goal:** The CEO hires **specialists** (each gated by your approval), delegates tasks, and
— with a **workspace folder** connected — agents produce **real files**.
**Time:** ~25 min. **Maps to:** Scenarios 4 & 7.

### 4.1 Connect a workspace folder

1. Create an empty output folder:

   ```bash
   mkdir -p ~/paperclip-workspace/nimbus-coffee
   ```

2. In the dashboard, open the company's **Workspace** settings and point it at that folder
   (or the path exposed inside the container — the Lab 1 data mount already persists the
   agent workspace).
3. Everything the team creates — web pages, copy, CSVs — now lands here.

### 4.2 CEO hires specialists (each needs your approval)

1. Open the **CEO agent**. From the approved strategy it proposes **specialist hires** — for
   Nimbus Coffee, perhaps a *Web Developer* agent and a *Copywriter* agent.
2. Each proposed hire enters an **approval gate**, exactly like the CEO hire.
3. **Review and Approve** each specialist. Set a **per-agent budget cap** if prompted.

> Specialists report to the **CEO**, not to you. Your role is approvals and oversight.

### 4.3 Delegate & execute

1. The CEO splits the strategy into tasks and assigns them. New cards appear in **todo**.
2. On each **heartbeat**, assigned agents pick up tasks (`in_progress`), run their adapter,
   and write output into the **workspace folder**.
3. Finished work moves to **in_review** for your acceptance.

Watch it happen:

```bash
docker compose -f docker-compose.quickstart.yml logs -f
```

### 4.4 Verify real files were created

```bash
ls -R ~/paperclip-workspace/nimbus-coffee
```

You should see real artefacts — e.g. `index.html`, `copy.md`, `social-posts.md`. Open them
and confirm they reflect your goal.

### 4.5 Review and accept deliverables

1. Open each task in **in_review** and inspect the linked file(s).
2. Good? **Approve** → **done**. Not yet? **Send back** with a note; the agent revises on the
   next heartbeat.
3. Repeat until the board is clear and the goal is met.

> **You just ran a company:** a goal became a strategy, the strategy became a team, and the
> team produced real deliverables — with a human approval at every decision that mattered.

### ✅ Lab 4 checklist

- [ ] A **workspace folder** is connected.
- [ ] Specialists **proposed** and **approved**.
- [ ] Tasks flowed `todo → in_progress → in_review`.
- [ ] **Real files** appear in the workspace and match the goal.
- [ ] You **reviewed and accepted** (or sent back) deliverables.

---

## Lab 5 — Govern: budgets, safety rails & audit

**Goal:** Put on your CFO hat. Set **budget caps**, trigger the **safety rails** (80%
warning, 100% pause), and **query the audit trail** in the embedded PostgreSQL.
**Time:** ~20 min. **Maps to:** Scenarios 5 & 6.

### 5.1 Budget caps & safety rails

Paperclip enforces limits at two levels:

- **Company-wide monthly cap** — the budget from Lab 1.
- **Per-agent caps** — an optional ceiling per agent.

Two automatic rails protect you:

| Threshold | What happens |
|-----------|--------------|
| **80%** of a cap | **Warning** — you're notified spend is approaching the limit. |
| **100%** of a cap | **Pause** — work stops so nothing runs away. Only *you* can resume. |

**Try it:**

1. Open **Settings → Budget** (company and/or a specific agent).
2. Temporarily set a **low cap** — just above current spend — to force the rails.
3. Nudge the team to do a little more work; watch for the **80% warning**, then the
   **100% pause**.
4. Restore a sensible cap and **resume** to lift the pause.

> **Under the hood:** every spend is written to **`cost_events`**; every action (hires,
> approvals, pauses) to **`activity_log`**. That's what powers both the rails and the audit.

### 5.2 Audit the company like a CFO (query PostgreSQL)

The whole history is queryable. Open a shell in the container and connect to the embedded
PostgreSQL.

```bash
# from the paperclip/ folder
docker compose -f docker-compose.quickstart.yml exec paperclip sh
```

Inside the container, connect with `psql` (the DB files live under `PAPERCLIP_HOME`,
i.e. `/paperclip`). Adjust the db name/user if your version differs — check
<https://docs.paperclip.ing>:

```bash
psql "postgresql://postgres@localhost:5432/paperclip"
```

**Every decision and action, newest first:**

```sql
SELECT created_at, actor_type, action, detail
FROM activity_log
ORDER BY created_at DESC
LIMIT 50;
```

**Separate *your* decisions from the agents' actions** (the `actor_type` field is the key):

```sql
SELECT actor_type, COUNT(*)
FROM activity_log
GROUP BY actor_type;
-- 'user'  = decisions only you could make (hires, approvals, budgets)
-- 'agent' = work agents did on their own
```

**Where did the money go?**

```sql
SELECT created_at, agent, amount, description
FROM cost_events
ORDER BY created_at DESC;

SELECT SUM(amount) AS total_spent FROM cost_events;
```

Exit with `\q`, then `exit` to leave the container.

> **What you're proving:** every dollar and every action is attributable — *who* (human vs.
> agent) did *what*, *when*, and *what it cost*. Full accountability.

### 5.3 Establish a monthly governance review

Set the recurring habit the crash course recommends. Ask the CEO agent (or note for
yourself) to run a monthly audit against a baseline:

> *"Walk through everything hired, configured, scheduled, approved, or paused since the last
> audit. Flag anything I did not explicitly sign off on."*

This catches **drift** without you hovering over the company daily.

### ✅ Lab 5 checklist

- [ ] A **company** and/or **per-agent** cap is set.
- [ ] You triggered the **80% warning** and **100% pause**, then **resumed**.
- [ ] You connected to **PostgreSQL** and read `activity_log`.
- [ ] You used **`actor_type`** to separate human vs. agent actions.
- [ ] You totalled spend from **`cost_events`**.
- [ ] You defined a **monthly audit** prompt.

🎉 **Congratulations** — you installed an AI company, staffed it, and now govern it with
budgets and a full audit trail.

**Where next:** the **Dynamic Workforce** crash course (scheduling recurring agent work) and
the cloud deployment guides at <https://docs.paperclip.ing>.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `docker: command not found` | Docker Desktop isn't installed/running. Install it and wait for the whale icon to say *running*. |
| `docker compose` unknown | Update Docker Desktop (Compose v2 ships with it). Older setups use `docker-compose` with a hyphen. |
| `docker-compose.quickstart.yml` not found | `find . -name "docker-compose.quickstart.yml"` and use that path (may be under `docker/`). |
| Port 3100 already in use | Run with `PAPERCLIP_PORT=3200 docker compose -f docker-compose.quickstart.yml up --build` and open `http://localhost:3200`. |
| Dashboard won't load | Wait ~30 s for startup; check `... logs -f`; confirm the container is `Up` with `docker compose -f docker-compose.quickstart.yml ps`. |
| No adapter detected | Ensure the CLI runs and is logged in (`claude --version`), then `docker compose -f docker-compose.quickstart.yml restart`. |
| Agents don't start work | Wait for the **heartbeat**, or use **Run now / Nudge**. Watch `... logs -f`. |
| Want a clean slate | `docker compose -f docker-compose.quickstart.yml down`, then delete the data folder (`rm -rf data/docker-paperclip`). |
| Build fails / corrupt image | `docker compose -f docker-compose.quickstart.yml build --no-cache` then `up`. |

---

## Command cheat-sheet

```bash
# --- Install (Lab 1) ---
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
docker compose -f docker-compose.quickstart.yml up --build      # open http://localhost:3100

# custom port / data dir
PAPERCLIP_PORT=3200 PAPERCLIP_DATA_DIR=./data/pc \
  docker compose -f docker-compose.quickstart.yml up --build

# --- Day-to-day (run from paperclip/) ---
docker compose -f docker-compose.quickstart.yml up -d           # start (background)
docker compose -f docker-compose.quickstart.yml logs -f         # follow logs
docker compose -f docker-compose.quickstart.yml ps              # status
docker compose -f docker-compose.quickstart.yml restart         # restart (re-scan adapters)
docker compose -f docker-compose.quickstart.yml down            # stop (keep data)
docker compose -f docker-compose.quickstart.yml exec paperclip sh   # shell into container

# --- Reset to factory-fresh ---
docker compose -f docker-compose.quickstart.yml down
rm -rf data/docker-paperclip

# --- Workspace (Lab 4) ---
mkdir -p ~/paperclip-workspace/nimbus-coffee
ls -R ~/paperclip-workspace/nimbus-coffee

# --- Audit (Lab 5, inside the container shell) ---
psql "postgresql://postgres@localhost:5432/paperclip"
#   SELECT actor_type, COUNT(*) FROM activity_log GROUP BY actor_type;
#   SELECT SUM(amount) FROM cost_events;
```

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
