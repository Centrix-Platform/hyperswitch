---
id: "CTX-065"
title: "Import acquirer settlement evidence and reconcile transaction outcomes"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "settlement-reconciliation"
depends_on: ["CTX-013", "CTX-028", "CTX-056", "CTX-057", "CTX-064"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "schema:reconciliation", "workflow:settlement-import"]
external_inputs: ["Pilot acquirer settlement format/API, business-day cutoffs and matching rules"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-065: Import acquirer settlement evidence and reconcile transaction outcomes

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Direct settlement to aggregators or their merchants does not remove the gateway's need to reconcile what it authorized, captured, refunded and reversed against acquirer records. Implement a pilot settlement import adapter and normalized reconciliation model keyed by owned account, external references, amount, currency and settlement period. Files or APIs may contain sensitive fields; allowlist normalized safe evidence and secure source access separately. Detect missing, duplicate, mismatched and late records without automatically creating compensating financial operations. Reconciliation can resolve UNKNOWN only through the agreed authoritative evidence and audited transition policy. This ticket produces operational matching and exceptions, not merchant balances, payout instructions or a full accounting ledger. Preserve provenance and idempotency for repeated source imports.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / settlement-reconciliation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/payment_attempt.rs](../crates/diesel_models/src/payment_attempt.rs)

- `Proposed: platform/reconciliation/`

- `Proposed: contracts/settlement-record.schema.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `schema:reconciliation`
- `workflow:settlement-import`

## Implementation plan

- [ ] Define pilot settlement source contract and normalized safe record schema.
- [ ] Implement authenticated import, source deduplication and immutable provenance.
- [ ] Match journal/attempt references using documented amount/date/tolerance rules.
- [ ] Create scoped exception workflow and approved UNKNOWN resolution evidence.
- [ ] Expose reconciliation age, unmatched counts and safe operator drill-down.

## Acceptance criteria

- [ ] Reimporting identical source evidence does not duplicate settlement records.
- [ ] Cross-account/aggregator records cannot match another owner payment.
- [ ] Amount/currency mismatches create exceptions rather than silent acceptance.
- [ ] UNKNOWN resolution retains source evidence and actor/policy attribution.
- [ ] No automatic refund/reversal/payout occurs merely because matching fails.

## Validation scenarios

- [ ] Import duplicate, late, missing and deliberately mismatched synthetic records.
- [ ] Reconcile an approved-but-response-lost transaction.
- [ ] Attempt source-reference collisions across two aggregators/accounts.

## Expected deliverables

- Settlement adapter and reconciliation workflow.
- Matching rules, exception contract and pilot fixtures.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot acquirer settlement format/API, business-day cutoffs and matching rules

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
