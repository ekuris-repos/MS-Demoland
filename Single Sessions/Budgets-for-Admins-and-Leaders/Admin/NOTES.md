# Budgets for Admins and Leaders

## Session profile

- Scheduled time: 12:30 PM to 2:00 PM PT
- Presenters: Erik in person, Guna remote
- Audience: budget owners, enterprise and organization administrators, finance partners, and account stakeholders
- Format: 50-slide core with expandable live demonstrations
- Labs: none
- Catalog listing: none

The deck is paced for the listed 90-minute session. If more time is available,
expand the two demonstrations and discussion prompts. Do not add more lecture.

## Presenter split

- Erik opens the session, covers slides 1 through 18, and facilitates room questions.
- Guna covers slides 19 through 31 and explains the budget-control sequence.
- Erik resumes after the break for slides 33 through 42.
- Guna drives Live Demo 2 remotely while Erik narrates and repeats room questions.
- Erik closes slides 44 through 50. Guna handles detailed product questions.

Confirm screen sharing, audio, GitHub access, and presenter handoffs before the
session. Keep one presenter signed into the demo enterprise and the other ready
with the fallback materials.

## Timing

| Clock | Slides | Segment | Target |
|---|---:|---|---:|
| 12:30 | 1 to 5 | Context and outcomes | 8 min |
| 12:38 | 6 to 16 | Billing fundamentals | 12 min |
| 12:50 | 17 to 18 | Live Demo 1 and debrief | 8 min |
| 12:58 | 19 to 31 | Budget layers and governance | 20 min |
| 1:18 | 32 | Break | 5 min |
| 1:23 | 33 to 42 | Reporting and automation | 15 min |
| 1:38 | 43 to 44 | Live Demo 2 and debrief | 10 min |
| 1:48 | 45 to 50 | Operating model and close | 12 min |

For a longer delivery, add up to 15 minutes to each demo. Use the extra time to
compare audience scenarios, filters, and budget configurations.

## Live Demo 1: Trace a task to AI credits

### Goal

Show why model choice, context size, and task length affect token composition
and AI credit consumption. Do not promise an exact price before the task runs.

### Setup

1. Use an account with current Copilot usage-based billing terminology.
2. Prepare one focused task against a selected function or small file.
3. Prepare one legitimate multi-file agent task with a clear outcome.
4. Open the AI usage view in a separate tab for the debrief.
5. Use synthetic or approved code only. Do not expose customer repositories.

### Demo flow

1. State the outcome required for each task.
2. Show the selected model and visible context.
3. Run the focused task and note its limited scope.
4. Run or replay the agentic task and identify additional context and steps.
5. Connect the difference to input, output, cache, model, and credit fields.
6. Ask whether the added capability produced proportionate value.

### Fallback

If usage data has not refreshed or account access fails, use slides 9 through
18 as the demonstration. Walk the interaction-to-invoice flow and compare the
two scenarios without claiming a live credit total.

## Live Demo 2: Current billing and AI reporting

### Goal

Move from the broad billing overview to a management-ready explanation of AI
usage. Show the current split among Billing overview, Metered usage, and AI
usage.

### Setup

1. Use an enterprise owner or billing manager account for user-level filtering.
2. Select a period with representative, non-sensitive usage.
3. Confirm that the Billing, Metered usage, AI usage, and Budgets and alerts
   pages are available.
4. Prepare a previously downloaded, sanitized AI usage report as fallback.

### Demo flow

1. Start in Billing overview and identify product-level summaries.
2. Open Metered usage and set a time frame, filter, and grouping.
3. Compare quantity, gross amount, discount amount, and net amount.
4. Open AI usage and inspect pool consumption, paid usage, models, and users.
5. Explain that organization owners need a report for user-level detail.
6. Show chart download and the Get usage report flow.
7. Open Budgets and alerts to connect evidence back to a control decision.

### Fallback

Use the sanitized AI usage CSV and slides 34 through 44. If the interface labels
have changed, state the observed label and avoid forcing the live UI to match
the deck. Record the difference for a post-session content update.

## Delivery cautions

- As of August 12, 2026, promotional included credits for existing Copilot
  Business and Enterprise customers end September 1, 2026.
- Paid AI credit usage is enabled by default for organizations and enterprises.
- User-level budgets always hard stop and apply during included and paid phases.
- Enterprise, organization, and cost-center budgets generally cap paid usage
  after the shared pool is exhausted.
- A budget without the stop-usage option enabled can continue accruing charges.
- Do not present low consumption as success without adoption and outcome data.
- Do not use individual usage data for employee performance evaluation.

## Official sources checked August 12, 2026

- [Usage-based billing for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)
- [Budgets for usage-based billing](https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing)
- [Budgets and alerts](https://docs.github.com/en/billing/concepts/budgets-and-alerts)
- [Cost centers](https://docs.github.com/en/billing/concepts/cost-centers)
- [Setting up budgets](https://docs.github.com/en/billing/how-tos/set-up-budgets)
- [Viewing metered products and licenses](https://docs.github.com/en/billing/how-tos/products/view-product-use)
- [Billing reports reference](https://docs.github.com/en/billing/reference/billing-reports)
- [Automating usage reporting](https://docs.github.com/en/billing/tutorials/automate-usage-reporting)
- [Models and pricing for GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)