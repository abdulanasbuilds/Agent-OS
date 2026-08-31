---
name: adversarial-assessment
description: Perform an authorized, evidence-driven adversarial security assessment of a declared application target, continuously testing realistic attack paths and driving findings into remediation and retesting.
---
# Adversarial Assessment

This is Agent OS's strongest defensive security workflow. It is an adversarial assessment capability, not a permission bypass.

## Mandatory scope gate

Before any active testing, establish:
- target identity and exact environment (local, test, staging, or explicitly authorized production);
- proof of ownership or explicit authorization recorded in the project security artifacts;
- allowed domains, hosts, APIs, accounts/roles, data classes, time window, and rate limits;
- prohibited actions and stop conditions;
- whether destructive tests are allowed.

If scope or authorization is unclear, do not perform active intrusion attempts. Switch to passive review or ask for authorization.

## Adversarial mindset

Think like a determined attacker rather than a checklist runner. Look for chains of weaknesses across:
- reconnaissance and attack-surface inventory;
- authentication and session handling;
- authorization and privilege boundaries;
- object and tenant isolation;
- input handling and output encoding;
- browser/client behavior;
- APIs and backend trust boundaries;
- file and resource handling;
- business logic and workflow abuse;
- configuration and deployment exposure;
- dependency and supply-chain risk;
- secrets and sensitive-data exposure;
- rate limiting and resource-consumption controls.

Use the weakest confirmed path to demonstrate impact, but minimize damage.

## Test strategy

1. Build a target map from the authorized environment.
2. Identify trust boundaries and high-value assets.
3. Establish benign baseline requests and expected behavior.
4. Test one control boundary at a time.
5. Correlate findings across components and identities.
6. Where chaining would materially increase risk, use the least harmful proof that establishes exploitability.
7. Capture exact evidence, affected component, preconditions, impact, and confidence.
8. Do not persist, destroy data, exfiltrate real secrets, create covert access, or expand beyond scope.
9. Stop immediately on an out-of-scope target, destructive side effect, or unexplained production impact.

## Authorization testing

Test whether users can access resources, actions, or data outside their intended role or tenant. Prefer controlled test identities and synthetic data. Cover both horizontal and vertical privilege boundaries.

## Browser and API coverage

For web applications, use the browser capability to exercise real user flows and capture runtime evidence. For APIs, inventory documented and observed endpoints, then validate authentication, authorization, input handling, object ownership, business-flow restrictions, error handling, and security configuration.

Do not treat a single scanner result as proof. Correlate automated findings with source, runtime behavior, and the application's actual trust model.

## Findings

For every finding record:
- title and severity;
- exact affected asset and component;
- preconditions;
- safe reproduction evidence;
- why the control failed;
- likely impact;
- confidence;
- recommended remediation;
- regression test to add.

Never store credentials or sensitive production data in the report.

## Remediation loop

After findings are confirmed:

`finding → root cause → smallest safe fix → targeted test → adversarial retest → regression coverage`

The agent may fix issues automatically when the project policy permits it. Otherwise it must request approval before changing protected code, security configuration, production systems, or other gated resources.

## Completion

A successful assessment is not "no scanner alerts." It requires:
- authorized scope recorded;
- meaningful attack-surface coverage;
- critical trust boundaries tested;
- findings independently verified where practical;
- remediations retested;
- regression checks added for fixed issues;
- final evidence and residual risk documented.

Never claim "secure" or "fully impenetrable." Report tested scope, evidence, coverage, and remaining uncertainty.

## Reference methodology

Use the current OWASP Web Security Testing Guide and ASVS as methodology references, adapting tests to the application's threat model and authorized rules of engagement.
