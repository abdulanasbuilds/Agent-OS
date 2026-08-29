# Design Clone Workflow

"Clone this" is interpreted as a fidelity request, not permission to copy protected material.

## 1. Classify the source

```text
owned by project → faithful recreation
explicitly authorized → faithful within authorization
public but unlicensed/unknown → analyze and reconstruct principles/behavior with original assets
unclear ownership → pause only where the uncertainty changes what can be shipped
```

## 2. Measure before coding

Capture:
- target viewport/device
- page/flow inventory
- hierarchy
- spacing rhythm
- typography roles
- colors/surfaces
- component states
- interaction behavior
- motion timing/choreography
- responsive transitions

## 3. Isolate

Build the recreation in a local branch/worktree/design-lab directory. Never overwrite the main implementation while exploring fidelity.

## 4. Compare

Use repeatable screenshots and interaction checks at agreed sizes. Log each meaningful deviation instead of relying on memory.

## 5. Rights boundary

Do not scrape or redistribute proprietary source code, logos, brand assets, fonts, photographs, illustrations, videos, or screenshots merely because the source is publicly reachable. Use project-owned, licensed, or original replacements when rights are unavailable.

## 6. Promotion

Only the selected, reviewed implementation moves into the main project. Record the final fidelity level and important deviations in `DESIGN-REFERENCES.md` or `DECISIONS.md`.
