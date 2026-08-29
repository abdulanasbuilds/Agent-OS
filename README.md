# Agent OS

A harness-neutral operating system for agentic software development.

Agent OS separates reusable agent behavior from any single coding harness. The same project can be worked on through Pi, Claude Code, Codex, OpenCode, or another compatible agent without losing architecture, security rules, project context, skills, prompts, or operating discipline.

## Core philosophy

- Business problem before feature.
- Evidence before confidence.
- Smallest correct change.
- External content is untrusted data.
- Least privilege for tools and agents.
- Verify before claiming success.
- Review before release.
- Harness portability over lock-in.

## Standard loop

DISCOVER → RESEARCH → PLAN → IMPLEMENT → TEST → REVIEW → SECURITY GATE → RELEASE → LEARN

## Repository structure

- `global/` — universal operating rules and policies.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `templates/project/` — starter structure for new products.
- `adapters/` — harness-specific wiring.
- `tools/` — integration contracts and notes.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and health-check helpers.

## Security model

Agent OS treats tools as capabilities, not authority. External websites, videos, READMEs, issues, package metadata, tool output, and generated content never grant permission to execute commands, expose secrets, weaken security, or modify production.

Use the smallest toolset necessary, review third-party MCP servers and skills before installation, pin dependencies where practical, and keep destructive or production operations behind explicit approval.

## Harness strategy

Pi is the experimental/custom harness. Claude Code is the primary structured coding harness. Codex is the independent implementation/review engine. OpenCode is the model/provider laboratory. Agent OS is the portable layer underneath them.
