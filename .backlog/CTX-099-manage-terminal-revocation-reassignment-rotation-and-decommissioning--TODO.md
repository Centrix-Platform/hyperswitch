---
id: "CTX-099"
title: "Manage terminal revocation, reassignment, rotation, and decommissioning"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Terminal deployment lifecycle"
depends_on: ["CTX-026", "CTX-041", "CTX-042", "CTX-047", "CTX-057", "CTX-062", "CTX-068", "CTX-078", "CTX-079", "CTX-080", "CTX-081", "CTX-082", "CTX-092"]
requires_one_of: []
conflict_domains: ["android/device-lifecycle", "payment-execution-state-boundary", "payment/route-eligibility", "platform/terminal-lifecycle"]
external_inputs: ["Vendor secure reset/key rotation/reprovisioning procedures and acquirer MID/TID retirement rules.", "Transfer authorization, financial draining, lost-device, and retention policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-099: Manage terminal revocation, reassignment, rotation, and decommissioning

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Physical devices outlive individual merchant deployments and must move safely through suspension, transfer, key rotation, loss, theft, and decommissioning. Reassignment must end the prior deployment and create a new immutable deployment identity/version rather than editing the merchant on historical rows. Revoke old SDK sessions and configuration authority, remove stale local state, and require approved enrollment/binding validation for the new merchant. Previously dispatched financial operations still belong to their original merchant and require an authorized platform or prior-merchant recovery path; a new deployment must not inherit access to them. Key rotation and re-provisioning must follow vendor security rules and cannot export terminal secrets. Define financial draining and operational controls before transfer, including unresolved completion/reversal cases and acquirer MID/TID retirement requirements.

## Prerequisites and dependency outputs

- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal deployment lifecycle**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform terminal lifecycle commands and immutable deployments`

- `Proposed: external Android fork revocation and re-enrollment handling`

- `Proposed: terminal transfer operational runbook`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/device-lifecycle`
- `payment-execution-state-boundary`
- `payment/route-eligibility`
- `platform/terminal-lifecycle`

## Implementation plan

- [ ] Define authorized suspension, revoke, rotate, transfer, loss/theft, and decommission state transitions with prerequisites and audit reasons.
- [ ] Implement old-deployment closure and new-deployment creation with immutable history and unique active assignment constraints.
- [ ] Invalidate sessions/configuration/caches and trigger approved local cleanup and device re-enrollment.
- [ ] Define draining and authorized recovery for outstanding original-merchant operations before or during transfer.
- [ ] Integrate vendor key reprovisioning/MID-TID retirement requirements and verify no old authority survives activation of the replacement.

## Acceptance criteria

- [ ] Reassignment never changes merchant ownership recorded on existing payments or attempts.
- [ ] Old sessions and manifests cannot authorize new captures after revocation within the defined bound.
- [ ] The new merchant cannot read or recover the old merchant’s operation details.
- [ ] Outstanding original operations have a documented safe completion/reconciliation route.
- [ ] Decommissioned devices require explicit authorized reprovisioning before any reuse.

## Validation scenarios

- [ ] Reassign a terminal with succeeded, pending, unknown, and completion-required operations.
- [ ] Replay old SDK tokens/manifests after transfer and key rotation.
- [ ] Race reassignment with payment admission and verify a consistent version boundary.
- [ ] Simulate lost/stolen device revocation while offline and upon reconnection.

## Expected deliverables

- Terminal deployment transfer/revocation workflows
- SDK cleanup and re-enrollment behavior
- Lifecycle and outstanding-operation recovery runbook

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Vendor secure reset/key rotation/reprovisioning procedures and acquirer MID/TID retirement rules.
- [ ] Transfer authorization, financial draining, lost-device, and retention policy.

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
