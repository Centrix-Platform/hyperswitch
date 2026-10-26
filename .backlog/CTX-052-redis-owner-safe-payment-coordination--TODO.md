---
id: "CTX-052"
title: "Implement short owner-safe Redis leases for payment coordination"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "core"
component: "payment-coordination"
depends_on: ["CTX-027", "CTX-034", "CTX-051"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:coordination", "redis:payment-leases"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-052: Implement short owner-safe Redis leases for payment coordination

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The native API locking module uses Redis keys to coordinate requests, but a lock is not a durable financial operation record. Introduce a focused coordination adapter using short leases with random ownership values and atomic compare-and-renew/release behavior. A lost lease can reduce coalescing but must never authorize a second charge; PostgreSQL admission remains authoritative. Define how duplicate callers poll or receive an existing operation reference, and avoid holding database transactions while waiting on a lease or acquirer. Handle lease expiry, owner crashes, Redis failover and unavailable Redis explicitly. This ticket optimizes contention and caching only, rather than claiming distributed locks provide exactly-once acquirer execution or eliminate all database deadlocks.

## Prerequisites and dependency outputs

- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.


## Relevant code and ownership

Primary repository/workstream: **core / payment-coordination**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- [crates/storage_impl/src/redis.rs](../crates/storage_impl/src/redis.rs)

- `Proposed: platform/payments/coordination/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:coordination`
- `redis:payment-leases`

## Implementation plan

- [ ] Define trusted scoped lease keys, ownership tokens and bounded TTLs.
- [ ] Implement atomic acquire, owner-checked renewal and owner-checked release.
- [ ] Integrate duplicate coalescing and safe result-cache reads with durable admission.
- [ ] Specify unavailable Redis behavior and bounded wait/backoff.
- [ ] Add metrics for contention, lease loss and coordination degradation.

## Acceptance criteria

- [ ] A stale owner cannot release or renew a successor lease.
- [ ] Lease expiry never independently triggers financial redispatch.
- [ ] No database transaction is held while waiting on Redis coordination.
- [ ] Redis outage behavior preserves durable duplicate safety.
- [ ] Cached responses are scoped, safe and non-authoritative for operation ownership.

## Validation scenarios

- [ ] Pause owner past TTL then acquire with another owner and test stale release.
- [ ] Fail over/flush Redis during concurrent requests.
- [ ] Disable Redis and confirm the durable admission invariant still holds.

## Expected deliverables

- Owner-safe Redis lease adapter and coordination policy.
- Redis fault/concurrency tests and operational metrics.

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
