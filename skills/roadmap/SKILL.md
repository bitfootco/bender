---
name: roadmap
description: Use when you have a large feature, project, or initiative to plan. Breaks it into discrete, sequenced milestones and writes them to a ROADMAP.md that milestone can consume.
argument-hint: "[topic or goal] (optional — describe what you're planning; skill will ask if not provided)"
---

# Roadmap

## Core Rule

**PLAN THE WORK, THEN WRITE IT DOWN.**

The output of this skill is a `ROADMAP.md` with sequenced, single-session milestones in `- [ ]` format. Every decision made here should be captured in that document — not in conversation history.

---

## Phase 1: Orient

Before asking anything, understand the current state:

1. Check whether a `ROADMAP.md` or `MILESTONES.md` already exists. If it does, read it — this may be an update session, not a fresh start.
2. Run `git log --oneline -15` to see what has already shipped. Do not propose milestones for work that's already done.
3. Read `CLAUDE.md` and `README.md` for project context, constraints, and conventions.

---

## Phase 2: Understand the goal

If `$ARGUMENTS` describes the goal clearly, use it. Otherwise ask one question to establish:

- What are we planning? (the feature, initiative, or project)
- What does "done" look like at the end of the roadmap?
- Anything that is explicitly out of scope?

One question only. If the scope is still unclear after one round, propose a narrower framing rather than asking again.

---

## Phase 3: Draft the milestones

Break the goal into a sequenced list of milestones:

- **Each milestone must be implementable in a single session** — if it feels larger, split it.
- **Sequence matters** — put foundational work before dependent work.
- **Be concrete** — a milestone name should make it obvious what gets built, not just what area it touches. Prefer "Add JWT authentication to the API" over "Authentication work".
- **Apply YAGNI** — do not add milestones for hypothetical future needs. Plan to the stated goal, not beyond it.
- **Don't re-plan completed work** — items already in git history should not appear as `- [ ]` items.

Aim for 3–8 milestones. If the breakdown exceeds 8 items, the goal is probably too large for one roadmap — propose splitting into phases.

---

## Phase 4: Review

Present the draft milestone list to the user. State:

- The goal as you understood it (one sentence)
- The milestone list, in order
- Any sequencing decisions worth calling out (e.g. "X must come before Y because…")
- Anything explicitly left out

Ask for feedback. Incorporate it. One round of revision is expected — if a second round is needed, the goal likely needs narrowing first.

---

## Phase 5: Write the ROADMAP.md

Once the milestone list is approved:

1. **If no roadmap file exists:** create `ROADMAP.md` at the project root.
2. **If one already exists:** ask whether to append a new section or replace. Do not silently overwrite.

Write the file using this format:

```markdown
# Roadmap

## [Goal or Phase Name]

- [ ] Milestone one description
- [ ] Milestone two description
- [ ] Milestone three description
```

Use `- [ ]` for every planned item. Use `- [x]` only for items already completed. Do not use any other done-marker — `milestone` parses this format.

After writing, confirm the file path and tell the user they can run `/bender:milestone` to start executing.

---

## Hard Rules

- Do not start writing the file until the milestone list is approved.
- Each milestone must fit in one implementation session. Split anything larger.
- Never add milestones for work already in git history.
- Use `- [ ]` format — this is what `milestone` parses.
- Do not silently overwrite an existing roadmap. Always ask first.
- YAGNI: plan to the goal, not beyond it.
