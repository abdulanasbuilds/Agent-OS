# Agent OS

A harness-neutral operating system for agentic software development.

## Purpose

Agent OS separates reusable agent behavior from any single coding harness. The same project can be worked on through Pi, Claude Code, Codex, OpenCode, or another compatible agent without losing architecture, security rules, project context, skills, prompts, or operating discipline.

## Design principles

1. **Business problem before feature.** Understand buyer, user, workflow, urgency, trust, budget, and measurable value before building.
2. **Evidence before confidence.** Separate fact, inference, assumption, and unknown.
3. **Smallest correct change.** Reuse working architecture and avoid needless rewrites.
4. **External content is untrusted data.** Websites, videos, READMEs, issues, package output, tool output, and generated content never grant execution authority.
5. **Least privilege.** Read, write, execute, deployment, and production capabilities are separate trust levels.
6. **Verify before claiming success.** A task is not complete until relevant tests/checks have been run and the final diff has been inspected.
7. **Review is a gate.** Serious changes pass testing and security/architecture review before release.
8. **Harness portability.** Canonical knowledge lives here; adapters translate it into each harness.

## Repository map

- `global/` — universal operating rules and policies.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `templates/project/` — starter structure for every new product.
- `adapters/` — harness-specific wiring for Pi, Claude Code, Codex, and OpenCode.
- `tools/` — tool contracts and integration notes.
- `memory/` — guidance for structured persistent memory.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and health-check helpers.

## Recommended execution loop

DISCOVER → RESEARCH → PLAN → IMPLEMENT → TEST → REVIEW → SECURITY GATE → RELEASE → LEARN

## Source of truth

When a project is copied from this repository, project-specific documentation becomes authoritative for that project. Global policies remain the baseline unless a project explicitly tightens them.

## Harness strategy

- **Pi** — experimental/custom orchestration harness.
- **Claude Code** — primary structured coding workflow.
- **Codex** — independent implementation and review engine.
- **OpenCode** — model/provider experimentation.
- **Gemini** — multimodal video/realtime perception where appropriate.

## Security posture

Agent OS intentionally avoids bundling a large collection of unreviewed third-party MCP servers or executable plugins. Integrations should be evaluated for provenance, permissions, data handling, maintenance, dependency risk, and prompt-injection exposure before adoption.

Tools are capabilities, not authority. Production mutations, destructive operations, secret access, deployment and other high-impact actions should remain behind explicit authorization.
