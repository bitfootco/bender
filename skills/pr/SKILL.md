---
name: pr
description: Generate a GitHub pull request description from the current branch. Produces a high-level, markdown-formatted summary and copies it to the clipboard. Pass a base branch if it's not main/master.
argument-hint: "[base branch] (optional — defaults to main or master)"
---

# Pull Request Description

## Core Rule

**DESCRIBE WHAT CHANGED AND WHY — NOT EVERY LINE THAT MOVED.**

The output is a markdown PR description ready to paste into GitHub. It should tell a reviewer what this branch does, why it exists, and anything they should know before reviewing. It should not be a narration of the diff.

---

## Phase 1: Gather context

1. Identify the base branch. If `$ARGUMENTS` names one, use it. Otherwise try `main`, then `master`, then `trunk`. Confirm it exists before proceeding.
2. Run `git log --oneline $(git merge-base HEAD <base>)..HEAD` to get the commit history for this branch.
3. Run `git diff $(git merge-base HEAD <base>)..HEAD --stat` to get the file-level change summary.
4. Run `git diff $(git merge-base HEAD <base>)..HEAD` to read the actual changes.
5. Read any relevant context files (`README.md`, `CLAUDE.md`, `ROADMAP.md`) if they help explain the purpose of the work.

Understand the full scope before writing anything.

---

## Phase 2: Write the description

Produce a single markdown document with these sections:

### Format

```markdown
## Summary

One to three sentences explaining what this PR does and why.

## Changes

- Bulleted list of the meaningful changes, grouped logically
- Each bullet describes a feature, fix, or improvement — not a file
- Nest sub-bullets only when grouping related items under a theme

## Notes for reviewers

Anything a reviewer should know: areas of risk, design tradeoffs, things you'd like specific feedback on, or migration steps. Omit this section entirely if there's nothing worth calling out.
```

### Writing guidelines

- **Lead with intent.** The summary answers "what does this branch accomplish?" — not "what files were touched."
- **Be specific but high-level.** "Add rate limiting to the `/auth` endpoint (10 req/min per IP)" is good. "Modified `middleware/rateLimit.js` to add a counter" is not.
- **Group by feature, not by file.** If three files changed to support one behavior, that's one bullet.
- **Skip the obvious.** Don't mention formatting changes, import reordering, or lockfile updates unless they're the point of the PR.
- **No preamble or sign-off.** No "This PR does…" openers. No "Please review" closers. Just the content.
- **Match the branch's scope.** A single-commit bug fix gets a two-line summary and a couple of bullets. A multi-day feature branch gets a thorough breakdown. Scale to fit.

---

## Phase 3: Copy to clipboard

After writing the description, copy the raw markdown to the system clipboard:

- **macOS:** pipe to `pbcopy`
- **Linux:** pipe to `xclip -selection clipboard` or `xsel --clipboard --input`

Tell the user the description has been copied and is ready to paste into GitHub.

---

## Hard Rules

- Do not list individual files or line numbers in the description. Think features, not files.
- Do not pad with filler. If the PR is simple, the description should be short.
- Do not include a PR title — GitHub has a separate field for that. Output only the body.
- Do not fabricate changes. Every bullet must trace back to something in the diff.
- Always copy to clipboard. If the clipboard command fails, print the raw markdown as a fenced code block so the user can copy manually.
- Do not ask the user any questions. Gather everything you need from git and the codebase.
