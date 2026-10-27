# Security Proving Trust in the System — Content Status

> **Track:** Non-Developer | **Level:** Enterprise
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

- [x] Slides 1-30: slide text and all speaker notes received a dated factual refresh
- [x] Slides 8-12: training, retention, residency, and exclusion scope/timing corrected
- [x] Slides 14-21: audit coverage, contractual defense, matching-code policy, and inheritance corrected
- [x] Slides 23-30: evidence boundaries, playbook, reporting caveats, and official sources refreshed
- [ ] Slide 11: current content-exclusion settings screenshot
- [ ] Slide 14: current Copilot audit-log screenshot
- [ ] Slide 20: current feature/model policy screenshot
- [ ] Human content approval and rendered visual review

## Notes

### 2026-10-27: Slide-only factual review and refresh

- Reviewed all 30 slides and speaker-note blocks. Corrected exclusion scope and
  propagation, retention versus training, audit completeness, public-code
  matching, policy inheritance, and conditional contractual defense. Added
  bounded agent/model/tool governance and an evidence matrix without adding slides.
- Official evidence: [GitHub content exclusions](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion),
  [configuration and refresh](https://docs.github.com/en/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot),
  [audit coverage](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs),
  [customer terms](https://github.com/customer-terms/github-generative-ai-services-terms),
  [policies](https://docs.github.com/en/copilot/concepts/enterprise/policies),
  [residency](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency),
  and [current Microsoft copyright mitigations](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment).
  Verification date: 2026-10-27.
- Remaining blockers: three explicit TODO screenshots; official CLI exclusion
  documentation conflicts; actual attestation scope and technical security
  specifications require vendor review; legal applicability and contractual
  coverage require organization-specific assessment. No human approval or
  rendered visual signoff is claimed.
- Labs explicitly excluded: no lab content was opened, reviewed, validated,
  or changed. The Demo / Lab Content area value is unchanged.
- Slide Content and Speaker Notes remain Ready for Review. Images & Diagrams
  and Reviewed & Approved remain In Progress pending their respective blockers.
  Rollup: In Progress. The orchestrator owns catalog JSON synchronization for
  this coordinated change set.
