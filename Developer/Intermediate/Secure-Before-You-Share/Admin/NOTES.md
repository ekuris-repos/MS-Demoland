# Secure Before You Share: Class Notes

> **Track:** Developer | **Level:** Intermediate | **Target:** 45 minutes

## Course Positioning

This course teaches a local-first secure development workflow. It complements the broader agentic delivery course, Review Me, Review Me Not, Review Me, by concentrating on the developer's own change before a pull request exists.

The central message is:

> Security starts before the pull request. Developer context finds risk early, and platform controls make protection consistent.

Learners should already understand Git branches, pull requests, automated tests, and basic Copilot Chat use.

## Suggested Pacing

| Slides | Topic | Time |
|---|---|---:|
| 1-4 | Challenge and secure change loop | 4 min |
| 5-11 | Local inspection, review, and remediation | 17 min |
| 12-16 | Transition from local evidence to CodeQL | 9 min |
| 17-20 | Autofix evaluation | 8 min |
| 21-23 | Platform controls and final gate | 6 min |
| 24 | Recap | 1 min |

Live scan timing can exceed the class window. Use prepared pull requests for the CodeQL and Autofix portions while learners perform the local review on their own branches.

## Delivery Emphasis

### Keep the Developer in Control

Copilot produces candidate findings, remediation options, and test ideas. The developer supplies intent, runtime evidence, classification, and validation. Require learners to record rejected hypotheses as well as confirmed findings.

### Trace the Path

For injection and path-based vulnerabilities, ask learners to identify:

- The untrusted source
- Each important propagation step
- The missing validation or authorization control
- The sensitive sink
- The resulting impact

Do not accept a line-level patch without checking the complete path.

### Use Precise Product Boundaries

- **CodeQL** runs deterministic queries over a code database and reports alerts and paths.
- **Copilot Autofix** generates a suggested correction for a supported alert.
- **Agentic Autofix** can explore the repository, implement a fix, rerun analysis, iterate, and open a draft pull request when available.
- **Copilot code review** adds contextual comments to a pull request.

Avoid describing any of these systems as an autonomous approver.

### Connect Local Practice to Platform Protection

The transition should feel cumulative. Local review uses developer context to prevent avoidable findings. CodeQL independently analyzes the committed change. Rulesets ensure that analysis occurs consistently. Autofix can shorten remediation time. Human approval evaluates the full risk and business context.

## Discussion Prompts

1. What did Copilot notice that the developer initially missed?
2. Which Copilot claim lacked enough evidence to act on?
3. Did CodeQL find the same path as the local review? Why or why not?
4. Did the Autofix remove the root cause or only block one payload?
5. Which controls should be required across every repository in the organization?

## Fallback Plan

1. Complete local review and remediation against the learner's disposable branch.
2. Open the prepared vulnerable pull request.
3. Trace the prepared CodeQL alert from source to sink.
4. Inspect the prepared Copilot Autofix suggestion.
5. Compare it with the prepared remediated pull request and passing checks.

State clearly when using prepared output. Do not imitate CodeQL or Autofix behavior with a generic local prompt.

## Audience Q&A Log

| Date | Question | Answer / Follow-up |
|---|---|---|
| | | |

## Resources

- [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)
- [Responsible use of Copilot Autofix](https://docs.github.com/en/code-security/responsible-use/responsible-use-autofix-code-scanning)
- [Resolving code-scanning alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)