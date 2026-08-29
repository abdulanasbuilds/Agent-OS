---
name: security-review
description: Perform an application security review before release or after meaningful security-sensitive changes. Use for auth, authorization, database, API, dependency, secrets, browser, webhook, storage, and deployment reviews.
---

# Security Review

Start with architecture and trust boundaries before hunting for bugs.

## Review order
1. Map assets, principals, trust boundaries, entry points, and sensitive operations.
2. Review authentication and session handling.
3. Review authorization and tenant isolation.
4. Review input validation and output encoding.
5. Review secrets, credentials, tokens, and logs.
6. Review database access, RLS/rules, functions, views, and grants.
7. Review file uploads, webhooks, SSRF-sensitive integrations, and browser boundaries.
8. Review dependencies and supply chain.
9. Review deployment configuration and production permissions.
10. Verify important findings with reproducible evidence where possible.

## Finding bar
Do not call a theoretical concern a confirmed vulnerability. State attacker, precondition, affected path, impact, and evidence. Distinguish vulnerabilities from hardening notes.

## Independence
For serious releases, perform a second adversarial pass or use an independent reviewer. A builder should not be the sole judge of the security of its own changes.
