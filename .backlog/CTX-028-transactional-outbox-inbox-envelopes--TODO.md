---
id: "CTX-028"
title: "Deliver domain events through transactional outbox and deduplicated inbox"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "event-delivery"
depends_on: ["CTX-006", "CTX-019", "CTX-027"]
requires_one_of: []
conflict_domains: ["contracts:events", "database-schema-migrations", "platform-contract-catalog", "schema:events", "workflow:outbox"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-028: Deliver domain events through transactional outbox and deduplicated inbox

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Provisioning, payment results, configuration changes and webhook delivery require reliable asynchronous communication. A database commit followed by an unrecorded publish can lose work, and broker redelivery is normal. Implement a platform-owned event envelope and transactional outbox that commits with domain state, plus consumer inbox deduplication. Events carry public ownership identifiers, event/resource versions and safe references; they must not transport raw card data, PIN material, sensitive authentication data or connector secrets. Preserve ordering requirements per aggregate without claiming global ordered delivery or exactly-once side effects. Each consumer still validates ownership and legal state transitions. This ticket establishes delivery primitives; specialized payment dispatch and financial recovery remain governed by their own state machines.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.


## Relevant code and ownership

Primary repository/workstream: **platform / event-delivery**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/kafka.rs](../crates/router/src/services/kafka.rs)

- `Proposed: platform/events/`

- `Proposed: contracts/events/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:events`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:events`
- `workflow:outbox`

## Implementation plan

- [ ] Define versioned envelope with event_id, aggregate_id, aggregator_id, environment and causation IDs.
- [ ] Create outbox/inbox tables with uniqueness, claims and bounded retry metadata.
- [ ] Implement publication after commit and consumer deduplication in the same transaction as effects.
- [ ] Define per-aggregate ordering and poison-event/dead-letter behavior.
- [ ] Add payload allowlists and expiry rules for secure external references.
- [ ] Define RLS-compatible job/outbox discovery: poll known aggregator scopes or use a narrowly granted metadata-only discovery interface, then enter the authenticated aggregator transaction before reading tenant payloads; do not grant general workers BYPASSRLS.

## Acceptance criteria

- [ ] Committed domain changes always retain a publishable event record.
- [ ] Publisher crashes can cause redelivery without duplicate consumer state changes.
- [ ] Envelope ownership is validated before processing.
- [ ] Forbidden payment/credential content is rejected from event payloads.
- [ ] Dead-letter records preserve safe diagnostic context and replay controls.
- [ ] Workers can discover eligible work without blanket tenant-data access; a forged discovery result cannot open another aggregator payload outside a scoped transaction.

## Validation scenarios

- [ ] Crash before commit, after commit and after broker acknowledgement.
- [ ] Deliver one event repeatedly and out of order to a test consumer.
- [ ] Inject a prohibited sensitive field and verify validation rejection.

## Expected deliverables

- Outbox/inbox migrations and publisher/consumer library.
- Event envelope schema and retry contract.

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
