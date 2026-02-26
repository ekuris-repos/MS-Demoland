---
applyTo: "**/lab.json"
---

# Lab Instruction Formatting Conventions

All `instruction` and `tip` fields in `lab.json` use inline HTML. This document
defines the formatting rules so step text is consistent across courses.

## Line breaks and paragraphs

Use `<br>` for a single line break. Use `<br><br>` to separate paragraphs or
introduce visual spacing between sections.

```json
"instruction": "First paragraph of guidance.<br><br>Second paragraph with more detail."
```

## Bullet lists

Use `&bull;` (•) for bullet points, each preceded by `<br>`:

```json
"instruction": "You learned:<br>&bull; How to open Copilot Chat<br>&bull; How to write effective prompts<br>&bull; How to review suggestions"
```

Do **not** use `<ul>`/`<li>` — the Lab Guide panel renders these as inline HTML,
not as block elements.

## Keyboard shortcuts

Wrap keyboard keys in `<kbd>` tags. Separate modifier keys with `+` inside a
single `<kbd>`:

```json
"instruction": "Press <kbd>Ctrl+Shift+I</kbd> to open Copilot Chat."
```

Common shortcuts:

| Shortcut | Markup |
|---|---|
| Ctrl+Shift+I | `<kbd>Ctrl+Shift+I</kbd>` |
| Ctrl+Shift+P | `<kbd>Ctrl+Shift+P</kbd>` |
| Ctrl+N | `<kbd>Ctrl+N</kbd>` |
| Ctrl+S | `<kbd>Ctrl+S</kbd>` |
| Ctrl+, | `<kbd>Ctrl+,</kbd>` |
| Ctrl+` | `<kbd>Ctrl+\`</kbd>` |
| Esc | `<kbd>Esc</kbd>` |
| Alt+[ / Alt+] | `<kbd>Alt+[</kbd>` / `<kbd>Alt+]</kbd>` |

Also use `<kbd>` for text the learner must type verbatim (e.g. prompts):

```json
"instruction": "Type <kbd>@workspace explain this project</kbd> in the chat input."
```

## UI element names

Wrap VS Code UI element names in `<strong>`:

```json
"instruction": "Click the <strong>Explorer</strong> icon in the sidebar."
```

Examples: `<strong>Copilot Chat</strong>`, `<strong>Command Palette</strong>`,
`<strong>Explorer</strong>`, `<strong>Source Control</strong>`,
`<strong>Settings</strong>`, `<strong>Terminal</strong>`,
`<strong>Extensions</strong>`, `<strong>Output Panel</strong>`.

## Technical terms and file names

Wrap file names, setting keys, and technical identifiers in `<code>`:

```json
"instruction": "Open the <code>lab.json</code> file and check the <code>focus</code> value."
```

## Emphasis within instructions

Use `<strong>` for emphasis on important words or phrases. Do **not** use `<em>`
or `<i>` — the guide panel style does not distinguish italic from regular text.

## Tips

The `tip` field follows the same formatting rules. Tips are optional and provide
extra context or alternative approaches:

```json
"tip": "You can also open Copilot Chat with <kbd>Ctrl+Shift+I</kbd> from anywhere in VS Code."
```

Keep tips to one or two sentences. They are hidden by default if the user
disables tips in settings.
