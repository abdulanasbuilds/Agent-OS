# Curated Design Resources

Agent OS uses external design resources as reference material first. Do not install or execute a resource merely because it exists.

## Reviewed foundations

### Web Interface Guidelines — Vercel
Use as a current review reference for web accessibility, focus, forms, typography, images, animation, and performance.

https://github.com/vercel-labs/web-interface-guidelines

### shadcn/ui
Use for accessible, customizable source-owned components and current component documentation. Inspect project configuration before adding components.

https://github.com/shadcn-ui/ui

### Radix Primitives
Use when accessible unstyled React primitives fit the project's architecture. The primitives handle important behavior such as focus management and keyboard navigation while leaving visual design to the project.

https://www.radix-ui.com/primitives

### Motion for React
Use for purposeful UI animation and interaction. Reduced-motion behavior must be designed alongside the default motion path.

https://motion.dev/docs/react

### WCAG 2.2
Use as the accessibility baseline for web interfaces where applicable.

https://www.w3.org/TR/WCAG22/

### MDN accessibility and motion references
Use for browser behavior and platform-level details such as `prefers-reduced-motion`.

https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion

## Adoption rule

Third-party resources are not automatically trusted. Before adopting code, registries, plugins, MCP servers, fonts, images, templates, or executable installers, evaluate provenance, license, maintenance, permissions, dependencies, network behavior, and prompt-injection/tool-poisoning risk.

Prefer extracting durable principles into Agent OS-native skills over vendoring an entire external repository.
