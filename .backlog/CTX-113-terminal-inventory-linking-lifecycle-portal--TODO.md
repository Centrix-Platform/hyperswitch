---
id: "CTX-113"
title: "Build terminal inventory, enrollment and merchant-binding screens"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Terminal management UI"
depends_on: ["CTX-026", "CTX-047", "CTX-079", "CTX-081", "CTX-099", "CTX-100", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-terminals"]
external_inputs: ["Controlled device/simulator inventory and approved binding/certification fixtures."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-113: Build terminal inventory, enrollment and merchant-binding screens

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Physical devices and smart-terminal applications have a lifecycle separate from merchant profiles and acquirer credentials. The portal must expose enrollment evidence, device identity, approved software/configuration versions, merchant assignment and eligible processing bindings without treating a typed serial number as authenticated identity. Operators need controlled activation, suspension, replacement and decommissioning journeys. Unlinking or reassigning a terminal must invalidate appropriate sessions/configuration and preserve its historical relationship with payments. Use backend enrollment and fleet APIs from the terminal track rather than implementing client-side trust decisions. The interface should explain why a terminal is ineligible, distinguish device and acquirer statuses, and avoid revealing encryption keys or allowing arbitrary unapproved MID/TID combinations.

## Prerequisites and dependency outputs

- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.
- [CTX-100](CTX-100-monitor-terminal-fleet-and-stage-configuration-revocation-rollouts--TODO.md) - consume its completed, reviewed deliverables: Monitor terminal fleets and stage configuration and revocation rollouts.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Terminal management UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- `Proposed: services/platform-control/src/terminals/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-terminals`

## Implementation plan

- [ ] Build scoped inventory/detail views showing canonical terminal ID, vendor/model, observed evidence, configured merchant, status and configuration version.
- [ ] Integrate enrollment initiation and status with bounded enrollment codes or approved QR contracts, never reusable operational credentials.
- [ ] Implement link/unlink and binding selection through eligible merchant/connector options and server-validated MID/TID/certification relationships.
- [ ] Add authorized suspend, revoke, replace and decommission actions with reasons and version checks.
- [ ] Expose stale configuration, revoked identity, certificate/attestation and fleet compatibility findings without sensitive payloads.
- [ ] Preserve historical assignments and explain in-flight payment handling during lifecycle changes.

## Acceptance criteria

- [ ] Only authenticated enrolled devices can become processing-active through the approved lifecycle.
- [ ] A terminal cannot be linked to another aggregator merchant or an ineligible processing binding.
- [ ] Unlink/revoke invalidates the required authority/configuration and leaves historical payments traceable.
- [ ] The UI displays device status, processing eligibility and configuration version separately.
- [ ] Terminal replacement does not silently reuse the old device identity or active sessions.
- [ ] No key material or raw payment data appears in enrollment screens or diagnostics.

## Validation scenarios

- [ ] Run enroll-to-link-to-suspend E2E tests with a simulator and two aggregators.
- [ ] Test conflicting assignment, stale version, revoked device and incompatible certification cases.
- [ ] Verify historical assignments and in-flight/UNKNOWN operations remain visible after unlink.

## Expected deliverables

- Terminal enrollment/inventory/binding UI.
- Lifecycle and cross-tenant E2E tests.
- Terminal operator workflow documentation.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Controlled device/simulator inventory and approved binding/certification fixtures.

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
