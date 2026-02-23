---
name: systematic-debugging
description: Use when encountering any bug, test failure, unexpected behavior, or when a previous fix attempt did not work. Use before proposing any solution.
---

# Systematic Debugging

## Core Rule

**NO FIXES WITHOUT ROOT CAUSE FIRST.**

Random fixes mask the real problem and create new bugs. The four phases below are mandatory — skip none, in any order.

## The Four Phases

### Phase 1: Understand the Failure

Before touching any code:

1. **Read the full error** — full stack traces, line numbers, error codes. Don't skim past the first line.
2. **Reproduce it reliably** — if you can't reproduce it consistently, you don't understand it yet. Find the minimal reproduction case.
3. **Scope the blast radius** — what changed recently? (`git log --oneline -20`) What are the exact conditions that trigger it vs. conditions where it does not occur?
4. **Trace the data flow** — follow the failing value or execution path from entry point to failure point. Use `Grep`, `Read`, and `Glob` to trace through the actual code — do not reconstruct from memory.

### Phase 2: Find the Pattern

1. **Find working examples** — locate code that does something similar and succeeds. Compare it completely against the failing code, not just the parts that seem relevant.
2. **Diff working vs. broken** — identify every difference. The bug is often in a difference you initially dismissed.
3. **Map dependencies** — what does the failing code depend on? Have any of those changed?

### Phase 3: Form and Test a Hypothesis

1. **State your hypothesis explicitly** — "The bug is caused by X because Y." If you can't state it clearly, you're not ready to fix it.
2. **Make the smallest possible change** to test the hypothesis.
3. **One variable at a time** — never bundle multiple changes into a single attempt.
4. **Confirm the hypothesis is correct** before writing a permanent fix.

### Phase 4: Fix

1. **Write a failing test first** that captures the exact failure condition.
2. **Implement the minimal fix** targeting only the confirmed root cause.
3. **Run the full test suite** — not just the one test you just wrote.
4. **Verify with fresh evidence** — show the output, don't assert it passes.

## Hard Stops

**Stop and restart from Phase 1 if any of these are true:**

- Three or more fix attempts have failed
- Each fix attempt reveals a new problem (whack-a-mole)
- You are about to try a fix but cannot explain why it should work

These are signals you have not found the root cause. More fixes will not help.

**Never:**

- Propose a fix before completing Phase 1
- Bundle multiple changes in a single fix attempt
- Write "this should fix it" — verify that it does

## Common Root Cause Patterns

| Pattern | How to Diagnose |
|---|---|
| Wrong assumption about state | Log or inspect the actual value vs. assumed value at the failure point |
| Timing / ordering issue | Trace the exact sequence of events; add timestamps or counters |
| Interface mismatch | Check the actual contract: types, required fields, return shape |
| Environment difference | Diff the environment where it works vs. where it fails |
| Regression | `git log` or `git bisect` to find the introducing commit |
| Off-by-one / boundary | Test with values at, above, and below the boundary |
