---
id: "CTX-023"
title: "Model aggregator acquirer accounts using versioned secret references"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "acquirer-accounts"
depends_on: ["CTX-009", "CTX-013", "CTX-014", "CTX-019"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "schema:acquirer", "secrets:credential-references"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-023: Model aggregator acquirer accounts using versioned secret references

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A Connector is implementation code and an MCA is a native configured processing account, currently carrying encrypted connector_account_details and an optional profile association. The public aggregator acquirer account is a different domain object: it represents authorized access to an acquirer relationship that may require several profile-specific MCA projections. Define canonical ownership, capabilities, environment and secret-version references without storing plaintext credentials in ordinary registry tables. Distinguish the aggregator-level credential from merchant MIDs, terminal TIDs, enrollment approvals and cryptographic domains. This ticket owns metadata and relationships; CTX-043 controls retrieval and rotation. It must not imply that every aggregator credential is reusable across merchants or that encrypted terminal traffic can be switched freely between acquirers.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.


## Relevant code and ownership

Primary repository/workstream: **platform / acquirer-accounts**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- [crates/storage_impl/src/merchant_connector_account.rs](../crates/storage_impl/src/merchant_connector_account.rs)

- `Proposed: platform/processing/accounts/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `schema:acquirer`
- `secrets:credential-references`

## Implementation plan

- [ ] Create acquirer account records with aggregator ownership, connector code, environment and lifecycle.
- [ ] Model immutable credential-version references and approved reuse boundaries.
- [ ] Define capability metadata and separate merchant enrollment requirements.
- [ ] Constrain references and indexes by aggregator and environment.
- [ ] Publish redacted account DTOs that never return secret material.

## Acceptance criteria

- [ ] Credential metadata contains only approved secret-store references and versions.
- [ ] One aggregator cannot link another aggregator acquirer account.
- [ ] Production and sandbox accounts cannot be mixed in one binding.
- [ ] Account metadata distinguishes credential reuse permission from merchant approval.
- [ ] Read APIs exclude native MCA IDs and credential contents.

## Validation scenarios

- [ ] Attempt cross-aggregator and cross-environment account references.
- [ ] Serialize account creation and inspection responses and scan for secrets.
- [ ] Represent shared and merchant-specific account arrangements in fixtures.

## Expected deliverables

- Acquirer-account schema and safe DTOs.
- Credential-reference ownership contract.

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
