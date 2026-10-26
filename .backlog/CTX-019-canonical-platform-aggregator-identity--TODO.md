---
id: "CTX-019"
title: "Create canonical platform and aggregator identifiers and native mappings"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "identity-registry"
depends_on: ["CTX-002", "CTX-005", "CTX-006", "CTX-008", "CTX-015"]
requires_one_of: []
conflict_domains: ["contracts:identifiers", "database-schema-migrations", "platform-contract-catalog", "schema:identity"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-019: Create canonical platform and aggregator identifiers and native mappings

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Hyperswitch infrastructure Tenant selects schemas and service namespaces; it is not a platform administrator identity. MerchantAccount already belongs to an Organization and is the intended processing boundary for an aggregator. Introduce platform-owned identifiers and explicit mappings rather than renaming native tables or leaking native IDs into customer contracts. The canonical registry must distinguish sandbox and live environments, deployment cells, native tenant IDs, organization IDs and MerchantAccount IDs. This ticket owns identity storage and lookup semantics only; provisioning execution belongs to CTX-020. Support incomplete provisioning without exposing an active account, enforce unambiguous mappings, and preserve an audit trail when placement changes. Keep application services independent from Diesel identifier wrappers.

## Prerequisites and dependency outputs

- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) - consume its completed, reviewed deliverables: Provision baseline PostgreSQL, Redis, pooling and backup infrastructure.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / identity-registry**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/merchant_account.rs](../crates/diesel_models/src/merchant_account.rs)

- [crates/diesel_models/src/organization.rs](../crates/diesel_models/src/organization.rs)

- [crates/hyperswitch_interfaces/src/configs.rs](../crates/hyperswitch_interfaces/src/configs.rs)

- `Proposed: platform/identity/`

- `Proposed: platform/migrations/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:identifiers`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:identity`

## Implementation plan

- [ ] Define typed public platform_id and aggregator_id formats and conversion boundaries.
- [ ] Create additive platform/aggregator/mapping tables with environment and cell placement constraints.
- [ ] Implement scoped mapping repository APIs and prevent ambiguous native ownership.
- [ ] Define mapping statuses, immutable identity fields and audited placement-change rules.
- [ ] Publish mapping fixtures and update internal domain glossary.

## Acceptance criteria

- [ ] Each public aggregator resolves to exactly one active native account per declared environment placement.
- [ ] Duplicate native-account mappings in one tenant/environment are rejected.
- [ ] Sandbox identifiers cannot resolve to live configuration.
- [ ] Public serializers omit native tenant, organization and MerchantAccount IDs.
- [ ] Provisioning and suspended mappings cannot silently become active.

## Validation scenarios

- [ ] Insert duplicate and cross-environment mappings and assert constraint failures.
- [ ] Round-trip synthetic IDs through registry lookup and public serializers.
- [ ] Verify unknown or incomplete mapping returns a stable domain error.

## Expected deliverables

- Identity migrations and repository interfaces.
- Identifier contract and mapping fixtures.

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
