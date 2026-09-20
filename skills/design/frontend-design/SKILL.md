---
name: frontend-design
description: Build distinctive, production-grade frontend interfaces from product context and an approved or reference-informed design direction; use design-router for unresolved high-visibility work.
---

# Frontend Design

## Before coding

- If the request is broad or the visual direction is unresolved, load design-router first.
- Read PROJECT.md, DESIGN-BRIEF.md, and DESIGN-SYSTEM.md when present.
- Identify the primary user task, business goal, target audience, market context, and content hierarchy.
- Resolve framework/runtime constraints.
- Check existing product patterns before inventing new ones.
- For unresolved high-visibility work, confirm that reference discovery and visual-reference analysis happened before styling decisions.
- Use the selected design direction as the implementation contract; do not keep inventing alternate visual systems during coding.

## Reference-informed implementation

Use the Agent OS reference catalog and project reference board to locate relevant inspiration, components, assets, and fonts.

For high-visibility public-facing work, prefer a small, diverse reference set and preserve the chain:

SOURCE → OBSERVATION → PRINCIPLE → ADAPTATION

References are research evidence, not automatic code or asset sources.

Verify reuse rights and provenance before copying or shipping external assets, templates, fonts, code, or media. When rights are unclear, recreate the useful principle from first principles with original/project-owned/licensed material.

## Implementation

Build real, functioning UI. Keep content hierarchy clear, states complete, semantics correct, responsive behavior intentional, and the approved/reference-informed visual direction coherent.

Use existing component primitives where appropriate, but customize composition and styling to fit the product rather than reproducing library demos or marketplace templates wholesale.

## Variants

When the user asks for alternatives or the brief leaves material visual uncertainty, use design-variants in an isolated worktree/branch rather than repeatedly replacing the main implementation.

Do not start by coding four cosmetic skins. Research the visual problem first, then create materially different hypotheses when justified.

## Anti-slop checks

Reject unexplained:
- generic hero + cards + bento formulas
- excessive gradients/glows/glass
- arbitrary huge headings
- default fonts selected without reasoning
- decorative animations with no purpose
- copied visual signatures from another brand
- dependence on a single marketplace/template structure
- cosmetic variants that are structurally identical

Every major visual decision should be explainable from product, audience, content, brand, market, or a documented reference principle.

## Quality gate

Before calling the interface complete:
- render and inspect representative desktop/mobile states;
- verify interaction states;
- check accessibility behavior;
- check performance-sensitive effects;
- use browser verification when available for web work;
- run the anti-AI-slop gate;
- confirm reference/asset provenance is recorded;
- inspect the final diff;
- report unresolved assumptions rather than inventing certainty.
