---
id: "CTX-027"
title: "Persist authoritative payment admission and attempt ownership"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "payment-operation-store"
depends_on: ["CTX-006", "CTX-015", "CTX-019", "CTX-021"]
requires_one_of: []
conflict_domains: ["contracts:payment-state", "database-schema-migrations", "platform-contract-catalog", "schema:payment-operation"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-027: Persist authoritative payment admission and attempt ownership

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Existing native PaymentIntent and PaymentAttempt records describe execution, while Redis API locks do not provide a durable public idempotency contract. Add platform operation and attempt records that reserve one business operation and explicitly map it to the native executor. Define which component is authoritative for each field: the platform owns admission and workflow policy; the native engine owns its execution result, ingested through controlled transitions. PostgreSQL uniqueness must cover environment, aggregator, merchant, operation scope and idempotency key digest. Store request fingerprints and safe responses, not raw payment payloads. Model DISPATCHING and UNKNOWN explicitly so a lease expiry, process crash or timeout cannot be mistaken for permission to initiate a second authorization.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-operation-store**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- [crates/diesel_models/src/payment_attempt.rs](../crates/diesel_models/src/payment_attempt.rs)

- `Proposed: platform/payments/operations/`

- `Proposed: platform/migrations/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:payment-state`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:payment-operation`

## Implementation plan

- [ ] Define operation/attempt states, version fields, authority mapping and legal transitions.
- [ ] Create scoped idempotency uniqueness and immutable canonical fingerprint fields.
- [ ] Add durable dispatch references, native execution mappings and safe route snapshot references.
- [ ] Define encrypted payload-reference expiry handling without storing SAD in operations.
- [ ] Add indexes and retention/tombstone requirements preserving duplicate protection.

## Acceptance criteria

- [ ] Concurrent reservation of one scoped key produces exactly one operation.
- [ ] Different business operations can use independent idempotency scopes.
- [ ] UNKNOWN is a first-class persisted state with no implicit failure transition.
- [ ] Schema excludes clear or encrypted SAD payload columns.
- [ ] Native execution mappings cannot attach an attempt to another aggregator operation.

## Validation scenarios

- [ ] Run concurrent inserts against the unique reservation constraint.
- [ ] Try illegal ownership and transition mutations.
- [ ] Expire response-cache data and verify durable duplicate identification remains.

## Expected deliverables

- Operation/attempt migrations and state ownership matrix.
- Idempotency scope and retention specification.

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
