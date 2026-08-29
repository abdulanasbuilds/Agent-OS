# Design Variant Lab Contract

Use this companion contract with `design-variants` when a local visual comparison is useful.

## Required behavior

- Keep `main` and the primary project workspace unchanged while variants are being explored.
- Prefer one Git worktree/branch per materially different variant.
- Build from the same functional baseline, content contract, and dependency state.
- Use separate preview ports and output folders for each web variant.
- For mobile/desktop work, isolate build artifacts and use the appropriate simulator/device/preview environment.
- Capture representative screenshots at the same viewport sizes for every candidate.
- Run the same functional, accessibility, responsive, performance, and visual checks for every candidate.
- Present the candidates side-by-side and wait for an explicit selection.
- Promote only the selected variant to the primary branch/workspace.

## Do not

- overwrite the primary branch during exploration;
- deploy an unapproved candidate;
- create variants solely by changing colors;
- copy proprietary assets or code without a clear reuse basis;
- fabricate a winner when the evidence is inconclusive.
