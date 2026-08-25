# Repository Documentation

This folder captures the recurring conventions, patterns, and operational knowledge for the MS Demoland course site.

## Purpose

MS Demoland is a static slide-deck catalog for GitHub Copilot and AI learning experiences. The repository is intentionally flat: shared assets live at the repo root, while individual course decks live under the Developer and Non-Developer tracks.

## Document Index

- [repository-overview.md](repository-overview.md) - architecture and repo layout
- [design-patterns.md](design-patterns.md) - reusable implementation patterns and conventions
- [course-authoring-guide.md](course-authoring-guide.md) - how to add or update a course deck

## Core repo facts

- Site root is the published GitHub Pages root
- Shared assets are in css/, js/, img/, and api/
- Course decks live under Developer/ and Non-Developer/
- Each course is a self-contained folder with index.html, lab.json, and optional image assets
- Status data is tracked manually in api/course-statuses.json and mirrored in each course Admin/STATUS.md

## Why this folder exists

The repository has strong repeatable patterns but a lot of the knowledge is spread across:

- the root index.html catalog
- template.html for slide structure
- js/slides.js for navigation behavior
- each course Admin/STATUS.md file
- repository instructions and site conventions

This folder centralizes the key information so future work can be faster and more consistent.
