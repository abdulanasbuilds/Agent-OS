# Design Variant Lab

## Purpose

The Design Variant Lab is the controlled experimentation workflow for web, frontend, mobile, and other interface work where visual direction is not yet settled.

The lab exists to prevent unapproved visual experiments from contaminating the primary project branch.

## Golden rule

**Explore in isolation. Select explicitly. Promote only the selected result.**

## Default flow

1. Complete enough design/business intake to establish the product goal, audience, content, functional requirements, constraints, and relevant references.
2. Freeze the shared functional contract so every variant solves the same problem.
3. Create a disposable local branch/worktree or isolated preview workspace for each materially different direction.
4. Build 2-4 variants only when the decision is genuinely uncertain or the user requests alternatives. Do not generate variants for trivial changes.
5. Start each variant with the same project baseline. A variant must not depend on another unfinished variant.
6. Run each variant locally. For web projects, expose each variant on a unique localhost port or equivalent isolated preview URL. For mobile/desktop projects, use the project's native preview/simulator path and record the exact environment.
7. Capture deterministic screenshots, key interaction recordings where useful, and a short implementation note for each variant.
8. Run the same functional, responsive, accessibility, performance, and visual checks against every candidate.
9. Present the candidates with a consistent comparison rubric.
10. Wait for an explicit selection when the user is the decision-maker. Do not silently promote a favorite.
11. Record the selected direction in the project's design-variant record and decisions log.
12. Promote only the selected implementation into the primary workspace/branch. Delete or archive discarded experiments according to project policy.

## Isolation requirements

- Never develop competing variants directly on `main`.
- Prefer Git worktrees or isolated branches when supported.
- Never share mutable build output between variants unless the toolchain guarantees isolation.
- Do not let one variant overwrite another variant's screenshots, generated assets, or environment files.
- Do not place secrets inside a variant directory merely to make a preview work.
- Never deploy an unapproved variant to production.

## Local preview contract

Every variant should report:

- variant ID
- local path/worktree
- branch name when applicable
- preview command
- preview URL/port when applicable
- runtime/toolchain used
- screenshot/recording paths
- known limitations
- cleanup status

## Comparison rubric

Use the same criteria for all candidates. Suggested criteria:

- product and business fit
- audience fit
- information hierarchy
- distinctiveness
- readability
- brand fit
- accessibility
- responsive behavior
- interaction quality
- motion quality when relevant
- performance
- implementation complexity
- maintainability

Do not use a numerical score when the evidence is too subjective to support fake precision. A qualitative comparison is preferable to fabricated certainty.

## Promotion gate

Promotion requires:

- explicit user choice, or
- a clearly documented project rule that delegates the choice to an authorized decision-maker.

Before promotion:

1. Verify the selected variant still matches the current project requirements.
2. Rebase/merge or copy the selected implementation cleanly from the isolated workspace.
3. Run the project's normal validation suite again after promotion.
4. Inspect the final diff.
5. Record the decision and discarded alternatives.

## When NOT to use the lab

Do not create multiple variants when:

- the user has already specified an approved design direction;
- the change is a small implementation detail;
- the project is in a bug/security hotfix path where variation adds risk;
- the same decision has already been made and recorded;
- generating variants would materially delay a time-critical task without increasing decision quality.

## Relationship to other skills

Use this skill with:

- `design-intake`
- `design-direction`
- `visual-reference-analysis`
- `frontend-design`
- `ui-audit`
- `responsive-design`
- `anti-ai-slop`
- `accessibility`
- `performance`
- `clone-reference` when faithful recreation is authorized

The lab controls experimentation; it does not replace normal engineering review.
