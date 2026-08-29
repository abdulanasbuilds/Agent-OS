# Project Lifecycle

Agent OS treats starting work as a lifecycle, not a blank-directory event.

## Entry points

The following aliases route to the canonical `project-lifecycle` skill:

- `/new-project` — infer the project type.
- `/new-app` — application profile.
- `/new-saas` — product/SaaS profile.
- `/new-business` — business/validation profile.
- `/new-client` — client engagement profile.
- `/new-website` — public website profile.
- `/new-web-app` — web application profile.
- `/new-mobile-app` — mobile application profile.
- `/new-experiment` — experiment/prototype profile.

Aliases are entry points, not separate methodologies.

## Lifecycle

```text
request
  ↓
inspect environment
  ↓
project intake
  ↓
business/product context
  ↓
requirements + non-goals
  ↓
architecture + security
  ↓
design intake when UI is relevant
  ↓
references/assets when needed
  ↓
initial plan
  ↓
create local workspace from Agent OS template
  ↓
initialize Git
  ↓
create remote repository when authenticated capability exists
  ↓
initial validation + commit/push
  ↓
handoff with exact state
```

## Business-first rule

A new business is not automatically a new software product. Determine the customer, problem, alternatives, acquisition path, urgency, trust, willingness to pay, economics, and validation evidence first.

## Client rule

Client projects should establish authorized scope, ownership of assets, stakeholder/approval boundaries, confidentiality, and repository visibility before work begins. Private is the default for proprietary/client repositories.

## Collision rule

A project name or repository that already exists is a stop condition. Never silently merge, overwrite, or reuse an existing project during bootstrap.

## Local creation

`scripts/new-project.sh` is the supported local bootstrap helper. It creates the project from the canonical template and can create/push a GitHub repository when the GitHub CLI is installed and authenticated.

The helper must not be treated as a permission bypass. The agent must still perform intake, collision checks, visibility decisions, and security checks first.

## Environment limitation

If the environment lacks an authenticated GitHub capability, local project creation may succeed while remote creation does not. The agent must report that exact state rather than claiming the remote exists.
