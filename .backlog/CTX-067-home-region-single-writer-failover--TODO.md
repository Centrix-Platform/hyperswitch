---
id: "CTX-067"
title: "Enforce home-region authority and controlled writer failover"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "regional-writer-authority"
depends_on: ["CTX-008", "CTX-015", "CTX-019", "CTX-027", "CTX-044", "CTX-053", "CTX-057"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "operations:region-authority", "payment-execution-state-boundary", "payment:single-writer", "schema:placement-epoch"]
external_inputs: ["Approved deployment topology, replication guarantees and recovery objectives"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-067: Enforce home-region authority and controlled writer failover

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Independent regional writers with eventually replicated idempotency records can admit duplicate financial operations. Establish a home region or deployment cell for each aggregator/payment and one authoritative writer for admission and state transitions. Requests reaching another region must route to that authority or fail safely. Controlled failover requires a durable authority epoch and a verified fence of the old writer; a database fence alone cannot cancel already-running acquirer requests. Define promotion prerequisites, replication/data-loss assumptions and treatment of in-flight UNKNOWN attempts. This ticket implements authority enforcement and recovery contracts rather than speculative active-active payments. If the platform chooses stronger multi-region consensus later, it must preserve the same business invariants and explicitly revisit availability/latency tradeoffs.

## Prerequisites and dependency outputs

- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.


## Relevant code and ownership

Primary repository/workstream: **platform / regional-writer-authority**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_interfaces/src/configs.rs](../crates/hyperswitch_interfaces/src/configs.rs)

- `Proposed: platform/placement/`

- `Proposed: platform/operations/failover/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `operations:region-authority`
- `payment-execution-state-boundary`
- `payment:single-writer`
- `schema:placement-epoch`

## Implementation plan

- [ ] Define placement routing and durable writer authority/epoch records.
- [ ] Enforce region authority before admission, dispatch and state mutation.
- [ ] Implement controlled promotion requiring old-writer fencing and readiness checks.
- [ ] Classify in-flight attempts for conservative inquiry after failover.
- [ ] Publish failover procedure with measured RPO/RTO and split-brain abort conditions.

## Acceptance criteria

- [ ] Two regions cannot independently admit the same scoped operation.
- [ ] Non-home writer requests are routed or rejected before financial side effects.
- [ ] Promotion requires evidence the previous writer is fenced.
- [ ] In-flight pre-failover attempts remain uncertain until resolved.
- [ ] Authority epoch changes cannot rewrite original route/account references.

## Validation scenarios

- [ ] Simulate partition with old writer still running and reject unsafe promotion.
- [ ] Promote after verified fencing and replay client requests.
- [ ] Lose a response during failover and recover via original-route inquiry.

## Expected deliverables

- Home-region routing/authority guard.
- Failover runbook, epoch contract and split-brain tests.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved deployment topology, replication guarantees and recovery objectives

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
