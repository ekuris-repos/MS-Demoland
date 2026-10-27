# MCP for You and Me — Content Status

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

- [x] Slide 1 — Title slide
- [x] Slide 2 — Agenda (section divider)
- [x] Slide 3 — Today's Journey (agenda items)
- [x] Slide 4 — What Is MCP? (section divider)
- [x] Slide 5 — The Problem MCP Solves
- [x] Slide 6 — The Model Context Protocol
- [x] Slide 7 — How MCP Works (section divider)
- [x] Slide 8 — The MCP Architecture
- [x] Slide 9 — What MCP Servers Expose
- [x] Slide 10 — Capability Support and Elicitation
- [x] Slide 11 — How Servers Connect
- [x] Slide 12 — Setting It Up (section divider)
- [x] Slide 13 — Enabling the GitHub MCP Server
- [x] Slide 14 — Verifying the Connection
- [x] Slide 15 — Working With Issues (section divider)
- [x] Slide 16 — Reading Issues From Chat
- [x] Slide 17 — Acting on Issues
- [x] Slide 18 — Code Search With MCP
- [x] Slide 19 — Discovering MCP Servers (section divider)
- [x] Slide 20 — The MCP Registry
- [x] Slide 21 — Installing a Registry Server
- [x] Slide 22 — The MCP Ecosystem (section divider)
- [x] Slide 23 — Community MCP Servers
- [x] Slide 24 — Security and Trust (section divider)
- [x] Slide 25 — Securing Your MCP Setup
- [x] Slide 26 — Security Best Practices
- [x] Slide 27 — MCP in Action (demo section divider)
- [x] Slide 28 — Demo: End-to-End Issue Workflow
- [x] Slide 29 — Demo: Combining MCP With Chat
- [x] Slide 30 — Wrap-Up & Next Steps (section divider)
- [x] Slide 31 — Key Takeaways
- [x] Slide 32 — Where to Go Next
- [x] Slide 33 — Closing slide

## Notes

- Slide deck contains 33 slides with nonempty speaker notes; checklist tracks slide authoring, not human approval.
- lab.json created with interactive steps across slides 1, 8, 12, 13, 15, 16, 17, 20, 22, 28.
- Architecture is inline Mermaid. Setup/tool-selection images are contextualized; issue-reading and code-search screenshots remain explicit TODO placeholders.
- Rollup stays "In Progress" until images are added and content is reviewed.

### 2026-10-27 slide-only factual refresh

- Corrected GitHub hosted-server setup and authentication, portable `mcpServers` versus VS Code `servers` schemas, access settings, explicit Agent selection, canonical issue tools, and connection success checks.
- Replaced the archived PostgreSQL runnable example with the maintained GitHub HTTP endpoint. Both JSON examples are alternatives, not instructions to configure duplicate connections.
- Qualified transport/authentication, compatibility, search, logging, approval, and secret-storage claims. Sampling is identified as deprecated in protocol revision 2026-07-28; added safe elicitation and untrusted-content guidance.
- Official sources verified 2026-10-27: [VS Code configuration](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), [setup](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [approvals](https://code.visualstudio.com/docs/agents/run/approvals), [GitHub server](https://github.com/github/github-mcp-server), [issue-tool consolidation](https://github.blog/changelog/2025-10-29-github-mcp-server-now-comes-with-server-instructions-better-tools-and-more/), and [MCP deprecations](https://modelcontextprotocol.io/specification/2026-07-28/deprecated).
- Focused source validation covers slide count/order, notes, JSON schemas, configured endpoint, and slide asset references. No server install, authenticated connection, issue mutation, or browser-render check was performed.
- Remaining blockers: two TODO screenshots, live authenticated workflow verification, slide-scale visual review, and human approval. Reviewed & Approved remains In Progress.
- Labs explicitly excluded: no lab content was opened, changed, or validated. Existing Demo / Lab Content status and historical lab note above are preserved, not re-certified. This is not a full-course approval.
- Final rollup: `In Progress`. The orchestrator owns central `api/course-statuses.json` synchronization for this change set.
