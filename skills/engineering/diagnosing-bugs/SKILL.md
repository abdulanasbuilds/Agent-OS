---
name: diagnosing-bugs
description: Diagnose difficult defects from reproducible evidence before changing code.
---
# Diagnosing Bugs

Reproduce the failure or document why reproduction is impossible. Capture expected versus actual behavior. Narrow the failure surface, inspect state/logs/traces/recent changes, form explicit hypotheses, and test them one at a time.

Add a regression test where practical. Apply the smallest root-cause fix, then rerun the reproduction and relevant suite. Check related failure modes.

Never disable validation, tests, authorization, or security controls just to make the failure disappear.
