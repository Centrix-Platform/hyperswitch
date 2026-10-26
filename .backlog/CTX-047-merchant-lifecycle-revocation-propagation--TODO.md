---
id: "CTX-047"
title: "Propagate merchant activation suspension and terminal revocation safely"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "merchant-lifecycle"
depends_on: ["CTX-021", "CTX-024", "CTX-028", "CTX-038", "CTX-041"]
requires_one_of: []
conflict_domains: ["auth:revocation", "authentication-authorization-boundary", "config:eligibility", "configuration-publication-boundary", "workflow:merchant-lifecycle"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-047: Propagate merchant activation suspension and terminal revocation safely

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Merchant activation requires canonical approval, required acquirer enrollment and ready native projections; none alone is sufficient. Suspension or closure must prevent new sessions and payment admission across gateway instances, routing caches and terminal configuration while preserving inquiry, reversal and reconciliation of existing financial obligations. Implement a versioned lifecycle evaluator and bounded revocation propagation rather than assuming token expiry is fast enough. Distinguish merchant suspension, aggregator suspension, terminal revocation and connector disablement, including precedence and recovery rules. This ticket owns lifecycle orchestration and admission gates; it must not blindly cancel already dispatched transactions or hide unresolved outcomes. Audit who changed status and publish safe versioned events to downstream consumers and portal read models.

## Prerequisites and dependency outputs

- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.


## Relevant code and ownership

Primary repository/workstream: **platform / merchant-lifecycle**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- `Proposed: platform/merchants/lifecycle/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:revocation`
- `authentication-authorization-boundary`
- `config:eligibility`
- `configuration-publication-boundary`
- `workflow:merchant-lifecycle`

## Implementation plan

- [ ] Define activation prerequisites and precedence for aggregator/merchant/terminal/account status.
- [ ] Implement lifecycle transitions with version checks and actor authorization.
- [ ] Publish revocation/activation events and invalidate relevant caches/sessions.
- [ ] Gate new issuance/admission while permitting explicitly authorized recovery operations.
- [ ] Expose safe status reasons and propagation observability.

## Acceptance criteria

- [ ] Activation fails until every mandatory prerequisite is satisfied.
- [ ] Suspension blocks new SDK sessions and new charges within the agreed bound.
- [ ] Previously dispatched UNKNOWN operations remain recoverable.
- [ ] Stale activation events cannot overwrite newer suspension.
- [ ] Every lifecycle transition records actor, reason and resource version.

## Validation scenarios

- [ ] Suspend during concurrent token minting and charge admission.
- [ ] Deliver activation/revocation events out of order.
- [ ] Recover inquiry/reversal for a payment after merchant suspension.

## Expected deliverables

- Lifecycle eligibility evaluator and revocation consumers.
- Status propagation contract and race-condition tests.

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
