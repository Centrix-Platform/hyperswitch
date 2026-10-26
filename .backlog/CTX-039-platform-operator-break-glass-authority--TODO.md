---
id: "CTX-039"
title: "Separate platform operator access and audited emergency authority"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "operator-access"
depends_on: ["CTX-014", "CTX-022", "CTX-029", "CTX-037", "CTX-038"]
requires_one_of: []
conflict_domains: ["auth:platform-operator", "authentication-authorization-boundary", "operations:break-glass"]
external_inputs: ["Approved operator access and emergency approval policy"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-039: Separate platform operator access and audited emergency authority

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Infrastructure Tenant configuration and native platform account features must not be confused with a super-admin login. Build a distinct operator authority domain for provisioning, cross-aggregator diagnostics and emergency controls. Platform master credentials are service/operator credentials with narrowly assigned capabilities, not universal tokens reused by portals or SDKs. Cross-aggregator access must be explicit, time-bounded where appropriate and attributable to an operator or automation identity. Define break-glass activation, approval policy, expiry and review evidence according to your operational needs without making ordinary troubleshooting depend on blanket database bypass. This ticket excludes normal aggregator sessions and does not create an unlogged impersonation path. Emergency payment disablement must remain possible without decrypting payment or acquirer secrets.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-037](CTX-037-oidc-portal-bff-session-authentication--TODO.md) - consume its completed, reviewed deliverables: Implement OIDC portal sessions and explicit aggregator context switching.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.


## Relevant code and ownership

Primary repository/workstream: **platform / operator-access**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: platform/operators/`

- `Proposed: platform/operations/break-glass/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:platform-operator`
- `authentication-authorization-boundary`
- `operations:break-glass`

## Implementation plan

- [ ] Define operator roles and distinct token audience/session endpoints.
- [ ] Implement explicit targeted aggregator context for privileged operations.
- [ ] Add audited break-glass issuance, expiry and revocation workflow.
- [ ] Separate master automation credential storage and network access.
- [ ] Provide emergency disable controls and safe read-only diagnostic access.

## Acceptance criteria

- [ ] Aggregator credentials cannot authenticate to operator endpoints.
- [ ] Every cross-aggregator operation records actor, target, purpose and result.
- [ ] Break-glass authority expires and is individually revocable.
- [ ] Master credentials are absent from browser/SDK configuration.
- [ ] Emergency disable does not require raw payment data or credential disclosure.

## Validation scenarios

- [ ] Attempt operator routes with valid aggregator sessions and keys.
- [ ] Exercise break-glass expiry and revoked operator membership.
- [ ] Audit a cross-aggregator diagnostic operation end to end.

## Expected deliverables

- Operator authority implementation and audit events.
- Break-glass and master-credential operational runbook.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved operator access and emergency approval policy

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
