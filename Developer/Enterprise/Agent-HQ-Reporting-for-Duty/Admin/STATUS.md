# Agent HQ Reporting for Duty — Content Status

> **Track:** Developer | **Level:** Enterprise
> **Last Updated:** 2026-10-27

## Rollup Status

<!-- This is the single value shown on the navigation screen.           -->
<!-- Set it to the LOWEST status from the table below.                  -->
<!-- Values: Not Started | In Progress | Ready for Review | Complete    -->

`Status: Not Started`

<!-- AGENT SYNC: When changing this status, you MUST also update the matching -->
<!-- entry in api/course-statuses.json so the nav page stays in sync. -->

## Overall Completion

| Area                  | Status           |
|-----------------------|------------------|
| Slide Content         | Ready for Review |
| Speaker Notes         | Ready for Review |
| Images & Diagrams     | In Progress      |
| Demo / Lab Content    | Not Started      |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Title slide (Enterprise · 1 Hour badge, subtitle, speaker notes)
- [x] Slide 2 — Section divider: What We'll Cover
- [x] Slide 3 — Today's Agenda (9-item roadmap with speaker notes)
- [x] Slide 4 — Section divider: What Is Agent Coordination?
- [x] Slide 5 — The Multi-Surface Reality (handoff flow and speaker notes)
- [x] Slide 6 — Agent Surfaces at a Glance (VS Code, GitHub.com, standalone CLI, Slack)
- [x] Slide 7 — Section divider: Agent Mode in VS Code
- [x] Slide 8 — Choose the Least Autonomous Workflow (focused help, questions, planning, execution)
- [x] Slide 9 — Agent Mode: How It Works (permissions versus edit review)
- [x] Slide 10 — Model Selection in Agent Workflows (current catalog, token costs, budgets)
- [x] Slide 11 — Section divider: Copilot Across Surfaces
- [x] Slide 12 — Copilot on GitHub.com (chat, tasks, summaries, review, access)
- [x] Slide 13 — Copilot in the CLI (standalone CLI and permission boundaries)
- [x] Slide 14 — Copilot in Slack (GitHub app, preview, identity and thread context)
- [x] Slide 15 — Section divider: The Copilot Cloud Agent
- [x] Slide 16 — What Is the Cloud Agent? (scope and PR safeguards)
- [x] Slide 17 — How the Cloud Agent Works (assignment, steering, workflow approval, integration)
- [x] Slide 18 — When to Use the Cloud Agent (bounded tasks and human involvement)
- [x] Slide 19 — Section divider: Launching Agents from Issues & PRs
- [x] Slide 20 — Issues, Changes, and Reviews (supported entry-point table)
- [x] Slide 21 — Automated Triage with Copilot (configured automations and preview workflows)
- [x] Slide 22 — Section divider: Multi-Agent Workflows
- [x] Slide 23 — Coordination Patterns (Sequential, Fan-Out, Event-Driven, Human-in-the-Loop)
- [x] Slide 24 — Track Parallel Work with Agent HQ (session tracking and isolation)
- [x] Slide 25 — Managing Parallel Agents (multiline Windows worktree example and prerequisites)
- [x] Slide 26 — End-to-End: From Issue to Merge (explicit gates and evidence)
- [x] Slide 27 — Section divider: MCP & Custom Agents
- [x] Slide 28 — Tools, Specialization, and Delegation (building-block comparison)
- [x] Slide 29 — A Governed Tool Integration (conceptual MCP flow, not server pseudocode)
- [x] Slide 30 — Section divider: Custom Instructions & Enterprise Governance
- [x] Slide 31 — Custom Instructions Across Surfaces (support table, no unrelated screenshot)
- [x] Slide 32 — Enterprise Permissions and Policies (exclusions caveat, controls, qualified terms)
- [x] Slide 33 — Audit Logs and Observability (evidence sources and coverage limits)
- [x] Slide 34 — Section divider: Real-World Scenarios
- [x] Slide 35 — Scenario: Security Vulnerability Remediation (alerts and qualified delegation)
- [x] Slide 36 — Scenario: Dependency Updates at Scale (batching, limits, ownership, measurement)
- [x] Slide 37 — Scenario: Documentation Generation (reviewable cross-repository updates)
- [x] Slide 38 — Section divider: Wrap-Up & Next Steps
- [x] Slide 39 — Key Takeaways (scope, isolation, controls, measured adoption)
- [x] Slide 40 — Thank You / Closing slide

## Notes

- 40 slides total; existing section order, section class sequence, and numeric navigation positions preserved.
- All 40 slides have nonempty audience-facing speaker notes; no em or en dashes in notes.
- Inline diagrams and support tables replace obsolete extension architecture and the unrelated instruction screenshot; visual acceptance remains pending.
- No lab.json required for this course.

### 2026-10-27 Slide-Only Review

- Refreshed slides and notes against official sources: [CLI replacement](https://github.com/github/copilot-cli), [extension retirement](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/), [supported cloud entry points](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github), [agent safeguards](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations), [content-exclusion limits](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion), [instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support), and [worktree syntax](https://git-scm.com/docs/git-worktree).
- Replaced retired CLI/extension guidance, unsupported mention-based triage, and blanket access/audit/IP guarantees. Added supported automation and task tracking; repaired the worktree example without executing mutating commands.
- Focused validation passed: 40 slide positions and navigation hashes, nonempty notes, punctuation, all local assets, six diagrams parsed by Mermaid 11, and both command examples parsed by PowerShell without execution. The existing orchestrator server served the course successfully; no server or dependency installation was started.
- Full visual acceptance is pending: the integrated browser tab was hidden, so shared animation-frame diagram rendering and manual navigation interaction could not be visually accepted. Diagram parsing and programmatic navigation checks passed. Tenant/UI behavior, preview availability, precise service/concurrency limits, and SIEM exports/connectors remain qualified and unverified in a live environment.
- Human approval and full visual acceptance are still pending. This is not a full-course approval.
- Labs explicitly excluded: all existing lab-related entries and the Demo / Lab Content value are preserved without reassessment. The lowest-area rollup remains **Not Started**.
- The orchestrator owns the matching catalog JSON update in the same change set; this course change does not edit that file.
