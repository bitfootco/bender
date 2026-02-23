# bender

A personal Claude Code plugin with skills for disciplined software engineering.

## Skills

| Skill | Invocation | Purpose |
|---|---|---|
| `systematic-debugging` | `/bender:systematic-debugging` | Four-phase root cause debugging before any fix attempt |

More coming: `verification-before-completion`, `test-driven-development`, `code-review`, `brainstorming`.

## Installation

**Add the marketplace and install the plugin:**

```shell
/plugin marketplace add bitfootco/bender
/plugin install bender@bender
```

Skills are namespaced under `bender:`, so invoke them as `/bender:skill-name`.

## Team setup

To prompt teammates to install when they open a project, add to `.claude/settings.json`:

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

To test skills live from this repo without installing:

```shell
claude --plugin-dir .
```

Skills reload on restart. Make a change, restart Claude Code, test with `/bender:skill-name`.
