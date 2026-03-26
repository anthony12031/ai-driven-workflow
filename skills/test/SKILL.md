---
name: test
description: Writes, runs, and fixes tests by following each repository’s own tooling and docs—never assumes a language or runner. Use when adding tests, running a suite, or debugging failures.
---

# Test

**The repository is the source of truth.** Do not assume a programming language, test runner, or command. Always **read the repo** (and its CI) to learn what to run and how tests are organized.

## 1. Discover how *this* repo runs tests

Do this **before** executing anything. Prefer **automation and docs over guessing**.

| Look here | What to learn |
|-----------|----------------|
| **CI** (`.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`, `azure-pipelines.yml`, …) | Exact commands the pipeline runs; env vars; services (DB, Redis). |
| **README**, **CONTRIBUTING**, `docs/` | Documented local commands, prerequisites, “how to test”. |
| **Project manifests** (whatever exists in the root or monorepo package) | Scripts and tool hints: `package.json`, `Cargo.toml`, `pyproject.toml` / `tox.ini`, `go.mod`, `Gemfile`, `pom.xml` / `build.gradle`, `mix.exs`, `composer.json`, … |
| **Make / task runners** | `Makefile`, `Taskfile`, `Justfile`, `rake`, `npm run` / `yarn` / `pnpm` **only as defined in that file or manifest**. |

Pick the **same** command CI uses (or the documented local equivalent). If CI and README disagree, prefer **CI** for “what must pass,” or ask.

## 2. Toolchain and dependencies

- Use the **runtime and toolchain the repo pins** (version files, `engines`, tool-specific version managers—whatever the project documents).
- **Install dependencies** the way the repo says (`bundle install`, `pip install -e .`, `cargo fetch`, lockfile installs, etc.) when tests require them.
- If tests fail only because the environment is wrong (missing DB, wrong version), fix **environment** first, then re-run.

## 3. Execute

- Run the **discovered** command—full suite unless the user or docs specify a subset.
- Capture failing test names, messages, and stack traces for debugging.

## 4. Writing tests

- **Infer framework and layout** from the same repo: existing test directories, config files, and patterns in neighboring tests.
- **Scope** (unit vs integration vs e2e) and **mocks** should match how the codebase already tests similar code.
- **Cases:** happy path, boundaries, errors, idempotency where relevant; clear arrange/act/assert (or the idiomatic equivalent for that stack).
- Prefer **fixing production code** when behavior is wrong; **change tests** only when the expectation or test itself is wrong (outdated, flaky setup, wrong assertion). Avoid flaky tests (time, randomness, async races).

## 5. Fixing failures

**Default: fix the implementation.** Treat passing tests as the contract unless product says otherwise.

**Change tests** only with a clear reason (wrong expectation, renamed API, intentional behavior change). Explain briefly, then update and re-run using the **same** discovered command.

## Summary

- **Never assume** language or runner—**discover** from CI + docs + manifests (`package.json` is one of many possibilities).
- **Match** toolchain, deps, and commands to the repo.
- **Write** tests consistent with existing project patterns.
- **Fix** code first; fix tests when the test is wrong.
