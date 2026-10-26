---
id: "CTX-125"
title: "Implement data lifecycle, privacy and account-closure workflows"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Data governance"
depends_on: ["CTX-001", "CTX-009", "CTX-012", "CTX-033", "CTX-035", "CTX-046", "CTX-064", "CTX-065", "CTX-069", "CTX-124"]
requires_one_of: []
conflict_domains: ["account-closure", "backup-policy", "data-retention"]
external_inputs: ["Qualified privacy/legal, acquirer and PCI policy input for jurisdictions/data flows actually selected; retention periods must not be invented by implementation agents."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-125: Implement data lifecycle, privacy and account-closure workflows

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform stores legal-entity documents, identities, terminal evidence, transaction records, exports and audit data with different purposes and retention requirements. Closing an aggregator or merchant must revoke authority and disable processing while preserving records that must remain available for reconciliation, dispute handling or lawful retention. Do not promise instantaneous deletion from immutable backups or erase accounting evidence blindly. Define deletion/anonymization and legal-hold behavior per data class with qualified policy input. Sensitive authentication data must not acquire a retention exception merely because it is encrypted or convenient for debugging. This ticket implements approved lifecycle controls across PostgreSQL, Redis, analytics, object storage and downstream projections, including restore-time suppression of data previously scheduled for deletion.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-033](CTX-033-submerchant-customer-vault-ownership--TODO.md) - consume its completed, reviewed deliverables: Isolate submerchant customer vault and mandate access or reject those features.
- [CTX-035](CTX-035-analytics-search-report-isolation--TODO.md) - consume its completed, reviewed deliverables: Enforce aggregator and merchant scope in analytics and reporting.
- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) - consume its completed, reviewed deliverables: Implement immutable administrative and privileged access auditing.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Data governance**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/user.rs](../crates/diesel_models/src/user.rs)

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- `Proposed: services/data-lifecycle/`

- `Proposed: docs/security/data-retention.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `account-closure`
- `backup-policy`
- `data-retention`

## Implementation plan

- [ ] Create a data inventory with owner, purpose, classification, retention trigger, lawful basis/policy reference and permitted deletion/anonymization method.
- [ ] Implement account closure sequencing: revoke users/keys/sessions, suspend new processing, resolve obligations and disable projections/terminal authority.
- [ ] Build idempotent retention jobs and privacy request tracking across operational databases, analytics, caches, documents, exports and vendor integrations.
- [ ] Implement legal holds with authorized creation/removal and clear precedence over ordinary deletion for retainable data.
- [ ] Define backup expiry, restored-data tombstone/suppression reconciliation and controlled evidence of eventual deletion.
- [ ] Verify prohibited sensitive authentication data is neither persisted nor included in ordinary backups/logs/queues, and publish operator handling guidance.

## Acceptance criteria

- [ ] Each stored data class has an approved retention/deletion policy and accountable owner.
- [ ] Closure blocks new authorized processing and revokes relevant authority without corrupting outstanding payment/reconciliation history.
- [ ] Retention jobs are scoped, restartable and produce auditable evidence across all configured stores.
- [ ] Legal holds prevent eligible deletion and are themselves authorized/audited.
- [ ] Restore procedures reapply deletion/closure state before restored services expose data.
- [ ] No policy grants post-authorization retention of prohibited SAD or treats encryption as permission to retain it.

## Validation scenarios

- [ ] Run merchant/aggregator closure with pending and UNKNOWN operations in a synthetic environment.
- [ ] Exercise retention expiry, duplicate jobs, legal holds and cross-tenant privacy requests across all stores.
- [ ] Restore a controlled backup and verify tombstone replay, access revocation and data suppression before serving traffic.

## Expected deliverables

- Data inventory and approved retention matrix.
- Closure/privacy/retention automation and legal-hold controls.
- Backup-aware deletion and restore verification evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Qualified privacy/legal, acquirer and PCI policy input for jurisdictions/data flows actually selected; retention periods must not be invented by implementation agents.

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
