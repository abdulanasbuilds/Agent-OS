---
name: implement
description: Build one approved vertical slice with tight feedback, then verify and review before promotion.
---
# Implement

Read the selected spec/ticket, project context, ADRs, architecture, and security constraints first. Confirm scope and the highest useful test seam.

Work in one vertical slice. Use TDD where valuable. Run focused checks after meaningful changes and avoid opportunistic refactors.

Before completion, run relevant tests/build/type/lint checks, inspect the diff, and invoke applicable review, security, accessibility, and performance checks. Do not deploy or mutate production without explicit authorization.
