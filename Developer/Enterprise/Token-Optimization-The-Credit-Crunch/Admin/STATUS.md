# Token Optimization - The Credit Crunch - Content Status

> **Track:** Developer | **Level:** Enterprise
> **Last Updated:** 2026-06-11

## Rollup Status

<!-- This is the single value shown on the navigation screen.           -->
<!-- Set it to the LOWEST status from the table below.                  -->
<!-- Values: Not Started | In Progress | Ready for Review | Complete    -->

`Status: Ready for Review`

<!-- AGENT SYNC: When changing this status, you MUST also update the matching -->
<!-- entry in api/course-statuses.json so the nav page stays in sync. -->

## Overall Completion

| Area                  | Status           |
|-----------------------|------------------|
| Slide Content         | Ready for Review |
| Speaker Notes         | Ready for Review |
| Images & Diagrams     | Ready for Review |
| Demo / Lab Content    | Ready for Review |
| Reviewed & Approved   | Not Started      |

> **How to update:** Set each area to `Not Started`, `In Progress`, `Ready for Review`, or `Complete`.
> Then set the **Rollup Status** above to the **lowest** value in the table.
> *(Not Started < In Progress < Ready for Review < Complete)*

## Slide-by-Slide Checklist

- [x] Slide 1 - Title slide finalized
- [x] Slide 2 - Overview section divider
- [x] Slide 3 - Agenda: Today's Agenda
- [x] Slide 4 - Part 1 section divider: The Credit Crunch
- [x] Slide 5 - Recap: AI Credits in One Slide
- [x] Slide 6 - Why Optimization Is the Next Frontier
- [x] Slide 7 - What Actually Consumes Tokens (table)
- [x] Slide 8 - The Hidden Cost of Unstructured AI Use (diagram placeholder)
- [x] Slide 9 - Part 2 section divider: Define Workflows First
- [x] Slide 10 - The "Tools Before Workflows" Mistake
- [x] Slide 11 - What Makes a Good AI Workflow
- [x] Slide 12 - Workflows AI Should and Should Not Undertake (table)
- [x] Slide 13 - Mapping and Prioritizing Your Workflows (Mermaid)
- [x] Slide 14 - Anatomy of a Defined Workflow (diagram placeholder)
- [x] Slide 15 - Part 3 section divider: Skills, Instructions, and Agent Personas
- [x] Slide 16 - Three Artifacts That Support a Workflow (table)
- [x] Slide 17 - Instructions: Standing Rules
- [x] Slide 18 - Skills: Packaged Procedures, Loaded on Demand
- [x] Slide 19 - Agent Personas: A Scoped Role With a Tool Set
- [x] Slide 20 - How Artifacts Cut Token Cost (Mermaid)
- [x] Slide 21 - Match the Workflow Signal to the Artifact (table)
- [x] Slide 22 - Part 4 section divider: Token Optimization Techniques
- [x] Slide 23 - Right-Size the Context You Send
- [x] Slide 24 - Reuse Artifacts Instead of Re-Explaining (two-column)
- [x] Slide 25 - Practice Session Hygiene
- [x] Slide 26 - Let Model Routing Match Cost to Complexity
- [x] Slide 27 - See What You Actually Send (debug-mode intro + usage block)
- [x] Slide 28 - Anatomy of the Usage Block (field-by-field table)
- [x] Slide 29 - Why Caching Changes the Math (caching economics)
- [x] Slide 30 - Optimization Has a Floor: Don't Starve the Model (two-column balance)
- [x] Slide 31 - Anti-Patterns That Quietly Burn Credits (table)
- [x] Slide 32 - Measure Workflow Efficiency, Not Just Total Spend (screenshot placeholder)
- [x] Slide 33 - Part 5 section divider: Operationalize Across the Team
- [x] Slide 34 - The Workflow-First Optimization Loop (Mermaid)
- [x] Slide 35 - A 30-Day Workflow Optimization Plan (table)
- [x] Slide 36 - Team Optimization Checklist
- [x] Slide 37 - Summary section divider
- [x] Slide 38 - Key Takeaways
- [x] Slide 39 - Resources
- [x] Slide 40 - Closing slide

## Notes

- Continuation of "Copilot Billing - From PRUs to Usage-Based Billing"; positioned as Part 2 of the billing story with a recap bridge on slide 5.
- Core thesis: define which workflows AI should undertake first, then build complementary skills, instructions, and agent personas that keep those workflows token-efficient.
- `/create-skill` and `/create-agent` are referenced as when-to-use tools (mechanics taught in lower courses); the lab uses both to scaffold artifacts for a dependency migration workflow.
- Three image placeholders remain: unstructured-vs-workflow token cost (slide 8), migration workflow anatomy (slide 14), and token-spend dashboard (slide 32).
- The debug-metadata topic is expanded across three slides: 27 (intro + usage block), 28 (field-by-field anatomy table), and 29 (caching economics, with the clarification that caching is provider-calculated and not user-controllable). All three are code/table-centric, so no screenshots are needed.
- Slide 30 covers the optimization-vs-context balance: under-context drives extra tool calls and more input tokens, so the goal is the cheapest correct answer, not the smallest prompt.
