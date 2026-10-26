---
id: "CTX-074"
title: "Rehearse tenancy migration rollback and financial recovery"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "tenancy-rollout-rehearsal"
depends_on: ["CTX-015", "CTX-018", "CTX-036", "CTX-057", "CTX-064", "CTX-065", "CTX-067", "CTX-071", "CTX-072", "CTX-073"]
requires_one_of: []
conflict_domains: ["operations:recovery", "release:migration-rehearsal"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-074: Rehearse tenancy migration rollback and financial recovery

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Before introducing live aggregators, demonstrate that the tenancy migration and recovery procedures work against production-shaped sanitized data. Combine expand/backfill/validate/contract stages with runtime policy activation, baseline native compatibility, restoration and controlled writer promotion. Verify that rollback never deletes payment operation reservations, journal evidence, native mappings or unresolved financial obligations. An application rollback is not permission to restore a stale database over newer acquirer activity. Document how operators reconcile any interval between restored storage and external financial truth, including UNKNOWN inquiry and settlement import. This ticket is a rehearsal and evidence gate, not an instruction to run destructive operations against production. Use isolated infrastructure and record measured recovery and lock/latency behavior.

## Prerequisites and dependency outputs

- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.
- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.
- [CTX-036](CTX-036-expand-backfill-validate-contract-rollout--TODO.md) - consume its completed, reviewed deliverables: Stage canonical and native tenancy migrations safely.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-071](CTX-071-cross-aggregator-isolation-release-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on adversarial ownership and privilege isolation.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.


## Relevant code and ownership

Primary repository/workstream: **platform / tenancy-rollout-rehearsal**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/storage_impl/src/database/store.rs](../crates/storage_impl/src/database/store.rs)

- `Proposed: platform/operations/rehearsals/`

- `Proposed: platform/tests/migration_recovery/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `operations:recovery`
- `release:migration-rehearsal`

## Implementation plan

- [ ] Build an isolated sanitized rehearsal dataset with ambiguous and incomplete mappings.
- [ ] Execute migration stages and readiness queries under representative load.
- [ ] Practice application rollback and forward-fix with preserved payment history.
- [ ] Restore backup into isolated cell and reconcile post-snapshot external activity.
- [ ] Record measured objectives, abort conditions and final rollout decision evidence.

## Acceptance criteria

- [ ] Backfill ambiguity is quarantined rather than guessed.
- [ ] Baseline and isolation suites pass before and after policy activation.
- [ ] Rollback preserves duplicate protection and UNKNOWN recovery context.
- [ ] Restore procedure identifies and reconciles external activity beyond the snapshot.
- [ ] Measured lock impact and recovery objectives meet the declared rollout criteria.

## Validation scenarios

- [ ] Interrupt migration and restore from checkpoint.
- [ ] Rehearse stale-backup recovery with simulator activity after snapshot.
- [ ] Run old/new binaries during compatibility window and verify ownership/state invariants.

## Expected deliverables

- Rehearsal automation and measured evidence report.
- Final migration/rollback/restore runbook with abort criteria.

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
