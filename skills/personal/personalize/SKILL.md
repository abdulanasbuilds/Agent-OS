---
name: personalize
description: Build or update a local personal agent profile by asking only high-value questions that materially change how agents should work for the user.
---

# Personalize

Use this skill when the user invokes `/personalize`, `/my-profile`, `/my-style`, `/my-workflow`, or `/my-stack`.

## Privacy boundary

Never store the user's actual personal answers in the public Agent OS repository. Write them only to the local ignored personal profile path configured by the harness, preferably `.agent-os-personal/` outside the repository when possible.

Never ask for passwords, API keys, recovery codes, financial-account credentials, authentication secrets, or other unnecessary sensitive data.

## Interview method

Ask the smallest useful set of questions. Ask in rounds rather than dumping a giant questionnaire.

Round 1 — working identity
- What kinds of work do you do most often?
- What are your highest-priority outcomes from an agent?
- What do you strongly prefer or strongly dislike in agent behavior?

Round 2 — engineering
- Preferred languages/frameworks when there is a choice?
- Preferred harnesses and model roles?
- How autonomous should the agent be for read, write, execute, deploy, and production actions?

Round 3 — product/design
- Design tastes and anti-patterns?
- Preferred level of visual experimentation?
- How should vague design/product requests be clarified?

Round 4 — delivery
- Preferred Git workflow?
- Preferred documentation depth?
- How should the agent report progress, uncertainty, and blockers?

Only ask another question when the answer changes routing, tool use, design decisions, or workflow behavior.

## Output schema

Create or update a local profile with these sections:

- identity_and_work
- engineering_preferences
- harness_preferences
- model_preferences
- product_preferences
- design_preferences
- communication_preferences
- git_and_release_preferences
- autonomy_boundaries
- recurring_constraints

For each stored preference include:
- value
- source: user-stated | inferred
- confidence: high | medium | low
- last_confirmed

User-stated preferences override inferred preferences. Never silently convert an inference into a hard rule.

## Conflicts

When preferences conflict with global security policy, safety, legal requirements, project constraints, or explicit current instructions, the higher-level constraint wins.

When a project-specific preference conflicts with the personal profile, the current project instruction wins for that project.
