---
id: "CTX-102"
title: "Validate SDK crash, network, hardware, and vendor compatibility"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Mobile reliability acceptance gate"
depends_on: ["CTX-017", "CTX-072", "CTX-077", "CTX-084", "CTX-090", "CTX-091", "CTX-092", "CTX-095", "CTX-096", "CTX-098", "CTX-099"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["android/hardware-matrix", "quality/mobile-reliability"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Supported device fleet and hardware lab inventory, vendor test tools, and approved fault-injection procedures.", "Compatibility support commitments and release promotion thresholds."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-102: Validate SDK crash, network, hardware, and vendor compatibility

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

An emulator success path is insufficient for terminal payments. Establish a bounded compatibility and reliability matrix covering supported Android/API/ABI combinations, device models, certified firmware/kernel/payment-app versions, network behaviors, lifecycle events, and release-mode host integration. Fault injection must cover the moments surrounding capture, gateway admission, downstream dispatch, authorization response, terminal completion, and recovery. Count financial side effects using server/acquirer simulator evidence rather than relying on visible UI callbacks. Test vendor-specific timeouts and hardware disconnect behavior without assuming identical cancellation guarantees. Record the exact approved tuple tested and prevent future SDK or shared-runtime updates from expanding compatibility claims automatically. This gate provides repeatable engineering evidence and highlights untested combinations; external certification remains a separate requirement. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite.

## Prerequisites and dependency outputs

- [CTX-017](CTX-017-build-synthetic-fixtures-and-acquirer-fault-harness--TODO.md) - consume its completed, reviewed deliverables: Build synthetic tenant fixtures and an acquirer fault-injection harness.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-095](CTX-095-detach-client-core-and-react-native-remote-endpoints--TODO.md) - consume its completed, reviewed deliverables: Detach shared client-core and React Native remote endpoints.
- [CTX-096](CTX-096-publish-stable-kotlin-and-java-sdk-facades--TODO.md) - consume its completed, reviewed deliverables: Publish stable Kotlin and Java SDK compatibility facades.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Mobile reliability acceptance gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork hardware/lifecycle compatibility tests`

- `Proposed: sandbox terminal/acquirer fault orchestration harness`

- `Proposed: SDK compatibility and reliability evidence matrix`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/hardware-matrix`
- `quality/mobile-reliability`

## Implementation plan

- [ ] Define supported and explicitly unsupported matrix dimensions with risk-based mandatory test combinations.
- [ ] Automate lifecycle/network fault injection and hardware/vendor scenarios where the approved tools permit it.
- [ ] Exercise process death, battery/power loss, service disconnect, app upgrade, configuration change, and token/key expiry.
- [ ] Verify single financial submission, immutable ownership, correct unknown handling, completion, and original-operation recovery using server evidence.
- [ ] Publish release compatibility results and wire mandatory matrix cases into promotion gates.

## Acceptance criteria

- [ ] Every supported production tuple has identified test evidence or an explicit release-blocking gap.
- [ ] Fault scenarios produce no duplicate charge and preserve correct unresolved outcomes.
- [ ] Release/minified host apps behave consistently with debug integration contracts.
- [ ] Recovery remains correct across supported upgrades and deployment lifecycle changes.
- [ ] Results record exact SDK/client-core/vendor/app/device/gateway versions.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.

## Validation scenarios

- [ ] Drop network before/after dispatch and reorder/delay responses and callbacks.
- [ ] Kill host/vendor processes and remove terminal power during protocol-defined stages.
- [ ] Run release-mode Kotlin/Java hosts across mandatory Android and hardware combinations.
- [ ] Upgrade app/configuration while operations are pending and verify recovery semantics.

## Expected deliverables

- Hardware/vendor compatibility matrix
- Automated fault-injection and conformance suite
- Release reliability evidence report

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Supported device fleet and hardware lab inventory, vendor test tools, and approved fault-injection procedures.
- [ ] Compatibility support commitments and release promotion thresholds.

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
