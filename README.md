# ai-driven-workflow

Cursor plugin for AI-driven development. Works with any language.

## Install

```bash
git clone git@github.com:anthony12031/ai-driven-workflow.git
cd ai-driven-workflow
chmod +x install.sh uninstall.sh scripts/*.sh
./install.sh
```

Restart Cursor (or **Developer: Reload Window**).

### Uninstall

From the same repository:

```bash
./uninstall.sh
```

Removes the plugin symlink under `~/.cursor/plugins/local/`, workspace mirrors in this repo’s `.cursor/`, and matching entries in `~/.cursor/commands`, `~/.cursor/agents`, and `~/.cursor/skills` **only when they still refer to this plugin** (hard links and skill symlinks created by `install.sh`). Source trees such as `commands/` and `skills/` are not deleted. Restart Cursor afterward.

`install.sh` registers the plugin under `~/.cursor/plugins/local/` **and** mirrors commands, agents, and skills into **`~/.cursor/commands`**, **`~/.cursor/agents`**, and **`~/.cursor/skills`**. That way slash commands, subagents, and plugin skills show up in **any** project you open, not only when this repository is the workspace root.

Per-repo assets (rules, hooks, MCP in `.cursor/` inside this clone) stay tied to this repo. **Multi-root workspaces** only show settings for the folder Cursor treats as the context for that panel—use **`/`** in Agent chat to confirm global commands still work.

If a skill name in `~/.cursor/skills/` already exists, re-running install points it at this plugin (back up custom skills first).

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
| Hooks    | 3     | format on edit, block risky shell commands, block PEM reads |
| MCP      | 1     | Figma (remote) |

## Layout

- `.cursor-plugin/plugin.json` — manifest
- `install.sh`, `uninstall.sh` — register or remove plugin and mirrors
- `commands/`, `skills/`, `agents/`, `rules/`, `hooks/`, `scripts/`, `mcp.json`
