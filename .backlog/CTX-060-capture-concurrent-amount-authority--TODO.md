---
id: "CTX-060"
title: "Enforce capture limits and concurrent partial-capture safety"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "capture-safety"
depends_on: ["CTX-027", "CTX-049", "CTX-053", "CTX-055", "CTX-056"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:amount-reservations", "payment:capture"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-060: Enforce capture limits and concurrent partial-capture safety

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Authorization and capture are distinct financial operations whose availability depends on terminal/acquirer capabilities. Define capture authority against the original payment's authorized amount, currency, account and route, including partial and final capture semantics. Concurrent requests with different idempotency keys must not over-consume the remaining capturable amount; reserve and release amount authority using short transactional conditional updates. UNKNOWN captures retain their reservation until resolved, because a timeout may already have moved money. Native capture code should execute through the port, not become a second independent amount ledger. Explicitly reject unsupported partial capture or overcapture rather than inheriting permissive profile defaults. This ticket excludes balances accounting and covers operation-specific downstream references and idempotency.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.


## Relevant code and ownership

Primary repository/workstream: **platform / capture-safety**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments/operations/payment_capture.rs](../crates/router/src/core/payments/operations/payment_capture.rs)

- [crates/router/src/core/payments/gateway/capture_gateway.rs](../crates/router/src/core/payments/gateway/capture_gateway.rs)

- [crates/diesel_models/src/capture.rs](../crates/diesel_models/src/capture.rs)

- `Proposed: platform/payments/capture/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:amount-reservations`
- `payment:capture`

## Implementation plan

- [ ] Define capturable amount invariant and capability rules for pilot network.
- [ ] Implement scoped capture endpoint and durable amount reservation.
- [ ] Route capture through original snapshot and executor capability contract.
- [ ] Resolve success/failure/UNKNOWN reservations through controlled transitions.
- [ ] Add capture-specific duplicate and final-capture semantics.

## Acceptance criteria

- [ ] Sum of successful plus unresolved reserved captures cannot exceed permitted authority.
- [ ] Concurrent distinct-key captures cannot overcapture.
- [ ] UNKNOWN capture cannot release its reservation optimistically.
- [ ] Capture retains original currency, account and payment ownership.
- [ ] Unsupported partial/final/overcapture modes fail before dispatch.

## Validation scenarios

- [ ] Race multiple partial captures at the remaining amount boundary.
- [ ] Lose an acquirer capture response and resolve by inquiry.
- [ ] Replay a capture key and attempt another aggregator payment ID.

## Expected deliverables

- Capture workflow and amount-reservation implementation.
- Capture capability contract and concurrency tests.

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
