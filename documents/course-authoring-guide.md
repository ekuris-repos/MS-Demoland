# Course Authoring Guide

## Goal

This guide describes the expected workflow for adding or updating a course deck in MS Demoland.

## Standard course structure

Each course should live in a folder under the correct track and level, for example:

- Developer/Beginner/My-Course
- Non-Developer/Enterprise/Another-Course

Inside the course folder, the expected structure is:

- index.html
- Admin/STATUS.md
- img/ (optional)
- .gitignore (optional)
- lab.json (if the course uses lab metadata)

## Starting from the template

When creating a new course:

1. Create the course folder in the right track/level section
2. Copy template.html to the new folder as index.html
3. Copy Templates/Admin/STATUS.md into the new Admin folder
4. Add a matching entry in api/course-statuses.json
5. Add a course card to the root index.html in the correct track and category

## Required status sync

Every course status change must be mirrored in both places:

- the course's Admin/STATUS.md
- the corresponding key in api/course-statuses.json

Allowed values are:

- Not Started
- In Progress
- Ready for Review
- Complete

## Catalog category rule

Each root navigation card should have exactly one category value:

- foundations
- automation
- security

Use the course's primary learning outcome to decide the category. Secondary topics should stay in the description rather than creating multiple category labels.

## Relative path rule

Course pages must use relative asset references. The repo is designed to work in static hosting environments where the site may live at either the root or a subpath.

The pattern is:

- root pages reference css/ and js/ directly
- course pages reference ../../../css/primer-brand.css and similar relative paths

## Deck creation checklist

Before a deck is considered ready:

- slide structure matches the template and guidelines
- title, sections, and summary slides are present
- speaker notes are added where helpful
- images and diagrams are included only when they improve the story
- course status is updated in both the local status file and the JSON registry
- the course card is visible with the right category and track placement

## Review expectation

This repository is highly convention-based. Consistency matters more than novelty. The best decks are the ones that respect the shared structure and review flow so learners get a uniform experience across the catalog.
