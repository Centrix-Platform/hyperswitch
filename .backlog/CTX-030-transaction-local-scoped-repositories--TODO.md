---
id: "CTX-030"
title: "Enforce transaction-local tenancy in scoped storage and pool APIs"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "scoped-storage"
depends_on: ["CTX-015", "CTX-019", "CTX-029"]
requires_one_of: []
conflict_domains: ["storage:pools", "storage:scoped-repositories", "tenancy-storage-boundary"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-030: Enforce transaction-local tenancy in scoped storage and pool APIs

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The current connection helpers lease master or replica connections and attach request correlation context, but they do not establish your new aggregator scope. Pool-checkout session state alone is unsafe because pooled connections are reused, transactions roll back, and different read/account pools exist. Introduce a required scoped unit-of-work API that begins a transaction, sets trusted transaction-local context before tenant-owned SQL and exposes scoped repositories rather than a raw pool. Include both canonical and native-account context when required by policies. No network side effect should be held inside that transaction. Keep separately authorized platform/global lookups explicit, and document replica behavior and transaction-pool compatibility. This ticket establishes the storage seam used by later RLS policies and migration work.

## Prerequisites and dependency outputs

- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.


## Relevant code and ownership

Primary repository/workstream: **core / scoped-storage**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/storage_impl/src/connection.rs](../crates/storage_impl/src/connection.rs)

- [crates/storage_impl/src/database/store.rs](../crates/storage_impl/src/database/store.rs)

- [crates/storage_impl/src/utils.rs](../crates/storage_impl/src/utils.rs)

- `Proposed: platform/storage/scoped_transaction/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `storage:pools`
- `storage:scoped-repositories`
- `tenancy-storage-boundary`

## Implementation plan

- [ ] Inventory payment, account, replica and worker connection entry points.
- [ ] Implement with_aggregator_transaction using transaction-local set_config and typed context.
- [ ] Expose scoped connection/repository handles that cannot escape transaction lifetime.
- [ ] Replace tenant-owned connection acquisition paths in the first vertical slice.
- [ ] Create explicit privileged/global lookup APIs with separate runtime grants.
- [ ] Define RLS-compatible job/outbox discovery: poll known aggregator scopes or use a narrowly granted metadata-only discovery interface, then enter the authenticated aggregator transaction before reading tenant payloads; do not grant general workers BYPASSRLS.
- [ ] Provide a bounded pre-authentication key/mapping lookup with dedicated least-privilege grants and rate-limited opaque lookup identifiers; return only verifier/owner metadata needed to establish trusted context, then use scoped repositories for tenant data.

## Acceptance criteria

- [ ] Every tenant query in the slice runs after trusted scope initialization.
- [ ] Commit, rollback and cancellation cannot leak scope into the next borrower.
- [ ] Account and replica paths have documented equivalent scoping.
- [ ] Tenant repository APIs cannot accept arbitrary aggregator overrides.
- [ ] External connector calls run outside open database transactions.
- [ ] Workers can discover eligible work without blanket tenant-data access; a forged discovery result cannot open another aggregator payload outside a scoped transaction.
- [ ] Opaque-key authentication can establish aggregator context without circular RLS requirements, and its bootstrap interface cannot list or retrieve unrelated tenant resources.

## Validation scenarios

- [ ] Reuse a one-connection pool for alternating aggregators after success and failure.
- [ ] Cancel a scoped operation mid-transaction and inspect the next borrower.
- [ ] Run under transaction-pooling configuration and test fail-closed missing context.

## Expected deliverables

- Scoped transaction/repository library and migrated vertical slice.
- Pool entry-point inventory and transaction-lifetime guide.

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
