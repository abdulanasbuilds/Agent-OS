---
name: option-lab
description: Run controlled alternative-solution experiments for decisions where multiple materially different approaches may be better, while preserving a common baseline, comparable evaluation, isolation, and explicit promotion.
---

# Option Lab

Use this for genuine design or engineering uncertainty. It is a decision-quality workflow, not a license to create unnecessary alternatives.

## Suitable uses

- visual/design directions
- architecture alternatives
- data-model alternatives
- implementation strategies
- UX flows
- API approaches
- performance strategies
- deployment approaches
- naming/copy alternatives when the decision is meaningful
- presentation narratives

## Workflow

1. Define the decision and success criteria.
2. Freeze the common requirements and constraints.
3. Identify 2-4 materially different hypotheses only when uncertainty justifies exploration.
4. Isolate each option in a branch, worktree, sandbox, document, or other reversible boundary appropriate to the task.
5. Evaluate every option using the same evidence and criteria.
6. Record trade-offs, risks, implementation cost, and what evidence changed the decision.
7. Require the authorized decision-maker to select an option when the choice is subjective or product-specific.
8. Promote only the selected option into the primary artifact.
9. Re-run the normal validation after promotion.
10. Record the final decision and why alternatives were rejected.

## Never use the lab to

- bypass security review;
- test destructive production changes;
- duplicate work with no meaningful hypothesis difference;
- create false precision with arbitrary scores;
- avoid making a necessary decision indefinitely.

## Isolation rule

An option must never silently depend on an unfinished alternative. Shared assumptions belong in the common baseline; differences belong in the option itself.

## Promotion rule

Exploration is disposable. The primary project remains stable until an option is explicitly selected and passes normal verification.
