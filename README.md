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

## Recommended execution loop

DISCOVER → RESEARCH → PLAN → IMPLEMENT → TEST → REVIEW → SECURITY GATE → RELEASE → LEARN

## Repository map

- `global/` — universal operating rules and policies.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `templates/project/` — starter structure for every new product.
- `adapters/` — harness-specific wiring and command mappings.
- `tools/` — tool contracts and integration notes.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and validation helpers.
- `docs/` — operating model, interoperability, skill specification and adoption standards.

## Global vs project

**Global:** principles, security, tool policy, evidence discipline, research methodology, generic engineering practices, and reusable skills.

**Project:** buyer/user context, product rules, architecture, schema, integrations, environment, decisions, project-specific security, known bugs and roadmap.

Start a new project from `templates/project/` and keep project-specific knowledge there.

## Harness strategy

- **Pi** — experimental/custom orchestration harness.
- **Claude Code** — primary structured coding workflow.
- **Codex** — independent implementation and review engine.
- **OpenCode** — model/provider experimentation.
- **Gemini** — multimodal video/realtime perception where appropriate.

See `docs/HARNESS-INTEROPERABILITY.md` and `adapters/COMMAND-MAP.yml` for the portable mapping.

## Skill invocation

Agent OS uses a canonical skill ID. Harnesses translate that ID into their own interface.

Examples:

```text
/skill:planning       # Pi/native Agent Skills style
/planning             # Claude Code style
planning via native skill tool / Agent Skills support   # OpenCode
Codex: load the canonical Agent Skill by ID            # Codex-compatible workflow
```

The skill itself never grants authority. Harness permissions remain the enforcement boundary.

## Bootstrap

The repository includes a standard-library-only validator:

```bash
python3 scripts/validate_agent_os.py
```

To install the canonical skills into a shared Agent Skills directory:

```bash
bash scripts/install-global-skill-links.sh ~/.agents/skills
```

For Claude Code, a common target is `~/.claude/skills`. For Pi, `~/.pi/agent/skills` is also supported. Check the installed harness release before adding additional automation.

## Security posture

Agent OS intentionally avoids bundling a large collection of unreviewed third-party MCP servers or executable plugins. Integrations are reviewed for provenance, permissions, data handling, maintenance, dependency risk, and prompt-injection exposure before adoption.

Tools are capabilities, not authority. Production mutations, destructive operations, secret access, deployment and other high-impact actions remain approval-gated unless a project explicitly defines a safer automated boundary.

## CI

Every push and pull request runs `scripts/validate_agent_os.py` through GitHub Actions with read-only repository permissions.

## Adding a capability

Do not add a tool because it is popular. First establish necessity, provenance, permission scope, maintenance, and security evidence. Prefer an Agent OS-native skill when the durable value is instruction/knowledge rather than executable code.

Record significant third-party adoption decisions in `docs/` and keep volatile provider behavior tied to current official documentation.
