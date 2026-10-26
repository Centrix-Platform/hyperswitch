---
id: "CTX-119"
title: "Build reconciliation reports and tenant-safe exports"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Reporting and reconciliation UI"
depends_on: ["CTX-035", "CTX-064", "CTX-065", "CTX-069", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-reports", "export-storage", "tenant-read-models"]
external_inputs: ["Representative sanitized acquirer settlement files and approved report/retention definitions."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-119: Build reconciliation reports and tenant-safe exports

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators need payment and settlement visibility across their merchants without gaining access to other aggregators or treating analytics as transactional truth. The native stack includes separate analytics paths, so PostgreSQL RLS alone does not secure report datasets, caches or generated files. This ticket joins the already scoped read/export backend to portal reconciliation views, with clear data freshness, matching status and currency semantics. CSV generation should be asynchronous for large results and must defend against spreadsheet formula injection. File links, notifications and download tokens remain bound to the requesting aggregator and permitted merchant scope. Direct acquirer settlement does not imply the platform maintains a custodial balance; label journal, gross/net settlement and unmatched records accurately.

## Prerequisites and dependency outputs

- [CTX-035](CTX-035-analytics-search-report-isolation--TODO.md) - consume its completed, reviewed deliverables: Enforce aggregator and merchant scope in analytics and reporting.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Reporting and reconciliation UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/api_models/src/analytics/payment_intents.rs](../crates/api_models/src/analytics/payment_intents.rs)

- [crates/analytics/src/payments/metrics/debit_routing.rs](../crates/analytics/src/payments/metrics/debit_routing.rs)

- [crates/router/src/routes.rs](../crates/router/src/routes.rs)

- `Proposed: services/reporting/src/exports/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-reports`
- `export-storage`
- `tenant-read-models`

## Implementation plan

- [ ] Build scoped payment/merchant/terminal and settlement matching reports using approved aggregate/read APIs and timezone/currency conventions.
- [ ] Show data watermark, reconciliation status, unmatched records and exception workflow links without inventing platform balances.
- [ ] Implement asynchronous export create/status/download through scoped jobs and private object storage.
- [ ] Apply export column allowlists, masking, spreadsheet-formula neutralization and explicit currency/minor-unit formatting.
- [ ] Bind export artifacts and notifications to aggregator, environment, requester capabilities, expiry and current authorization.
- [ ] Add pagination/limits and accessible empty/error/stale-data states for analytics lag or partial ingestion.

## Acceptance criteria

- [ ] Report and export results contain only authorized aggregator/merchant data, including analytics-backed paths.
- [ ] Exports use private storage and access-controlled, expiring delivery with no public predictable object URLs.
- [ ] Formula-like cell input cannot execute as a spreadsheet formula in the documented export format.
- [ ] Reports show currency and data freshness and do not sum incompatible currencies silently.
- [ ] Settlement exceptions can be traced to journal/payment references and are distinct from custodial balances.
- [ ] Revoked access prevents subsequent export retrieval according to the documented policy.

## Validation scenarios

- [ ] Run report/export negative tests using colliding merchant references across two aggregators.
- [ ] Inspect object ACLs, signed-link expiry, stale authorization and job notification routing.
- [ ] Verify large export pagination/completeness, currency totals and formula-injection fixtures.

## Expected deliverables

- Reconciliation/reporting portal and export workflow.
- Export safety and ownership tests.
- Metric definitions and data-freshness documentation.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Representative sanitized acquirer settlement files and approved report/retention definitions.

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
