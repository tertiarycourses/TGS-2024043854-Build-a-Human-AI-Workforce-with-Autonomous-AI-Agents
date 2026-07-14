# Lab 14 — Webhook

## Objective
LO3: Integrate the agent with external systems via webhooks. You will wire **Athena** to the outside world: create a webhook endpoint on the dashboard, trigger the agent with a test `curl` payload, watch it act, and then lock the endpoint down with a secret so only authorized callers can trigger it.

## Prerequisites
- **Lab 1–13 complete** — Hermes running with the local gateway serving (Lab 2).
- A way to send a test HTTP request (`curl`, Postman, or a webhook-testing service).

## Estimated Time
35–45 minutes

## 📺 Reference Video
[Webhook](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

## Steps

### 1. Watch the reference video
Watch how a webhook endpoint is created for the agent and how an incoming payload triggers it. Note where the Webhooks page sits in the dashboard, what the generated endpoint URL looks like, and how the payload is mapped to an agent action — those are the three things you reproduce below.

[https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

### 2. Confirm the local gateway is serving
Webhooks ride on the local gateway — if it isn't up, nothing can receive a request. Check its status and note the host/port it reports (typically `localhost` plus a port); that host/port is the base of your webhook URL.

```bash
hermes gateway status
```

If it isn't healthy, restart Hermes/the gateway before continuing.

### 3. Create / enable a webhook endpoint on the dashboard
Open the dashboard and click **Webhooks** (`/webhooks`) in the sidebar. Click **New webhook** (or the enable toggle), give it a recognizable name like `briefing-trigger`, and save. The dashboard generates a unique endpoint URL for it.

> The exact page layout and creation flow are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 4. Copy the endpoint URL and map it to an agent action
Use the copy button next to the new webhook to copy its full URL, and paste it somewhere handy. Then set what the webhook *does*: map incoming payloads to an agent action — for this lab, have it run a short briefing (e.g. instruction: *"When this webhook fires, read the payload's `message` field and act on it"*). Without a mapping, a payload is accepted but nothing happens.

### 5. Send a test payload with curl
From a terminal, simulate an external system by POSTing a JSON payload to the endpoint. Replace `<endpoint-url>` with the URL you copied in step 4:

```bash
curl -X POST <endpoint-url> \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"Trigger Athena briefing"}'
```

You should get a **2xx** response back, which means the gateway accepted the payload. A connection error means the gateway isn't serving (step 2); a 404 means the URL is wrong — re-copy it.

### 6. Watch the agent react
Switch to the chat/session view (or the logs) and confirm the payload actually triggered Athena: the mapped action runs and its output appears — e.g. a briefing message referencing "Trigger Athena briefing" from your payload. Also check the webhook's row on the /webhooks page; most builds show a delivery/last-triggered indicator. Accepted-but-no-action means the mapping in step 4 isn't wired — fix it and re-send.

### 7. Secure the endpoint, then re-send with the secret
An open webhook lets anyone on the network drive your agent, so lock it down. On the webhook's settings, add a **shared secret/token** (and an IP allowlist if your build offers one), save, and re-send the test **including** the secret header — it should still return 2xx and trigger the agent:

```bash
curl -X POST <endpoint-url> \
  -H "Authorization: Bearer <secret>" \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"Trigger Athena briefing"}'
```

> Whether the secret goes in an `Authorization` header, a custom header, or a signature is version-specific — verify in the video / docs link above.

### 8. Confirm unauthorized calls are rejected
Re-run the **step 5** curl (the one *without* the secret header). It must now be rejected with **401/403**, and Athena must not act. If it still returns 2xx, the secret isn't enforced — re-check the webhook's security settings and save again. You now have a working, secured inbound integration.

## Verification / Expected Output
- A webhook exists on the dashboard **/webhooks** page with a copyable endpoint URL.
- A **test payload triggers the agent** and produces the mapped action's output (2xx response + visible agent activity).
- The endpoint is **secured** — the call with the secret succeeds, the call without it is rejected with 401/403.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `curl` returns connection refused | The local gateway isn't serving — check `hermes gateway status`; use the correct host/port from its output. |
| 404 on the endpoint | Wrong URL — re-copy it from the webhook's row on the /webhooks page. |
| 2xx response but agent doesn't act | The webhook isn't mapped to an action — re-check the mapping (step 4) and restart Hermes. |
| Endpoint reachable from anywhere | Add a secret/token and/or IP allowlist so only authorized callers trigger the agent. |
| 401/403 on your own test | You added a secret — include the matching `Authorization` header/token in the `curl` request. |
| Unsure of the webhook config schema | Webhook config is version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Chain a real trigger: point a free webhook-testing/automation service (or a GitHub webhook) at Athena's endpoint so that an external event — e.g. a new calendar invite or a form submission — makes Athena send you a formatted summary. Then rotate the webhook secret and confirm the old secret no longer works, demonstrating end-to-end secured integration.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
