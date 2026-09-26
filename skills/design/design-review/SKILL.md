---
name: design-review
description: Adversarially review an interface for visual quality, hierarchy, usability, accessibility, responsiveness, performance, and resistance to generic AI-generated design patterns.
---

# Design Review

Review the actual rendered interface when possible, not only source code.

## Review order
1. Product/message clarity
2. Visual hierarchy
3. Composition and spacing rhythm
4. Typography
5. Color and contrast
6. Component consistency
7. Interaction states
8. Responsive behavior
9. Motion and reduced motion
10. Assets and authenticity
11. Accessibility
12. Performance and layout stability

## Motion review output

When motion is a material part of the review, include motion findings in the same evidence table and identify the exact property/value that is wrong.

Use these impact buckets when useful:
1. **Feel-breaking** — slow or wrong response, inappropriate high-frequency animation, bad easing, or a visible origin/jump problem.
2. **Simplification** — motion that should be removed or drastically reduced.
3. **Performance** — layout animation, thrashing, expensive effects, or avoidable main-thread work.
4. **Interruptibility** — motion that restarts instead of retargeting, or gestures that lose velocity.
5. **Accessibility** — missing reduced-motion or hover gating.
6. **Cohesion** — motion language that conflicts with the product's established character.

When a finding depends on a subjective feel that cannot be established from source alone, label the uncertainty and request rendered/browser evidence rather than pretending the code proves it.

## Anti-slop review
Flag interfaces whose strongest visual identity comes from fashionable effects rather than product-specific decisions. Look for generic hero formulas, excessive cards, arbitrary gradients, ornamental blur/glow, over-animation, and weak information hierarchy.

## Findings
For each issue state:
- severity
- affected area
- observed behavior
- why it matters
- concrete fix
- verification method

Do not label personal taste as a defect. Distinguish objective usability/accessibility problems from subjective art-direction differences.

## References
- https://github.com/vercel-labs/web-interface-guidelines
- https://www.w3.org/TR/WCAG22/


## Reconstruction review

For reference-driven website work, load `skills/design/website-reconstruction/SKILL.md` and compare the implementation route-by-route against the evidence record. Verify direct-load behavior, responsive differences, interaction states, image/media behavior, motion, white-label removals, deployment correctness, and truthful integration states—not only visual similarity.
