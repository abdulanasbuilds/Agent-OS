# Agent OS Design Constitution

## Purpose

Produce distinctive, useful, accessible interfaces that fit the product, audience, brand, and context. Avoid generic AI-generated visual patterns and trend-following for its own sake.

## Design-before-code rule

A vague request such as "make a modern website" is not sufficient to choose a final visual direction. Before implementation, gather enough context to determine:

- product and business objective
- primary audience and their expectations
- industry and market
- brand personality and constraints
- desired emotional response
- content type and information hierarchy
- reference sites or visual examples
- available photography, illustration, iconography, or video
- technical constraints
- accessibility requirements
- performance budget
- required interactions and motion

When critical context is missing, ask focused design questions before committing to a final direction.

## Anti-slop rules

Do not default to:

- the same fashionable SaaS hero used everywhere
- oversized gradient text without a product reason
- gratuitous glassmorphism
- excessive rounded cards or floating panels
- random neon gradients
- excessive blur, glow, noise, or grain used as decoration
- animated blobs with no semantic purpose
- stock imagery chosen only because it looks "AI-generated"
- excessive pills, badges, or floating UI fragments
- giant headlines that consume the entire first viewport without useful information
- arbitrary purple/blue palettes merely because they are common in AI products
- trendy fonts selected without considering the brand, language, readability, and available weights
- motion on every section
- parallax or auto-playing visual effects without a product reason

These are not forbidden technologies. They are forbidden **defaults**. A deliberate, context-supported use is acceptable.

## Distinctiveness rule

The visual direction must be explainable in terms of product and audience. If the same design could be pasted onto five unrelated companies without modification, it is probably too generic.

## Typography

Choose typography for hierarchy, readability, language support, brand fit, and performance. Do not select fonts because they are currently fashionable. Limit the type system to a deliberate role structure.

## Layout

Use hierarchy, rhythm, whitespace, density, alignment, and content priority before decoration. Avoid cards for everything. Allow plain sections, lists, editorial layouts, tables, split views, or immersive compositions when those structures better communicate the content.

## Components

Build a small coherent component vocabulary. Prefer accessible primitives and existing project components before adding new dependencies. Components should express product language rather than look like unmodified library demos.

## Motion

Motion should communicate state, hierarchy, continuity, feedback, or delight. Every non-trivial animation should have a reason to exist and a reduced-motion strategy. Respect `prefers-reduced-motion`; large transforms, parallax, and auto-playing effects require extra justification.

## Assets

Prefer authentic product photography, original illustrations, licensed assets, or intentionally art-directed imagery. Never invent factual people, facilities, products, logos, or testimonials merely to fill visual space.

## Accessibility and performance

Accessibility is part of the design system. Preserve semantic structure, keyboard access, focus visibility, contrast, readable type, equivalent content, and reduced-motion behavior. Avoid visual choices that cause unnecessary layout shift or performance cost.

## Variant rule

When the brief leaves legitimate room for multiple directions, create several **meaningfully different** variants. Do not create minor color swaps and call them variants. Each variant should differ in composition, hierarchy, typography, imagery, or interaction model.

Keep variants isolated in a design-lab branch/worktree. Only the selected direction is promoted to the main project.

## Review rule

A design is not approved because it "looks good." Review:

1. business/message clarity
2. visual hierarchy
3. brand fit
4. distinctiveness
5. usability
6. accessibility
7. responsive behavior
8. motion behavior
9. performance implications
10. implementation maintainability

## Source policy

External design systems, examples, screenshots, fonts, images, component registries, and inspiration sites are reference material. Do not copy proprietary assets or instructions into a project without checking licensing and provenance.
