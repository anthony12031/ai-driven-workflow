---
name: init-repo
description: Initializes Cursor and Claude Code rules for the open repository—scans configs, linters, and representative source, then writes project-specific rules under .cursor/rules/ and .claude/rules/ and keeps them local via .git/info/exclude. Use when the user invokes /init-repo or says init this project or set up rules for this repo.
---

# Init repo

Use when the user invokes `/init-repo` or wants to bootstrap AI guidance for the **current** workspace (natural language like “init this project” maps here).

Follow the **project-init** skill end to end:

1. **Discover** — Read linter/formatter configs (eslint, biome, ruff, prettier, rustfmt, editorconfig), package manifests, CI configs, CONTRIBUTING or style docs, `tsconfig`, test configs. Sample a few source files for naming and structure.
2. **Respect existing rules** — If `.cursor/rules/` or `.claude/rules/` already has files, merge or skip duplicates; ask before overwriting user-authored rules.
3. **Author Cursor rules** — Create focused `.mdc` files under `.cursor/rules/` (e.g. `project-conventions.mdc`) with globs matching the primary languages. Encode: test runner, formatter, import style, strictness, framework choices, path aliases, and team doc requirements.
4. **Author Claude Code rules** — Mirror the same conventions in `.claude/rules/*.md` (plain Markdown). Match stems where useful (e.g. `project-conventions.md`).
5. **Git exclude** — Append `.cursor/rules/` and `.claude/rules/` to `.git/info/exclude` (each on its own line) if not already present so generated rules stay local. Do not modify tracked `.gitignore` unless the user asks.
6. **Confirm** — List created or updated files and what was inferred.

## Rules

- Prefer concrete, repo-grounded rules over generic plugin defaults.
- Keep Cursor `.mdc` and Claude `.md` content aligned.
- If inference is uncertain, **ask the user to clarify**; only after that, record agreed conventions in the rule files (avoid silent assumptions).
