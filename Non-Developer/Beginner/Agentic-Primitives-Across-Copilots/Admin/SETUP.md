# Agentic Primitives - Setup

> **Track:** Non-Developer | **Level:** Beginner

## Required

- A browser and access to the course site.
- Paper or a text editor for the two-surface mapping exercise.
- No product licenses, Azure subscription, organizational data, or connected tools.

The fictional source packet and all exercise instructions are in the
[slide deck](../index.html). The lightweight [Lab Guide](../lab.json) mirrors the
no-code activity for the VS Code extension without opening panels or running
commands. The slides also contain the complete activity for standalone use.

## Present From the Site

Open the course from the Non-Developer beginner catalog. It appears under both
All non-developer courses and the foundations category. Use the arrow keys to
navigate, `N` for speaker notes, and `T` for the table of contents.
Long slides scroll within the course view so tables and speaker notes remain
reachable on small screens.

The shared slide engine loads Mermaid from a CDN for the runtime diagram. Check
network access before presenting; the speaker notes explain the same flow if
the CDN is unavailable.

## Local Development

From the repository root, run `npm run dev`. Open the URL printed by Vite, then
navigate through the catalog to the course. Use the root package dependencies;
there is no course-specific install or build step. GitHub Pages serves the same
relative-path assets without a build.

## Optional Live Demonstration

Use only a product and account already approved by your organization. Paste the
fictional Cedar packet into an existing chat and request a draft. Do not connect
mailboxes, issue trackers, local shell tools, or publishing actions for this
exercise. A written draft and configuration mapping are the complete fallback.

If showing configuration screens, prepare them before class and verify the
actual harness, licensing, tenant policy, and release availability. Scout requires
Frontier preview access and the prerequisites in its
[getting-started guide](https://learn.microsoft.com/en-us/microsoft-scout/get-started).
Foundry provisioning and resource deployment are outside this course.
