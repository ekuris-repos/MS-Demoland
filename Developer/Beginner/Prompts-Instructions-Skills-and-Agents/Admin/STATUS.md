# Copilot Primitives - Prompts, Instructions, Skills, Hooks, and Agents — Content Status

> **Track:** Developer | **Level:** Beginner
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
| Slide Content         | Complete    |
| Speaker Notes         | Complete    |
| Images & Diagrams     | In Progress |
| Demo / Lab Content    | Complete    |
| Reviewed & Approved   | In Progress |

> **How to update:** Set each area to `Not Started`, `In Progress`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 — Copilot Primitives - Prompts, Instructions, Skills, Hooks, and Agents
- [x] Slide 2 — What We'll Cover
- [x] Slide 3 — Today's Journey
- [x] Slide 4 — The Building Blocks
- [x] Slide 5 — Four Building Blocks
- [x] Slide 6 — Where They Live in Your Repo
- [x] Slide 7 — Prompt Files
- [x] Slide 8 — What Is a Prompt File?
- [x] Slide 9 — Anatomy of a Prompt File
- [x] Slide 10 — Running & Sharing Prompts
- [x] Slide 11 — Instruction Files
- [x] Slide 12 — What Are Instruction Files?
- [x] Slide 13 — Repo-Wide: copilot-instructions.md
- [x] Slide 14 — Scoped: .instructions.md Files
- [x] Slide 15 — Skills
- [x] Slide 16 — What Is a Skill?
- [x] Slide 17 — Anatomy of a SKILL.md
- [x] Slide 18 — How Skills Load
- [x] Slide 19 — Agent Hooks
- [x] Slide 20 — What Is an Agent Hook?
- [x] Slide 21 — Hook Lifecycle Events
- [x] Slide 22 — Anatomy of a Workspace Hook
- [x] Slide 23 — Hook Execution Flow
- [x] Slide 24 — Hooks Are Executable Automation
- [x] Slide 25 — When to Use What
- [x] Slide 26 — How They Work Together
- [x] Slide 27 — These Four Are Not the Whole Platform
- [x] Slide 28 — Wrap-Up & Next Steps
- [x] Slide 29 — Key Takeaways
- [x] Slide 30 — Where to Go Next

## Notes

- Slide 10 retains an older general slash-menu screenshot, explicitly labeled as illustrative. TODO: capture a current Local session showing a course prompt; media remains In Progress.
- Lab content (lab.json) created with 15 steps across 9 slide anchors
- Old course "Prompts-Instructions-Agents-and-Chats" has been removed; this is the replacement

### Slide-only factual refresh: 2026-10-27

- Preserved and integrated the existing slide and status edits. Kept all 30 slides and their positional anchors.
- Corrected Local-only prompt invocation versus Copilot skill/hook composition. Removed the unsupported current-file interpolation and azd version floor, aligned test naming guidance, and added discovery/execution checks and the Node.js execution-host prerequisite.
- Official sources checked: [VS Code prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files), [customization migration](https://code.visualstudio.com/docs/agent-customization/migrate-customizations), [instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions), [skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [hooks](https://code.visualstudio.com/docs/agent-customization/hooks), [Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference), and [azd reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference). Verification date: 2026-10-27.
- Remaining blockers: real screenshot recapture, live VS Code prompt/skill/hook verification and browser/media rendering review. Examples were checked statically, not executed or deployed. Human approval is outstanding; Reviewed & Approved remains In Progress.
- Labs explicitly excluded: no lab content was read, reviewed, validated or changed. Existing lab status values and notes are preserved, not re-certified. This is not a full-course approval.
- Rollup remains In Progress. Catalog status synchronization is reserved for the orchestrator in this change set.
