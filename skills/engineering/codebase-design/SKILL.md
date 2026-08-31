---
name: codebase-design
description: Shape maintainable modules by hiding meaningful complexity behind small, stable, testable interfaces.
---
# Codebase Design

Before introducing a boundary, identify the complexity it should hide and the highest useful seam for callers.

Prefer deep modules with small public contracts. Keep callers away from incidental implementation details. Reuse existing seams when they are sound. Avoid speculative abstractions and wrappers that merely rename a dependency.

For a proposed boundary, record responsibility, contract, hidden complexity, dependencies, test seam, and likely change points. Validate the boundary with focused tests before broad refactoring.
