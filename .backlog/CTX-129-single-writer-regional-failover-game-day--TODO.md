---
id: "CTX-129"
title: "Validate single-writer regional failover and UNKNOWN-outcome recovery"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "infra"
component: "Regional resilience"
depends_on: ["CTX-008", "CTX-057", "CTX-067", "CTX-072", "CTX-128", "CTX-131", "CTX-132"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment-writer", "recovery-drills", "regional-failover"]
external_inputs: ["Approved regional topology, RPO/RTO, failover authority and controlled multi-region test infrastructure; production drills require a separately approved change window."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-129: Validate single-writer regional failover and UNKNOWN-outcome recovery

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Regional resilience must preserve one authoritative financial writer for an aggregator/payment. Promoting a replica or redirecting ingress while an old region can still reach the acquirer can duplicate side effects even when the new database is writable. The home-region and writer-fencing design must be exercised under asymmetric partitions, not only a clean shutdown. Pending and UNKNOWN operations require inquiry/reconciliation against original references after failover; database fencing cannot recall an already dispatched external request. This ticket validates the implemented control and runbooks through a controlled game day. It does not authorize production failover or acquirer traffic. Define failback, operator decision rights and conditions for staying unavailable when safety cannot be established.

## Prerequisites and dependency outputs

- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-128](CTX-128-backup-restore-key-custody-and-journal-recovery--TODO.md) - consume its completed, reviewed deliverables: Exercise backup restore and cryptographic/journal recovery.
- [CTX-131](CTX-131-payment-slos-alerts-and-operator-dashboards--TODO.md) - consume its completed, reviewed deliverables: Implement SLO dashboards and actionable payment health alerts.
- [CTX-132](CTX-132-payment-security-and-acquirer-incident-runbooks--TODO.md) - consume its completed, reviewed deliverables: Create and rehearse payment and security incident runbooks.


## Relevant code and ownership

Primary repository/workstream: **infra / Regional resilience**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [config/deployments/README.md](../config/deployments/README.md)

- [config/deployments/production.toml](../config/deployments/production.toml)

- `Proposed: infra/regional-failover/`

- `Proposed: docs/operations/region-failover.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment-writer`
- `recovery-drills`
- `regional-failover`

## Implementation plan

- [ ] Create a game-day plan for region loss, split-brain network paths, stale workers, replica lag and regional key/configuration availability.
- [ ] Verify fencing/epoch and egress/worker shutdown mechanisms prevent concurrent authoritative writers during promotion.
- [ ] Run controlled failover with in-flight operations at admission, dispatch, response-loss and UNKNOWN checkpoints using a simulator.
- [ ] Reconcile original acquirer references before retrying and demonstrate safe backlog resumption without route changes for ambiguous attempts.
- [ ] Exercise failback, rollback/abort and prolonged unavailability decisions under the approved operator policy.
- [ ] Record decision timeline, observed RPO/RTO, invariant checks and remaining gaps.

## Acceptance criteria

- [ ] At most one active writer can dispatch for the protected scope throughout the tested partition/failover scenarios.
- [ ] Stale-region workers cannot resume dispatch merely because an old lease/credential remains locally available.
- [ ] In-flight/UNKNOWN attempts recover by original references and do not create blind alternate-acquirer authorizations.
- [ ] Measured failover RPO/RTO and reconciliation delay meet the approved objectives or produce explicit blockers.
- [ ] Failback and abort procedures preserve the same safety invariants.
- [ ] Game-day evidence identifies exact topology, versions and conditions outside the tested guarantee.

## Validation scenarios

- [ ] Execute simulator-backed asymmetric partition and stale-worker scenarios in a controlled environment.
- [ ] Compare dispatch logs, acquirer simulator effects and durable journal/attempt records for uniqueness.
- [ ] Rehearse operator runbooks and alert routing, including inability-to-prove-safety stop conditions.

## Expected deliverables

- Regional failover/failback game-day plan and automation.
- Single-writer/UNKNOWN recovery evidence.
- Updated resilience runbooks and remediation tickets.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved regional topology, RPO/RTO, failover authority and controlled multi-region test infrastructure; production drills require a separately approved change window.

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
