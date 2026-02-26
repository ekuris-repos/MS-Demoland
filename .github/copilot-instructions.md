# Copilot Instructions — MS Demoland

## Repository structure

This is a course slide-deck site with a flat layout — shared assets (`css/`,
`js/`, `img/`, `api/`, `index.html`) live at the **repo root** alongside the
course directories. Course content lives under `Developer/` and `Non-Developer/`,
organized by level (`Beginner`, `Intermediate`, `Enterprise`, `Add-Ons`).

The `Templates/` folder contains only admin files (`Admin/`, `README.md`). The
slide deck template is `template.html` at the repo root.

## Course status — KEEP IN SYNC

Every course folder has an `Admin/STATUS.md` file with a rollup status value:

```
`Status: Not Started`   or   `Status: In Progress`   or   `Status: Ready for Review`   or   `Status: Complete`
```

The navigation page (`index.html`) reads statuses from a **static JSON file** at
`api/course-statuses.json`. This file is NOT auto-generated — it must be updated
manually whenever a course status changes.

### Rule: When you change a STATUS.md, you MUST also update course-statuses.json

The JSON key is the course path relative to the repo root, without the
`Admin/STATUS.md` suffix. For example:

| STATUS.md location | JSON key |
|---|---|
| `Developer/Beginner/MCP-for-You-and-Me/Admin/STATUS.md` | `Developer/Beginner/MCP-for-You-and-Me` |
| `Non-Developer/Enterprise/Proving-Trust-in-the-System/Admin/STATUS.md` | `Non-Developer/Enterprise/Proving-Trust-in-the-System` |

Allowed values: `Not Started`, `In Progress`, `Ready for Review`, `Complete`

**Both files must always agree.** If you update one, update the other in the
same commit/change set.

### Rule: When you add a new course folder

1. Create the course folder under the correct track and level.
2. Copy `template.html` as the starting slide deck (`index.html`).
3. Copy `Templates/Admin/STATUS.md` as the starting status file.
4. Add a new entry to `api/course-statuses.json`.
5. Add a course card to `index.html` in the appropriate track/level section.

## GitHub Pages

This site is designed to run on GitHub Pages as a static site — no build step
required. The repo root IS the site root. Deploy from branch → `master` → `/ (root)`.

All HTML files use **relative paths** (not root-absolute) so the site works
whether served at `/` (local dev) or at a subpath like `/MS-Demoland/` (GitHub Pages).

- Root files (`index.html`, `template.html`): `css/primer-brand.css`, `js/slides.js`, `img/ms-github-logo.svg`
- Course files (3 levels deep): `../../../css/primer-brand.css`, `../../../js/slides.js`, `../../../img/ms-github-logo.svg`

## Style guide

See `/memories/repo/style-guide.md` for writing conventions (e.g. em dash usage).

## Commit and push

Always commit **and push** in the same operation. Never leave committed changes
unpushed.

## Local development

Run `npm run dev` from the repo root to start the Vite dev server. Everything
is served from the flat directory structure — no plugins needed.
