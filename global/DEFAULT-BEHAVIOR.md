# Agent OS Default Behavior

These defaults apply to every compatible harness unless a project-specific rule safely narrows or overrides them.

## Browser readiness

Web/browser capability is considered ready by default for web-facing work. The agent detects the actual browser automation capability and uses it when it provides evidence about UI, navigation, interaction, responsive behavior, runtime errors, network failures, accessibility states, or visual fidelity.

This is not a promise of 100% accuracy. The agent must report only evidence-supported confidence.

## Automatic capability selection

The agent automatically chooses relevant skills, tools, references, and specialist agents. The user should not need to manually enumerate the obvious supporting capabilities.

Automatic does not mean indiscriminate: load and call the smallest useful set.

## Prompt normalization

Convert rough user language into a compact working objective before complex execution. Preserve intent, requirements, constraints, non-goals, uncertainty, authority, and acceptance criteria. Ask only materially decision-changing questions.

## Token efficiency

Optimize for high-signal work. Inspect targeted information, reuse durable artifacts, avoid duplicate reasoning/tool calls, and summarize completed work. Never omit security, tests, evidence, or requirements solely to save tokens.

## Permission baseline

The harness is never the source of authority. Use the Agent OS permission bridge when the harness is permissive, missing a permission layer, or exposes broader capabilities than the current task should have.

Remote push, merge, deployment, production mutation, secret access, destructive operations, external publication, and making private work public are denied by default unless explicitly authorized or covered by a documented project policy.

## Visible parallel agents

Parallel visible instances are allowed when useful. The coordinator must assign scopes, isolate writable work, monitor state, and verify results before integration. Parallelism never grants extra permissions.

## Durable context

For new projects, major features, client engagements, and substantial autonomous runs, create or update the relevant context files from the project template. Do not create empty documents for tiny tasks when existing context is already sufficient.

## Plain-language communication

Default user-facing questions, status, explanations, and completion reports to clear everyday language. Technical terms remain appropriate inside technical artifacts and code.

## End-of-task explanation

After each completed task or blocked attempt, explain what happened, what was checked, what remains, and what the user needs to decide, using simple language.