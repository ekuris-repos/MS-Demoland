# Enterprise Grade Marmalade — Content Status

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
| Demo / Lab Content    | Not Applicable   |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Title slide (badge, title, subtitle, speaker notes)
- [x] Slide 2 — Agenda section divider
- [x] Slide 3 — Agenda items with full topic list and speaker notes
- [x] Slide 4 — Section divider: The Problem
- [x] Slide 5 — The Consistency Challenge (5 bullet points, speaker notes)
- [x] Slide 6 — What Goes Wrong Without Standards (4 cards, speaker notes)
- [x] Slide 7 — Section divider: Central Prompt Repositories
- [x] Slide 8 — What Is a Central Prompt Repository? (6 bullets, speaker notes)
- [x] Slide 9 — The Four File Types (4 cards, speaker notes)
- [x] Slide 10 — Section divider: Organizing Your Repository
- [x] Slide 11 — Recommended Folder Structure (code block, speaker notes)
- [x] Slide 12 — Naming Conventions and Best Practices (6 bullets, speaker notes)
- [x] Slide 13 — Section divider: Distribution Models
- [x] Slide 14 — Distribution: Git Submodules & npm (2 cards with code, speaker notes)
- [x] Slide 15 — Distribution: Symlinks & Copy-on-Clone (2 cards with code, speaker notes)
- [x] Slide 16 — Choosing the Right Distribution Model (comparison table, speaker notes)
- [x] Slide 17 — Section divider: Governance
- [x] Slide 18 — Ownership and Maintenance (5 bullets + CODEOWNERS code, speaker notes)
- [x] Slide 19 — PR Review Process and Versioning (5 bullets, speaker notes)
- [x] Slide 20 — Section divider: Template Patterns
- [x] Slide 21 — Standard Prompt Templates: Code Review (full example, speaker notes)
- [x] Slide 22 — More Templates: Test Generation & Documentation (2 cards, speaker notes)
- [x] Slide 23 — Migration Assistant Template (full example, speaker notes)
- [x] Slide 24 — Section divider: Scoped Instructions at Scale
- [x] Slide 25 — Language and Framework Instructions (TypeScript + React examples, speaker notes)
- [x] Slide 26 — API Design and Architecture Instructions (.NET example, speaker notes)
- [x] Slide 27 — Section divider: Skills & Agents
- [x] Slide 28 — Skills as Institutional Knowledge (deployment pipeline SKILL.md, speaker notes)
- [x] Slide 29 — Agents as Team Roles: Security Reviewer (full example, speaker notes)
- [x] Slide 30 — More Agent Examples: DevOps & Migration (2 cards, speaker notes)
- [x] Slide 31 — Onboarding Acceleration (5 bullets, speaker notes)
- [x] Slide 32 — Measuring Effectiveness (6 bullets, speaker notes)
- [x] Slide 33 — CI/CD Integration (4 bullets + workflow code, speaker notes)
- [x] Slide 34 — Section divider: Summary
- [x] Slide 35 — Key Takeaways (8 bullets, speaker notes)
- [x] Slide 36 — Getting Started Checklist (8 items, speaker notes)
- [x] Slide 37 — Closing slide (Thank You, speaker notes)

## Notes

### 2026-10-27 — Slide-only factual refresh

All 37 slides and nonempty speaker notes retained. Corrected native discovery
paths, Local versus Copilot harness support, skill metadata, symlink resolution,
submodule update semantics, CODEOWNERS enforcement prerequisites, supported Node
runtime guidance, coherent .NET examples, and measurement/guarantee claims.
The `ccpr_root` name now labels an illustrative structure; no public template
provenance is asserted. Added a concise native-sharing/plugin comparison and
discovery/evaluation checks. The workflow is explicitly a scaffold requiring
team-owned validation scripts, not supplied runnable tooling.

Official sources checked on 2026-10-27:
- [VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions),
  [prompt migration](https://code.visualstudio.com/docs/agent-customization/migrate-customizations),
  [skills](https://code.visualstudio.com/docs/agent-customization/agent-skills),
  and [plugins](https://code.visualstudio.com/docs/agent-customization/agent-plugins).
- [Git submodules](https://git-scm.com/docs/git-submodule) and
  [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- [Node release status](https://nodejs.org/en/about/previous-releases),
  [checkout](https://github.com/actions/checkout), and
  [setup-node](https://github.com/actions/setup-node).
- [ASP.NET Core responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses?view=aspnetcore-10.0)
  and [authorization](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/security?view=aspnetcore-10.0).

Static slide checks passed; no human approval is claimed. Remaining blockers:
browser/layout and Mermaid rendering review; real-client discovery, invocation
and permissions testing; team-owned validator implementation; and an approved
public template reference if one is later required. Images & Diagrams is
applicable because slide 5 contains Mermaid, but rendering remains unverified.
The existing server loaded the 37-slide deck, but the browser session became
unavailable before detailed checks; a shared external font also returned HTTP
404. Shared font configuration is outside this course-only refresh.
Labs were excluded, and all existing lab status values were preserved verbatim.
This is not a full-course or lab approval. Final rollup: **In Progress**.
The orchestrator owns catalog JSON synchronization for this change set.
