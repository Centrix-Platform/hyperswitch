---
id: "CTX-066"
title: "Isolate aggregator capacity with quotas and fair work scheduling"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "capacity-isolation"
depends_on: ["CTX-019", "CTX-029", "CTX-034", "CTX-052", "CTX-063"]
requires_one_of: []
conflict_domains: ["operations:quotas", "payment-execution-state-boundary", "payment:backpressure", "workflow:fair-scheduling"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-066: Isolate aggregator capacity with quotas and fair work scheduling

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators share gateway infrastructure, so one integration's retry storm, terminal fleet or slow acquirer must not exhaust connections and workers for every customer. Define per-aggregator and per-acquirer concurrency limits, request quotas, bounded queues and fair scheduling across synchronous admission and asynchronous recovery. Separate critical inquiry/reversal capacity from new-charge throughput so an outage cannot starve financial resolution. Rate limits are availability controls, not payment duplicate protection, and Redis loss must not open unbounded traffic by accident. Preserve stable idempotency semantics when clients receive 429 or an admitted 202 response. This ticket implements backpressure and operational policy; it does not promise fixed throughput until measured against the selected deployment and acquirer limits.

## Prerequisites and dependency outputs

- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-052](CTX-052-redis-owner-safe-payment-coordination--TODO.md) - consume its completed, reviewed deliverables: Implement short owner-safe Redis leases for payment coordination.
- [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) - consume its completed, reviewed deliverables: Authorize background jobs and constrain retry and replay behavior.


## Relevant code and ownership

Primary repository/workstream: **platform / capacity-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- [crates/scheduler/src/scheduler.rs](../crates/scheduler/src/scheduler.rs)

- `Proposed: platform/operations/quotas/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `operations:quotas`
- `payment-execution-state-boundary`
- `payment:backpressure`
- `workflow:fair-scheduling`

## Implementation plan

- [ ] Define resource budgets and priority classes for admission, recovery, webhooks and reports.
- [ ] Implement trusted-context rate/concurrency limits and bounded queues.
- [ ] Add per-acquirer bulkheads, timeout budgets and fair worker scheduling.
- [ ] Reserve capacity for inquiry/reversal and expose retry guidance.
- [ ] Publish quota configuration, usage metrics and safe degraded-mode behavior.

## Acceptance criteria

- [ ] One aggregator saturation does not consume all shared worker/database capacity.
- [ ] Recovery operations retain documented reserved capacity.
- [ ] Rejected requests clearly distinguish not-admitted from admitted/pending.
- [ ] Redis quota-store failure follows bounded safe behavior.
- [ ] Quota configuration cannot broaden ownership or bypass idempotency.

## Validation scenarios

- [ ] Load one noisy aggregator while measuring another aggregator baseline.
- [ ] Simulate one stalled acquirer and confirm healthy routes retain capacity.
- [ ] Exhaust queues and validate 429/202 and retry semantics.

## Expected deliverables

- Quota/bulkhead middleware and fair scheduling controls.
- Capacity policy and multi-aggregator load scenarios.

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
