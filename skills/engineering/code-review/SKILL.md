---
name: code-review
description: Review a diff against explicit repository standards and originating requirements before promotion.
---
# Code Review

Start from a fixed comparison point. Report two distinct axes when possible: standards and specification fidelity. Every material finding needs evidence from the diff and the applicable rule or requirement. Distinguish defects from judgement calls.

Check relevant security, authorization, data handling, accessibility, performance, error handling, observability, maintainability, and regression risks.

If no originating spec exists, state that instead of inventing one. Review does not itself authorize merge, deploy, or production mutation.
