# Design Variant Workflow

## Purpose

Explore design directions without contaminating the main product implementation.

## When to use

Use the variant lab when:
- the visual direction is not settled;
- the user explicitly asks for alternatives;
- the brief supports multiple credible compositions;
- a major redesign is being considered;
- the surface is new, public-facing, or otherwise high visibility.

For unresolved high-visibility frontend work, research references before inventing variants.

Do not use variants to avoid making an already-established design decision.

## Reference-first research

Use the smallest useful progressive ladder:
1. Agent OS curated references, project-owned references, and supplied references.
2. Relevant template/community ecosystems.
3. Current live industry/product websites, including relevant market/geography.
4. Broader web/image discovery only when the earlier tiers do not answer the design question.

Record the resulting reference ancestry and licensing/reuse status. Extract principles rather than cloning a source.

## Isolation

Create one branch or worktree per direction:

```text
main
├── design/variant-editorial
├── design/variant-product
├── design/variant-immersive
└── design/variant-minimal
```

Each branch should start from the same approved application state.

## Comparison protocol

Every variant must be evaluated at the same representative viewport sizes and through the same key flows.

Record:
- design thesis
- reference ancestry
- intended audience response
- information hierarchy
- strengths
- weaknesses
- accessibility findings
- performance findings
- implementation cost
- screenshots/preview URL

## Promotion

The chosen variant becomes the source for the next implementation step. Record the decision in `DECISIONS.md` and remove abandoned experimental code when appropriate.

Never merge a variant merely because it was generated first. The decision should be based on the project's success criteria.
