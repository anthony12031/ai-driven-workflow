---
name: design
description: Produces an investigation and shareable design document with architecture, diagrams, trade-offs, and tasks—no implementation.
---

# Design

Use when the user invokes `/design` and wants a design-only artifact for team review (no code changes).

## Phases

1. **Requirements** — Scope, constraints, non-functional needs.
2. **Investigation** — Explore the codebase; summarize existing systems, APIs, and data models. Use **architect** agent for structure.
3. **Design** — Write `docs/designs/<feature-slug>.md`: Context, Requirements, Investigation, Proposed Design (architecture Mermaid, components, API contracts, data model), Trade-offs, Open Questions.
4. **Tasks** — Ordered tasks with rough estimates and acceptance hints. Note **dependencies** or **waves** where tasks can run in parallel during implementation vs where order matters.
5. **Present** — Give path to the doc and a short executive summary for sharing.

## Rules

- Do not implement production code unless the user explicitly changes scope.
- Optimize the doc for async review (clear headings, diagrams, open questions).
- List **open questions** for anything uncertain; **ask the user to clarify** instead of assuming requirements or constraints.
