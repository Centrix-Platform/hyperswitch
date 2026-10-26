---
id: "CTX-038"
title: "Enforce permissions ownership and bounded role delegation"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "authorization"
depends_on: ["CTX-022", "CTX-029"]
requires_one_of: []
conflict_domains: ["auth:policy-enforcement", "auth:role-cache", "authentication-authorization-boundary", "contracts:permissions", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-038: Enforce permissions ownership and bounded role delegation

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A valid session proves identity but does not authorize every action under its aggregator. Implement server-side permission checks combined with resource ownership and any restricted merchant set. Native role information and cache helpers exist, but platform permissions must cover onboarding, terminals, routing, keys, refunds, exports and invitations consistently. A role editor cannot grant authority it does not possess, invitation acceptance cannot substitute a different aggregator, and cached grants must respect revocation versions. Apply policy to direct reads, mutations, lists, exports and asynchronous requests, not only visible portal controls. This ticket owns the authorization evaluator and endpoint integration pattern. Native administrator or platform-role shortcuts must not accidentally broaden an ordinary aggregator session.

## Prerequisites and dependency outputs

- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.


## Relevant code and ownership

Primary repository/workstream: **platform / authorization**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authorization.rs](../crates/router/src/services/authorization.rs)

- [crates/router/src/services/authorization/permissions.rs](../crates/router/src/services/authorization/permissions.rs)

- [crates/router/src/core/user_role.rs](../crates/router/src/core/user_role.rs)

- `Proposed: platform/identity/policy/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:policy-enforcement`
- `auth:role-cache`
- `authentication-authorization-boundary`
- `contracts:permissions`
- `platform-contract-catalog`

## Implementation plan

- [ ] Implement permission/ownership evaluator consuming immutable trusted context.
- [ ] Define endpoint policy matrix and bounded merchant-set evaluation.
- [ ] Add invitation issuance/acceptance and role-edit anti-escalation rules.
- [ ] Version authorization caches and invalidate membership/role changes.
- [ ] Integrate policy middleware and negative tests for the initial onboarding/payment/terminal APIs.

## Acceptance criteria

- [ ] Permission plus ownership is required for every protected endpoint.
- [ ] Users cannot delegate permissions or merchant scope they do not hold.
- [ ] Invitation acceptance is bound to intended identity and aggregator.
- [ ] List/export authorization equals individual-resource authorization.
- [ ] Revoked or stale cached grants are denied within the documented bound.

## Validation scenarios

- [ ] Run a default-role by endpoint authorization matrix.
- [ ] Attempt self-escalation, foreign invitations and merchant-subset bypass.
- [ ] Revoke a cached role and retry synchronous and queued actions.

## Expected deliverables

- Authorization policy engine and endpoint matrix.
- Invitation/role contracts and adversarial tests.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

Inputs are the actual source checkout, completed prerequisite deliverables and any explicitly required decisions above.

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
