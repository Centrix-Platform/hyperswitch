---
id: "CTX-089"
title: "Secure explicit intent, Binder, and AIDL partner communication"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "android"
component: "Android IPC authorization"
depends_on: ["CTX-014", "CTX-076", "CTX-077", "CTX-079", "CTX-082"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["android/ipc-boundary", "android/partner-app-contract"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Vendor-required exported component contracts and caller-verification mechanisms.", "Authorized partner package/signing identities, rotation lineage, and cross-signer onboarding policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-089: Secure explicit intent, Binder, and AIDL partner communication

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

An embedded library should use ordinary Kotlin/Java calls inside its host process; IPC is reserved for actual vendor or partner application boundaries. Exported components create a separate authorization surface and must not trust a terminal_id, calling-package string, intent action, or callback extra supplied by a requester. Default components to non-exported. For necessary exported Binder/AIDL contracts, identify the runtime caller UID and validate its installed package/signing identity against the approved partner policy on each request. Signature permissions are useful only for the appropriate shared signer arrangement; differently signed aggregator APKs need a deliberate partner trust model. Bind replies and callbacks to an authorized session and original operation. No sensitive payment data should be broadcast or delivered through ambiguous implicit intent resolution. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **android / Android IPC authorization**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork IPC authorization layer and manifest controls`

- `Proposed: approved vendor explicit service/activity adapter`

- `Proposed: Android attacker test application`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/ipc-boundary`
- `android/partner-app-contract`

## Implementation plan

- [ ] Inventory SDK/vendor activities, services, receivers, providers, deep links, and pending intents with their required export status.
- [ ] Replace implicit payment IPC with explicit approved components and non-exported internal entry points.
- [ ] Implement runtime UID/package/signing-certificate authorization for exported services, including multi-package UIDs and approved signing lineage.
- [ ] Bind callbacks and one-use request tokens to caller identity, session, operation, and freshness; validate all IPC sizes and types.
- [ ] Add manifest merge checks, immutable/appropriately scoped pending intents, and documented trust rules for differently signed partner APKs.

## Acceptance criteria

- [ ] Untrusted applications cannot invoke payment, enrollment, configuration, or callback operations.
- [ ] Same-action malicious apps cannot intercept or satisfy vendor communication.
- [ ] Every exported service request validates runtime caller identity and operation authority.
- [ ] Differently signed partners are authorized by explicit policy rather than an ineffective signature-permission assumption.
- [ ] No payment payload or secret is exposed through broadcasts or uncontrolled URI permissions.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.

## Validation scenarios

- [ ] Invoke exported components from attacker APKs with spoofed extras and matching intent actions.
- [ ] Test package/signature replacement, approved signer rotation, and shared UID cases.
- [ ] Replay callbacks and one-use tokens across operations and callers.
- [ ] Inspect merged manifests and exercise malformed/oversized Binder/intent inputs.

## Expected deliverables

- Hardened Android IPC implementation and manifest policy
- Partner application identity/trust configuration
- Attacker APK security regression tests

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Vendor-required exported component contracts and caller-verification mechanisms.
- [ ] Authorized partner package/signing identities, rotation lineage, and cross-signer onboarding policy.

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
