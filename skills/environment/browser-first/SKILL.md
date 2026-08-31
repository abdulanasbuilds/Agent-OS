---
name: browser-first
description: Keep browser-based verification readily available for web-facing work and use it by default when web behavior is part of the acceptance criteria.
---
# Browser First

For web-facing software, detect available browser automation and keep it ready during implementation and review.

Use the browser when it provides evidence that source inspection cannot:
- route/navigation behavior;
- interaction behavior;
- responsive layout;
- visible content and states;
- accessibility-relevant interaction;
- console/runtime failures;
- meaningful network failures;
- screenshot or visual comparison.

Workflow:

inspect → run → interact → capture evidence → diagnose → fix → rerun → compare.

Never claim 100% accuracy. State confidence from observed behavior and tests.

Do not spend browser calls on unrelated backend-only, data-only, library-only, or administrative work where they add no evidence.
