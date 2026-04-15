# ai-driven-workflow

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-anthony12031%2Fai--driven--workflow-181717?logo=github)](https://github.com/anthony12031/ai-driven-workflow)

**One plugin, two editors** — the same bundle runs as a **[Cursor](https://cursor.com)** plugin and a **[Claude Code](https://code.claude.com/docs/en/plugins)** plugin: slash commands, skills, subagents, language rules, hooks, and Figma MCP. Use it for spec-driven features, design docs, bug workflows, and repo init in **any** stack.

| | [Cursor](#install--cursor) | [Claude Code](#install--claude-code) |
|---|--------|-------------|
| Install | `./install.sh` (symlinks + `~/.cursor/` mirrors) | Marketplace + `claude plugin install` (no shell installer) |
| Manifest | `.cursor-plugin/plugin.json` | `.claude-plugin/plugin.json` + `marketplace.json` |
| Hooks | `hooks/cursor-hooks.json` | `hooks/hooks.json` ([event reference](https://code.claude.com/docs/en/hooks)) |
| MCP | `mcp.json` | `.mcp.json` → `mcp.json` |
| Rules | `rules/*.mdc` (Cursor) | Add `.claude/rules/` in your app repo if you want Claude-only text rules |

---

## Contents

- [Why this exists](#why-this-exists)
- [Quick install](#quick-install)
- [Workflow](#workflow)
- [What’s included](#whats-included)
- [Repository layout](#repository-layout)
- [Figma MCP](#figma-mcp)
- [Maintainer](#maintainer)

---

## Why this exists

- **Shared workflows** — `/build-feature`, `/design`, `/fix-bug`, `/init-repo` plus reusable skills and agents.
- **Polyglot** — language rules (TypeScript, Python, Go, Rust, …), not tied to one framework.
- **Safety rails** — format-on-save style hooks, risky shell patterns gated, PEM reads guarded (separate hook configs per product).
- **Honest ambiguity** — instructions bias toward **asking you to clarify** instead of guessing.

---

## Quick install

### Install — Cursor

```bash
git clone https://github.com/anthony12031/ai-driven-workflow.git
cd ai-driven-workflow
chmod +x install.sh uninstall.sh scripts/*.sh
./install.sh
```

Then **Developer: Reload Window** in Cursor.

`install.sh` registers `~/.cursor/plugins/local/ai-driven-workflow` and mirrors **commands**, **agents**, and **skills** into **`~/.cursor/commands`**, **`~/.cursor/agents`**, and **`~/.cursor/skills`** so they show up in every repo you open. **Rules**, **hooks**, and **MCP** for this clone live under **this repo’s** `.cursor/`.

**Uninstall:** `./uninstall.sh` (only removes paths that still match this plugin). Restart Cursor after.

If `~/.cursor/skills/<name>` already exists, re-running install repoints it here—back up custom skills first. In **multi-root** workspaces, use **`/`** in Agent chat if the settings panel looks scoped to one folder.

### Install — Claude Code

Plugins are installed via [marketplaces](https://code.claude.com/docs/en/discover-plugins). This repo includes `.claude-plugin/marketplace.json` so you can add **GitHub** `anthony12031/ai-driven-workflow` and install by id.

| | |
|---|---|
| **Plugin** | `ai-driven-workflow` |
| **Marketplace** | `ai-driven-workflow-marketplace` |

**CLI**

```bash
claude plugin marketplace add anthony12031/ai-driven-workflow
claude plugin install ai-driven-workflow@ai-driven-workflow-marketplace
```

**In the app:** `/plugin` → Marketplaces → add **`anthony12031/ai-driven-workflow`** → Discover → install **ai-driven-workflow** → **`/reload-plugins`**.

**Local dev:** from a clone, `claude plugin marketplace add .` then `claude plugin install ai-driven-workflow@ai-driven-workflow-marketplace --scope local`, then **`/reload-plugins`**.

**Validate (optional):** `claude plugin validate /path/to/ai-driven-workflow`

**Uninstall:** `claude plugin uninstall ai-driven-workflow@ai-driven-workflow-marketplace` or `/plugin` → Installed → remove, then **`/reload-plugins`**.

More detail: [Plugins](https://code.claude.com/docs/en/plugins), [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [Configuration scopes](https://code.claude.com/docs/en/settings#configuration-scopes).

---

## Workflow

### 1. Init a project

`/init-repo` or *“init this project”* — scans configs and linters, writes `.cursor/rules/`, adds `.cursor/rules/` to `.git/info/exclude`.

### 2. Build a feature

`/build-feature` … — `docs/specs/…`, approval gates, implementation with **parallel subagents** when tasks are independent, then review.

### 3. Design only

`/design` … — `docs/designs/…` for async review; no implementation.

### 4. Fix a bug

`/fix-bug` … — `docs/rca/…`, your approval, then fix and verification.

### 5. Everything else

Natural language; skills and agents attach when relevant.

---

## What’s included

| Type | Count | Examples |
|------|-------|----------|
| Commands | 4 | `/init-repo`, `/build-feature`, `/design`, `/fix-bug` |
| Skills | 8 | architecture, debug, refactor, security-audit, performance, test, code-gen, project-init |
| Agents | 7 | architect, code-reviewer, debugger, security-auditor, performance-analyst, test-engineer, devops-engineer |
| Rules | 12 | code-quality, security, typescript, python, go, rust, java, react, css, docker, terraform, shell |
| Hooks | 3 | format on edit, risky shell guard, PEM read guard (Cursor + Claude hook files) |
| MCP | 1 | Figma (remote) |

---

## Repository layout

| Path | Role |
|------|------|
| `.cursor-plugin/plugin.json` | Cursor manifest (`hooks` → `hooks/cursor-hooks.json`) |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest |
| `.claude-plugin/marketplace.json` | Catalog for `ai-driven-workflow@ai-driven-workflow-marketplace` |
| `.mcp.json` | Symlink to `mcp.json` (Claude Code) |
| `hooks/cursor-hooks.json` | Cursor hook events |
| `hooks/hooks.json` | Claude Code hook events (`${CLAUDE_PLUGIN_ROOT}` in commands) |
| `install.sh` / `uninstall.sh` | Cursor registration + mirrors / cleanup |
| `commands/`, `skills/`, `agents/`, `rules/`, `scripts/`, `mcp.json` | Shared plugin payload |

---

## Figma MCP

Bundled config points at the [Figma remote MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) (`https://mcp.figma.com/mcp`). Connect and sign in under your editor’s MCP settings when prompted.

---

## Maintainer

**[Anthony Vargas](https://github.com/anthony12031/)** — [github.com/anthony12031](https://github.com/anthony12031/)

Repository: **https://github.com/anthony12031/ai-driven-workflow**
