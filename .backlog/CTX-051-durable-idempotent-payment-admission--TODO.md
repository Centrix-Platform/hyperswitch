---
id: "CTX-051"
title: "Reserve charges durably and replay equivalent operations safely"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "payment-idempotency"
depends_on: ["CTX-027", "CTX-029", "CTX-038", "CTX-042", "CTX-049", "CTX-050"]
requires_one_of: []
conflict_domains: ["contracts:idempotency", "database-schema-migrations", "payment-execution-state-boundary", "payment:admission", "platform-contract-catalog", "schema:payment-operation"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-051: Reserve charges durably and replay equivalent operations safely

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Redis coordination cannot be the final authority for whether a payment operation already exists. Implement durable PostgreSQL admission using the scoped unique key and canonical request fingerprint, after authentication and authorization. Scope keys by environment, aggregator, merchant and operation target/type; do not include the caller key identity. Equivalent retries return the existing safe result or operation reference, and changed business fields return a conflict. Define how randomized encryption is handled: retries reuse an immutable secure payload reference or a validated stable payload identity rather than treating fresh ciphertext as a new operation. Admission must survive Redis loss and preserve UNKNOWN outcomes. Response retention and duplicate-protection retention are separate policies, with stale payload references handled safely.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-idempotency**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- [crates/storage_impl/src/payments/payment_intent.rs](../crates/storage_impl/src/payments/payment_intent.rs)

- `Proposed: platform/payments/admission/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:idempotency`
- `database-schema-migrations`
- `payment-execution-state-boundary`
- `payment:admission`
- `platform-contract-catalog`
- `schema:payment-operation`

## Implementation plan

- [ ] Define canonical fingerprint algorithm/version and stable encrypted-payload identity rules.
- [ ] Implement short transactional insert-or-load under unique idempotency scope.
- [ ] Return completed safe replay, pending operation or explicit fingerprint conflict.
- [ ] Persist dispatch identity before exposing admitted status.
- [ ] Separate response-cache retention from durable tombstone/duplicate-protection retention.

## Acceptance criteria

- [ ] Concurrent equivalent requests admit one business operation.
- [ ] Changed immutable fields under the same key return 409.
- [ ] Key rotation and Redis flush do not permit duplicate admission.
- [ ] UNKNOWN replays return the original operation without dispatching a new charge.
- [ ] Canonical fingerprint vectors match across supported SDK/server implementations.

## Validation scenarios

- [ ] Run high-concurrency same-key and changed-body requests.
- [ ] Flush Redis and rotate operational keys between retries.
- [ ] Replay randomized-envelope requests using the approved stable identity contract.

## Expected deliverables

- Durable admission service and idempotency API semantics.
- Fingerprint vectors and concurrency tests.

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
