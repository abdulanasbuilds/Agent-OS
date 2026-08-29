---
name: motion-system
description: Design purposeful interface motion, transitions, gestures, scroll behavior, feedback, and microinteractions that reinforce hierarchy without overwhelming users. Use for animated web or app interfaces.
---

# Motion System

Motion communicates state, hierarchy, continuity, and feedback. It is not decoration by default.

## Define before implementing
- what changed
- why the user needs to perceive the change
- trigger and interaction
- duration and easing character
- spatial relationship
- interruption behavior
- reduced-motion alternative

## Use motion for
- continuity between related states
- orientation and hierarchy
- confirmation and feedback
- progressive disclosure
- attention to important but non-critical events

## Avoid
- animation on every element
- long entrance sequences that delay content
- parallax used only because it is trendy
- cursor-following effects on ordinary interfaces
- animation that competes with primary tasks

## Accessibility
Respect `prefers-reduced-motion`. Preserve meaning and feedback when motion is reduced, usually through opacity, color, instant state changes, or other non-spatial cues.

## Performance
Prefer compositor-friendly transforms/opacity where practical. Measure expensive effects rather than assuming a GPU-friendly transform makes everything cheap.

## References
- https://motion.dev/docs/react-accessibility
- https://motion.dev/docs/react-use-reduced-motion
