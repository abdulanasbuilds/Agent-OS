# Workspace Governance

Agent OS uses a strict **global-container → isolated-project** filesystem model.

## 1. Workspace model

A category folder is a container, not a project.

Example:

```text
Desktop/
├── Clients/
│   ├── Dambo Soccer Academy/
│   ├── Kennedy Digital Satellite/
│   └── Local Restaurant/
├── My Projects/
│   ├── The Scenes/
│   ├── Abdul Anas Portfolio/
│   └── CallHola/
├── Open Source/
├── Learning/
└── Experiments/
```

The agent must treat each immediate project subfolder as an isolated project workspace.

## 2. Active-project binding

At the start of every meaningful task, the agent MUST establish exactly one active project root.

Resolve it in this order:

1. Current working directory, if it is already inside a project.
2. A project explicitly named by the user.
3. A project found by searching configured workspace roots.
4. For new work, resolve category selection before any creation.

A category/container folder containing multiple projects is NOT a valid active project for implementation work.

If the requested project name matches multiple folders, stop and report the ambiguity rather than guessing.

## 3. Project identity

Every managed project should contain:

```text
.agent-os/project-scope.yml
```

This file identifies the project category, stable slug, project root, and Git boundary.

The active project root is the directory containing this file.

## 4. No cross-project work

Once the active project is bound:

- Read/write operations for implementation are limited to the active project root.
- Do not edit sibling projects.
- Do not create files in the parent category merely because it is convenient.
- Do not move files between projects without explicit user authorization.
- Do not use one project's assets, configuration, environment files, credentials, or Git metadata for another project.
- Do not "clean up" nearby projects.
- Do not treat the entire `Clients`, `My Projects`, or other container as one workspace.

Navigation/search may inspect sibling names when necessary to resolve a user's request, but implementation changes must remain inside the selected project.

## 5. Natural-language project resolution

The user does not need to provide a full filesystem path.

Examples:

- "Work on Dambo Soccer Academy."
- "Find the Kennedy Digital Satellite project and fix the mobile layout."
- "Create a new restaurant client project under Clients."

The agent should resolve those requests against configured workspace roots.

For NEW PROJECT creation:

1. Inspect actual/configured categories.
2. Ask the user which category should contain the project unless they already specified it.
3. Never invent a category from documentation examples.
4. Never create a category automatically.
5. Only after category selection, sanitize the project slug and check for local collisions.
6. Create only the requested project directory.
7. Initialize the project scope manifest and Agent OS project files.
8. Never create unrelated top-level categories or sample projects.
9. Existing projects are never moved merely to satisfy Agent OS.

## 6. Git boundary

For a managed project, the Git repository root MUST normally equal the active project root.

Before commit, push, branch mutation, merge, or history operation:

1. Resolve the active project root.
2. Resolve `git rev-parse --show-toplevel`.
3. Normalize both paths.
4. Require exact equality.
5. Inspect `git status --short` and `git diff --name-only`.
6. Reject the operation if the repository root is the parent category, a sibling project, or any other location.
7. Reject the operation if the project scope manifest is missing or invalid.

A project that intentionally lives inside a larger monorepo is an explicit exception and must declare that exception in its project scope manifest.

Never run Git commands from the global category merely because it contains the project.

## 7. GitHub remote boundary

Before creating, committing, pushing, opening a PR, or changing a remote:

- verify the active project;
- verify the local repository root;
- verify the configured/actual remote;
- ensure the remote belongs to the active project;
- never select a remote merely because it is the nearest or most recently used repository.

Never push changes from Project A to Project B.

Remote push remains approval-gated under Agent OS unless a documented standing project policy authorizes it.

## 8. Multi-agent isolation

Multiple agents may work at the same time only when scopes are explicitly isolated.

Preferred model:

```text
Project/
├── main worktree
├── .worktrees/
│   ├── agent-a/
│   └── agent-b/
└── ...
```

Rules:

- One writable agent scope at a time per worktree.
- Parallel agents working on the same repository should use separate worktrees/branches.
- Each agent receives an explicit project root/worktree, branch, file scope, non-goals, and acceptance criteria.
- No two agents may concurrently edit the same file, migration, lockfile, generated file, or shared configuration.
- Worker agents must not independently push to the project's remote unless explicitly authorized.
- Prefer one integration/commit owner when several agents contribute to one repository.
- Before integration, inspect every agent diff and verify changed paths.

## 9. Project creation boundary

When asked to create a project:

- never overwrite an existing folder;
- never silently reuse a similarly named existing project;
- never initialize Git in the parent category;
- create the Git repository at the project root;
- write the project scope manifest before meaningful implementation;
- install the project Git boundary hook;
- preserve the user's category hierarchy.

## 10. Protected containers

Configured category folders are organizational containers. Names shown in documentation are examples only and are never treated as real categories unless they actually exist on the user's machine or are explicitly configured.

The agent must not:

- initialize a Git repository there for ordinary project work;
- place application source files directly in them;
- install project dependencies there;
- create shared `node_modules`, `.venv`, `.git`, databases, or build artifacts there;
- use them as a catch-all temporary workspace.

## 11. Exceptions

An exception requires explicit user instruction or a documented project policy.

When an exception is requested, the agent should state:

- active project;
- intended filesystem scope;
- intended Git scope;
- why the exception is required;
- what other projects remain untouched.

Default behavior is **stop rather than guess**.

## 12. Enforcement hierarchy

Workspace Governance is enforced in layers:

1. Global Agent OS instructions.
2. Project `AGENTS.md`.
3. `.agent-os/project-scope.yml`.
4. Agent OS workspace/Git boundary checks.
5. Git hooks.
6. Harness/tool permissions.

A less restrictive harness must never weaken this policy.
