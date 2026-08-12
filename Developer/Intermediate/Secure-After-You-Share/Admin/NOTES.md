# Secure After You Share: Class Notes

> **Track:** Developer | **Level:** Intermediate | **Target:** 45 minutes

## Course Positioning

This course is the cloud-side companion to Secure Before You Share. The first course teaches local review and remediation before a pull request exists. This course begins at the pull request and builds repeatable GitHub-hosted security controls around the change.

The central message is:

> Make the cloud prove it. Independent signals, enforceable policy, and human accountability protect every merge.

Learners should understand pull requests, GitHub Actions fundamentals, automated tests, and basic GitHub Copilot use.

## Suggested Pacing

| Slides | Topic | Time |
|---|---|---:|
| 1-4 | Challenge and cloud security loop | 4 min |
| 5-9 | Secure GitHub Actions and cloud deployment | 8 min |
| 10-15 | CodeQL, secrets, and supply-chain signals | 11 min |
| 16-20 | Copilot review, agent boundaries, and provenance | 8 min |
| 21-22 | Rulesets and ownership | 4 min |
| 23-28 | Security campaigns | 8 min |
| 29 | Merge decision | 1 min |
| 30 | Recap | 1 min |

Cloud checks and agent reviews may not complete during the class window. Use a prepared pull request with captured results while learners perform the workflow review and document their decisions locally.

## Delivery Emphasis

### Secure the Security Workflow

Treat workflow files as executable code with access to tokens, secrets, artifacts, and deployment targets. Start review with the event trigger, then follow trust through permissions, action references, event inputs, and runners. Keep untrusted pull-request code separate from privileged jobs.

### Keep Product Boundaries Precise

- **GitHub Actions** executes repeatable automation. Its security depends on workflow design, permissions, dependencies, and runner isolation.
- **CodeQL** runs semantic queries over a code database and reports alerts and data-flow paths.
- **Secret scanning** detects supported credential patterns. Push protection prevents supported secrets before they enter the repository.
- **Dependency review** evaluates package and license changes introduced by a pull request.
- **Dependabot** reports vulnerable dependencies and can propose version updates.
- **Copilot code review** adds contextual comments to a pull request. It does not approve or merge.
- **Copilot Autofix** proposes a remediation for supported code-scanning alerts.
- **Artifact attestations** provide signed build provenance. They do not prove an artifact is vulnerability-free.
- **Security campaigns** group selected code scanning or secret scanning alerts into time-bound remediation work. Secret scanning campaigns are currently in public preview.

### Respond According to the Signal

A CodeQL alert calls for path analysis and remediation. An exposed credential calls for revocation, rotation, and investigation. A dependency alert calls for reachability, exposure, and update analysis. Do not reduce all three to a shared severity score or a generic passing check.

### Preserve Human Accountability

Rulesets establish the minimum evidence required for merge. Human reviewers evaluate business intent, residual risk, and exceptions that automated checks cannot understand. Generated code and agent comments never approve themselves.

## Discussion Prompts

1. Which workflow event creates the largest trust-boundary change?
2. Which token permission can be removed without changing intended behavior?
3. Why does deleting an exposed secret fail to complete the response?
4. Which Copilot review comment was easiest to falsify?
5. Which checks should block merge, and who owns each failure?
6. What does an artifact attestation prove, and what does it not prove?
7. Which alert cohort would make a focused, achievable security campaign?

## Fallback Plan

1. Review the prepared workflow diff locally.
2. Open the captured Actions run and CodeQL alert.
3. Inspect the prepared secret scanning and dependency review results.
4. Compare captured Copilot code review comments with the final remediation.
5. Review a captured security campaign overview and explain its scope, owner, and due date.
6. Use the prepared ruleset screenshot to make the final merge decision.

State clearly when using prepared output. Do not imitate GitHub security results with a generic local prompt.

## Audience Q&A Log

| Date | Question | Answer / Follow-up |
|---|---|---|
| | | |

## Resources

- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- [OpenID Connect in cloud providers](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [About code scanning with CodeQL](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)
- [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
- [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review)
- [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)
- [About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)
- [Using artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [About security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns)
- [Creating and managing security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns)