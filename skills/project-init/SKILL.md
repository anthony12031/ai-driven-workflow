---
name: project-init
description: Scans repository configs, documentation, and representative source files to infer project conventions, then writes project-specific rules under .cursor/rules/ (Cursor .mdc) and .claude/rules/ (Claude Code Markdown), and registers both paths in .git/info/exclude so generated rules stay local and uncommitted. Use when the user says init this project, set up cursor rules for this repo, or capture team conventions for the AI.
---

# Project Init

## Workflow

1. **Discover** — Read linter/formatter configs (eslint, biome, ruff, prettier, rustfmt, editorconfig), package manifests, CI configs, CONTRIBUTING or style docs, `tsconfig`, test configs. Sample a few source files for naming and structure.
2. **Respect existing rules** — If `.cursor/rules/` or `.claude/rules/` already has files, merge or skip duplicates; ask before overwriting user-authored rules.
3. **Author Cursor rules** — Create focused `.mdc` files under `.cursor/rules/` (e.g. `project-conventions.mdc`) with globs matching the primary languages. Encode: test runner, formatter, import style, strictness, framework choices, path aliases, and team doc requirements.
4. **Author Claude Code rules** — Mirror the same conventions in `.claude/rules/*.md` (plain Markdown, no `.mdc` frontmatter). Use the same stems where it helps (e.g. `project-conventions.md`). Include scope (“applies to …”) in headings or a short intro so Claude Code picks up parity with the Cursor rules.
5. **Git exclude** — Append `.cursor/rules/` and `.claude/rules/` to `.git/info/exclude` (each on its own line) if not already present so generated rules are not committed. Do not modify tracked `.gitignore` unless the user asks.
6. **Confirm** — List created or updated files and what was inferred.

## Principles

- Project-specific rules should override generic plugin rules by being concrete and repo-grounded.
- Keep **Cursor** (`.mdc` + globs) and **Claude** (`.md`) guidance aligned; update both when conventions change.
- If inference is uncertain, **ask the user to clarify** first; record only what was agreed in the rule files (no silent assumptions).
