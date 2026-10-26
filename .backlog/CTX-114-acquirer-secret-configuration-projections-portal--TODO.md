---
id: "CTX-114"
title: "Build acquirer configuration and write-only credential management"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Acquirer configuration UI"
depends_on: ["CTX-023", "CTX-024", "CTX-043", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-acquirers"]
external_inputs: ["Approved acquirer credential schemas and non-production credentials or protocol stubs; live secrets are not required for implementation."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-114: Build acquirer configuration and write-only credential management

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators own processing relationships with acquirers, while the platform projects approved configurations into merchant/profile-specific Hyperswitch MCAs. A connector implementation, credential set and terminal binding are different resources and should not be combined into a generic free-form JSON form. The portal must accept secrets through approved write-only APIs, then show identifiers, validation status, masked metadata and credential version only. Reusing an aggregator credential across authorized merchant projections must remain explicit and auditable. Configuration changes need validation, staging and safe rotation rather than overwriting live secrets blindly. This ticket implements operator journeys around the acquirer-account and projection services; it does not add new network protocols or assert certification of a newly selected terminal combination.

## Prerequisites and dependency outputs

- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Acquirer configuration UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- [crates/openapi/src/routes/merchant_connector_account.rs](../crates/openapi/src/routes/merchant_connector_account.rs)

- `Proposed: services/platform-control/src/acquirer-accounts/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-acquirers`

## Implementation plan

- [ ] Create acquirer-account list/detail and connector-specific forms generated from approved field definitions with client/server validation.
- [ ] Submit secrets only to dedicated credential-ingestion endpoints; clear browser form values and prevent telemetry/autocomplete leakage as appropriate.
- [ ] Display write-only secret status, version, expiry and validation outcome without retrieve/reveal functionality.
- [ ] Provide merchant-specific projection status, safe retry and authorization-aware assignment of acquirer accounts.
- [ ] Integrate staged credential rotation, test-connection operations and activation workflows without exposing secret-store references to ordinary users.
- [ ] Explain certification/terminal eligibility and preserve configuration history for incident review.

## Acceptance criteria

- [ ] Stored credentials cannot be fetched or revealed through the portal/read APIs.
- [ ] Forms submit only approved connector fields and redact all sensitive validation/logging output.
- [ ] Cross-aggregator acquirer-account and merchant-projection assignments are denied.
- [ ] Rotation produces a new version and preserves the documented behavior of existing in-flight attempts.
- [ ] Projection failures are observable and retryable without duplicating MCA relationships.
- [ ] The interface does not imply that connector selection certifies a terminal integration.

## Validation scenarios

- [ ] Inspect browser traffic, error reporting and logs during credential create/validate/rotate using fake secrets.
- [ ] Run projection and ownership tests against two aggregators and several merchant profiles.
- [ ] Exercise validation failure, stale edits, partial provisioning and rotation rollback conditions.

## Expected deliverables

- Write-only acquirer account and credential forms.
- Merchant/MCA projection management screens.
- Secret-handling and rotation UI test evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved acquirer credential schemas and non-production credentials or protocol stubs; live secrets are not required for implementation.

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
