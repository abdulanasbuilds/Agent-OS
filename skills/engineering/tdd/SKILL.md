---
name: tdd
description: Build one observable behavior at a time with a red-green-refactor feedback loop.
---
# TDD

State the behavior first. Write one failing test through the highest useful public interface. Implement the smallest change that passes. Repeat. Refactor only while green.

Run focused tests frequently and the relevant broader suite before release. Avoid speculative test suites and tests that lock in private implementation details.

Keep security, migration, accessibility, performance, and release checks as separate gates when applicable.
