---
name: code-review
description: Independently review code before committing or merging. Use for a diff, branch, commit, path, or pending changes; route whole-repository or subsystem audits to code-audit.
---

# Code Review

Act as an independent code reviewer. Prefer a fresh subagent context when the user explicitly requests independent or delegated review and subagent tools are available. Otherwise, review from the current context while relying on the diff and repository evidence rather than implementation-session assumptions.

Use `$code-audit` for an open-ended assessment of a repository or subsystem. Keep requests focused on a changeset, commit, or specified files in `$code-review`.

## What to Review

Determine scope from the user's request:

- **No argument** — run `git diff` and `git diff --cached` to get all uncommitted changes (staged and unstaged)
- **`branch`** — find the base branch (try `main`, then `master`, then `trunk`), then run `git diff $(git merge-base HEAD <base>)..HEAD` to get everything on the current branch not yet in the base
- **File or directory path** — read the file(s) and review in context of the surrounding codebase
- **Git ref** (e.g. `HEAD~3`, a commit SHA) — run `git diff <ref>` to get that changeset

Read the relevant code. Understand what it's trying to do before evaluating it.

## Review Checklist

Work through each section. Do not skip.

### Correctness
- Does the code do what it's supposed to do?
- Are there edge cases or inputs that would cause incorrect behavior?
- Are error conditions handled, or silently swallowed?
- Are there any obvious logic errors?

### Spec Compliance
- Does this match the visible intent (adjacent code, comments, test names, function names)?
- Is anything clearly missing from what was attempted?

### Test Coverage
- Is there test coverage for the new behavior?
- Do the tests cover failure paths, not just the happy path?
- Would a test catch a regression if this code changed?

### Security
- Is any user input reaching the filesystem, database, shell, or network without validation or sanitization?
- Are credentials, tokens, or sensitive values handled safely?
- Are there any injection risks (SQL, shell, path traversal)?

### Code Quality
- **DRY** — is logic duplicated that could be shared? Are there copy-paste patterns that should be extracted?
- **Single responsibility** — are functions or modules doing more than one distinct thing?
- **Naming** — do names accurately describe what the thing is or does? Would a new reader be misled?
- **Complexity** — is any function or block harder to follow than it needs to be? Could it be broken up?
- **Error handling** — are errors surfaced clearly or swallowed silently?

### YAGNI
- Is there code that isn't called or used anywhere?
- Is there abstraction serving a use case that doesn't exist yet?
- Is anything more complex than the current requirements justify?

### Readability
- Would someone unfamiliar with this code understand what it does?
- Is anything surprising that should be explained with a comment?

## Report Format

Group findings by severity:

**Must fix** — correctness bugs, security issues, missing required behavior. Block commit/merge until resolved.

**Should fix** — test gaps, readability problems, unnecessary complexity. Address before merging if possible.

**Consider** — style preferences, optional improvements, open questions about intent. Non-blocking.

For each finding:
- File and line number
- What the problem is
- A concrete suggestion for fixing it

Close with a one-line verdict: what's the overall state and is it ready to commit?
