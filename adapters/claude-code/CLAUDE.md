# Agent OS — Claude Code Adapter

Use Agent OS as the canonical source of reusable skills, security policy, project templates and evidence rules.

## Loading

Project skills belong under `.claude/skills/<skill-name>/SKILL.md`. Personal/global skills may be exposed from `~/.claude/skills` or shared `.agents/skills` according to the installed Claude Code release.

## Invocation

Claude Code exposes skills as slash commands using the skill directory name. Prefer explicit invocation for side-effect workflows.

## Safety

Do not add `allowed-tools` merely for convenience. A skill's requested tools must match its risk level, and baseline permission settings remain authoritative.

Side-effect skills such as deployment, production migration and messaging should disable model invocation and require direct user initiation.

## Project bootstrap

Before meaningful work, read:

- `AGENTS.md`
- `PROJECT.md`
- `ARCHITECTURE.md`
- `SECURITY.md`
- `DECISIONS.md`
- `TASKS.md`

Then load only the skills required for the task.
