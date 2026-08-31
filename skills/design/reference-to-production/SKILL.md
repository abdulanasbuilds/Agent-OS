---
name: reference-to-production
description: Convert an authorized or reference interface into a project-specific production UI through context capture, visual forensics, controlled cloning, design transformation, variant worktrees, motion prototyping, theme-token hardening, and evidence-based verification.
---
# Reference to Production

Use when a user has an existing app/site/reference they want to learn from, faithfully recreate when authorized, or use as the structural starting point for a distinct production design.

## 0. Establish intent and rights
Classify the source before extracting anything:
- project-owned
- authorized
- public-reference
- unknown

Use `clone-reference` for fidelity/rights rules. Public visibility alone never authorizes copying protected source code, assets, logos, fonts, or proprietary media.

## 1. Freeze project context
Read the current project brief, decisions, requirements/spec, design system, security rules, and existing UI before changing code.
Create a concise reference brief containing:
- product/business goal
- audience and primary action
- target surfaces/routes
- functional invariants
- visual invariants
- explicit deviations from the reference
- assets that are supplied, licensed, generated, or forbidden

Do not let the reference silently redefine product requirements.

## 2. Visual and implementation forensics
Inspect the reference at representative viewport sizes and states. When source code is available and authorized, inspect it. Extract evidence, not assumptions:
- page hierarchy and layout primitives
- typography roles and spacing rhythm
- component families and states
- navigation and interaction patterns
- responsive transformations
- color/theme tokens
- data-density patterns
- motion/transition sequences
- media usage and asset dimensions
- likely reusable libraries, only when evidence supports the inference

Prefer screenshots, DOM/CSS inspection, source code, and runtime behavior over visual guessing.

## 3. Build a baseline in isolation
Create a frozen baseline or authorized clone in an isolated branch/worktree. Never experiment directly on the main project branch when multiple competing designs are being explored.

The baseline is a reference artifact, not automatically the final product.

## 4. Combine the baseline with project context
Map project requirements onto the reference architecture:
- preserve required functional behavior
- replace domain language and content
- replace unauthorized/proprietary assets
- introduce the approved project design direction
- preserve useful interaction patterns only where they fit the product

Record deliberate deviations.

## 5. Controlled restyle
Use the design system and specialist skills to transform the baseline without random drift.
For an existing design, choose one explicit mode:
- retint
- skin/restyle
- structural redesign
- new visual world

Do not mix incompatible directions without documenting the decision.

## 6. Variant laboratory
When meaningful visual uncertainty exists, create isolated variants as worktrees/branches. Typical candidate set:
- small change
- medium change
- large change
- optional surprise direction

Variants must share the same functional/spec baseline. Give each a stable local preview port and record its commit/worktree path.

Never overwrite the main branch while variants are running.

## 7. Motion/media pipeline
When the project calls for rich motion or generated media:
1. Find a lawful visual/motion reference.
2. Analyze the sequence and timing.
3. Create a storyboard or keyframe sheet before expensive video generation.
4. Generate only the smallest useful media candidates.
5. Trim/reframe candidates before integration.
6. Prefer CSS/Web Animations/native motion when sufficient; use Motion/GSAP/Anime/Lenis/Three.js or an external media generator only when the capability is justified.
7. Respect reduced-motion, performance, licensing, and asset provenance.

External media-generation services are optional capabilities, not mandatory global dependencies.

## 8. Theme-token hardening
After restyling, scan the full project for hard-coded visual values that should be semantic tokens. Consolidate:
- color roles
- typography roles
- spacing scale
- radii
- elevation/shadows
- motion timings/easings
- chart colors where applicable
- light/dark mode mappings

Do not abstract one-off values merely to create a token system. Promote values that are genuinely shared.

## 9. Page/state audit
Check the entire product, not only the hero:
- every route/screen
- loading
- empty
- error
- success
- disabled
- long content
- dark/light theme
- responsive states
- keyboard/touch interaction
- contrast/focus
- console/runtime errors

Use specialist reviewers where beneficial; parallelize by independently owned surface and use worktrees when agents edit overlapping files.

## 10. Select and promote
Show the variants locally. Compare against the same project requirements, interaction paths, screenshots, accessibility checks, and performance checks.

The user selects a candidate or explicitly requests another iteration. Only then:
- promote the selected branch/worktree
- remove rejected variants
- update decisions/design documentation
- run the full project gates

## 11. Finish
Before release:
- verify no temporary clone/variant artifacts remain
- verify no unauthorized assets were promoted
- verify tokens are consistent
- verify tests/builds pass
- inspect the final diff
- run security/release gates
- commit/push/deploy only when the active permission policy allows it

## Anti-slop rule
A successful reference workflow does not mean copying a popular aesthetic. The final design must have a clear relationship to the project's audience, business goal, content, product behavior, and chosen references.
