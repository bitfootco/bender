---
name: verification-before-completion
description: Use before claiming any work is complete, fixed, or passing. Use before every "done", "fixed", "tests pass", or "it's working" statement.
---

# Verification Before Completion

## Core Rule

**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

"Should work", "probably passes", and "looks good" are not verification. Run the command. Show the output.

## The Verification Gate

Before any completion claim, you must:

1. **Identify** the exact command that proves the claim
2. **Run it fresh** — not a cached result, not a result from earlier in the session
3. **Show the full output** — not a summary, not selected lines
4. **Confirm it supports the claim** — check the exit code, specific output, and absence of unexpected warnings

Then state your conclusion with the evidence attached.

## Prohibited Language

Stop immediately if you catch yourself writing any of these:

- "This should fix..."
- "The tests probably pass..."
- "It looks like it's working..."
- "I believe this is correct..."
- "This ought to..."

These phrases signal you are about to make an unverified claim. Run the verification first.

## What Counts as Verification

| Claim | Required Evidence |
|---|---|
| "Tests pass" | Run the test suite, show full output and exit code |
| "Bug is fixed" | Reproduce the original failure, show it no longer occurs |
| "Build succeeds" | Run the build, show successful completion |
| "No lint errors" | Run the linter, show clean output |
| "Feature works" | Exercise it against the actual requirement, show the result |
| "All tests pass" | Run the project's full CI or test suite command (not a single file), show output and exit code |

## What Does Not Count

- A test run from earlier in the session
- An agent's report that it passed
- Reading the code and judging it correct
- A passing linter when the claim is about runtime behavior
- Partial output that shows only selected lines

Each claim requires its own fresh verification run.

## CI / Full Suite Verification

When the claim involves overall project health ("tests pass", "everything works", "ready to commit"), verification must include the project's CI or full test suite — not just the tests you wrote or modified this session.

Discover the CI command via: `bin/ci` → `CLAUDE.md` → auto-discover from project files (`package.json`, `Makefile`, `Cargo.toml`, etc.). If no CI command is found, run the broadest test command available.

Running a single test file that passes does not verify that other tests weren't broken.
