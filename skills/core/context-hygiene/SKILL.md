---
name: context-hygiene
description: Preserve important reasoning across sessions and choose the least lossy context transition.
---
# Context Hygiene

Prefer the same context while decisions are actively being resolved. Use a handoff when work must cross a session, harness, directory, or person. Use compaction at intentional phase boundaries when verbatim history is no longer required. Use focused subagents only for tightly scoped independent work.

Before a context boundary, persist durable state in project artifacts: decisions, requirements, ADRs, tickets, changed files, tests, blockers, and next actions.

A summary is not equivalent to source evidence. Re-read primary artifacts when a decision depends on exact wording or details.
