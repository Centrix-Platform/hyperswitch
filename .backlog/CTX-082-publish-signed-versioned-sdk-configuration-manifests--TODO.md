---
id: "CTX-082"
title: "Publish signed versioned SDK configuration manifests"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "SDK configuration distribution"
depends_on: ["CTX-009", "CTX-043", "CTX-068", "CTX-076", "CTX-079", "CTX-080", "CTX-081"]
requires_one_of: []
conflict_domains: ["android/config-verifier", "configuration-publication-boundary", "platform/config-publisher"]
external_inputs: ["Configuration signing ownership, algorithms, trust bootstrap distribution, and rotation/revocation policy.", "Approved gateway/asset hosts, expiry periods, clock-skew tolerances, and recovery-only rules."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-082: Publish signed versioned SDK configuration manifests

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The SDK needs trusted configuration for gateway endpoints, device deployment, supported capabilities, branding references, and approved terminal bindings. A downloaded JSON document must not be able to redirect payment data to an arbitrary host or revive a revoked processing configuration. Publish signed manifests bound to environment, deployment, intended audience, configuration version, issuance, expiry, and key identifier. Maintain a small bootstrap trust set with an explicit rotation path. Cache only verified configuration and establish fail-closed behavior for expired payment authority while preserving status recovery for existing operations. Rollback should publish a newly authorized higher version that references approved previous behavior, rather than accepting stale lower versions. Keep acquirer credentials, decryption keys, operational API keys, and unnecessary merchant PII out of mobile configuration.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / SDK configuration distribution**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform signed configuration publisher`

- `Proposed: external Android fork configuration verifier and cache`

- `External: juspay/hyperswitch-sdk-android/hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/model/Model.kt (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/config-verifier`
- `configuration-publication-boundary`
- `platform/config-publisher`

## Implementation plan

- [ ] Define canonical manifest signing/verification format and separate trust roots for configuration signing and payment data encryption.
- [ ] Implement platform publication with deployment/audience binding, monotonic versions, expiry, signing key IDs, and approved endpoint allowlists.
- [ ] Implement SDK verification before use, secure cache metadata, anti-rollback checks, and clock-skew policy.
- [ ] Support planned signing-key rotation and emergency revocation using an authenticated bootstrap/update process.
- [ ] Implement superseding configuration rollback, stale-cache handling, and recovery-only operation mode.

## Acceptance criteria

- [ ] Modified, expired, wrong-environment, wrong-deployment, or untrusted-signer manifests are rejected.
- [ ] A lower configuration version cannot reactivate revoked authority.
- [ ] A permitted rollback is represented by a new signed version and explicit policy.
- [ ] Configuration contains no operational/acquirer/decryption secrets.
- [ ] Status recovery can continue under defined restrictions when fresh capture configuration is unavailable.

## Validation scenarios

- [ ] Tamper independently with endpoint, merchant, binding, expiry, and signing key fields.
- [ ] Test signing-key overlap, removal, unknown key IDs, and emergency revocation.
- [ ] Replay older manifests after device restart and configuration cache restoration.
- [ ] Exercise clock skew, no network, expired cache, and a valid superseding rollback.

## Expected deliverables

- Signed configuration manifest specification and publisher
- Android manifest verifier/cache implementation
- Signing rotation and rollback runbook

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Configuration signing ownership, algorithms, trust bootstrap distribution, and rotation/revocation policy.
- [ ] Approved gateway/asset hosts, expiry periods, clock-skew tolerances, and recovery-only rules.

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
