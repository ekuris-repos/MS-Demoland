# Review Me Review Me Not Review Me: Class Notes

> **Track:** Developer | **Level:** Add-Ons | **Target:** 45 minutes

## Course Positioning

This course teaches an agentic delivery loop. It is not a general introduction to Copilot code review, CodeQL, or GitHub Actions. Learners should already understand pull requests, basic Copilot Chat use, and automated tests.

The central message is:

> Successful cloud-agent work begins before delegation. Execution may move between environments, but accountability does not.

## Suggested Pacing

| Slides | Topic | Time |
|---|---|---:|
| 1-4 | Challenge and delivery loop | 3 min |
| 5-8 | Choose the execution surface | 5 min |
| 9-15 | Optimize before handoff | 11 min |
| 16-20 | Local-to-cloud handoff and supervision | 9 min |
| 21-25 | CodeQL and agentic remediation | 9 min |
| 26-29 | Review gates and return handoff | 6 min |
| 30 | Recap | 2 min |

The guided challenge can exceed 45 minutes when learners wait for live cloud sessions and security scans. For a fixed session, start the cloud work early and use prepared pull requests for the security portion.

## Demo Preparation

Prepare these states before class:

1. A clean default branch with passing build and tests.
2. A scoped issue suitable for a single cloud session.
3. A branch or pull request with a CodeQL-detectable vulnerability.
4. A completed cloud-agent session and pull request as a timing fallback.
5. An agentic Autofix draft pull request as a licensing or service fallback.
6. A ruleset view showing required checks and human approval.

Never use real secrets or production access. Keep the demo repository disposable.

## Delivery Emphasis

### Choosing an Agent

Describe local, background, and cloud agents as execution surfaces with different context boundaries. Do not imply that cloud is always more capable. It is optimized for autonomous, repository-contained work.

### Optimizing Before Handoff

Spend the most time here. Highlight that repository engineering often matters more than prompt length:

- Deterministic dependency installation
- Fast and meaningful tests
- Explicit validation commands
- Small task scope
- Durable instructions
- Restricted network and tool access

### Handoff Behavior

Current VS Code supports transferring a local conversation to a cloud agent by changing the session type to Cloud. The Plan agent also provides **Continue in Cloud**, and background sessions can use `/delegate`. The conversation transfers; unsaved files and local runtime state do not.

### Security Terminology

Use precise product boundaries:

- **CodeQL** detects security and quality paths through deterministic analysis.
- **Copilot Autofix** generates a suggested correction.
- **Agentic Autofix** assigns alerts to Copilot cloud agent for repository exploration, implementation, rerun, iteration, and draft pull-request creation.
- **Copilot code review** adds contextual review comments.
- **GitHub Code Quality** combines deterministic and AI-powered quality findings, coverage, remediation, and ruleset gates.

Avoid the product name "CodeQL agent." Use "CodeQL and security agents" when describing the combined workflow.

## Expected Questions

### Does Continue in Cloud send my entire local workspace?

No. It transfers conversation context and operates against the selected GitHub repository. Unsaved files, transient terminal state, and local-only services are not automatically available.

### Does passing CodeQL prove the fix is secure?

No. It proves the configured analysis no longer reports that path. Reviewers must still inspect alternate paths, behavior changes, regressions, dependencies, permissions, and network access.

### Is the cloud-agent firewall a complete data-loss prevention boundary?

No. It is an important control with documented limitations. It does not cover MCP servers or processes started by setup steps, and it may not stop sophisticated bypasses.

### What happens when setup steps fail?

The remaining setup steps are skipped, and the cloud agent begins with the environment in its current state. This is why the setup workflow must be tested before delegation.

### Can one session update multiple repositories?

No. A cloud-agent session changes one repository, works on one branch, and creates one pull request for the assigned task.

## Fallback Plan

If a live session is slow or unavailable:

1. Show the prepared cloud session log.
2. Ask learners to compare its evidence with the handoff packet.
3. Open the prepared pull request and CodeQL alert.
4. Show the prepared agentic remediation session and draft pull request.
5. Continue with the gate and return-handoff exercises.

State clearly when showing prepared output. Do not imitate cloud-agent or Autofix behavior with a generic local Chat prompt.

## Audience Q&A Log

| Date | Question | Answer / Follow-up |
|---|---|---|
| | | |

## Feedback and Improvements

Record where learners lose time during setup, which acceptance criteria remain ambiguous, and whether the security alert is detected reliably. Those observations should drive changes to the demo repository and handoff packet before adding more slides.

## Resources

- [About GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [Cloud agents in Visual Studio Code](https://code.visualstudio.com/docs/agents/agent-types/cloud-agents)
- [Configure the cloud-agent development environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)
- [Customize the Copilot firewall](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-firewall)
- [Resolve code-scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts)
- [GitHub Code Quality](https://docs.github.com/en/code-security/concepts/code-quality/code-quality)
