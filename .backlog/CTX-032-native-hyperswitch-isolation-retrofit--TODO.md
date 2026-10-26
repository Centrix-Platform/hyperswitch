---
id: "CTX-032"
title: "Audit and enforce isolation across native payment and account storage"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "native-data-isolation"
depends_on: ["CTX-018", "CTX-030", "CTX-031"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "schema:native-rls", "storage:kv-safety", "storage:native-repositories"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-032: Audit and enforce isolation across native payment and account storage

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Protecting the platform registry does not protect native PaymentIntent, PaymentAttempt, refund, customer, mandate or account tables. Inventory every exposed execution and read path for the selected feature set, identify its native merchant/profile ownership columns and enforce the resolved MerchantAccount boundary. Profile-level merchant isolation requires additional ownership checks where the native schema lacks that boundary. The payment store supports PostgreSQL and RedisKv paths; PostgreSQL policies cannot protect Redis-only results or a drainer that writes under broad authority. Default critical admission and persistence to authoritative PostgreSQL for the first slice, and disable unreviewed KV paths. Avoid blanket schema edits that assume v1 and v2 have identical columns or silently break existing native administration workflows.

## Prerequisites and dependency outputs

- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.
- [CTX-030](CTX-030-transaction-local-scoped-repositories--TODO.md) - consume its completed, reviewed deliverables: Enforce transaction-local tenancy in scoped storage and pool APIs.
- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **core / native-data-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/storage_impl/src/payments/payment_intent.rs](../crates/storage_impl/src/payments/payment_intent.rs)

- [crates/storage_impl/src/payments/payment_attempt.rs](../crates/storage_impl/src/payments/payment_attempt.rs)

- [crates/storage_impl/src/kv_router_store.rs](../crates/storage_impl/src/kv_router_store.rs)

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- [crates/diesel_models/src/customers.rs](../crates/diesel_models/src/customers.rs)


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `schema:native-rls`
- `storage:kv-safety`
- `storage:native-repositories`

## Implementation plan

- [ ] Build table/query/cache coverage matrix for the pinned feature configuration.
- [ ] Add native account isolation policies or equivalent scoped adapters with explicit justified exceptions.
- [ ] Retrofit writes, joins, list queries and account-pool access to trusted ownership context.
- [ ] Gate RedisKv and drainer paths until equivalent isolation is demonstrated.
- [ ] Keep native admin/migration roles private and separately authorized.

## Acceptance criteria

- [ ] Every exposed native resource has a documented isolation owner and enforcement point.
- [ ] Another aggregator account cannot be read or mutated through native-backed APIs.
- [ ] Profile scoping is not claimed for customer/vault data without an overlay.
- [ ] Unreviewed RedisKv execution paths cannot be enabled in production configuration.
- [ ] Pinned native payment compatibility flow still passes with runtime roles.

## Validation scenarios

- [ ] Run native-backed charge/read/refund/list flows with two aggregators.
- [ ] Attempt cache-hit and drainer bypass scenarios.
- [ ] Compile/test supported feature combinations affected by schema and storage changes.

## Expected deliverables

- Native isolation coverage matrix and retrofit migrations/adapters.
- Storage-scheme safety gate and regression suite.

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
