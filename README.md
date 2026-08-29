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

DISCOVER → INTAKE → RESEARCH → PLAN → IMPLEMENT → TEST → REVIEW → SECURITY GATE → RELEASE → LEARN

## Repository map

- `global/` — universal operating rules, including security, tool, design, and presentation policies.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `references/` — curated discovery catalogs for design and presentation sources.
- `templates/project/` — starter structure for every new product, including design and presentation artifacts.
- `adapters/` — harness-specific wiring and command mappings.
- `tools/` — tool contracts and integration notes.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and validation helpers.
- `docs/` — operating model, interoperability, resource-adoption decisions, design workflows, and presentation workflows.

## Global vs project

**Global:** principles, security, tool policy, evidence discipline, research methodology, generic engineering practices, reusable design/presentation practices, and reusable skills.

**Project:** buyer/user context, product rules, architecture, schema, integrations, environment, design/presentation briefs and systems, decisions, project-specific security, known bugs, assets, and roadmap.

Start a new project from `templates/project/` and keep project-specific knowledge there.

## Design system

Design is treated as a first-class product capability rather than final polish. The design layer includes design intake, business-aware visual direction, typography, layout, components, interaction, motion, asset direction/provenance, reference discovery, UI/accessibility/performance review, controlled variants, and anti-AI-slop safeguards.

When the user says `design`, `website`, `web-design`, `frontend-design`, `mobile-app-design`, or another supported visual entry point, route through the canonical design router and load only the specialist skills the project actually needs.

See `global/DESIGN-POLICY.md`, `global/DESIGN-ROUTING.md`, `docs/DESIGN-LAB.md`, and `docs/DESIGN-REFERENCE-LIBRARY.md`.

## Presentation system

Presentation work is a separate first-class capability because a deck has a narrative, audience, delivery mode, slide grammar, data-storytelling requirements, speaker notes, accessibility requirements, and output-format constraints that differ from product UI.

Supported entry points include:

```text
/presentation
/presentations
/slides
/deck
/ppt
/pitch-deck
/presentation-design
```

These route to `presentation-router`, which determines communication purpose and business/decision context before loading narrative, visual storytelling, slide composition, assets, typography, production, and QA skills.

The presentation system supports live talks, forwarded/self-read decks, pitch decks, teaching/training decks, executive reports, product/demo decks, PPTX, PDF, and HTML/web outputs.

See `global/PRESENTATION-POLICY.md`, `docs/PRESENTATION-WORKFLOW.md`, `references/PRESENTATION-REFERENCE-CATALOG.yml`, and the presentation project templates.

## Design and presentation variants

When multiple visual directions are legitimately possible, use an isolated variant lab rather than repeatedly overwriting the main implementation.

```text
approved baseline
      ↓
variant A / B / C
      ↓
local previews + screenshots
      ↓
compare against fixed criteria
      ↓
user selects
      ↓
record decision
      ↓
promote selected direction
```

## References and assets

Visual galleries, component libraries, presentation templates, screenshots, fonts, animations, images, and other external material are discovery sources unless reuse rights are verified.

Agent OS records provenance and reuse status. Global catalogs do not become hidden asset dumps. Approved project assets belong in the project workspace with their source/license information.

## Harness strategy

- **Pi** — experimental/custom orchestration harness.
- **Claude Code** — primary structured coding workflow.
- **Codex** — independent implementation and review engine.
- **OpenCode** — model/provider experimentation.
- **Gemini** — multimodal video/realtime perception where appropriate.

See `docs/HARNESS-INTEROPERABILITY.md` and `adapters/COMMAND-MAP.yml`.

## Skill invocation

Agent OS uses canonical skill IDs and maps them to harness-specific interfaces.

```text
/skill:planning                 # Pi-style
/planning                       # Claude Code style
native skill tool               # OpenCode
Agent Skills + AGENTS.md        # Codex-compatible workflow
```

A skill never grants tool permission. Harness permissions remain the authority boundary.

## Security posture

Agent OS intentionally avoids bundling large collections of unreviewed third-party MCP servers or executable plugins. External skills and tools are reviewed for provenance, permissions, data handling, maintenance, licensing, dependency risk, and prompt-injection/tool-poisoning exposure before adoption.

Production mutations, destructive operations, secret access, deployment, and other high-impact actions remain approval-gated unless a project explicitly establishes a safer automated boundary.

## Validation

Run the standard-library-only validator:

```bash
python3 scripts/validate_agent_os.py
```

Every push and pull request runs the validator through GitHub Actions with read-only repository permissions.

## Adding capabilities

Do not add a tool because it is popular. First establish necessity, provenance, permission scope, maintenance, licensing, and security evidence. Prefer an Agent OS-native skill when the durable value is instruction/knowledge rather than executable code.

Keep fast-moving provider behavior tied to current official documentation. Do not freeze volatile API behavior inside long-lived prompts.
