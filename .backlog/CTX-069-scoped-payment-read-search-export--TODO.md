---
id: "CTX-069"
title: "Expose authorized payment status search and export APIs"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "payment-read-api"
depends_on: ["CTX-029", "CTX-032", "CTX-035", "CTX-038", "CTX-049", "CTX-057", "CTX-064"]
requires_one_of: []
conflict_domains: ["contracts:payment-reads", "platform-contract-catalog", "reporting:payment-export"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-069: Expose authorized payment status search and export APIs

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

SDK recovery, portal operations and aggregator servers need payment visibility through stable platform APIs rather than native payment IDs or unrestricted analytics endpoints. Implement operation/payment reads, scoped search and asynchronous exports using canonical attribution and the declared financial state owner. A merchant-limited user must receive the same restrictions in counts, pagination, bulk operations and export downloads as in individual reads. Pending and UNKNOWN results must remain explicit so clients do not infer a failed payment and start again. Use historical ownership and frozen attempt attribution after terminal reassignment or configuration changes. This ticket owns safe read contracts and authorization-preserving query execution; it does not redefine execution state or expose sensitive terminal data for debugging.

## Prerequisites and dependency outputs

- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.
- [CTX-035](CTX-035-analytics-search-report-isolation--TODO.md) - consume its completed, reviewed deliverables: Enforce aggregator and merchant scope in analytics and reporting.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-read-api**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/payments.rs](../crates/router/src/routes/payments.rs)

- [crates/analytics/src/search.rs](../crates/analytics/src/search.rs)

- `Proposed: platform/payments/reads/`

- `Proposed: contracts/public/openapi.yaml`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:payment-reads`
- `platform-contract-catalog`
- `reporting:payment-export`

## Implementation plan

- [ ] Define safe operation/payment DTOs and ownership-aware status mapping.
- [ ] Implement get/list/search with mandatory aggregator and merchant-scope predicates.
- [ ] Bind pagination tokens to authorized query/environment context.
- [ ] Implement scoped export jobs and short-lived authorized downloads.
- [ ] Document consistency/lag and pending/UNKNOWN recovery behavior.

## Acceptance criteria

- [ ] Native identifiers and sensitive payment payloads are absent from public reads.
- [ ] Foreign resource IDs return ownership-safe denial.
- [ ] Counts, pages and exports honor restricted merchant scope.
- [ ] Pagination tokens cannot be reused to change aggregator or query authority.
- [ ] UNKNOWN status remains distinguishable from failure in every read format.

## Validation scenarios

- [ ] Tamper with resource IDs, filters and pagination tokens across aggregators.
- [ ] Export as a merchant-limited analyst and inspect every record/count.
- [ ] Move a terminal and verify historical payment attribution remains unchanged.

## Expected deliverables

- Payment read/search/export API contract.
- Authorized query adapters and negative integration tests.

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
