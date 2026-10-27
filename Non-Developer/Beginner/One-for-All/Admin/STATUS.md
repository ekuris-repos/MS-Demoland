# GitHub One for All — Content Status

> **Track:** Non-Developer | **Level:** Beginner
> **Last Updated:** 2026-10-27

## Rollup Status

<!-- This is the single value shown on the navigation screen.           -->
<!-- Set it to the LOWEST status from the table below.                  -->
<!-- Values: Not Started | In Progress | Complete                       -->

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

> **How to update:** Set each area to `Not Started`, `In Progress`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Complete)*

## Slide-by-Slide Checklist

- [x] Slides 1-3: title, scope, and agenda reviewed
- [x] Slides 4-12: platform, repositories, Issues, and Projects reviewed
- [x] Slides 13-21: Actions, code quality, and security reviewed
- [x] Slides 22-27: Copilot, enterprise controls, and connected workflow reviewed
- [x] Slides 28-31: takeaways, next steps, and closing reviewed
- [x] All 31 speaker-note blocks reviewed; presenter directives rewritten
- [ ] Browser review of slide layout, diagrams, and navigation completed
- [ ] Human review and approval completed

## Notes

### 2026-10-27 slide-only review

- Reviewed all 31 slides and speaker-note blocks against live official GitHub
  documentation and dated Changelog posts. This is not human approval or a
  full-course review. Labs were explicitly excluded; their status is unchanged.
- Corrected repository-policy scope and public-preview labeling, clarified
  Enterprise Cloud and identity applicability, replaced an unsupported Copilot
  governance-reporting claim, and rewrote four presenter directives as spoken
  questions. Added brief Copilot policy-default and permission context.
- Slide Content and Speaker Notes remain Ready for Review. Images & Diagrams
  remains In Progress pending browser rendering, layout, and diagram checks.
  Referenced assets exist; no TODO media placeholders occur in this deck.
- Exact identity-provider/provisioning recipes and automatic Copilot access to
  enterprise reports were not verified and are not promised. Human approval is
  still outstanding.
- Rollup is In Progress, the lowest current area status. The orchestrator owns
  synchronization of `api/course-statuses.json` in this change set.

Official sources verified 2026-10-27:

- [Repository policies and their preview scope](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/governing-how-people-use-repositories-in-your-enterprise)
- [Enterprise Cloud and enterprise types](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-enterprise-cloud)
- [Copilot on GitHub.com](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github)
- [Copilot feature-default policy, 2026-10-22](https://github.blog/changelog/2026-10-22-global-default-for-copilot-features-generally-available/)
- [Assisted permissions, 2026-10-26](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available/)
