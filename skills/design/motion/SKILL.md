---
name: motion
description: Design and implement purposeful interface motion, transitions, gestures, and scroll effects with performance and reduced-motion accessibility built in.
---

# Motion

Motion exists to communicate or enhance an interaction. It is not decoration by default.

## Motion roles
- state change
- spatial continuity
- hierarchy/focus
- feedback
- progress
- guided attention
- intentional delight

## Process
1. Identify the user event that causes motion.
2. Define what the motion communicates.
3. Choose the smallest animation that communicates it.
4. Prefer compositor-friendly properties where practical.
5. Define duration/easing or spring behavior consistently with the product.
6. Define interruption/cancellation behavior.
7. Define reduced-motion behavior before shipping.

## Accessibility
Honor `prefers-reduced-motion`. Replace large transforms, parallax, and similar motion with opacity/color/state changes where possible. Do not make motion essential to understanding unless an accessible equivalent exists.

## Verification
Test normal motion, rapid repeated interaction, slow devices, reduced-motion preference, keyboard interaction, and route/state changes.

## References
- https://motion.dev/docs/react-accessibility
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- https://www.w3.org/TR/WCAG22/
