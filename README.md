# bender

AI coding conventions and workflow skills for Claude Code, built and used by [The Bitfoot Company](https://github.com/bitfootco).

These are practical, opinionated skills for disciplined software engineering — the stuff that keeps code quality high and debugging sessions short. Install them once, use them across every project.

---

## Skills

| Skill | Invocation | When it activates |
|---|---|---|
| `systematic-debugging` | `/bender:systematic-debugging` | Auto — whenever Claude encounters a bug or test failure |
| `verification-before-completion` | `/bender:verification-before-completion` | Auto — before any "done", "fixed", or "tests pass" claim |
| `test-driven-development` | `/bender:test-driven-development` | Auto — when implementing features or fixing bugs |
| `brainstorming` | `/bender:brainstorming` | Auto — when starting new features or design decisions |
| `code-review` | `/bender:code-review` · `/bender:code-review branch` | Manual — no arg reviews uncommitted changes; `branch` reviews everything on the current branch vs. main |
| `milestone` | `/bender:milestone` · `/bender:milestone path/to/ROADMAP.md` | Manual — cold-start session skill: finds your roadmap, identifies the next incomplete item, scopes it, and implements it |
| `pr` | `/bender:pr` · `/bender:pr develop` | Manual — generates a high-level PR description from the current branch, copies it to the clipboard |
| `roadmap` | `/bender:roadmap` · `/bender:roadmap "goal description"` | Manual — breaks a large feature or initiative into sequenced, single-session milestones and writes them to `ROADMAP.md` |

**Auto** skills load when Claude determines they're relevant. **Manual** skills only run when you invoke them directly — `code-review` runs in a fresh subagent context so it has no bias from the implementing session. Use `roadmap` to plan, then `milestone` to execute session by session.

---

## Installation

From within any Claude Code session:

```shell
/plugin marketplace add bitfootco/bender
/plugin install bender@bender
```

Skills are namespaced under `bender:` to avoid conflicts with other plugins.

---

## Team setup

To have teammates automatically prompted to install when they trust a project folder, add to `.claude/settings.json` in your repo:

```json
{
  "extraKnownMarketplaces": {
    "bender": {
      "source": {
        "source": "github",
        "repo": "bitfootco/bender"
      }
    }
  },
  "enabledPlugins": {
    "bender@bender": true
  }
}
```

---

## Local development

To test changes live without installing:

```shell
claude --plugin-dir .
```

Skills reload on restart. Make a change, restart, test with `/bender:skill-name`.

---

## Philosophy

These skills encode the engineering principles The Bitfoot Company works by:

- **Root cause over symptom** — never fix what you don't understand
- **Evidence over assertion** — never claim something works without showing it
- **Design before code** — never build before you know what you're building
- **Test first** — the test suite is the specification
- **Fresh eyes on review** — the person who wrote the code is the worst person to review it
