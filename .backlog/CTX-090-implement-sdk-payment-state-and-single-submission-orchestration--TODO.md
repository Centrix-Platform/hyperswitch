---
id: "CTX-090"
title: "Implement SDK payment-state and single-submission orchestration"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "android"
component: "SDK payment workflow"
depends_on: ["CTX-051", "CTX-053", "CTX-057", "CTX-060", "CTX-061", "CTX-062", "CTX-076", "CTX-077", "CTX-083", "CTX-084", "CTX-087", "CTX-089"]
requires_one_of: []
conflict_domains: ["android-public-contract", "android/payment-orchestration", "android/public-results"]
external_inputs: ["Vendor cancellation, completion, and recovery guarantees.", "Approved gateway status mapping and host-facing UX policy for pending/unknown operations."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-090: Implement SDK payment-state and single-submission orchestration

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The SDK must coordinate terminal interaction and gateway execution without treating a local timeout, callback duplication, UI recreation, or user navigation as permission to start another charge. Define one logical payment operation with an immutable session, idempotency key, canonical business fields, terminal deployment, and configuration version. Map vendor states and gateway states explicitly, including completion-required, pending, unknown, succeeded, failed, and cancelled-before-dispatch. Distinguish a cancellation request from confirmed financial cancellation or reversal. The gateway remains authoritative for admitted financial state, while the adapter owns local hardware interaction and documented completion. Repeated calls from host code must either attach to the existing operation or fail consistently. User-facing callbacks need deterministic ordering and safe reattachment after lifecycle changes without replaying financial side effects.

## Prerequisites and dependency outputs

- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.
- [CTX-089](CTX-089-secure-explicit-intent-binder-and-aidl-partner-communication--TODO.md) - consume its completed, reviewed deliverables: Secure explicit intent, Binder, and AIDL partner communication.


## Relevant code and ownership

Primary repository/workstream: **android / SDK payment workflow**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/PaymentSession.kt (verify pinned fork)`

- `Proposed: external Android fork terminal payment state coordinator`

- `Proposed: external Android fork typed payment result API`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android-public-contract`
- `android/payment-orchestration`
- `android/public-results`

## Implementation plan

- [ ] Define the SDK state transition matrix and map gateway/vendor status semantics with explicit side-effect ownership.
- [ ] Create a single-submission coordinator that freezes session, operation ID, idempotency key, business fingerprint, and configuration before dispatch.
- [ ] Deduplicate host calls, transport callbacks, and vendor callbacks and support observer reattachment without resubmission.
- [ ] Implement cancellation and terminal-completion handoffs separately from financial reversal/capture endpoints.
- [ ] Expose typed Kotlin/Java result streams/callbacks with safe operation references and explicit pending/unknown recovery instructions.

## Acceptance criteria

- [ ] One logical operation cannot produce multiple authorization submissions through concurrent host calls or duplicate callbacks.
- [ ] Timeouts after possible dispatch produce pending/unknown and preserve original correlation.
- [ ] Cancelled UI state cannot be misreported as confirmed financial reversal.
- [ ] Reattached observers receive consistent authoritative state without triggering payment initiation.
- [ ] Illegal state transitions fail safely and emit redacted diagnostic reasons.

## Validation scenarios

- [ ] Invoke confirmation concurrently and replay both HTTP and vendor callbacks.
- [ ] Rotate the device, detach observers, and recreate host activities during each state.
- [ ] Timeout before dispatch, during dispatch, and after approval but before response delivery.
- [ ] Request cancellation before capture, after dispatch, and after approval.

## Expected deliverables

- SDK payment state machine and coordinator
- Public status/result mapping documentation
- Single-submission/lifecycle conformance evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Vendor cancellation, completion, and recovery guarantees.
- [ ] Approved gateway status mapping and host-facing UX policy for pending/unknown operations.

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
