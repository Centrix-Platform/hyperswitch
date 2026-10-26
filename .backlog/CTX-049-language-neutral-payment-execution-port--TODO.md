---
id: "CTX-049"
title: "Define payment execution port and implement the Rust compatibility adapter"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "payment-execution-port"
depends_on: ["CTX-005", "CTX-006", "CTX-018", "CTX-027", "CTX-029", "CTX-044"]
requires_one_of: []
conflict_domains: ["contracts:payment-executor", "native:execution-adapter", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-049: Define payment execution port and implement the Rust compatibility adapter

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Your public gateway should not expose Hyperswitch DTOs, connector enums or Diesel models as its permanent contract. Define a language-neutral payment execution port that lets platform admission and policy invoke the pinned Rust engine while retaining a future Kotlin implementation seam. Assign one authoritative writer to each operation and native execution field; the adapter translates status and identifiers without running a competing payment state machine. Include authorization, inquiry, capture, refund and reversal capabilities with explicit unsupported outcomes. Contract calls must propagate stable operation/attempt references and trusted ownership context. Shadow execution is prohibited for financial side effects; only side-effect-free translation or eligibility decisions may be compared during future migration. Preserve the native baseline behavior behind conformance tests.

## Prerequisites and dependency outputs

- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **core / payment-execution-port**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- [crates/api_models/src/payments.rs](../crates/api_models/src/payments.rs)

- [crates/router/src/core/refunds.rs](../crates/router/src/core/refunds.rs)

- `Proposed: contracts/internal/payment-executor/`

- `Proposed: platform/payments/executor/`

- [crates/router/src/core/payments/retry.rs](../crates/router/src/core/payments/retry.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:payment-executor`
- `native:execution-adapter`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define versioned executor commands/results and capability negotiation.
- [ ] Document state ownership and status/error translation from native execution.
- [ ] Implement Rust adapter resolving native IDs from internal mappings.
- [ ] Propagate stable operation references, deadlines and authenticated service context.
- [ ] Add conformance harness reusable by a future Kotlin executor.
- [ ] Inventory native automatic, manual, clear-PAN and connector-expansion retry paths; disable them for terminal flows unless an explicitly approved policy preserves the same authorization owner, certified binding, original reference and documented acquirer duplicate semantics.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] Public contracts contain no native model types or IDs.
- [ ] One owner is documented and enforced for each financial state transition.
- [ ] Unsupported operations return typed outcomes before financial dispatch.
- [ ] Executor retries cannot create an independent native payment accidentally.
- [ ] The baseline native flow passes through the new port.
- [ ] Native retry configuration cannot bypass UNKNOWN handling, frozen certification/crypto-domain constraints or the single financial-dispatch policy; a timeout never silently starts a new connector attempt.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Run adapter conformance against synthetic authorization/inquiry/capture/refund results.
- [ ] Inject unknown native statuses and verify safe handling.
- [ ] Assert test migration/shadow mode cannot send duplicate financial requests.

## Expected deliverables

- PaymentExecutor contract and Rust adapter.
- State ownership matrix and language-neutral conformance fixtures.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

Inputs are the actual source checkout, completed prerequisite deliverables and any explicitly required decisions above.

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
