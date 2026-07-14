# Lab 14 — Webhook

## Objective
LO3: Integrate the agent with external systems via webhooks. You will wire **Athena** to the outside world with webhooks: trigger the agent from an incoming webhook payload and/or have it call an outgoing webhook, then secure the endpoint.

## Prerequisites
- **Lab 1–13 complete** — Hermes running with the local gateway serving (Lab 2).
- A way to send a test HTTP request (`curl`, Postman, or a webhook-testing service).

## Estimated Time
35–45 minutes

## 📺 Reference Video
[Webhook](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

## Steps

### 1. Watch the reference video
See how a webhook endpoint is configured for the agent and how an incoming payload triggers it:

[https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31](https://www.youtube.com/watch?v=WNYe5mD4fY8&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=31)

### 2. Configure a webhook trigger/endpoint for the agent
Set up a webhook endpoint that Athena listens on.

> Configure the webhook in the Hermes automation/integration settings (Desktop app or the webhook section of `~/.hermes/config.yaml`), mapping an incoming URL to an agent action. The exact config keys and the endpoint URL are **version-specific** — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/). Note the endpoint URL served by your local gateway (from `hermes gateway status`).

### 3. Send a test payload to the webhook
Send a test HTTP POST to the endpoint to simulate an external event:

```bash
curl -X POST <your-webhook-endpoint-url> \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"Trigger Athena briefing"}'
```

Replace `<your-webhook-endpoint-url>` with the endpoint from step 2. You should get a 2xx response indicating the payload was accepted.

### 4. Confirm the agent receives the event and responds/acts
Check that the incoming payload triggered Athena — e.g. it ran the mapped action (a briefing, a reply, a message to a channel). Confirm the action's output where you expect it (chat, channel, or logs).

### 5. Secure the webhook (secret/token, allowlist)
Lock the endpoint down so only authorized callers can trigger the agent:

> Add a shared secret/token that callers must include (e.g. an `Authorization` header or a signing secret), and/or an IP allowlist. Re-send the test with and without the secret to confirm unauthorized calls are rejected. Verify the exact security options in the video / docs link above.

## Verification / Expected Output
- A **test payload to the webhook triggers the agent** and produces the expected action.
- The endpoint is **secured** — calls without the correct secret/token are rejected.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `curl` returns connection refused | The local gateway isn't serving — check `hermes gateway status`; use the correct host/port. |
| Endpoint responds but agent doesn't act | The webhook isn't mapped to an action — re-check the trigger config and restart Hermes. |
| Endpoint reachable from anywhere | Add a secret/token and/or IP allowlist so only authorized callers trigger the agent. |
| 401/403 on your own test | You added a secret — include the matching `Authorization` header/token in the `curl` request. |
| Unsure of the webhook config schema | Webhook config is version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Chain a real trigger: point a free webhook-testing/automation service (or a GitHub webhook) at Athena's endpoint so that an external event — e.g. a new calendar invite or a form submission — makes Athena send you a formatted summary. Then rotate the webhook secret and confirm the old secret no longer works, demonstrating end-to-end secured integration.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
