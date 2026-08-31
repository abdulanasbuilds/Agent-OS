---
name: spec-build-review
description: Run a specification-to-implementation review loop: interview when requirements are unclear, write a durable spec, implement exactly the approved scope, review line by line, and feed concrete gaps back into implementation.
---
# Spec → Build → Review

Use this as the canonical implementation loop behind `/spec`, `/build`, and `/review` when a feature or app needs a durable contract.

## Spec phase

If the request is not sufficiently understood, ask focused questions until goal, users, scope, must-have behavior, non-goals, edge cases, acceptance criteria, and constraints are clear.

Do not build during the interview.

Write the approved specification to the project `specs/` location. Include:
- objective and user outcome;
- exact functional requirements;
- non-functional requirements that matter;
- edge/error cases;
- data/API/security implications;
- acceptance criteria;
- explicit non-goals;
- unresolved decisions, if any.

## Build phase

Read the selected spec and current project context before editing.

Implement exactly the approved requirements. Do not add speculative features, perform unrelated refactors, or reinterpret missing requirements as permission to invent behavior.

For every implementation slice, record which requirement IDs are covered.

## Review phase

Compare the current implementation against the spec line by line and acceptance criterion by acceptance criterion.

For each failure record:
- exact requirement/criterion;
- observed gap or bug;
- evidence;
- concrete corrective action.

If gaps exist, return only actionable corrections to the implementation loop. Re-review after the fixes.

## Guardrails

The spec is a contract, not a permission grant. Security, project policy, and explicit current instructions remain higher priority.

Never declare a requirement complete because a file exists or a build succeeds. Require behavior-level evidence.

Never silently expand scope to resolve ambiguity. Ask, record, or stop.
