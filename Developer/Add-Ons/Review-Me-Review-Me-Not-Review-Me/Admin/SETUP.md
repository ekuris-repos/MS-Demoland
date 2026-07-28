# Review Me Review Me Not Review Me: Setup Instructions

> **Track:** Developer | **Level:** Add-Ons

## Course Environment

This course uses a disposable GitHub repository to demonstrate a real local-to-cloud agent handoff and cloud security remediation. Do not use a production repository or a repository containing sensitive information.

### Required Access

- [ ] A paid GitHub Copilot plan with Copilot cloud agent enabled
- [ ] Write access to a disposable GitHub repository
- [ ] GitHub Actions enabled for the repository
- [ ] Code scanning with CodeQL enabled
- [ ] GitHub Code Security or GitHub Advanced Security for agentic Autofix exercises
- [ ] Permission to create branches, pull requests, and repository workflow files

Organization administrators may need to enable Copilot cloud agent, Copilot Autofix, GitHub Actions, and code scanning before class. Agentic Autofix is a public preview feature and may not be available in every organization.

### Required Local Tools

- [ ] Current VS Code or VS Code Insiders with GitHub Copilot Chat
- [ ] GitHub CLI authenticated with `gh auth status`
- [ ] Git
- [ ] The runtime and package manager required by the disposable repository
- [ ] A local clone of the disposable repository

## Repository Readiness

Before class, prepare one small application with:

- A deterministic dependency lock file
- A documented build command
- A documented test command
- At least one fast automated test
- A default branch that builds and tests successfully
- CodeQL analysis running on pull requests
- No real credentials, customer data, or production access

The instructor should also prepare a branch or issue containing a CodeQL-detectable vulnerability. A command injection, SQL injection, path traversal, or reflected cross-site scripting example works well when the selected language is supported by CodeQL.

## Preflight Check

Run these checks from the disposable repository before class:

```powershell
gh auth status
git status --short
gh repo view --web
```

Then run the repository's normal dependency installation, build, and test commands. Record those commands because learners will add them to the cloud-agent setup and handoff packet.

## Cloud Agent Configuration

Verify the following on the repository default branch:

1. Copilot cloud agent is enabled for the repository.
2. GitHub Actions can run workflows from pull requests.
3. Repository rulesets allow Copilot to create and update its working branch.
4. The Copilot firewall permits only the package registries required by the project.
5. Any agent secrets or variables are scoped specifically for Copilot and contain no production credentials.

## Presenting the Slides

From the MS Demoland repository root, run:

```powershell
npm install
npm run dev
```

Open the URL printed by Vite, then navigate to this course. Use the Lab Guide extension for the guided challenge steps.

## Fallback Delivery

If cloud agent or agentic Autofix is unavailable, use a prerecorded agent session and prepared draft pull request. Learners can still complete the repository optimization, handoff-packet, local validation, PR review, and security-gate portions of the lab. Clearly identify the recorded portion rather than simulating cloud behavior in Copilot Chat.

## Troubleshooting

| Issue | Resolution |
|---|---|
| Cloud session cannot start | Confirm the Copilot policy, repository eligibility, and write access |
| Setup steps are ignored | Confirm `.github/workflows/copilot-setup-steps.yml` is on the default branch and the job is named `copilot-setup-steps` |
| Dependency download is blocked | Review the Copilot firewall warning and add only the required registry URL |
| CodeQL does not analyze the pull request | Confirm the language is supported and code scanning is enabled for pull requests |
| Assign to Copilot is unavailable | Confirm cloud agent, Copilot Autofix, and the required security license are enabled |
| Agent cannot update its branch | Review branch protection and ruleset compatibility |
