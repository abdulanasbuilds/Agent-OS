# Agent OS — OpenCode Adapter

OpenCode can discover skills from project/global `.opencode/skills`, Claude-compatible skill directories, and `.agents/skills`. Keep Agent OS canonical content provider-neutral and expose only the skills needed by the project.

## Agents

Map Agent OS specialist roles into OpenCode agent profiles when needed:

- `planner` → primary planning profile
- `builder` → primary build profile
- `researcher` / `explore` → read-heavy research profile
- `reviewer` / `security-auditor` → read-only subagents by default

## Permissions

Use OpenCode's current permission model for the installed release. Default to approval for shell and edits in high-risk workflows; deny production mutation and secret access unless explicitly configured by the project owner.

Do not assume V1 and V2 configuration syntax are interchangeable. Check the installed version before generating `opencode.json` automation.

## Skill discovery

Use the canonical skill ID and lowercase kebab-case directory naming. Keep provider-specific skills separate from generic skills to avoid loading irrelevant instructions.
