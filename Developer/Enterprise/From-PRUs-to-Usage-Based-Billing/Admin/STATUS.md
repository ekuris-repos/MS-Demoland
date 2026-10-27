# Copilot Billing - From PRUs to Usage-Based Billing - Content Status

> **Track:** Developer | **Level:** Enterprise
> **Last Updated:** 2026-10-27

## Rollup Status

<!-- This is the single value shown on the navigation screen.           -->
<!-- Set it to the LOWEST status from the table below.                  -->
<!-- Values: Not Started | In Progress | Ready for Review | Complete    -->

`Status: In Progress`

<!-- AGENT SYNC: When changing this status, you MUST also update the matching -->
<!-- entry in api/course-statuses.json so the nav page stays in sync. -->

## Overall Completion

| Area                  | Status           |
|-----------------------|------------------|
| Slide Content         | Ready for Review |
| Speaker Notes         | Ready for Review |
| Images & Diagrams     | In Progress      |
| Demo / Lab Content    | Ready for Review |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 - Title slide finalized
- [x] Slide 2 - Overview section divider
- [x] Slide 3 - Agenda: Today's Agenda
- [x] Slide 4 - Part 1 section divider: Why GitHub Changed Billing
- [x] Slide 5 - Why Move Away From PRUs?
- [x] Slide 6 - PRUs vs. AI Credits (comparison table)
- [x] Slide 7 - What Stays the Same, What Changes (two-column comparison)
- [x] Slide 8 - Migration Timing and Transitional Details
- [x] Slide 9 - Part 2 section divider: How Usage-Based Billing Works
- [x] Slide 10 - What Is a GitHub AI Credit?
- [x] Slide 11 - What Is Billed and What Is Not? (table)
- [x] Slide 12 - Included Usage by Plan (table)
- [x] Slide 13 - How Spend Accumulates (Mermaid flow)
- [x] Slide 14 - The Four Spend Levers You Control
- [x] Slide 15 - Part 3 section divider: Admin Controls and Governance
- [x] Slide 16 - Pooled Credits Change the Economics
- [x] Slide 17 - Budget Control Scopes (semantics and precedence table)
- [x] Slide 18 - What Happens When the Pool Runs Out?
- [x] Slide 19 - A Sane Starting Policy (table)
- [ ] Slide 20 - Current AI usage screenshot still required; explicit TODO placeholder added
- [x] Slide 21 - Part 4 section divider: Developer Habits That Lower Spend
- [x] Slide 22 - Choose the Cheapest Surface That Still Solves the Task (table)
- [x] Slide 23 - Example: Use Inline Chat on a Single Function
- [x] Slide 24 - Example: Architect with Comments, Then Let Completions Fill It In
- [x] Slide 25 - Use Auto for the Default Path
- [x] Slide 26 - Override Auto Only When the Task Justifies It (table)
- [x] Slide 27 - Keep Prompts Concise and Batch Related Asks
- [x] Slide 28 - Reset or Compact Long Sessions
- [x] Slide 29 - Preserve Useful Context, Cut Rework (official cache-aware guidance)
- [x] Slide 30 - Part 5 section divider: Rollout and Real Scenarios
- [x] Slide 31 - Scenario: Same Bug, Cheaper Workflow (table)
- [x] Slide 32 - Scenario: When Higher Spend Is the Right Call (two-column)
- [x] Slide 33 - A Practical 30-Day Rollout Plan (table)
- [x] Slide 34 - Team Policy Checklist
- [x] Slide 35 - Summary section divider
- [x] Slide 36 - Key Takeaways
- [x] Slide 37 - Resources
- [x] Slide 38 - Closing slide

## Notes

- 2026-10-27 slide-only automated review and factual refresh: corrected retired preview billing steps, annual-plan exceptions, Copilot CLI compaction, pre-request budget checks, and hosted Actions cost qualifications. Added current budget semantics, paid-usage defaults, cost-center controls, Auto tiers/discount, calendar resets, and cache-aware workflow guidance within the existing 38 slides.
- Official sources verified 2026-10-27: [organizational billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing), [individual billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing), [budgets](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/budgets), [models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), [Auto selection](https://docs.github.com/en/copilot/concepts/models/auto-model-selection), [efficiency and compaction](https://docs.github.com/en/copilot/tutorials/optimize-ai-usage), [code review](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/code-review), and [VS Code inline chat](https://code.visualstudio.com/docs/chat/inline-chat).
- Dated changelog evidence: [preview retirement, August 4](https://github.blog/changelog/2026-08-04-retiring-the-copilot-billing-preview-app/), [Auto tiers, September 14](https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection/), and [review billing controls, October 8](https://github.blog/changelog/2026-10-08-copilot-code-review-new-organization-billing-options-and-controls/).
- Media remains In Progress: slide 20 now has an explicit local TODO for a current AI usage screenshot. No screenshot was fabricated. Human approval and browser/media acceptance remain pending; Reviewed & Approved is In Progress, not approved.
- Labs explicitly excluded: no lab content was opened, reviewed, validated, or changed; all existing lab checklist/area values are preserved. This is not a full-course readiness or approval claim.
- Rollup remains In Progress, the lowest remaining area status. Catalog JSON synchronization is owned by the orchestrator for this change set.
- Minimal lab.json included to match the current course folder pattern in this repository.