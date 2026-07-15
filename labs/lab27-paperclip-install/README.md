# Lab 27 — Install Paperclip on Windows & Mac

## Objective
LO1: Install and self-host Paperclip on Windows and macOS. Watch the Paperclip overview, then self-host **Paperclip** with Docker Compose on your own machine — **Docker Desktop on macOS**, or **Docker Desktop + WSL2 on Windows** — and open the dashboard at `http://localhost:3100`. This is the platform on which you will found **Altera AI Blogs**, a zero-human company you direct as the Board whose mission is to research the AI landscape daily and publish AI-related blogs end to end.

## Prerequisites
- A machine running **macOS** or **Windows 10/11** with admin rights (to install Docker Desktop / enable WSL2).
- **Git** installed (`git --version`).
- Roughly 4 GB free RAM and 5 GB free disk for the container build.
- A free TCP port **3100** on your machine (Paperclip's dashboard).

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Explain Paperclip (overview)](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

## Steps

### 1. Watch the Paperclip overview (Explain Paperclip)
Get the big picture first — what a "company of AI agents" is, and how the Board (you), the CEO and the hired agents fit together:

[https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

### 2. Watch the setup reference video for this lab
The setup walkthrough from the Paperclip playlist mirrors exactly what you build below:

[https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2](https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2)

### 3. Install Docker Desktop — macOS: download from docker.com; Windows: enable WSL2 first, then install Docker Desktop with the WSL2 backend
- **macOS** — download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/), drag it into Applications, launch it and wait for the whale icon to settle.
- **Windows** — enable **WSL2** first (open PowerShell **as Administrator**), then install Docker Desktop and select the **WSL2 backend** during setup:

```bash
wsl --install
```

Reboot if prompted, then confirm Docker is alive on either platform with `docker --version` and `docker compose version`.

### 4. Clone the Paperclip repository
```bash
git clone https://github.com/paperclipai/paperclip.git
```

Then `cd paperclip` so the compose file in the next step resolves.

### 5. Start Paperclip with the quickstart compose file (same command in the macOS Terminal or the Windows WSL2/PowerShell shell)
```bash
docker compose -f docker-compose.quickstart.yml up --build
```

The first build pulls images and compiles the dashboard — give it a few minutes. Leave this terminal running; it is your Paperclip server.

### 6. Open the dashboard in your browser at http://localhost:3100 and create your Board account
Browse to [http://localhost:3100](http://localhost:3100). The first-run screen asks you to create your **Board account** — this identity is the human owner every agent ultimately answers to. Sign in and land on the empty dashboard.

## Verification / Expected Output
- Docker shows the Paperclip containers running (`docker ps` lists them, and Docker Desktop shows them green).
- The dashboard loads at `http://localhost:3100` on your platform (macOS or Windows).
- You are signed in with your Board account and can see the (still empty) Paperclip dashboard.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `wsl --install` fails or hangs (Windows) | Run PowerShell **as Administrator**, ensure virtualization is enabled in BIOS/UEFI, then reboot and retry. |
| `docker: command not found` | Docker Desktop isn't installed or isn't running — launch it and wait for the engine to report "running". |
| `docker compose` unknown flag / not found | You have legacy Compose v1 — upgrade Docker Desktop; the quickstart needs Compose v2 (`docker compose`, no hyphen). |
| Build fails or containers exit immediately | Check free disk/RAM, then rerun `docker compose -f docker-compose.quickstart.yml up --build` and read the first error in the log. |
| Port 3100 already in use | Stop whatever holds it (`lsof -i :3100` / `netstat -ano`) or map another host port in the compose file. |
| Dashboard never loads at localhost:3100 | Wait for the build to finish (watch the compose log), then hard-refresh; on Windows browse from Windows, not from inside WSL2. |

## Exercise / Challenge
Stop the stack with `Ctrl+C`, then restart it **detached** (`docker compose -f docker-compose.quickstart.yml up -d`) and confirm the dashboard still loads. Then write down, in two sentences, what stays (your Board account, company data — persisted in Docker volumes) and what disappears (the log output) when you restart — you will rely on this in every later Paperclip lab.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
