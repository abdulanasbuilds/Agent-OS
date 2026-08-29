---
name: project-machine-bootstrap
description: Prepare a reproducible development environment for a project on the local machine, a container, or an approved remote environment without silently installing unnecessary software.
---

# Project Machine Bootstrap

## Workflow

1. Read the project requirements and selected profile.
2. Detect the current environment and existing toolchain.
3. Determine the minimum runtime, package manager, SDK, browser, database, and container requirements.
4. Reuse installed tools whenever possible.
5. Install only missing, necessary dependencies after approval when installation changes the machine.
6. Prefer project-local version files and lockfiles over global upgrades.
7. Use dev containers or an approved remote workspace when the local environment cannot satisfy requirements.
8. Record environment requirements for reproducibility.
9. Verify the development command and test command actually work.

## Safety

Never use global package installation as a default just to make a project work.
Never run arbitrary setup scripts from the internet without review.
Never modify shell startup files or system-wide configuration unless explicitly required and approved.
Never store credentials in the environment documentation.
