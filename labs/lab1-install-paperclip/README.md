# Lab 1 — Install Paperclip with Docker Compose & Create Your Company

**Goal:** Self-host Paperclip on your own laptop using Docker Compose, then create your
first **company** — a single goal plus a monthly budget. By the end you will have the
Paperclip dashboard open at `http://localhost:3100` and an empty company waiting for its
CEO.

**Time:** ~25 min · **Maps to:** Crash-course Scenario 1

---

## 1. Prerequisites

- **Docker Desktop** installed and **running** — <https://www.docker.com/products/docker-desktop/>
- **Git** installed — check with `git --version`.
- A terminal opened in this folder (`labs/lab1-install-paperclip/`).

> Paperclip runs **entirely on your laptop**. Company state lives in an **embedded
> PostgreSQL** database; no cloud account is required to complete these labs.

---

## 2. Get the Paperclip source

Clone the repository next to this lab folder (so the `../paperclip` build path in the
included `docker-compose.yml` resolves):

```bash
# from labs/lab1-install-paperclip/
git clone https://github.com/paperclipai/paperclip.git ../paperclip
```

> If cloning elsewhere, edit `context:` in [`docker-compose.yml`](docker-compose.yml) to
> point at your clone.

---

## 3. Start Paperclip (the official quickstart)

The simplest, blessed path is to run Paperclip's own quickstart compose file from the repo
root:

```bash
cd ../paperclip
docker compose -f docker/docker-compose.quickstart.yml up --build
```

Then open **<http://localhost:3100>**.

- `--build` builds the image the first time (subsequent starts are fast).
- Leave this terminal running, or add `-d` to run detached in the background.

### Change the port or data location

`PAPERCLIP_PORT` and `PAPERCLIP_DATA_DIR` override the defaults:

```bash
PAPERCLIP_PORT=3200 PAPERCLIP_DATA_DIR=../data/pc \
  docker compose -f docker/docker-compose.quickstart.yml up --build
```

> ⚠️ `PAPERCLIP_DATA_DIR` is resolved **relative to the compose file in `docker/`**, so
> `../data/pc` maps to `data/pc` at the repo root.

### (Alternative) Run from this lab folder

This lab also ships a documented [`docker-compose.yml`](docker-compose.yml) you can run
straight from `labs/lab1-install-paperclip/`:

```bash
docker compose up --build
```

| Task | Command |
|------|---------|
| View logs | `docker compose logs -f` |
| Stop (keep data) | `docker compose down` |
| Start again | `docker compose up -d` |
| **Reset to fresh install** | `docker compose down` then delete the data folder (e.g. `rm -rf data/docker-paperclip`) |

### What the data mount holds

A **single bind mount** persists everything that must survive a restart:

- Embedded **PostgreSQL** data (all company state)
- Uploaded assets and local secrets
- The **agent workspace** (files agents create — used in Lab 4)

Delete that folder and you get a clean slate.

---

## 4. Create your first company

1. In the dashboard, choose **Create company** (first-run setup).
2. Give it a clear, single **goal** — this anchors *all* future agent work. Example:

   > *"Launch a simple one-page marketing website for a fictional coffee brand, ‘Nimbus
   > Coffee’, and draft its first three social posts."*

3. Set a **monthly budget** (a spending ceiling). Start small, e.g. **$20**. You will wire
   up the safety rails around this number in Lab 5.
4. Confirm. Paperclip records the creation in its **activity log** (`activity_log` table),
   tagged with `actor_type = user` because *you* — the Board — made this decision.

> **Why a single goal?** Paperclip is opinionated: one clear objective keeps the CEO agent
> and its team aligned. You can always revise it later.

---

## 5. Quick checklist

- [ ] Docker Desktop is running.
- [ ] Paperclip built and started (`docker compose ... up --build`).
- [ ] Dashboard loads at **http://localhost:3100**.
- [ ] A **company** exists with a one-line **goal** and a **monthly budget**.
- [ ] The company creation appears in the activity log.

✅ **Next:** [Lab 2 — Hire Your CEO Agent](../lab2-hire-ceo/README.md)

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
