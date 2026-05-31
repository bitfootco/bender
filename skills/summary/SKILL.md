---
name: summary
description: Summarize the most recent commit or pending changes — what they do, how they fit into the existing code, and a diagram if the change is structural.
---

# Change Summary

## Core Rule

**EXPLAIN WHAT THE CHANGE SHIPS AND HOW IT FITS — NOT WHAT FILES MOVED OR WHAT LINES CHANGED.**

The output should let someone who hasn't touched the code in a week immediately understand what the change is, why it matters, and how it connects to the existing system. Keep it short enough to read in under 30 seconds.

---

## Phase 1: Determine scope

Run these in order and use whichever produces output first:

1. `git diff HEAD` — unstaged working tree changes
2. `git diff --cached` — staged-only changes
3. `git show HEAD` — most recent commit

If none of these produce output (brand-new repo with no commits), say so and stop.

---

## Phase 2: Gather context

1. Get the file-level summary: `git diff --stat HEAD` (or `git show --stat HEAD` if falling back to the commit)
2. Read the full diff — every line of it
3. For each file that changed substantially, read the surrounding code in that file: the functions, classes, or modules adjacent to the changed lines. Don't read only the diff lines — understand what the changed code lives inside and connects to.
4. If there's a `README.md`, `CLAUDE.md`, or `ROADMAP.md` at the project root and the change seems architectural, skim it for context on the project's structure and intent.

Goal: understand not just *what changed* but *what role those changes play* in the larger codebase.

---

## Phase 3: Produce the summary

Write the output directly — no preamble, no sign-off, no "Here is your summary:".

### Format

```
**[One-line title — the change in plain English]**

[2–3 sentences: what it does and why. Lead with the behavior or capability, not the mechanism.]

[1–2 sentences: how it connects to the existing code — what it replaces, extends, calls into, or is called by.]

[Diagram OR key details — see below]
```

### Diagram vs. prose

Use a **Mermaid diagram** when the change involves any of:
- Data or control flow between components
- A new call chain or middleware layer
- New wiring between modules (a new service, handler, hook, or event listener)
- Relationships between the new code and multiple existing parts of the system

Use **bullet points** for contained changes:
- Bug fixes
- Config or constant updates
- Single-function additions with no architectural implications
- Copy or text changes

**Diagram rules:**
- Mermaid only — no ASCII art
- 4–8 nodes maximum
- Label every edge to show what flows or what triggers what
- Show only what the change introduces or touches — not the whole system
- Use `graph LR` for flows, `sequenceDiagram` for call sequences

**Bullet rules:**
- 3–6 bullets maximum
- Each bullet is a behavior or consequence, not a file name or line number

---

## Hard Rules

- Target 10–20 lines of output. Never exceed 30.
- No file names, line numbers, or "this was modified in X" narration.
- No padding. Short changes get short summaries.
- If the diff doesn't make the intent obvious, describe what it does — don't invent a "why."
- No questions. No asking for clarification. Run the commands, read the code, write the summary.
