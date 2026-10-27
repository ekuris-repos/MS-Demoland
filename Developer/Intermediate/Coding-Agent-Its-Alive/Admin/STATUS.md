# GitHub Coding Agent Its Alive — Content Status

> **Track:** Developer | **Level:** Intermediate
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
| Demo / Lab Content    | N/A              |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Title slide finalized
- [x] Slide 2 — Overview section divider
- [x] Slide 3 — Agenda: Today's Journey
- [x] Slide 4 — Part 1 section divider: Meet the Cloud Agent
- [x] Slide 5 — What Is Copilot Cloud Agent?
- [x] Slide 6 — Cloud vs. Local VS Code Sessions (two-column)
- [x] Slide 7 — Parallelizing Agent Work
- [x] Slide 8 — How the Cloud Agent Works (issue and prompt paths)
- [x] Slide 9 — Part 2 section divider: Triggering the Cloud Agent
- [x] Slide 10 — Assigning Issues to Copilot
- [x] Slide 11 — Writing Effective Issue Descriptions (two-column)
- [x] Slide 12 — Watching the Agent Work (text refreshed; session screenshot TODO)
- [x] Slide 13 — Part 3 section divider: Custom Instructions
- [x] Slide 14 — Organization-Level Instructions
- [x] Slide 15 — Example: Organization Settings Text
- [x] Slide 16 — Repository-Level Instructions
- [x] Slide 17 — Example: Repo-Level copilot-instructions.md
- [x] Slide 18 — Layering: Org + Repo Instructions
- [x] Slide 19 — Part 4 section divider: Environment Setup
- [x] Slide 20 — The copilot-setup-steps.yml File
- [x] Slide 21 — Example: complete setup workflow
- [x] Slide 22 — Part 5 section divider: Reviewing & Handoff
- [x] Slide 23 — Reviewing Cloud Agent Pull Requests
- [x] Slide 24 — Common Patterns in Agent Output (two-column)
- [x] Slide 25 — Handoff: VS Code → Cloud Agent
- [x] Slide 26 — Handoff: Cloud Agent → VS Code
- [x] Slide 27 — Part 6 section divider: Governance & Best Practices
- [x] Slide 28 — Managing Sessions and Capacity
- [x] Slide 29 — Security and Trust
- [x] Slide 30 — Best Practices for Success
- [x] Slide 31 — Summary section divider
- [x] Slide 32 — Key Takeaways
- [x] Slide 33 — Where to Go Next
- [x] Slide 34 — Closing slide

## Notes

### 2026-10-27 slide-only factual refresh

All 34 slide sections and their speaker notes were reviewed and refreshed. Labs
were explicitly excluded and the Demo / Lab Content value above is unchanged.
This is not human approval or a full-course/lab sign-off.

- Corrected organization instructions to Settings → Copilot → Custom instructions;
  retained repository files and added scoped-instruction awareness.
- Replaced the invalid setup path and fragment with a complete
  `.github/workflows/copilot-setup-steps.yml` workflow, checkout, current action
  examples, a supported Node 24 baseline, and explicit lockfile/project-script
  assumptions. Setup is optional preparation, not a guarantee of validation.
- Corrected issue assignment, session steering, PR feedback, branch-first work,
  native IDE handoff, workflow approval and separate-reviewer requirements.
- Refreshed AI-credit budget guidance, explicitly configured secrets/context,
  firewall limits, persistent logs and optional Memory. Removed unverified
  Firecracker, exact training-policy and plan-specific Actions-allocation claims
  rather than asserting they were verified.
- Corrected screenshot placement/alt text, removed two unsuitable diagram
  placeholders, repaired documentation links, and reconciled the 34-slide count.
- Remaining media blocker: slide 12 explicitly requests a real session-log and
  steering screenshot at `img/TODO-screenshot-cloud-agent-session-log.png`.
  No screenshot was fabricated. Human review, visual fit and authenticated
  workflow/IDE checks remain outstanding; no install or live workflow was run.

Official sources verified 2026-10-27:
[organization instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-organization-instructions),
[agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment),
[task kickoff](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task),
[review gates](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output),
[secrets](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables),
[billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing),
[Node lifecycle](https://nodejs.org/en/about/previous-releases), and
[VS Code handoff](https://code.visualstudio.com/docs/agents/run/agent-harnesses).
Supporting current documentation and dated changelog evidence are retained in
the session review JSON.

Rollup remains **In Progress**, the lowest applicable area status. Catalog JSON
synchronization is reserved for the orchestrator in this change set.
