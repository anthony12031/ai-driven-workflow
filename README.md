# ai-driven-workflow

Cursor and **Claude Code** plugin for AI-driven development. Works with any language.

## Cursor and Claude Code

The same repository is wired for **both** products:

| | Cursor | Claude Code |
|---|--------|-------------|
| Manifest | `.cursor-plugin/plugin.json` (hooks → `hooks/cursor-hooks.json`) | `.claude-plugin/plugin.json` |
| MCP | `mcp.json` | `.mcp.json` → `mcp.json` (symlink) |
| Hooks | `hooks/cursor-hooks.json` (Cursor events) | `hooks/hooks.json` ([Claude hook events](https://code.claude.com/docs/en/hooks)) |
| Commands, skills, agents | Same `commands/`, `skills/`, `agents/` tree | Same tree ([plugin reference](https://code.claude.com/docs/en/plugins-reference)) |
| Rules | `rules/*.mdc` for Cursor | Not loaded as Cursor rules; use project `.claude/rules/` if you want Claude-only guidance |

**Cursor:** use **`./install.sh`** (see [Install — Cursor](#install--cursor)).

**Claude Code:** use **marketplace + plugin install** (see [Install — Claude Code](#install--claude-code)); there is no `install.sh`. Hooks use `${CLAUDE_PLUGIN_ROOT}` for bundled scripts.

## Repository

**https://github.com/anthony12031/ai-driven-workflow**

Clone with SSH or HTTPS, for example:

```bash
git clone https://github.com/anthony12031/ai-driven-workflow.git
```

## Install — Cursor

1. Clone the repo (see [Repository](#repository)) and enter the directory.
2. Make scripts executable and run the installer:

```bash
cd ai-driven-workflow
chmod +x install.sh uninstall.sh scripts/*.sh
./install.sh
```

3. Restart Cursor (**Developer: Reload Window**).

`install.sh` symlinks the plugin under `~/.cursor/plugins/local/ai-driven-workflow` and mirrors **commands**, **agents**, and **skills** into **`~/.cursor/commands`**, **`~/.cursor/agents`**, and **`~/.cursor/skills`** so they appear in **every** project you open. Workspace-only assets (**rules**, **hooks**, **MCP**) are mirrored under **this clone’s** `.cursor/` directory.

If a name under `~/.cursor/skills/` already exists, re-running install repoints it at this plugin (back up custom skills first). In **multi-root** workspaces, use **`/`** in Agent chat if the settings panel looks scoped to one folder.

### Uninstall — Cursor

From the cloned repository:

```bash
./uninstall.sh
```

Removes the Cursor plugin symlink, this repo’s `.cursor/` mirrors, and matching global `~/.cursor/` entries **only when they still match this plugin**. Your `commands/`, `skills/`, etc. in the repo are not deleted. Restart Cursor afterward.

## Install — Claude Code

Claude Code installs plugins through [marketplaces](https://code.claude.com/docs/en/discover-plugins). This repository ships a tiny catalog at `.claude-plugin/marketplace.json` so you can add **this GitHub repo** as a marketplace and install the plugin by name (no `install.sh`).

**Plugin:** `ai-driven-workflow`  
**Marketplace id:** `ai-driven-workflow-marketplace` (the `name` field in `marketplace.json`)

### From GitHub (recommended)

In a terminal (with the [Claude Code CLI](https://code.claude.com/docs/en/setup) on your `PATH`):

```bash
claude plugin marketplace add anthony12031/ai-driven-workflow
claude plugin install ai-driven-workflow@ai-driven-workflow-marketplace
```

Or inside Claude Code:

1. Run **`/plugin`** → **Marketplaces** → add **`anthony12031/ai-driven-workflow`** (same as `owner/repo` on GitHub).
2. **Discover** → install **ai-driven-workflow** (pick **user**, **project**, or **local** [scope](https://code.claude.com/docs/en/settings#configuration-scopes) as you prefer).
3. Run **`/reload-plugins`**.

Optional: validate a local clone:

```bash
claude plugin validate /path/to/ai-driven-workflow
```

### From a local clone (development)

```bash
cd /path/to/ai-driven-workflow
claude plugin marketplace add .
claude plugin install ai-driven-workflow@ai-driven-workflow-marketplace --scope local
```

Then **`/reload-plugins`** in the app.

### Uninstall — Claude Code

```bash
claude plugin uninstall ai-driven-workflow@ai-driven-workflow-marketplace
```

Or **`/plugin`** → **Installed** → remove **ai-driven-workflow**. Use **`/reload-plugins`** after changes.

See also: [Plugins](https://code.claude.com/docs/en/plugins), [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

During development, when something is ambiguous, the workflow expects the agent to **ask you to clarify** instead of guessing.

## Workflow

### 1. Init a project

Open the target repo in Cursor, then either:

> `/init-repo`

or say naturally:

> init this project

Scans configs, linters, and representative source. Writes project-specific rules under `.cursor/rules/` and adds `.cursor/rules/` to `.git/info/exclude` so generated rules stay local.

### 2. Build a feature

> `/build-feature` Add OAuth2 login with Google and GitHub

Creates `docs/specs/…`. You approve design and tasks before implementation; then implementation, tests, and review are coordinated. Independent tasks are implemented in **parallel subagents** when they do not depend on each other.

### 3. Design for the team

> `/design` Add real-time notifications with WebSockets

Writes `docs/designs/…` with investigation, architecture, trade-offs, and tasks. No implementation.

### 4. Fix a bug

> `/fix-bug` Users get 403 after password reset

Writes `docs/rca/…` for your review, then implements the fix after you approve the diagnosis.

### 5. Everything else

Ask naturally. Skills and agents apply when relevant (review, security, performance, refactor, tests, codegen).

## Figma

This plugin registers the [Figma remote MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) (`https://mcp.figma.com/mcp`). In Cursor, connect and authenticate Figma in MCP settings when prompted.

## What’s included

| Type     | Count | Examples |
|----------|-------|----------|
| Commands | 4     | `/init-repo`, `/build-feature`, `/design`, `/fix-bug` |
| Skills   | 8     | architecture, debug, refactor, security-audit, performance, test, code-gen, project-init |
| Agents   | 7     | architect, code-reviewer, debugger, security-auditor, performance-analyst, test-engineer, devops-engineer |
| Rules    | 12    | code-quality, security, typescript, python, go, rust, java, react, css, docker, terraform, shell |
| Hooks    | 3     | format on edit, block risky shell, block PEM reads (dual Cursor + Claude configs) |
| MCP      | 1     | Figma (remote) |

## Layout

- `.cursor-plugin/plugin.json` — Cursor manifest (custom hooks path)
- `.claude-plugin/plugin.json` — Claude Code plugin manifest
- `.claude-plugin/marketplace.json` — Claude Code marketplace catalog (install `ai-driven-workflow@ai-driven-workflow-marketplace`)
- `.mcp.json` — symlink to `mcp.json` for Claude Code
- `install.sh`, `uninstall.sh` — register or remove **Cursor** plugin and mirrors
- `hooks/hooks.json` — Claude Code hooks (`PostToolUse`, `PreToolUse`)
- `hooks/cursor-hooks.json` — Cursor hooks
- `commands/`, `skills/`, `agents/`, `rules/`, `scripts/`, `mcp.json`
