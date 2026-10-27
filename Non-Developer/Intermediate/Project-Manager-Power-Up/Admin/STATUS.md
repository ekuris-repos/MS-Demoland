# Project Manager Power Up — Content Status

> **Track:** Non-Developer | **Level:** Intermediate
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

- [x] All 31 slide sections and nonempty speaker notes reviewed for the scoped factual refresh
- [x] PR summaries, TSV export, accuracy caveats, delivery states, and team-level measurement corrected
- [ ] Slides 8, 11, and 18: capture and review the explicit TODO screenshots
- [ ] Confirm account-specific Copilot access and run the browser workflows with the intended audience
- [ ] Human review and approval

## Notes

### 2026-10-27: scoped slide-only factual refresh

Corrected on-demand PR summaries and refresh limitations, TSV view exports, unsupported accuracy/live-data claims, and distinctions between merged, released, and deployed work. Replaced commit-based productivity judgments with contextual team-level flow and outcome guidance. Qualified Copilot access, source coverage, and interpretation of risk signals.

Official sources checked on 2026-10-27:

- [GitHub PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary) and [Copilot responsible use](https://docs.github.com/en/copilot/responsible-use/chat)
- [Project TSV exports](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/exporting-your-projects-data) and [Insights](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects)
- [Linked-PR workflow](https://github.blog/changelog/2025-11-06-improved-onboarding-flow-for-github-projects/) and [issue closure rules](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
- [GitHub measurement guidance](https://github.blog/enterprise-software/devops/measuring-enterprise-developer-productivity/) and [DORA metrics](https://dora.dev/guides/dora-metrics/)

All 31 slide sections and notes remain present. Screenshots on slides 8, 11, and 18 remain missing and explicitly marked TODO. Account-specific Copilot entitlements, organization policies, authenticated workflows, and browser rendering remain unverified. Automated slide review is not human approval; Reviewed & Approved remains In Progress.

Labs were explicitly excluded and untouched. This is not a full-course approval. Rollup remains In Progress because media, approval, and the unchanged lab area are not complete. The orchestrator owns central catalog status synchronization; no catalog JSON was changed here.
