---
id: "CTX-100"
title: "Monitor terminal fleets and stage configuration and revocation rollouts"
status: "TODO"
phase: 3
priority: "P1"
size: "L"
repository: "multi-repo"
component: "Terminal fleet operations"
depends_on: ["CTX-025", "CTX-026", "CTX-068", "CTX-070", "CTX-079", "CTX-080", "CTX-081", "CTX-082", "CTX-093", "CTX-098", "CTX-099"]
requires_one_of: []
conflict_domains: ["android/safe-telemetry", "configuration-publication-boundary", "platform/config-rollout", "platform/fleet-operations"]
external_inputs: ["Fleet scale/freshness objectives, permitted telemetry, cohort policy, and revocation propagation targets.", "Vendor device-management integration and push capabilities if any."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-100: Monitor terminal fleets and stage configuration and revocation rollouts

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A white-label terminal fleet needs operational visibility into approved software/configuration versions, enrollment freshness, service health, and rollout failures without collecting payment payloads. Build tenant-scoped fleet reporting from safe device/configuration evidence and immutable deployment records. Support staged configuration and trust-policy rollout by explicit cohorts with pause, superseding rollback, and health gates. Emergency capture revocation must have a documented propagation target and fail-closed admission behavior; disconnected devices cannot be assumed to receive a push, so server admission and short-lived authority remain essential. Rollout policy must preserve status inquiry and protocol-required completion of already dispatched operations. Separate ordinary telemetry delay from certification invalidity and show operators which data is observed, attested, or stale. Aggregators may view and manage only their authorized fleets.

## Prerequisites and dependency outputs

- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) - consume its completed, reviewed deliverables: Redact mobile logs, crashes, storage, and backups.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal fleet operations**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform fleet telemetry and rollout service`

- `Proposed: external Android fork safe configuration health reporting`

- `Proposed: fleet rollout and revocation dashboards`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/safe-telemetry`
- `configuration-publication-boundary`
- `platform/config-rollout`
- `platform/fleet-operations`

## Implementation plan

- [ ] Define allowlisted fleet health/version signals, freshness classification, collection limits, and retention.
- [ ] Implement tenant-scoped fleet read models and safe telemetry ingestion with device/session authorization.
- [ ] Build cohort-based configuration rollout with canary gates, pause, promotion, and higher-version superseding rollback.
- [ ] Implement emergency capture revocation propagation through session/configuration/routing admission and measure convergence.
- [ ] Create alerts and runbooks for stale fleets, version skew, trust failures, and rollout regressions.

## Acceptance criteria

- [ ] Fleet queries and telemetry cannot cross aggregator boundaries.
- [ ] Telemetry contains no payment payload, PAN/PIN, tokens, or sensitive authentication material.
- [ ] Rollout state identifies cohort, config/policy version, health gate, and authorized operator.
- [ ] Revocation blocks new capture within the documented enforcement bound even if push delivery fails.
- [ ] Existing operations retain the approved completion/status recovery path.

## Validation scenarios

- [ ] Canary a deliberately invalid configuration and verify rollout pause and superseding rollback.
- [ ] Simulate offline devices, delayed telemetry, and missing push delivery.
- [ ] Revoke a certification while active sessions and caches exist.
- [ ] Attempt cross-aggregator fleet queries and spoofed telemetry submission.

## Expected deliverables

- Tenant-scoped terminal fleet read model
- Staged rollout/revocation controls
- Fleet health dashboards and operational runbooks

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Fleet scale/freshness objectives, permitted telemetry, cohort policy, and revocation propagation targets.
- [ ] Vendor device-management integration and push capabilities if any.

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
