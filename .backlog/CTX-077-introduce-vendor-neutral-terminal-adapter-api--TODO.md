---
id: "CTX-077"
title: "Introduce a vendor-neutral terminal adapter API"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "android"
component: "Terminal adapter boundary"
depends_on: ["CTX-013", "CTX-050", "CTX-062", "CTX-075", "CTX-076"]
requires_one_of: []
conflict_domains: ["android/payment-orchestration", "android/terminal-api"]
external_inputs: ["Vendor lifecycle, completion, cancellation, and recovery protocol documentation.", "Approved terminal capability vocabulary and supported Android threading constraints."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-077: Introduce a vendor-neutral terminal adapter API

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Hyperswitch's checkout SDK is not a certified terminal acquisition stack. Introduce a narrow terminal adapter boundary that can wrap approved vendor hardware or a certified payment application while keeping vendor libraries outside the core SDK API. The boundary must represent capture, readiness, capability discovery, completion with issuer data, cancellation requests, and recovery of an existing operation. Cancellation is not a guarantee that an authorization was reversed, and recovery must not start another charge. Vendor results must expose only approved opaque tokens or encrypted payload references plus safe status metadata. State and lifecycle ownership must be explicit when Android activities are recreated or a vendor service disconnects. This interface is the extension point for multiple terminal families rather than a promise that all vendors share identical capabilities.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.


## Relevant code and ownership

Primary repository/workstream: **android / Terminal adapter boundary**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork gateway-sdk-terminal-api module`

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/PaymentSession.kt (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/payment-orchestration`
- `android/terminal-api`

## Implementation plan

- [ ] Define TerminalAdapter, capability, readiness, capture, completion, cancellation, and recovery interfaces using the versioned DTOs.
- [ ] Model asynchronous callbacks and coroutine cancellation independently from financial cancellation or reversal.
- [ ] Define immutable operation correlation, allowed status transitions, adapter timeouts, and vendor disconnect behavior.
- [ ] Provide a fake adapter implementing deterministic success, decline, pending, unknown, cancellation, and completion-required scenarios.
- [ ] Add adapter registration and capability negotiation without reflection-based untrusted class loading or leakage of vendor types.

## Acceptance criteria

- [ ] The core SDK compiles without any specific vendor SDK dependency.
- [ ] Adapters cannot return raw PAN, PIN, or track data through public types.
- [ ] Recovery accepts an existing operation reference and cannot implicitly initiate a new authorization.
- [ ] Coroutine/Activity cancellation preserves the original financial operation identity.
- [ ] Unsupported completion/cancellation capabilities produce explicit errors rather than simulated success.

## Validation scenarios

- [ ] Run adapter contract tests against the fake adapter for all status transitions.
- [ ] Destroy/recreate a host activity while an adapter operation is active.
- [ ] Disconnect and reconnect the vendor service during capture and completion.
- [ ] Verify public API signatures contain no vendor classes or native Hyperswitch DTOs.

## Expected deliverables

- Vendor-neutral terminal API module
- Deterministic fake adapter
- Adapter conformance test suite

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Vendor lifecycle, completion, cancellation, and recovery protocol documentation.
- [ ] Approved terminal capability vocabulary and supported Android threading constraints.

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
