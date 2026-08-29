---
name: database-security
description: Review database security as a system-wide boundary. Use for schema changes, roles/grants, RLS, functions, views, secrets, backups, extensions, network access, tenant isolation, and production database operations.
---

# Database Security

A database can be compromised even when application code looks clean. Audit the complete path from identity to query to stored data.

## Review areas
- authentication identity propagation
- authorization/RLS/policies
- roles and grants
- service/administrative credentials
- SECURITY DEFINER functions and search_path
- views and exposed schemas
- dynamic SQL and unsafe identifiers
- row ownership and tenant isolation
- backups/exports and restore permissions
- extensions and privileged capabilities
- connection strings and network access
- logs that may contain sensitive data

## Safe defaults
- deny access until a legitimate path is explicitly granted
- least privilege for database roles
- database-enforced constraints for durable invariants
- separate development/test/production credentials and environments
- never commit credentials or dumps containing secrets

## Verification
Attempt to cross every intended boundary with unauthorized identities. Review both the happy path and bypass paths such as alternate queries, functions, views, batch endpoints, exports, and background jobs.
