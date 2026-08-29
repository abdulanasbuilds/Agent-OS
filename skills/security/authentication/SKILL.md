---
name: authentication
description: Design, implement, and review authentication flows for web, mobile, and backend systems. Use for sign-up, sign-in, sessions, tokens, MFA, OAuth/OIDC, password reset, email verification, service identities, and auth troubleshooting.
---

# Authentication

Separate identity verification from authorization.

## Before implementation
- Identify client type and trusted backend boundary.
- Identify the identity provider and supported sign-in methods.
- Define session lifetime, refresh behavior, logout/revocation expectations, and recovery flows.
- Decide where tokens/cookies live and what can read them.

## Security requirements
- Never store raw passwords; use the provider's approved password handling.
- Use secure, appropriately scoped cookies/tokens according to the platform.
- Validate tokens on the trusted boundary before trusting claims.
- Do not treat client-provided role, tenant, or verification flags as authoritative.
- Protect account recovery and email/phone verification from takeover paths.
- Consider replay, session fixation, CSRF where applicable, token theft, enumeration, and rate abuse.

## Provider rule
For Supabase, Firebase, Clerk, Auth0, or another provider, retrieve current official authentication docs before implementation. Do not mix security models between providers.

## Verification
Test new account, existing account, invalid credential, expired session, logout, recovery, unverified identity, unauthorized resource, and privilege escalation cases.
