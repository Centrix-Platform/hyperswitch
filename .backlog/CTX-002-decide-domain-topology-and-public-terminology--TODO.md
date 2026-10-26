---
id: "CTX-002"
title: "Decide the native account topology and public domain terminology"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "architecture"
depends_on: ["CTX-001", "CTX-003"]
requires_one_of: []
conflict_domains: ["architecture-domain-model", "platform-contract-catalog", "public-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-002: Decide the native account topology and public domain terminology

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The proposed public mapping is Platform -> Aggregator -> Merchant -> Terminal. The initial native mapping uses a MerchantAccount for an aggregator and a BusinessProfile for its merchant, with a separate canonical legal-merchant registry. BusinessProfile does not supply independent legal onboarding or automatic customer/vault isolation: the inspected v1 customer and payment-method models are merchant-account scoped. Hyperswitch also contains Platform/Connected account support with organization constraints. Compare these options against actual first-release requirements and choose one executable topology; do not implement incompatible branches simultaneously. An infrastructure Tenant is a storage/configuration partition and is distinct from a platform super-admin identity. This decision gates schema mappings, credentials, reporting and later migrations.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **platform / architecture**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_interfaces/src/configs.rs](../crates/hyperswitch_interfaces/src/configs.rs)

- [crates/diesel_models/src/merchant_account.rs](../crates/diesel_models/src/merchant_account.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- [crates/diesel_models/src/customers.rs](../crates/diesel_models/src/customers.rs)

- [crates/diesel_models/src/payment_method.rs](../crates/diesel_models/src/payment_method.rs)

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: docs/architecture/domain-topology.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `architecture-domain-model`
- `platform-contract-catalog`
- `public-contracts`

## Implementation plan

- [ ] Inventory native Tenant, Organization, MerchantAccount, Profile, MCA, customer and payment-method ownership in the pinned feature baseline.
- [ ] Compare profile-backed canonical merchants against Platform/Connected accounts for credentials, vault, reporting and lifecycle requirements.
- [ ] Choose a default topology with a migration path, and identify features that remain unavailable until their merchant ownership overlay exists.
- [ ] Define canonical/public IDs, internal native references and translation errors without bulk renaming native tables or connector DTOs.
- [ ] Publish invariants and bind schema/API tickets to the selected topology.

## Acceptance criteria

- [ ] One ADR records the chosen topology, evidence and rejected alternatives.
- [ ] The mapping distinguishes infrastructure tenancy, administrative authority and legal merchant identity.
- [ ] Customer, stored-card and mandate isolation requirements have explicit owners and enforcement points.
- [ ] The external API never requires customers to interpret an aggregator as a native merchant.
- [ ] CTX-033 applicability is resolved without silently enabling cross-merchant vault access.

## Validation scenarios

- [ ] Trace one aggregator with two merchants and prove ownership for payment, customer, vault, credential and report reads.
- [ ] Check native same-organization constraints against the proposed organization layout.
- [ ] Review the mapping against both current schema feature sets while implementing only the chosen baseline.

## Expected deliverables

- Domain topology ADR
- Canonical/native identifier mapping
- Feature eligibility and migration decision table

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
