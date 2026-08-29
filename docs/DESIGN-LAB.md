# Design Lab

Design Lab is the controlled workflow for exploring frontend directions before merging a visual decision into a primary project branch.

## Goal

Let the user compare real, functioning design alternatives without polluting the main implementation.

## Workflow

1. Start from `templates/project/design/DESIGN-BRIEF.md`.
2. Collect only the missing decisions that materially affect the visual outcome.
3. Analyze supplied screenshots, websites, brand assets, or references.
4. Create a design system proposal.
5. Generate 2-4 distinct variants when the user has not approved a direction.
6. Put each variant in an isolated branch/worktree/preview path.
7. Run the same content, responsive, accessibility, performance, and interaction checks.
8. Capture screenshots/recordings and present a comparison matrix.
9. User selects a direction.
10. Merge only the selected visual direction into the project branch.

## Variant dimensions

A meaningful variant may change:
- composition
- typography
- density
- imagery/art direction
- material/surface treatment
- interaction rhythm
- motion language

Do not create cosmetic color swaps and call them separate concepts.

## Local preview contract

The agent should prefer a local preview command already defined by the project. It must not invent deployment or production mutations. If a framework has no local preview command documented, inspect the project's package scripts first.

## Approval boundary

No design variant becomes the primary implementation until the user selects or explicitly authorizes it.

## Deliverables

Each variant should produce:
- variant name
- design rationale
- screenshots at agreed viewport sizes
- known trade-offs
- accessibility/performance notes
- implementation cost
- assets and their provenance

## Safety and IP

Reference analysis may borrow principles but should not reproduce protected artwork, logos, proprietary illustrations, or complete branded layouts without permission.
