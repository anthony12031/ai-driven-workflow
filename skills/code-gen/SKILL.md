---
name: code-gen
description: Scaffolds projects and generates boilerplate (modules, APIs, CLI stubs, configs) following existing repo conventions. Use when bootstrapping a service, adding CRUD scaffolding, creating package layout, or when the user asks to generate starter code or file structure.
---

# Code Gen

## Workflow

1. Inspect existing layout: directories, naming, module system, and tooling.
2. Match style: imports, exports, error handling, and config patterns already in the repo.
3. Generate minimal files needed for the request; avoid unused boilerplate.
4. Add pointers to where tests and docs should live if the project has patterns for them.

## Principles

- Prefer consistency with the codebase over generic templates.
- Do not add dependencies without checking existing package management and versions.
- Keep generated code easy to delete or extend.
