---
id: "CTX-043"
title: "Enforce secret retrieval rotation and cryptographic service boundaries"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "credential-boundary"
depends_on: ["CTX-009", "CTX-014", "CTX-023"]
requires_one_of: []
conflict_domains: ["crypto:boundary", "native:mca-credentials", "secrets:credential-provider"]
external_inputs: ["Secret store/HSM interfaces and acquirer credential/key rotation requirements"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-043: Enforce secret retrieval rotation and cryptographic service boundaries

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Acquirer account metadata references versioned secrets, whereas existing MCAs contain encrypted connector credentials needed by native execution. Implement a controlled CredentialProvider boundary that resolves only the selected aggregator/account/version inside the authorized adapter. Distinguish ordinary API credentials from terminal data/PIN key domains and HSM operations; they have different custody and approval requirements. General gateway services should not acquire decryption keys for opaque terminal payloads. Rotation must preserve the credential version required to inquire, reverse or reconcile existing attempts without selecting a new account accidentally. This ticket integrates retrieval and lifecycle, not custom payment cryptography. Logs, events, route snapshots and administrative reads must carry safe references only, with audited access and bounded caching.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.


## Relevant code and ownership

Primary repository/workstream: **platform / credential-boundary**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- [crates/storage_impl/src/merchant_key_store.rs](../crates/storage_impl/src/merchant_key_store.rs)

- `Proposed: platform/processing/credentials/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `crypto:boundary`
- `native:mca-credentials`
- `secrets:credential-provider`

## Implementation plan

- [ ] Define credential-provider API and service authorization by account/purpose/version.
- [ ] Integrate secret store and approved HSM/crypto interfaces where actually required.
- [ ] Implement rotation overlap, revocation and historical-attempt access policy.
- [ ] Adapt native MCA credential materialization without leaking secrets to control-plane jobs.
- [ ] Add safe diagnostics, cache expiry and access audit records.

## Acceptance criteria

- [ ] Credential access requires authorized account, environment, purpose and version.
- [ ] General gateway processes lack terminal private decryption authority by default.
- [ ] Historical recovery uses the frozen credential/account version according to policy.
- [ ] No credential value appears in snapshots, logs, events or public responses.
- [ ] Unavailable credentials fail safely without rerouting an uncertain payment.

## Validation scenarios

- [ ] Rotate credentials during an in-flight operation and recover its original attempt.
- [ ] Attempt cross-aggregator and wrong-purpose secret retrieval.
- [ ] Inspect logs/outbox/cache contents and test secret-store outage.

## Expected deliverables

- CredentialProvider adapter and access policy.
- Rotation/recovery runbook and secret leakage tests.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Secret store/HSM interfaces and acquirer credential/key rotation requirements

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
