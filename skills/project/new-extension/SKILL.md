---
name: new-extension
description: Start a browser, editor, IDE, CLI, or platform-extension project with explicit host API, permissions, distribution, update, and security requirements.
---

# New Extension

Route to `project-lifecycle` with profile `browser extension/integration`.

Collect only decisions that materially affect the host platform, extension APIs, permissions, data access, UI surfaces, content-script/background behavior, compatibility, packaging, signing, distribution, and update policy.

Request the minimum host permissions. Treat web page content and external messages as untrusted input. Keep secrets and privileged operations out of client-side extension code unless the host explicitly provides a secure boundary.
