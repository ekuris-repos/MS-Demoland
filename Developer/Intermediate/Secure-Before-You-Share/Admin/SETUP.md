# Secure Before You Share: Setup Instructions

> **Track:** Developer | **Level:** Intermediate

## Course Environment

This course uses a disposable GitHub repository with an intentionally vulnerable feature branch. Do not use a production repository, real credentials, customer data, or production access.

### Required Access

- [ ] A GitHub Copilot plan with Copilot Chat enabled in VS Code
- [ ] Write access to a disposable GitHub repository
- [ ] GitHub Actions enabled
- [ ] Code scanning with CodeQL enabled for pull requests
- [ ] GitHub Code Security or GitHub Advanced Security for Copilot Autofix exercises
- [ ] Permission to create branches, commits, and draft pull requests

Copilot Autofix availability depends on repository visibility, licensing, language support, and organization policy. Agentic Autofix is optional and may not be available in every organization.

### Required Local Tools

- [ ] Current VS Code or VS Code Insiders with GitHub Copilot Chat
- [ ] GitHub CLI authenticated with `gh auth status`
- [ ] Git
- [ ] The runtime and package manager required by the disposable repository
- [ ] A local clone of the disposable repository

## Demo Repository

Prepare a small application with:

- A clean default branch with passing tests, lint, and build
- A deterministic dependency lock file
- One intentionally vulnerable feature branch
- At least one fast regression-test location
- CodeQL analysis configured to run on pull requests
- A ruleset that requires checks and human approval

Choose a vulnerability with a clear source-to-sink path supported by CodeQL for the selected language. SQL injection, command injection, path traversal, or reflected cross-site scripting are suitable. Keep the change small enough to understand in one review.

Prepare two fallback pull requests:

1. A vulnerable draft pull request with a CodeQL alert and Copilot Autofix suggestion.
2. A remediated pull request with passing tests and code scanning.

## Preflight Check

Run these commands from the disposable repository:

```powershell
gh auth status
git status --short
gh repo view --web
gh workflow list
```

Run the repository's normal install, test, lint, and build commands. Confirm that CodeQL analyzes the selected language and that the prepared vulnerable pull request produces the expected alert.

## Presenting the Slides

From the MS Demoland repository root, run:

```powershell
npm install
npm run dev
```

Open the URL printed by Vite, navigate to this course, and use the Lab Guide extension for the challenge steps.

## Fallback Delivery

If CodeQL or Copilot Autofix is slow or unavailable, use the prepared pull requests. Learners can still complete the local diff review, review record, remediation, regression test, and final gate evaluation. Clearly identify prepared output rather than simulating CodeQL or Autofix with generic Chat responses.

## Troubleshooting

| Issue | Resolution |
|---|---|
| CodeQL does not run | Confirm the language is supported and code scanning is enabled for pull requests |
| Expected alert is absent | Confirm the vulnerable path reaches the sink and the relevant query suite is enabled |
| Copilot Autofix is unavailable | Confirm licensing, policy, repository eligibility, and alert support; use the prepared suggestion |
| `gh pr create` fails | Run `gh auth status`, confirm the branch is pushed, and verify repository write access |
| Checks do not appear | Confirm workflow triggers include pull requests and Actions are enabled |
| Learner branch has unrelated changes | Reset the disposable clone or provide a fresh prepared branch |