---
name: workspace-boundary
description: Resolve and enforce the active project workspace, prevent cross-project writes, and bind Git operations to the correct project root.
---

# Workspace Boundary

Use automatically for every task that can read, write, create, move, delete, commit, branch, push, or otherwise mutate local project state.

## Mandatory startup check

Before meaningful work:

1. Identify the current working directory.
2. Discover the nearest `.agent-os/project-scope.yml`.
3. Resolve its project root.
4. If no project scope exists, determine whether the current directory is a configured workspace container.
5. Never treat a multi-project container as the active implementation workspace.

## Natural-language resolution

When the user names a project without a full path, search only the configured Agent OS workspace roots first.

Do not guess between multiple matches.

When creating a project, use the requested category root, sanitize the new project slug, check for collisions, create the project root, and immediately create its scope manifest.

## Write boundary

All implementation writes must be under the active project root.

Navigation/search may inspect other project names or metadata to locate the requested project. That is not permission to modify them.

Before any write:

- confirm active project;
- confirm destination is inside active project root;
- reject sibling, parent-container, and unrelated repository paths.

## Git boundary

Before any Git write:

```text
active project root
        ==
git rev-parse --show-toplevel
```

If not equal, stop.

Before commit:

- inspect status;
- inspect changed paths;
- ensure all intended changes belong to the active project;
- verify the remote belongs to the active project;
- respect Agent OS remote-push authorization.

## Parallel agents

Every parallel worker receives an isolated worktree or an explicitly non-overlapping file scope.

Never allow multiple workers to share a writable worktree without an explicit ownership protocol.

Workers do not inherit permission to affect siblings, parent containers, other projects, or unrelated remotes.

## Conflict behavior

If project identity, scope, Git root, remote, or ownership is ambiguous:

**STOP. DO NOT GUESS.**

Report the exact ambiguity and require resolution before mutation.

## Principle

The project directory is the unit of work.

The category directory is only an organizational container.

The agent must never confuse the two.
