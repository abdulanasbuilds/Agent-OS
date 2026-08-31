---
name: human-readable-output
description: Make default user-facing explanations, questions, status updates, and completion reports understandable to a non-specialist without sacrificing technical correctness.
---
# Human-Readable Output

Default to plain, direct language.

Use the pattern:

- what happened;
- why it matters;
- what was checked;
- what remains;
- what the user needs to decide, if anything.

Avoid unexplained acronyms and dense implementation jargon. When a technical term is necessary, explain it briefly in ordinary words.

Do not hide failures or uncertainty behind vague language. Say what failed, where, and what evidence supports the diagnosis.

Code, stack traces, schemas, configuration files, and other technical artifacts may use normal engineering terminology when that is their required format.