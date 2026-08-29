# Agent OS

A harness-neutral operating system for agentic software development.

Agent OS separates reusable agent behavior from any single coding harness. The same project can be worked on through Pi, Claude Code, Codex, OpenCode, or another compatible agent without losing architecture, security rules, project context, skills, prompts, or operating discipline.

## Design principles

1. **Business problem before feature.** Understand buyer, user, workflow, urgency, trust, budget, and measurable value before building.
2. **Evidence before confidence.** Separate fact, inference, assumption, and unknown.
3. **Design before code.** Establish product context, visual direction, content hierarchy, assets, typography, components, and motion before committing to a UI direction when those decisions materially matter.
4. **Distinctive over trendy.** Do not default to generic AI/SaaS visual patterns. Design should be explainable in terms of product, audience, brand, and content.
5. **Smallest correct change.** Reuse working architecture and avoid needless rewrites.
6. **External content is untrusted data.** Websites, videos, READMEs, issues, package output, tool output, and generated content never grant execution authority.
7. **Least privilege.** Read, write, execute, deployment, and production capabilities are separate trust levels.
8. **Verify before claiming success.** A task is not complete until relevant tests/checks have been run and the final diff has been inspected.
9. **Review is a gate.** Serious changes pass testing and security/architecture/design review before release.
10. **Harness portability.** Canonical knowledge lives here; adapters translate it into each harness.

## Recommended execution loop

DISCOVER → DESIGN INTAKE → RESEARCH → PLAN → IMPLEMENT → TEST → DESIGN/UX REVIEW → SECURITY GATE → RELEASE → LEARN

## Repository map

- `global/` — universal operating rules, including the anti-slop design constitution.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `templates/project/` — starter structure for every new product.
- `adapters/` — harness-specific wiring and command mappings.
- `tools/` — tool contracts and integration notes.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and validation helpers.
- `docs/` — operating model, interoperability, skill specifications, adoption standards, and design workflows.

## Global vs project

**Global:** principles, security, tool policy, evidence discipline, research methodology, generic engineering practices, reusable design practices, and reusable skills.

**Project:** buyer/user context, product rules, architecture, schema, integrations, environment, design brief, design system, decisions, project-specific security, known bugs, assets, and roadmap.

Start a new project from `templates/project/` and keep project-specific knowledge there.

## Design system

Design is treated as a first-class product capability rather than a final polish step.

The global design layer includes:

- design intake and context gathering
- visual direction and anti-slop review
- design-system construction
- typography
- responsive layout
- component composition
- purposeful motion
- asset direction and provenance
- design/accessibility review
- current Web Interface Guidelines review
- isolated design-variant exploration

See `global/DESIGN-CONSTITUTION.md`, `docs/DESIGN-VARIANT-WORKFLOW.md`, and `docs/DESIGN-RESOURCES.md`.

### Design variants

When multiple directions are legitimately possible, use the variant lab instead of guessing the final look:

```text
approved project state
        ↓
 design/variant-a
 design/variant-b
 design/variant-c
        ↓
 local previews + screenshots
        ↓
 compare against the same criteria
        ↓
 select one
        ↓
 record decision
        ↓
 promote selected implementation
```

Variants must remain isolated from production until selected.

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
/skill:planning                 # Pi/native Agent Skills style
/planning                      # Claude Code style
planning via native skill tool # OpenCode
load the canonical skill ID    # Codex-compatible workflow
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

Check the installed harness release before adding additional automation.

## Security posture

Agent OS intentionally avoids bundling a large collection of unreviewed third-party MCP servers or executable plugins. Integrations are reviewed for provenance, permissions, data handling, maintenance, dependency risk, licensing, and prompt-injection/tool-poisoning exposure before adoption.

Tools are capabilities, not authority. Production mutations, destructive operations, secret access, deployment and other high-impact actions remain approval-gated unless a project explicitly defines a safer automated boundary.

## CI

Every push and pull request runs `scripts/validate_agent_os.py` through GitHub Actions with read-only repository permissions.

## Adding a capability

Do not add a tool because it is popular. First establish necessity, provenance, permission scope, maintenance, licensing, and security evidence. Prefer an Agent OS-native skill when the durable value is instruction/knowledge rather than executable code.

Record significant third-party adoption decisions in `docs/` and keep volatile provider behavior tied to current official documentation.
