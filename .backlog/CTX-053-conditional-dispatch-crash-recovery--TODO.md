---
id: "CTX-053"
title: "Claim payment attempts conditionally and recover dispatch ambiguity"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "payment-dispatch"
depends_on: ["CTX-027", "CTX-028", "CTX-049", "CTX-051", "CTX-052"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:dispatch-state", "workflow:payment-worker"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-053: Claim payment attempts conditionally and recover dispatch ambiguity

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

An admitted operation is not safe to dispatch repeatedly just because a worker lease expired. Implement a durable conditional claim and attempt state machine around the executor, with stable references committed before external activity and versioned writes afterward. The platform owns dispatch policy while the native executor owns its recorded result; result ingestion must reconcile those authorities deliberately. A crash before or after the network call can leave ambiguity, so recovery must conservatively retain DISPATCHING/UNKNOWN and use inquiry or documented duplicate semantics. Database fencing prevents stale state writes but cannot stop a financial request already in flight. Keep external calls outside transactions and prohibit generic worker retries from reissuing an authorization without the recovery decision.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-052](CTX-052-redis-owner-safe-payment-coordination--TODO.md) - consume its completed, reviewed deliverables: Implement short owner-safe Redis leases for payment coordination.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-dispatch**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- [crates/diesel_models/src/payment_attempt.rs](../crates/diesel_models/src/payment_attempt.rs)

- `Proposed: platform/payments/dispatch/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:dispatch-state`
- `workflow:payment-worker`

## Implementation plan

- [ ] Define dispatch claim, attempt version/fence and legal state transitions.
- [ ] Commit attempt/reference before invoking the authenticated executor.
- [ ] Persist executor result and outbox event in short transactions.
- [ ] Classify crash/timeout windows and transition ambiguity to recovery-required state.
- [ ] Reject stale worker writes and route recovery through explicit inquiry policy.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] Only one durable attempt claim wins for a dispatchable operation.
- [ ] Stale workers cannot overwrite a newer terminal result.
- [ ] Crash recovery does not treat lease expiry as financial failure.
- [ ] No database transaction spans an acquirer/executor network call.
- [ ] Ambiguous dispatch is visible and queued for recovery without blind resubmission.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Crash before claim, after claim, during call and before result commit.
- [ ] Delay a stale worker result until a newer inquiry result arrives.
- [ ] Inject database deadlock retries and assert external action is not repeated.

## Expected deliverables

- Dispatch state machine and worker adapter.
- Crash-window matrix and stale-worker tests.

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
