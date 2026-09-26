---
name: clone-reference
description: Recreate an interface from a reference for authorized projects, separating functional fidelity from protected content and assets and preserving an evidence-driven comparison workflow.
---

# Clone Reference

## Canonical website-reconstruction workflow

For website reconstruction, faithful website cloning, screenshot/video-driven rebuilds, or multi-route reference recreation, load `skills/design/website-reconstruction/SKILL.md` first. It is the canonical contract for route-by-route inspection, reusable architecture, asset handling, motion, white-labeling, deployment, and final validation.


Use this skill when the user explicitly wants an interface recreated from a reference.

## First classify the reference
- `project-owned`: the user owns or controls the source. Faithful recreation is allowed subject to project requirements.
- `authorized`: the user has permission to recreate it. Follow the authorization scope.
- `public-reference`: publicly viewable but reuse rights are unclear. Use it for analysis and recreate the general interaction/structural ideas without copying protected assets or source content.
- `unknown`: do not make assumptions; ask for ownership/permission context only when it changes what can be shipped.

## Fidelity ladder
For owned/authorized references:
1. visual structure
2. typography and spacing
3. component behavior
4. responsive behavior
5. motion and timing
6. content and assets when supplied/authorized

For public/unknown references:
- analyze layout, hierarchy, interaction, behavior, and implementation patterns
- use original content and project-owned/licensed assets
- do not redistribute scraped source assets or proprietary code

## Comparison workflow
1. Load the canonical website-reconstruction workflow.
2. Capture a reference record.
3. Build in an isolated local branch/worktree.
4. Compare screenshots and interaction states at agreed viewport sizes.
5. Compare every enabled route individually and record deviations explicitly.
6. Do not promote to the main project until the target fidelity level is recorded and validation gates pass.

## Hard rule
"Clone exactly" means exact within the rights and authorization actually available. It does not override licensing, copyright, trademarks, privacy, or project security policies.
