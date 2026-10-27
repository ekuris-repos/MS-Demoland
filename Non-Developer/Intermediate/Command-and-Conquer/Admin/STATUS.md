# Executives Command and Conquer — Content Status

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

- [x] Slides 1-7 — Executive framing and agenda refreshed; unsupported benchmarks removed
- [x] Slide 8 — Current usage reports, permissions, and separate seat/billing sources explained
- [ ] Slide 9 — Content refreshed; current usage-dashboard screenshot still pending
- [x] Slides 10-13 — Engagement, telemetry limits, outcome evidence, and capacity framing refreshed
- [x] Slide 14 — Illustrative monthly model, pooled AI credits, and budget ownership added
- [x] Slides 15-17 — Governance boundaries and contract-specific qualifications corrected
- [ ] Slide 18 — Policies refreshed; current AI-controls screenshot still pending
- [x] Slides 19-22 — Privacy-aware reporting and pre-pilot governance refreshed
- [x] Slides 23-24 — Neutral evaluation criteria and MCP replacement explained
- [x] Slides 25-28 — Takeaways, action plan, and closing aligned with corrections
- [ ] Human review and approval of the refreshed slides and notes

## Notes

### 2026-10-27: Slide-only factual review and refresh

- Reviewed all 28 slides and speaker-note blocks; retained slide order, section
  classes, shared-asset links, and navigation script. Reformatted the previously
  minified HTML for maintainability. No slide IDs existed to change.
- Replaced the retired Metrics API workflow with current usage-report downloads
  and separated usage, seat inventory, and billing sources. Corrected latency,
  permissions, reporting scope, and policy-delegation claims.
- Replaced deterministic suggestion-to-dollar ROI with an explicitly hypothetical
  monthly capacity model. Added license-plus-usage costs, pooled AI credits,
  default paid-usage awareness, and budget ownership.
- Qualified content-exclusion coverage, data handling, and contractual IP
  protections. Replaced retired GitHub App-based Copilot Extensions with MCP.
  Baseline data/tool policies and budgets now precede new access.
- Validation: 28 slides and 28 nonempty notes; no em/en dashes in notes; no
  explicit slide IDs added or removed; local shared assets resolve. Two
  intentionally missing TODO screenshots remain. Numerical examples checked.
- Remaining blockers: current dashboard/control screenshots, applicable current
  retention/indemnity terms for the customer's agreement, tenant-specific
  policy/permission verification, and human approval. Exact dashboard/API
  telemetry coverage must be checked for the report and client in use.
- **Labs excluded:** No lab content was opened, reviewed, validated, or changed.
  The Demo / Lab Content area value is preserved unchanged.
- Slide Content and Speaker Notes remain **Ready for Review**, not approved.
  Images & Diagrams and Reviewed & Approved remain **In Progress**.
  Rollup: **In Progress**. The orchestrator owns catalog JSON synchronization;
  no catalog file was edited in this scoped change.

Official sources verified on 2026-10-27:

- [Legacy metrics API retirement](https://github.blog/changelog/2026-01-29-closing-down-notice-of-legacy-copilot-metrics-apis/) (2026-01-29).
- [Current usage metrics APIs](https://docs.github.com/en/rest/copilot/copilot-usage-metrics) and [usage concepts](https://docs.github.com/en/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics).
- [Dashboard access and latency](https://docs.github.com/en/copilot/how-tos/administer-copilot/view-usage-and-adoption).
- [Seat costs](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/seats-and-billing-cycles) and [AI-credit billing/budgets](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing).
- [Exclusion limitations](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion) and [policy scope/conflicts](https://docs.github.com/en/copilot/concepts/enterprise/policies).
- [Extensions sunset and MCP replacement](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/) (2025-09-24).
- [Current customer-terms directory](https://github.com/customer-terms) and [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
  Contract-specific coverage remains unverified; archived terms were not treated
  as the current agreement.
