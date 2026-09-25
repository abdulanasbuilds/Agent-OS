---
name: multi-instance-orchestration
description: Coordinate visible independent agent sessions in parallel across terminals, worktrees, folders, and different harnesses while preventing write conflicts and uncontrolled side effects.
---
# Multi-Instance Orchestration

Use this when parallel visible agent instances are useful. The coordinator may launch or address Pi, Claude Code, Codex, OpenCode, or other compatible sessions, but each remains an independent session the user can see and manage.

## Before delegation

Create a task map with one owner per independently writable scope. Record:
- objective;
- scope and non-goals;
- project/folder;
- branch/worktree;
- files or components owned;
- tools allowed;
- acceptance criteria;
- validation commands;
- handoff format.

## Project-boundary requirement

Before starting a worker, resolve the active project and bind the worker to exactly one project root or one dedicated worktree.

A category container containing several projects is never a worker workspace.

Each worker must receive the exact project/worktree path, branch name, writable file scope, non-goals, validation command, and handoff destination. If a worker cannot establish those values, do not delegate it.

## Safe parallelism

Parallelize independent files, features, research tracks, test suites, or experiments.

For implementation work on the same repository, prefer one dedicated worktree and branch per agent.

Do not let multiple instances concurrently mutate the same source file, migration, lockfile, generated output, package manifest, shared configuration, project scope manifest, or Git metadata.

Shared project resources should be read-only unless ownership is explicit.

Workers must never write to sibling projects, parent category folders, or a different repository because that repository happens to be nearby.

## Commit ownership

For a multi-agent implementation:
- worker agents normally do not push remotely;
- prefer one integration owner for the final commit and push;
- workers may commit to their isolated branch when explicitly authorized;
- the integration owner must inspect every worker diff before integration;
- after integration, run end-to-end verification from the project root.

A worker's access to Git does not grant authority over the parent category or other repositories.

## Monitoring

The coordinator tracks every instance's status, changed files, tests, blockers, and last meaningful output.

It intervenes when an instance leaves its project/worktree, touches a protected resource, changes another agent's owned file, attempts a remote write outside its authorization, repeats a failure without new evidence, or needs a decision outside its authority.

## Integration

A completion message is not proof.

Inspect each instance's diff, run required checks, review acceptance criteria, resolve conflicts deliberately, then integrate selected work.

Before integration, verify:
- each diff belongs to the intended project;
- the active repository root is correct;
- no sibling project paths were touched;
- the selected branch/worktree is the expected one.

End-to-end verification happens after integration.

## Remote boundaries

Sub-agent or visible-instance status never grants remote-write, deployment, production, destructive, or secret authority. The global permission bridge applies equally to every session.
