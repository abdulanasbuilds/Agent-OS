---
name: environment-capabilities
description: Inspect the current machine, workspace, shell, runtimes, Git, GitHub authentication, browser, containers, and remote-development capabilities before performing environment-dependent work.
---

# Environment Capabilities

Never assume a capability exists.

## Workflow

1. Identify the requested operation.
2. Determine the minimum capabilities required.
3. Inspect availability, versions, and permissions.
4. Respect the project workspace boundary.
5. Use the smallest available capability path.
6. Prefer a configured remote development environment when the local machine lacks required capacity and the user has authorized it.
7. Verify the resulting state independently.

## Capability classes

- filesystem/workspace
- process/shell
- Git
- GitHub CLI/API
- runtime/package manager
- browser automation
- container runtime
- remote development/Codespaces
- secrets/environment injection

## Truth rule

A documented capability is not an available capability until the harness/environment reports that it exists.
A local Git remote is not proof that a remote repository exists.
A successful process start is not proof that the requested end state exists.
Never claim completion without verification.

## Safety

Do not broaden filesystem access merely because a command fails.
Do not bypass authentication, sandboxing, or permission controls.
Do not expose credentials while inspecting the environment.
Do not install tools unless the project actually requires them and the dependency operation is permitted.
