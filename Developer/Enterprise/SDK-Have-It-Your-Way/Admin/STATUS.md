# SDK Have It Your Way — Content Status

> **Track:** Developer | **Level:** Enterprise
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

- [x] Slides 1-10 — Intent, agenda, runtime architecture, and event model refreshed
- [x] Slides 11-15 — Pinned setup, explicit credentials, complete local application and HTTP example
- [x] Slides 16-18 — Event streaming fragment and implemented read-only fixture tool
- [x] Slides 19-24 — Context boundaries, multi-turn program, Azure token callback, and provider choice
- [x] Slides 25-30 — Deployment caveats, telemetry, identity, permissions, and operations
- [x] Slides 31-34 — Takeaways, official resource links, and closing notes
- [ ] All 34 slides — Human content approval and browser/slide-scale media review
- [ ] Code examples — Installed-package, live provider, identity, and deployment validation

## Notes

2026-10-27 slide-only factual refresh, based on the official
[SDK v1.0.27 release](https://github.com/github/copilot-sdk/releases/tag/v1.0.27),
[versioned SDK guides](https://github.com/github/copilot-sdk/tree/v1.0.27/docs),
[Azure sample](https://github.com/Azure-Samples/copilot-sdk-service), and
[deployment-type guidance](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types).
Corrected setup/version drift, token options, event streaming, tool handlers,
Azure credential renewal, product boundaries, residency claims, and monitoring
assurances. Complete local programs and insertion/configuration fragments are
labeled separately. The optional Azure sample remains on SDK 0.1.25 and is not
represented as compatible with the 1.0.27 examples.

Speaker notes are slide-only reviewed, not human approved. Automated checks
preserved 34 slides and nonempty notes, verified local asset paths, parsed the
PowerShell examples, and passed 48 JavaScript syntax/mock-behavior checks using
VS Code's Node v24.18.1 runtime. Browser navigation reached all 34 slides;
selected content and scrollable code panels fit the 768px-high viewport.
Images & Diagrams remain In Progress: inline Mermaid rendering was not observed,
the external font request failed, and final human media approval is outstanding.
No screenshots or approval were fabricated. Node/npm/azd are absent from PATH;
the discovered VS Code Node runtime was used without installing dependencies.
No models were called or resources deployed. Installed-package integration,
provider availability, real credentials, RBAC, actual HTTP transport behavior,
and hosted operation remain verification blockers.

Labs explicitly excluded: no lab files inspected or changed, and the Demo / Lab
Content area value is preserved. Rollup remains In Progress because approval,
media, and untouched lab work are unresolved. The orchestrator owns central
`api/course-statuses.json` synchronization for this change set.
