---
id: "CTX-106"
title: "Preserve immutable terminal, configuration, and deployment audit history"
status: "TODO"
phase: 3
priority: "P0"
size: "M"
repository: "platform"
component: "Terminal audit and provenance"
depends_on: ["CTX-025", "CTX-026", "CTX-028", "CTX-055", "CTX-068", "CTX-070", "CTX-078", "CTX-079", "CTX-080", "CTX-081", "CTX-082", "CTX-099", "CTX-100"]
requires_one_of: []
conflict_domains: ["configuration-publication-boundary", "platform/config-provenance", "platform/terminal-audit"]
external_inputs: ["Retention/legal requirements, permitted evidence fields, investigation authority, and tamper-evidence expectations.", "Platform incident-response and evidence-export approval policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-106: Preserve immutable terminal, configuration, and deployment audit history

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Payment investigations must reconstruct which aggregator, merchant deployment, device key, approved software/certification bundle, configuration, MID/TID, crypto domain, and route were effective for an attempt. Mutable inventory rows cannot provide that evidence after a reassignment or emergency rollout. Implement append-only lifecycle/configuration records and immutable payment references to the versions used at admission and dispatch. Store safe identifiers and evidence references, not secret values, full payment payloads, or prohibited authentication data. Record actors, authority, reasons, timestamps, event causation, and effective intervals, with corrections represented by new events. Tenant-scoped views must prevent a new merchant deployment from learning the prior merchant's financial history, while authorized platform investigations retain controlled access. Define retention and export policy together with reconciliation and incident-response needs.

## Prerequisites and dependency outputs

- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.
- [CTX-100](CTX-100-monitor-terminal-fleet-and-stage-configuration-revocation-rollouts--TODO.md) - consume its completed, reviewed deliverables: Monitor terminal fleets and stage configuration and revocation rollouts.


## Relevant code and ownership

Primary repository/workstream: **platform / Terminal audit and provenance**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform append-only terminal and configuration audit store`

- `Proposed: payment attempt terminal/configuration snapshot integration`

- `Proposed: scoped terminal investigation API`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `configuration-publication-boundary`
- `platform/config-provenance`
- `platform/terminal-audit`

## Implementation plan

- [ ] Define append-only deployment, binding, certification, key-identity, and configuration version events with causal references.
- [ ] Snapshot safe effective versions on payment attempts and preserve original merchant/aggregator ownership.
- [ ] Implement transactional event emission and idempotent read-model projection with tamper-evident export where required.
- [ ] Enforce tenant/merchant-scoped audit reads and separate controlled platform investigation access.
- [ ] Document retention, correction, evidence export, and secret/PII minimization rules; prevent destructive history updates.

## Acceptance criteria

- [ ] An investigation can reconstruct the exact effective terminal/configuration/route tuple for any retained attempt.
- [ ] Reassignment and rollback do not alter historical payment ownership or version references.
- [ ] Audit events contain actor, reason, authority, causation, and timestamps without secret/payment payload material.
- [ ] Ordinary runtime roles cannot rewrite or delete protected audit history outside defined retention workflows.
- [ ] Cross-merchant and cross-aggregator audit access is denied except authorized platform investigation paths.

## Validation scenarios

- [ ] Trace one payment through configuration rotation, suspension, reassignment, and reconciliation.
- [ ] Attempt history mutation/deletion using normal service roles.
- [ ] Replay outbox events and verify idempotent immutable projection.
- [ ] Export evidence and scan for secrets, prohibited payment data, and unauthorized merchant records.

## Expected deliverables

- Immutable terminal/configuration audit schema and events
- Scoped investigation/read API
- Audit reconstruction and retention runbook

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Retention/legal requirements, permitted evidence fields, investigation authority, and tamper-evidence expectations.
- [ ] Platform incident-response and evidence-export approval policy.

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
