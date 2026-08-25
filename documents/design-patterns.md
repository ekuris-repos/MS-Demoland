# Design Patterns in the Repository

## 1. Shared shell with local content

The repository uses a composition pattern: the root catalog and shared CSS/JS provide a consistent experience, while each course adds only its own page content.

This reduces duplication and makes update work centralized. Example files:

- index.html
- template.html
- js/slides.js
- css/primer-brand.css

## 2. Template-driven course authoring

New decks are created from a known starting point rather than from scratch. The repo expects a template HTML and role-specific status structure.

The standard pattern is:

- copy template.html into a new course folder as index.html
- copy Templates/Admin/STATUS.md into that course's Admin folder
- add the course card to the root catalog
- add the status entry to api/course-statuses.json

This keeps the training content style and review process consistent across many courses.

## 3. Status mirroring pattern

The repository intentionally stores the same status in two places:

- the course's Admin/STATUS.md file
- the root api/course-statuses.json registry

This reflects an operational principle: the course's local record is the source for content review, while the catalog depends on the JSON to render status values in the navigation page.

The status scale is intentionally limited:

- Not Started
- In Progress
- Ready for Review
- Complete

## 4. Manual catalog registry pattern

The navigation page is static and driven by hand-maintained data rather than a dynamic backend.

Because of this, course creation involves multiple related updates:

- folder creation
- new deck file
- status file
- status registry entry
- navigation card in index.html

This is a human-managed registry pattern, not a database-backed content system.

## 5. Relative-path portability pattern

The repo is designed to work under GitHub Pages and local static serving. To achieve that, all page references use relative paths instead of root-absolute URLs.

This matters because the same repo may be served from:

- / on localhost
- /MS-Demoland/ on GitHub Pages

The design pattern is simple but important: keep links relative and avoid hard-coded absolute root references.

## 6. Presentation-first structure

Each slide deck is authored as a long sequence of section elements in HTML. The structure supports narrative delivery with slide-level speaker notes, cards, diagrams, and code blocks.

This gives instructors and presenters a content-first presentation mode while still allowing the deck to be used as a digital experience.

## 7. Filtered navigation model

The root catalog uses tabs for audience track and category. Each course card carries a data-category value that controls filtering.

Supported categories include:

- foundations
- automation
- security

This design gives the site a strong browse-by-competency model without introducing a backend or search engine.

## 8. Minimal automation, high convention discipline

This repo favors simple, explicit workflow steps over automation. The site is static, there is no build step beyond local Vite serving, and the main correctness guardrail is manual synchronization discipline.

That makes the repository easy to understand but also means documentation and process are important.

## 9. Speaker note and content layering

Each slide can include a speaker-notes block that sits beneath the visible slide content. This is an explicit teaching pattern that enables two information layers:

- the visible deck content for learners
- the presenter guidance for teaching context

This layering is part of the repository's educational design philosophy.

## 10. Documented operational risk

The biggest design risk in the repo is drift between content and metadata. Because status data is duplicated and the catalog is static, every change must be reviewed for consistency.

This is exactly why documentation and process notes are valuable in this repo.
