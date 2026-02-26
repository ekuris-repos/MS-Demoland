---
applyTo: "**/lab.json"
---

# Welcome and Completion Step Conventions

Every lab must begin with a Welcome step and end with a Completion step. These
bookend steps follow strict conventions so the learner experience is consistent.

## Welcome step (slide 1)

The first entry in `slides` is always `"1"` and contains exactly one step:

```json
{
  "1": {
    "steps": [
      {
        "title": "Welcome to the Lab",
        "instruction": "Welcome! In this hands-on lab you will …",
        "focus": "guide"
      }
    ]
  }
}
```

### Rules

- **`title`**: Always `"Welcome to the Lab"` — no variation.
- **`focus`**: Always `"guide"` so the learner sees the Lab Guide panel first.
- **No `action`**: The welcome step never opens a panel or runs a command.
- **No `tip`**: Tips are for instructional steps, not the welcome.
- **Exactly one step**: Slide 1 always has a single step.
- **`instruction`** content: Start with `"Welcome!"` or
  `"Welcome to the <strong>Course Name</strong> lab."` and briefly describe what
  the learner will accomplish. Use `<strong>` for product/feature names and
  `<br><br>` to separate paragraphs.

## Completion step (last slide)

The last entry in `slides` is the final slide number and contains exactly one
step:

```json
{
  "30": {
    "steps": [
      {
        "title": "Lab Complete!",
        "instruction": "<strong>Congratulations!</strong> You have completed …<br><br>You learned:<br>&bull; …<br>&bull; …",
        "focus": "guide"
      }
    ]
  }
}
```

### Rules

- **`title`**: Always `"Lab Complete!"` — no variation.
- **`focus`**: Always `"guide"` so the learner reads the summary in the Lab
  Guide panel.
- **No `action`**: The completion step never opens a panel.
- **No `tip`** or **`onLeave`**: Not needed on the final step.
- **Exactly one step**: The completion slide always has a single step.
- **`instruction`** content: Start with `<strong>Congratulations!</strong>` (or
  a thematic closing line like `<strong>Mission accomplished!</strong>`),
  followed by a recap of what the learner built or learned. Use `&bull;` bullet
  lists for the recap items.
