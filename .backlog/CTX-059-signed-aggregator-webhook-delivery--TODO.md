---
id: "CTX-059"
title: "Deliver signed versioned aggregator webhooks with safe retries"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "aggregator-webhooks"
depends_on: ["CTX-028", "CTX-034", "CTX-038", "CTX-043", "CTX-057"]
requires_one_of: []
conflict_domains: ["contracts:outbound-webhooks", "platform-contract-catalog", "workflow:webhook-delivery"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-059: Deliver signed versioned aggregator webhooks with safe retries

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators need asynchronous onboarding, payment and terminal lifecycle results without depending on a mobile process remaining alive. Deliver platform-owned events through a durable outbound webhook service with per-aggregator endpoint ownership, signing-key versions, event IDs and resource versions. Delivery is at least once and may be reordered; consumers must be able to deduplicate and fetch current resource state. Use bounded retry/backoff, dead-letter inspection and controlled replay rather than mutating payment truth when delivery fails. Endpoint registration needs URL validation and SSRF controls because aggregator-selected destinations are untrusted input. Keep card data, sensitive authentication data, native IDs and operational credentials out of payloads. Signing rotation and replay behavior must be explicitly documented and tested.

## Prerequisites and dependency outputs

- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.


## Relevant code and ownership

Primary repository/workstream: **platform / aggregator-webhooks**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/webhooks/outgoing.rs](../crates/router/src/core/webhooks/outgoing.rs)

- [crates/api_models/src/webhooks.rs](../crates/api_models/src/webhooks.rs)

- `Proposed: platform/webhooks/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:outbound-webhooks`
- `platform-contract-catalog`
- `workflow:webhook-delivery`

## Implementation plan

- [ ] Define event schema, signing canonicalization, timestamp tolerance and key discovery.
- [ ] Implement authorized endpoint registration and network destination/redirect controls.
- [ ] Create durable delivery attempts, bounded retries and dead-letter/replay tooling.
- [ ] Support overlap key rotation and per-endpoint disablement.
- [ ] Publish receiver examples and event/resource-version deduplication guidance.

## Acceptance criteria

- [ ] Each delivery is authenticated with a versioned signing key and event ID.
- [ ] Retries preserve event identity and do not repeat financial effects.
- [ ] Foreign aggregator endpoints/events cannot be read or replayed.
- [ ] Unsafe internal destinations and redirect bypasses are rejected.
- [ ] Payloads contain public IDs and safe business outcome fields only.

## Validation scenarios

- [ ] Fail receiver repeatedly then recover and verify duplicate event identity.
- [ ] Rotate signing keys while deliveries remain queued.
- [ ] Test SSRF/redirect inputs and reordered receiver consumption.

## Expected deliverables

- Webhook delivery service and public event/signing contract.
- Receiver fixtures and retry/replay runbook.

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
