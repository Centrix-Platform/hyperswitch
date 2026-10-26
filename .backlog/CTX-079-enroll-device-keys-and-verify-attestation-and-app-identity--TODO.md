---
id: "CTX-079"
title: "Enroll device keys and verify attestation and application identity"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Device identity and enrollment"
depends_on: ["CTX-009", "CTX-014", "CTX-025", "CTX-026", "CTX-041", "CTX-042", "CTX-075", "CTX-076", "CTX-078"]
requires_one_of: []
conflict_domains: ["android/device-enrollment", "platform/device-trust", "platform/terminal-registry"]
external_inputs: ["Approved attestation/vendor trust roots and revocation distribution mechanism.", "Allowed APK package/signing identities, signing rotation lineage, and minimum device security policy.", "Vendor-managed key alternatives for devices that do not use standard Android attestation."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-079: Enroll device keys and verify attestation and application identity

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Payment-capable SDK sessions must be bound to an enrolled device key rather than a terminal_id supplied by an arbitrary APK. Generate a non-exportable key through Android Keystore where supported and prove possession during a server-challenged enrollment. Validate attestation on the server using the approved roots, challenge, identity, security-level expectations, and revocation information. Treat application package and signing identity as separate policy inputs and record signing-key lineage when rotation is permitted. Unsupported hardware, unavailable attestation, or vendor-specific trust evidence requires an explicit policy decision, never an automatic downgrade. Attestation provides evidence about a key/device environment; it does not certify card capture or prove terminal/acquirer integration approval. Preserve a path for certified vendor keys that use a different documented enrollment model.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Device identity and enrollment**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork gateway-sdk-device module`

- `Proposed: platform enrollment challenge and attestation verifier`

- `Proposed: device trust policy and evidence storage`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/device-enrollment`
- `platform/device-trust`
- `platform/terminal-registry`

## Implementation plan

- [ ] Implement Keystore key creation with explicit algorithm, purposes, key alias lifecycle, and hardware/security-level policy.
- [ ] Add server-generated short-lived enrollment challenges and proof-of-possession binding to deployment, aggregator, and environment.
- [ ] Verify the complete attestation chain, challenge, applicable application identity data, trust roots, revocation, and policy on the server.
- [ ] Record public key thumbprint, trust evidence, signing lineage, verification time, and policy version without storing private keys.
- [ ] Implement re-enrollment, key rotation, unsupported-device handling, and revocation invalidation for SDK sessions.

## Acceptance criteria

- [ ] No private device key leaves the platform-approved secure key storage.
- [ ] Replayed, wrong-environment, wrong-deployment, and expired challenges are rejected.
- [ ] Attestation is verified server-side and independently of client assertions.
- [ ] Unknown signer/device trust evidence cannot silently produce payment-capable enrollment.
- [ ] Key rotation and revocation invalidate prior authority according to documented policy.

## Validation scenarios

- [ ] Submit altered chains, mismatched challenges, revoked evidence, and untrusted roots.
- [ ] Test software-backed, TEE-backed, and supported StrongBox behavior against explicit policy.
- [ ] Enroll an APK with a different signing certificate and verify rejection or approved lineage handling.
- [ ] Rotate a device key during an active session and validate the defined recovery/re-enrollment behavior.

## Expected deliverables

- Android device-key enrollment implementation
- Server attestation and application identity verifier
- Enrollment trust-policy fixtures and operational runbook

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved attestation/vendor trust roots and revocation distribution mechanism.
- [ ] Allowed APK package/signing identities, signing rotation lineage, and minimum device security policy.
- [ ] Vendor-managed key alternatives for devices that do not use standard Android attestation.

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
