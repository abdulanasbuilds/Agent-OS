---
name: gates
description: Apply Agent OS approval and verification gates for autonomous work, separating reversible development actions from high-impact or irreversible operations.
---
# Gates

Every autonomous run evaluates the next action against four dimensions:

- impact: read, edit, execute, deploy, production, external communication;
- reversibility: easy rollback versus material loss;
- authorization: current instruction, project policy, or explicit approval;
- evidence: tests/checks proving the action is safe enough.

## Default policy

Read/inspect → normally autonomous.

Edit/create project files → autonomous when inside authorized workspace.

Run tests/builds → autonomous when commands are known and bounded.

Git branch/commit → autonomous when project policy allows.

Push to an existing repository → only when repository/branch policy permits.

Create a new repository → only after name, owner, visibility, and collision checks are resolved.

Deploy → requires explicit project/environment authority; production deploy is never inferred from a vague request.

Production data mutation/destructive action/external publication → approval required unless an explicit pre-established policy authorizes that exact class of action.

## Verification gate

Before promotion, verify the smallest relevant set of:
- unit/integration/end-to-end tests;
- build/type/lint checks;
- browser/runtime behavior;
- security checks;
- accessibility/performance checks where relevant;
- diff/repository state;
- deployment health when applicable.

## Stop conditions

Stop rather than guess when:
- required capability is unavailable;
- authorization is missing or ambiguous for a high-impact action;
- requirements conflict;
- security cannot be established;
- repeated repair attempts fail without new evidence;
- the next action would materially expand scope.
