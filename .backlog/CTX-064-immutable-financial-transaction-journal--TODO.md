---
id: "CTX-064"
title: "Record immutable payment lifecycle and reconciliation evidence"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "transaction-journal"
depends_on: ["CTX-027", "CTX-028", "CTX-049", "CTX-057", "CTX-060", "CTX-061"]
requires_one_of: []
conflict_domains: ["contracts:financial-events", "database-schema-migrations", "platform-contract-catalog", "schema:transaction-journal"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-064: Record immutable payment lifecycle and reconciliation evidence

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The initial platform routes payments with direct acquirer settlement; it does not automatically need a customer balances ledger. It does need an immutable, attributable record of authorization, capture, refund, reversal, inquiry corrections and settlement observations. Build a transaction journal from authoritative state transitions, preserving amount/currency, ownership, original references, causation and event versions without storing raw card or sensitive authentication data. Corrections append new evidence rather than rewriting past facts. Journal publication must follow the same database transaction/outbox boundary as the corresponding state change, with deduplication and reconciliation completeness checks. This ticket excludes balances, reserves, fees and payouts; adding those later requires a separate double-entry accounting domain and explicit funds-flow decisions.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.


## Relevant code and ownership

Primary repository/workstream: **platform / transaction-journal**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- [crates/diesel_models/src/payment_attempt.rs](../crates/diesel_models/src/payment_attempt.rs)

- [crates/diesel_models/src/refund.rs](../crates/diesel_models/src/refund.rs)

- `Proposed: platform/financial_journal/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:financial-events`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:transaction-journal`

## Implementation plan

- [ ] Define immutable journal event types and authoritative source mappings.
- [ ] Create append-only journal storage with event/operation uniqueness.
- [ ] Write safe financial facts atomically with state changes or through validated idempotent ingestion.
- [ ] Implement correction/supersession records and restricted audit access.
- [ ] Add completeness checks between operations, attempts and journal entries.

## Acceptance criteria

- [ ] Each authoritative financial transition has one attributable journal fact.
- [ ] Duplicate event delivery cannot duplicate financial facts.
- [ ] Corrections preserve the original entry and causation chain.
- [ ] Journal records contain no raw card, PIN or SAD payloads.
- [ ] No balances or settlement entitlement are inferred without a separate accounting model.

## Validation scenarios

- [ ] Replay transition events and check journal uniqueness.
- [ ] Correct an inquiry result and inspect appended history.
- [ ] Compare operation/attempt counts and totals to journal completeness checks.

## Expected deliverables

- Append-only journal schema and writer.
- Financial event taxonomy and completeness queries.

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
