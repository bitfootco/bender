---
name: milestone
description: Pick up and implement the next item from a roadmap or milestone document. Use at the start of a session when the user asks to continue a roadmap, execute the next milestone, or supplies a roadmap path. Implement one parent directly; use inchstone instead when the user explicitly asks for surgical chunking.
---

# Milestone

## Core Rule

**FIND THE NEXT ITEM. UNDERSTAND THE CURRENT STATE. THEN IMPLEMENT.**

Do not guess what to work on from conversation context alone. Always read the roadmap document and the recent project state first. Do not begin implementation until Phases 1–3 are complete.

## Phase 1: Orient (cold start)

1. Locate the roadmap. Use a user-supplied path; otherwise check `ROADMAP.md`, `MILESTONES.md`, `docs/ROADMAP.md`, `docs/MILESTONES.md`, then `.github/ROADMAP.md`. If none exists, stop; do not invent work.
2. Run `git log --oneline -15` and `git status`. Preserve unrelated user work and stop before touching an overlapping path or hunk.
3. Read applicable `AGENTS.md` and `CLAUDE.md`, then only the README sections needed for the item.
4. Discover CI in this order: `bin/ci`; repository instructions; project manifests or build files. If none exists, use the broadest available test command and report the limitation.

## Phase 2: Identify the Next Item

1. Parse incomplete roadmap items and their dependencies or ordering.
2. Select the first clearly ready item and state the selection. If multiple items are equally ready, present at most three and ask one focused question.
3. Quote the selected parent verbatim and identify its acceptance criteria, dependencies, and exclusions.
4. If the item is too vague to determine observable completion, ask one focused question before continuing.

## Phase 3: Scope and Plan

1. Trace relevant entry points, callers, tests, data flow, and repository conventions. Identify behavior already satisfied and behavior still required.
2. Apply the narrow interpretation rule. Prefer extending existing paths over adding concepts.
3. Present a concise implementation summary: intended outcome, direct approach, likely affected behavior or files, acceptance criteria, and explicit exclusions.
4. Proceed unless the user corrects the boundary. Do not introduce chunk selection or approach approval gates.

## Phase 4: Implement Directly

1. Implement the selected parent in the current context rather than delegating it through `chunk`.
2. Use test-driven development: add the smallest failing behavior test, confirm the failure, implement the minimum change, and refactor while green.
3. Do not implement adjacent features or unrelated cleanup. Preserve pre-existing work.
4. If a test fails unexpectedly, use systematic debugging before changing more code.
5. Run focused tests, then the discovered full CI command.
6. Apply the `code-review` skill to the milestone-attributable diff. Resolve must-fix findings, rerun affected tests and CI, and re-review as needed.

## Phase 5: Milestone Fidelity Check

Before declaring completion or editing the roadmap:

1. Re-read the parent item verbatim.
2. Map every acceptance criterion to code and tests.
3. Confirm the implementation matches the parent. If it is narrower or broader, report the delta and do not mark it complete.
4. Confirm final CI and review succeeded with fresh evidence.
5. Only then mark the selected item done using the roadmap's existing convention.
6. Do not rewrite, reorder, annotate, or reprioritize other roadmap content.

## Phase 6: Doc Sync

Follow any documentation maintenance protocol in `AGENTS.md` or `CLAUDE.md`; otherwise update only the parent marker. Validate the docs-only diff with the configured validator or `git diff --check`.

## Hard Rules

- Complete one parent per invocation.
- Never start implementation before orientation, selection, and scoping.
- Implement directly; generic roadmap continuation belongs here, while explicit surgical or chunked execution belongs to `inchstone`.
- Never add routine chunk approval gates.
- Never mark an item complete until fidelity, CI, and review succeed.
- Preserve unrelated user changes and stop on unsafe overlap or uncertain attribution.
- Keep scope narrow and do not rewrite or reorder the roadmap.
