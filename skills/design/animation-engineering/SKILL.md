---
name: animation-engineering
description: Implement and review animation systems with appropriate browser APIs or libraries, emphasizing performance, reduced motion, interaction feedback, lifecycle cleanup, and maintainability.
---

# Animation Engineering

Choose the smallest appropriate mechanism.

## Selection order
1. CSS transitions/keyframes for simple state changes.
2. Web Animations API for framework-neutral imperative sequences when useful.
3. The project's existing motion library when it already provides the required behavior.
4. A specialized library such as Motion, GSAP, Anime.js, or Lenis only when its capability is justified.
5. Three.js or another 3D engine only when 3D is essential to the experience.

## Rules
- Do not add an animation dependency for one trivial transition.
- Prefer transform/opacity for frequently animated elements where appropriate.
- Avoid forced synchronous layout and unbounded scroll handlers.
- Clean up listeners, animation loops, observers, and timelines.
- Respect reduced-motion preferences.
- Test touch and keyboard interactions as well as pointer interactions.

## Verification
Inspect frame behavior, layout shift, CPU/GPU cost, battery impact on mobile where practical, and behavior when the user has reduced motion enabled.

## Library references
- Motion: https://motion.dev/
- GSAP: https://gsap.com/
- Anime.js: https://animejs.com/
- Lenis: https://lenis.dev/
- Three.js: https://threejs.org/
