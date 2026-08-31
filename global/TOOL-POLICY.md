# Tool Permission Policy

Tools are capabilities, not authority.

## Trust levels

READ: generally allowed when relevant.
WRITE: scoped to the authorized workspace/task; inspect the diff afterward.
EXECUTE: run only commands whose purpose, inputs, and environment scope are understood.
REMOTE-WRITE: changes to remote repositories, issues, pull requests, or branches; requires explicit authorization or an established project policy.
DEPLOY: separate trust boundary; requires explicit authorization or a pre-approved release policy.
PRODUCTION-MUTATION: explicit authorization for destructive, irreversible, or materially risky production changes.
SECRET-ACCESS: explicit authorization; never print, copy, or publish secret values.

## Mandatory default

Never push remotely by default.

Local commits are allowed only when they are part of the active task and the project Git policy permits them. Remote push, merge, release, deployment, making a private project public, and production changes are always approval-gated unless the user has explicitly established a standing project rule for that repository.

## Permissive harnesses

If a harness is YOLO-style or has weak permission controls, Agent OS must enforce these trust levels itself. Harness permissiveness is not user authorization.

## Parallel agent isolation

Every visible agent instance gets a bounded scope and workspace/branch. The coordinator must prevent uncontrolled concurrent writes and remote side effects.

## Side-effect verification

After any authorized side effect, verify the resulting state directly. Never report a repository push, deployment, deletion, or other external mutation as successful without evidence.

Checkpoint before destructive operations.