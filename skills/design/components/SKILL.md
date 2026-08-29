---
name: components
description: Plan, select, compose, and review reusable UI components and primitives while preserving product-specific visual language, accessibility, consistency, and maintainability.
---

# Components

Components are a system, not a shopping list.

## Process
1. Inventory existing project components before creating new ones.
2. Identify repeated interaction patterns.
3. Prefer accessible primitives when they provide the behavior required.
4. Define component anatomy, states, variants, responsive behavior, and interaction rules.
5. Compose complex interfaces from smaller primitives.
6. Keep content semantics independent from purely visual styling.

## Libraries
Use existing libraries only when they fit the project's stack and license. For shadcn/ui, inspect the project's configuration and current component docs before adding or changing components. Radix is useful where accessible unstyled primitives are appropriate.

## Anti-slop rule
Do not use a library's demo styling as the final visual identity. Adapt components to the project's design system.

## Verification
Check default, hover, focus, active, disabled, loading, error, empty, overflow, mobile, keyboard, and reduced-motion states where relevant.

## Safety
Do not run component installers blindly. Review the command, package source, version, changed files, and dependency impact first.

## References
- https://ui.shadcn.com/
- https://www.radix-ui.com/primitives
