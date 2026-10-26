---
id: "CTX-026"
title: "Model device deployments and merchant-specific processing bindings"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "terminal-registry"
depends_on: ["CTX-021", "CTX-023", "CTX-025"]
requires_one_of: []
conflict_domains: ["contracts:terminal", "database-schema-migrations", "platform-contract-catalog", "schema:terminal"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-026: Model device deployments and merchant-specific processing bindings

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Terminals require their own identity and lifecycle rather than being represented as credentials inside an MCA. A logical deployment belongs to one aggregator and merchant, is backed by enrolled device keys and an approved application identity, and may have several eligible processing bindings. Each binding references a merchant-specific connector projection, acquirer MID/TID, certification bundle, encryption domain and immutable version. Preserve assignment history so moving a physical device cannot reattribute past payments. This ticket owns relational integrity and metadata only; enrollment protocols and routing behavior are separate work. Prevent cross-merchant and cross-aggregator links with composite constraints, and treat serial numbers or claimed terminal IDs as descriptive attributes rather than authentication proof.

## Prerequisites and dependency outputs

- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / terminal-registry**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- `Proposed: platform/terminals/registry/`

- `Proposed: platform/migrations/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:terminal`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:terminal`

## Implementation plan

- [ ] Create terminal deployment, device identity and assignment-history tables.
- [ ] Create versioned terminal bindings with merchant/profile connector ownership constraints.
- [ ] Represent activation, suspension, revocation and reassignment without rewriting history.
- [ ] Add uniqueness rules for active binding identities according to the selected acquirer requirements.
- [ ] Define safe terminal/binding DTOs and indexes for authenticated lookup.

## Acceptance criteria

- [ ] Binding cannot reference another aggregator or another merchant connector.
- [ ] Terminal reassignment creates a new deployment/history segment.
- [ ] Device public-key thumbprints and approved app identity are required for active deployment.
- [ ] Historical bindings remain addressable for inquiry and reversal.
- [ ] MID/TID uniqueness follows declared network scope rather than a universal assumption.

## Validation scenarios

- [ ] Attempt all cross-owner foreign-key combinations with two aggregators.
- [ ] Reassign one device and verify past payment references retain original merchant.
- [ ] Insert competing active bindings and test intended uniqueness behavior.

## Expected deliverables

- Terminal and binding migrations.
- Deployment lifecycle and binding contract.

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
