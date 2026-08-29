---
name: design-variants
description: Build multiple intentionally different frontend design directions in an isolated local branch or preview environment before committing a high-visibility page to the main project. Use when visual direction is unresolved or the user wants options.
---

# Design Variants

Variants are controlled experiments, not random skins.

## Workflow
1. Lock the functional requirements and content.
2. Preserve the same information architecture and core interactions.
3. Define 2-4 distinct visual hypotheses with different composition, type, material, imagery, and motion choices.
4. Implement each in an isolated branch/worktree/preview path.
5. Run the same responsive, accessibility, performance, and interaction checks on each.
6. Capture screenshots or recordings and summarize trade-offs.
7. Ask the user to choose one direction before merging visual work into the primary branch.

## Variant rules
Do not create four copies that differ only by color. Change the design hypothesis meaningfully while keeping functionality comparable.

## Evaluation rubric
Score each variant for product fit, distinctiveness, hierarchy, readability, accessibility, performance, content fit, brand fit, and implementation cost.

## Safety
Do not alter production data or deploy an unapproved variant. Keep experiments isolated and reversible.
