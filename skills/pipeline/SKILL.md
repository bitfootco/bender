---
name: pipeline
description: Orchestrate a full roadmap-to-committed-code flow by delegating each parent to inchstone, independently inspecting verified changes, reviewing once per parent, and committing completed parents. Use when the user asks to run a whole roadmap or pipeline. Accept `--auto` to skip the parent review gate and `--parallel` for isolated independent worktrees.
---

# Pipeline

## Core Rule

**ROADMAP IN, COMMITTED CODE OUT. EACH PARENT GETS INCHSTONE-QUALITY EXECUTION, VERIFIED OWNERSHIP, REVIEW, AND A COMMIT.**

Pipeline owns parent selection, dependency order, attribution baselines, review gates, commits, roadmap markers, worktree integration, and the final summary. Delegate implementation and whole-parent technical verification to `inchstone`.

## Modes

- Default: execute ready parents sequentially and pause once for human review per parent.
- `--auto`: skip only the parent review gate. Continue to stop for material ambiguity, blockers, unsafe attribution, requirement conflicts, or failed verification.
- `--parallel`: execute only explicitly independent ready parents in isolated worktrees. Never infer parallel safety from convenience. Combine with `--auto` only when both flags are explicit.

Strip recognized flags before interpreting a roadmap path.

## Phase 1: Orient

1. Locate the supplied roadmap or check `ROADMAP.md`, `MILESTONES.md`, `docs/ROADMAP.md`, `docs/MILESTONES.md`, then `.github/ROADMAP.md`. Stop if none exists.
2. Read `git log --oneline -15`, `git status`, applicable `AGENTS.md` and `CLAUDE.md`, and relevant README sections.
3. Read the complete `inchstone` and `code-review` skills.
4. Discover CI from `bin/ci`, repository instructions, or project manifests. Stop and request a command if none can be determined.
5. Parse IDs, dependency markers, ordering, and completed items. Without IDs, treat parents as sequential. With IDs but no dependency markers, treat them as independent only when the roadmap explicitly says so.
6. Record outside the repository the initial `HEAD`, status including untracked files, full unstaged diff, and full staged diff. Treat all recorded work as user-owned.

## Phase 2: Select Parent Work

Find incomplete parents whose dependencies are satisfied. Sequential mode selects the first ready parent. Do not ask whether to parallelize; parallel execution occurs only with explicit `--parallel`.

For `--parallel`, select only ready parents whose implementation code, data, migrations, generated artifacts, parent-branch documentation, and acceptance criteria are demonstrably independent. Centralized roadmap markers do not disqualify otherwise independent parents. If implementation independence is uncertain, run sequentially. Limit concurrent workers to available agent capacity and at most three parent worktrees; batch the rest.

Quote each selected parent verbatim and extract acceptance criteria, dependencies, exclusions, and repository constraints.

## Phase 3: Establish Isolation and Delegated Contract

Immediately before each delegation, capture a parent baseline containing `HEAD`, short status, full staged and unstaged diffs, and untracked paths. Stop if the parent needs a user-owned path or hunk.

In sequential mode, delegate in the current worktree. In parallel mode:

1. Create a dedicated branch `pipeline/<parent-id>` and isolated worktree from the same verified base.
2. Never copy uncommitted user work into a parent worktree.
3. Give each worktree its own temporary attribution workspace.
4. Do not allow workers to merge, commit, mark roadmap items, or clean up worktrees.
5. Give concurrent workers isolated databases, ports, caches, containers, and external test namespaces where the project supports them. Otherwise serialize full CI; focused tests may overlap only when their runtime state is isolated.

Pass inchstone exactly:

- repository worktree and roadmap paths;
- selected parent text verbatim and explicit acceptance criteria;
- dependencies, exclusions, repository constraints, CI command, and verified existing behavior;
- the parent attribution baseline and any pipeline-accepted patch manifest;
- delegated mode with automatic acceptance only for uniquely dominant kernels and approaches;
- an instruction to return every material ambiguity, requirement conflict, cross-chunk redesign, dirty-worktree overlap, blocker, unsafe attribution, or failed verification;
- ownership rules reserving commits, markers, dependency sequencing, integration, and the parent review gate to pipeline.

## Phase 4: Inspect Delegated Results

When inchstone returns, independently verify rather than trusting its report:

1. Compare the worktree with the parent and pipeline baselines.
2. Reconstruct the returned patch from its persisted hunk manifest and confirm it excludes all pre-existing and between-chunk user edits.
3. Confirm every accepted kernel and approach met the clear-dominance standard. If any recommendation concealed a meaningful tradeoff, stop and present it to the user.
4. Map every acceptance criterion to code and tests; trace unchanged callers and integration boundaries.
5. Inspect fresh focused-test, full-CI, slimming, and whole-parent review evidence.
6. Apply `code-review` independently to the exact parent-attributable patch. Route must-fix or behavior-changing findings back through delegated inchstone; do not edit implementation directly.
7. Re-run full CI after remediation. Stop on failed verification or uncertain ownership.

## Phase 5: Parent Review Gate

Present the only routine approval stop for the parent:

- parent item verbatim;
- completed kernels and automatically accepted choices;
- criterion-to-evidence map;
- CI command and result;
- inchstone and pipeline review verdicts;
- attributable `git diff --stat`;
- excluded user-owned changes and remaining findings.

Wait for approval or requested changes. Route requested implementation changes through delegated inchstone, reinspect, and present the gate again. Cap at three review rounds, then stop and discuss.

Ambiguity and safety decisions are exceptional mandatory stops, not additional routine review gates, and do not consume the parent review gate.

With `--auto`, log the same package and skip this gate only. Never skip ambiguity, safety, attribution, fidelity, review, or verification stops.

## Phase 6: Fidelity, Commit, and Marker

1. Re-read the parent verbatim and confirm the accepted patch exactly satisfies it. Stop on a narrower or broader result.
2. Capture a fresh status and full staged/unstaged diff immediately before staging. Compare it with the accepted manifest and prior baseline; classify every newly arrived hunk as user-owned and stop on overlap or uncertain attribution.
3. Stage only parent-attributable implementation changes. Never stage user-owned work.
4. In sequential mode, mark only the selected roadmap parent complete, follow required documentation protocols, validate the docs diff, and create one Conventional Commit containing implementation and marker/docs.
5. In parallel mode, commit only the verified implementation on its isolated branch. Do not edit roadmap markers there; marker ownership remains central for Phase 7.
6. Do not push unless requested. Record the commit hash, verification evidence, and deferred observations.

## Phase 7: Parallel Integration and Continuation

For `--parallel`, only integrate parent branches whose delegated work, independent inspection, review gate (unless `--auto`), fidelity check, CI, and implementation commit all succeeded.

Create a dedicated clean integration worktree from the verified target base. Immediately before each merge, capture its `HEAD`, status, and staged/unstaged diff; require it to contain only previously accepted pipeline integrations. Merge verified parent branches there in dependency-safe order. Stop for user resolution on conflicts; do not auto-resolve.

After each merge, compare the integrated tree with its baseline and the accepted parent manifest. Run full CI. If CI fails, stop with the batch unaccepted, preserve the recoverable integration branch and evidence, and isolate the failing interaction before advancing; never mark parents or continue selection through a failed batch.

After successful integration CI, centrally mark each integrated parent complete in dependency-safe order, follow documentation protocols, validate the marker/docs diff, and commit those centralized roadmap updates. Attribute that centralized commit to every parent it marks. Re-run full CI when repository protocol requires it.

Before updating the original target branch, verify its `HEAD`, status, and staged/unstaged diff still match the recorded target baseline. If it moved, became dirty, or overlaps the integration, stop. Otherwise fast-forward it to the verified integration branch, or merge the integration branch explicitly when a fast-forward is impossible, then confirm the target resolves to the verified integrated tree. Keep failed or ambiguous branches isolated. Remove worktrees and branches only after this handoff succeeds and cleanup is safe.

Return to parent selection until the roadmap has no ready incomplete work. Finish with completed parents, commit hashes, integrated parallel batches, verification commands, and deferred findings or blockers.

## Hard Rules

- Delegate every parent implementation to `inchstone`; pipeline never implements fixes directly.
- Sequential is the default. Parallel work requires explicit `--parallel`, proven independence, and isolated worktrees.
- Exactly one routine human gate occurs per parent; `--auto` skips only that gate.
- Material ambiguity always reaches the user, including under `--auto`.
- Pipeline alone owns commits, roadmap markers, dependency sequencing, worktree integration, and final reporting.
- Never commit, mark done, merge, or clean up when ownership, fidelity, review, or verification is uncertain.
- Never include pre-existing or between-chunk user edits in an accepted patch or commit.
