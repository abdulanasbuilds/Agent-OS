# Design Routing

Use design capabilities progressively. Do not load every design skill for every task.

## Routing rules

### New website/app/page with vague visual requirements

For a new public-facing or high-visibility surface with unresolved visual direction, load:
- `design-intake`
- `design-business-analysis`
- `reference-discovery`
- `visual-reference-analysis`
- `design-direction`
- `design-system`
- `design-variants` when genuine visual uncertainty remains
- `frontend-design`
- `responsive-design`
- `accessibility`
- `anti-ai-slop`
- `ui-audit`

Use browser verification where the environment supports it.

For small changes or already-approved directions, skip unnecessary research and variants.

### User provides screenshots/reference sites
Load:
- `design-intake`
- `reference-discovery`
- `visual-reference-analysis`
- `design-direction`
- `design-system`
- `frontend-design`

Add `design-variants` when the supplied reference is inspiration rather than an approved direction and meaningful alternatives should be explored. Add `asset-art-direction` when imagery is part of the reference.

### Typography-focused task
Load `typography` and `design-system`.

### Component/library task
Load `component-architecture`, `interaction-design`, `responsive-design`, and `ui-audit` as appropriate.

### Animation/motion task
Load:
- `motion-system`
- `animation-engineering`
- `ui-audit`

Prefer the project's existing animation mechanism before adding a new dependency.

### 3D/WebGL task
Load `animation-engineering` and the project-specific 3D tooling guidance only after the product need for 3D is established.

### Existing UI review
Load:
- `ui-audit`
- `anti-ai-slop`
- `responsive-design`
- `accessibility`
- `performance`

### Design selection request
Load `reference-discovery`, `visual-reference-analysis`, `design-variants`, and use the Design Lab workflow. Do not merge a variant merely because the agent prefers it.

### Reference-first workflow
For unresolved high-visibility frontend work, search progressively:
curated/project references → template/community ecosystems → live industry/product websites → broad web/image discovery.

Use the smallest useful set. Record reference ancestry and licensing/reuse status. Reference research must precede arbitrary visual invention, while small or already-settled tasks may skip the workflow.

## Principle
Load the minimum set that covers the task. Skills are not badges; unnecessary context reduces attention and can encourage generic output.
