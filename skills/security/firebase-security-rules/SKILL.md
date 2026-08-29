---
name: firebase-security-rules
description: Design and audit Firebase Firestore/Storage Security Rules with deny-by-default, authentication, ownership, tenant, validation, and least-privilege reasoning. Use for any rules change or security review.
---

# Firebase Security Rules

Start from a deny-by-default posture. Understand the data path and the identity claims available to Rules before writing conditions.

## Review sequence
1. Enumerate protected resources and operations.
2. Identify anonymous, authenticated, owner, tenant, moderator, admin, and service principals.
3. Map `request.auth`, UID, token claims, path variables, and existing resource data.
4. Separate create from update and delete semantics.
5. Validate immutable ownership fields on create/update.
6. Check for wildcard matches that accidentally broaden access.
7. Check that collection/document structure matches rule assumptions.
8. Exercise positive and negative test cases with the emulator.

## Dangerous patterns
- broad `allow read, write: if true`
- trusting client-provided role or tenant fields without a trusted claim/path check
- allowing updates that let users change ownership
- rules that protect one collection but leave a parallel path exposed
- relying on client-side filtering as authorization
- server/Admin SDK access being mistaken for Rule enforcement

## Verification
Rules must be tested, not merely inspected. Prefer emulator tests for representative allowed and denied cases.

## References
- https://firebase.google.com/docs/rules
- https://firebase.google.com/docs/firestore/security/get-started
- https://firebase.google.com/docs/storage/security
- https://firebase.google.com/docs/emulator-suite
