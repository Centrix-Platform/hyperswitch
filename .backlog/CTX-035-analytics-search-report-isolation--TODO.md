---
id: "CTX-035"
title: "Enforce aggregator and merchant scope in analytics and reporting"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "analytics-isolation"
depends_on: ["CTX-029", "CTX-032", "CTX-034"]
requires_one_of: []
conflict_domains: ["analytics:tenant-scope", "contracts:reporting", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-035: Enforce aggregator and merchant scope in analytics and reporting

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Hyperswitch infrastructure tenancy selects a ClickHouse database, but one such database may contain many aggregator MerchantAccounts. Payment reporting, search, metrics and exports therefore need an additional trusted aggregator boundary and, for restricted users, a merchant subset. A filtered dashboard is insufficient if its analytics API, generated query, cached result or export worker can omit the predicate. Trace attribution from native ingestion through read models so public merchant IDs map consistently without exposing native IDs. This ticket supplies isolation and query authorization rather than a complete business reporting product. Handle delayed events and reassigned terminals using historical payment ownership, not current terminal assignment. Privileged platform analytics must use a separate audited path.

## Prerequisites and dependency outputs

- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.


## Relevant code and ownership

Primary repository/workstream: **core / analytics-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/analytics/src/payments.rs](../crates/analytics/src/payments.rs)

- [crates/analytics/src/search.rs](../crates/analytics/src/search.rs)

- [crates/analytics/src/payment_intents/filters.rs](../crates/analytics/src/payment_intents/filters.rs)

- `Proposed: platform/reporting/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `analytics:tenant-scope`
- `contracts:reporting`
- `platform-contract-catalog`

## Implementation plan

- [ ] Inventory ClickHouse/search/report data sources and ownership columns.
- [ ] Propagate canonical attribution through sanitized ingestion/read-model adapters.
- [ ] Require trusted scope in query builders, cached results and export jobs.
- [ ] Apply merchant-subset authorization to pagination, aggregates and download URLs.
- [ ] Separate platform-wide analytics privileges and document ingestion lag.

## Acceptance criteria

- [ ] Every exposed aggregate and search result is limited to authorized ownership.
- [ ] Exports retain requester scope through execution and download.
- [ ] Terminal reassignment does not change historical report attribution.
- [ ] Raw query parameters cannot remove mandatory scope predicates.
- [ ] Global analytics requires explicit platform authority.

## Validation scenarios

- [ ] Compare same query across two aggregators with overlapping references.
- [ ] Tamper with filters, pagination tokens and export job IDs.
- [ ] Replay delayed events after terminal reassignment and verify ownership.

## Expected deliverables

- Analytics isolation adapters and coverage matrix.
- Scoped export/query contracts and negative tests.

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
