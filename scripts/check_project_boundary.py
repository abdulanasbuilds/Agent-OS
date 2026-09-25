#!/usr/bin/env python3
"""Verify that a managed project and its Git repository share the same root."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


def norm(path: Path) -> Path:
    return path.expanduser().resolve()


def git_root(start: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return norm(Path(result.stdout.strip()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = norm(args.project)
    scope_file = project / ".agent-os" / "project-scope.yml"

    if not scope_file.is_file():
        message = f"BOUNDARY BLOCK: missing {scope_file}"
        if args.json:
            print(json.dumps({"ok": False, "reason": "missing_scope", "message": message}))
        else:
            print(message)
        return 2

    try:
        root = git_root(project)
    except (subprocess.CalledProcessError, FileNotFoundError):
        root = None

    if root is not None and root != project:
        message = (
            "BOUNDARY BLOCK: Git repository root does not equal the active project root. "
            f"project={project} git_root={root}"
        )
        if args.json:
            print(json.dumps({"ok": False, "reason": "git_root_mismatch", "message": message}))
        else:
            print(message)
        return 3

    payload = {
        "ok": True,
        "project_root": str(project),
        "scope_file": str(scope_file),
        "git_root": str(root) if root else None,
    }

    if args.json:
        print(json.dumps(payload))
    else:
        print("PROJECT BOUNDARY OK")
        print(f"project_root={project}")
        print(f"git_root={root if root else 'not initialized'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
