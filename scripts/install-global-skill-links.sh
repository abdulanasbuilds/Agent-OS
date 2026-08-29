#!/usr/bin/env bash
set -euo pipefail

AGENT_OS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-$HOME/.agents/skills}"

mkdir -p "$DEST"

while IFS= read -r -d '' skill_file; do
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  target="$DEST/$skill_name"

  # Canonical skill IDs are unique across Agent OS. Install one directory per
  # skill ID so Claude Code, Pi, OpenCode and other Agent Skills consumers see
  # predictable names and slash commands.
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
done < <(find "$AGENT_OS_DIR/skills" -mindepth 2 -maxdepth 3 -type f -name SKILL.md -print0 | sort -z)

echo "Installed Agent OS skills under $DEST"
