---
name: copywriting
description: Create or edit concise, brand-aware marketing, website, product, documentation, and editorial copy. Use for content writing and copy passes; do not activate for ordinary assistant replies, progress updates, or code-only tasks.
---

# Copywriting

Write useful copy that sounds like the brand, makes supported value clear, and guides the reader toward the intended outcome. Once the brand foundation is established, return the requested copy first. Add rationale only when requested or when a decision remains unresolved.

## Establish the brand

Find `BRAND.md` files from the target content directory to the project root. Apply the root guide first, then any nearer guide as a scoped override. An explicitly named guide wins; ask only when that choice creates an unresolved conflict.

If no `BRAND.md` exists:

1. Inspect existing site copy, product documentation, README material, and other reliable product evidence.
2. Explain that final copy needs an agreed brand foundation and draft a compact `BRAND.md` from the evidence.
3. Read [Brand setup](references/brand-setup.md), ask only the questions needed to resolve material gaps, and refine the draft iteratively.
4. Obtain confirmation before treating the guide as authoritative or producing final copy.
5. Save the confirmed guide at the project root, or in the relevant subtree when the repository clearly contains multiple brands. File creation still requires the user's requested write scope.

Provisional exploration copy is allowed while shaping the brand, but label it as provisional. Never invent positioning, proof, customer claims, metrics, or product capabilities.

When a guide exists, follow it. Ask about a gap only when it materially changes the requested copy; otherwise make the narrowest evidence-supported choice. Do not silently rewrite the brand guide during a copy task.

## Shape the content

Before writing, determine the audience, surface, desired reader action, and claims supported by the request or repository.

For marketing and product surfaces:

- Lead with the reader's outcome or a concrete value proposition.
- Connect features to benefits without turning every sentence into a slogan.
- Use specific proof when available and omit unsupported superlatives.
- Give each section one job and use one clear call to action where the surface calls for it.

For documentation:

- Optimize for successful use: accurate concepts, prerequisites, steps, examples, and recovery information.
- Preserve necessary technical detail and search-relevant terms.
- Use brand voice without inserting promotional language or calls to action into procedural material.

For every format:

- Prefer concrete verbs and familiar words.
- Remove filler, repeated claims, throat-clearing, inflated language, generic slogans, and unnecessary alternatives.
- Keep accessibility, meaning, technical accuracy, legal constraints, and existing information hierarchy intact.
- Match length to the surface. Concision means every sentence earns its place, not an arbitrary word limit.

When editing files, change only the requested content and preserve surrounding structure and formatting. Do not publish, deploy, or change product behavior unless separately requested.

## Deliver

Present ready-to-use copy in the requested structure. When facts or brand decisions remain unresolved, identify them briefly after the copy and keep affected wording provisional. Do not bury the deliverable beneath an essay about the writing process.
