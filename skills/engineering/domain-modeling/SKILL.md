---
name: domain-modeling
description: Establish precise domain vocabulary and durable domain decisions before complexity spreads through code.
---
# Domain Modeling

Read existing context documents, glossary, ADRs, and code before introducing terminology. Find overloaded or vague nouns and resolve them against the actual business domain.

Update the project's domain context when terminology is settled. Record an ADR only for a hard-to-reverse, surprising, or high-impact decision. Keep vocabulary separate from implementation detail and propagate agreed nouns into specs, tickets, tests, data models, APIs, and UI.

Do not trigger broad renames merely for style; evaluate migration and compatibility costs first.
