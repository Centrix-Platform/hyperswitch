---
id: "CTX-080"
title: "Enforce firmware, kernel, application, and certification admission policy"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "platform"
component: "Terminal certification admission"
depends_on: ["CTX-013", "CTX-014", "CTX-025", "CTX-026", "CTX-043", "CTX-078", "CTX-079"]
requires_one_of: []
conflict_domains: ["platform/certification-policy", "platform/device-trust", "platform/terminal-registry"]
external_inputs: ["Exact vendor/model/firmware/kernel/app approval documents and applicable acquirer acceptance evidence.", "Trusted software-version evidence and revocation sources.", "Named authority for exceptions, expiry policy, and enforcement propagation objectives."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-080: Enforce firmware, kernel, application, and certification admission policy

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A hardware approval or successful Android attestation does not authorize every terminal software, encryption, gateway, and acquirer combination. Build an admission policy that evaluates the exact approved deployment tuple: vendor/model, secure firmware, payment kernel, payment application, host integration, crypto domain, protocol version, and acquirer enrollment where applicable. Keep evidence references, effective dates, revocations, and exception authority auditable. Device-reported versions may require signed vendor evidence or a trusted management source; unverified values cannot establish certification. Separate temporary operational suspension from certification revocation and ensure both affect newly minted sessions and payment admission. Existing dispatched financial operations must still reach safe completion, reversal, or reconciliation even when new captures are blocked. The policy engine should produce explainable decisions without exposing sensitive trust material.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / Terminal certification admission**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform certification registry and admission policy service`

- `Proposed: certification policy migrations and fixtures`

- `Proposed: terminal activation and session admission integration`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `platform/certification-policy`
- `platform/device-trust`
- `platform/terminal-registry`

## Implementation plan

- [ ] Model versioned certification bundles, approved deployment tuples, trust roots, validity intervals, and revocation sources.
- [ ] Implement deterministic admission evaluation for enrollment, activation, session minting, and new payment capture.
- [ ] Verify vendor/software evidence through documented trust mechanisms and classify unsupported or unverifiable observations.
- [ ] Propagate suspension/revocation decisions to configuration publishing and payment admission with bounded cache freshness.
- [ ] Publish structured denial reasons and operator remediation workflows with tightly controlled exception handling.

## Acceptance criteria

- [ ] Unapproved combinations cannot activate or obtain new capture authority.
- [ ] Attestation success alone cannot satisfy terminal/acquirer certification checks.
- [ ] Expired or revoked policy evidence takes effect within a documented propagation bound.
- [ ] Dispatched operations retain access to approved completion/inquiry paths after capture suspension.
- [ ] Every admission decision records the evaluated evidence and policy versions.

## Validation scenarios

- [ ] Change one tuple dimension at a time and verify approval fails until explicitly permitted.
- [ ] Revoke a certification bundle while sessions and configuration caches exist.
- [ ] Supply unsigned or spoofed firmware/kernel observations.
- [ ] Exercise policy-source outage with fresh, stale, and missing cached policy.

## Expected deliverables

- Certification admission evaluator
- Approved-tuple and revocation schema
- Decision evidence and operator remediation guide

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Exact vendor/model/firmware/kernel/app approval documents and applicable acquirer acceptance evidence.
- [ ] Trusted software-version evidence and revocation sources.
- [ ] Named authority for exceptions, expiry policy, and enforcement propagation objectives.

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
