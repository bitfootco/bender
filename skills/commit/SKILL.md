---
name: commit
description: Generate one concise Conventional Commit subject for the current uncommitted work. Use when the user invokes $commit or asks for a one-line, scoped, conventional commit message for recent or pending changes. Inspect the repository and return a message only; never create the commit.
---

# Commit Message

## Gather evidence

1. Run `git status --short`, `git diff HEAD --stat`, and `git diff HEAD`.
2. Run `git log -25 --pretty=format:%s` to learn the repository's established types, scopes, and tone.
3. Read surrounding code only when the diff does not make the change's intent clear.
4. If there are no uncommitted changes, say `No uncommitted changes to describe.` and stop.

## Compose the subject

Use this exact form:

`type(scope): summary`

- Choose the type by intent: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `build`, `ci`, `style`, or `revert`.
- Infer the narrowest meaningful scope from the behavior's owner and the repository's recent scope vocabulary. Prefer the production area over `test` when tests support a production change.
- Describe the coherent outcome, not file operations or implementation trivia.
- Use imperative, present-tense wording; start lowercase; omit the final period.
- Keep the entire subject concise, preferably at most 72 characters.
- Do not invent ticket numbers, breaking-change markers, or motivations absent from the diff.

## Output contract

Return exactly one plain-text line. Do not use Markdown, quotes, explanation, alternatives, a body, or a sign-off. Do not stage files or create a commit.
