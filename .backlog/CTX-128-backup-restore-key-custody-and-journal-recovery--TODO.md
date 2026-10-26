---
id: "CTX-128"
title: "Exercise backup restore and cryptographic/journal recovery"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "infra"
component: "Disaster recovery"
depends_on: ["CTX-008", "CTX-009", "CTX-064", "CTX-065", "CTX-067", "CTX-074", "CTX-125", "CTX-134"]
requires_one_of: []
conflict_domains: ["backup-recovery", "key-custody", "recovery-drills"]
external_inputs: ["Approved RPO/RTO targets; cloud/database backup and KMS/HSM capabilities; authorized isolated recovery environment and custody-role participation."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-128: Exercise backup restore and cryptographic/journal recovery

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Backups are useful only if the platform can restore correct financial state, tenant isolation and cryptographic access within agreed recovery objectives. PostgreSQL, audit/object stores, configuration registries and external key custody have different consistency and recovery behavior; Redis response caches must not become the authority for completed operations. A restore may rewind payment state while the acquirer has already processed transactions, so recovery must reconcile external effects before resubmission. Define recovery-point and recovery-time objectives with business owners, test encryption key availability separately and retain evidence of usable backups. Do not export raw HSM keys or copy production payment data into an uncontrolled drill environment. Reapply closure/deletion and credential revocation state before opening recovered services.

## Prerequisites and dependency outputs

- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-074](CTX-074-tenancy-migration-recovery-rehearsal--TODO.md) - consume its completed, reviewed deliverables: Rehearse tenancy migration rollback and financial recovery.
- [CTX-125](CTX-125-privacy-retention-closure-and-legal-holds--TODO.md) - consume its completed, reviewed deliverables: Implement data lifecycle, privacy and account-closure workflows.
- [CTX-134](CTX-134-production-infrastructure-hardening-and-scaling--TODO.md) - consume its completed, reviewed deliverables: Implement production IaC, segmentation and resilient runtime configuration.


## Relevant code and ownership

Primary repository/workstream: **infra / Disaster recovery**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [config/deployments/production.toml](../config/deployments/production.toml)

- [crates/drainer/README.md](../crates/drainer/README.md)

- `Proposed: infra/backup/`

- `Proposed: docs/operations/disaster-recovery.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `backup-recovery`
- `key-custody`
- `recovery-drills`

## Implementation plan

- [ ] Inventory authoritative stores, dependencies, retention and encryption/key recovery requirements with explicit RPO/RTO per service.
- [ ] Implement encrypted backups/PITR and protected configuration/audit/object-store recovery with least-privilege restore roles.
- [ ] Document HSM/KMS/secret-store availability, rotation and recovery procedures appropriate to each non-exportable/exportable key class.
- [ ] Restore a representative system into an isolated environment and reconcile journal, idempotency, outbox/inbox and acquirer references before permitting execution.
- [ ] Reapply account closure, legal holds, deletion suppression and revocation state from CTX-125.
- [ ] Measure achieved recovery times/data loss, automate integrity checks and record remediation for unmet objectives.

## Acceptance criteria

- [ ] A clean isolated restore recovers authoritative payment/journal/configuration state within the approved measured RPO/RTO.
- [ ] Required cryptographic operations work after recovery without unauthorized key export or weakened custody.
- [ ] Recovery does not blindly repeat attempts whose external financial outcome may already exist.
- [ ] Tenant RLS, service grants, revocations and deletion suppression hold before traffic can resume.
- [ ] Backup integrity, immutability/retention and restore access are verifiably monitored.
- [ ] The runbook identifies owners, decision points and reconciliation gates for unrecoverable or uncertain state.

## Validation scenarios

- [ ] Execute a timed restore/PITR drill with synthetic data and known payment/outbox/inbox checkpoints.
- [ ] Simulate unavailable key version, incomplete backup and clock/retention edge cases.
- [ ] Compare restored state to simulator/acquirer records and validate tenant isolation and closure tombstone replay.

## Expected deliverables

- Backup/restore and key-custody runbooks.
- Automated integrity/recovery checks.
- Measured RPO/RTO drill evidence and remediation list.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved RPO/RTO targets; cloud/database backup and KMS/HSM capabilities; authorized isolated recovery environment and custody-role participation.

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
