# GitHub Copilot CLI — Setup Instructions

> **Track:** Developer | **Level:** Intermediate

## Prerequisites

- [ ] A supported GitHub Copilot plan with Copilot CLI enabled by policy
- [ ] Copilot CLI installed through npm, WinGet, Homebrew, or a direct download
- [ ] Node.js 22 or later only when using the npm installation route
- [ ] PowerShell 6 or later on Windows
- [ ] Git clone of this repository in a location safe for lab changes

## Quick Start

1. Open a terminal at the repository root.
2. Install the slide-site dependencies:
   ```
   npm install
   ```
3. Start the local dev server:
   ```
   npm run dev
   ```
4. Open the course URL:
   ```
   http://localhost:5173/Developer/Intermediate/Copilot-CLI-The-Who-the-How-and-the-Why/
   ```

## Presenting

- Use **arrow keys** or **click** to navigate slides.
- Press **F** for fullscreen (browser native).

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Port already in use | Change port in `vite.config.js` or kill the process using the port |
| `copilot` command not found | Reopen the terminal and verify the selected installation method |
| Copilot access denied | Confirm plan eligibility and organization policy with an administrator |
| Slides not advancing | Check browser console for JS errors in `slides.js` |

## Additional Setup

- Use a disposable branch or worktree for lab exercises that create files.
- Authenticate interactively before delivery and verify the GitHub MCP server can read the demo repository.
- Do not store tokens in the course files or shell history.
