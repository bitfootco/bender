---
name: code-audit
description: Audit a repository, package, or directory for evidenced correctness, security, reliability, scale, test, performance, and complexity problems. Use for whole-codebase or subsystem audits; use code-review for a diff, branch, commit, or pending changes.
---

# Code Audit

Produce a read-only, evidence-based audit of the requested scope. Do not edit code, create tickets or roadmaps, or add the audit to pipeline gates unless the user separately asks.

## Map the system

- Audit the named repository, package, or directory; default to the current repository.
- Read applicable contributor guidance, the README, dependency and build files, deployment configuration, entry points, and representative tests.
- Trace the highest-risk flows end to end: trust boundaries, authentication, money, persistence, destructive operations, background work, and shared state.
- Derive load and operating assumptions from repository evidence. State assumptions that materially affect findings.
- For a large scope, prioritize costly failures instead of scanning every file equally. Record meaningful coverage limits.

## Find consequential problems

Prioritize:

1. Incorrect behavior, broken contracts, crashes, and inconsistent business rules.
2. Security vulnerabilities, exposed secrets, unsafe input handling, and data-loss paths.
3. Concurrency and scale failures under the supported operating model.
4. Risky behavior that lacks a test capable of detecting regression.
5. Material performance problems on demonstrated hot or high-volume paths.
6. Unnecessary code, dependencies, duplication, pass-through layers, speculative options, and responsibilities that should be separated.

Complexity is a finding only when it has a concrete present-day cost. A single implementation, wrapper, or abstraction is not inherently defective.

## Validate every finding

- Show a concrete input, state, call path, or maintenance failure for every finding. If repository evidence cannot establish the scenario, report it as an unverified assumption or omit it.
- Trace relevant callers and callees. Before declaring code unused, search tests, fixtures, configuration, generated use, registration, reflection, and string references.
- Distinguish observed defects from assumptions that require runtime, production, or domain evidence.
- Run focused read-only checks when they materially confirm or reject a finding. Do not present an unrun check as evidence.
- Recommend the smallest fix that addresses the cause while preserving validation, error handling, security, accessibility, and explicit requirements.
- Exclude style preferences, vague concerns, and speculative future architecture.

## Report

Begin with a short description of the system, audited scope, and material operating assumptions. List no more than the ten highest-value confirmed findings, numbered across these groups:

- **Must fix:** correctness, security, data loss, or failure under supported operation.
- **Should fix:** meaningful test gaps, performance costs, duplication, or complexity with demonstrated impact.
- **Consider:** verified lower-impact improvements.

For each finding include:

- a concise title with file and line;
- the relevant behavior;
- the concrete failure or cost;
- the smallest suitable fix;
- the consequence of leaving it unresolved.

Close with a one-line verdict and `Coverage limits:` describing important areas or runtime behavior not verified. If there are no confirmed findings, say that none were found in the inspected scope; do not claim the entire system is healthy.

Do not estimate lines or dependencies removable unless the audit demonstrates an exact count.

## Attribution

This workflow is adapted from Dietrich Gebert's Ponytail `ponytail-audit` skill under the MIT License. See [LICENSE](LICENSE).
