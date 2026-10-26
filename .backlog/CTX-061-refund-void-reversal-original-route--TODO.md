---
id: "CTX-061"
title: "Implement bounded refunds voids and reversals on the original route"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "refund-void-reversal"
depends_on: ["CTX-027", "CTX-049", "CTX-053", "CTX-055", "CTX-056", "CTX-060"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:amount-reservations", "payment:refund-reversal"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-061: Implement bounded refunds voids and reversals on the original route

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Refund, void and reversal are different operations with network-specific timing, amount and reference requirements. Expose separate typed contracts and permissions, retaining original aggregator, merchant, currency, account and route attribution. Protect refundable amounts against concurrent requests using durable reservations, and retain UNKNOWN reservations until financial resolution. Reversal must correlate to the original attempted authorization even when its final status was uncertain. Native refund/void functionality is reused through the execution port after capability validation; generic routing must not choose a cheaper or newly configured acquirer. This ticket does not implement payouts or ledger balances. Define full/partial refund support, settlement cutoffs, duplicate semantics and safe treatment of merchant suspension so required recovery is still possible.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.


## Relevant code and ownership

Primary repository/workstream: **platform / refund-void-reversal**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/refunds.rs](../crates/router/src/core/refunds.rs)

- [crates/api_models/src/refunds.rs](../crates/api_models/src/refunds.rs)

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- `Proposed: platform/payments/refunds_reversals/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:amount-reservations`
- `payment:refund-reversal`

## Implementation plan

- [ ] Define operation-specific permissions, capabilities, cutoffs and original-reference requirements.
- [ ] Implement durable refund amount reservations and separate reversal/void state models.
- [ ] Invoke original-route executor with stable downstream references.
- [ ] Handle uncertain outcomes through inquiry/reconciliation without optimistic amount release.
- [ ] Publish safe errors for unsupported, excessive and unauthorized requests.

## Acceptance criteria

- [ ] Concurrent refunds cannot exceed confirmed refundable authority.
- [ ] Refund/void/reversal never use a newly ranked processing route.
- [ ] UNKNOWN results retain required reservations and recovery context.
- [ ] Foreign merchant/payment references are denied.
- [ ] Suspension policy explicitly permits or denies each recovery operation without losing obligations.

## Validation scenarios

- [ ] Race partial refunds and replay identical/different operation keys.
- [ ] Timeout reversal/void and recover using original transaction references.
- [ ] Change routing then refund an older payment and inspect selected account.

## Expected deliverables

- Refund/void/reversal workflows and amount invariants.
- Operation contracts and original-route tests.

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
