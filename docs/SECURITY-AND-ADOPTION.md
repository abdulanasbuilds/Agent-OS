# Security and Adoption Standard

Agent OS does not treat popularity, stars, vendor branding, or a README as evidence that an integration is safe.

## Review gates

Before adding any third-party skill, MCP server, plugin, extension, package or script:

1. Identify the publisher and repository provenance.
2. Read the entrypoint files and every executable file that can run automatically.
3. Inspect requested permissions, filesystem access, environment-variable access, subprocess use and network calls.
4. Check maintenance signals, release history and known security issues.
5. Determine whether the capability is actually necessary.
6. Prefer an Agent OS-native implementation when the useful behavior is simple and can be represented as instructions instead of executable code.
7. Pin versions or commits when executable dependencies are unavoidable.
8. Record the decision and references under `docs/`.

## Rejection triggers

Reject an integration when it:

- asks for unrestricted filesystem access without a compelling reason;
- reads secrets by default;
- executes arbitrary remote code or shell content without a clear boundary;
- silently changes package registries or install sources;
- bundles opaque binaries when source is available and inspection is expected;
- has unresolved critical security concerns relevant to its intended use;
- duplicates a capability already provided safely by Agent OS or the harness;
- relies on stale or undocumented APIs for a critical workflow.

## Preferred pattern

THIRD-PARTY SOURCE → REVIEW → EXTRACT DURABLE PRACTICE → WRITE NATIVE SKILL → TEST → RECORD PROVENANCE

## Never assume

A provider's official integration can still change or contain unsafe defaults. Review the exact version and runtime behavior being adopted.
