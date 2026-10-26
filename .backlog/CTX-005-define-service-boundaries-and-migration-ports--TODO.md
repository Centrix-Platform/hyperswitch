---
id: "CTX-005"
title: "Define service ownership, execution ports and the Kotlin migration boundary"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "architecture"
depends_on: ["CTX-001", "CTX-002", "CTX-003"]
requires_one_of: []
conflict_domains: ["architecture-domain-model", "payment-execution-state-boundary", "payment-state-authority", "platform-contract-catalog", "public-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-005: Define service ownership, execution ports and the Kotlin migration boundary

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform must own stable public payment and onboarding contracts while Hyperswitch initially owns execution attempts and connector results. Separate identity, merchant management, terminal management, processing configuration, payment execution and reconciliation domains before splitting deployment units. Shared mutable tables or exposing Diesel/native DTOs through public APIs would bind later Kotlin work to Rust internals. Conversely, creating a second financial state writer beside the native engine introduces races. Establish logical boundaries, canonical/native state mappings and the sole writer for each object. Service extraction can then follow operational need instead of starting with a distributed transaction between every component. Kotlin is an implementation replacement behind a contract, not a parallel live charge path.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **platform / architecture**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_domain_models/src/payments.rs](../crates/hyperswitch_domain_models/src/payments.rs)

- [crates/hyperswitch_interfaces](../crates/hyperswitch_interfaces)

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- [crates/storage_impl](../crates/storage_impl)

- `Proposed: docs/architecture/service-boundaries.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `architecture-domain-model`
- `payment-execution-state-boundary`
- `payment-state-authority`
- `platform-contract-catalog`
- `public-contracts`

## Implementation plan

- [ ] Map each domain to owned aggregates, writable schema, API/events, deployment and accountable owner.
- [ ] Define PaymentExecutor, MerchantProvisioner, TerminalRegistry and CredentialProvider ports and canonical/native ID translations.
- [ ] Document authority for operation admission, native attempts, callbacks, journal and reconciliation state.
- [ ] Select an initial deployment layout and proposed module paths without asserting those paths already exist.
- [ ] Specify extraction/migration rules: versioned contracts, outbox events, one writer, no cross-domain SQL ownership and no duplicate live side effects.

## Acceptance criteria

- [ ] A service/data ownership matrix assigns exactly one writer per aggregate.
- [ ] Public contracts do not expose Diesel types or require native connector enums.
- [ ] The Rust adapter boundary supports a later language-neutral replacement.
- [ ] Payment and native attempt state mappings explain callback and recovery ownership.
- [ ] Initial deployment decisions avoid unnecessary synchronous domain chains on the charge path.

## Validation scenarios

- [ ] Trace create/confirm/callback/reconcile and merchant provisioning across the ownership diagram.
- [ ] Review an example Kotlin executor contract without linking Rust source models.
- [ ] Identify every cross-service consistency boundary and its compensation/reconciliation owner.

## Expected deliverables

- Service/data ownership ADR
- Execution and provisioning port contracts
- State-authority and extraction map

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
