---
id: "CTX-076"
title: "Define versioned terminal and SDK configuration contracts"
status: "TODO"
phase: 3
priority: "P0"
size: "M"
repository: "multi-repo"
component: "Terminal and SDK contracts"
depends_on: ["CTX-006", "CTX-025", "CTX-026", "CTX-041", "CTX-050", "CTX-075"]
requires_one_of: []
conflict_domains: ["android-public-contract", "android/public-models", "contracts/terminal-sdk", "platform-contract-catalog"]
external_inputs: ["Initial terminal vendor capability descriptions and approved encrypted payload reference formats.", "Supported currency, operation, Android-version, and API compatibility policies."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-076: Define versioned terminal and SDK configuration contracts

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The public SDK must describe this platform's aggregator, merchant, terminal deployment, and approved processing binding without exposing Hyperswitch MerchantAccount, BusinessProfile, or MCA identifiers. Device observations are claims to validate; server assignments remain authoritative. Define contracts before vendor adapters so terminal capabilities, configuration versions, payment-session constraints, encrypted payload references, and uncertain outcomes are represented consistently across Kotlin, Java, the gateway, and future Kotlin services. The contract must separate terminal identity from acquirer MID/TID and separate payment creation from terminal completion. Amounts use integer minor units with explicit currency and bounded values. Raw PAN, track data, PIN data, cryptographic keys, and arbitrary acquirer URLs are outside these DTOs. Unknown fields and enum evolution require a documented compatibility policy.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal and SDK contracts**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/model/Model.kt (verify pinned fork)`

- `Proposed: platform OpenAPI terminal and SDK schema package`

- `Proposed: external Android fork versioned terminal DTO module`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android-public-contract`
- `android/public-models`
- `contracts/terminal-sdk`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define versioned schemas for terminal observations, deployment identity, bindings, signed configuration, SDK sessions, secure payload references, and payment results.
- [ ] Specify ownership and mutability for every field, distinguishing device observations from server-approved assignments.
- [ ] Specify amount/currency validation, opaque identifier formats, capability negotiation, error categories, and pending/unknown status semantics.
- [ ] Generate or hand-maintain Kotlin/Java DTOs against the published OpenAPI/JSON schemas without importing native engine models.
- [ ] Publish representative valid and invalid fixtures plus backward/forward compatibility rules.

## Acceptance criteria

- [ ] Contracts include explicit schema version, deployment/configuration version, environment, and session identity.
- [ ] Mobile input cannot select another aggregator, merchant, MCA, credential, decryption key, or arbitrary endpoint.
- [ ] Unknown and pending financial results are distinguishable from failures.
- [ ] Kotlin, Java, and gateway fixtures round-trip with equivalent semantics.
- [ ] Schema review confirms no clear cardholder or sensitive authentication fields are included.

## Validation scenarios

- [ ] Validate complete and minimal fixtures for each schema version.
- [ ] Reject fractional/overflow amounts, mismatched currencies, and unsupported required capabilities.
- [ ] Exercise unknown optional fields and future enum values according to compatibility policy.
- [ ] Verify engine-internal IDs and secret fields cannot appear in generated public payloads.

## Expected deliverables

- Versioned terminal/SDK schema package
- Kotlin/Java contract fixtures
- Field authority and compatibility specification

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Initial terminal vendor capability descriptions and approved encrypted payload reference formats.
- [ ] Supported currency, operation, Android-version, and API compatibility policies.

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
