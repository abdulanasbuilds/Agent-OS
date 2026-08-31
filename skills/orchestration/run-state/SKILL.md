---
name: run-state
description: Maintain a compact durable state record for autonomous Agent OS runs so work can resume safely across sessions, harnesses, or context limits.
---
# Run State

Maintain project-local state for each autonomous run. Never store secrets.

Record:
- objective;
- current phase;
- approved scope/spec reference;
- completed slices;
- verification results;
- failed attempts and root causes;
- active blockers;
- pending approval gates;
- next action;
- last confirmed repository/branch state.

Prefer concise summaries over full transcripts. When resuming, re-check the live repository and environment before acting; do not trust stale run-state as proof of current state.

A resumed run must reconcile:
1. filesystem state;
2. Git status/diff;
3. remote/branch state;
4. relevant tests/build state;
5. current project instructions;
6. any changed dependencies or external documentation.

If state conflicts with the live environment, live evidence wins and the discrepancy is recorded.
