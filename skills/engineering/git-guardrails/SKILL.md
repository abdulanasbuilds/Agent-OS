---
name: git-guardrails
description: Establish safe Git command boundaries and approval gates around destructive history operations.
---
# Git Guardrails

Read-only Git inspection is low risk. Require an explicit approval boundary before force-pushes, hard resets, destructive cleans, history rewrites, remote replacement, risky branch deletion, or bypassing verification hooks.

Before destructive Git work: explain effect, preserve recoverability, verify target, obtain approval, execute the smallest action, and verify repository integrity afterward.

Never embed credentials in Git URLs or commands. Never treat a tool's ability to execute Git as authorization to rewrite history.
