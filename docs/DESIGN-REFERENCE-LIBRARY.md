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

When the user asks for a new or high-visibility design:
1. Determine the product/business/audience/market context and primary design question.
2. Search the reference catalog and project-owned references first.
3. Search relevant template/community ecosystems when they can answer the design question.
4. Search current live industry/product websites, including relevant geography/market and comparable user journeys.
5. Use broader web/image/source tools only when the higher-signal tiers do not answer the question.
6. Prefer a small, diverse, high-signal reference set over a large moodboard.
7. Extract principles: hierarchy, typography, spacing, imagery, interaction, motion, component behavior, responsiveness.
8. Build a synthesis chain: SOURCE → OBSERVATION → PRINCIPLE → ADAPTATION.
9. Separate research references from assets/templates cleared for direct reuse.
10. Save only project-relevant references.

## Reference-first variant research

For unresolved high-visibility frontend work, reference research should happen before design variants are invented.

Each variant should be traceable to the research through a compact reference ancestry record:
- source and URL;
- why it was selected;
- observed principle;
- transferable pattern;
- product-specific element intentionally not copied;
- licensing/reuse status;
- adaptation rationale.

Multiple independent source categories are preferred when practical. One external source should not dictate the entire visual direction unless it is project-owned or explicitly authorized.

## Images and screenshots

A screenshot can be evidence for analysis without being licensed as a reusable asset. Do not automatically ship screenshots from galleries, marketplaces, community resources, competitors, or live sites.

For asset sources, record the exact asset URL and current license page. Avoid assets containing trademarks, identifiable people, artwork, or other rights-sensitive material when the intended usage could require additional permission.

## Fonts

Treat fonts as assets with licenses. Prefer established open-font sources and self-hosting when appropriate. Record the family and license in the project asset register.

## Motion references

Use motion libraries and galleries to study timing, easing, choreography, gesture, transition purpose, and accessibility. Do not import a motion library merely because a reference uses it.

## Business design

A beautiful reference that does not serve the project's job is a bad reference. Every major reference should answer at least one question about trust, comprehension, conversion, navigation, product understanding, or interaction quality.
