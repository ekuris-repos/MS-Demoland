# Agent Potato License to Chat — Content Status

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

| Area                  | Status      |
|-----------------------|-------------|
| Slide Content         | In Progress |
| Speaker Notes         | Complete    |
| Images & Diagrams     | In Progress |
| Demo / Lab Content    | In Progress |
| Reviewed & Approved   | In Progress |

> **How to update:** Set each area to `Not Started`, `In Progress`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Title slide
- [x] Slide 2 — Today's Mission
- [x] Slide 3 — Mission Briefing
- [x] Slide 4 — Reconnaissance section divider
- [x] Slide 5 — OctoCAT Supply: Verify Before Building
- [x] Slide 6 — Exploring With Agent Mode
- [x] Slide 7 — Agent Mode Deep Dive section divider
- [x] Slide 8 — Tools Available to Agent Mode
- [x] Slide 9 — Approval Gates and Control
- [x] Slide 10 — The Agent Picker section divider
- [x] Slide 11 — Three Agents, Three Jobs
- [x] Slide 12 — Preparing the Mission section divider
- [x] Slide 13 — Instructions Shape Every Response
- [x] Slide 14 — Instructions for OctoCAT Supply
- [x] Slide 15 — Building the Feature section divider
- [x] Slide 16 — Writing a Good Agent Prompt
- [x] Slide 17 — Building the Frontend
- [x] Slide 18 — Parallelizing Agent Work
- [x] Slide 19 — Quality Assurance section divider
- [x] Slide 20 — Testing With Agent Mode
- [x] Slide 21 — Iterative Refinement
- [x] Slide 22 — Multi-File Workflows section divider
- [x] Slide 23 — Cross-Stack Changes
- [x] Slide 24 — When Agent Mode Struggles
- [x] Slide 25 — Prompt Files for Common Tasks
- [x] Slide 26 — Mission Debrief: The Solution
- [x] Slide 27 — Debrief section divider
- [x] Slide 28 — How Did Your Mission Go?
- [x] Slide 29 — Where to Go Next
- [x] Slide 30 — Closing slide

## Notes

- Slide-only editorial pass complete (30 slides with speaker notes); runnable feature delivery remains unverified.
- Lab guide (lab.json) created with interactive exercises mapped to slides
- Lab repo: msft-common-demos/octocat_supply-ubiquitous-octo-bassoon
- 2026-10-27 slide-only review: corrected Copilot versus Local harness compatibility, approval labels and command rules, prompt-file and `/init` scope, MCP destinations, worktree caveats, validation criteria, and spoken narration. Added contract-first API/component testing and a browser smoke-check prompt; removed invented sample paths, dependency assertions, and unsupported throughput guarantees.
- Official sources checked 2026-10-27: [harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [approvals](https://code.visualstudio.com/docs/agents/run/approvals), [assisted permissions GA, 2026-10-26](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available/), [instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions), [prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files), [MCP configuration](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), and [Git worktrees](https://git-scm.com/docs/git-worktree).
- Blocker: the original sample repository and public main/master README URLs returned 404. No replacement was fabricated. Its revision, schema, dependencies, commands, and working feature remain UNVERIFIED; the slides now state that limitation explicitly.
- Media: shared asset references resolve; role/harness and debrief tables plus the existing Mermaid loop avoid unnecessary screenshot placeholders. Visual acceptance remains In Progress.
- Focused validation: balanced HTML, 30 preserved slide sections/implicit anchors, 30 nonempty directive-free notes without em/en dashes, four resolved local asset references, approval JSON, optional prompt frontmatter, and unchanged lab metadata passed. A browser pass checked 30 distinct slide titles and the condensed debrief; the agent-picker slide was shortened after an excess-height finding. Final cross-viewport acceptance remains blocked by browser-session failures; the shared external font also failed to load.
- This is not human approval or a full-course review. All lab content was excluded and existing lab status values remain unchanged. Reviewed & Approved and overall rollup remain In Progress.
