# Operations Enterprise Scale — Content Status

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

- [x] Slide 1 — Title and scope reviewed
- [x] Slide 2 — Overview reviewed
- [x] Slide 3 — Agenda reviewed
- [x] Slide 4 — Scale challenge transition reviewed
- [x] Slide 5 — Manual operations scenario reviewed
- [x] Slide 6 — AI context, evidence, and data boundaries corrected
- [x] Slide 7 — Automation transition reviewed
- [x] Slide 8 — Compilation, preview, approval, and identity distinctions corrected
- [x] Slide 9 — Pipeline prompt and tested-version guidance corrected
- [x] Slide 10 — Ops tasks transition reviewed
- [x] Slide 11 — Script dry-run and logging safeguards clarified
- [x] Slide 12 — Sanitized logs, hypotheses, and query validation clarified
- [x] Slide 13 — Runbook context and review requirements clarified
- [x] Slide 14 — Observability transition reviewed
- [x] Slide 15 — Query languages, platform, labels, and duration clarified
- [x] Slide 16 — Dashboard schema and validation requirements clarified
- [x] Slide 17 — Incident response transition reviewed
- [x] Slide 18 — Evidence-based correlation and qualified outcomes corrected
- [x] Slide 19 — Rollback context, approval, and verification corrected
- [x] Slide 20 — Postmortem data handling and follow-up dates clarified
- [x] Slide 21 — Reporting transition reviewed
- [x] Slide 22 — SLI/SLO/SLA definitions and controlled publishing clarified
- [x] Slide 23 — Billing data, evidence, and pricing boundaries clarified
- [x] Slide 24 — Platform transition reviewed
- [x] Slide 25 — Private/internal visibility and configuration boundaries corrected
- [x] Slide 26 — Security packaging, push protection, and entitlements corrected
- [x] Slide 27 — Summary transition reviewed
- [x] Slide 28 — Qualified takeaways corrected
- [x] Slide 29 — Environment availability and safe follow-up clarified

## Notes

### 2026-10-27 slide-only review and factual refresh

- Reviewed all 29 slides and speaker-note blocks. Checklist marks record this
  slide-content pass, not human approval or full-course readiness.
- Corrected Bicep compilation versus resource preview, Kubernetes rollback
  context, internal repository read visibility, and push-time secret protection.
  Added sensitive-data minimization and authorized publishing boundaries.
- Qualified generated-output, performance, integration, and entitlement claims.
  Refreshed dashboard/schema, version-pin, reliability-definition, and security
  product wording without asserting new pricing or announcement dates.
- Official references verified in phase 1 on 2026-10-27:
  [Bicep CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-cli),
  [Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if),
  [Kubernetes rollback](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/),
  [GitHub base permissions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization),
  [push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection),
  [Copilot responsible use](https://docs.github.com/en/copilot/responsible-use/chat),
  [Azure OIDC](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure),
  and [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features).
- Images & Diagrams remains In Progress pending visual/browser rendering review;
  no missing local assets were found during the slide-only checks. No screenshot
  was fabricated and no remaining visual work is claimed complete.
- Focused validation passed: balanced HTML, 29 slides in the original order,
  29 nonempty notes without em/en dashes, four retained Mermaid blocks, four
  resolving local asset references, and the illustrative error-budget arithmetic.
  Existing section-anchor state and shared navigation links are preserved.
- Human approval is pending. Tenant-specific integrations, queries, deployment
  permissions, and entitlements have not been executed or independently tested.
  Performance improvements are not established benchmarks.
- Labs explicitly excluded: no lab files were opened or changed. The Demo / Lab
  Content status is preserved exactly and remains an unresolved readiness area.
- Rollup remains **In Progress**, the lowest area status. Catalog JSON
  synchronization is owned by the orchestrator, not this course change.
