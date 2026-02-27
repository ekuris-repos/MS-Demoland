---
applyTo: "{Developer,Non-Developer}/**/index.html"
---

# Slide Image Placeholders

When generating or expanding course slide decks, insert placeholder `<img>` tags
on slides where a visual would meaningfully aid comprehension. The placeholder
renders as a **broken image link**, making it immediately visible to testers,
reviewers, and other agents so the needed asset can be created later.

## When to add an image placeholder

**YES — image helps:**

- Architecture or flow diagrams
- UI screenshots for demos and walkthroughs
- Dashboard or metrics visuals
- Process illustrations
- Before/after comparisons

**NO — image does not help:**

- Code-centric slides (the code IS the visual)
- Self-sufficient bullet lists
- Agenda, takeaway, or next-steps slides
- Card-based comparisons (the cards are already visual)
- Definition or concept text slides

## Naming convention

| Type | Pattern | Example |
|---|---|---|
| UI screenshot | `img/TODO-screenshot-{slug}.png` | `img/TODO-screenshot-setting-up-copilot-in-teams.png` |
| Architecture / flow diagram | `img/TODO-diagram-{slug}.png` | `img/TODO-diagram-agent-orchestration-flow.png` |

- `{slug}` is a lowercase, hyphenated description derived from the slide title
  or the visual's subject.
- All placeholders live in the course's local `img/` directory.

## Markup

```html
<img src="img/TODO-diagram-{slug}.png" alt="TODO: Add diagram for &quot;Slide Title or Description&quot;" />
```

### Rules

1. Use a self-closing `<img … />` tag.
2. The `src` must point to a nonexistent file so it renders as a broken image.
3. The `alt` text must start with `TODO:` followed by `Add screenshot for` or
   `Add diagram for` and a quoted description of what the image should show.
   Escape inner quotes with `&quot;`.
4. Place the `<img>` **after** the slide's text/list content and **before** the
   `<aside class="speaker-notes">` block.
5. Follow the `<img>` with a blank line for readability.
6. Do **not** wrap the image in a `<figure>`, `<div>`, or `<p>` tag.

## Full example

```html
<section>
  <h2>How the Agent Orchestrator Works</h2>
  <ul>
    <li>Receives task from the user</li>
    <li>Decomposes into sub-tasks</li>
    <li>Routes each sub-task to the best-fit agent</li>
    <li>Aggregates results and responds</li>
  </ul>
  <img src="img/TODO-diagram-agent-orchestrator-flow.png" alt="TODO: Add diagram for &quot;How the Agent Orchestrator Works&quot;" />

  <aside class="speaker-notes">
    The orchestrator acts as a central router …
  </aside>
</section>
```
