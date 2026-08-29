---
name: api-design
description: Design, review, and evolve APIs safely. Use for REST, RPC, webhooks, request/response schemas, versioning, validation, errors, idempotency, pagination, rate limits, and backward compatibility.
---

# API Design

Design the contract before implementation.

## Workflow
1. Identify consumers, trust boundaries, data sensitivity, and failure modes.
2. Define request/response schemas and validation rules.
3. Define authentication and authorization separately from transport.
4. Define error semantics, idempotency, retries, pagination, filtering, and rate limits where relevant.
5. Check backward compatibility and migration strategy.
6. Use existing project conventions before introducing a new pattern.
7. Test valid, invalid, unauthorized, duplicate, timeout, and malformed-input cases.

## Security
Never trust client-supplied identity, role, tenant, price, or ownership fields. Validate untrusted input at the server/trusted boundary. Avoid leaking sensitive fields through errors, logs, broad list endpoints, or debug responses.

## Verification
Document the contract and verify representative requests plus negative authorization cases before declaring an API complete.
