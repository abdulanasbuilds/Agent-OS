#!/usr/bin/env python3
"""Install Agent OS global instructions and a user-owned workspace configuration."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

BEGIN = "<!-- BEGIN AGENT OS MANAGED BLOCK -->"
END = "<!-- END AGENT OS MANAGED BLOCK -->"

TARGETS = {
    "opencode": Path("~/.config/opencode/AGENTS.md"),
    "claude-code": Path("~/.claude/CLAUDE.md"),
    "codex": Path("~/.codex/AGENTS.md"),
    "pi": Path("~/.pi/agent/AGENTS.md"),
    "shared": Path("~/.agents/AGENTS.md"),
}

WORKSPACE_CONFIG = """version: 2

# Agent OS does not invent, rename, or create categories automatically.
# Add only the category containers you actually use.
#
# Example shape only:
# workspace_roots:
#   - name: Your Category
#     path: ~/Desktop/Your Category
#
workspace_roots: []

policy:
  ask_for_category_on_new_project: true
  create_categories_automatically: false
  do_not_reorganize_existing_projects: true
  discover_existing_projects: true
"""


def expand(path: Path) -> Path:
    return Path(os.path.expandvars(str(path.expanduser())))


def managed_block(canonical: str) -> str:
    return f"{BEGIN}\n{canonical.rstrip()}\n{END}\n"


def merge_managed(existing: str, canonical: str) -> str:
    block = managed_block(canonical)
    start = existing.find(BEGIN)
    end = existing.find(END)
    if start >= 0 and end >= start:
        end += len(END)
        before = existing[:start].rstrip()
        after = existing[end:].lstrip()
        pieces = [before, block.rstrip(), after]
        return "\n\n".join(p for p in pieces if p) + "\n"
    if existing.strip():
        return block + "\n" + existing.lstrip()
    return block


def install_file(path: Path, canonical: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    updated = merge_managed(current, canonical)
    if current != updated:
        path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agent-os-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to the Agent OS repository.",
    )
    parser.add_argument(
        "--no-workspace-config",
        action="store_true",
        help="Do not create the workspace configuration.",
    )
    args = parser.parse_args()

    root = args.agent_os_root.resolve()
    canonical_path = root / "global" / "AGENTS.md"
    if not canonical_path.is_file():
        raise SystemExit(f"Missing canonical global instructions: {canonical_path}")

    canonical = canonical_path.read_text(encoding="utf-8")

    local_canonical = Path.home() / ".agent-os" / "global" / "AGENTS.md"
    local_canonical.parent.mkdir(parents=True, exist_ok=True)
    local_canonical.write_text(canonical, encoding="utf-8")

    for target in TARGETS.values():
        install_file(expand(target), canonical)

    if not args.no_workspace_config:
        workspace = Path.home() / ".agent-os" / "workspace.yml"
        workspace.parent.mkdir(parents=True, exist_ok=True)
        if not workspace.exists():
            workspace.write_text(WORKSPACE_CONFIG, encoding="utf-8")

    print("Agent OS global instructions installed.")
    print(f"Canonical copy: {local_canonical}")
    print("Installed targets:")
    for target in TARGETS.values():
        print(f"  - {expand(target)}")
    if not args.no_workspace_config:
        print(f"Workspace config: {Path.home() / '.agent-os' / 'workspace.yml'}")
        print("No categories or projects were created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
