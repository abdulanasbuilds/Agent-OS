# Design Reference Library

## Why this exists

Agents often produce generic UI because they reason from model memory instead of inspecting real visual evidence. Agent OS provides a curated reference index so the agent can search real interfaces, interactions, typography, motion, components, and imagery when those references materially improve a design decision.

This is a **research system**, not a content mirror.

## Three layers

### 1. Global source index
`references/DESIGN-REFERENCE-CATALOG.yml` contains source metadata and usage rules.

### 2. Project reference workspace
Each project may keep its own:

```text
references/
├── sites/
├── mobile/
├── screenshots/
├── components/
├── motion/
├── typography/
├── imagery/
└── notes/
```

Store URLs, notes, screenshots, or assets only when the project has a legitimate basis to retain them.

### 3. Asset register
Every shipped external asset is recorded in `ASSET-REGISTER.md` with source and rights information.

## Search behavior

When the user asks for a design:
1. Determine the product/business/audience context.
2. Search the reference catalog for relevant sources.
3. Use current web/image/source tools available to the harness.
4. Prefer several high-signal references over a giant moodboard.
5. Extract principles: hierarchy, typography, spacing, imagery, interaction, motion, component behavior.
6. Separate references from assets cleared for use.
7. Save only project-relevant references.

## Images and screenshots

A screenshot can be evidence for analysis without being licensed as a reusable asset. Do not automatically ship screenshots from galleries or competitors.

For asset sources, record the exact asset URL and current license page. Avoid assets containing trademarks, identifiable people, artwork, or other rights-sensitive material when the intended usage could require additional permission.

## Fonts

Treat fonts as assets with licenses. Prefer established open-font sources and self-hosting when appropriate. Record the family and license in the project asset register.

## Motion references

Use motion libraries and galleries to study timing, easing, choreography, gesture, transition purpose, and accessibility. Do not import a motion library merely because a reference uses it.

## Business design

A beautiful reference that does not serve the project's job is a bad reference. Every major reference should answer at least one question about trust, comprehension, conversion, navigation, product understanding, or interaction quality.
