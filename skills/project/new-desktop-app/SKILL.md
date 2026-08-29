---
name: new-desktop-app
description: Start a desktop application project by routing through project intake, platform constraints, UI design, local storage/security needs, packaging, and release requirements.
---

# New Desktop App

Route to `project-lifecycle` with profile `desktop-application`.

Collect only decisions that change the target OS, framework/runtime, packaging model, data/storage, offline behavior, permissions, update strategy, or distribution.

Use `environment-capabilities` before installing SDKs or build tools. Use `project-machine-bootstrap` for reproducible setup. Keep OS-specific packaging and signing separate from generic application architecture.
