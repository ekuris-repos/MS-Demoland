# Multi Agent Multi Repo Roundup — Content Status

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
| Demo / Lab Content    | Not Applicable   |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

| # | Type    | Title                                    | Notes | Status |
|---|---------|------------------------------------------|-------|--------|
| 1 | Title   | Cross-Repo Agents - Multi-Agent Multi-Repo Roundup | ✅ | Ready for Review |
| 2 | Section | What We'll Cover                         | ✅ | Ready for Review |
| 3 | Content | Today's Agenda                           | ✅ | Ready for Review |
| 4 | Section | The Multi-Repo Reality                   | ✅ | Ready for Review |
| 5 | Content | Why Enterprises Have Many Repos          | ✅ | Ready for Review |
| 6 | Content | Monorepo vs. Polyrepo Tradeoffs           | ✅ | Ready for Review |
| 7 | Section | Copilot's Context Model                  | ✅ | Ready for Review |
| 8 | Content | How Copilot Understands a Single Repo     | ✅ | Ready for Review |
| 9 | Content | The Cross-Repo Context Gap                | ✅ | Ready for Review |
| 10 | Content | Repository Indexing Deep Dive           | ✅ | Ready for Review |
| 11 | Section | Org-Level Custom Instructions           | ✅ | Ready for Review |
| 12 | Content | Custom Instructions Strategy            | ✅ | Ready for Review |
| 13 | Content | CCPR-Based Instructions Example         | ✅ | Ready for Review |
| 14 | Content | Scaling Instructions with Prompt Files  | ✅ | Ready for Review |
| 15 | Section | Shared Context Across Repos             | ✅ | Ready for Review |
| 16 | Content | Copilot Spaces and Repository Search    | ✅ | Ready for Review |
| 17 | Content | Curating Effective Cross-Repo Context    | ✅ | Ready for Review |
| 18 | Section | MCP Servers as Cross-Repo Bridges       | ✅ | Ready for Review |
| 19 | Content | MCP for Cross-Repo Context              | ✅ | Ready for Review |
| 20 | Content | Example: Cross-Repo API Spec Tool       | ✅ | Ready for Review |
| 21 | Section | Copilot Cloud Agent Across Repos        | ✅ | Ready for Review |
| 22 | Content | Cloud Agent Fundamentals                | ✅ | Ready for Review |
| 23 | Content | Multi-Repo Patterns with the Cloud Agent | ✅ | Ready for Review |
| 24 | Content | Local Parallelism: Sessions and Worktrees | ✅ | Ready for Review |
| 25 | Content | GitHub Actions as Agent Triggers        | ✅ | Ready for Review |
| 26 | Section | Multi-Agent Orchestration               | ✅ | Ready for Review |
| 27 | Content | Orchestration Patterns                  | ✅ | Ready for Review |
| 28 | Content | Fan-Out Pattern                         | ✅ | Ready for Review |
| 29 | Content | Dependency Management Across Repos      | ✅ | Ready for Review |
| 30 | Content | Code Consistency Across Repos           | ✅ | Ready for Review |
| 31 | Content | Migration Strategies with Agents        | ✅ | Ready for Review |
| 32 | Section | Governance & Permissions                | ✅ | Ready for Review |
| 33 | Content | Agent Access Controls                   | ✅ | Ready for Review |
| 34 | Content | Audit Trails & Compliance               | ✅ | Ready for Review |
| 35 | Content | Policy Guardrails for Multi-Repo Agents | ✅ | Ready for Review |
| 36 | Section | The Evolving Landscape                  | ✅ | Ready for Review |
| 37 | Content | What Is Changing                        | ✅ | Ready for Review |
| 38 | Content | What to Watch For                       | ✅ | Ready for Review |
| 39 | Content | Practical Recommendations Today         | ✅ | Ready for Review |
| 40 | Section | Wrap-Up & Key Takeaways                 | ✅ | Ready for Review |
| 41 | Content | Key Takeaways                           | ✅ | Ready for Review |
| 42 | Title   | Thank You                               | ✅ | Ready for Review |

## Notes

### 2026-10-27 slide-only factual refresh

- **Archive preserved:** The course remains under `Developer/Archive` with its Departing badge. All 42 slide positions, the existing absence of section IDs, deck classes, and relative shared-asset links are preserved. No catalog or visibility changes.
- **Corrections:** Separated organization settings from repository instructions and template copies; corrected cloud-agent setup, credentials, explicit task starts, worktree branch creation/isolation, and migration ordering. Restored multiline examples. The MCP example is explicitly non-executable pseudocode with no certified SDK/API or demo path.
- **Current context:** Replaced legacy knowledge-base assumptions with Spaces, scoped search, and MCP boundaries; added native local session/subagent context in existing slide positions. Recorded GitHub App-based Copilot Extensions retirement without implying ordinary GitHub Apps or client-side extensions were retired. Condensed speculative roadmap claims.
- **Checks completed:** Source-level HTML nesting, 42 sections with 42 nonempty notes, no em/en dashes in notes, shared local assets, checklist/title alignment, and example formatting/syntax checks. No mutating example commands executed.
- **Remaining blockers:** Browser/slide-scale and Mermaid runtime review remain pending, so Images & Diagrams is In Progress. Exact legacy `@github` behavior, comprehensive audit event/retention coverage, custom MCP runtime behavior, and tenant-specific UI/preview availability are not verified; the slides now say so or avoid depending on them. Human approval is pending; Reviewed & Approved is In Progress.
- **Labs excluded:** No lab content was opened, reviewed, validated, or modified. The Demo / Lab Content value remains exactly Not Applicable. This is not a full-course or lab-completion certification.
- **Status synchronization:** The orchestrator owns `api/course-statuses.json` synchronization in this change set. Reported rollup: **In Progress**; this agent did not edit catalog JSON.

Official sources checked on 2026-10-27:

- [Organization instructions and supported surfaces](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-organization-instructions)
- [Cloud-agent scope and limitations](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github), [permission/review protections](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations), [setup workflow](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment), and [API authentication](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api)
- [Copilot Spaces](https://docs.github.com/en/copilot/concepts/prompting-and-context/spaces), [workspace context](https://code.visualstudio.com/docs/agents/reference/workspace-context), and [native subagents](https://code.visualstudio.com/docs/agents/run/subagents)
- [Knowledge-base sunset notice, 2025-08-20; retirement updated to 2025-11-01](https://github.blog/changelog/2025-08-20-sunset-notice-copilot-knowledge-bases/) and [GitHub App-based Extensions sunset notice, 2025-09-24; sunset 2025-11-10](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/)
- [VS Code multi-agent release context, 2026-02-05](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development), [Agentic Workflows preview announcement, 2026-02-13](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/), and [Git worktree syntax](https://git-scm.com/docs/git-worktree)
