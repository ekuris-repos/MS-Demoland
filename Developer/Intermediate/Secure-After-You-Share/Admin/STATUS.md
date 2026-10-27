# Secure After You Share: Content Status

> **Track:** Developer | **Level:** Intermediate
> **Last Updated:** 2026-10-27

## Rollup Status

<!-- This is the single value shown on the navigation screen.                    -->
<!-- Set it to the LOWEST status from the table below.                           -->
<!-- Values: Not Started | In Progress | Ready for Review | Complete             -->

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

- [x] Slides 1-4: Challenge, outcomes, and cloud security loop
- [x] Slides 5-9: Actions trust boundaries, permissions, OIDC, and environments
- [x] Slides 10-15: CodeQL, secret scanning, dependency review, and triage
- [x] Slides 16-20: Copilot code review, agent boundaries, and artifact attestations
- [x] Slides 21-22: Rulesets and ownership
- [x] Slides 23-28: Security campaign scoping, operation, remediation, and outcomes
- [x] Slide 29: Merge decision
- [x] Slide 30: Completion

## Notes

- Select or create the disposable repository and prepared pull request used by the lab.
- Capture fallback screenshots for CodeQL, secret scanning, and Copilot code review.
- Confirm product availability, licensing, and terminology before delivery.
- Confirm secret campaign availability before delivery: the dated GA announcement and live documentation's preview label conflict.
- Validate the workflow permission and OIDC examples against the selected cloud provider.

### Slide-only factual review: 2026-10-27

- Corrected the complete JavaScript/TypeScript CodeQL example with verified full commit pins, initialization, no-build analysis, and job-scoped write permission. Corrected the environment gate and OIDC token-exchange sequence.
- Separated direct agentic-autofix assignment from Copilot Autofix suggestions; clarified current agent naming, validation limits, prerequisites, dependency-check enforcement, and CodeQL data-flow scope.
- Official sources: [CodeQL Action](https://github.com/github/codeql-action), [OIDC](https://docs.github.com/en/actions/concepts/security/openid-connect), [environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments), [autofix](https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning), and [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets), verified 2026-10-27.
- Lifecycle discrepancy retained explicitly: [2025-11-25 secret campaign GA announcement](https://github.blog/changelog/2025-11-25-secret-scanning-alert-assignees-security-campaigns-are-generally-available/) versus the preview label in [live campaign documentation](https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns). Tenant availability is unverified.
- Slide Content and Speaker Notes remain Ready for Review, not human-approved. Images & Diagrams and Reviewed & Approved remain In Progress. The two TODO screenshots remain explicit; cloud-provider trust, tenant entitlements/policies, workflow execution, and rendered-slide verification remain delivery checks.
- Labs were explicitly excluded: no lab content was read, validated, or modified, and all existing lab status values and checklist entries are unchanged. This is not a full-course approval. Rollup remains In Progress.