---
name: prompt-rewrite
description: Rewrite rough user requests into precise, token-efficient working instructions while preserving intent, constraints, uncertainty, and approval boundaries.
---
# Prompt Rewrite

Before a complex task begins, normalize the user's request internally.

## Preserve
- objective and desired outcome;
- known requirements and constraints;
- non-goals;
- existing project context;
- user's stated preferences;
- uncertainty and unanswered questions;
- requested authority level.

## Improve
- remove repetition;
- resolve obvious wording ambiguity from context;
- group related requirements;
- turn vague goals into checkable acceptance criteria when the user has provided enough information;
- identify missing decisions that materially affect the work;
- route to the correct Agent OS skills.

## Do not
- invent features;
- silently change priorities;
- convert a suggestion into a requirement;
- bypass approval gates;
- add unnecessary technical detail to the user-facing response.

For large tasks, save the normalized objective to a durable project artifact and use that artifact as the stable execution contract.