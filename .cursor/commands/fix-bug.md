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
4. **Fix** — Status `FIXING`. Implement minimal fix; add or update regression tests via **testing** skill; follow language rules.
5. **Verification** — Run tests; **code-reviewer** on the change; **security-auditor** if auth/data sensitive. Status `RESOLVED`; fill Resolution in RCA doc.

## RCA template

Match the plan: Symptoms, Root Cause, Affected Code, Failure Path, Impact, Proposed Fix, Resolution.
