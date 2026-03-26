---
name: testing
description: Writes and improves automated tests after implementation in any language: chooses frameworks from project config, designs cases (happy path, edge cases, errors), and suggests coverage for critical paths. Use when adding tests, increasing coverage, or when the user asks to test a feature without mandating test-first workflow.
---

# Testing

## Workflow

1. **Detect framework** — From `package.json`, `pyproject.toml`, `Cargo.toml`, `go test`, JUnit config, etc.
2. **Scope** — Unit vs integration vs e2e; what to mock (network, clock, filesystem).
3. **Cases** — Happy path, boundary values, error paths, idempotency where relevant.
4. **Implement** — Tests that fail on regression; clear arrange/act/assert structure.
5. **Run** — Use the project's test command; fix implementation or test per project conventions.

## Principles

- Prefer fixing production code when the behavior is wrong; change tests only when expectations were wrong or outdated.
- Avoid flaky tests: control time, randomness, and async boundaries.
- Keep tests readable and colocated with project conventions.
