---
name: pipeline
description: Orchestrates the full roadmap-to-committed-code flow. Iterates through milestones — implementing, testing, reviewing, and committing each — with human approval gates.
argument-hint: "[--auto] [roadmap file path] (optional — --auto skips human review gate per milestone; roadmap auto-discovers if not specified)"
---

# Pipeline

## Core Rule

**ROADMAP IN, COMMITTED CODE OUT. EVERY MILESTONE PASSES CI AND REVIEW BEFORE COMMITTING.**

Do not skip steps, do not reorder phases, do not commit without human approval — unless `--auto` mode is active.

---

## Phase 1: Orient

1. **Parse mode flag.** If `$ARGUMENTS` contains `--auto`, enable auto mode (skip Phase 4 human review gate). Strip the flag before interpreting the rest as a file path.

2. **Locate the roadmap.** If `$ARGUMENTS` provides a file path, read that file. Otherwise auto-discover in this order:
   - `ROADMAP.md`
   - `MILESTONES.md`
   - `docs/ROADMAP.md`
   - `docs/MILESTONES.md`
   - `.github/ROADMAP.md`

   If no roadmap is found after checking all locations, **stop immediately**. Tell the user no roadmap was found and suggest running `/bender:roadmap` first.

3. **Read recent git history.** Run `git log --oneline -15` to understand what has been completed recently.

4. **Check for work in progress.** Run `git status` to detect uncommitted changes or in-progress work.

5. **Check project conventions.** Read `CLAUDE.md` if it exists, then `README.md`, to understand project patterns, constraints, and file maintenance protocols.

6. **Discover CI command.** Use this fallback chain (stop at first match):
   1. `bin/ci` exists → use it
   2. `CLAUDE.md` specifies a CI/test command → use it
   3. Auto-discover from project files:
      - `package.json` with `scripts.test` → `npm test` (or `yarn test`/`pnpm test`/`bun test` based on lockfile)
      - `Makefile` with `ci` or `test` target → `make ci` or `make test`
      - `Cargo.toml` → `cargo test`
      - `Gemfile` → `bundle exec rspec`
      - `go.mod` → `go test ./...`
      - `pyproject.toml` or `setup.py` → `pytest`
   4. If nothing found → **stop**. Tell the user no CI command was discovered and ask them to specify one.

7. **Parse dependency graph.** Scan milestones for IDs (`M<n>:` prefix) and `{depends: ...}` markers:
   - If IDs and dependency markers are present → build a directed graph
   - If IDs are present but no `{depends:}` markers → milestones without markers are independent
   - If no IDs anywhere → assume sequential (each depends on the previous)
   - Completed `[x]` items satisfy dependencies

---

## Phase 2: Select Milestone(s)

1. **Parse the roadmap** for incomplete `- [ ]` items.

2. **Evaluate the dependency graph** to find milestones whose dependencies are all satisfied.

3. **If 2+ milestones are independent and ready**, ask the user one question: run them in parallel worktrees or sequentially?
   - **Sequential:** pick the first ready milestone
   - **Parallel:** launch each in its own worktree branch (`pipeline/<milestone-id>`). Max 3 parallel worktrees at once; batch the rest.

4. **If only one milestone is ready**, select it and proceed.

---

## Phase 3: Implement (per-milestone loop)

### 3a — Scope and plan

Identify affected files, apply the narrow interpretation rule, write a 3–5 line summary (what, approach, files, out-of-scope). No pause for approval — pipeline trusts roadmap specificity.

### 3b — Implement with TDD

Follow standard bender practices: TDD, verification before completion claims, systematic debugging if anything breaks. No scope creep — each milestone implements exactly what the roadmap says.

### 3c — Run CI

Execute the discovered CI command.

- If CI fails: debug and retry using systematic-debugging practices.
- Cap at **3 consecutive CI failure → fix attempts**. If CI still fails after 3 attempts → **escalate to human**. Present the failures clearly and ask for guidance.

### 3d — Code review + auto-fix loop

1. Run `/bender:code-review`
2. If **must-fix** findings:
   - Fix them
   - Re-run CI
   - Re-review
   - Max **3 loop iterations**. If must-fix findings persist after 3 iterations → escalate to human.
3. **Should-fix** findings: attempt once. Include any remaining in the human summary.
4. **Consider** findings: note in human summary, don't act on them.

---

## Phase 4: Human Review Gate

**If `--auto` mode is active:** skip this phase entirely. Log the summary below to the conversation for traceability, then proceed directly to Phase 5.

**Otherwise**, this is the **only pause point** in the pipeline. Present a summary:

- Milestone item (verbatim from roadmap)
- What was implemented (concise list)
- CI status (pass/fail, command used)
- Code review verdict (pass, or remaining findings by severity)
- `git diff --stat` output
- Auto-fix iteration count (how many review→fix loops ran)

Wait for user response:
- **Approve** → proceed to Phase 5
- **Request changes** → apply changes, re-run CI + code review, re-present summary. Max **3 human review rounds** per milestone. If still not approved → stop and discuss.

---

## Phase 5: Commit and Doc Sync

1. **Fidelity check.** Re-read the milestone item verbatim from the roadmap. List what was implemented. Confirm the two match. If they don't → flag the delta to the user before committing.

2. **Commit.** Stage all changes and create a single conventional commit: `type(scope): description`. Do not push unless the user asks.

3. **Mark done.** Update the roadmap: change `- [ ]` to `- [x]` for the completed milestone.

4. **Doc sync.** Read `CLAUDE.md` for any file maintenance protocol. Update referenced docs as needed. If no protocol is found, only update the roadmap checkbox. All doc changes go in the same commit (amend the previous commit).

---

## Phase 6: Next Milestone

1. **Return to Phase 2** to select the next ready milestone.

2. **If parallel worktrees were used:**
   - Merge completed branches back (`--no-ff`)
   - If merge conflicts arise → present them to the user for resolution
   - Run CI on the merged result
   - Clean up worktree branches

3. **When all milestones are complete:** present a final summary:
   - Total milestones completed
   - Commits made (list with hashes)
   - Any deferred notes (should-fix/consider findings, out-of-scope observations)

---

## Hard Rules

- Never skip CI — every milestone passes before code review.
- Never skip code review — every milestone is reviewed before human approval.
- Never commit without human approval (Phase 4 gate is mandatory) — unless `--auto` mode is active, in which case CI + code review must still pass.
- Never mark done without fidelity check.
- Auto-fix loop capped at 3 attempts → escalate.
- Human review rounds capped at 3 per milestone.
- CI failures after 3 fix attempts → escalate.
- No scope creep — each milestone implements exactly what the roadmap says.
- Don't rewrite or reorder the roadmap — only mark items done.
- No roadmap found → stop immediately.
- Sequential milestones complete in order; only explicitly independent milestones may parallelize.
- Conventional commits only: `type(scope): description`.
- Max 3 parallel worktrees at once; batch if more are independent.
