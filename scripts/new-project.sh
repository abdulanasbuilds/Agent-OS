#!/usr/bin/env bash
set -euo pipefail

AGENT_OS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"

if [[ -z "$TARGET" ]]; then
  echo "Usage: ./scripts/new-project.sh /path/to/project" >&2
  exit 1
fi

mkdir -p "$TARGET"
cp "$AGENT_OS_DIR/templates/project/AGENTS.md" "$TARGET/AGENTS.md"
cp "$AGENT_OS_DIR/templates/project/PROJECT.md" "$TARGET/PROJECT.md"
cp "$AGENT_OS_DIR/templates/project/ARCHITECTURE.md" "$TARGET/ARCHITECTURE.md"
cp "$AGENT_OS_DIR/templates/project/SECURITY.md" "$TARGET/SECURITY.md"
cp "$AGENT_OS_DIR/templates/project/DECISIONS.md" "$TARGET/DECISIONS.md"
cp "$AGENT_OS_DIR/templates/project/TASKS.md" "$TARGET/TASKS.md"
cp "$AGENT_OS_DIR/templates/project/CHANGELOG.md" "$TARGET/CHANGELOG.md"
mkdir -p "$TARGET/docs" "$TARGET/.agents/skills" "$TARGET/.claude/skills" "$TARGET/.opencode/skills" "$TARGET/.pi/skills" "$TARGET/.pi/extensions"

echo "Created Agent OS project skeleton at $TARGET"
echo "Next: fill PROJECT.md, ARCHITECTURE.md, SECURITY.md, DECISIONS.md, and TASKS.md."
