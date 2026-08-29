---
name: component-architecture
description: Design reusable interface components with clear anatomy, variants, states, composition, and responsive behavior. Use for component libraries and repeated UI patterns.
---

# Component Architecture

A component should encode a real reusable pattern, not hide a one-off design.

## Process
- Start from repeated product patterns and user tasks.
- Define anatomy, responsibilities, states, variants, slots, and composition rules.
- Keep variant count small; do not turn every visual difference into a prop.
- Separate content from presentation where practical.
- Preserve keyboard, touch, focus, loading, error, and disabled behavior.
- Prefer composition over boolean-prop explosion.

## Verification
Test every meaningful state and at least one realistic content extreme. Check mobile interaction, keyboard access, focus visibility, and responsive layout.

## Anti-slop rule
Do not build a giant generic component system before the product actually needs it. Extract patterns after observing repetition.
