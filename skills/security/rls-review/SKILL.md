---
name: rls-review
description: Audit Row-Level Security and tenant isolation for Supabase/Postgres systems. Use before or after changing tables, policies, views, functions, roles, or multi-tenant access.
---

# RLS Review

Treat authorization as a database boundary.

## Audit sequence
1. Enumerate tables/views/functions reachable from client-facing paths.
2. Confirm whether RLS is enabled where it should be.
3. Map policies by operation: SELECT, INSERT, UPDATE, DELETE.
4. Check both `USING` and `WITH CHECK` semantics.
5. Trace identity and tenant context from auth/session to database predicates.
6. Review views, SECURITY DEFINER functions, grants, roles, and search_path.
7. Test same-user, different-user, same-tenant, different-tenant, anonymous, and privileged cases.
8. Look for alternate paths that bypass the intended policy.

## Common failure modes
- RLS enabled but no effective policy for a required operation.
- `USING` protects reads but `WITH CHECK` does not protect inserted/updated ownership.
- Client-supplied tenant IDs are trusted without a server/database-derived identity check.
- SECURITY DEFINER functions expose more data or actions than intended.
- A view/function silently bypasses assumptions made about direct table access.
- Server-side privileged clients are mistakenly treated as if RLS protects them.

## Outcome
Return a table of boundary, principal, operation, enforcement point, test evidence, and remaining risk. Do not call a system secure merely because RLS is present.

## References
- https://supabase.com/docs/guides/database/postgres/row-level-security
- https://supabase.com/docs/guides/auth/row-level-security
- https://www.postgresql.org/docs/current/ddl-rowsecurity.html
