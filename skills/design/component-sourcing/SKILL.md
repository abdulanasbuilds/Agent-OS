---
name: component-sourcing
description: Select UI component libraries, copyable component sources, and animation primitives based on project needs, licensing, accessibility, performance, maintenance, and ecosystem fit. Use before adding a new frontend dependency.
---

# Component Sourcing

A component source is a design and code dependency decision.

## Evaluate
- actual product need
- framework/runtime compatibility
- accessibility quality
- API/composability
- bundle and runtime cost
- dependency count and transitive risk
- maintenance and release cadence
- license and asset rights
- visual distinctiveness and customization ability
- SSR/client constraints where relevant

## Selection rule
Prefer the project's existing system when it can satisfy the requirement. Add a library when its capability materially reduces risk or effort.

## Curated reference preferences

When the project has no existing equivalent, these are useful starting points because they are focused tools rather than an excuse to expand the dependency graph:

- **Base UI** for accessible unstyled primitives.
- **cmdk** for command palettes.
- **Sonner** for notifications/toasts.
- **input-otp** for verification-code inputs.
- **Motion** for springs, gestures, and coordinated enter/exit behavior.
- **NumberFlow** for animated numeric changes.
- **Shiki** for syntax highlighting.
- **Cobe** for lightweight globe visualizations.
- **dnd kit** for drag-and-drop.
- **Virtuoso** for very long lists/tables.
- **Zustand** for shared client state when local state/composition is insufficient.
- **clsx/cva** for class composition and typed variants.

These remain recommendations, not mandatory stack decisions. Existing project architecture, current documentation, accessibility, licensing, maintenance, dependency risk, and performance still win.

## Source categories
- MUI / HeroUI: full component-system options for projects that choose those ecosystems.
- Aceternity UI: copyable effect/component inspiration; use selectively and customize.
- Relume / Figma Community: information architecture and design exploration resources, not automatic runtime dependencies.
- Motion / GSAP / Anime.js / Lenis: specialized motion tooling; choose the smallest tool that fits.
- Three.js: higher-complexity 3D runtime; justify the need first.

## Security
Do not run an installer or plugin from a resource merely because a prompt recommends it. Review provenance, package scripts, permissions, lockfile impact, and transitive dependencies first.
