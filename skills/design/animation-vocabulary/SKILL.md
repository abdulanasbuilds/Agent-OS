---
name: animation-vocabulary
description: Translate vague descriptions of interface motion into precise animation terminology so people and agents can communicate about motion accurately. Use for naming or disambiguating effects, not for implementing them.
---

# Animation Vocabulary

Use when someone describes what an animation feels or looks like but does not know the technical name.

## Operating rule

Lead with the most precise term. If two terms are plausible, give the best match first and one brief distinction. Never invent terminology to make a vague description sound technical.

## Vocabulary

### Entrances and transitions
- **Fade** — opacity changes in or out.
- **Slide** — an element enters or leaves by translating.
- **Scale** — size changes through a transform.
- **Pop** — a scale/opacity entrance with a small overshoot or spring feel.
- **Reveal** — content is progressively uncovered with clipping or masking.
- **Crossfade** — one state fades into another in the same place.
- **Morph** — one visual form transforms into another.
- **Shared element transition** — a visual element travels and transforms between locations while preserving identity.
- **Layout animation** — a size or position change animates instead of snapping.
- **Continuity transition** — before and after states remain visually connected.

### Sequencing
- **Stagger** — related items animate with small offsets rather than all at once.
- **Orchestration** — several animations are deliberately timed to read as one interaction.
- **Keyframes** — explicit animation waypoints.
- **Duration** — how long motion runs.
- **Delay** — time before motion starts.

### Gesture and physicality
- **Drag** — direct pointer/touch movement.
- **Swipe to dismiss** — drag/flick behavior used to remove a surface.
- **Rubber-banding** — progressive resistance past a boundary followed by return.
- **Momentum** — movement continuing after release because velocity is carried forward.
- **Velocity handoff** — gesture release velocity becomes the initial velocity of the settling animation.
- **Interruptible animation** — motion can be redirected smoothly before completion.
- **Spring** — physics-like motion settling toward a target.
- **Bounce** — overshoot and settle.
- **Damping** — controls overshoot/oscillation.
- **Response** — designer-facing measure of how quickly a spring reaches its target.

### Transform and origin
- **Translate** — movement along an axis.
- **Transform origin** — the anchor around which scaling or rotation happens.
- **Origin-aware animation** — motion starts from the spatial source or trigger.
- **3D tilt / flip** — rotation in 3D space.
- **Perspective** — the strength of perceived 3D depth.

### Scroll and feedback
- **Scroll reveal** — motion triggered by entering the viewport.
- **Scroll-driven animation** — animation progress is tied to scroll position.
- **Parallax** — layers move at different speeds.
- **Press feedback** — immediate response to a press/tap.
- **Ripple** — expanding feedback from the interaction point.
- **Shake / wiggle** — small oscillation used as feedback.
- **Hold-to-confirm** — progress fills while the user holds an action.
- **Number ticker** — digits visibly transition between values.

### Polish and performance
- **Blur bridge** — subtle blur during a difficult crossfade to reduce double-exposure.
- **Clip-path reveal** — a reveal created by animating a clipping region.
- **Skeleton / shimmer** — a loading placeholder with animated sheen.
- **Jank** — visible stutter from missed frame deadlines.
- **Compositing** — moving work into a browser path suited to independent visual updates.
- **Layout thrashing** — repeated layout reads/writes that cause avoidable recalculation.

### Easing
- **Ease-out** — fast start, slow finish; common for responsive entrances/exits.
- **Ease-in-out** — slow/fast/slow; useful for moving an already-visible element.
- **Linear** — constant speed; appropriate for some continuous motion.
- **Cubic-bezier** — a custom easing curve.
- **Asymmetric easing** — entry and exit deliberately use different timing or curves.

## Output

For a naming request, lead with:

**Term** — one-sentence definition.

Then add a **Close alternative** only when the distinction helps choose between similar terms.

Use motion-system or animation-engineering when the user wants the effect designed or implemented.