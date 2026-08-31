# Matt Pocock skill-system adoption

This document records the deliberate adoption from `mattpocock/skills` and AI Hero. Agent OS does not vendor the upstream repository or install its full catalog.

## Why adopt

The upstream system is intentionally small and composable, with a clear idea→ship flow: resolve domain language, write a durable spec, slice into vertical work, implement with tight feedback, then review. It also provides useful on-ramps for bugs, large/uncertain work, handoffs, and codebase upkeep. citehttps://www.aihero.dev/skills-post

## Adopted into Agent OS

- `ask-agent` — Agent OS router replacing provider/person-specific routing.
- `context-hygiene` — preserves primary-source reasoning across context boundaries.
- `grilling` — reusable one-question-at-a-time decision interview.
- `domain-modeling` — project vocabulary, bounded context, and durable domain decisions.
- `codebase-design` — deep-module and interface-boundary discipline.
- `wayfinder` — bounded planning for work too large for one session.
- `handoff` — evidence-linked session/harness handoff.
- `tdd` — red/green/refactor through public behavior.
- `to-spec` — durable spec synthesis after decisions settle.
- `to-tickets` — vertical-slice work decomposition.
- `implement` — one approved slice with tight feedback and review gates.
- `code-review` — standards vs specification review.
- `triage` — incoming issue/request classification and readiness.
- `diagnosing-bugs` — reproduce → narrow → hypothesize → fix → regress.
- `resolving-merge-conflicts` — intent-driven conflict resolution with verification.
- `git-guardrails` — explicit safety gates around destructive Git operations.
- `setup-pre-commit` — minimal, project-native local quality gates.
- `retro` — evidence-backed process learning.
- `writing-for-agents` — skill/document authoring discipline.

## Intentionally not adopted

- installer/setup-only skills that exist mainly to install the upstream pack
- personal or vendor-specific skills
- course/exercise-specific skills
- deprecated or superseded skills
- redundant skills already covered by Agent OS
- skills whose main behavior would require a harness-specific background-agent command
- technology-specific migration skills that do not belong in the global layer
- note-taking integrations that are not core to engineering execution

## Important upstream lessons applied defensively

The upstream repository demonstrates why small composable skills and a router are useful, but its public issue history also shows that skill counts, routing, plugin availability, and bounded storage can drift or fail. Agent OS therefore requires manifest/routing validation and bounded artifacts rather than copying claims or implementation details verbatim. citehttps://github.com/mattpocock/skills/issues/869https://github.com/mattpocock/skills/issues/946

`wayfinder` in Agent OS explicitly bounds stored maps to avoid silent truncation in size-limited tracker fields. The routing layer uses canonical family-qualified IDs to avoid orphaned commands.

## Adaptation rules

1. Agent OS terminology wins over upstream naming where they overlap.
2. Security, permission, and provenance policies from Agent OS remain authoritative.
3. Skills describe workflows; tools and harness adapters provide capabilities.
4. No skill may imply permission to run commands, access production, expose secrets, or mutate remote state.
5. Fast-moving provider behavior should be retrieved from current official documentation.
6. Every adopted skill must remain small enough to audit and should point to project artifacts instead of duplicating context.
