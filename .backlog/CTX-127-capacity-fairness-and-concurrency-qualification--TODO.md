---
id: "CTX-127"
title: "Qualify payment capacity, concurrency and aggregator fairness"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Performance qualification"
depends_on: ["CTX-051", "CTX-052", "CTX-053", "CTX-063", "CTX-066", "CTX-067", "CTX-070", "CTX-072", "CTX-123", "CTX-134"]
requires_one_of: []
conflict_domains: ["load-qualification", "payment-execution-state-boundary", "payment-runtime"]
external_inputs: ["Business throughput/concurrency projections, measurable SLO targets and an approved non-production load-test budget/environment."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-127: Qualify payment capacity, concurrency and aggregator fairness

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

High concurrency must preserve admission uniqueness, state correctness and fair access across aggregators under normal and degraded dependencies. A single transactions-per-second number hides database pool exhaustion, lock contention, Redis failover, analytics/export interference and acquirer latency. Extend the repository load-testing facilities with realistic payment-operation mixes and a controlled acquirer simulator. Measure API acceptance separately from final financial resolution and test bursty noisy neighbors, duplicate keys and long UNKNOWN recovery queues. Tune only after establishing workload assumptions and resource budgets. Do not benchmark against real acquirers without their explicit approved test window. Performance qualification should report sustainable headroom and safety behavior rather than claiming that a Redis lease eliminates all database deadlocks.

## Prerequisites and dependency outputs

- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-052](CTX-052-redis-owner-safe-payment-coordination--TODO.md) - consume its completed, reviewed deliverables: Implement short owner-safe Redis leases for payment coordination.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) - consume its completed, reviewed deliverables: Authorize background jobs and constrain retry and replay behavior.
- [CTX-066](CTX-066-aggregator-quotas-bulkheads-backpressure--TODO.md) - consume its completed, reviewed deliverables: Isolate aggregator capacity with quotas and fair work scheduling.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.
- [CTX-134](CTX-134-production-infrastructure-hardening-and-scaling--TODO.md) - consume its completed, reviewed deliverables: Implement production IaC, segmentation and resilient runtime configuration.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Performance qualification**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [loadtest/README.md](../loadtest/README.md)

- [loadtest/loadtest.sh](../loadtest/loadtest.sh)

- [loadtest/docker-compose.yaml](../loadtest/docker-compose.yaml)

- [config/prometheus.yaml](../config/prometheus.yaml)

- `Proposed: loadtest/platform/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `load-qualification`
- `payment-execution-state-boundary`
- `payment-runtime`

## Implementation plan

- [ ] Define workload classes, target concurrency/latency/availability, aggregator skew, duplicate rate and acquirer latency/error distributions with capacity owners.
- [ ] Build simulator-backed scenarios for admissions, duplicates, sessions, callbacks, captures/refunds, reports and reconciliation jobs.
- [ ] Exercise pool/queue limits, hot keys, Redis unavailability/failover, DB contention, slow acquirers and noisy-neighbor workloads.
- [ ] Measure admission versus completion latency, saturation, lock waits/deadlocks, lease churn, fairness and recovery lag with redacted correlated metrics.
- [ ] Tune bounded concurrency, indexing, backpressure and per-aggregator quotas without weakening durable correctness or bypassing limits.
- [ ] Publish reproducible capacity envelopes, scaling triggers and regression thresholds tied to the tested deployment.

## Acceptance criteria

- [ ] The agreed target workload meets documented admission/completion SLOs with measured headroom.
- [ ] Repeated idempotency keys under concurrency produce one admitted operation and no unjustified duplicate acquirer submission.
- [ ] One aggregator cannot exhaust shared pools/queues beyond the approved fairness policy.
- [ ] Dependency degradation applies bounded backpressure and preserves UNKNOWN/recovery semantics.
- [ ] Database lock/deadlock handling is observed and safely retried only around repeatable local transactions.
- [ ] Results identify exact artifacts, infrastructure, workload seeds and simulator assumptions.

## Validation scenarios

- [ ] Run baseline, target, burst, soak and noisy-neighbor scenarios against non-production infrastructure.
- [ ] Inject Redis, database and acquirer degradation while checking operation/journal invariants.
- [ ] Compare before/after tuning metrics and enforce agreed performance regression thresholds.

## Expected deliverables

- Load scenarios and controlled acquirer workload simulator configuration.
- Capacity/fairness qualification report.
- Scaling and saturation thresholds.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Business throughput/concurrency projections, measurable SLO targets and an approved non-production load-test budget/environment.

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
