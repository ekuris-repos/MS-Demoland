---
applyTo: "**/lab.json"
---

# Panel Lifecycle Management

Every `lab.json` file must manage VS Code panel state so the learner's workspace
stays clean between steps. When a step opens a panel, the lab must close it
before the user moves on. This is handled with two mechanisms: **`onLeave`** and
**"Panels Closed" recap steps**.

## Core rules

1. **If a step opens a panel, it (or a later step on the same slide) must close
   it via `onLeave`.** The `onLeave` field fires automatically when the user
   advances past that step. Place it on the last step that still needs the panel
   visible.

2. **Every slide that opens a panel must end with a "Panels Closed" recap step.**
   This step has no action; it tells the user what was closed and lists keyboard
   shortcuts for reopening.

3. **Panel transitions within a slide** require an intermediate `onLeave`. If
   step A opens the Explorer (sidebar) and step B opens Copilot Chat (also
   sidebar), step A needs `onLeave` to close the sidebar before step B replaces
   it.

4. **Never use `action` to close a panel.** Older courses had steps like
   `"action": "workbench.action.closeSidebar"`. This is incorrect. Close
   commands belong in `onLeave`, not `action`. If you find an existing close
   action, convert it to `onLeave` and remove the `action`/`actionLabel` fields.

5. **Do not use slide-level `onLeave`.** All close handling is per-step, not
   per-slide.

## Action-to-close mapping

| Open action | Close command (`onLeave`) |
|---|---|
| `workbench.action.chat.open` | `workbench.action.closeSidebar` |
| `workbench.view.explorer` | `workbench.action.closeSidebar` |
| `workbench.view.scm` | `workbench.action.closeSidebar` |
| `workbench.view.extensions` | `workbench.action.closeSidebar` |
| `workbench.action.showCommands` | `workbench.action.closeQuickOpen` |
| `workbench.action.openSettings` | `workbench.action.closeActiveEditor` |
| `workbench.action.files.newUntitledFile` | `workbench.action.closeActiveEditor` |
| `workbench.action.output.toggleOutput` | `workbench.action.closePanel` |
| `workbench.action.terminal.toggleTerminal` | `workbench.action.closePanel` |
| `workbench.action.problems.focus` | `workbench.action.closePanel` |

When multiple panels are open on the same slide, `onLeave` accepts an array:

```json
"onLeave": ["workbench.action.closePanel", "workbench.action.closeSidebar"]
```

## Hotkey reference for recap steps

Use these labels in "Panels Closed" `instruction` fields:

| Panel | Label |
|---|---|
| Copilot Chat | `<strong>Copilot Chat</strong>: <kbd>Ctrl+Shift+I</kbd>` |
| Command Palette | `<strong>Command Palette</strong>: <kbd>Ctrl+Shift+P</kbd>` |
| Settings | `<strong>Settings</strong>: <kbd>Ctrl+,</kbd>` |
| Output Panel | `<strong>Output Panel</strong>: <kbd>Ctrl+Shift+U</kbd>` |
| Explorer | `<strong>Explorer</strong>: <kbd>Ctrl+Shift+E</kbd>` |
| Source Control | `<strong>Source Control</strong>: <kbd>Ctrl+Shift+G</kbd>` |
| Extensions | `<strong>Extensions</strong>: <kbd>Ctrl+Shift+X</kbd>` |
| Terminal | <code>&lt;strong&gt;Terminal&lt;/strong&gt;: &lt;kbd&gt;Ctrl+\`&lt;/kbd&gt;</code> |
| New File | `<strong>New File</strong>: <kbd>Ctrl+N</kbd>` |
| Problems Panel | `<strong>Problems Panel</strong>: <kbd>Ctrl+Shift+M</kbd>` |

## Example: single panel opened and closed

```json
{
  "12": {
    "steps": [
      {
        "title": "Open Copilot Chat",
        "instruction": "We've opened <strong>Copilot Chat</strong> for you.",
        "focus": "right",
        "action": "workbench.action.chat.open",
        "actionLabel": "Open Copilot Chat"
      },
      {
        "title": "Ask a Question",
        "instruction": "Type your question in the chat panel.",
        "focus": "right",
        "onLeave": "workbench.action.closeSidebar"
      },
      {
        "title": "Panels Closed",
        "instruction": "We've closed the sidebar for you.<br><br>For future reference:<br>&bull; <strong>Copilot Chat</strong>: <kbd>Ctrl+Shift+I</kbd>",
        "focus": "slides"
      }
    ]
  }
}
```

## Example: panel transition mid-slide

```json
{
  "14": {
    "steps": [
      {
        "title": "Create a File",
        "instruction": "We've opened a new file for you.",
        "action": "workbench.action.files.newUntitledFile",
        "onLeave": "workbench.action.closeActiveEditor"
      },
      {
        "title": "Ask Copilot to Review",
        "instruction": "We've opened Copilot Chat.",
        "action": "workbench.action.chat.open",
        "focus": "right",
        "onLeave": "workbench.action.closeSidebar"
      },
      {
        "title": "Panels Closed",
        "instruction": "We've closed the editor tab and the sidebar for you.<br><br>For future reference:<br>&bull; <strong>New File</strong>: <kbd>Ctrl+N</kbd><br>&bull; <strong>Copilot Chat</strong>: <kbd>Ctrl+Shift+I</kbd>",
        "focus": "slides"
      }
    ]
  }
}
```

## Example: multiple panels open simultaneously

```json
{
  "25": {
    "steps": [
      {
        "title": "Monitor a Tool Call",
        "instruction": "The Output panel is open. Switch to Chat and run a query, then check Output.",
        "action": "workbench.action.output.toggleOutput",
        "focus": "bottom",
        "onLeave": ["workbench.action.closePanel", "workbench.action.closeSidebar"]
      },
      {
        "title": "Panels Closed",
        "instruction": "We've closed the bottom panel and the sidebar for you.<br><br>For future reference:<br>&bull; <strong>Copilot Chat</strong>: <kbd>Ctrl+Shift+I</kbd><br>&bull; <strong>Output Panel</strong>: <kbd>Ctrl+Shift+U</kbd>",
        "focus": "slides"
      }
    ]
  }
}
```

## Recap step format

The "Panels Closed" step always follows this structure:

```json
{
  "title": "Panels Closed",
  "instruction": "We've closed <WHAT> for you.<br><br>For future reference:<br>&bull; <HOTKEY_1><br>&bull; <HOTKEY_2>",
  "focus": "slides"
}
```

- **Title** is always exactly `"Panels Closed"`.
- **`focus`** is always `"slides"` (returns attention to the slide deck).
- **No `action`, `actionLabel`, `onLeave`, or `tip`** fields.
- If only one panel was opened on the slide, list only that hotkey.
- If multiple panels were opened, list all of them.
