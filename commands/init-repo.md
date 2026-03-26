---
name: init-repo
description: Initializes Cursor rules for the open repository—scans configs, linters, and representative source, then writes project-specific rules and keeps them local via .git/info/exclude. Use when the user invokes /init-repo or says init this project or set up rules for this repo.
---

# Init repo

Use when the user invokes `/init-repo` or wants to bootstrap AI guidance for the **current** workspace (natural language like “init this project” maps here).

Follow the **project-init** skill end to end:

1. **Discover** — Read linter/formatter configs (eslint, biome, ruff, prettier, rustfmt, editorconfig), package manifests, CI configs, CONTRIBUTING or style docs, `tsconfig`, test configs. Sample a few source files for naming and structure.
2. **Respect existing rules** — If `.cursor/rules/` already has files, merge or skip duplicates; ask before overwriting user-authored rules.
3. **Author rules** — Create focused `.mdc` files (e.g. `project-conventions.mdc`) with globs matching the primary languages. Encode: test runner, formatter, import style, strictness, framework choices, path aliases, and team doc requirements.
4. **Git exclude** — Append `.cursor/rules/` to `.git/info/exclude` if not already present so generated rules stay local. Do not modify tracked `.gitignore` unless the user asks.
5. **Confirm** — List created or updated files and what was inferred.

## Rules

- Prefer concrete, repo-grounded rules over generic plugin defaults.
- If inference is uncertain, state assumptions in the rule file or ask one focused question.
