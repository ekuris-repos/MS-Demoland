# Repository Overview

## Project purpose

This repository publishes a collection of interactive slide decks for developer and non-developer learning tracks. The content is organized as a course catalog with a landing page, level-based grouping, and per-course slides.

## High-level structure

- Root files: static site shell and shared assets
- Developer/: technical learning tracks
- Non-Developer/: business and executive learning tracks
- Single Sessions/: standalone deck packages
- Templates/: admin and starter templates
- api/: runtime metadata such as course statuses and training profile data
- css/ and js/: shared styling and deck behavior
- img/: shared images and branding assets

## Shared asset model

The website is intentionally simple and static:

- The root index.html acts as the catalog and navigation hub
- Each course uses a local index.html for its slide deck
- All deck pages use relative paths so the site works at root and in a GitHub Pages subpath
- The global CSS and JS are shared, which keeps course content visually consistent and reduces duplication

## Deck runtime behavior

The slide engine in js/slides.js provides:

- previous/next navigation
- hash-based slide jumps
- keyboard support
- progress indicator
- table of contents overlay
- speaker notes toggling
- optional Mermaid rendering when diagrams exist

This makes the content usable both as a presentation and as an in-browser guided experience.

## Course metadata model

Each course is expected to have:

- a course folder with an index.html deck
- an Admin/STATUS.md file with the rollup status
- a matching api/course-statuses.json entry
- a course card in the root index.html catalog

The status flow is manually kept in sync. This is a deliberate pattern because the site is static and not generated from CMS data.

## Notable documentable items in the repo

1. Root catalog and filter model
2. Shared slide shell and deck engine
3. Per-course folder authoring conventions
4. Status synchronization conventions
5. Relative path strategy for GitHub Pages compatibility
6. Course categorization model for foundations, automation, and security

## Operational observations

- The site is a static architecture, not a framework app
- Most authoring is template-based rather than code-generated
- Presentation consistency is preserved by shared styling and shared deck components
- Course creation is mostly a convention-heavy workflow rather than a runtime pipeline
