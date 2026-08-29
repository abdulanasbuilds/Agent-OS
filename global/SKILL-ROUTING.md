# Skill Routing Policy

Agent OS uses a two-stage routing model.

## Stage 1 — discovery

Match the user's intent against skill descriptions and project context. Load only the minimum relevant skills.

## Stage 2 — authorization

Before a skill performs a mutation, classify the requested action as READ, WRITE, EXECUTE, DEPLOY, or PRODUCTION MUTATION. Skill relevance never grants authorization.

## Routing rules

- Project-specific skills override generic guidance for project behavior, but cannot weaken global security policies.
- Provider skills are loaded only when that provider is actually in the project.
- Security skills may be added to a workflow automatically when risk indicators are present.
- Destructive/side-effect skills are user-invocable by default and should not be triggered solely by model inference.
- Prefer one canonical skill over overlapping duplicates.
- When two skills conflict, use the project source of truth plus the stricter security boundary; record the conflict.

## Canonical command form

Harnesses may expose different syntax. The canonical ID is the skill directory name, for example:

`security/rls-review` → `rls-review`

Harness mappings live under `adapters/COMMAND-MAP.yml`.

## Failure behavior

If no skill clearly matches, do not invent a procedure. Use general reasoning, inspect the project, and state the uncertainty. If several skills match, choose the smallest sufficient set.
