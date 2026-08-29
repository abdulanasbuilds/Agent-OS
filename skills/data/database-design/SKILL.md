---
name: database-design
description: Design relational or document data models before implementation. Use when deciding entities, relationships, keys, constraints, normalization, tenancy, indexes, lifecycle, auditability, or query patterns.
---

# Database Design

Treat the data model as a security and product boundary, not just storage.

## Workflow
1. Identify business entities, actors, ownership, and lifecycle.
2. Write the critical read/write workflows and invariants.
3. Choose relational vs document structure based on access patterns and integrity needs.
4. Define primary keys, foreign keys, uniqueness, nullability, defaults, checks, and deletion behavior.
5. Define tenant boundaries before writing application queries.
6. Design indexes from real query patterns; do not index every column.
7. Separate public/client data from privileged/server data.
8. Define migrations and rollback strategy.
9. Create representative test data and verify constraints.
10. Review security before implementation.

## Required output
- entities and ownership
- relationships and cardinalities
- constraints/invariants
- likely query patterns
- indexes with rationale
- authorization boundary
- migration plan
- unresolved assumptions

## Rules
Do not invent fields merely because they are convenient for code. Do not use an ORM abstraction to hide an unclear data model. Preserve database-enforced invariants whenever the database can enforce them.

## Source guidance
For provider-specific behavior, retrieve current official documentation before implementation.
- PostgreSQL: https://www.postgresql.org/docs/current/
- Supabase: https://supabase.com/docs
- Firebase/Firestore: https://firebase.google.com/docs/firestore
