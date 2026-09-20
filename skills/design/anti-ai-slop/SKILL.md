---
name: anti-ai-slop
description: Detect and prevent generic AI-generated frontend aesthetics, template imitation, repetitive layouts, trend-chasing effects, and unexplained visual choices; use on every high-visibility frontend task.
---

# Anti-AI-Slop

The goal is not to avoid modern design. The goal is to avoid interchangeable design.

## Red flags

- default Inter/Arial/system typography without consideration
- giant gradient headline over a dark canvas with floating glow shapes
- glassmorphism applied to everything
- arbitrary bento grids with weak information hierarchy
- excessive pills and rounded cards
- decorative blobs, stars, noise, or grids with no conceptual reason
- cursor-followers or magnetic effects on ordinary interfaces
- repeated text reveals and parallax used as filler
- copied layouts from popular AI/SaaS galleries
- generic stock photography chosen without an art direction
- excessive dark-mode contrast and neon accents without brand justification
- visual dependence on one marketplace/template source
- “different” variants that keep the same structure and only change colors, fonts, or minor decoration

## Reference-synthesis test

For a reference-informed design, ask:
- Which external observations influenced this design?
- What principles were extracted rather than copied?
- Are the principles adapted to this product, audience, market, and content?
- Could a single external reference be recognized as the full source of the page?
- Were any protected assets, branding, code, screenshots, or distinctive artwork reused without a clear basis?

## Adversarial questions

- Could this page be mistaken for ten unrelated AI-generated sites?
- Can every major visual decision be explained by product context or a documented design principle?
- Does the design remain strong with decorative effects removed?
- Is the typography recognizable and appropriate?
- Does the composition serve the content instead of forcing content into a template?
- Did the reference research produce a genuinely product-specific design, or did the agent simply reproduce another template?
- Are the variants materially different hypotheses, or cosmetic reskins of the same layout?

## Corrective action

Do not merely remove effects.

Replace generic choices with intentional composition, typography, imagery, spacing, material, interaction, or information architecture decisions that fit the product and its real users.

When a variant is too derivative, return to the reference analysis and synthesize again instead of adding more decoration.
