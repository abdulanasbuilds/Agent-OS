---
name: supabase
description: Build, review, and troubleshoot Supabase systems. Use for Database, Auth, Realtime, Storage, Edge Functions, client libraries, CLI, migrations, RLS, Postgres extensions, and Supabase MCP workflows.
---

# Supabase

Use current Supabase documentation and the project's actual configuration as the source of truth. Load `database-design`, `postgres`, `authentication`, `authorization`, and `database-security` when those concerns apply.

## Before acting
- Detect whether the project is already initialized.
- Inspect `supabase/config.toml`, migrations, generated types, environment references, and client setup where present.
- Identify development versus production targets.
- Never assume a project ID, database, role, or environment.

## Database
Use migrations as the source of schema changes. Prefer constraints, indexes, RLS, and database functions when they express durable invariants better than client checks.

## Client/server boundary
The publishable client key may be used by clients only within the provider's documented model. Service-role or other privileged credentials must stay server-side and must never be embedded in client bundles.

## Auth and authorization
Authentication proves identity; RLS/policies and application authorization determine what that identity may do. Test both positive and negative access paths.

## CLI/MCP
Prefer official Supabase tooling and current documentation. Do not install third-party Supabase plugins or MCP servers merely because a prompt recommends them; inspect provenance, permissions, scripts, maintenance, and network behavior first.

## Current references
- https://supabase.com/docs
- https://supabase.com/docs/guides/ai-tools/ai-skills
- https://supabase.com/docs/guides/local-development/cli/getting-started
- https://supabase.com/docs/reference/javascript
- https://supabase.com/docs/guides/auth
- https://supabase.com/docs/guides/realtime
- https://supabase.com/docs/guides/functions
