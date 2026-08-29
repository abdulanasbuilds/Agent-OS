---
name: authorization
description: Design and audit authorization, RBAC, ABAC, tenant isolation, resource ownership, and privilege boundaries. Use whenever an authenticated user or service must be limited to specific actions or resources.
---

# Authorization

Model authorization explicitly. Authentication answers “who are you?” Authorization answers “what may you do here, to this resource, under this condition?”

## Workflow
1. Enumerate principals, roles, resources, actions, and contexts.
2. Define invariants in plain language before implementation.
3. Pick the enforcement point that can reliably enforce each invariant.
4. Prefer server/database enforcement for security boundaries; client checks are UX only.
5. Test horizontal access control (other user's data) and vertical access control (higher-privilege actions).
6. Test indirect object references, alternate endpoints, bulk operations, exports, and background jobs.
7. Review service-to-service identities separately from end-user identities.

## Multi-tenancy
Every tenant-scoped resource needs a trustworthy tenant identity and an enforcement path that cannot be changed by the client. Avoid accepting arbitrary tenant IDs as proof of membership.

## Roles
Keep role names and privileges explicit. Do not infer security from UI visibility. Record privileged role changes and review who can grant/revoke roles.

## Outcome
Produce a permission matrix and negative test cases. Flag any path where a lower-trust principal can cross an intended boundary.
