---
id: "CTX-072"
title: "Gate releases on payment concurrency crash and failover invariants"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "payment-safety-release-gate"
depends_on: ["CTX-017", "CTX-051", "CTX-052", "CTX-053", "CTX-055", "CTX-056", "CTX-057", "CTX-058", "CTX-060", "CTX-061", "CTX-062", "CTX-066", "CTX-067"]
requires_one_of: []
conflict_domains: ["release:financial-correctness", "tests:payment-safety"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-072: Gate releases on payment concurrency crash and failover invariants

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Payment correctness cannot be established by a happy-path unit test or an assertion that Redis acquired a lock. Build deterministic integration and fault-injection scenarios around durable admission, native execution and the pilot acquirer simulator. Crash workers and interrupt networks at documented dispatch boundaries, duplicate callbacks, expire leases, rotate credentials and fail over only under controlled writer authority. Assert business invariants: one admitted scoped operation, no blind resubmission after ambiguity, bounded capture/refund authority and preserved original-route recovery. Do not claim exactly-once network delivery; measure the gateway's decisions and downstream effects under the simulator's documented duplicate behavior. This ticket produces a repeatable release gate and failure evidence suitable for implementation by independent agents.

## Prerequisites and dependency outputs

- [CTX-017](CTX-017-build-synthetic-fixtures-and-acquirer-fault-harness--TODO.md) - consume its completed, reviewed deliverables: Build synthetic tenant fixtures and an acquirer fault-injection harness.
- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-052](CTX-052-redis-owner-safe-payment-coordination--TODO.md) - consume its completed, reviewed deliverables: Implement short owner-safe Redis leases for payment coordination.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-058](CTX-058-authenticated-acquirer-notification-inbox--TODO.md) - consume its completed, reviewed deliverables: Authenticate and deduplicate inbound acquirer notifications.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-066](CTX-066-aggregator-quotas-bulkheads-backpressure--TODO.md) - consume its completed, reviewed deliverables: Isolate aggregator capacity with quotas and fair work scheduling.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-safety-release-gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- `Proposed: platform/tests/payment_safety/`

- `Proposed: platform/tests/acquirer_simulator/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `release:financial-correctness`
- `tests:payment-safety`

## Implementation plan

- [ ] Encode invariant checks against operation, attempt, journal and simulator records.
- [ ] Add deterministic crash hooks around claim/call/result-commit boundaries.
- [ ] Exercise same/different-key concurrency, callback races and Redis loss.
- [ ] Test capture/refund reservations and home-region failover fencing.
- [ ] Publish failure seeds, timing traces and required remediation links.

## Acceptance criteria

- [ ] Equivalent concurrent retries create one admitted business operation.
- [ ] Approved-but-response-lost cases never trigger blind second authorization.
- [ ] Stale workers cannot overwrite newer results.
- [ ] Concurrent amount operations respect authorized/refundable limits.
- [ ] Unsafe split-brain promotion is rejected and original-route recovery remains intact.
- [ ] Native automatic, manual and clear-PAN retry paths are exercised explicitly; the number of upstream financial actions matches the approved owner/reference policy under every timeout/crash case.

## Validation scenarios

- [ ] Run seeded fault matrix repeatedly with bounded runtime.
- [ ] Verify a deliberately unsafe retry implementation is detected.
- [ ] Compare native/external effects and durable records after every injected crash.
- [ ] Enable adversarial native automatic/manual/clear-PAN retry settings and prove terminal admission/execution overrides prevent hidden new authorization or connector expansion after ambiguity.

## Expected deliverables

- Payment safety fault suite and invariant checker.
- CI release gate and crash-window evidence report.

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
