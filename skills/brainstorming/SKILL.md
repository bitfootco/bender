---
name: brainstorming
description: Use when starting any new feature, significant change, or architectural decision. Explores requirements and options before any implementation begins.
---

# Brainstorming

## Core Rule

**NO IMPLEMENTATION BEFORE DESIGN APPROVAL.**

Do not write code, scaffold files, or invoke any implementation action until the user has explicitly approved an approach.

## The Process

### 1. Understand the goal

Ask clarifying questions one at a time. Prefer multiple-choice questions over open-ended ones. Stop when you understand:

- What problem this solves and for whom
- What success looks like concretely
- Hard constraints: tech stack, existing patterns, things that must not break

Cap at 3 questions. If you need more, the scope is likely too large to design in one session — say so and propose breaking it down.

### 2. Explore what already exists

Before proposing anything, look at the codebase:

- Find related files with `Glob` and `Grep`
- Understand existing patterns and conventions
- Identify what can be reused vs. what needs to be built

Never propose a solution that ignores what's already there.

### 3. Propose 2–3 approaches

For each approach, state:

- **What it is** — one sentence
- **Why you'd choose it** — the key advantage
- **The tradeoff** — what you give up or complicate
- **Scope** — small / medium / large

Apply YAGNI ruthlessly. Do not propose approaches that add complexity for hypothetical future requirements.

### 4. Get approval

Present the approaches. Ask the user to pick one or suggest modifications. Do not start anything until they confirm.

### 5. Summarize before proceeding

Once an approach is approved, write a brief summary:

- What we're building
- The chosen approach and why
- Key constraints or decisions made
- What we're explicitly not building

Then ask whether to proceed directly to implementation or plan it out first.

## Rules

- One question per message during clarification — do not ask multiple questions at once
- Never propose more than 3 approaches
- Never begin implementation without explicit user approval
- YAGNI: if it isn't needed this week, don't design for it
