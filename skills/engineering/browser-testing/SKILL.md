---
name: browser-testing
description: Validate real web behavior through browser automation.
---

Build → run → open → interact → inspect DOM/UI → inspect console/network → test responsive states → fix → retest. Do not declare UI success from source inspection alone.

## Website reconstruction checks

When validating a reconstructed/reference-driven website, additionally verify:
- every enabled public route on direct navigation and browser refresh;
- route links match the reference or approved brief;
- desktop, tablet, and mobile layouts against recorded reference states;
- image and media loads, dimensions, object positioning, and fallback behavior;
- hover, focus, active, open/closed, loading, error, and form states;
- reduced-motion behavior;
- no unintended external CTAs, analytics, builder branding, or reference-brand remnants when white-labeling is requested;
- representative production/deployment URLs when deployment is in scope.
