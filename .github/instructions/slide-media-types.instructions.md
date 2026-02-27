---
applyTo: "{Developer,Non-Developer}/**/index.html"
---

# Slide Media Types

Course slide decks are overwhelmingly bullet lists. When generating or expanding
slides, **use the richest media type you can generate inline** before falling
back to an image placeholder that requires a separate asset. The goal is to
minimize the number of TODO image requests while maximizing visual variety.

## Decision ladder

Work through these options top-to-bottom. Use the **first** type that fits the
content:

| Priority | Media type | Can you generate it inline? | When to use it |
|---|---|---|---|
| 1 | **HTML `<table>`** | Yes — generate the markup | Comparing 3+ items across 2+ attributes |
| 2 | **Mermaid diagram** | Yes — generate the fenced block | Linear flows, trees, sequences, state machines, ER diagrams |
| 3 | **CSS-only chart** | Yes — generate the markup + inline styles | Simple bar comparisons with ≤ 8 items and known values |
| 4 | **Image placeholder** | No — produces a broken-image TODO | Screenshots, rich infographics, complex annotated visuals |

> **Rule of thumb**: if you can express the visual in HTML/CSS/Mermaid and it
> renders acceptably at slide scale, generate it. Only request an image when the
> visual *cannot* be approximated with markup.

---

## 1. HTML tables

### When to use

- Feature/tool comparison matrices (3+ rows, 2+ columns)
- Side-by-side attribute grids (plan tiers, tool trade-offs, metric definitions)
- Data that has a clear header row and uniform structure

### When NOT to use

- Two-item comparisons — use a `columns` + `card` layout instead
- Narrative content that happens to have colons — keep as a list
- Data with only one attribute per row — a `<ul>` is simpler

### Markup

Use a plain `<table>` with `<thead>` and `<tbody>`. The stylesheet will inherit
base sizing from `primer-brand.css`. Add no classes; keep it semantic.

```html
<table>
  <thead>
    <tr>
      <th>Plan</th>
      <th>Seats</th>
      <th>Premium Requests</th>
      <th>Key Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Free</td>
      <td>1</td>
      <td>50/mo</td>
      <td>Completions, Chat, CLI</td>
    </tr>
    <tr>
      <td>Pro</td>
      <td>1</td>
      <td>Unlimited standard</td>
      <td>+ Unlimited completions, agent mode</td>
    </tr>
  </tbody>
</table>
```

### Placement rules

1. Replace the bullet list, card set, or columns layout it supersedes — do not
   keep both.
2. Position the table after the `<h2>` and any introductory `<p>`, **before**
   `<aside class="speaker-notes">`.
3. Keep tables ≤ 6 columns so content remains legible at slide scale.
4. Use `<code>` for inline commands/paths inside cells where appropriate.

---

## 2. Mermaid diagrams

### When to use

- Linear process flows (≤ 10 nodes)
- Sequence diagrams (≤ 6 participants)
- State machines and lifecycle diagrams
- Simple tree/hierarchy diagrams (≤ 3 levels)
- Entity-relationship diagrams

### When NOT to use

- Visuals that require pixel-precision layout, annotations, or brand artwork —
  use an image placeholder
- Screenshots of UI — obviously not generatable
- Diagrams with > 12 nodes or heavy cross-linking — readability suffers; use an
  image placeholder instead
- Diagrams that need custom icons, colors, or callout boxes beyond Mermaid's
  built-in styling

### Markup

Wrap the Mermaid definition in a `<pre class="mermaid">` block. The slide deck
loads the Mermaid library at runtime; no build step is required.

```html
<pre class="mermaid">
graph LR
  A[User types code] --> B[Context gathered]
  B --> C[Sent to LLM]
  C --> D[Suggestion returned]
  D --> E{Accept?}
  E -->|Tab| F[Code inserted]
  E -->|Esc| A
</pre>
```

### Supported diagram types

| Mermaid type | Slide use case |
|---|---|
| `graph LR` / `graph TD` | Architecture flows, process steps |
| `sequenceDiagram` | API call sequences, auth flows, agent handoffs |
| `stateDiagram-v2` | Lifecycle states (PR states, agent states) |
| `erDiagram` | Data model relationships |
| `pie` | Proportion breakdowns (≤ 6 slices) |
| `gantt` | Timeline / phased rollout plans |

### Placement rules

1. The `<pre class="mermaid">` block replaces a bullet list or supplements it —
   never duplicate the same information in both a list and a diagram.
2. Position after text content and before `<aside class="speaker-notes">`.
3. Indent the Mermaid source at the same depth as surrounding slide content
   (8 spaces inside `<div class="slide-inner">`).
4. Keep labels short (≤ 5 words per node) for readability at slide scale.
5. Prefer `graph LR` (left to right) for flows; `graph TD` (top down) for
   hierarchies.

### Mermaid vs. image placeholder: choosing

| Content | Use Mermaid | Use image placeholder |
|---|---|---|
| 4-step linear flow | Yes | No |
| Auth sequence with 3 actors | Yes | No |
| Full enterprise network topology | No | Yes — too complex |
| UI screenshot of a dashboard | No | Yes — not diagrammable |
| Agent loop (Observe → Think → Act) | Yes | No |
| Annotated screenshot with callouts | No | Yes |

---

## 3. CSS-only bar charts

### When to use

- Simple comparisons of ≤ 8 numeric values where the relative sizes tell the
  story (e.g., "time saved per task," "adoption by team," "suggestions by
  language")
- The values are known or representative — you are embedding them directly

### When NOT to use

- Data that changes at runtime or per-customer — describe the metric and let the
  speaker fill in real numbers
- More than 8 bars — too dense for a slide
- Data that needs axes, gridlines, or precise labels — use an image placeholder
- Pie/donut charts — use a Mermaid `pie` diagram instead

### Markup

Use a `<div class="bar-chart">` with individual bars. Each bar uses inline
`style` for its width (percentage of max) and a `<span>` for the label.

```html
<div class="bar-chart">
  <div class="bar-row">
    <span class="bar-label">Python</span>
    <div class="bar" style="width:92%"><span class="bar-value">92%</span></div>
  </div>
  <div class="bar-row">
    <span class="bar-label">JavaScript</span>
    <div class="bar" style="width:78%"><span class="bar-value">78%</span></div>
  </div>
  <div class="bar-row">
    <span class="bar-label">TypeScript</span>
    <div class="bar" style="width:71%"><span class="bar-value">71%</span></div>
  </div>
  <div class="bar-row">
    <span class="bar-label">Go</span>
    <div class="bar" style="width:45%"><span class="bar-value">45%</span></div>
  </div>
</div>
```

### Placement rules

1. Position after any introductory text and before `<aside class="speaker-notes">`.
2. Use `width` as a percentage of the widest bar (which should be ~92–100%).
3. Keep labels ≤ 15 characters.
4. Include the numeric value inside the bar for accessibility.

---

## 4. Image placeholders (last resort)

When none of the inline media types above can represent the visual, insert a
TODO image placeholder following the rules in
[slide-image-placeholders.instructions.md](slide-image-placeholders.instructions.md).

**Before inserting an image placeholder, verify**:
- Could this be a Mermaid flow? → Use Mermaid.
- Could this be a table? → Use a table.
- Could this be a bar chart? → Use a bar chart.
- Is this a screenshot, annotated visual, or complex infographic? → Image
  placeholder is correct.

---

## Summary: media type cheat sheet

| Content pattern | Medium | Generated? |
|---|---|---|
| "Compare tools A, B, C across features X, Y, Z" | `<table>` | Yes |
| "Step 1 → Step 2 → Step 3 → Result" | Mermaid `graph LR` | Yes |
| "User calls API → Server validates → DB writes → Response" | Mermaid `sequenceDiagram` | Yes |
| "Feature has states: Draft → Review → Approved → Merged" | Mermaid `stateDiagram-v2` | Yes |
| "Adoption is 40% Python, 30% JS, 20% TS, 10% Go" | Mermaid `pie` or CSS bar chart | Yes |
| "Rollout: Pilot (Month 1–2), Expand (3–4), Optimize (5–6)" | Mermaid `gantt` | Yes |
| "Screenshot of the Settings panel in VS Code" | Image placeholder | No |
| "Annotated dashboard with callout boxes" | Image placeholder | No |
| "Complex network topology with 15 nodes" | Image placeholder | No |
