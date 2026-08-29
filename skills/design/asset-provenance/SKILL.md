---
name: asset-provenance
description: Track the origin, license, permissions, modifications, and project assignment of fonts, images, icons, video, illustrations, screenshots, templates, and other design assets.
---

# Asset Provenance

Every external asset that enters a project must have a traceable origin and a reuse decision.

## Required record
- asset identifier and local path
- source URL
- creator or publisher when available
- asset type
- license or terms URL
- date checked
- project assigned to
- modification status
- attribution requirement if any
- restrictions or unresolved rights

## Reuse classes
- `project-owned`: created or supplied by the project owner.
- `licensed`: reuse rights were verified for the intended project.
- `open-license`: license permits the intended use and requirements are recorded.
- `reference-only`: may be viewed/analyzed but must not be shipped.
- `needs-permission`: do not ship until rights are obtained.
- `reject`: provenance or terms are unacceptable.

## Safety rules
- Never scrape and commit a third-party site's image library as a design corpus.
- Never assume a screenshot is reusable merely because it is publicly visible.
- Never assume a font is free for commercial redistribution; verify its license.
- Strip hidden credentials and metadata when project policy requires it.
- Keep downloads isolated to the intended project.

## Verification
Before release, compare shipped assets against the asset register and check that their recorded license matches the actual use.
