# Lab 2 — Deployment — Local Install & Hermes Desktop App

## Objective
LO1: Deploy Hermes locally and run it through the Hermes Desktop app. You will run Hermes as a persistent local deployment (the preferred setup) and also install the Hermes Desktop app for a GUI experience, confirming both talk to the **same Athena agent** and that the local gateway is serving.

## Prerequisites
- **Lab 1 complete** — Hermes installed, `hermes doctor` green, and you've signed in to the Nous Portal.
- The same Nous Portal account you used in Lab 1.
- Permission to install a desktop application on your machine.

## Estimated Time
30–40 minutes

## 📺 Reference Video
Primary walkthrough:
[Deployment — Local Install & Hermes Desktop App](https://www.youtube.com/watch?v=dcXmUUZvDLE&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=3)

Additional walkthrough (also refer):
[Hermes Desktop / deployment — supplementary](https://www.youtube.com/watch?v=3ObcurqJJA0&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=17)

## Steps

### 1. Watch the reference videos
Watch both videos above. The primary shows the local deployment; the additional walkthrough covers the Desktop app in more depth. Note any UI screens that differ from the steps below.

### 2. Confirm the local install runs (preferred deployment)
Verify the CLI runtime you installed in Lab 1 is present and check its version. The local install is the **preferred deployment** — it keeps the agent runtime on your machine:

```bash
hermes --version
```

You should see a version string (e.g. `hermes x.y.z`). Note it — you'll compare it after updating in step 6.

### 3. Download and install the Hermes Desktop app
Download the Desktop app for your OS from the official site and install it like any normal application:

```bash
# from https://hermes-agent.nousresearch.com/ (GUI)
```

Open the site in a browser, choose the Desktop download for your platform (macOS `.dmg`, Windows installer, or Linux package), and run through the installer.

### 4. Open the Desktop app and sign in
Launch the Hermes Desktop app and sign in with **the same Nous Portal account** you used for the CLI in Lab 1. Signing in with the same account is what makes the Desktop app and the CLI drive the same agent.

> This step is UI-only — there is no terminal command. In the app, choose *Sign in with Nous Portal* and complete the browser/authentication prompt.

### 5. Verify the local gateway is serving
The gateway is the local service that both the CLI and Desktop app connect to. Confirm it is up and healthy:

```bash
hermes gateway status
```
Or just ask the agent: "Check that your local gateway is up and serving"


You should see a status of **running / healthy** along with the address/port it is serving on. If it reports stopped, start it as directed by the command's hint (and re-check).

### 6. Keep the runtime up to date
Update Hermes to the latest release so the CLI and Desktop app stay compatible:

```bash
hermes update
```

After it finishes, run `hermes --version` again and confirm the version advanced (or is already latest).

## Verification / Expected Output
- Both the **local CLI** (`hermes --tui`) and the **Desktop app** drive the same Athena agent — a message or memory created in one appears to the other.
- `hermes gateway status` reports **healthy** and shows the serving address.
- `hermes --version` shows a valid version, and `hermes update` completes without error.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Desktop app and CLI seem to be different agents | You signed in with a different account — sign out of the Desktop app and sign back in with the **same** Nous Portal account as the CLI. |
| `hermes gateway status` reports stopped | Start the gateway (follow the command's hint / restart Hermes), then re-run the status command. |
| Desktop app can't connect to local gateway | Ensure the gateway is running and no firewall is blocking the local port shown by `hermes gateway status`. |
| `hermes update` fails | Check connectivity; if a process is locking the binary, close all Hermes windows/TUI sessions and retry. |
| Version unchanged after update | You were already on latest, or PATH points at an old binary — confirm with `which hermes`. |

## Exercise / Challenge
Prove the two front-ends share state: in the **CLI TUI** tell Athena a fact ("My office is in Singapore"), then open the **Desktop app** and ask "Where is my office?". Confirm the Desktop app answers correctly — this demonstrates a single local deployment serving multiple clients.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
