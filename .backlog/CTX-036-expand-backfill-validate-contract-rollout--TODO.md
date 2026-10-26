---
id: "CTX-036"
title: "Stage canonical and native tenancy migrations safely"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "tenancy-migrations"
depends_on: ["CTX-019", "CTX-021", "CTX-026", "CTX-027", "CTX-031", "CTX-032"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "release:tenancy-rollout", "schema:migration-order"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-036: Stage canonical and native tenancy migrations safely

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The proposed domain overlay and native isolation changes affect both existing data and runtime query behavior. Do not add mandatory ownership fields, enable deny-by-default policies or drop compatibility paths in one deployment. Design an expand/backfill/validate/contract sequence with one authoritative writer per ownership field and explicit readiness checks. Backfill native mappings from verified account relationships; ambiguous records must be quarantined for review rather than assigned to a guessed default aggregator or profile. Account for v1 feature selection, large indexes, replica lag, lock duration, deployment rollback and event consumers reading old envelopes. The migration plan must preserve financial records and duplicate-protection history even if application binaries are rolled back. Destructive cleanup is a separately gated final step.

## Prerequisites and dependency outputs

- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / tenancy-migrations**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/schema.rs](../crates/diesel_models/src/schema.rs)

- [crates/diesel_models/src/schema_v2.rs](../crates/diesel_models/src/schema_v2.rs)

- `Proposed: platform/migrations/`

- `Proposed: platform/operations/tenancy-rollout/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `release:tenancy-rollout`
- `schema:migration-order`

## Implementation plan

- [ ] Create ordered migration manifest with compatibility windows and owner assignments.
- [ ] Implement resumable bounded backfill jobs and ambiguity quarantine reports.
- [ ] Add validation queries for orphaned mappings, duplicates and foreign ownership.
- [ ] Stage constraints/policies behind readiness gates and measure lock impact.
- [ ] Document forward-fix and rollback procedures without deleting payment history.

## Acceptance criteria

- [ ] Old and new binaries coexist through the documented expansion window.
- [ ] Backfill resumes from checkpoints without duplicate or guessed ownership.
- [ ] Policy activation is blocked until coverage and integrity checks pass.
- [ ] Rollback preserves admitted operations and native mapping history.
- [ ] Constraint/index rollout meets agreed lock and latency limits.

## Validation scenarios

- [ ] Rehearse against a production-shaped sanitized snapshot.
- [ ] Interrupt backfill and resume from checkpoint.
- [ ] Rollback application version between each migration stage and run the baseline flow.

## Expected deliverables

- Ordered migration/backfill tooling.
- Readiness queries and rollback/forward-fix runbook.

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
