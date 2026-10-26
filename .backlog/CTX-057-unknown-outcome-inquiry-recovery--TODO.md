---
id: "CTX-057"
title: "Resolve uncertain outcomes through inquiry and reconciliation"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "unknown-outcome-recovery"
depends_on: ["CTX-028", "CTX-053", "CTX-055", "CTX-056"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:unknown-recovery", "workflow:inquiry"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-057: Resolve uncertain outcomes through inquiry and reconciliation

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Timeouts and process crashes can occur after the acquirer has approved a payment but before the gateway records the result. UNKNOWN therefore represents a financial uncertainty, not an ordinary failure. Build recovery that uses the frozen account/credential/reference and the acquirer's documented inquiry behavior, accepts authenticated notifications and escalates unresolved cases to reconciliation or manual operations. Do not create another authorization or choose a different acquirer merely because a client retries or a worker lease expires. Define conflicting-result precedence and terminal-state correction policy with an audit trail. Expose a stable pending operation to SDKs and aggregator webhooks while recovery runs, and bound polling frequency so one outage cannot exhaust the network or processing workers.

## Prerequisites and dependency outputs

- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.


## Relevant code and ownership

Primary repository/workstream: **platform / unknown-outcome-recovery**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments/gateway/psync_gateway.rs](../crates/router/src/core/payments/gateway/psync_gateway.rs)

- [crates/router/src/core/payments/flows/psync_flow.rs](../crates/router/src/core/payments/flows/psync_flow.rs)

- `Proposed: platform/payments/recovery/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:unknown-recovery`
- `workflow:inquiry`

## Implementation plan

- [ ] Define UNKNOWN entry conditions, recovery schedule and result precedence.
- [ ] Implement original-route inquiry using immutable attempt references.
- [ ] Coordinate callback/inquiry races with conditional state transitions.
- [ ] Escalate unresolved cases with safe operator context and settlement correlation.
- [ ] Expose pending/recovered outcomes without encouraging a new charge.

## Acceptance criteria

- [ ] A timeout after simulated approval does not create a second authorization.
- [ ] Inquiry uses the original account, reference and credential version.
- [ ] Callback/inquiry races produce one coherent authoritative result.
- [ ] Unresolved operations remain visible with age and escalation status.
- [ ] Client retries return the existing uncertain operation.

## Validation scenarios

- [ ] Simulate approved-but-response-lost and declined-but-response-lost cases.
- [ ] Deliver late conflicting notifications around inquiry completion.
- [ ] Disable inquiry support and verify explicit manual/reconciliation fallback.

## Expected deliverables

- UNKNOWN recovery workflow and status contract.
- Ambiguity test scenarios and operator runbook.

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
