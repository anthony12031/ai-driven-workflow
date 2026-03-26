---
name: fix-bug
description: Investigates a bug, writes a root cause analysis for review, then implements and verifies a fix after user approval.
---

# Fix bug

Use when the user invokes `/fix-bug` with symptoms, errors, or reproduction hints.

## Phases

1. **Reproduce** — Understand and narrow reproduction; gather logs and stack traces; locate relevant code paths.
2. **Root cause analysis** — Use **debugger** agent style: trace failure, document root cause, impact, proposed fix approach (not code yet). Write `docs/rca/<bug-slug>.md`. Include a Mermaid failure-path diagram when helpful. Status: `INVESTIGATING` → `RCA_REVIEW`.
3. **User review** — **Stop** and ask the user to confirm the RCA and proposed approach. Iterate if they disagree.
4. **Fix** — Status `FIXING`. Implement minimal fix; add or update regression tests via **test** skill; follow language rules. If the RCA lists **multiple independent changes** (disjoint areas, no shared prerequisite), delegate to **subagents in parallel**; otherwise implement in order.
5. **Verification** — Run tests; **code-reviewer** on the change; **security-auditor** if auth/data sensitive. Status `RESOLVED`; fill Resolution in RCA doc.

## Rules

- If reproduction, impact, or fix scope is **unclear**, **ask the user to clarify** before coding or closing the RCA; avoid filling gaps with unstated assumptions.

## RCA template

Match the plan: Symptoms, Root Cause, Affected Code, Failure Path, Impact, Proposed Fix, Resolution.
