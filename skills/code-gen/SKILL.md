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

## Parallel implementation

When implementing several tasks from a spec (e.g. `/build-feature`):

- If tasks are **independent** (no ordering dependency, disjoint files or modules), prefer **parallel subagents**—separate delegations with explicit boundaries and acceptance criteria—so work proceeds concurrently; merge and integrate afterward.
- If tasks **share files**, **state**, or **outputs**, keep a single sequence or finish prerequisite tasks before parallelizing downstream work.

## Principles

- Prefer consistency with the codebase over generic templates.
- Do not add dependencies without checking existing package management and versions.
- Keep generated code easy to delete or extend.
- When behavior, API shape, or conventions are ambiguous, **ask the user to clarify** instead of assuming.
