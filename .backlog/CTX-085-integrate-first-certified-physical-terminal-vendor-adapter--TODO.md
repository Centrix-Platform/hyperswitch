---
id: "CTX-085"
title: "Integrate the first certified physical-terminal vendor adapter"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Physical terminal adapter"
depends_on: ["CTX-013", "CTX-050", "CTX-062", "CTX-077", "CTX-079", "CTX-080", "CTX-081", "CTX-082", "CTX-084"]
requires_one_of: []
conflict_domains: ["android/terminal-adapter-physical", "payment-execution-state-boundary", "payment/terminal-payload-format"]
external_inputs: ["CTX-013 recorded pilot path selection: physical or smart terminal, with named vendor/application/acquirer tuple; the unselected adapter remains expansion work.", "Named physical terminal vendor/model, SDK/license/artifact access, test devices, and integration documentation.", "Acquirer sandbox, approved crypto provisioning, test cards/scripts, and certification test plan."]
external_inputs_resolved: false
applicability: "integration-dependent"
applicability_decision: "pending"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-085: Integrate the first certified physical-terminal vendor adapter

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Implement one named physical-terminal family using its approved vendor SDK or service, not a generic assumption that any EMV reader can return interchangeable ciphertext. The initial integration must pin the actual hardware, secure firmware, kernel, payment app/library, host protocol, crypto domain, and acquirer environment. Card and PIN collection stay inside the vendor's approved secure component. The adapter returns only the approved opaque encrypted result/token and safe status metadata to the SDK. Capabilities such as contact/contactless, online-only behavior, cancellation, issuer scripts, and completion must reflect the vendor protocol. Test fixtures cannot be inferred production field mappings. Completion, recovery, and certification evidence are separate gates that must be met before live activation, even if a sandbox authorization succeeds. CTX-013 selects the first pilot path; this adapter is required when selected and otherwise remains expansion work outside the initial pilot critical path.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Physical terminal adapter**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork gateway-sdk-terminal-first-physical-vendor module`

- `Proposed: platform approved physical-terminal payload adapter`

- `Proposed: vendor hardware conformance fixtures`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/terminal-adapter-physical`
- `payment-execution-state-boundary`
- `payment/terminal-payload-format`

## Implementation plan

- [ ] Select and record the first approved hardware/software tuple and import vendor dependencies through controlled artifact inputs.
- [ ] Implement readiness and capability checks plus secure capture under the vendor-neutral adapter interface.
- [ ] Map vendor identifiers, opaque payload format, correlation references, and safe errors into the versioned SDK contract.
- [ ] Implement documented cancel/disconnect behavior and handoff points for terminal completion and original-operation recovery.
- [ ] Build vendor-sandbox contract tests and document unsupported capabilities and required certification evidence.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] The adapter compiles against the pinned approved vendor dependency and supports the declared terminal family only.
- [ ] Host APK and core SDK APIs never receive clear PAN, PIN, or track data.
- [ ] Unapproved firmware/application/configuration tuples are denied before capture.
- [ ] Payload references and transaction identifiers remain stable across recoverable disconnects.
- [ ] Unsupported operations fail explicitly and no fallback raw-card collector is introduced.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Run vendor-provided approval/decline/cancel fixtures on the named hardware revision.
- [ ] Disconnect power/network/service at vendor-defined capture and handoff points.
- [ ] Attempt operation under a mismatched crypto domain and configuration version.
- [ ] Inspect memory/log/IPC boundaries using approved test data and vendor instrumentation.

## Expected deliverables

- First physical-terminal adapter module
- Pinned vendor integration matrix and payload mapping
- Hardware sandbox conformance evidence

## External inputs and applicability

Applicability: **integration-dependent**. Initial decision: **pending**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 recorded pilot path selection: physical or smart terminal, with named vendor/application/acquirer tuple; the unselected adapter remains expansion work.
- [ ] Named physical terminal vendor/model, SDK/license/artifact access, test devices, and integration documentation.
- [ ] Acquirer sandbox, approved crypto provisioning, test cards/scripts, and certification test plan.

Record evidence and update `external_inputs_resolved` only after these inputs are verified. Continue independent work while a necessary input is pending.

CTX-013 selects the initial adapter. Mark the selected branch applicable; retain the other as expansion work. A headless SDK does not change vendor certification or ownership requirements.

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
