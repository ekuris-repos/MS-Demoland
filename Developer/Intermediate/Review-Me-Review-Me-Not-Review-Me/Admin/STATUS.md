# Review Me Review Me Not Review Me — Content Status

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
| Demo / Lab Content    | In Progress      |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [ ] Slide 1 — Title slide finalized
- [ ] Slide 2 — Agenda / section divider
- [ ] Slide 3 — Core content
- [ ] Slide 4 — Additional content slides (add rows as needed)
- [ ] Slide N — Closing slide

## Notes

### 2026-10-27 slide-only factual refresh

- Corrected PR-only versus default-branch alert routing. New PR findings are fixed on the same PR; agentic autofix accepts eligible default-branch alerts. Vulnerable code must not be merged to make an alert eligible.
- Updated agentic autofix to general availability on October 15, 2026, with separate access controls, administrator/billing prerequisites, and best-effort validation limits for custom queries, `security-extended`, and third-party tools.
- Qualified VS Code handoff controls by harness, clarified setup and instruction paths, and distinguished built-in agent checks from repository-required checks. Added workflow-run approval, independent human review, conditional Code Quality coverage prerequisites, and runner-dependent costs.
- Rewrote presenter directives as spoken narration. All 30 slides and nonempty note blocks remain; no slide anchors or shared-asset paths changed.
- Focused validation passed: slide numbering and note coverage, unchanged empty anchor set, four resolving local asset references, five structurally checked Mermaid blocks, parsed setup-workflow YAML, corrected-claim regression checks, preserved checklist/lab status, and lowest-area rollup. Example commands and workflows were not executed.
- Slide Content and Speaker Notes remain **Ready for Review**. This is an automated slide-only review, not human approval or a full-course signoff. Reviewed & Approved is **In Progress**.
- Images & Diagrams remains **In Progress** pending rendered layout and Mermaid checks. No screenshot was fabricated and no existing TODO visual was removed. Actual VS Code UI, repository eligibility/policies/billing, workflow execution, coverage upload, and an independent reviewer still require delivery-environment verification.
- **Labs excluded:** no lab file or exercise was inspected, validated, or changed. The Demo / Lab Content area and existing checklist entries are preserved exactly.
- Rollup remains **In Progress**, the lowest current area status. Catalog JSON synchronization is owned by the orchestrator for this coordinated change set; this course change does not edit it.

Official sources verified October 27, 2026:

- [Agentic autofix GA, October 15, 2026](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/)
- [Autofix capabilities and validation limits](https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning)
- [Agentic autofix access controls](https://docs.github.com/en/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/managing-access-to-agentic-autofix-for-code-scanning)
- [VS Code harnesses and handoff](https://code.visualstudio.com/docs/agents/run/agent-harnesses) and [planning controls](https://code.visualstudio.com/docs/agents/run/planning)
- [Cloud-agent security and approval controls](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations)
- [Setup steps](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment), [repository instruction paths](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions), and [MCP configuration](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers)
- [Code Quality prerequisites](https://docs.github.com/en/code-security/concepts/code-quality/code-quality) and [Copilot code-review runner usage](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/code-review)
