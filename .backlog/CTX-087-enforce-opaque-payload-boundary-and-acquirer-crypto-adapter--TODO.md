---
id: "CTX-087"
title: "Enforce the opaque payment-payload boundary and acquirer crypto adapter"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Payment payload and crypto boundary"
depends_on: ["CTX-009", "CTX-014", "CTX-043", "CTX-049", "CTX-050", "CTX-054", "CTX-055", "CTX-056", "CTX-076", "CTX-081", "CTX-084"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["acquirer/crypto-adapter", "android/secure-payload-model", "payment-execution-state-boundary", "payment/secure-payload-boundary"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Approved vendor/acquirer payload specification, encryption/key ownership, HSM requirements, and test vectors.", "PCI assessor/security approval of the actual deployed boundary and retention policy.", "Credential and key provisioning procedures; no production secrets should be attached to this ticket."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-087: Enforce the opaque payment-payload boundary and acquirer crypto adapter

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The preferred terminal flow keeps card and PIN capture within an approved vendor boundary and transports only an opaque token or acquirer-encrypted payload through the SDK and general gateway. Implement the exact documented payload format and crypto-domain checks for the selected integration; do not translate terminal encryption into a homegrown public-key scheme. General services must not possess decryption keys or log/persist sensitive authentication content. If the selected acquirer requires gateway-side cryptographic processing, isolate it within an explicitly assessed security boundary with approved HSM/key management and tightly scoped access, rather than claiming the gateway is out of PCI scope. Separate secure payload lifetime from durable payment history. Durable operations retain safe identifiers and references, with vendor-approved inquiry/reconciliation resolving uncertain outcomes. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Payment payload and crypto boundary**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform secure payload admission and reference store`

- `Proposed: isolated acquirer cryptographic adapter where required`

- `Proposed: external Android fork opaque payload contract integration`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `acquirer/crypto-adapter`
- `android/secure-payload-model`
- `payment-execution-state-boundary`
- `payment/secure-payload-boundary`

## Implementation plan

- [ ] Document data flow, decrypting party, key custodians, approved formats, retention boundaries, and applicable security assessment assumptions.
- [ ] Implement typed payload admission that checks format, crypto domain, terminal binding, operation identity, freshness, and size limits.
- [ ] Implement the acquirer adapter using approved token/encrypted payload transport and HSM interfaces only where the chosen contract requires them.
- [ ] Keep opaque content outside general outbox/events/logs; use tightly scoped short-lived references and defined deletion/retention behavior.
- [ ] Prevent cross-domain rerouting and provide safe inquiry/reconciliation correlation without retaining prohibited authentication data.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] General gateway services cannot retrieve private decryption keys.
- [ ] Payloads cannot be routed to an incompatible acquirer or crypto domain.
- [ ] Outbox, trace, audit, and database records contain only permitted safe references and metadata.
- [ ] Selected vendor/acquirer fixtures pass the exact documented wire-format checks.
- [ ] Assessment documentation accurately identifies any component that decrypts or can affect payment security.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Inspect representative log, event, cache, and database records for payload leakage.
- [ ] Send oversized, malformed, stale, wrong-domain, and wrong-binding envelopes.
- [ ] Simulate crypto/HSM adapter outage and verify no unapproved fallback.
- [ ] Resolve an unknown result after secure payload cleanup using safe transaction references.

## Expected deliverables

- Approved secure-payload data-flow and retention specification
- Acquirer crypto/payload adapter
- Boundary enforcement and wire-format evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Approved vendor/acquirer payload specification, encryption/key ownership, HSM requirements, and test vectors.
- [ ] PCI assessor/security approval of the actual deployed boundary and retention policy.
- [ ] Credential and key provisioning procedures; no production secrets should be attached to this ticket.

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
