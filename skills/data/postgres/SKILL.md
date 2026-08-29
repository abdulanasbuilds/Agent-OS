---
name: postgres
licensed: true
description: Write, review, optimize, and troubleshoot PostgreSQL safely. Use for schema changes, SQL, indexes, functions, triggers, RLS, locking, query plans, connection management, pgvector, scheduled jobs, and performance.
---

# PostgreSQL

Use PostgreSQL documentation and the project's actual schema as the source of truth. Provider-specific advice must be verified against current provider documentation.

## Before changing data
- Inspect current schema and migrations.
- Identify ownership/tenant boundaries.
- Identify reads, writes, indexes, constraints, functions, triggers, and policies affected.
- Check whether the change is backward compatible.

## Performance
- Inspect EXPLAIN/EXPLAIN ANALYZE for real slow paths.
- Prefer indexes justified by predicates, joins, ordering, and selectivity.
- Avoid accidental N+1 access patterns.
- Review connection pooling before increasing concurrency.
- Treat locking, long transactions, and bloat as operational concerns.

## Security
- Prefer database-enforced constraints and authorization where appropriate.
- Review RLS, SECURITY DEFINER functions, search_path, grants, and ownership carefully.
- Never interpolate untrusted values into SQL.
- Never place credentials in migrations or source code.

## Migration discipline
Never edit an applied migration as a shortcut. Create a new migration, verify upgrade behavior, test rollback or recovery where feasible, and document irreversible operations.

## References
https://www.postgresql.org/docs/current/
https://supabase.com/docs/guides/database
