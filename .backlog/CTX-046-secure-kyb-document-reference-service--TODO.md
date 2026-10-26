---
id: "CTX-046"
title: "Secure onboarding document uploads and sensitive merchant evidence"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "onboarding-evidence"
depends_on: ["CTX-014", "CTX-021", "CTX-029", "CTX-034", "CTX-038"]
requires_one_of: []
conflict_domains: ["contracts:document-references", "platform-contract-catalog", "privacy:merchant-pii", "storage:kyb-documents"]
external_inputs: ["Approved KYB document requirements, retention and access policy"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-046: Secure onboarding document uploads and sensitive merchant evidence

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Onboarding requires evidence, but merchant/profile metadata and generic event payloads are unsuitable document stores. Implement an owned document reference service with constrained upload/download authorization, encryption, scanning and explicit retention/access policy. The onboarding API should accept an approved document-set reference tied to the aggregator and merchant or pre-onboarding case, not an arbitrary object URL. Protect legal identifiers and personal data separately from payment telemetry, and limit operator/support access to the stated purpose. This ticket is about evidence handling and secure references, not automating legal approval decisions. Include failed uploads, malware/quarantine outcomes, expiry and deletion/hold semantics so later agents cannot accidentally make a pending upload count as validated KYB evidence.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.


## Relevant code and ownership

Primary repository/workstream: **platform / onboarding-evidence**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/file.rs](../crates/diesel_models/src/file.rs)

- `Proposed: platform/merchants/documents/`

- `Proposed: contracts/document-reference.schema.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:document-references`
- `platform-contract-catalog`
- `privacy:merchant-pii`
- `storage:kyb-documents`

## Implementation plan

- [ ] Define document-set ownership, classification, readiness and retention states.
- [ ] Implement short-lived upload/download grants with size/type/content checks.
- [ ] Integrate scanning/quarantine and approved object encryption/access controls.
- [ ] Bind document references to onboarding cases and prohibit foreign URL ingestion.
- [ ] Audit access and implement retention, legal-hold and deletion workflows.

## Acceptance criteria

- [ ] Another aggregator cannot read or attach a document-set reference.
- [ ] Upload permission is limited to target object, method, size and expiry.
- [ ] Unscanned/quarantined documents cannot satisfy onboarding evidence readiness.
- [ ] Document contents and sensitive identifiers are absent from ordinary logs/events.
- [ ] Retention deletion respects documented hold and audit requirements.

## Validation scenarios

- [ ] Attempt object path traversal and foreign-reference attachment.
- [ ] Upload oversized, disallowed and synthetic malicious test files.
- [ ] Expire grants and exercise retention versus legal hold.

## Expected deliverables

- Document-reference API and storage policy.
- Evidence lifecycle tests and PII access audit schema.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved KYB document requirements, retention and access policy

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
