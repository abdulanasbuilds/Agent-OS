# Design Resource Adoption

This registry records what Agent OS adopts, references, or intentionally excludes from the supplied design resources.

## Adopt as guidance

- Vercel Agent Skills: web-design-guidelines, React/React Native guidance, composition patterns. Adopt principles selectively; do not vendor deployment skills globally.
- ui-ux-pro-max: adopt the design-system reasoning pattern, style/typography/color search concepts, accessibility and anti-pattern checks. Do not vendor its CLI or generated data as a global runtime dependency.
- ibelick/ui-skills: adopt the design-engineering mindset and practical UI heuristics as reference material.
- ConardLi/garden-skills: adopt web-design-engineer concepts as reference; use pinned releases when an external skill is deliberately evaluated.
- TypeUI: adopt the idea of reusable design-system prompts and layout variations; do not require its MCP/CLI globally.
- Kimi UI/UX guidance: adopt task decomposition such as design-system extraction, wireframing, visual design, interaction, testing, and accessibility.
- Laws of UX: use as a conceptual UX reference, not as a code dependency.
- Webflow designer skills: use for broad craft considerations such as typography, layout, interaction, accessibility, content, and responsive thinking.

## Reference-only resource galleries

- Recent Design
- Awwwards
- Behance
- Dribbble
- Figma Community
- Relume Community
- daily.dev design/inspiration content

These are discovery and inspiration sources. Agent OS should store links and observations, not copy protected assets or complete designs without permission. Figma explicitly describes Community as a place for shared design resources, templates, plugins, widgets, and apps, and notes that Community resources are published by creators. The repository's own community-resource index also advises due diligence and security review. 

## Motion and rendering references

- Motion: preferred React motion reference when the project already uses it; always support reduced motion.
- GSAP: powerful timeline/sequence tool; project-level and justified, not a global default.
- Anime.js: useful lightweight animation engine; project-level and justified.
- Lenis: smooth-scroll layer only when smooth scrolling materially improves the experience; not a default dependency.
- Three.js: use only when 3D is essential to the product or storytelling; treat as a higher-complexity project dependency.
- LottieFiles: use as an asset source only when the specific asset has an appropriate reuse license; prefer original or licensed assets.
- Animate.css: useful for small CSS animations, but CSS should be preferred directly for simple effects when that avoids a dependency.
- Aceternity UI: source of copyable component ideas; use selectively and redesign rather than defaulting to its recognizable effects.
- HeroUI and MUI: component-library references for projects that actually choose those ecosystems; do not force either into every project.

## Explicit global exclusions

Do not install these as global mandatory dependencies or executable plugins:
- arbitrary third-party MCP servers
- deployment automation from design repositories
- image-generation plugins that can write files or execute code without project approval
- remote tool servers with broad filesystem/shell permissions
- complete design repositories vendored wholesale merely for inspiration

## Security note

A “no known vulnerabilities” result for a package is not equivalent to zero risk. Agent OS treats package provenance, permissions, dependencies, maintenance, licenses, runtime behavior, and prompt-injection exposure as separate review questions. For example, current security scans may show no direct issues for Motion, Anime.js, Lenis, GSAP, or Three.js versions reviewed, but dependencies and future releases still require project-level auditing.

## Source links

- https://vercel.com/docs/agent-resources/skills
- https://github.com/vercel-labs/agent-skills
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- https://recent.design/
- https://lottiefiles.com/
- https://animejs.com/
- https://lenis.dev/
- https://gsap.com/
- https://motion.dev/
- https://ui.aceternity.com/
- https://www.awwwards.com/
- https://www.behance.net/
- https://dribbble.com/
- https://www.figma.com/community
- https://daily.dev/
- https://animate.style/
- https://threejs.org/
- https://heroui.com/
- https://mui.com/
- https://community.relume.io/
- https://webflow.com/blog/web-designer-skills
- https://www.typeui.sh/design-skills
- https://github.com/ConardLi/garden-skills
- https://smithery.ai/skills/anthropics/frontend-design
- https://github.com/ibelick/ui-skills
- https://www.ui-skills.com/
- https://www.kimi.ai/resources/ui-ux-design-skills-for-agents
- https://lawsofux.com/
