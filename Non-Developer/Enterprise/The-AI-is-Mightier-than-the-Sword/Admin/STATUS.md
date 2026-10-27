# The AI is Mightier than the Sword — Content Status

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

- [x] Slides 1-6 — Scope and single-agent baseline qualified; unsupported superiority claims removed
- [x] Slides 7-10 — Research patterns corrected; optional subagent delegation and operating limits explained
- [x] Slides 11-14 — Agent picker guidance, multiline YAML, read-only starter, and role names corrected
- [x] Slides 15-18 — Evidence contract, fresh-chat guidance, shared-workspace caveat, and fair comparisons refreshed
- [x] Slides 19-22 — Retired GitHub App-based integration advice replaced with approved MCP and enterprise safeguards
- [x] Slides 23-25 — Correlated-error caveat, source checks, uncertainty, and stop conditions strengthened
- [x] Slides 26-31 — Use cases, getting-started steps, and takeaways aligned with corrected workflows
- [ ] Slide 12 — Capture a current research-agent/picker screenshot; existing code-review file image is explicitly illustrative
- [ ] Delivery verification — Confirm agent discovery, selected tools, fresh-chat controls, and an approved read-only MCP call
- [ ] Human slide approval — Pending; automated factual refresh is not approval

## Notes

### 2026-10-27 — Slide-only factual refresh

Reviewed and refreshed all 31 slide sections and their speaker notes. Corrected the retired GitHub App-based Copilot Extensions pathway, custom-agent selection, malformed YAML, delegation restrictions, MCP configuration guidance, and source-verification claims. Added approved-source boundaries, least-privilege access, untrusted-content handling, evidence provenance, and operating limits. Slide order, layout classes, navigation, shared-asset paths, and existing anchors were preserved.

Official sources checked:
- [GitHub sunset notice, 2025-09-24](https://github.blog/changelog/2025-09-24-deprecate-github-copilot-extensions-github-apps/) — GitHub App-based Extensions sunset November 10, 2025; client-side VS Code extensions are unaffected.
- [VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) and [file reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference) — Agent dropdown, repository location, multiline syntax, and harness-dependent tools.
- [VS Code subagents](https://code.visualstudio.com/docs/agents/run/subagents) and [session management](https://code.visualstudio.com/docs/agents/run/sessions/manage-sessions) — Bounded delegation and separate conversations versus shared files.
- [MCP setup](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), and [security guidance](https://code.visualstudio.com/docs/agents/run/security) — Approved connections, configuration formats, trust, and approvals.

Focused static validation passed for 31 slides/notes, structure, preserved identifiers, local assets, YAML parsing, and stale-claim checks. An initial browser smoke check loaded slide 13 at its existing hash with 31 slides, 31 notes, the multiline example, all images loaded, and no captured JavaScript exceptions. Full viewport/diagram interaction checks were incomplete: browser controls were not interactable and the browser page later became unavailable; an external font request also failed. Delivery-environment UI/tool checks remain unverified. The read/search example is explicitly workspace-only; external retrieval requires separately approved and tested tools. The existing slide 12 screenshot remains an illustrative code-review file, not a current research workflow capture. Human approval is pending.

**Labs excluded:** No lab content was opened, reviewed, changed, or validated. All existing lab status entries are preserved exactly. This is not a full-course approval. Rollup remains **In Progress**, limited by unresolved media/delivery verification and approval. The orchestrator owns catalog JSON synchronization for this change set.
