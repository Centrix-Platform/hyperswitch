---
id: "CTX-088"
title: "Support approved application-layer JWE envelopes where required"
status: "TODO"
phase: 3
priority: "P1"
size: "L"
repository: "multi-repo"
component: "Conditional application-layer encryption"
depends_on: ["CTX-009", "CTX-014", "CTX-043", "CTX-076", "CTX-082", "CTX-084", "CTX-087"]
requires_one_of: []
conflict_domains: ["acquirer/crypto-adapter", "android/envelope-encryption", "contracts/jwe-envelope", "platform-contract-catalog"]
external_inputs: ["Explicit vendor/acquirer and security approval for supplementary application-layer encryption.", "Chosen approved JWE algorithm profile, key-distribution trust model, test vectors, and decryption endpoint ownership."]
external_inputs_resolved: false
applicability: "conditional"
applicability_decision: "pending"
requires_decisions: ["application_layer_jwe"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-088: Support approved application-layer JWE envelopes where required

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

This ticket applies only if the selected certified integration explicitly requires an additional application-layer public-key envelope for data the SDK is already authorized to handle. It does not authorize raw PAN/PIN collection in the host APK, replace terminal encryption, or establish PCI scope reduction. Prefer the approved vendor opaque payload/token path from CTX-087 when no additional envelope is required. If activated, define a vetted JWE profile with authenticated recipient-key distribution, allowed algorithms, environment/key-purpose separation, and binding to immutable transaction context. The private decryption key must remain in the approved endpoint security boundary. Randomized encryption means retries require a stable operation/payload reference or reuse of the original permitted envelope; bytewise changes must not accidentally create a different financial operation.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.

- Required recorded decision: `application_layer_jwe` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Conditional application-layer encryption**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork approved envelope encryption module if applicable`

- `Proposed: platform recipient public-key distribution contract if applicable`

- `Proposed: approved decrypting endpoint JWE validation if applicable`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `acquirer/crypto-adapter`
- `android/envelope-encryption`
- `contracts/jwe-envelope`
- `platform-contract-catalog`

## Implementation plan

- [ ] Record the approved requirement and decision to activate or mark this conditional ticket not applicable, including the security owner.
- [ ] Specify a vetted JWE profile, allowed algorithms, protected headers, recipient key usage, authenticated context, and size limits.
- [ ] Implement authenticated versioned recipient-key discovery, purpose/environment/expiry validation, rotation overlap, and unknown-key handling.
- [ ] Implement envelope creation and receiving-end validation with an established cryptographic library and approved test vectors.
- [ ] Define retry identity, secure buffer lifetime, redaction, and interoperability tests without adding a raw payment-data capture API.

## Acceptance criteria

- [ ] Implementation exists only after an explicit approved integration requirement is recorded.
- [ ] Private recipient keys are absent from APKs and general gateway services.
- [ ] Algorithm confusion, wrong-purpose/environment keys, expired keys, and modified context are rejected.
- [ ] Retry behavior preserves one business operation despite randomized envelope generation.
- [ ] Documentation makes no claim that JWE alone certifies capture or removes PCI obligations.

## Validation scenarios

- [ ] Run approved interoperability vectors across Android and the authorized decrypting endpoint.
- [ ] Mutate protected headers, authenticated context, recipient key ID, and ciphertext.
- [ ] Rotate keys through overlap/expiry and test stale cached discovery responses.
- [ ] Retry one operation with the defined stable reference and verify duplicate protection.

## Expected deliverables

- Conditional decision record and approved JWE profile
- Android/receiver envelope support if activated
- Cryptographic interoperability and retry fixtures

## External inputs and applicability

Applicability: **conditional**. Initial decision: **pending**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Explicit vendor/acquirer and security approval for supplementary application-layer encryption.
- [ ] Chosen approved JWE algorithm profile, key-distribution trust model, test vectors, and decryption endpoint ownership.

Record evidence and update `external_inputs_resolved` only after these inputs are verified. Continue independent work while a necessary input is pending.

Activate this conditional branch only with the recorded integration requirement and owner evidence. Downstream conditional prerequisites enforce its completion before qualified use.

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
