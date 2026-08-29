# Design Routing

Use design capabilities progressively. Do not load every design skill for every task.

## Routing rules

### New website/app/page with vague visual requirements
Load:
- `design-intake`
- `design-direction`
- `design-system`
- `anti-ai-slop`
- `responsive-design`
- `frontend-design`

If the visual direction remains unresolved, add `design-variants` before implementation.

### User provides screenshots/reference sites
Load:
- `design-intake`
- `visual-reference-analysis`
- `design-direction`
- `design-system`
- `frontend-design`

Add `asset-art-direction` when imagery is part of the reference.

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
Load `design-variants` and use the Design Lab workflow. Do not merge a variant merely because the agent prefers it.

## Principle
Load the minimum set that covers the task. Skills are not badges; unnecessary context reduces attention and can encourage generic output.
