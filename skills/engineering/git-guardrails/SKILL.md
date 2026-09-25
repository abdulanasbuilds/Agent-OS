---
name: git-guardrails
description: Establish safe Git command boundaries and approval gates around destructive history operations and cross-project repository mistakes.
---
# Git Guardrails

Read-only Git inspection is low risk. Require an explicit approval boundary before force-pushes, hard resets, destructive cleans, history rewrites, remote replacement, risky branch deletion, or bypassing verification hooks.

## Project and repository binding

Before any Git write:
1. Resolve the active Agent OS project root.
2. Require .agent-os/project-scope.yml.
3. Resolve git rev-parse --show-toplevel.
4. Require the Git root to equal the active project root unless the project scope explicitly declares an approved monorepo exception.
5. Inspect git status --short.
6. Inspect git diff --name-only and, before commit, git diff --cached --name-only.
7. Reject the operation if the target repository is a parent category, sibling project, or unrelated directory.

Never initialize Git in a multi-project category folder for ordinary project work.

## Remote binding

Before push, branch publication, PR creation, or remote mutation:
- verify the active project;
- verify the repository root;
- inspect the configured remote URL;
- verify that the remote belongs to the active project;
- respect Agent OS remote-push authorization.

Never let a remembered, inferred, or recently-used remote substitute for verification.

## Before destructive Git work

Explain effect, preserve recoverability, verify target, obtain approval, execute the smallest action, and verify repository integrity afterward.

Never embed credentials in Git URLs or commands. Never treat a tool's ability to execute Git as authorization to rewrite history.

## Hooks

Managed projects should install the Agent OS boundary hook and keep verification hooks enabled. Bypassing the boundary hook is a policy violation and requires explicit authorization.
