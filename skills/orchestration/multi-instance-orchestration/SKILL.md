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

## Safe parallelism

Parallelize independent files, features, research tracks, test suites, or experiments. Do not let multiple instances concurrently mutate the same migrations, lockfiles, generated files, configuration, or shared component without an explicit ownership protocol.

Prefer one worktree/branch per implementation variant. Shared project resources should be read-only unless ownership is explicit.

## Monitoring

The coordinator tracks every instance's status, changed files, tests, blockers, and last meaningful output. It intervenes when an instance leaves scope, repeats a failure, touches protected resources, or needs a decision outside its authority.

## Integration

A completion message is not proof. Inspect each instance's diff, run required checks, review acceptance criteria, resolve conflicts deliberately, then integrate selected work. End-to-end verification happens after integration.

## Remote boundaries

Sub-agent or visible-instance status never grants remote-write, deployment, production, destructive, or secret authority. The global permission bridge applies equally to every session.
