---
name: build-feature
description: Runs spec-driven development for a new feature—requirements, design, task breakdown, implementation, and review—with user approval gates before coding.
---

# Build feature

Use when the user invokes `/build-feature` or wants end-to-end delivery of a feature from description to implemented, tested, reviewed code.

## Phases

1. **Requirements** — Clarify scope and constraints. Create `docs/specs/<feature-slug>.md` with requirements and acceptance criteria. Set status to `REQUIREMENTS` then advance.
2. **Design** — Use the **architect** agent patterns: architecture section with Mermaid diagrams, components, data flow, key decisions. Set status to `DESIGN_REVIEW`. **Stop and ask the user to approve or revise the design.**
3. **Task breakdown** — Ordered checklist of implementable tasks in the same file. Where tasks can be parallelized, note **dependencies** (or group into waves: Wave A, Wave B) so implementation can schedule work. Set status to `TASK_REVIEW`. **Stop and ask the user to approve or revise tasks.**
4. **Implementation** — Set status `IN_PROGRESS`. Infer **dependencies** between tasks from the design and task list (ordering, shared state, same files, integration points). If something is **unclear or ambiguous**, **ask the user to clarify** before proceeding; do not rely on silent assumptions. After clarification, add any dependency note or wave list to the spec before coding.
   - **Independent tasks** (no ordering dependency, disjoint work): **delegate in parallel**—spawn multiple **subagents** (Task tool), each with a narrow scope (task IDs, file boundaries, or modules), so they run concurrently. Merge results, fix integration, then update the spec.
   - **Dependent tasks**: run **after** prerequisites; use **sequential** work or parallel waves only after prior waves complete.
   - **Within each task or wave**: implement using **code-gen** and language **rules**; add tests with the **test** skill; mark tasks complete in the spec.
5. **Review** — Use **code-reviewer**; add **security-auditor** or **performance-analyst** when relevant. Set status `REVIEW`, record findings in the spec.
6. **Complete** — Set status `COMPLETE`; short summary and follow-ups.

## Spec template

Use the structure from the project plan: Feature title, Status, Branch, Date, Requirements, Acceptance Criteria, Design, Tasks, Implementation Notes, Review.

## Rules

- Do not skip approval gates unless the user explicitly asks to skip planning.
- Keep the spec file updated as the single source of truth.
- When tasks do not depend on each other, **parallelize** via subagents; when they share files or depend on prior outputs, **sequential** work or ordered waves.
- During development, if a decision is missing or ambiguous, **ask the user to clarify** instead of inventing defaults; record agreed choices in the spec.
