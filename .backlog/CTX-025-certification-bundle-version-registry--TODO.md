---
id: "CTX-025"
title: "Track approved terminal and acquirer integration combinations"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "certification-registry"
depends_on: ["CTX-013", "CTX-019", "CTX-023"]
requires_one_of: []
conflict_domains: ["contracts:certification", "database-schema-migrations", "platform-contract-catalog", "schema:certification"]
external_inputs: ["Pilot terminal vendor/acquirer approval evidence and supported version combinations"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-025: Track approved terminal and acquirer integration combinations

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A pre-certified device is not automatically approved for every gateway, application, firmware, kernel, cryptographic domain and acquirer combination. The blueprint requires an explicit certification bundle that routing can evaluate before accepting terminal transactions. Create a registry of approved combinations and supporting evidence references, including validity periods, permitted transaction types, currencies and change-control constraints. This is a technical eligibility record, not a replacement for acquirer or assessor approval. Separate observed device versions from approved versions, make approvals immutable and supersedable, and preserve historical evidence for existing attempts. CTX-054 consumes the registry; this ticket must prevent vague boolean certification fields from allowing unreviewed software or network changes into live processing.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.


## Relevant code and ownership

Primary repository/workstream: **platform / certification-registry**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform/terminals/certifications/`

- `Proposed: platform/migrations/`

- `Proposed: contracts/certification-bundle.schema.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:certification`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:certification`

## Implementation plan

- [ ] Define certification bundle dimensions and version-comparison rules from the pilot evidence matrix.
- [ ] Create immutable bundle versions, approval evidence references, validity and revocation state.
- [ ] Model permitted capabilities, processing networks and encryption/key domains.
- [ ] Expose operator-controlled registration and inspection interfaces.
- [ ] Publish representative approved, expired and revoked fixtures.

## Acceptance criteria

- [ ] Approval identifies the complete integration combination and issuing evidence.
- [ ] Unknown firmware or payment-app versions do not match by default.
- [ ] Expired and revoked versions are distinguishable from superseded versions.
- [ ] Historical attempts can retain a stable bundle reference after later revocation.
- [ ] Aggregators cannot self-assert a live certification approval.

## Validation scenarios

- [ ] Match synthetic terminal configurations against exact approved bundles.
- [ ] Expire and revoke bundles and check resulting eligibility inputs.
- [ ] Attempt mutation of an approved version and require a new version.

## Expected deliverables

- Certification registry schema and approval contract.
- Pilot certification fixtures and change-control rules.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot terminal vendor/acquirer approval evidence and supported version combinations

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
