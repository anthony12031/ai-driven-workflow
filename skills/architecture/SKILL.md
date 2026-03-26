---
name: architecture
description: Designs system architecture, plans components, creates Mermaid diagrams, and recommends tech stack decisions. Use when starting a new feature, designing APIs, planning migrations, refactoring boundaries, or when the user asks about system design, architecture, or how to structure a solution.
---

# Architecture

## Workflow

1. Clarify requirements, constraints, and non-goals (scale, latency, compliance, team skills).
2. Identify components, boundaries, and data flows (entry points, services, storage, external systems).
3. Produce at least one Mermaid diagram: `flowchart`, `sequenceDiagram`, or component relationships. Follow project Mermaid rules (no custom colors; avoid reserved subgraph IDs).
4. Recommend patterns and stack choices with short trade-off notes (simplicity vs flexibility).
5. Break work into implementable tasks or phases when useful.

## Principles

- Prefer the simplest design that meets requirements.
- Call out risks: single points of failure, coupling, migration cost.
- Reference real paths and symbols in the codebase when describing existing systems.
- If information is missing, state assumptions explicitly.

## Output

- Summary of the proposed architecture.
- Diagram(s) in Mermaid.
- Optional: ADR-style bullets for key decisions.
- List of open questions if the design cannot be finalized.
