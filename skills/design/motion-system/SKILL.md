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


## Specialist craft rules

These rules are intentionally more concrete than the general motion policy.

### Common interaction recipes

**Button press**
```css
.button { transition: transform 160ms ease-out; }
.button:active { transform: scale(0.97); }
```

**Popover/dropdown entrance**
Use a small scale plus opacity, not `scale(0)`. Anchor the transform origin to the triggering control. A typical pattern is `scale(0.95)` + `opacity: 0` → settled state.

**Toast/dynamic item entry**
Use an interruptible transition or `@starting-style` rather than a restart-heavy keyframe. Enter and exit from the same spatial edge.

**Group entry**
Use a short stagger, roughly 30–80ms between siblings, only when the group is occasional enough that the delay does not become friction.

**Hold-to-confirm**
The deliberate phase may use a slow progress fill; release/cancel should snap back quickly. The user must never be forced to wait for decorative motion.

### Gesture quality bar

For a drag/sheet/carousel:
- motion follows the pointer continuously after the gesture is recognized;
- preserve the original grab offset;
- capture the pointer during the gesture;
- carry release velocity into the settling animation when supported;
- project momentum when choosing a snap point when the interaction calls for flick behavior;
- use increasing resistance beyond boundaries rather than an abrupt invisible wall;
- allow the gesture to reverse without a visual jump.

### Vocabulary discipline

Use precise terms in design notes and code comments: stagger, origin-aware animation, shared element transition, rubber-banding, momentum, velocity handoff, interruptible animation, spring, damping, response, clip-path reveal, blur bridge, and layout thrashing. Avoid vague instructions such as “make it smoother.”

### Restraint test

Before adding motion, ask what information the movement communicates. If the answer is only decoration and the surface is frequent or information-dense, prefer no motion or an almost imperceptible response.

