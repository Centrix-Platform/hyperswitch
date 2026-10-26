---
id: "CTX-021"
title: "Model legal merchants and their onboarding lifecycle independently of profiles"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "merchant-domain"
depends_on: ["CTX-001", "CTX-002", "CTX-019"]
requires_one_of: []
conflict_domains: ["contracts:merchant", "database-schema-migrations", "platform-contract-catalog", "schema:merchant"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-021: Model legal merchants and their onboarding lifecycle independently of profiles

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A Hyperswitch BusinessProfile carries processing configuration under a MerchantAccount, including routing and payment settings. It is not a legal merchant account, underwriting decision or KYB case. Create the canonical merchant record owned by an aggregator and model provisioning, review, approval, suspension and closure separately from its profile projection. Store references to sensitive KYB evidence rather than documents or unrestricted PII blobs in profile metadata. A merchant can exist before native provisioning or acquirer acceptance, and approval must not be inferred from profile existence. Define immutable public identity and aggregator-scoped external references so later agents can build onboarding, terminal assignment and reporting against a stable contract without adopting native naming.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / merchant-domain**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- `Proposed: platform/merchants/domain/`

- `Proposed: platform/migrations/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:merchant`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:merchant`

## Implementation plan

- [ ] Define merchant lifecycle states, permitted transitions and responsible actors.
- [ ] Create canonical merchant, legal-entity reference and lifecycle-history schema.
- [ ] Add aggregator-scoped external_reference uniqueness and optional profile mapping.
- [ ] Define safe merchant read/write DTOs and field-level sensitivity classifications.
- [ ] Implement repository operations that require aggregator context and optimistic version checks.

## Acceptance criteria

- [ ] Profile creation alone cannot set merchant processing status active.
- [ ] Two aggregators may reuse an external reference without collision.
- [ ] One aggregator cannot create duplicate external references.
- [ ] Illegal lifecycle transitions fail without modifying history.
- [ ] Canonical records contain evidence references rather than uploaded document contents.

## Validation scenarios

- [ ] Exercise the complete pending-review through activation lifecycle with synthetic data.
- [ ] Attempt concurrent conflicting lifecycle updates and assert one valid winner.
- [ ] Inspect DTOs and fixtures for native identifier or evidence-content leakage.

## Expected deliverables

- Merchant schema and lifecycle transition specification.
- Canonical merchant DTOs and scoped repository.

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
