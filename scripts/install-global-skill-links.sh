#!/usr/bin/env bash
set -euo pipefail

AGENT_OS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-$HOME/.agents/skills}"

mkdir -p "$DEST"

while IFS= read -r -d '' skill_dir; do
  rel="${skill_dir#$AGENT_OS_DIR/skills/}"
  target="$DEST/${rel//\//--}"
  # Keep a copy rather than a symlink by default for portability; users can
  # adapt this script to their preferred shared skill mechanism.
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
done < <(find "$AGENT_OS_DIR/skills" -mindepth 2 -maxdepth 2 -type d -print0 | sort -z)

echo "Installed copies of Agent OS skills under $DEST"
