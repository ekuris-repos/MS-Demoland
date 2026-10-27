# Token Optimization - The Credit Crunch - Content Status

> **Track:** Developer | **Level:** Enterprise
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
| Images & Diagrams     | Ready for Review |
| Demo / Lab Content    | Ready for Review |
| Reviewed & Approved   | In Progress      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 - Title slide finalized
- [x] Slide 2 - Today's Agenda
- [x] Slide 3 - Recap: AI Credits in One Slide
- [x] Slide 4 - Why Optimization Is the Next Frontier
- [x] Slide 5 - What Actually Consumes Tokens (table)
- [x] Slide 6 - The Hidden Cost of Unstructured AI Use (Mermaid)
- [x] Slide 7 - The "Tools Before Workflows" Mistake
- [x] Slide 8 - What Makes a Good AI Workflow
- [x] Slide 9 - Workflows AI Should and Should Not Undertake (table)
- [x] Slide 10 - Anatomy of a Defined Workflow (Mermaid)
- [x] Slide 11 - Three Artifacts That Support a Workflow (table)
- [x] Slide 12 - Instructions: Standing Rules
- [x] Slide 13 - Skills: Packaged Procedures, Loaded on Demand
- [x] Slide 14 - Agent Personas: A Scoped Role With a Tool Set
- [x] Slide 15 - Build the Smallest Sufficient Artifact (table)
- [x] Slide 16 - Right-Size the Context You Send
- [x] Slide 17 - Use Preview CLI Credit Limits With Care
- [x] Slide 18 - Practice Session Hygiene
- [x] Slide 19 - Let Model Routing Match Cost to Complexity (Auto tiers and effort)
- [x] Slide 20 - Measure the Turn and the Session
- [x] Slide 21 - Inspect the Agent With Debug Logs (preview, capture, and data handling)
- [x] Slide 22 - Why Caching Changes the Math
- [x] Slide 23 - Optimization Has a Floor: Don't Starve the Model
- [x] Slide 24 - Anti-Patterns That Quietly Burn Credits (table)
- [x] Slide 25 - Measure Workflow Efficiency, Not Just Total Spend
- [x] Slide 26 - The Workflow-First Optimization Loop (Mermaid)
- [x] Slide 27 - Team Optimization Checklist
- [x] Slide 28 - Key Takeaways
- [x] Slide 29 - Resources
- [x] Slide 30 - Closing slide

## Notes

- Continuation of "Copilot Billing - From PRUs to Usage-Based Billing"; positioned as Part 2 of the billing story with a recap bridge on slide 3.
- Core thesis: define which workflows AI should undertake first, then build complementary skills, instructions, and agent personas that keep those workflows token-efficient.
- Artifact creation uses the target harness's Customizations editor; `/create-skill` remains an optional shortcut where available. No universal `/create-agent` availability is claimed.
- The current deck has 30 slides and three inline Mermaid diagrams. No TODO image references remain; browser rendering and human visual approval are still outstanding.
- Slides 20-22 cover credit measurement, preview Agent Debug Logs capture prerequisites and sensitive data, and provider-dependent caching.
- Slide 23 covers the optimization-vs-context balance: under-context drives extra tool calls and more input tokens, so the goal is the cheapest correct answer, not the smallest prompt.

## Slide-Only Review - 2026-10-27

- Corrected cache-aware routing, active-history/compaction, skill activation, and categorical tool-savings claims. Added Auto tiers, supported-model thinking-effort defaults, deterministic batching, and cost-estimate caveats.
- Qualified preview CLI limits with the documented minimum and soft overshoot. Official sources conflict on session-wide versus per-message reset scope; SDK/background guarantees were removed rather than assumed.
- Added harness-specific debug-capture prerequisites, preview status, and log redaction/retention caveats. Local asset references and notes were checked; no human approval or full-course review is claimed.
- Official sources verified 2026-10-27: [Auto routing](https://docs.github.com/en/copilot/concepts/models/auto-model-selection), [Auto tiers announcement, 2026-09-14](https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection/), [CLI limit guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit), [CLI reference and OpenTelemetry](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference), [model pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), [context management](https://docs.github.com/en/copilot/concepts/prompting-and-context/context-management), [customizations](https://code.visualstudio.com/docs/agent-customization/overview), [skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents), [debug logs](https://code.visualstudio.com/docs/agents/agent-troubleshooting/chat-debug-view), [Cache Explorer](https://code.visualstudio.com/docs/agents/agent-troubleshooting/cache-explorer), and [usage optimization](https://code.visualstudio.com/docs/agents/guides/optimize-usage).
- Remaining blockers: verify preview limit semantics on the approved client; browser/diagram layout review and human approval remain outstanding. Labs were explicitly excluded and their status values were preserved without validation.
- Rollup is **In Progress**, the lowest area status. Catalog JSON synchronization is owned by the orchestrator and intentionally not performed by this course worker.
