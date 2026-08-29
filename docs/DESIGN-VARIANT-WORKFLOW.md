# Design Variant Workflow

## Purpose

Explore design directions without contaminating the main product implementation.

## When to use

Use the variant lab when:
- the visual direction is not settled;
- the user explicitly asks for alternatives;
- the brief supports multiple credible compositions;
- a major redesign is being considered.

Do not use variants to avoid making an already-established design decision.

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
