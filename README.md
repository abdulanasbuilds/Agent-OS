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
11. **Project intake before creation.** New work begins with enough context to choose the right profile, not with a blind scaffold.
12. **Collision before write.** Existing local folders and remote repositories are never silently overwritten.
13. **Capability before claim.** The agent must detect required runtime/tool capabilities before claiming it can perform an action.

## Recommended execution loop

DISCOVER → INTAKE → RESEARCH → DESIGN (when relevant) → PLAN → IMPLEMENT → TEST → REVIEW → SECURITY GATE → RELEASE → LEARN

## Repository map

- `global/` — universal operating rules, including security, tool, design, presentation, and project-creation policies.
- `skills/` — reusable workflows and expertise.
- `agents/` — specialist role instructions.
- `prompts/` — reusable prompt templates.
- `policies/` — security and permission boundaries.
- `references/` — curated discovery catalogs for design and presentation sources.
- `templates/project/` — starter structure for every new product, including design and presentation artifacts.
- `templates/profiles/` — profile-specific briefs for products, clients, businesses, websites, and experiments.
- `adapters/` — harness-specific wiring and command mappings.
- `tools/` — tool contracts and integration notes.
- `checklists/` — repeatable execution gates.
- `scripts/` — bootstrap and validation helpers.
- `docs/` — operating model, lifecycle, interoperability, resource-adoption decisions, design workflows, and presentation workflows.

## New work / project lifecycle

Starting a project is a first-class Agent OS capability.

Supported entry points include:

```text
/new-project
/new-app
/new-saas
/new-business
/new-client
/new-website
/new-web-app
/new-mobile-app
/new-desktop-app
/new-cli
/new-api
/new-library
/new-extension
/new-experiment
/new-prototype
```

These are aliases into the canonical `project-lifecycle` skill. The router determines the correct project type, gathers only decision-changing context, checks for local/remote collisions, creates the correct project documentation, detects environment capabilities, and then bootstraps the workspace.

A business idea is not automatically converted into software. A client engagement is not automatically public. A website is not automatically treated as a generic SaaS landing page. A desktop tool, CLI, API, library, browser extension, experiment, or mobile app gets the project profile appropriate to its actual distribution and constraints.

When authenticated GitHub tooling exists, the GitHub repository skill can create the remote, connect it to the local project, push the initial commit, and verify the remote state. When remote capabilities are unavailable, the agent reports the blocker rather than pretending the repository exists.

See `docs/PROJECT-LIFECYCLE.md`, `skills/project/project-lifecycle/SKILL.md`, `skills/project/workspace-bootstrap/SKILL.md`, and `skills/project/project-github-repository/SKILL.md`.

## Global vs project

**Global:** principles, security, tool policy, evidence discipline, research methodology, generic engineering practices, reusable design/presentation practices, reusable project lifecycle skills, and reusable skills.

**Project:** buyer/user context, product rules, architecture, schema, integrations, environment, design/presentation briefs and systems, decisions, project-specific security, known bugs, assets, and roadmap.

Start a new project from `templates/project/` and select the relevant profile under `templates/profiles/`.

## Design system

Design is treated as a first-class product capability rather than final polish. The design layer includes design intake, business-aware visual direction, typography, layout, components, interaction, motion, asset direction/provenance, reference discovery, UI/accessibility/performance review, controlled variants, anti-AI-slop safeguards, and faithful-clone rules.

When the user says `design`, `website`, `web-design`, `frontend-design`, `mobile-app-design`, or another supported visual entry point, route through the canonical design router and load only the specialist skills the project actually needs.

## Presentation system

Presentation work is a separate first-class capability because a deck has a narrative, audience, delivery mode, slide grammar, data-storytelling requirements, speaker notes, accessibility requirements, and output-format constraints that differ from product UI.

Supported entry points include `/presentation`, `/slides`, `/deck`, `/ppt`, `/pitch-deck`, and `/presentation-design`. These route to `presentation-router`.

## References and assets

Visual galleries, component libraries, presentation templates, screenshots, fonts, animations, images, and other external material are discovery sources unless reuse rights are verified.

Agent OS records provenance and reuse status. Global catalogs do not become hidden asset dumps. Approved project assets belong in the project workspace with their source/license information.

## Environment and machine capabilities

Agent OS treats the local machine, container, browser, runtime/toolchain, Git, GitHub, and remote-development environments as discoverable capabilities rather than assumptions.

The environment layer can detect what is actually available and select a safe execution path. A missing capability is a blocker or fallback condition, not permission to invent success.

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

Every push and pull request runs validation through GitHub Actions with read-only repository permissions.

## Adding capabilities

Do not add a tool because it is popular. First establish necessity, provenance, permission scope, maintenance, licensing, and security evidence. Prefer an Agent OS-native skill when the durable value is instruction/knowledge rather than executable code.

Keep fast-moving provider behavior tied to current official documentation. Do not freeze volatile API behavior inside long-lived prompts.
