---
name: build-feature
description: Runs spec-driven development for a new feature—requirements, design, task breakdown, implementation, and review—with user approval gates before coding.
---

# Build feature

Use when the user invokes `/build-feature` or wants end-to-end delivery of a feature from description to implemented, tested, reviewed code.

## Phases

1. **Requirements** — Clarify scope and constraints. Create `docs/specs/<feature-slug>.md` with requirements and acceptance criteria. Set status to `REQUIREMENTS` then advance.
2. **Design** — Use the **architect** agent patterns: architecture section with Mermaid diagrams, components, data flow, key decisions. Set status to `DESIGN_REVIEW`. **Stop and ask the user to approve or revise the design.**
3. **Task breakdown** — Ordered checklist of implementable tasks in the same file. Set status to `TASK_REVIEW`. **Stop and ask the user to approve or revise tasks.**
4. **Implementation** — Set status `IN_PROGRESS`. For each task: implement using **code-gen** and language **rules**; add tests with the **test** skill; mark tasks complete in the spec.
5. **Review** — Use **code-reviewer**; add **security-auditor** or **performance-analyst** when relevant. Set status `REVIEW`, record findings in the spec.
6. **Complete** — Set status `COMPLETE`; short summary and follow-ups.

## Spec template

Use the structure from the project plan: Feature title, Status, Branch, Date, Requirements, Acceptance Criteria, Design, Tasks, Implementation Notes, Review.

## Rules

- Do not skip approval gates unless the user explicitly asks to skip planning.
- Keep the spec file updated as the single source of truth.
