---
name: project-github-repository
description: Create, connect, verify, and safely push a project to GitHub using authenticated GitHub tooling without overwriting existing repositories or exposing credentials.
---

# Project GitHub Repository

## Preconditions

- Confirm the project path and repository owner/name.
- Confirm repository visibility explicitly; default to private for new client/private work when a choice is required.
- Check local and remote collisions before writing.
- Detect an authenticated GitHub CLI/API capability.

## Preferred local workflow

When `gh` is installed and authenticated, prefer:

`gh repo create OWNER/REPO --private|--public --source PATH --remote origin --push`

Use `--public` only when the user explicitly chose public visibility. Prefer `--private` for client work and private product development unless the user says otherwise.

## Verification

After creation:
- verify repository existence
- verify owner/name
- verify visibility
- verify default branch
- verify the latest commit matches the local project commit
- verify the remote URL

## Failure behavior

If authentication or GitHub tooling is unavailable, leave the local project intact and report the missing capability. Never claim that the remote repository was created.

## Security

Never place tokens in Git remotes, source files, logs, prompts, or documentation. Never delete, rename, force-push, or repurpose an existing repository merely to satisfy creation.
