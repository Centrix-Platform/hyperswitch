---
id: "CTX-055"
title: "Freeze eligible route and versioned processing configuration per attempt"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "route-snapshot"
depends_on: ["CTX-023", "CTX-024", "CTX-043", "CTX-049", "CTX-053", "CTX-054"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "payment-execution-state-boundary", "payment:route-selection", "schema:route-snapshot"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-055: Freeze eligible route and versioned processing configuration per attempt

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Hyperswitch supports routing configuration at merchant/profile level, but terminal processing adds certified binding and cryptographic constraints. Select only from CTX-054's eligible set and freeze the selected public binding, internal projection, account, credential version, certification bundle and policy version before dispatch. Store safe identifiers rather than secret values or raw terminal payloads. A later configuration update must affect new attempts, not mutate the route of an in-flight or UNKNOWN operation. An opaque payload encrypted for one acquirer cannot be assumed portable to another. This ticket owns route selection and snapshot persistence, not automatic financial retries. Define deterministic tie-break behavior and explain safe re-selection only before any potentially financial dispatch has occurred.

## Prerequisites and dependency outputs

- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.


## Relevant code and ownership

Primary repository/workstream: **core / route-snapshot**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments/routing.rs](../crates/router/src/core/payments/routing.rs)

- [crates/router/src/core/routing.rs](../crates/router/src/core/routing.rs)

- [crates/diesel_models/src/routing_algorithm.rs](../crates/diesel_models/src/routing_algorithm.rs)

- `Proposed: platform/payments/routing/`

- [crates/router/src/core/payments/retry.rs](../crates/router/src/core/payments/retry.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `payment-execution-state-boundary`
- `payment:route-selection`
- `schema:route-snapshot`

## Implementation plan

- [ ] Adapt routing input to the constrained eligible connector set.
- [ ] Define immutable snapshot schema and exact credential/configuration version references.
- [ ] Persist selection atomically with the attempt dispatch readiness.
- [ ] Pin executor invocation and later inquiry/refund/reversal to original snapshot.
- [ ] Reject incompatible encrypted-payload fallback and record safe decision reasons.
- [ ] Inventory native automatic, manual, clear-PAN and connector-expansion retry paths; disable them for terminal flows unless an explicitly approved policy preserves the same authorization owner, certified binding, original reference and documented acquirer duplicate semantics.

## Acceptance criteria

- [ ] Every dispatched attempt has one complete immutable route snapshot.
- [ ] Configuration changes do not alter existing attempt routing.
- [ ] Snapshots contain references only, with no credentials or SAD.
- [ ] UNKNOWN attempts cannot be routed to another acquirer automatically.
- [ ] Route ranking is deterministic for the same policy/input version.
- [ ] Native retry configuration cannot bypass UNKNOWN handling, frozen certification/crypto-domain constraints or the single financial-dispatch policy; a timeout never silently starts a new connector attempt.

## Validation scenarios

- [ ] Change routing and credentials during an in-flight attempt.
- [ ] Submit payload encrypted for a different key domain and reject fallback.
- [ ] Reconstruct original inquiry/refund route after current configuration removal.

## Expected deliverables

- Route-selection adapter and snapshot schema.
- Frozen-route regression fixtures and operational explanation fields.

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
