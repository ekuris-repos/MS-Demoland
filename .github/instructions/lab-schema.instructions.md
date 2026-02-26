---
applyTo: "**/lab.json"
---

# Lab JSON Schema Reference

Every course has a `lab.json` that the Lab Guide VS Code extension reads. This
document defines the complete schema, valid field values, and pairing rules.

## Top-level structure

```jsonc
{
  "title": "Topic Category — Course Display Name",
  "repo": "org/repo-name",          // optional — single repo to clone
  "repos": ["org/repo-a", "org/b"], // optional — multi-repo (v0.7.0+)
  "slides": {
    "1": { "steps": [ /* … */ ] },
    "5": { "steps": [ /* … */ ] }
  }
}
```

- **`title`** (required): Format is `"Topic Category — Course Display Name"`.
  Use an em dash ` — ` (surrounded by spaces) as the separator.
- **`repo`** / **`repos`**: Mutually exclusive. Most courses omit both. Use
  `repo` when the lab needs one cloned repository; use `repos` when it needs
  multiple.
- **`slides`**: Keys are **slide numbers** (as strings). Not every slide in the
  HTML deck needs a lab entry — only slides that have guided steps.

## SlideEntry

```jsonc
{
  "steps": [ /* LabStep[] — at least one step required */ ],
  "onLeave": "command"  // DEPRECATED — use step-level onLeave instead
}
```

Slide-level `onLeave` is deprecated. Always place `onLeave` on individual steps.

## LabStep

```jsonc
{
  "title": "Step Title",
  "instruction": "HTML-formatted guidance shown in the Lab Guide panel.",
  "tip": "Optional hint shown when tips are enabled.",
  "focus": "right",
  "action": "workbench.action.chat.open",
  "actionLabel": "Open Copilot Chat",
  "onLeave": "workbench.action.closeSidebar"
}
```

### Field reference

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | `string` | Yes | Short label shown in the status bar and step header. |
| `instruction` | `string` | Yes | HTML content displayed in the guide panel. Use `<br>` for line breaks. |
| `tip` | `string` | No | Additional hint. Only visible when the user has tips enabled. |
| `focus` | `string` | No | Where VS Code should draw the learner's attention (see below). |
| `action` | `string \| string[]` | No | VS Code command(s) to execute when the step loads. |
| `actionLabel` | `string` | No | Human-readable label describing the action. Required when `action` is present. |
| `onLeave` | `string \| string[]` | No | VS Code command(s) to execute when the user advances past this step. |

### `focus` values

Single values (most common):

| Value | Draws attention to |
|---|---|
| `right` | Secondary sidebar / Copilot Chat panel |
| `slides` | The slide deck (browser panel) |
| `editor` | The active editor area |
| `guide` | The Lab Guide panel itself |
| `terminal` | The integrated terminal |
| `top` | The top bar / title bar area |
| `left` | The primary sidebar (Explorer, SCM, etc.) |
| `bottom` | The bottom panel area |
| `chat` | The Copilot Chat input specifically |

Compound values use commas to highlight multiple areas simultaneously:
`"editor,right"`, `"editor,chat"`, `"top,right"`, `"terminal,chat"`, etc.

### `action` commands

Only use registered VS Code commands. The commands used across existing courses:

| Command | Opens | Frequency |
|---|---|---|
| `workbench.action.chat.open` | Copilot Chat (sidebar) | Most common |
| `workbench.action.files.newUntitledFile` | New untitled editor tab | Common |
| `workbench.action.terminal.toggleTerminal` | Integrated terminal | Common |
| `workbench.view.explorer` | Explorer sidebar | Common |
| `workbench.action.openSettings` | Settings editor | Occasional |
| `workbench.action.showCommands` | Command Palette | Occasional |
| `workbench.action.output.toggleOutput` | Output panel | Occasional |
| `workbench.view.scm` | Source Control sidebar | Occasional |
| `workbench.action.problems.focus` | Problems panel | Rare |
| `workbench.view.extensions` | Extensions sidebar | Rare |

### `actionLabel` rule

**Every step with an `action` must have an `actionLabel`.** The label tells the
learner what the extension just did for them. Use short, descriptive phrases:

- `"Open Copilot Chat"`
- `"Open New File"`
- `"Open Terminal"`
- `"Open Explorer"`
- `"Open Settings"`
- `"Open Command Palette"`
- `"Open Source Control"`
- `"Open Output Panel"`

When `action` is an array, the `actionLabel` should describe the combined effect.

### `onLeave` usage

See the companion file `lab-panel-lifecycle.instructions.md` for full rules on
when and how to use `onLeave` to manage panel state.
