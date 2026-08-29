---
name: design-system
description: Define an implementation-ready design system for a project or major surface, including tokens, type, layout, components, states, imagery, motion, accessibility, and performance constraints.
---

# Design System

Build a system, not isolated pretty screens.

## Required layers
- semantic color tokens rather than hard-coded page colors
- typography families, roles, scale, line-height, tracking, and loading strategy
- spacing and layout rhythm
- container/grid rules and responsive breakpoints
- shape language, borders, shadows, surfaces, and elevation
- component anatomy and variants
- interaction states: default, hover, focus, pressed, disabled, loading, success, error, empty
- imagery and icon rules
- motion principles and reduced-motion behavior
- accessibility and contrast requirements
- performance budgets for fonts, images, JavaScript, and animation

## Workflow
1. Start from the Design Brief and chosen direction.
2. Create semantic tokens before component styling.
3. Define a small core component vocabulary.
4. Document reusable patterns and exceptions.
5. Persist the system in the project design directory.
6. Review pages against the system before release.

## Rule
Do not invent a new visual treatment for each section unless the design system explicitly calls for controlled variation.
