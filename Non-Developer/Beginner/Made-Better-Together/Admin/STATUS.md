# Copilot and Azure DevOps — Content Status

> **Track:** Non-Developer | **Level:** Beginner
> **Last Updated:** 2026-10-27 (slide-only factual refresh)

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
| Demo / Lab Content    | In Progress      |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Scope and audience clarified
- [x] Slide 2 — Agenda divider and notes reviewed
- [x] Slide 3 — Agenda names connected Copilot surfaces accurately
- [x] Slide 4 — Two-platform divider and notes reviewed
- [x] Slide 5 — Coexistence context reviewed
- [x] Slide 6 — Plan, policy, permissions, and separate-charge caveat refreshed
- [x] Slide 7 — Security divider and notes reviewed
- [x] Slide 8 — Azure Repos boundary and active-committer billing clarified
- [x] Slide 9 — Documented security views replace unverified widgets
- [x] Slide 10 — Boards integration divider reviewed
- [ ] Slide 11 — Linking and transitions corrected; verified UI screenshot still TODO
- [x] Slide 12 — Conditional state changes and burndown limitations corrected
- [x] Slide 13 — Native versus connected assistance distinguished
- [x] Slide 14 — Verified surface table replaces unsupported native bundle and misleading image
- [x] Slide 15 — GitHub Copilot divider reviewed
- [x] Slide 16 — Retired extensions replaced; issue triage and CODEOWNERS separated
- [x] Slide 17 — Prompts require bounded context, citations, and human verification
- [x] Slide 18 — Workflow divider reviewed
- [x] Slide 19 — Evidence flow simplified; secret-consumer arrow corrected
- [x] Slide 20 — Separate reporting surfaces, access, and refresh limits clarified
- [x] Slide 21 — Migration divider reviewed
- [x] Slide 22 — Process and compliance comparisons made requirement-based
- [x] Slide 23 — Consolidation no longer promises all Copilot entitlements
- [x] Slide 24 — Scenario divider reviewed
- [x] Slide 25 — Planning scenario uses approved MCP access and verified linking syntax
- [x] Slide 26 — Reporting scenario uses reviewed sources and documented security views
- [x] Slide 27 — Wrap-up divider reviewed
- [x] Slide 28 — Takeaways corrected consistently with the content
- [x] Slide 29 — Pilot requires authorization, cost review, and accuracy checks
- [x] Slide 30 — Closing and notes reviewed

## Notes

### 2026-10-27 slide-only review

- Refreshed all 30 slides and their speaker notes where factual corrections were needed. Checked slide count/order, section attributes and existing anchors, nonempty notes, punctuation, local references, and the linking examples. Checklist marks record slide-text review, not human approval or a live demonstration.
- Replaced retired GitHub App-based Copilot Extensions with approved MCP guidance. Distinguished agent-plus-MCP planning, native Azure Repos code-review public preview, and GitHub.com PR summaries. Corrected AB# linking versus default-branch completion, branch linking, security scope, report expectations, and pilot access/cost caveats.
- Removed the misleading GitHub.com image from the Azure DevOps feature claim; the replacement is a generated surface table, not a fabricated screenshot. Removed two redundant diagram TODOs because the existing definition list and comparison cards are self-contained. Slide 11 still has an explicit missing `img/TODO-screenshot-azure-boards-github-linking.png` placeholder.
- Remaining blockers: verified linking screenshot, browser/viewport and Mermaid rendering review, human approval, and target-tenant/client validation of permissions, MCP operations, preview availability, reporting access, and charges. Unidentified native AI bundles and security widgets remain unverified and are no longer promised.
- **Labs excluded:** no lab content was opened, reviewed, validated, or changed. The Demo / Lab Content area value is preserved exactly; no full-course completion is claimed.
- **Rollup: In Progress.** Media and approval remain In Progress, as does the untouched Demo / Lab Content area. The orchestrator owns catalog JSON synchronization in this change set.

Official sources verified 2026-10-27:

- [Extensions sunset, announced 2025-09-24](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/)
- [Azure Boards linking and transition rules](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops)
- [Azure DevOps MCP overview](https://learn.microsoft.com/en-us/azure/devops/mcp-server/mcp-server-overview?view=azure-devops) and [remote-first setup](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops)
- [Azure Repos code-review public preview, 2026-08-26](https://devblogs.microsoft.com/devops/copilot-code-reviews-for-azure-repos-public-preview/)
- [Azure Repos Security overview](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-security-overview?view=azure-devops) and [Advanced Security billing](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-billing?view=azure-devops)
- [GitHub PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary) and [responsible Copilot Chat use](https://docs.github.com/en/copilot/responsible-use/chat)
- [Azure DevOps Power BI integration](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/overview?view=azure-devops) and [GitHub connector limitations](https://learn.microsoft.com/en-us/power-query/connectors/github)
