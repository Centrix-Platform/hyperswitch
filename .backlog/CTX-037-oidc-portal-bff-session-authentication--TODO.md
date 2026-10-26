---
id: "CTX-037"
title: "Implement OIDC portal sessions and explicit aggregator context switching"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "portal-authentication"
depends_on: ["CTX-016", "CTX-022", "CTX-029"]
requires_one_of: []
conflict_domains: ["auth:portal-session", "authentication-authorization-boundary", "contracts:portal-auth", "platform-contract-catalog"]
external_inputs: ["OIDC provider issuer/client configuration and approved MFA/session policy"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-037: Implement OIDC portal sessions and explicit aggregator context switching

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The portal needs human authentication rather than operational API keys in browser storage. Native JWT/user functions provide useful integration points, but the public product should authenticate through an OIDC provider and a backend-for-frontend that resolves canonical membership. Issue an HttpOnly secure browser session bound to one aggregator and environment, enforce CSRF protection, and require the agreed MFA or step-up policy for sensitive actions. Users with multiple memberships must explicitly exchange their session context after fresh authorization; editing a header or dropdown value cannot select authority. Handle logout, membership revocation, session fixation, identity-provider outages and return URLs. This ticket implements authentication lifecycle only; permission and resource checks remain mandatory under CTX-038.

## Prerequisites and dependency outputs

- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.


## Relevant code and ownership

Primary repository/workstream: **platform / portal-authentication**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/router/src/services/authentication/cookies.rs](../crates/router/src/services/authentication/cookies.rs)

- `Proposed: platform/portal_bff/auth/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:portal-session`
- `authentication-authorization-boundary`
- `contracts:portal-auth`
- `platform-contract-catalog`

## Implementation plan

- [ ] Integrate OIDC authorization-code flow with PKCE, state and nonce validation.
- [ ] Implement server-side session storage and secure cookie/CSRF policy.
- [ ] Resolve active membership and issue a single-aggregator environment-bound session.
- [ ] Implement explicit context switch, logout, revocation and sensitive-action step-up.
- [ ] Restrict callback/return URLs and redact identity/session secrets from logs.

## Acceptance criteria

- [ ] Browser JavaScript cannot read session or operational credentials.
- [ ] OIDC callbacks validate issuer, audience, state, nonce and authorized return destination.
- [ ] Switching aggregator requires an active membership and rotates session authority.
- [ ] Revoked memberships lose access within the documented bound.
- [ ] Sensitive administrative operations enforce the configured MFA/step-up policy.

## Validation scenarios

- [ ] Exercise forged callback, CSRF and session-fixation scenarios.
- [ ] Switch between two memberships and retry a stale session.
- [ ] Simulate identity-provider outage and membership revocation.

## Expected deliverables

- Portal BFF authentication routes and session store.
- OIDC deployment configuration and session security tests.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] OIDC provider issuer/client configuration and approved MFA/session policy

Record evidence and update `external_inputs_resolved` only after these inputs are verified. Continue independent work while a necessary input is pending.

## Execution guardrails

- Preserve public Platform -> Aggregator -> Merchant -> Terminal terminology and server-resolved ownership; native account/profile/MCA identifiers remain internal.
- Maintain one authoritative financial writer. Redis coordination, transport success or lease expiry cannot authorize duplicate acquirer effects; UNKNOWN outcomes require original-operation recovery.
- Use approved capture/crypto boundaries. Keep operational secrets, CHD/SAD and sensitive documents out of ordinary task evidence, logs, events, caches and source files.
- Preserve unrelated user changes. Resolve contract/schema ownership and actual changed-file conflicts before parallel implementation.
- Use synthetic/sandbox evidence for implementation. Real deployments, charges, external customer onboarding, package publication and third-party messages require their own applicable authorization and gates.

## Handoff record

Complete this section during execution; leave it unclaimed while the ticket is TODO.

- Implementation commits / PRs / repositories: _pending_
- Final schemas, contracts, configuration versions and actual paths: _pending_
- Acceptance evidence and exact validation commands/results: _pending_
- Migration, rollout and backout/forward-recovery notes: _pending_
- Verified external evidence / resolved decisions / remaining blockers: _pending_
- Downstream handoff and follow-up ticket IDs: _pending_
