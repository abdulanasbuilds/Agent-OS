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


## High-value recipes

Use these as starting patterns; adapt them to the project's existing tokens and component system.

### CSS press feedback
```css
.button {
  transition: transform 160ms ease-out;
}
.button:active {
  transform: scale(0.97);
}
```

### Entry without `scale(0)`
```css
.surface {
  opacity: 1;
  transform: scale(1);
  transition: opacity 180ms cubic-bezier(0.23, 1, 0.32, 1),
              transform 180ms cubic-bezier(0.23, 1, 0.32, 1);
  @starting-style {
    opacity: 0;
    transform: scale(0.95);
  }
}
```

### Trigger-aware surface
When a component exposes a reliable trigger-origin value, set `transform-origin` from that value rather than forcing every anchored surface to originate from center. Keep centered modals centered.

### Dynamic UI
For toasts, toggles, and other rapidly repeated state changes, prefer transitions or springs that can retarget. Avoid keyframes that restart from zero when interruption is possible.

### Stagger
Keep group-entry delays short, roughly 30–80ms. Never make the UI wait for the entire stagger sequence before accepting input.

### Blur bridge
For a crossfade that visually double-exposes two states, test a subtle `blur(2px)` during the transition rather than stacking heavier opacity tricks. Keep expensive filters restrained and verify on realistic devices.

## Engineering caveat

Do not freeze library-specific rendering claims as universal truths. For Motion, GSAP, browser APIs, and other libraries, verify current behavior against the current installed version and actual runtime traces. The durable rule is to prefer the simplest mechanism that stays smooth, interruptible, accessible, and maintainable.

