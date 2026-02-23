# AI Pair Programming — The Copilot Awakens — Setup Instructions

> **Track:** Developer | **Level:** Beginner | **Duration:** 30 minutes

## Prerequisites

### Presenter Machine

- [ ] VS Code (latest stable) with the **GitHub Copilot Chat** extension installed and signed in
- [ ] A GitHub account with an active Copilot license (Individual, Business, or Enterprise)
- [ ] Node.js v18+ (for the Vite dev server and demo code)
- [ ] Git clone of this repository
- [ ] The **MS Demoland Lab Guide** extension installed (`lab-guide/`)

### Attendee Machines (if hands-on)

- [ ] VS Code installed
- [ ] GitHub account with Copilot seat provisioned
- [ ] Internet access (Copilot requires connectivity to GitHub's API)

## Quick Start — Slides

1. Open a terminal at the **repo root**:
   ```
   npm run dev
   ```
2. Navigate to `Developer/Beginner/The-Copilot-Awakens/index.html` in the browser.
3. Use **arrow keys** or **click** to navigate slides.

## Quick Start — Lab Guide Extension

1. Open this repository in VS Code.
2. Open the built-in Simple Browser and navigate to the course navigator (`/?vscode`).
3. Click the **"AI Pair Programming — The Copilot Awakens"** card.
4. The Lab Guide extension loads `lab.json` and opens the simulated Copilot Chat panel.
5. Follow the step-by-step instructions in the panel.

## Demo Prep

- **Demo file:** Create a temporary `utils.js` in the repo root for the inline completion demo (slide 21). Delete it after the session.
- **Suggested demo flow:**
  1. Type the CSV parser comment → let Copilot complete the function
  2. Select the function → `/explain`
  3. Inline chat (`Ctrl+I`) → "Add error handling"
  4. Chat panel → `/tests`
- **Fallback:** If Copilot is slow or unavailable, the `lab.json` has pre-scripted chat messages you can walk through in the simulated panel.

## Presenting

- Use **arrow keys** or **click** to navigate slides.
- Press **F** for fullscreen (browser native).
- The lab panel (in VS Code) runs independently — advance lab steps with the Next/Prev buttons.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Port already in use | Change port in `vite.config.js` or kill the process using the port |
| Copilot not activating | Check GitHub account sign-in, verify license at github.com/settings/copilot |
| Lab Guide not loading | Ensure the `lab-guide` extension is installed and the dev server is running |
| Slides not advancing | Check browser console for JS errors in `slides.js` |
| Ghost text not appearing | Ensure `editor.inlineSuggest.enabled` is `true` in VS Code settings |
