---
id: "CTX-008"
title: "Define sandbox/live cells, data residency and home-region ownership"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "infrastructure"
depends_on: ["CTX-001", "CTX-002", "CTX-003"]
requires_one_of: []
conflict_domains: ["cell-placement", "payment-execution-state-boundary", "payment-state-authority"]
external_inputs: ["Chosen infrastructure regions and business-approved data residency/RPO/RTO targets."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-008: Define sandbox/live cells, data residency and home-region ownership

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

An infrastructure Tenant can partition schemas, accounts storage, Redis prefixes and analytics databases, but it does not grant global operator authority or isolate every public resource by itself. Decide how platform environments and deployment cells map to infrastructure tenants and canonical aggregators. Sandbox and live credentials, data, callbacks and device configurations must not be interchangeable. Payments need a single home-region writer with a controlled failover protocol; independently active writers backed only by asynchronously replicated locks are unsafe. This ticket defines the placement and failure model that PostgreSQL, routing, ingress and later regional recovery implement. Treat residency and recovery targets as explicit business decisions rather than promises inferred from the infrastructure vendor.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **platform / infrastructure**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_interfaces/src/configs.rs](../crates/hyperswitch_interfaces/src/configs.rs)

- [crates/router/src/configs/settings.rs](../crates/router/src/configs/settings.rs)

- [crates/storage_impl/src/lib.rs](../crates/storage_impl/src/lib.rs)

- [config](../config)

- `Proposed: docs/architecture/environment-cells.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `cell-placement`
- `payment-execution-state-boundary`
- `payment-state-authority`

## Implementation plan

- [ ] Define environment/cell/tenant/aggregator relationships and immutable placement identifiers.
- [ ] Specify sandbox/live data, secret, device, API audience, webhook and analytics separation.
- [ ] Assign payment/aggregator home-region authority and the conditions for writer failover.
- [ ] Document residency, backup location, RPO/RTO targets and dependencies for the selected pilot.
- [ ] Specify global operator read aggregation without a client-controlled cross-tenant bypass.

## Acceptance criteria

- [ ] A placement matrix covers PostgreSQL/accounts storage, Redis, analytics, objects and secrets.
- [ ] Sandbox artifacts and credentials fail when presented to live audiences or endpoints.
- [ ] Exactly one write authority exists for a payment during normal operation and controlled failover.
- [ ] Recovery/data residency targets have an explicit owner and no unsupported zero-loss claim.
- [ ] Platform-wide visibility remains a separately authenticated control-plane capability.

## Validation scenarios

- [ ] Walk through a sandbox token against live ingress and confirm the design denies it.
- [ ] Tabletop a home-region outage with an in-flight authorization and delayed callback.
- [ ] Map tenant settings to every backing store and identify missing isolation namespaces.

## Expected deliverables

- Environment/cell placement ADR
- Home-region failover authority design
- Residency and recovery target register

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Chosen infrastructure regions and business-approved data residency/RPO/RTO targets.

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
