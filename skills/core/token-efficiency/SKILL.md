---
name: token-efficiency
description: Keep agent work compact and high-signal by controlling context size, tool calls, repetition, and unnecessary output while preserving correctness.
---
# Token Efficiency

Optimize for useful work per unit of context, not minimum token count.

1. Load only the smallest useful skills and project documents.
2. Inspect targeted files before broad repository dumps.
3. Reuse artifacts already produced instead of regenerating them.
4. Summarize completed phases into durable artifacts and stop replaying long histories.
5. Batch compatible read operations when the harness supports it.
6. Prefer primary sources and focused retrieval for changing technical facts.
7. Do not shorten evidence, requirements, tests, or safety checks merely to save tokens.
8. Avoid speculative work, decorative output, duplicate explanations, and unnecessary refactors.
9. When several agents are working in parallel, give each a narrow context and return compact evidence to the coordinator.
10. At completion, report the result, evidence, blockers, and next state in plain language.

Efficiency is subordinate to correctness, security, and explicit acceptance criteria.
