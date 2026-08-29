---
name: cloudflare-data
description: Design and review Cloudflare data/storage choices such as D1, R2, KV, Durable Objects storage, and related Workers bindings. Use when choosing a Cloudflare persistence layer or reviewing data-access security.
---

# Cloudflare Data

Choose the storage primitive from workload and consistency requirements, not familiarity.

## Decision factors
- relational queries and transactions → D1/SQL
- object/blob storage → R2
- small key/value configuration or caching → KV
- strongly coordinated state tied to an actor/session → Durable Objects storage

## Security
- scope bindings to the smallest required Worker/service
- never expose privileged binding credentials or administrative APIs to clients
- validate authentication and authorization before accessing tenant data
- separate public object access from private object operations
- review signed URLs, object keys, cache behavior, and retention

## Operations
Document backups/export strategy, consistency assumptions, limits, failure behavior, and migration plan. Verify current Cloudflare documentation for APIs, limits, pricing, and product status before implementation.

## References
- https://developers.cloudflare.com/d1/
- https://developers.cloudflare.com/r2/
- https://developers.cloudflare.com/kv/
- https://developers.cloudflare.com/durable-objects/
- https://developers.cloudflare.com/docs-for-agents/
