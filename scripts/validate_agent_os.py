#!/usr/bin/env python3
"""Validate Agent OS structure, manifest references, command targets, metadata, and obvious secret leaks."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9]{16,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAIza[A-Za-z0-9_-]{30,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
REQUIRED_FILES = [
    "README.md", "LICENSE", "MANIFEST.yml", "global/AGENTS.md",
    "global/SECURITY.md", "global/TOOL-POLICY.md", "global/EVIDENCE-POLICY.md",
    "global/MEMORY-POLICY.md", "global/MODEL-ROUTING.md", "global/SKILL-ROUTING.md",
    "docs/SKILL-SPEC.md", "docs/HARNESS-INTEROPERABILITY.md",
    "docs/SECURITY-AND-ADOPTION.md", "adapters/COMMAND-MAP.yml",
]
PROJECT_FILES = [
    "templates/project/AGENTS.md", "templates/project/PROJECT.md",
    "templates/project/ARCHITECTURE.md", "templates/project/SECURITY.md",
    "templates/project/DECISIONS.md", "templates/project/TASKS.md",
]


def fail(message: str) -> None:
    ERRORS.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")
    for rel in PROJECT_FILES:
        if not (ROOT / rel).is_file():
            fail(f"project template missing: {rel}")


def check_skills() -> set[str]:
    ids: set[str] = set()
    root = ROOT / "skills"
    if not root.is_dir():
        fail("skills directory missing")
        return ids
    for path in sorted(root.glob("**/SKILL.md")):
        rel = path.relative_to(ROOT).as_posix()
        parent = path.parent.name
        front = parse_frontmatter(path.read_text(encoding="utf-8"))
        name = front.get("name", "")
        description = front.get("description", "")
        if not name:
            fail(f"{rel}: missing frontmatter name")
        elif not NAME_RE.fullmatch(name):
            fail(f"{rel}: invalid skill name {name!r}")
        if name and name != parent:
            fail(f"{rel}: frontmatter name {name!r} does not match directory {parent!r}")
        if not description:
            fail(f"{rel}: missing frontmatter description")
        if name in ids:
            fail(f"duplicate skill name: {name}")
        ids.add(name)
    if not ids:
        fail("no skills found")
    return ids


def manifest_skill_ids() -> set[str]:
    path = ROOT / "MANIFEST.yml"
    if not path.is_file():
        return set()
    text = path.read_text(encoding="utf-8")
    if "core_skills:" not in text or "agents:" not in text:
        fail("MANIFEST.yml missing core_skills or agents section")
        return set()
    section = text.split("core_skills:", 1)[1].split("agents:", 1)[0]
    return {line.strip()[2:] for line in section.splitlines() if line.strip().startswith("- ")}


def check_manifest(skill_ids: set[str]) -> None:
    declared = manifest_skill_ids()
    for skill_path in sorted(declared):
        expected = ROOT / "skills" / skill_path / "SKILL.md"
        name = skill_path.rsplit("/", 1)[-1]
        if not expected.is_file():
            fail(f"manifest skill missing: {skill_path}")
        elif name not in skill_ids:
            fail(f"manifest skill name mismatch: {skill_path}")


def check_command_targets() -> None:
    path = ROOT / "adapters/COMMAND-MAP.yml"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "target:" not in line:
            continue
        target = line.split("target:", 1)[1].strip().split(",", 1)[0].strip().strip("{} ")
        if not target:
            continue
        matches = list((ROOT / "skills").glob(f"*/{target}/SKILL.md"))
        if not matches:
            fail(f"command target missing: {target}")


def scan_secrets() -> None:
    excluded = {".git", ".pytest_cache", "node_modules", ".venv"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in excluded for part in path.parts):
            continue
        if path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret pattern in {path.relative_to(ROOT)}")
                break


def main() -> int:
    check_required_files()
    skill_ids = check_skills()
    check_manifest(skill_ids)
    check_command_targets()
    scan_secrets()
    if ERRORS:
        print("Agent OS validation FAILED")
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1
    print("Agent OS validation PASSED")
    print(f"Skills: {len(skill_ids)}")
    print("No obvious credential patterns detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
