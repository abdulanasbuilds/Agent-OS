---
name: setup-pre-commit
description: Add lightweight local quality gates using the project's existing formatter, linter, typecheck, test, and secret-scan tooling when justified.
---
# Setup Pre-Commit

Inspect existing tooling first. Do not add redundant frameworks merely to create hooks.

Keep ordinary commit checks fast and deterministic. Put expensive suites in CI or release stages. Do not place production credentials, deployment mutations, or network-dependent provisioning in pre-commit hooks.

After setup, run the hooks on representative files, document bypass/removal behavior, and ensure release gates remain independent of local hooks.
