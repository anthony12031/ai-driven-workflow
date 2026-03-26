---
name: refactor
description: Guides safe refactoring: extract functions, rename symbols, restructure modules, and reduce complexity while preserving behavior. Use when improving readability, reducing duplication, preparing for a feature, or when the user asks to refactor, clean up, or simplify code without changing external behavior.
---

# Refactor

## Preconditions

- Prefer a green test baseline before large refactors. If tests are missing for the area, add minimal characterization tests when feasible.
- Work in small steps; keep the codebase buildable after each step when possible.

## Workflow

1. Identify scope: files, public APIs, and callers that must stay stable.
2. Choose a strategy: extract function, move module, introduce interface, split file, rename with tooling.
3. Apply changes incrementally; run relevant tests or typecheck after each logical chunk.
4. Avoid drive-by behavior changes unless the user explicitly wants them.

## Principles

- Preserve observable behavior unless the user requests a semantic change.
- Prefer compiler and test feedback over large blind edits.
- Update imports and re-exports consistently after moves.
