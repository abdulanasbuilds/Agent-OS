# Skill Hierarchy and Parent-Command Routing

Agent OS is intentionally too large to require the user to memorize skill IDs or aliases.

## Parent rule

For a canonical path skills/<family>/<skill-id>/SKILL.md, the default parent alias is /<family> unless the command map defines a more specific parent router.

Examples:
- presentation/presentation-router -> /presentation
- design/frontend-design -> /design
- project/new-client -> /project
- security/rls-review -> /security

## Parent-command behavior

A parent command is an entry point, not a request to load every child skill.

When a parent concept is invoked, Agent OS must:
1. identify the user's actual intent;
2. inspect project context;
3. identify matching child skills and aliases;
4. compose only the smallest useful child set;
5. preserve the safety and authorization rules of every selected child;
6. report ambiguity only when the intent cannot be resolved safely.

## Alias behavior

Child aliases are precise implementation/routing vocabulary. Parent commands are the human-facing entry points.

Examples:
- /presentation can select narrative, slide composition, visual storytelling, data storytelling, typography, assets, production, QA, and accessibility as needed.
- /design can select website, web-app, mobile, frontend, motion, reference, clone, variant, accessibility, and audit workflows as needed.
- /project can select project intake, project type, client, website, app, SaaS, experiment, workspace bootstrap, and GitHub repository workflows as needed.
- /engineering can select architecture, implementation, debugging, testing, TDD, review, Git, performance, API, accessibility, database, and related workflows as needed.
- /security can select security audit, review, authentication, authorization, prompt-injection defense, dependency supply chain, database security, RLS, and related workflows as needed.

## Parent routing precedence

1. Explicit child command from the user.
2. Dedicated family router.
3. Generic parent family router.
4. General /ask router.

An explicit child command is not overridden by the parent unless safety or project policy blocks it.

## Automatic selection

Natural-language intent is sufficient. The user does not need to remember the child aliases.

## Do not over-route

Parent routing is semantic composition, not bulk loading. Load only the smallest useful child set.

The governing objective is: USER INTENT -> PARENT -> MINIMUM RELEVANT CHILD SKILLS.

## Discovery fallback

If a family has no dedicated router yet, use the generic parent-router skill and the family skill descriptions to select the narrowest useful child set.
