---
applyTo: "{Developer,Non-Developer}/**/index.html"
---

# Slide Speaker Notes

Speaker notes are a script the presenter can say aloud. Write them as natural
spoken narration addressed to the audience, not as directions to an instructor
or a mechanical summary of the slide.

## Required voice

- Speak directly to the room using natural language such as `we`, `you`,
	`let's`, and `here is why` where appropriate.
- Connect the current slide to the previous idea and explain why the content
	matters in practice.
- Add context, reasoning, examples, caveats, or a question that is not already
	obvious from the visible slide.
- Use varied sentence lengths and contractions that sound natural when spoken.
- Match the audience and course level. Beginner notes should be reassuring and
	concrete. Intermediate notes should frame choices and challenges. Enterprise
	notes should emphasize scale, tradeoffs, governance, and operations.
- Keep professional punctuation. Do not use em dashes or en dashes.

## Do not write facilitator directives

Do not put stage directions or instructions to the presenter inside
`<aside class="speaker-notes">`.

Avoid phrasing such as:

- `Frame the challenge around...`
- `Use this slide to...`
- `Encourage learners to...`
- `Ask learners to...`
- `Emphasize that...`
- `Warn against...`
- `Transition from...`
- `Recap the workflow...`
- `The learner should...`

Rewrite those ideas as words the presenter can deliver directly. Put delivery
instructions, timing, demo setup, and fallback guidance in `Admin/NOTES.md`.

## Do not narrate mechanically

- Do not restate the title and read every bullet in order.
- Do not begin every note with `This slide shows` or `On this slide`.
- Do not use detached documentation language such as `Learners will...` when
	the presenter could say `You will...` or `We will...`.
- Do not fill notes with generic claims that could apply to any course.
- Do not turn every note into a checklist. Explain the decision, tension, or
	consequence behind the visible content.

## Recommended shape

Most content-slide notes should follow this loose spoken rhythm:

1. **Orient:** Connect to the scenario or previous slide.
2. **Explain:** Add the reasoning behind the visible content.
3. **Apply:** Give a practical example, decision rule, caveat, or audience
	 question.
4. **Transition:** Point naturally toward the next action or idea when useful.

This is a rhythm, not a mandatory four-sentence template. Vary the structure so
the presentation does not sound generated.

Section-divider notes may be shorter, but they must still sound speakable and
create a useful transition. Every slide must have nonempty speaker notes.

## Examples

### Mechanical

```html
<aside class="speaker-notes">
	Frame the challenge around a realistic pressure point. Encourage learners to
	identify which part of the workflow creates the most risk.
</aside>
```

### Conversational

```html
<aside class="speaker-notes">
	Here is the situation: the feature works, the tests pass, and you are one
	command away from committing it. That is exactly when security issues are
	easiest to overlook, because everything feels finished. Which part of this
	change would be most expensive to discover after merge?
</aside>
```

### Mechanical restatement

```html
<aside class="speaker-notes">
	This slide lists CodeQL, Copilot Autofix, code review, and human approval.
</aside>
```

### Conversational explanation

```html
<aside class="speaker-notes">
	These tools are easy to group together, but they do different jobs. CodeQL
	gives us a repeatable security finding. Autofix proposes a change. Code
	review adds another perspective, and a human still owns the final decision.
	The value comes from combining different kinds of evidence, not asking one
	tool to approve its own work.
</aside>
```

## Review checklist

Before finishing a course deck, verify:

- Every slide has one nonempty `<aside class="speaker-notes">` block.
- The notes can be read aloud without translating instructions into speech.
- Notes explain more than the visible bullets, table, code, or diagram.
- Transitions and openings vary across the deck.
- Audience language is appropriate for the course level.
- Product claims and terminology are accurate.
- No facilitator directives, em dashes, or en dashes remain.
