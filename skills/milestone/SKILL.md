---
name: milestone
description: Use at the start of a session when there is a roadmap or milestone document and you want to pick up the next item. Orients from a cold start, locates the roadmap, identifies the next unfinished item, and proceeds to implementation.
argument-hint: "[roadmap file path] (optional — auto-discovers ROADMAP.md, MILESTONES.md, docs/*.md if not specified)"
---

# Milestone

## Core Rule

**FIND THE NEXT ITEM. UNDERSTAND THE CURRENT STATE. THEN IMPLEMENT.**

Do not guess what to work on from conversation context alone. Always read the roadmap document and the recent project state first. Do not begin implementation until Phases 1–3 are complete.

---

## Phase 1: Orient (cold start)

1. **Locate the roadmap.** If `$ARGUMENTS` is provided, read that file. Otherwise auto-discover in this order:
   - `ROADMAP.md`
   - `MILESTONES.md`
   - `docs/ROADMAP.md`
   - `docs/MILESTONES.md`
   - `.github/ROADMAP.md`

   If no roadmap is found after checking all locations, **stop immediately**. Tell the user no roadmap was found and suggest creating one. Do not invent a backlog or guess at what to work on.

2. **Read recent git history.** Run `git log --oneline -15` to understand what has been completed recently.

3. **Check for work in progress.** Run `git status` to detect uncommitted changes or in-progress work.

4. **Check project conventions.** Read `CLAUDE.md` if it exists, then `README.md`, to understand project patterns and constraints.

---

## Phase 2: Identify the next item

1. **Parse the roadmap** for incomplete items — unchecked `- [ ]` boxes, un-struck items, items not marked done.

2. **Select the next item:**
   - If one item is clearly next (sequentially first incomplete, or marked with priority), select it automatically and state the selection.
   - If multiple items are ambiguous (parallel tracks, unclear priority), present at most 3 candidates and ask the user to pick one. **One question only.**

3. **Do not start Phase 3 until the item is confirmed** — either explicitly by the user or implicitly because there is only one clear candidate.

---

## Phase 3: Scope and plan

1. **Identify affected files.** Use `Glob` and `Grep` to find files most likely touched by this milestone item. Note existing patterns and utilities to reuse — never ignore what's already there.

2. **Apply the narrow interpretation rule.** If the milestone item could be read broadly or narrowly, take the narrower reading.

3. **Write a 3–5 line implementation summary:**
   - What we are building (one sentence)
   - The approach (one sentence)
   - Files we expect to touch
   - What we are explicitly **not** building this session
   - State the interpretation explicitly if there was any ambiguity

4. **Present the summary.** If the user confirms (or does not object), proceed to Phase 4. No further approval ceremony needed.

---

## Phase 4: Implement

- Follow standard bender engineering practices: TDD, verification before completion claims, systematic debugging if anything breaks.
- Do not implement adjacent features, refactor nearby code, or add "while I'm in here" improvements. If something obviously needs fixing outside the milestone scope, note it as a candidate for a future roadmap item — do not act on it now.
- When implementation is functionally complete and CI / spec checks are passing, run `/bender:code-review` before proceeding. Resolve any **must fix** findings before moving on.
- After implementation is complete, verified, and reviewed, proceed to Phase 5 before touching the roadmap.

---

## Phase 5: Milestone fidelity check (before marking done)

Before declaring the work complete or updating the roadmap:

1. Re-read the milestone item verbatim from the roadmap document.
2. List what was implemented.
3. Confirm the two match. If implementation went narrower than described, note what remains. If it went broader, flag the delta explicitly.
4. Only once the match is confirmed, mark the item done in the roadmap — check the box, strike the item, or follow whatever convention the doc uses.
5. **Do not rewrite or reorder the roadmap doc.** Only mark the completed item. Never restructure, re-prioritize, or editorialize the document.

---

## Hard Rules

- Never start Phase 4 without completing Phases 1–3.
- If no roadmap file is found, stop immediately — do not invent a backlog.
- Cap clarifying questions at 1. If scope is unclear after one question, flag it and propose breaking the item down into smaller roadmap entries first.
- Never mark an item complete in the roadmap until the Phase 5 fidelity check passes.
- **No scope creep.** Adjacent improvements go on the roadmap as new items, not into this session.
- **Ambiguity → narrow interpretation.** State it explicitly so the user can correct before work begins.
- **Do not rewrite or reorder the roadmap doc** — only mark the completed item done.
