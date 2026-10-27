# Agent Wars Return of the Chat ai — Content Status

> **Track:** Developer | **Level:** Add-Ons
> **Last Updated:** 2026-10-27
> **Disposition:** Archived; no catalog visibility change.

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

The checks below cover slide text and speaker notes only, not media, tenant execution, or human approval.

- [x] Slides 1-3: archived disposition, scope, and agenda corrected
- [x] Slides 4-6: ChatOps benefits qualified; notifications, commands, and agents distinguished
- [x] Slides 7-10: Teams app, invocation, setup roles, and illustrative delegation corrected
- [x] Slides 11-14: Slack setup, issue commands, subscriptions, and workflow controls corrected
- [x] Slides 15-17: retired server-side Copilot Extensions replaced with supported integration boundaries
- [x] Slides 18-21: native versus custom workflows and evidence-based investigations clarified
- [x] Slides 22-24: scoped Apps, webhook safeguards, and supported Teams transport guidance added
- [x] Slides 25-27: identity, context capture, privacy, audit coverage, and review boundaries corrected
- [x] Slides 28-30: summary and closing aligned with the archived slide-only scope
- [ ] Slide 8: capture a current, authorized Teams setup screenshot; TODO placeholder remains
- [ ] Slide 11: verify or replace the existing illustration against the current Slack interface
- [ ] Verify authorized Teams/Slack tenant setup, policies, permissions, and example workflows
- [ ] Obtain human review and approval of the refreshed slides and notes

## Notes

### 2026-10-27: slide-only factual refresh

The course remains archived. All 30 slide positions, section classes, and shared relative asset links are preserved; the original deck had no explicit slide IDs. Speaker notes remain nonempty and contain no em/en dashes. This is not a full-course completion claim or human approval.

Replaced retired GitHub App-based Copilot Extension teaching with a compact historical/current boundary and supported integration choices. Corrected Teams `@GitHub` invocation, Slack command syntax, optional agent delegation, and native workflow controls versus custom dispatch. Removed invented outputs and qualified identity, thread-context capture, no-model-training versus retention, and audit coverage. Added webhook validation and supported Teams messaging guidance.

Official sources checked on 2026-10-27:

- [Copilot Extension sunset, announced 2025-09-24; disabled 2025-11-10](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/)
- [Current Teams agent integration and prerequisites](https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams)
- [Current Slack agent integration and prerequisites](https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-slack)
- [Slack commands and issue actions](https://docs.github.com/en/integrations/how-tos/slack/use-github-in-slack) and [official integration README](https://github.com/integrations/slack)
- [Workflow dispatch API](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event) and [webhook best practices](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks)
- [Copilot data-use policies](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies) and [organization audit-log scope](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)
- [Teams connector warning and supported messaging guidance](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

Remaining blockers: slide 8 TODO screenshot; slide 11 media currency; no authorized tenant execution, entitlement, or current UX verification; human approval outstanding. Current docs label the agent features public preview; historical release wording and differing official Teams app installation links should not be treated as proof of tenant availability. Examples are illustrative, not executed.

Labs were explicitly excluded: no lab files were opened, validated, or changed, and the Demo / Lab Content status is preserved exactly. The referenced style guide was unavailable. Images & Diagrams and Reviewed & Approved remain In Progress. The lowest-area rollup remains **In Progress**; the orchestrator owns central JSON synchronization. No catalog JSON or visibility changes are part of this course refresh.
