---
name: security-audit
description: "Reviews code and dependencies for common security issues: injection, authn/authz gaps, secrets exposure, unsafe deserialization, SSRF, path traversal, and dependency risks. Use when the user asks for a security review, before shipping sensitive features, or when touching auth, crypto, file uploads, or SQL."
---

# Security Audit

## Checklist (adapt to stack)

- **Secrets** — No API keys, tokens, or private keys in source or logs. Env and secret managers used correctly.
- **Injection** — Parameterized queries; safe shell usage; validated redirects and URLs.
- **Authn/Authz** — Authentication on protected routes; authorization checks on every sensitive action; least privilege.
- **Input** — Validate and bound inputs; correct content types and size limits.
- **Dependencies** — Known vulnerable versions; lockfiles; minimal attack surface.
- **Crypto** — Strong algorithms; no custom crypto; secure randomness where needed.
- **Headers / transport** — HTTPS for sensitive data; secure cookie flags when applicable.

## Workflow

1. Scope the review: entry points, data stores, external calls.
2. Search for high-risk patterns (exec, eval, raw SQL concat, `dangerouslySetInnerHTML`, etc.).
3. Report findings by severity with file references and concrete remediation.
4. Suggest tests or checks that would prevent regressions.
