---
id: "CTX-042"
title: "Validate device proof transaction integrity and replay limits"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "sdk-request-validation"
depends_on: ["CTX-014", "CTX-029", "CTX-034", "CTX-041"]
requires_one_of: []
conflict_domains: ["auth:device-proof", "auth:replay-store", "authentication-authorization-boundary", "contracts:payment-integrity", "platform-contract-catalog"]
external_inputs: ["Approved sender-constrained proof and transaction-envelope protocol"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-042: Validate device proof transaction integrity and replay limits

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A short-lived bearer token can still be stolen, replayed or used with a modified transaction body. Validate a standard sender-constrained proof design where appropriate, including audience, method, target URI, freshness, unique proof identifier and device-key binding. DPoP alone does not authenticate the complete payment body, so separately specify how immutable amount, currency, payment session, operation and secure payload reference are bound to the transaction. Use vetted cryptographic libraries and published test vectors rather than a proprietary signature format. Replay protection is scoped and bounded, while durable business idempotency remains PostgreSQL-backed. This ticket validates mobile requests before admission; it cannot establish terminal payment certification or turn an untrusted terminal ID into hardware identity.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.


## Relevant code and ownership

Primary repository/workstream: **platform / sdk-request-validation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: platform/identity/device_proof/`

- `Proposed: contracts/payment-integrity/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:device-proof`
- `auth:replay-store`
- `authentication-authorization-boundary`
- `contracts:payment-integrity`
- `platform-contract-catalog`

## Implementation plan

- [ ] Finalize proof and canonical transaction-integrity contract with security review.
- [ ] Implement signature, claim, URI/method, device thumbprint and body-binding checks.
- [ ] Add scoped nonce/proof replay store and explicit clock-skew policy.
- [ ] Integrate key revocation, session constraints and configuration-version checks.
- [ ] Publish cross-language positive/negative test vectors for SDK implementers.

## Acceptance criteria

- [ ] Changing amount, currency or payload reference invalidates transaction integrity.
- [ ] Proof for one URI/method/device cannot authorize another.
- [ ] Expired, repeated and revoked proofs are rejected according to policy.
- [ ] Redis replay-store failure follows an explicit safe availability policy.
- [ ] Business idempotency remains independent from proof uniqueness.

## Validation scenarios

- [ ] Run tampering, URI normalization, duplicate proof and clock-skew vectors.
- [ ] Retry the same business operation using a fresh valid proof.
- [ ] Simulate replay-store outage and device-key revocation.

## Expected deliverables

- Proof/integrity validator and replay-store adapter.
- Language-neutral signed-request vectors and protocol specification.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved sender-constrained proof and transaction-envelope protocol

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
