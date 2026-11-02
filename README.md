# bender

Portable AI coding workflows for Codex and Claude Code, built and used by [The Bitfoot Company](https://github.com/bitfootco).

Bender packages practical, opinionated skills for planning, implementation, debugging, review, and delivery. The same `skills/` directory is distributed through the portable Agent Plugins manifest and Claude Code marketplace metadata, so both hosts execute the same workflows.

## Skills

| Skill | Codex | Claude Code | Purpose |
|---|---|---|---|
| `brainstorming` | `$brainstorming` | `/bender:brainstorming` | Explore and approve a design before implementation |
| `chunk` | `$chunk` | `/bender:chunk` | Isolate and implement one coherent kernel of code |
| `code-audit` | `$code-audit` | `/bender:code-audit` | Audit a repository or subsystem for evidenced risks |
| `code-review` | `$code-review` | `/bender:code-review` | Review a diff, branch, commit, path, or pending changes |
| `commit` | `$commit` | `/bender:commit` | Draft one Conventional Commit subject |
| `copywriting` | `$copywriting` | `/bender:copywriting` | Create concise copy within brand constraints |
| `inchstone` | `$inchstone` | `/bender:inchstone` | Execute one roadmap parent as surgical behavior slices |
| `milestone` | `$milestone` | `/bender:milestone` | Implement the next roadmap parent directly |
| `pipeline` | `$pipeline` | `/bender:pipeline` | Run a complete roadmap through implementation and review |
| `pr` | `$pr` | `/bender:pr` | Draft a high-level pull request description |
| `roadmap` | `$roadmap` | `/bender:roadmap` | Break an initiative into executable milestones |
| `summary` | `$summary` | `/bender:summary` | Explain what the current change ships |
| `systematic-debugging` | `$systematic-debugging` | `/bender:systematic-debugging` | Find root causes before applying fixes |
| `test-driven-development` | `$test-driven-development` | `/bender:test-driven-development` | Implement changes with red-green-refactor |
| `verification-before-completion` | `$verification-before-completion` | `/bender:verification-before-completion` | Require fresh evidence before completion claims |

Skills can also activate implicitly when a request matches their description. Explicit invocation is useful when you want a particular workflow or mode.

## Install for Codex

Add the GitHub repository as a marketplace, then install Bender:

```shell
codex plugin marketplace add bitfootco/bender
codex plugin add bender@bender
```

Use `/skills` in Codex to inspect the installed skills, or mention one with `$skill-name`.

## Install for Claude Code

From a Claude Code session:

```text
/plugin marketplace add bitfootco/bender
/plugin install bender@bender
```

Skills are namespaced under `bender:` to avoid conflicts with other Claude Code plugins.

### Claude Code team setup

To prompt teammates to install Bender when they trust a project folder, add this to `.claude/settings.json`:

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

## Local development

Codex can load the current checkout as a local marketplace:

```shell
codex plugin marketplace add .
codex plugin add bender@bender
```

Claude Code can load the checkout directly:

```shell
claude --plugin-dir .
```

Validate the cross-host package contract before publishing:

```shell
python3 -m unittest discover -s tests -v
```

Restart the host after changing installed plugin files if it does not detect the update automatically.

## Package layout

```text
plugin.json                    Portable Agent Plugins manifest
.claude-plugin/                Claude Code marketplace metadata
skills/<name>/SKILL.md         Shared workflow instructions
skills/<name>/agents/          Codex presentation metadata
skills/<name>/references/      Supporting material loaded when required
tests/                         Cross-host packaging contract
```

The root `skills/` directory is the single source of truth. Host-specific copies are intentionally not maintained.

## Philosophy

- **Root cause over symptom** — never fix what you do not understand
- **Evidence over assertion** — never claim something works without showing it
- **Design before code** — never build before you know what you are building
- **Test first** — the test suite is the specification
- **Fresh eyes on review** — review the evidence, not the implementation-session narrative
