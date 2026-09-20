# Global Design Policy

Agent OS treats visual quality as a product concern, not decoration.

## Anti-slop doctrine

Do not default to the current AI-generated web aesthetic. Avoid interchangeable layouts, trend-chasing gradients, excessive glass, decorative blobs, arbitrary bento grids, generic SaaS hero sections, default Inter/Arial typography, gratuitous 3D, cursor gimmicks, and animation with no communicative purpose.

A design must have a reason for its visual language. The agent should identify the product, audience, brand context, content, platform, conversion goal, and emotional target before selecting style.

## Design decisions

Every new project or major visual surface should establish:
- design direction
- typography system
- color/semantic tokens
- spacing and layout rhythm
- component language
- imagery/art direction
- interaction principles
- motion principles
- accessibility requirements
- performance budget

## Reference-first design research

For new public-facing or otherwise high-visibility frontend work where visual direction is unresolved, reference research precedes arbitrary visual invention.

Use a progressive source ladder:
1. Agent OS curated references, project-owned references, and supplied references.
2. Relevant template/community ecosystems such as Webflow Marketplace, Made in Webflow, Framer Marketplace, ThemeForest/Envato, Relume Community, and Figma Community.
3. Current live websites from the same or adjacent industry, including relevant geography/market and comparable user journeys.
4. Broader web/image discovery only when the earlier tiers do not answer the design question.

Do not require every tier. Prefer a small, diverse, high-signal set.

For each selected reference, record the source, URL, reason for selection, observed principles, transferable patterns, product-specific elements that must not be copied, licensing/reuse status, and intended adaptation.

The synthesis chain is:

REFERENCE → ANALYZE → EXTRACT PRINCIPLES → SYNTHESIZE

References should inform a product-specific direction, not become a template-cloning shortcut.

## Reference use

Reference galleries, live sites, marketplace templates, community resources, and screenshots are inspiration/evidence by default, not permission to copy protected assets, brands, layouts, code, or media wholesale. Extract principles and recreate them from first principles unless reuse is clearly authorized and licensed.

A template may be used as a direct implementation starting point only when its current license and intended project use permit it.

## Variation before commitment

When the user has not specified a visual direction, do not silently commit to one arbitrary design. Ask the Design Intake questions. For high-visibility pages with genuine visual uncertainty, complete the reference-first workflow and create 2-4 intentionally different local variants, explain their reference-informed trade-offs, and let the authorized decision-maker select one before integrating it into the primary branch.

Do not generate variants for trivial changes, already-approved directions, security/bug hotfixes, or low-value internal surfaces where additional visual exploration would not improve the decision.

## Anti-slop review

Run the anti-AI-slop review before implementation of high-visibility variants and again before promotion.

Reject:
- generic SaaS/template repetition;
- dependence on one marketplace/template source;
- identical structures disguised as multiple variants;
- unexplained trend-driven effects;
- reference copying instead of principle extraction.

Ask whether the reference research actually produced a product-specific design.

## Accessibility and performance

Motion must respect reduced-motion preferences. Interactive controls need clear states, semantic structure, keyboard/touch access, and adequate targets. Visual richness must not justify avoidable layout shift, slow loading, excessive JavaScript, or poor mobile behavior.

## Principle

Distinctive does not mean noisy. Minimal does not mean generic. The goal is intentional, coherent, memorable design that serves the product.
