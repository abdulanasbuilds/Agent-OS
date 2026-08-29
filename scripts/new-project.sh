#!/usr/bin/env bash
set -euo pipefail

# Agent OS project bootstrapper.
# Usage: ./scripts/new-project.sh <path> [repo-name] [visibility]
# visibility: private (default) | public | internal

AGENT_OS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"
REPO_NAME="${2:-}"
VISIBILITY="${3:-private}"

if [[ -z "$TARGET" ]]; then
  echo "Usage: ./scripts/new-project.sh /path/to/project [repo-name] [private|public|internal]" >&2
  exit 1
fi

case "$VISIBILITY" in
  private|public|internal) ;;
  *) echo "Invalid visibility: $VISIBILITY" >&2; exit 1 ;;
esac

# Refuse ambiguous paths and collisions.
TARGET="$(python3 - "$TARGET" <<'PY'
import os, sys
p = os.path.abspath(os.path.expanduser(sys.argv[1]))
if p == os.path.sep or p == os.path.expanduser("~"):
    raise SystemExit("Refusing unsafe root/home directory target")
print(p)
PY
)"

if [[ -e "$TARGET" ]] && [[ -n "$(ls -A "$TARGET" 2>/dev/null || true)" ]]; then
  echo "Target exists and is not empty: $TARGET" >&2
  exit 2
fi

if [[ -z "$REPO_NAME" ]]; then
  REPO_NAME="$(basename "$TARGET")"
fi

# Strict repository slug: safe for GitHub and shell use.
if [[ ! "$REPO_NAME" =~ ^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$ ]]; then
  echo "Invalid repository name: $REPO_NAME" >&2
  exit 3
fi

mkdir -p "$TARGET"

# Copy the canonical project template. Do not copy generated runtime state.
cp "$AGENT_OS_DIR/templates/project/AGENTS.md" "$TARGET/AGENTS.md"
cp "$AGENT_OS_DIR/templates/project/PROJECT.md" "$TARGET/PROJECT.md"
cp "$AGENT_OS_DIR/templates/project/ARCHITECTURE.md" "$TARGET/ARCHITECTURE.md"
cp "$AGENT_OS_DIR/templates/project/SECURITY.md" "$TARGET/SECURITY.md"
cp "$AGENT_OS_DIR/templates/project/DECISIONS.md" "$TARGET/DECISIONS.md"
cp "$AGENT_OS_DIR/templates/project/TASKS.md" "$TARGET/TASKS.md"
cp "$AGENT_OS_DIR/templates/project/CHANGELOG.md" "$TARGET/CHANGELOG.md"

for file in \
  DESIGN-BRIEF.md \
  DESIGN-SYSTEM.md \
  DESIGN-REFERENCES.md \
  DESIGN-VARIANTS.md \
  ASSET-REGISTER.md \
  PRESENTATION-BRIEF.md \
  PRESENTATION-SYSTEM.md \
  PRESENTATION-VARIANTS.md; do
  if [[ -f "$AGENT_OS_DIR/templates/project/$file" ]]; then
    cp "$AGENT_OS_DIR/templates/project/$file" "$TARGET/$file"
  fi
done

mkdir -p \
  "$TARGET/docs" \
  "$TARGET/references" \
  "$TARGET/assets" \
  "$TARGET/design-lab" \
  "$TARGET/presentation-lab" \
  "$TARGET/.agents/skills" \
  "$TARGET/.claude/skills" \
  "$TARGET/.opencode/skills" \
  "$TARGET/.pi/skills" \
  "$TARGET/.pi/extensions"

cd "$TARGET"
git init
printf '%s\n' ".env" ".env.*" "!.env.example" "node_modules/" ".DS_Store" >> .gitignore

git add .
git commit -m "chore: initialize project from Agent OS template"

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  if gh repo view "$REPO_NAME" >/dev/null 2>&1; then
    echo "GitHub repository already exists: $REPO_NAME" >&2
    exit 4
  fi
  gh repo create "$REPO_NAME" --"$VISIBILITY" --source=. --remote=origin --push
  echo "Created and pushed GitHub repository: $REPO_NAME"
else
  echo "Local Agent OS project created: $TARGET"
  echo "GitHub CLI is unavailable or not authenticated; remote repository was not created."
  echo "After authentication, run: gh repo create $REPO_NAME --$VISIBILITY --source=. --remote=origin --push"
fi

echo "Project bootstrap complete: $TARGET"
