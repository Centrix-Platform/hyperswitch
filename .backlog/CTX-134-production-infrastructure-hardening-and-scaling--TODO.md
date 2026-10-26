---
id: "CTX-134"
title: "Implement production IaC, segmentation and resilient runtime configuration"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "infra"
component: "Production infrastructure"
depends_on: ["CTX-008", "CTX-009", "CTX-010", "CTX-011", "CTX-015", "CTX-016", "CTX-030", "CTX-031", "CTX-034", "CTX-044", "CTX-063", "CTX-066", "CTX-067", "CTX-070"]
requires_one_of: []
conflict_domains: ["database-runtime", "network-segmentation", "platform-iac", "tenancy-storage-boundary"]
external_inputs: ["Chosen cloud/runtime/provider accounts, regions, approved domains, network/acquirer connectivity and service sizing targets. Production application requires a separately approved change/release gate."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-134: Implement production IaC, segmentation and resilient runtime configuration

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Production deployment needs explicit security and failure boundaries for public ingress, portal/control plane, payment execution, credential/HSM integrations and data stores. Repository Docker and TOML files are implementation inputs, not a ready production topology. Encode a supported deployment model in IaC, with separate live/sandbox cells, private databases, least-privilege service identities and one authoritative payment writer. Multi-AZ durability and scaling must preserve database pool budgets, tenant context and bounded worker concurrency. The first release should keep authoritative critical payment persistence in PostgreSQL unless the alternative RedisKv/drainer path has equivalent isolation and failure qualification. This ticket builds and validates infrastructure definitions in controlled environments; applying production changes requires the approved release/change workflow.

## Prerequisites and dependency outputs

- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) - consume its completed, reviewed deliverables: Establish SBOM, artifact signing and license provenance.
- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-030](CTX-030-transaction-local-scoped-repositories--TODO.md) - consume its completed, reviewed deliverables: Enforce transaction-local tenancy in scoped storage and pool APIs.
- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) - consume its completed, reviewed deliverables: Authorize background jobs and constrain retry and replay behavior.
- [CTX-066](CTX-066-aggregator-quotas-bulkheads-backpressure--TODO.md) - consume its completed, reviewed deliverables: Isolate aggregator capacity with quotas and fair work scheduling.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.


## Relevant code and ownership

Primary repository/workstream: **infra / Production infrastructure**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [Dockerfile](../Dockerfile)

- [config/deployments/production.toml](../config/deployments/production.toml)

- [config/deployments/sandbox.toml](../config/deployments/sandbox.toml)

- [config/deployments/README.md](../config/deployments/README.md)

- [crates/drainer/README.md](../crates/drainer/README.md)

- `Proposed: infra/production/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-runtime`
- `network-segmentation`
- `platform-iac`
- `tenancy-storage-boundary`

## Implementation plan

- [ ] Implement versioned IaC modules for network segmentation, ingress/WAF policy, private data stores, service identities, secrets and approved HSM/KMS connectivity.
- [ ] Provision managed PostgreSQL high availability/backups, Redis coordination/cache isolation and object/audit storage with encryption and restrictive access.
- [ ] Configure transaction-compatible pooling, connection budgets, RLS runtime roles, timeouts and separate migration/operator identities.
- [ ] Implement resource limits, autoscaling/backpressure and bounded worker dispatch consistent with home-region/single-writer policy.
- [ ] Restrict native admin/metrics/debug endpoints, outbound acquirer egress and infrastructure management to approved paths.
- [ ] Validate IaC plans/policies, hardened images, environment separation and rollback/recovery integration before a gated deployment.

## Acceptance criteria

- [ ] Infrastructure is reproducible from reviewed versioned definitions with documented environment parameters.
- [ ] Public ingress cannot reach private native admin, database, Redis, metrics or credential-management endpoints.
- [ ] Runtime roles cannot bypass tenant RLS and pooled connections preserve transaction-local context.
- [ ] Multi-AZ recovery/scaling respects connection and dispatch limits without creating a second writer.
- [ ] Critical authoritative payment storage follows the qualified persistence mode, with unqualified KV paths disabled.
- [ ] Secrets are referenced through approved custody mechanisms and never embedded in source or IaC outputs.

## Validation scenarios

- [ ] Run IaC format/validate/plan and policy checks with reviewed non-production parameters.
- [ ] Test network reachability/egress, role grants and environment isolation against a controlled deployment.
- [ ] Exercise scale/zone-failure conditions with payment invariants and connection-budget monitoring.

## Expected deliverables

- Production IaC modules and parameter catalog.
- Hardened runtime/network/database configuration.
- Non-production infrastructure qualification and reviewed deployment plan.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Chosen cloud/runtime/provider accounts, regions, approved domains, network/acquirer connectivity and service sizing targets. Production application requires a separately approved change/release gate.

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
