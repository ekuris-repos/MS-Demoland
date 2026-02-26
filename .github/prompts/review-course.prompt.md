---
description: "Critical factual review of a course slide deck and lab guide. Read-only assessment; no edits."
agent: "ask"
---

# Critical Factual Review — Course Content Audit

You are reviewing a course in the MS Demoland training repository. Your job is to
perform a thorough factual and usefulness assessment of the slide deck
(`index.html`) and interactive lab guide (`lab.json`) in the course folder the
user specifies.

## Context gathering

Before you start, read these files for repository context:

- `.github/copilot-instructions.md` (repo structure and rules)
- `/memories/repo/style-guide.md` (writing conventions — em dash policy, etc.)

## Required reading

Read **every line** of `index.html` and `lab.json` in the target course folder.
Do not summarize from file names or headings; read the actual content, including
speaker notes (`<aside class="speaker-notes">`).

## Evaluation categories

### 1. Factual Errors (FE)

Statements that are wrong today. Check:

- Extension names, keyboard shortcuts, and UI element locations against current
  VS Code and GitHub Copilot.
- API names, CLI commands, config file paths, and setting names.
- Descriptions of how features work under the hood.
- Any claims about what a feature can or cannot do.

### 2. Potentially Stale Information (PSI)

Content that was likely correct at some point but may have drifted. Check:

- Pricing, quotas, plan names, and feature-tier assignments.
- Product terminology (features get renamed).
- Version-specific references.

### 3. Major Omissions (MO)

Important capabilities a learner in this course's track and level should at
minimum be aware of, even if not covered in depth. Consider what the product
looks like today vs. what the slides describe. Flag features that are completely
absent but would surprise a learner if they encountered them right after this
course.

### 4. Minor Issues (MI)

- Screenshot mismatches or image reuse across unrelated slides.
- Alt-text inaccuracies.
- Lab steps that reference a concept the slides mention but never exercise.
- Broken cross-references to other courses.

### 5. What Works Well

Call out genuinely strong content: good pedagogical flow, effective speaker
notes, well-designed lab exercises, accurate and forward-looking coverage.

## Output format

For each finding, provide:

| Field | Content |
|---|---|
| **Category & ID** | e.g., FE1, PSI2, MO3 |
| **Location** | Slide number and/or lab.json slide key + step title |
| **What it says** | Quote the relevant text |
| **What's wrong / missing** | What the correct or current state is |
| **Suggested action** | Fix, reword, add content, verify, or no change needed |

End with a **Recommendation** section that answers:

1. Is this a factual refresh, a structural rework, or production-ready?
2. List the specific actions in priority order.

## Important

**Do NOT make any edits.** This is a read-only assessment. Return only the
review.
