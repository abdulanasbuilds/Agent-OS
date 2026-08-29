# Harness Interoperability

Agent OS is a portable policy and capability layer. Harnesses are adapters, not sources of truth.

## Canonical layers

1. Global rules — always apply unless a project explicitly tightens them.
2. Project context — product-specific facts, architecture, constraints and decisions.
3. Skills — reusable procedures and domain knowledge.
4. Agents — role-specific operating instructions.
5. Harness adapters — syntax, discovery paths and permission translation.
6. Tools — external capabilities subject to policy.

## Supported harnesses

### Pi

Pi is the experimental/custom harness. It supports Agent Skills, project/global skill discovery and extension-based commands/tools. Keep extensions minimal and review them as executable code.

### Claude Code

Claude Code maps `SKILL.md` directories to slash commands and supports project and personal skill scopes. Side-effect skills should be user-triggered and permission-gated.

### Codex

Codex uses project instructions and Agent Skills. Keep persistent project rules in `AGENTS.md` and avoid relying on undocumented slash-command behavior; verify the installed release before generating automation.

### OpenCode

OpenCode supports Agent Skills and configurable agents/permissions. Its configuration syntax changes between major/current documentation generations, so Agent OS intentionally avoids copying a fixed permission schema into projects without version detection.

## Portability rule

A canonical skill must remain useful without its harness-specific adapter. Adapters may translate invocation syntax, discovery paths and permissions, but must not change the safety contract.

## Permission rule

The harness permission layer is an enforcement boundary. A skill can describe a required operation, but it cannot independently grant permission to perform that operation.

## Drift control

When a harness changes:

1. update its adapter documentation;
2. update `adapters/COMMAND-MAP.yml` if discovery/invocation changes;
3. verify affected skill loading;
4. do not rewrite canonical skills unless the underlying workflow changed;
5. record the compatibility change in `CHANGELOG.md` and `MANIFEST.yml`.
