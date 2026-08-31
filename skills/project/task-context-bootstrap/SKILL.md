---
name: task-context-bootstrap
description: Establish the minimum durable context artifacts for a new task or project so agents can work across sessions and harnesses without losing decisions or requirements.
---
# Task Context Bootstrap

For new projects, new applications, major features, client work, and autonomous runs, ensure the workspace has a usable context set.

Prefer these project-local files when relevant:

- `AGENTS.md` — project operating rules and scope;
- `PROJECT.md` — product/problem and users;
- `ARCHITECTURE.md` — system structure and major boundaries;
- `PLAN.md` — current execution plan;
- `TASKS.md` — verifiable work items;
- `DECISIONS.md` — accepted decisions and reasons;
- `SECURITY.md` — security assumptions and controls;
- `CHANGELOG.md` — meaningful changes;
- `docs/agents/OBJECTIVE.md` — current autonomous objective;
- `docs/agents/STATUS.md` — current run state;
- `docs/agents/REVIEW.md` — review findings;
- `docs/agents/EVIDENCE.md` — verification evidence.

Do not overwrite meaningful existing files. Merge/update deliberately.

For a small routine task, use the existing project context rather than generating empty documents. The purpose is continuity and verification, not file-count inflation.

After bootstrap, every agent should know which artifacts are authoritative for the current task and avoid keeping critical decisions only in chat history.