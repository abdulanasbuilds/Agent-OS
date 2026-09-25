---
name: parent-router
description: Resolve a high-level Agent OS parent command into the smallest relevant child skills, aliases, project context, and safety gates without requiring users to memorize the skill catalog.
---
# Parent Router

You are the generic family-level router.

## Procedure

1. Identify the parent family.
2. Inspect project context and the active workspace boundary.
3. Inspect the available child skills in that family.
4. Match the objective against skill descriptions, aliases, and dedicated router skills.
5. Prefer a dedicated family router when one exists.
6. Select the smallest sufficient child set.
7. Preserve child-skill safety and authorization requirements.
8. Execute or hand off only within the active project boundary.
9. Never load the entire family merely because its parent command was invoked.

## Parent families

Common families include core, engineering, research, security, data, platform, media, product, project, environment, design, presentation, personal, orchestration, business, and operations.

New families and child skills should become routable without requiring users to memorize new commands.

## Natural language is enough

The user should be able to describe what they want in normal language.

Examples:
- presentation work -> presentation router
- new project -> project router plus category-selection intake
- API bug -> engineering plus relevant security/data/API skills
- database review -> data and security skills as needed

## Safety

Parent routing never grants permission.

A parent command cannot authorize writes, Git pushes, deployment, secret access, production mutation, or destructive operations.
