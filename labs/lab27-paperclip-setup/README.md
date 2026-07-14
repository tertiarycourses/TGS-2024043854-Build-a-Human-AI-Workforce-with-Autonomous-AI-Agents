# Lab 27 — Setup Paperclip

## Objective
Self-host **Paperclip** with Docker Compose and **found your company** — **Nimbus Coffee, Inc.**, a zero-human company you govern as the Board. By the end you will have Paperclip running at `http://localhost:3100` and a company created with a single goal and a monthly budget, ready for you to staff with AI agents in the labs that follow.

## Prerequisites
- **Docker** and **Docker Compose v2** installed and running (`docker --version`, `docker compose version`).
- **Git** installed (`git --version`).
- Roughly 4 GB free RAM and 5 GB free disk for the container build.
- A free TCP port **3100** on your machine (Paperclip's dashboard).
- Internet access to clone the repo and pull base images.

## Estimated Time
30–40 minutes

## 📺 Reference Video
- Overview — [Explain Paperclip](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)
- Setup walkthrough — [Setup Paperclip](https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2)

## Steps

1. **Watch the Paperclip overview (Explain Paperclip).** This introduces the mental model: Paperclip runs an entire *company* of AI agents (a CEO who hires specialists), and you sit above them as the Board, approving hires and spend. Keep that framing in mind — every later lab maps to a real corporate function.

   [https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

2. **Watch the setup reference video for this lab.** This is the exact self-hosting walkthrough for the steps below — follow along so the on-screen dashboard matches yours.

   [https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2](https://www.youtube.com/watch?v=f2eian-bR_U&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=2)

3. **Clone the Paperclip repository.** This pulls the source and the Docker Compose files you need to run it locally:

   ```bash
   git clone https://github.com/paperclipai/paperclip.git
   cd paperclip
   ```

4. **Start Paperclip with the quickstart compose file.** This builds the image and brings up the full stack (the app plus its embedded PostgreSQL):

   ```bash
   docker compose -f docker-compose.quickstart.yml up --build
   ```

   The first build takes several minutes. Leave this terminal running — it streams the container logs. Wait until you see the app report that it is listening on port 3100.

5. **Open the dashboard.** In your browser, go to:

   ```bash
   # http://localhost:3100
   ```

   You should see the Paperclip dashboard load. This is the control surface for your whole AI company.

6. **Create the company with a single goal and a monthly budget.** In the dashboard, start a new company. Name it **Nimbus Coffee, Inc.**, give it **one clear goal** (e.g. "Launch a direct-to-consumer specialty coffee brand and make the first sale"), and set a **monthly budget cap** (your spend ceiling). Save. This company is the entity the CEO and specialist agents will work inside for every remaining Paperclip lab.

   > The exact wording of the "Create company" / goal / budget fields is version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

## Verification / Expected Output
- The dashboard **loads at `http://localhost:3100`**.
- A company named **Nimbus Coffee, Inc.** exists, showing its **goal** and its **monthly budget**.
- The `docker compose ... up` terminal shows the app and database containers healthy with no crash-looping.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `http://localhost:3100` refuses to connect | The stack is still building or crashed. Watch the compose logs; wait for the "listening on 3100" line, or re-run `docker compose -f docker-compose.quickstart.yml up --build`. |
| Port 3100 already in use | Another process owns the port. Stop it, or remap the port in `docker-compose.quickstart.yml`, then restart. |
| Build fails pulling base images | Check internet/proxy and that Docker is logged in if needed; re-run the `up --build` command. |
| Container exits immediately | Insufficient RAM or a bad build. Free memory (≥4 GB), run `docker compose ... down`, then `up --build` again. |
| "Create company" form fields differ from the video | The UI wording is version-specific — verify field names in the video / docs (<https://docs.paperclip.ing>). |

## Exercise / Challenge
Write your Nimbus Coffee company **charter** in three lines: the single goal, the monthly budget, and one measurable definition of success (e.g. "first paid order shipped within budget"). Enter it as the company goal, then take a screenshot of the dashboard showing the company, its goal, and its budget — this is the baseline you will hold every later lab accountable to.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
