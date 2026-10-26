---
id: "CTX-015"
title: "Provision baseline PostgreSQL, Redis, pooling and backup infrastructure"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "infra"
component: "infrastructure"
depends_on: ["CTX-007", "CTX-008", "CTX-009"]
requires_one_of: []
conflict_domains: ["database-role-policy", "infra-storage"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-015: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform uses PostgreSQL as authoritative payment admission/state storage and Redis for coordination, caches and limits. Establish explicit durability, availability and connection-pooling configurations before application agents assume they exist. The core supports payment and accounts pools plus optional KV storage paths, so deployment configuration must document what is authoritative and which runtime roles own access. Use non-owner application database roles compatible with RLS; keep migration/admin privileges separate. Connection budgets must account for gateway instances and workers to avoid exhausting the database under peak load. This ticket creates baseline infrastructure definitions and non-production evidence; production hardening, capacity qualification and recovery drills remain independent later gates.

## Prerequisites and dependency outputs

- [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) - consume its completed, reviewed deliverables: Establish a reproducible, isolated local development stack.
- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.


## Relevant code and ownership

Primary repository/workstream: **infra / infrastructure**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [docker-compose-development.yml](../docker-compose-development.yml)

- [crates/router/src/configs/settings.rs](../crates/router/src/configs/settings.rs)

- [crates/storage_impl/src/lib.rs](../crates/storage_impl/src/lib.rs)

- `Proposed: infra/storage`

- `Proposed: docs/operations/storage-baseline.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-role-policy`
- `infra-storage`

## Implementation plan

- [ ] Define IaC/local settings for primary/accounts PostgreSQL stores, Redis and approved pool topology.
- [ ] Create runtime/migration/operations roles with least privilege and no routine RLS bypass.
- [ ] Configure authoritative persistence, replica read policy, timeouts, connection budgets and Redis loss behavior.
- [ ] Define backups, encryption, monitoring and a non-production restore check.
- [ ] Expose versioned connection/secret references without writing secrets into tracked configuration.

## Acceptance criteria

- [ ] Infrastructure definitions identify authority and consistency behavior for each store.
- [ ] Runtime database roles are distinct from table owners, migration and global operator roles.
- [ ] Pool budgets fit a documented database connection ceiling.
- [ ] A Redis outage cannot silently change PostgreSQL financial authority.
- [ ] Backup and secret references can be restored in a controlled non-production environment.

## Validation scenarios

- [ ] Verify runtime role privileges, TLS and connection budgets against instantiated sandbox resources.
- [ ] Drop/restart Redis in a baseline smoke scenario and verify defined failure behavior.
- [ ] Restore a synthetic PostgreSQL backup and validate environment/cell identity.

## Expected deliverables

- Baseline storage/pool IaC
- Runtime role and connection budget definitions
- Sandbox backup/restore evidence

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
