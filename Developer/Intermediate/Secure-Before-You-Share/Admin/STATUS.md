# Secure Before You Share: Content Status

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
| Images & Diagrams     | Ready for Review |
| Demo / Lab Content    | In Progress      |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slides 1-4: Challenge, outcomes, and secure change loop
- [x] Slides 5-11: Local inspection, review, triage, and remediation
- [x] Slides 12-16: Local-to-platform transition and CodeQL
- [x] Slides 17-20: Autofix boundaries and evaluation
- [x] Slides 21-23: Organization controls and final gate
- [x] Slide 24: Completion

## Notes

- Validate the challenge against the selected disposable demo repository.
- Verify a supported default-branch backlog alert and effective Autofix settings in the delivery environment, or capture a candidate proposal before delivery. Do not assume PR-only alerts expose the same actions.
- Confirm current product availability and terminology before delivery.

### Slide-only factual refresh: 2026-10-27

- Reviewed and refreshed all 24 slides and speaker notes only. Corrected Autofix controls, branch/PR behavior, access and cost prerequisites, conditional availability, local diff context, CodeQL path interpretation, and configured merge-gate limitations. Added brief advisory-only AI Scan context without expanding the hands-on scope.
- Official sources checked 2026-10-27: [Autofix concepts](https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning), [alert resolution](https://docs.github.com/en/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts), [merge protection](https://docs.github.com/en/code-security/concepts/code-scanning/merge-protection), [AI Scan](https://docs.github.com/en/code-security/concepts/code-scanning/ai-powered-security-detections), and the [2026-10-15 agentic autofix GA announcement](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/).
- Slide content, notes, and inline diagrams are ready for review, not approved. No TODO visual references remain; browser rendering and the live demonstration environment are not verified. Official documentation conflicts on one-step Autofix for CodeQL PR-only alerts, so delivery requires the explicit default-branch/environment prerequisite or captured-proposal fallback.
- Labs were explicitly excluded and untouched. Demo / Lab Content and Reviewed & Approved remain In Progress; the rollup remains In Progress. No human approval or full-course completion is claimed.