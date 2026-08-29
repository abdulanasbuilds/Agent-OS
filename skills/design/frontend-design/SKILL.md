---
name: frontend-design
description: Build distinctive, production-grade frontend interfaces from product context and an approved design direction. Use for pages, websites, web apps, dashboards, and interactive surfaces; route broad requests through design-router when the visual direction or product context is not yet settled.
---

# Frontend Design

## Before coding
- If the request is broad or the visual direction is unresolved, load `design-router` first.
- Read `PROJECT.md`, `DESIGN-BRIEF.md`, and `DESIGN-SYSTEM.md` when present.
- Identify the primary user task, business goal, target audience, market context, and content hierarchy.
- Check existing product patterns before inventing new ones.
- Resolve framework/runtime constraints.
- Select external references only when they improve a specific design decision.

## Implementation
Build real, functioning UI. Keep content hierarchy clear, states complete, semantics correct, responsive behavior intentional, and the approved visual direction coherent. Use existing component primitives where appropriate, but customize composition and styling to fit the product rather than reproducing library demos.

## Resource usage
Use the Agent OS reference catalog and project reference board to locate relevant inspiration, components, assets, and fonts. Verify reuse rights and provenance before copying or shipping external assets.

## Variants
When the user asks for alternatives or the brief leaves material visual uncertainty, use `design-variants` in an isolated worktree/branch rather than repeatedly replacing the main implementation.

## Anti-slop checks
Reject unexplained:
- generic hero + cards + bento formulas
- excessive gradients/glows/glass
- arbitrary huge headings
- default fonts selected without reasoning
- decorative animations with no purpose
- copied visual signatures from another brand

## Quality gate
Before calling the interface complete, render it and inspect representative desktop/mobile states, interaction states, accessibility behavior, performance-sensitive effects, and the final diff. Report unresolved assumptions rather than inventing certainty.
