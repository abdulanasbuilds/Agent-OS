---
name: workspace-bootstrap
description: Safely materialize an Agent OS project workspace from the selected profile, detect available local/remote capabilities, initialize version control when appropriate, and verify the resulting workspace without overwriting existing work.
---

# Workspace Bootstrap

## Preconditions

- Run project intake and select a project profile.
- Resolve the intended local path and check whether it already exists.
- Resolve the intended remote repository name and check for collisions.
- Detect available capabilities such as Git, GitHub CLI/API, container runtime, runtime/toolchain, and remote-development options.

## Bootstrap

1. Create the smallest appropriate project workspace.
2. Materialize only the selected profile's templates.
3. Initialize Git only when the project is meant to be version-controlled.
4. Never copy secrets into generated files.
5. Create a remote repository only through an authenticated and explicitly authorized capability.
6. Prefer private visibility for client/private work unless public visibility is explicitly requested.
7. Push only after the local project has a clean initial state and the remote collision check passes.

## Verification

Report the actual state of:
- local path
- Git repository
- remote URL
- remote repository existence/visibility
- initial commit
- available runtime/toolchain

If a capability is unavailable, preserve the local workspace and report the exact missing capability. Never claim that a step succeeded when it was not executed.