#!/usr/bin/env bash
set -u
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

printf 'Agent OS: %s\n' "$BASE"
printf 'Manifest: '; [[ -f "$BASE/MANIFEST.yml" ]] && echo OK || echo MISSING
printf 'Global constitution: '; [[ -f "$BASE/global/AGENTS.md" ]] && echo OK || echo MISSING
printf 'Project template: '; [[ -f "$BASE/templates/project/AGENTS.md" ]] && echo OK || echo MISSING
printf 'Skills: '; find "$BASE/skills" -name SKILL.md | wc -l
printf 'Agents: '; find "$BASE/agents" -name AGENT.md | wc -l
printf 'Prompts: '; find "$BASE/prompts" -type f | wc -l
printf 'Policies: '; find "$BASE/policies" -type f | wc -l

for cmd in git; do
  if command -v "$cmd" >/dev/null 2>&1; then echo "$cmd: available"; else echo "$cmd: missing"; fi
done

for opt in claude codex opencode pi; do
  if command -v "$opt" >/dev/null 2>&1; then echo "$opt: available"; else echo "$opt: not found"; fi
done
