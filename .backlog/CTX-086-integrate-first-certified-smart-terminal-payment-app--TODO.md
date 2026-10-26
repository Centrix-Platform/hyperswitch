---
id: "CTX-086"
title: "Integrate the first certified smart-terminal payment application"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Smart terminal payment-app adapter"
depends_on: ["CTX-013", "CTX-050", "CTX-062", "CTX-077", "CTX-079", "CTX-080", "CTX-081", "CTX-082", "CTX-084"]
requires_one_of: []
conflict_domains: ["android/partner-app-contract", "android/terminal-adapter-smart"]
external_inputs: ["CTX-013 recorded pilot path selection: physical or smart terminal, with named vendor/application/acquirer tuple; the unselected adapter remains expansion work.", "Named smart-terminal vendor/payment app, approved version and signer, IPC SDK/documentation, and test hardware.", "Whether the vendor app captures only or executes authorization, plus inquiry/completion APIs and acquirer evidence."]
external_inputs_resolved: false
applicability: "integration-dependent"
applicability_decision: "pending"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-086: Integrate the first certified smart-terminal payment application

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Smart terminals frequently delegate capture to a vendor payment application running in another Android process. Integrate one explicitly approved application/version/signing identity and its documented service or activity contract. The host SDK must not invent a raw EMV capture pathway or treat ordinary Android NFC access as certified SoftPOS. Define which component owns card interaction, authorization transport, completion, and financial correlation; some vendor applications perform the authorization themselves, so forwarding their result into a second gateway charge would be a duplicate. Normalize the chosen model into the terminal adapter contract and retain its original operation reference. Secure caller/callee authorization is a prerequisite for production and is hardened in the dedicated IPC ticket. Unknown vendor outcomes must be recoverable through the original vendor/gateway operation. CTX-013 selects the first pilot path; this adapter is required when selected and otherwise remains expansion work outside the initial pilot critical path.

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

Primary repository/workstream: **multi-repo / Smart terminal payment-app adapter**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork gateway-sdk-terminal-first-smart-vendor module`

- `Proposed: approved vendor payment-app IPC integration`

- `Proposed: smart-terminal execution ownership contract`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/partner-app-contract`
- `android/terminal-adapter-smart`

## Implementation plan

- [ ] Document the vendor application’s execution model, ownership of authorization, supported protocol, signing identity, and approved deployment tuple.
- [ ] Implement explicit component integration behind TerminalAdapter without implicit intent discovery or raw card collection.
- [ ] Map vendor session/correlation IDs and opaque results to capture-only or vendor-executed payment flows as appropriate.
- [ ] Implement lifecycle, user-return, service disconnect, capability, and completion/recovery handoffs.
- [ ] Provide contract fixtures and integration evidence for the chosen vendor app/version and block unsupported execution models.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] Only the configured approved payment application can satisfy the integration handshake.
- [ ] A vendor-executed authorization is not submitted again as a gateway authorization.
- [ ] The adapter preserves vendor and gateway operation correlation through app/task switches.
- [ ] Sensitive payloads do not leak through implicit intents, broadcasts, or exported diagnostics.
- [ ] The approved app/version/signing tuple is enforced and unresolved outcomes remain pending/unknown.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Substitute an app with the same advertised intent action but a different signer.
- [ ] Kill/restart host and payment app during user interaction and return.
- [ ] Exercise capture-only and vendor-executed fixtures and count financial submissions.
- [ ] Install an unapproved payment-app version and verify admission failure.

## Expected deliverables

- First smart-terminal payment-app adapter
- Execution-ownership and IPC contract
- Smart-terminal sandbox interoperability evidence

## External inputs and applicability

Applicability: **integration-dependent**. Initial decision: **pending**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 recorded pilot path selection: physical or smart terminal, with named vendor/application/acquirer tuple; the unselected adapter remains expansion work.
- [ ] Named smart-terminal vendor/payment app, approved version and signer, IPC SDK/documentation, and test hardware.
- [ ] Whether the vendor app captures only or executes authorization, plus inquiry/completion APIs and acquirer evidence.

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
