---
name: terminal-multiplexing
description: Coordinate visible independent agent sessions through supported terminal multiplexer or tab capabilities without hiding work in background sub-agents.
---
# Terminal Multiplexing

Use this when a task benefits from multiple visible agent instances.

## Detect first

Identify available terminal/session capabilities such as tmux, a supported terminal tab API, cmux, or another approved multiplexer. Do not assume a specific terminal product exists.

## Session contract

For every spawned session record:
- harness and model/provider;
- project path;
- branch/worktree;
- task scope;
- files owned;
- start command;
- expected evidence;
- status.

## Isolation

Separate writable scopes with branches/worktrees when parallel changes could overlap. Use separate ports for simultaneously running web applications. Never assume two agents can safely write the same files concurrently.

## Control

The coordinator may start, prompt, inspect, test, pause, or stop visible sessions when the terminal capability supports it. It must not silently take remote, deployment, production, destructive, or secret authority from the session.

## Failure

If a session cannot be controlled or verified, mark it unavailable and use a safer fallback rather than simulating control.
