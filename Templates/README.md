# Primer Brand – Course Slide Deck Template

A reusable template for building web-viewable courses styled with [GitHub Primer Brand](https://primer.style/brand/) design tokens.

## Quick Start

```bash
# 1. Copy this template into a new course folder
cp -r Templates/ ../my-course-name/
cd ../my-course-name/

# 2. Install dependencies
npm install

# 3. Start the dev server (hot-reload)
npm run dev

# 4. Build for production
npm run build       # → outputs to dist/
npm run preview     # preview the build locally
```

## Project Structure

```
├── index.html            ← Your course (edit this)
├── css/
│   └── primer-brand.css  ← Primer Brand theme & slide layout
├── js/
│   └── slides.js         ← Navigation engine (keyboard, touch, buttons)
├── package.json
├── vite.config.js
└── README.md
```

## Creating a New Course

1. **Copy** the `Templates/` folder to a sibling directory:
   ```
   MS Demoland/
     Templates/          ← this repo (don't edit directly)
     Azure-Fundamentals/ ← your new course
     DevOps-Pipelines/   ← another course
   ```

2. **Edit** `index.html` – each `<section class="slide">` is one slide.

3. **Pick a slide variant** by adding a class:

   | Class | Purpose |
   |---|---|
   | `slide--title` | Dark hero slide (course title, closing) |
   | `slide--section` | Light blue section divider |
   | `slide--content` | Default content slide |

4. **Use layouts** inside `.slide-inner`:
   - Single column: just write your content
   - Two columns: wrap in `<div class="columns">…</div>`
   - Cards: wrap groups in `<div class="card">…</div>`

## Catalog Categorisation

Every course appears under either the **Developer** or **Non-Developer** track
and keeps its learning level (`Beginner`, `Intermediate`, `Enterprise`, or
`Add-Ons`). The catalog also assigns each course to one GitHub capability
section. This second classification helps learners find related courses
without duplicating course cards.

| Catalog section | Assign courses here when the primary focus is... |
|---|---|
| **GitHub foundations** | GitHub platform concepts, repositories, collaboration, Copilot fundamentals, prompts, MCP, SDKs, APIs, or project workflows |
| **Automation and delivery** | GitHub Actions, Coding Agent, Copilot CLI, agent orchestration, CI/CD, deployment pipelines, or Azure DevOps integration |
| **Security and governance** | Code review, CodeQL, code scanning, Dependabot, secret scanning, Copilot governance, billing controls, or usage and token optimization |

The catalog also provides an **All courses** view. Assign a course to the one
section that best matches its main learning outcome. Do not create a new
section for a secondary topic. When a course genuinely spans multiple areas,
choose the section that matches the hands-on task and mention the supporting
topics in the course description.

When adding a course, update all of these locations:

1. Add the course card to the appropriate track and level in the root
   `index.html`.
2. Add `data-category="foundations"`, `data-category="automation"`, or
   `data-category="security"` to the card. The `all` value is reserved for
   the catalog tab controls.
3. Keep the course status synchronized between `Admin/STATUS.md` and
   `api/course-statuses.json`.
4. Verify that the course appears in the expected category tab and in the
   **All courses** view.

## Navigation

| Action | Input |
|---|---|
| Next slide | → arrow, Space, or click ▶ |
| Previous slide | ← arrow or click ◀ |
| Jump to slide | Press **T** for table of contents |
| First / Last | Home / End |
| Swipe | Touch left/right on mobile |
| Direct link | `#slide-3` in the URL |

## Git Workflow

```bash
# In your new course folder:
git init
git add .
git commit -m "Initial course scaffold"
git remote add origin https://github.com/ekuris-repos/my-course-name.git
git push -u origin main
```

## Customisation

- **Colors**: edit CSS custom properties in `css/primer-brand.css` under `:root`
- **Fonts**: Mona Sans loads from GitHub's CDN; swap the `@font-face` if needed
- **Print**: `Ctrl+P` renders all slides sequentially (nav chrome hidden)

## License

Internal use — Microsoft Demoland.
