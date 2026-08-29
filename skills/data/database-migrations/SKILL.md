---
name: database-migrations
description: Plan and execute safe database schema/data migrations. Use for adding or changing tables, columns, constraints, indexes, policies, functions, backfills, or destructive changes.
---

# Database Migrations

Treat migrations as durable production history.

## Before writing
- Inspect the current schema and migration history.
- Identify readers/writers that depend on the object.
- Classify the change as additive, compatible, backfill, constraint-tightening, rename, or destructive.
- Identify lock, downtime, data-loss, and rollback implications.

## Preferred pattern
1. Add new structures compatibly.
2. Deploy code that can work with old and new structures when required.
3. Backfill safely and in bounded batches.
4. Validate data invariants.
5. Tighten constraints after compatibility is established.
6. Remove obsolete structures only after dependencies are gone.

## Rules
Never edit an already-applied migration to “fix history.” Never perform an irreversible production mutation without an explicit recovery strategy. Never mix unrelated schema changes into one migration merely for convenience.

## Verification
Run migration tests against a representative database. Verify resulting schema, permissions, indexes, constraints, and application behavior.
