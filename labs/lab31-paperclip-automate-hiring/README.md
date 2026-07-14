# Lab 31 — Automate AI Hiring

## Objective
Let **Nimbus Coffee, Inc.** staff itself: **hire the CEO agent**, then let the CEO propose **specialist hires** — each passing a **human approval gate** where you, the Board, approve or reject. By the end the company will have an active CEO and one or more approved specialists, with every hire logged as a human decision.

## Prerequisites
- **Lab 30 complete**: you can see and track tasks on the company task board.
- The Codex adapter available (Lab 28) — agents need a brain to be worth hiring.
- Nimbus Coffee configured with a budget and workspace (Lab 29).

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Automate AI Hiring](https://www.youtube.com/watch?v=tgqcHHxiwfk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=6)

## Steps

1. **Watch the reference video for this lab.** It shows the hiring flow: hiring the CEO, the CEO proposing specialists, and the approval gate you control.

   [https://www.youtube.com/watch?v=tgqcHHxiwfk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=6](https://www.youtube.com/watch?v=tgqcHHxiwfk&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=6)

2. **Hire the CEO agent from the company page.** On the **Nimbus Coffee, Inc.** page, choose to **hire the CEO**. The CEO is the top agent that reads the company goal and works out what roles the company needs to achieve it.

3. **Approve the CEO hire (you are the Board).** The hire pauses at an **approval gate**. Review it and **approve** — as the Board, nothing joins the company without your sign-off. This is the core governance pattern: agents propose, humans approve.

4. **Let the CEO propose specialist hires.** Once active, the CEO analyses the goal and **proposes specialists** it needs (for a coffee brand, perhaps a Marketer, an Engineer for the storefront, and an Operations agent). Each proposal explains the role and why it helps reach the goal.

5. **Review and approve each specialist at the approval gate.** For every proposed hire, review the role and **approve or reject** it at the gate. Approve the ones that genuinely serve the Nimbus Coffee goal; reject any that don't. Each approval is recorded as a human decision — an `actor_type=user` entry in the audit trail you'll inspect in Lab 33.

## Verification / Expected Output
- The **CEO and approved specialists are active** in the company.
- Each hire that you approved is **logged as an `actor_type=user` decision** (a human action, distinct from agent actions).
- Any hire you rejected does not appear as an active agent.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| No "hire CEO" option | Confirm the company exists and the Codex adapter is available (Lab 28); reload the company page. |
| CEO proposes no specialists | Give the company a clearer, more specific goal (Lab 27) so the CEO has something to staff for. |
| Approval gate never appears | Hires may auto-approve if a setting is off — verify the approvals/governance setting in the video / docs (<https://docs.paperclip.ing>). |
| Hire fails after approval | The budget may be exhausted or the adapter unauthorized. Check budget (Lab 29) and Codex status (Lab 28). |
| Can't tell human vs agent actions | You'll confirm this via the `actor_type` audit query in Lab 33. |

## Exercise / Challenge
After approving the CEO, deliberately **reject** the first specialist the CEO proposes and note how the CEO responds (does it propose an alternative or re-justify?). Then approve the specialists you actually want. Write two sentences on how the approval gate keeps you in control even while the company staffs itself — the essence of governing a zero-human company.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
