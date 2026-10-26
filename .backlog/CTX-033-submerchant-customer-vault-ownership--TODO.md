---
id: "CTX-033"
title: "Isolate submerchant customer vault and mandate access or reject those features"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "stored-payment-isolation"
depends_on: ["CTX-002", "CTX-021", "CTX-032"]
requires_one_of: []
conflict_domains: ["contracts:stored-payments", "database-schema-migrations", "native:vault-access", "platform-contract-catalog", "schema:customer-ownership"]
external_inputs: []
external_inputs_resolved: true
applicability: "topology-dependent"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-033: Isolate submerchant customer vault and mandate access or reject those features

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

In this v1 topology, many legal merchants map to BusinessProfiles inside one aggregator MerchantAccount. Native customers, stored payment methods and mandates are not automatically isolated by that profile boundary. Before exposing any saved-payment feature, select an explicit policy: implement a canonical merchant ownership overlay at every access path, migrate to a topology with adequate native boundaries, or reject unsupported features. This ticket is topology-dependent but its decision is mandatory before feature enablement. Token secrecy alone is not authorization, and cloning a native customer ID into metadata is not enforcement. Cover lookup, update, deletion, customer sessions, recurring charges, exports and vault callbacks. Do not implement cross-merchant sharing unless separately specified and authorized.

## Prerequisites and dependency outputs

- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **core / stored-payment-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/customers.rs](../crates/diesel_models/src/customers.rs)

- [crates/diesel_models/src/payment_method.rs](../crates/diesel_models/src/payment_method.rs)

- [crates/diesel_models/src/mandate.rs](../crates/diesel_models/src/mandate.rs)

- [crates/diesel_models/src/ephemeral_key.rs](../crates/diesel_models/src/ephemeral_key.rs)

- [crates/router/src/core/payment_methods/vault.rs](../crates/router/src/core/payment_methods/vault.rs)


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:stored-payments`
- `database-schema-migrations`
- `native:vault-access`
- `platform-contract-catalog`
- `schema:customer-ownership`

## Implementation plan

- [ ] Inventory customer, payment-method, mandate and ephemeral-key access under the selected topology.
- [ ] Document supported feature policy and choose overlay, native-account isolation or explicit rejection.
- [ ] If overlay is chosen, add immutable merchant ownership mappings and enforce them at every boundary.
- [ ] Constrain recurring-payment and vault callback attribution to the original legal merchant.
- [ ] Add production feature gates for paths without demonstrated ownership enforcement.

## Acceptance criteria

- [ ] No stored-payment feature is enabled solely because a profile exists.
- [ ] Merchant B cannot use Merchant A customer, payment method, mandate or session.
- [ ] Unknown ownership fails closed, including callbacks and background jobs.
- [ ] Unsupported features return a documented stable error.
- [ ] Topology decision and migration implications are recorded before enablement.

## Validation scenarios

- [ ] Attempt cross-profile reuse of customer/payment-method/mandate identifiers.
- [ ] Exercise delete/export/recurring paths and cache hits.
- [ ] Run feature-disabled tests proving no downstream vault call occurs.

## Expected deliverables

- Stored-payment ownership ADR and feature support matrix.
- Ownership overlay or explicit feature-rejection implementation.

## External inputs and applicability

Applicability: **topology-dependent**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

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
