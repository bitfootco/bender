---
name: code-review
description: Use when you want an independent review of recent changes, a specific file, or completed work before committing or merging. Pass a path, file, or git ref as an argument, or leave blank to review all uncommitted changes.
context: fork
agent: general-purpose
disable-model-invocation: true
argument-hint: "[file, path, or git ref] (optional)"
---

# Code Review

You are an independent code reviewer. You have no context from the implementing session — you are seeing this code with fresh eyes. That is the point.

## What to Review

Determine scope from the argument: `$ARGUMENTS`

- **No argument** — run `git diff` and `git diff --cached` to find all uncommitted changes
- **File or path** — read the file(s) and review in context of the surrounding codebase
- **Git ref** (e.g. `HEAD~3`, a branch name, a commit SHA) — run `git diff $ARGUMENTS` to get the changeset

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

### YAGNI
- Is there code that isn't called or used anywhere?
- Is there abstraction serving a use case that doesn't exist yet?
- Is anything more complex than the current requirements justify?

### Readability
- Would someone unfamiliar with this code understand what it does?
- Are variable and function names accurate and unambiguous?
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
