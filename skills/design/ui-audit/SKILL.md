---
name: ui-audit
description: Audit implemented interfaces for usability, accessibility, consistency, responsive behavior, visual hierarchy, interaction states, content quality, and performance. Use before calling a design implementation finished.
---

# UI Audit

Audit the implementation, not the intention.

## Inspect
- information hierarchy and task clarity
- typography and readable measure
- color/contrast and state differentiation
- spacing/alignment consistency
- component consistency and state coverage
- navigation and interaction feedback
- responsive behavior and overflow
- keyboard/focus/touch access
- images, alt text, loading, and layout shift
- animation and reduced motion
- perceived and actual performance

## Evidence
Use the running application, screenshots, DOM where useful, browser console/network information, and representative content. Cite concrete examples rather than vague impressions.

## Output
Return Critical, High, Medium, and Polish findings. A page passes only when important functional, accessibility, responsive, and performance problems are resolved.

## Relationship
Use `/security-review` for security problems; this skill focuses on interface quality while still flagging unsafe interaction patterns when discovered.
