---
name: project-init
description: Scans repository configs, documentation, and representative source files to infer project conventions, then writes project-specific Cursor rules under .cursor/rules/ and registers .cursor/rules/ in .git/info/exclude so generated rules stay local and uncommitted. Use when the user says init this project, set up cursor rules for this repo, or capture team conventions for the AI.
---

# Project Init

## Workflow

1. **Discover** — Read linter/formatter configs (eslint, biome, ruff, prettier, rustfmt, editorconfig), package manifests, CI configs, CONTRIBUTING or style docs, `tsconfig`, test configs. Sample a few source files for naming and structure.
2. **Respect existing rules** — If `.cursor/rules/` already has files, merge or skip duplicates; ask before overwriting user-authored rules.
3. **Author rules** — Create focused `.mdc` files (e.g. `project-conventions.mdc`) with globs matching the primary languages. Encode: test runner, formatter, import style, strictness, framework choices, path aliases, and team doc requirements.
4. **Git exclude** — Append a line `.cursor/rules/` to `.git/info/exclude` if not already present so generated rules are not committed. Do not modify tracked `.gitignore` unless the user asks.
5. **Confirm** — List created or updated files and what was inferred.

## Principles

- Project-specific rules should override generic plugin rules by being concrete and repo-grounded.
- If inference is uncertain, **ask the user to clarify** first; record only what was agreed in the rule file (no silent assumptions).
