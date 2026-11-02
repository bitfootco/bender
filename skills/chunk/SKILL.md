---
name: chunk
description: Isolate, research, compare, implement, and simplify exactly one coherent kernel of code. Use when the user invokes `$chunk`, asks to decompose work into one small surgical slice and compare implementation options before editing, or asks to trace and implement one recurring simplification across a large diff. Accept `$chunk [plan-or-slice]` and `$chunk review [branch|path|git-ref]`. Do not use for broad milestone execution, ordinary feature implementation, brainstorming alone, or report-only code review.
---

# Chunk

Implement one independently valuable idea with the least code and fewest concepts the repository can support.

## Core Rules

**ONE KERNEL. RESEARCH FIRST. COMPARE REAL OPTIONS. GET AUTHORIZATION. THEN EDIT.**

- Treat correctness and explicit requirements as constraints, not tradeoffs.
- Prefer deleting, inlining, or extending an existing pattern over adding a new layer.
- Add an abstraction only when it reduces code or concepts in the current change.
- Never mix adjacent cleanup, speculative reuse, or a second behavior into the chunk.
- Never edit code before the applicable authorization contract has passed.
- Never mark a broader parent roadmap or milestone item complete. If the selected kernel exactly equals the source item, update its marker only when the user requested roadmap maintenance and every acceptance criterion is verified.

## Inputs and Modes

### Authorization modes

Direct `$chunk` invocations use the two explicit approval gates below. A controller
skill may instead supply a previously user-approved execution brief that:

- names the parent boundary and acceptance criteria;
- authorizes sequential kernel work within that boundary;
- defines when the controller may accept a recommendation; and
- requires escalation for material ambiguity or departure from the brief.

Under that contract, return kernel selection and its approach comparison together.
The controller may authorize both in one recorded decision. This exception does not
let the worker choose silently, widen scope, or resolve a material tradeoff. If the
contract is absent or incomplete, use the direct gates.

### Plan mode

Use for direct prose, a plan section, a whole milestone, or a roadmap path. If no source is given, discover it in this order:

1. `ROADMAP.md`
2. `MILESTONES.md`
3. `docs/ROADMAP.md`
4. `docs/MILESTONES.md`
5. `.github/ROADMAP.md`

Stop if no request or plan source exists. Do not invent work.

### Review mode

Use when invoked as `$chunk review [scope]` or when the request explicitly asks to implement one simplification across existing changes. Route report-only review requests to `code-review`; do not edit for them.

- No scope: staged and unstaged changes
- `branch`: current branch from its merge base with `main`, `master`, or `trunk`
- Path: changes and surrounding code for that file or directory
- Git ref or range: that changeset

Review mode is not a report-only audit. It identifies candidate kernels, then follows the same approval and implementation workflow as plan mode.

## Phase 1: Orient

Before proposing a kernel:

1. Read `git status` and a bounded recent history sample. Preserve unrelated user work.
2. Read repository-root and affected-subtree `AGENTS.md` or `CLAUDE.md` files, plus only the README sections needed to understand the affected behavior.
3. Discover the project's test and CI commands.
4. Read the source request or plan text. In review mode, read the complete diff for the requested scope.
5. Map the relevant behavior in repository context. Search definitions, callers, tests, data flow, and existing utilities; do not reason from filenames or changed lines alone.

For a large diff, cluster changes by behavior or repeated idea rather than by file. Include unchanged consumers when tracing each cluster.

## Phase 2: Select One Kernel

A kernel is one coherent behavior or simplification that:

- has one observable purpose;
- can be implemented and verified independently;
- leaves the repository in a valid state; and
- does not require bundling unrelated cleanup.

Decompose broad input into candidate kernels. Rank them by dependency readiness, value, risk reduction, and how cleanly they can be isolated. In review mode, favor repeated complexity, parallel implementations of one rule, removable indirection, and concepts introduced more than once.

Present at most three candidates. For each, state:

- the kernel in one sentence;
- why it is independently valuable;
- likely affected behavior, not a speculative file list;
- what remains outside it; and
- why it ranks where it does.

**Direct approval gate 1:** Ask the user to select a kernel. Do not continue until
the selection is explicit. Under a valid controller contract, trace the recommended
kernel immediately and include the other candidates in the combined decision packet.

## Phase 3: Trace and Compare Approaches

After selection, trace the kernel end to end:

- locate every relevant entry point, caller, state transition, persistence boundary, and output;
- read covering tests and nearby repository conventions;
- distinguish required behavior from incidental current structure;
- identify code that can be removed or reused; and
- note compatibility, migration, security, or failure-path constraints.

Generate every materially distinct, repository-supported approach. Consider these shapes when they are real options:

1. Direct surgical insertion at the existing decision point
2. Reuse or extension of an existing seam
3. Replacement or deletion of an unnecessary path
4. No code change because the behavior already exists

Do not pad the comparison with cosmetic variants or hypothetical architectures. Reject an approach immediately if another option provides the same behavior with no extra risk and fewer concepts.

Rank viable approaches lexicographically:

1. Correctness and complete requirement coverage
2. Fit with current repository conventions and data flow
3. Fewer concepts, branches, files, and lines changed
4. Readability at the call site and in the main execution path
5. Ease of testing and diagnosing failures
6. Reversibility and compatibility

Lines of code are evidence, not the goal. A slightly longer direct implementation may beat a short abstraction when it is easier to read locally. An abstraction wins only when it reduces present-day duplication or removes more concepts than it adds.

Present up to three viable approaches with concrete repository evidence, explicit tradeoffs, and one recommendation. Include a short rejected-options note so the search is auditable.

**Direct approval gate 2:** Ask the user to approve an approach. Do not edit before
approval. Under a valid controller contract, return this comparison with kernel
selection and wait for the controller's single recorded authorization.

## Phase 4: Implement Surgically

After approval:

1. State the exact behavior boundary and what will not change.
2. Use test-driven development: add the smallest failing behavior test, confirm the failure, implement the minimum change, then refactor while green.
3. Touch only files required by the chosen approach. Reuse the repository's names, control flow, error handling, and test style.
4. Keep the main path linear. Prefer values over wrappers, functions over objects, local logic over new modules, and one representation of each fact.
5. Do not add configuration, extension points, generic helpers, compatibility layers, comments that restate code, or defensive branches without a current requirement.
6. If implementation evidence invalidates the approved approach, stop and return to Phase 3. Do not improvise a new design.
7. If a test fails unexpectedly, apply systematic debugging before changing more code.

## Phase 5: Verify and Slim

Run the focused tests, then the broadest available CI or test command. Do not claim completion without fresh successful output.

Review the final diff as one kernel, not file by file:

1. Re-read the selected kernel and approved approach.
2. Trace the behavior through every affected use, including unchanged callers.
3. List each new concept: type, object, helper, branch, state, configuration value, and dependency.
4. For each concept, ask whether deleting, inlining, combining, or using an existing construct preserves clarity and behavior.
5. Search for duplicated rules, parallel representations, pass-through wrappers, dead paths, speculative generality, and tests coupled to implementation details.
6. Make only mechanical simplifications inherent in the approved approach, keeping tests green after each change. Return to Phase 3 for approval before adding a file, deleting behavior, changing a representation, materially changing control flow, or otherwise departing from the approved design.
7. Re-run focused tests and full verification after slimming.

Finish with:

- the kernel completed;
- the chosen approach and why it won;
- tests and verification run;
- code or concepts removed or avoided;
- remaining parent-plan work and whether its completion marker changed under the exact-match rule.

## Invocation Examples

- `$chunk ROADMAP.md — take the next small slice`
- `$chunk "add retry handling from milestone 3"`
- `$chunk review branch`
- `$chunk review path/to/subsystem`
