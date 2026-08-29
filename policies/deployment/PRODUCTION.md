# Production Policy

Before release: tests pass, security checks pass, configuration is reviewed, secrets are externalized, migrations are understood, rollback exists, final diff is inspected, and monitoring is available.

Destructive production actions require explicit authorization unless a documented automation policy says otherwise.