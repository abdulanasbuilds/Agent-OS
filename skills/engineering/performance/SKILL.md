---
name: performance
description: Diagnose and improve software performance using measurements. Use for slow requests, UI jank, database bottlenecks, excessive memory/CPU, concurrency, bundle size, caching, and scalability work.
---

# Performance

Measure before optimizing.

## Workflow
1. Define the user-visible or system-level performance target.
2. Reproduce the slow path and capture baseline measurements.
3. Identify the dominant bottleneck with profiling, query plans, network traces, logs, or representative benchmarks.
4. Change the smallest relevant layer.
5. Re-measure under the same or better test conditions.
6. Add a regression check when the bottleneck is likely to return.

## Common areas
- unnecessary client/server round trips
- N+1 database access
- missing or excessive indexes
- unbounded queries and payloads
- blocking work on latency-sensitive paths
- excessive renders or large client bundles
- connection-pool exhaustion
- memory leaks and runaway background work
- cache invalidation and stale-data tradeoffs

## Safety
Do not trade correctness, authorization, privacy, or reliability for a benchmark win. Never weaken security controls to improve a metric.

## Verification
Report baseline, change, post-change measurement, test conditions, and remaining tradeoffs. Do not claim a performance improvement without evidence.
