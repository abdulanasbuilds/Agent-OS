---
name: firestore
description: Design and secure Cloud Firestore data models, indexes, SDK access patterns, and Security Rules. Use when working with collections/documents, queries, rules, indexes, transactions, or migration of Firestore data.
---

# Cloud Firestore

First identify the database instance and edition where the current Firebase workflow requires it. Then inspect the existing model, rules, indexes, and application access patterns.

## Data modeling
Design around access patterns. Make ownership/tenant boundaries explicit. Prefer stable identifiers and avoid duplicating mutable authoritative data without a consistency strategy.

## Security Rules
Every client-accessible path needs an intentional rule. Start deny-by-default and add narrowly scoped read/write permissions. Test unauthenticated, authorized, unauthorized, cross-user, and cross-tenant cases.

## Queries and indexes
Design indexes from actual query combinations. Do not create broad indexes blindly. Check query behavior and costs before adding complexity.

## Server boundary
Admin SDK/server credentials bypass client Security Rules in server contexts; therefore server authorization must be explicit and independently reviewed.

## Verification
Use the Emulator Suite where practical for rules and application behavior. Deploy only after the target project is verified.

## References
- https://firebase.google.com/docs/firestore
- https://firebase.google.com/docs/firestore/security/get-started
- https://firebase.google.com/docs/rules
- https://firebase.google.com/docs/emulator-suite
