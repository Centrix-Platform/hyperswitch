---
id: "CTX-109"
title: "Integrate the portal with secure BFF sessions and OIDC"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Portal authentication"
depends_on: ["CTX-037", "CTX-038", "CTX-044", "CTX-108"]
requires_one_of: []
conflict_domains: ["dashboard-auth", "portal-bff"]
external_inputs: ["Approved OIDC provider/client registration, callback domains and test memberships. Production identity configuration is a later gated deployment input."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-109: Integrate the portal with secure BFF sessions and OIDC

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The browser must authenticate people through the platform identity service without storing aggregator operational keys or native Hyperswitch admin credentials. CTX-037 supplies backend OIDC/session foundations; this ticket connects the actual React/ReScript portal to that backend and verifies browser-specific boundaries. Sessions are bound to an environment and one active aggregator membership, with server-derived permissions and controlled context switching. Secure HttpOnly cookies reduce token exposure but require an explicit CSRF design and correctly scoped cookie/domain settings. Authentication redirects, custom domains, logout and expired memberships must behave consistently. CORS is an allowlist for approved origins and never a substitute for authorization. Preserve safe return destinations and ensure errors do not leak whether another aggregator or membership exists.

## Prerequisites and dependency outputs

- [CTX-037](CTX-037-oidc-portal-bff-session-authentication--TODO.md) - consume its completed, reviewed deliverables: Implement OIDC portal sessions and explicit aggregator context switching.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-108](CTX-108-white-label-dashboard-runtime-baseline--TODO.md) - consume its completed, reviewed deliverables: Fork and detach the Aggregator Portal runtime from upstream branding and services.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Portal authentication**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/router/src/routes/user.rs](../crates/router/src/routes/user.rs)

- `Proposed: services/portal-bff/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-auth`
- `portal-bff`

## Implementation plan

- [ ] Implement BFF login, callback, session discovery, renewal and logout integration using the contracts from CTX-037.
- [ ] Configure Secure/HttpOnly/SameSite cookies appropriate to the approved domain topology, and require the selected CSRF defense for state-changing browser requests.
- [ ] Apply validated Origin/Referer and CORS policy with exact approved origins and explicit credential handling.
- [ ] Map server session capabilities to portal state; remove browser storage of operational/native admin secrets and sanitize return URLs.
- [ ] Handle expiry, membership revocation, authorization-version changes and concurrent tabs without silently retaining previous aggregator data.
- [ ] Document authentication behavior for custom domains and federated logout failure cases.

## Acceptance criteria

- [ ] An authenticated portal session resolves to one authorized aggregator/environment and a server-controlled permission set.
- [ ] Cross-site mutation requests fail the CSRF policy and unapproved credentialed origins are denied.
- [ ] No operational key or reusable privileged access token is stored in localStorage or exposed to frontend logging.
- [ ] Logout, expiry and revoked membership clear sensitive in-memory/cache state and prevent subsequent mutations.
- [ ] Open redirects, session fixation and cross-aggregator cookie confusion are prevented in tested flows.

## Validation scenarios

- [ ] Run browser integration tests for login, callback replay, expired sessions, logout and membership revocation.
- [ ] Test CSRF, malicious Origin, preflight, custom-domain cookies and redirect allowlists.
- [ ] Inspect browser storage, cookie flags and network/log captures using synthetic accounts.

## Expected deliverables

- Portal BFF authentication integration.
- Browser/session security test evidence.
- Documented cookie, CSRF, CORS and redirect configuration.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved OIDC provider/client registration, callback domains and test memberships. Production identity configuration is a later gated deployment input.

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
