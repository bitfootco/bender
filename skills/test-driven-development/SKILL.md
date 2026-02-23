---
name: test-driven-development
description: Use when implementing any new feature, fixing a bug, or refactoring existing code. Enforces red-green-refactor discipline throughout.
---

# Test-Driven Development

## Core Rule

**NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.**

Write the test. Watch it fail for the right reason. Write the minimum code to make it pass. Refactor. Repeat.

This is not a guideline. If code exists before its test, delete the code and start over.

## The Cycle

### RED — Write a failing test

1. Write the smallest test that demonstrates the missing behavior.
2. Run it. Confirm it **fails** — and fails for the right reason (the feature doesn't exist, not a setup error, not a typo in the test).
3. Do not proceed until you have a legitimate red state.

### GREEN — Write the minimum code to pass

1. Write only the code needed to make the test pass. Nothing more.
2. Resist the urge to build the "real" implementation — that's what refactor is for.
3. Run the test. Confirm it passes.
4. Run the full suite. Confirm nothing else broke.

### REFACTOR — Clean up

1. Improve the implementation without changing behavior.
2. Tests must stay green throughout. If a test goes red, the refactor broke something.
3. Remove duplication. Clarify intent. Do not add new behavior here.

Repeat for the next behavior.

## Hard Rules

- Watching the test fail is **mandatory**. A test written after the code proves nothing — it will pass immediately regardless of whether it's testing the right thing.
- Any code written before its test **must be deleted** and rewritten after a failing test exists. "I'll use it as a reference while I write the test" is rationalization.
- "I'll add tests after" is not TDD. It is writing code twice, in the wrong order.
- Manual testing does not substitute for an automated test suite.

## What Makes a Good Test

- **Minimal** — tests one behavior, not a whole workflow
- **Named clearly** — the name describes the expected behavior, readable as a sentence
- **Tests behavior** — not implementation details or internal state
- **Uses real inputs** — prefer real values over mocks where the real thing is practical

## Common Rationalizations to Reject

| Rationalization | Response |
|---|---|
| "This code is too simple to need a test" | Simple code has simple tests. Write it. |
| "I'll add tests once the API stabilizes" | The tests help stabilize the API. Write them first. |
| "There's no time for TDD right now" | TDD is faster than debugging untested code later. |
| "It's already written, I'll just test it now" | Delete it. Rewrite it after the test. |
| "I need to see it working before I can write a test" | Write the test for how it should work. That's the point. |
