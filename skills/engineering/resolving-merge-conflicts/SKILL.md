---
name: resolving-merge-conflicts
description: Resolve Git merge or rebase conflicts by reconstructing intent and validating the resulting tree.
---
# Resolving Merge Conflicts

Inspect repository state and identify the purpose of each side before resolving a hunk. Use surrounding code, tests, ADRs, and specs to choose behavior by intent rather than ours/theirs.

Preserve security, data, and API invariants. After resolution, search for conflict markers, run focused and relevant broader tests, inspect the final diff/history, and verify the merge/rebase state.

Do not reflexively hard-reset, force-push, abort, or discard unique work. Destructive history changes require explicit approval and a recoverable checkpoint.
