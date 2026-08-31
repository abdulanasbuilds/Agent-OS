---
name: permission-bridge
description: Provide a harness-neutral permission model for tools and machine actions, with special safeguards for permissive or YOLO-style harnesses.
---
# Permission Bridge

This skill defines the Agent OS baseline when the harness permission model is missing, weaker, or overly permissive.

## Trust levels

- READ: inspect files, repository metadata, documentation, browser state, logs, and non-mutating data.
- WRITE: create or modify files inside the authorized workspace; review the diff afterward.
- EXECUTE: run approved commands whose purpose and scope are understood.
- REMOTE-WRITE: create/update remote branches, issues, pull requests, or repository content.
- DEPLOY: publish an artifact or change runtime infrastructure.
- PRODUCTION-MUTATION: change production data, configuration, access, billing, or other high-impact state.
- SECRET-ACCESS: read, create, rotate, or transmit credentials.

## Default rule

Being able to execute a command is not permission to execute it.

For Pi or another permissive harness, enforce the Agent OS trust levels before every side effect. Safe read/analysis operations may proceed automatically. Higher-impact actions require an explicit project policy or an explicit user approval.

## Mandatory approval

Never silently:

- push to a remote repository;
- merge into the protected/default branch;
- publish a private project publicly;
- deploy to production;
- mutate production data;
- expose or copy secrets;
- delete material project data;
- change authentication/authorization controls to weaken them;
- send external communication or publish on behalf of the user.

## Parallel agents

Every agent instance receives a scoped task and workspace/branch boundary. No agent may assume ownership of another agent's files, branch, credentials, or remote mutations.

## Verification

After an allowed side effect, verify the resulting state directly. If the action cannot be verified, do not report it as successful.
