---
name: debug
description: Performs language-agnostic systematic debugging: reproduce, isolate root cause, implement minimal fixes, and verify. Use when the user reports errors, test failures, flaky behavior, or unexpected runtime results in any stack (Node, Python, Go, Rust, JVM, etc.).
---

# Debug

## Workflow

1. **Capture** — Error message, stack trace, logs, last known good version or commit if relevant.
2. **Reproduce** — Smallest steps or command to reproduce. If unclear, ask for reproduction details.
3. **Isolate** — Narrow to a function, module, or integration boundary. Use search, reads, and tests.
4. **Hypothesize** — State the most likely cause and how to confirm or falsify it.
5. **Fix** — Minimal change that addresses root cause, not symptoms.
6. **Verify** — Re-run tests or the reproduction path. Add or adjust tests when appropriate.

## Principles

- Prefer evidence (logs, failing test, debugger output) over guesses.
- Fix the underlying bug; avoid masking with broad catch-all handlers unless justified.
- Document non-obvious fixes briefly in code or commit message when the user will commit.
