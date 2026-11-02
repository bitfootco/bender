---
name: inchstone
description: Execute one roadmap or milestone parent through sequential, simplicity-first behavior slices. Use when the user invokes `$inchstone` or explicitly asks to execute a roadmap parent surgically, incrementally, or as chunks. Authorize the parent once, verify each slice with targeted checks, and reserve full CI for the final review gate. Delegated pipeline mode returns verified changes without committing or marking the roadmap.
---

# Inchstone

Complete one roadmap parent through bounded, sequential behavior slices. Keep
scope, attribution, TDD and simplicity checks explicit throughout; review the
combined result independently before final CI and completion.

## Core Rule

**BOUND THE PARENT. IMPLEMENT ONE COHERENT BEHAVIOR AT A TIME. VERIFY AND SIMPLIFY BEFORE ADVANCING. MARK DONE ONLY WHEN THE WHOLE PARENT MATCHES.**

A slice has one observable purpose and a reviewable acceptance boundary. Prefer
vertical slices that carry a behavior through its relevant domain, transport,
storage, adapter and UI paths. Crossing files or languages does not make a slice
too broad. Split when behaviors are independently valuable, risks need isolation,
or the result would be difficult to verify and review together. Do not split
mechanically by architectural layer or bundle unrelated cleanup.

Unlike direct milestone implementation, retain explicit intermediate behavior
boundaries, targeted evidence and a simplicity check before starting the next slice.

## Modes and Ownership

### Standalone

Agree one bounded parent execution brief, then own routine implementation decisions
within it. Existing explicit authorization, including a request to proceed without
routine approvals, satisfies this gate; do not ask again. Ask only for a material
decision outside that authorization or a genuine permission requirement. Own final
verification and review, then mark only the selected parent complete.

### Delegated pipeline

Pipeline supplies one selected parent and its authorization, dependencies,
acceptance criteria, exclusions, attribution baseline and accepted patches.
Pipeline owns sequencing, integration, commits and roadmap markers. Inchstone
returns attributable verified changes and must not commit or mark the parent.
Request only missing contract details that prevent safe progress.

### Using `chunk`

Read `chunk` and retain its end-to-end tracing, evidence-based approach selection,
TDD and slimming discipline. This controller supplies the parent authorization and
sets the following execution rules for its slices:

- Choose and briefly record the next behavior, approach and targeted checks.
  Proceed directly when repository evidence clearly favors the existing path.
- Compare alternatives only when materially different viable options exist. Do
  not manufacture candidate lists or repeat research for settled contracts.
- Routine decisions need neither a worker proposal/authorization round trip nor
  separate user gates. These controller rules replace `chunk`'s direct approval
  gates, per-slice decision packets and broad-CI cadence for this execution only.
- Reassess when evidence invalidates the approach. Resolve routine engineering
  choices within the brief; escalate meaningful product, compatibility, safety or
  scope tradeoffs beyond it. Adding a file or changing an internal representation
  does not by itself require approval.

Direct `$chunk` invocations keep their own approval rules. Authorization never
permits unsafe attribution, scope expansion or bypassing failed verification.

## Verification and Command Cadence

- Use the smallest meaningful failing behavior test, implement, then refactor while
  green. Verify affected callers and integration boundaries, not just new helpers.
- After each slice, run targeted tests and relevant type/build/lint checks.
  Incremental compilation is suitable when supported; emitted tests must use current
  output. Reuse independent retained behavior or adapter fixtures where useful.
- Run no full CI entrypoint during intermediate slices. Reserve full CI, required
  packaging and phase-wide checks for the final gate, after combined review and
  targeted remediation. The gate defaults to parent completion; an explicitly
  agreed aggregate gate may cover multiple parents, which remain awaiting it.
- Broaden targeted checks when an actual dependency, failure or unresolved concern
  warrants it. Reuse passing evidence while its code and dependencies are unchanged;
  do not repeat checks merely for handoffs, read-only review or documentation edits.
- Prefer direct repository commands already covered by execution permissions and
  the narrowest suitable checks. Batch independent reads. Avoid unnecessary shell
  wrappers, pipelines, dependency installs and repeated packaging. Never reshape a
  command to evade approval; request permission only when genuinely required.
- Discover conflicting repository verification requirements before implementation
  and resolve them against explicit user instructions. Do not silently skip required
  checks or describe targeted evidence as overall project health.

Supply this cadence to any delegated implementer. It replaces broader per-slice
requirements in supporting skills, while preserving their behavioral testing and
fresh-evidence requirements.

## 1. Orient Once

1. Locate and read the roadmap, recent history, working-tree status and applicable
   contributor instructions. Use the supplied roadmap path or standard repository
   roadmap locations; stop if none exists. Read only relevant supporting documentation.
2. Identify targeted verification commands and the final CI/review gate.
3. Record the parent baseline outside the repository: HEAD, status including
   untracked files, staged and unstaged diffs, and affected pre-existing file
   contents needed to attribute later edits. Preserve unrelated work.
4. Reuse this context through the parent. Re-read when evidence or external changes
   invalidate it, rather than restarting orientation for every slice.

Treat pre-existing work as user-owned unless earlier accepted patches or explicit
authorization establish otherwise. Stop on unsafe overlap or uncertain attribution.

## 2. Bound and Authorize the Parent

Select the first clearly ready parent, or use exactly the delegated parent. Ask
one focused question if equally ready choices lack a clear ordering. Quote its
text and identify observable acceptance criteria, dependencies, exclusions,
already satisfied behavior and remaining work.

Present one concise execution brief: the outcome and boundary, recommended first
vertical slice and approach, a revisable sequence, targeted checks and final gate.
Include alternatives only for a real unresolved tradeoff. Trace shared integration
constraints early so interface and lifecycle failures surface before broad porting.

Obtain approval only when the existing session or pipeline contract does not already
authorize the brief. After authorization, continue sequentially without routine
gates. Re-plan within scope as evidence changes; ask when a meaningful decision
exceeds the agreed brief or observable completion cannot be determined.

## 3. Implement, Verify and Simplify Each Slice

### Keep context with the implementer

Use the current implementer by default across closely related slices. Delegate
when an isolated task or context reset provides a concrete benefit; do not rotate
workers merely because a slice ended. A fresh perspective is most valuable for
independent final review. Never run implementation workers concurrently in the
same worktree.

Give a delegated implementer the parent contract, relevant established interfaces,
attribution baseline and verification cadence. Within that authorization, let it
research and implement routine slices without returning an approval packet for
each one. Keep unresolved material decisions with the controller.

### Carry one behavior through

1. Check for external changes against the last accepted snapshot before editing.
   Trace the chosen behavior through relevant callers, persistence and failure
   boundaries. Reuse established contracts; investigate only new uncertainties.
2. Record the slice purpose, chosen approach and checks briefly. Implement using
   TDD, keeping the repository valid and the behavior independently verifiable.
3. Integrate the relevant layers early. Do not accumulate disconnected domain,
   protocol and facade implementations solely to keep each patch tiny.
4. Run targeted verification. Diagnose unexpected failures before changing more
   code; reassess the approach if evidence invalidates it.
5. Read the attributable diff as one behavior and trace affected consumers. Remove
   unnecessary concepts, duplicated rules, pass-through layers, speculative
   generality and implementation-mirroring tests. Re-run checks invalidated by
   corrections; a passing test alone does not establish a simple design.
6. Accept only attributable changes. Retain an exact accepted patch, including new
   files, and enough before/after evidence outside the repository to establish
   ownership. Reuse the parent baseline plus incremental snapshots; do not copy
   the entire workspace or rebuild the same full evidence packet per slice.
7. Map the newly satisfied behavior to the parent and choose the next slice. Keep
   routine notes brief; intermediate verification never marks the parent complete.

## 4. Final Review and Verification Gate

1. Re-read the parent verbatim and map every acceptance criterion to code and fresh
   applicable evidence. Report narrower or broader coverage rather than marking
   an incomplete parent done.
2. Assemble the combined attributable diff from the baseline and accepted patches.
   Never infer ownership from an unexplained dirty working tree.
3. Apply `code-review` independently of implementation and check cross-slice
   simplicity, integration and recovery behavior. A fresh reviewer may help when
   available and authorized; review must still trace the actual code and callers.
4. Resolve must-fix findings and run affected targeted checks. Re-review corrections
   before the final CI invocation.
5. Run full CI against the reviewed implementation, including required packaging
   and platform checks. Diagnose failures with targeted checks, fix and review,
   then rerun the invalidated final gate. Repeat successful broad checks only when
   subsequent changes invalidate them.
6. Complete only after criterion coverage, attribution, review and required final
   verification all succeed. Disclose material limits and unresolved obligations.

## 5. Return and Documentation

In delegated mode, return the criterion-to-evidence map, exact attributable patch,
targeted and final verification results, review verdict, excluded user work and
remaining limits. Pipeline owns commits and markers.

In standalone mode, mark only the selected parent complete after its final gate.
Maintain existing documentation sources at parent boundaries; record material
contract or product decisions promptly when needed. Avoid per-slice roadmap
annotations, repeated test-count updates and repository session diaries. Validate
documentation edits and keep the final report concise and self-contained.

## Hard Rules

- One parent per invocation unless the user explicitly authorizes a broader block;
  one coherent implementation slice at a time.
- Preserve scope, attribution, TDD, targeted verification and per-slice slimming.
- Existing authorization persists; meaningful out-of-scope decisions and genuine
  execution permissions remain gates.
- No full CI before the final review gate; no completion claims before required
  review and fresh final verification.
- No automatic commits or roadmap markers in delegated mode.
- Never sacrifice correctness or recovery guarantees to reduce process overhead.
