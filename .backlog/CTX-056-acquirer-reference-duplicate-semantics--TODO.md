---
id: "CTX-056"
title: "Implement documented downstream reference and duplicate-handling rules"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "acquirer-duplicate-policy"
depends_on: ["CTX-013", "CTX-049", "CTX-050", "CTX-055"]
requires_one_of: []
conflict_domains: ["contracts:acquirer-duplicates", "payment-execution-state-boundary", "payment:downstream-reference", "platform-contract-catalog"]
external_inputs: ["Pilot acquirer reference/idempotency contract, inquiry protocol and test evidence"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-056: Implement documented downstream reference and duplicate-handling rules

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A gateway-generated request reference does not guarantee that the acquirer deduplicates a repeated authorization. For each supported operation on the pilot network, document and implement reference format, uniqueness scope, retention window, inquiry correlation and duplicate response behavior. Distinguish reference reuse for safe recovery from an unsupported retransmission or a genuinely new attempt. The platform must preserve its durable operation identity across native translation and credential rotation. Where the acquirer lacks usable deduplication or inquiry, mark recovery as manual/blocked rather than promising exactly-once effects. This ticket includes adapter conformance and certification evidence; it does not permit automatic cross-acquirer fallback after ambiguity or use a short Redis lease as downstream duplicate protection.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.


## Relevant code and ownership

Primary repository/workstream: **platform / acquirer-duplicate-policy**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_connectors/src/types.rs](../crates/hyperswitch_connectors/src/types.rs)

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- `Proposed: platform/processing/acquirer_semantics/`

- [crates/router/src/core/payments/retry.rs](../crates/router/src/core/payments/retry.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:acquirer-duplicates`
- `payment-execution-state-boundary`
- `payment:downstream-reference`
- `platform-contract-catalog`

## Implementation plan

- [ ] Create per-operation acquirer duplicate/reference capability matrix.
- [ ] Implement stable reference generation and native adapter propagation.
- [ ] Validate external length/character/sequence constraints without collisions.
- [ ] Map duplicate responses and inquiry identifiers to the original attempt.
- [ ] Define safe recovery and manual-review policy for unsupported semantics.
- [ ] Inventory native automatic, manual, clear-PAN and connector-expansion retry paths; disable them for terminal flows unless an explicitly approved policy preserves the same authorization owner, certified binding, original reference and documented acquirer duplicate semantics.

## Acceptance criteria

- [ ] Each enabled operation has documented tested downstream duplicate semantics.
- [ ] Reference scope and lifetime meet the acquirer contract.
- [ ] Adapter retries preserve the original reference where required.
- [ ] Unsupported ambiguous recovery never silently resubmits a new authorization.
- [ ] External responses are attributed to the original aggregator/attempt.
- [ ] Native retry configuration cannot bypass UNKNOWN handling, frozen certification/crypto-domain constraints or the single financial-dispatch policy; a timeout never silently starts a new connector attempt.

## Validation scenarios

- [ ] Replay approved duplicate cases against simulator and certification environment.
- [ ] Test truncation/format collision and reference-retention boundaries.
- [ ] Verify unknown semantics disable automatic retry in the adapter.

## Expected deliverables

- Acquirer reference adapter and capability matrix.
- Downstream duplicate conformance tests and evidence references.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot acquirer reference/idempotency contract, inquiry protocol and test evidence

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
