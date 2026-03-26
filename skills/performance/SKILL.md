---
name: performance
description: Identifies performance bottlenecks through profiling, benchmarking, and code inspection; suggests optimizations with trade-offs. Use when the user reports slowness, high CPU/memory, timeouts, N+1 queries, or large payloads.
---

# Performance

## Workflow

1. **Define** — Latency vs throughput; p95/p99 if known; which operation is slow.
2. **Measure** — Prefer profiler, APM, traces, or timing logs over guessing.
3. **Hypothesize** — Hot path, I/O wait, lock contention, algorithmic complexity, unnecessary work.
4. **Change** — One optimization at a time when possible; keep behavior correct.
5. **Verify** — Compare before/after with the same workload.

## Common areas

- Database: indexes, N+1 queries, batching, pagination.
- Network: payload size, caching, compression, connection pooling.
- CPU: algorithm choice, unnecessary allocations, parallelization where safe.
- Frontend: bundle size, render cost, list virtualization, image optimization.

## Principles

- Measure before and after material changes.
- Document trade-offs (memory vs speed, complexity vs gain).
