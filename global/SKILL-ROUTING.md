# Skill Routing Policy

Agent OS uses intent routing plus hierarchical parent routing.

## Stage 1 — discovery

Match the user's intent against skill descriptions, parent families, aliases, and project context.

## Stage 2 — parent selection

Resolve the highest useful parent concept before selecting child skills.

The user should normally be able to describe the goal in natural language or invoke a parent command. They should not need to remember the complete skill catalog.

## Stage 3 — child composition

Within the selected parent family, select only the smallest relevant child skills.

A parent command does NOT mean "load everything under this family."

It means:

USER INTENT -> PARENT -> MINIMUM RELEVANT CHILD SKILLS

## Stage 4 — authorization

Before a skill performs a mutation, classify the requested action as READ, WRITE, EXECUTE, DEPLOY, or PRODUCTION MUTATION. Skill relevance never grants authorization.

## Parent-family rule

For every canonical skill path:

skills/<family>/<skill-id>/SKILL.md

the default parent alias is /<family>.

Dedicated routers may override generic parent behavior when they provide richer domain-specific routing, such as /design, /presentation, and /project.

Child aliases remain available for precise control, but they are optional.

## Routing rules

- Automatically select relevant skills/tools/agents; the user should not need to enumerate capabilities.
- Prefer a dedicated family router when one exists.
- Prefer one canonical skill over overlapping duplicates.
- Load only the minimum relevant child skills.
- Project-specific skills override generic guidance for project behavior, but cannot weaken global security policies.
- Provider skills are loaded only when that provider is actually in the project.
- Security skills may be added automatically when risk indicators are present.
- Destructive/side-effect skills remain authorization-gated.
- Parent routing preserves active-project and Git boundaries.
- New projects must pass category-selection intake before any project directory is created.
- Existing projects must not be reorganized merely because Agent OS is introduced.

## Canonical command form

Harnesses may expose different syntax. The canonical ID is the skill directory name.

Examples:

security/rls-review -> rls-review -> parent /security

presentation/presentation-assets -> presentation-assets -> parent /presentation

Harness mappings live under adapters/COMMAND-MAP.yml.

## Failure behavior

If no child clearly matches, use generic parent routing and then the general /ask router.

If several children match, choose the smallest sufficient set.

If authorization is ambiguous, stop at the relevant gate rather than guessing.
