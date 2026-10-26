---
id: "CTX-096"
title: "Publish stable Kotlin and Java SDK compatibility facades"
status: "TODO"
phase: 3
priority: "P0"
size: "M"
repository: "android"
component: "Public SDK API compatibility"
depends_on: ["CTX-006", "CTX-075", "CTX-076", "CTX-077", "CTX-083", "CTX-090", "CTX-091", "CTX-092", "CTX-094"]
requires_one_of: []
conflict_domains: ["android-public-contract", "android/java-interop", "android/public-api"]
external_inputs: ["Supported Java/Kotlin toolchain versions, minimum Android API, and host lifecycle support policy.", "Public package naming and long-term API compatibility commitments."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-096: Publish stable Kotlin and Java SDK compatibility facades

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The public integration surface should remain stable when internal payment execution moves between Rust, Kotlin, shared JavaScript, or vendor adapters. Provide a small Kotlin-first facade and a deliberately designed Java interface without leaking coroutines-only types, React Native objects, vendor classes, or Hyperswitch internal IDs into ordinary host usage. Initialization, device enrollment, session attachment, terminal readiness, confirmation, status observation, cancellation requests, and recovery need explicit ownership and lifecycle semantics. API evolution must distinguish additive fields from changes that alter financial behavior. Hosts should receive typed safe results and operation references, with clear threading and callback delivery rules. This ticket consolidates the public API after the orchestration behavior is defined; it must not create an alternative submission path that bypasses state, device proof, or session constraints.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-094](CTX-094-white-label-sdk-ui-resources-localization-and-accessibility--TODO.md) - consume its completed, reviewed deliverables: White-label optional SDK UI, resources, localization, and accessibility.


## Relevant code and ownership

Primary repository/workstream: **android / Public SDK API compatibility**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/PaymentConfiguration.kt (verify pinned fork)`

- `External: juspay/hyperswitch-sdk-android/hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/model/Model.kt (verify pinned fork)`

- `Proposed: external Android fork stable Kotlin and Java facade modules`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android-public-contract`
- `android/java-interop`
- `android/public-api`

## Implementation plan

- [ ] Define owned public entry points and initialization/session/result types with explicit lifecycle, threading, and error semantics.
- [ ] Implement Kotlin coroutine/Flow conveniences and Java callback/future adapters over the same coordinator.
- [ ] Hide shared-runtime/vendor/native implementation details and mark internal APIs appropriately.
- [ ] Establish semantic versioning, deprecation, binary/source compatibility checks, and documented API-change review.
- [ ] Compile representative Kotlin and Java host snippets against published artifacts and verify identical financial behavior.

## Acceptance criteria

- [ ] Kotlin and Java hosts can perform enrollment, session attachment, payment observation, and recovery without implementation-specific classes.
- [ ] Both facades call the same single-submission coordinator and authorization checks.
- [ ] Public API signatures do not expose React Native, vendor SDK, or engine-native types.
- [ ] Callbacks have documented threading/lifecycle delivery and do not leak destroyed hosts.
- [ ] Compatibility tooling detects breaking public API changes.

## Validation scenarios

- [ ] Compile and run Kotlin and Java minimal hosts against debug and release artifacts.
- [ ] Compare result/status/error semantics across both facade styles.
- [ ] Destroy/recreate host components while callbacks and flows are active.
- [ ] Introduce a deliberate public binary break in a fixture and verify CI rejection.

## Expected deliverables

- Stable Kotlin/Java SDK facade
- Public API compatibility baseline and versioning policy
- Compilable host integration fixtures

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Supported Java/Kotlin toolchain versions, minimum Android API, and host lifecycle support policy.
- [ ] Public package naming and long-term API compatibility commitments.

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
