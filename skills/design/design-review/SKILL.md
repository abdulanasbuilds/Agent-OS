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
