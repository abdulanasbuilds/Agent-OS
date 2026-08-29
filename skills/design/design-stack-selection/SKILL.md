---
name: design-stack-selection
description: Select frontend UI, animation, rendering, icon, typography, and visual tooling for a project without unnecessary dependencies. Use when choosing a design stack or adding a new visual library.
---

# Design Stack Selection

Select a stack from constraints, not from popularity.

## Decision order
1. Existing project stack and conventions.
2. Required interaction and rendering capability.
3. Accessibility and platform support.
4. Performance and bundle/runtime budget.
5. Maintainability and team familiarity.
6. License/provenance and supply-chain risk.
7. Developer experience and documentation quality.

## Defaults
- CSS first for simple visual states.
- Existing component system before a second component library.
- Motion library only when CSS/Web Animations are insufficient.
- GSAP/Anime.js for advanced timelines or imperative sequences when justified.
- Lenis only when smooth scrolling is a deliberate experience choice.
- Three.js only for genuine 3D requirements.

## Rule
Do not combine Motion + GSAP + Anime.js + Lenis merely because all four are available. One project should normally have a small, coherent motion stack.

## Output
Document the selected stack, rejected alternatives, reasons, versions, license considerations, and performance/accessibility expectations in the project design system.
