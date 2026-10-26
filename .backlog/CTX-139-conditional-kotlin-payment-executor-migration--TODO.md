---
id: "CTX-139"
title: "Plan and qualify a future Kotlin service migration without dual financial execution"
status: "TODO"
phase: 4
priority: "P2"
size: "L"
repository: "multi-repo"
component: "Conditional language migration"
depends_on: ["CTX-005", "CTX-006", "CTX-049", "CTX-055", "CTX-056", "CTX-057", "CTX-064", "CTX-067", "CTX-073", "CTX-123", "CTX-130"]
requires_one_of: []
conflict_domains: ["execution-contract", "future-kotlin-executor", "payment-execution-state-boundary", "payment-writer", "platform-contract-catalog"]
external_inputs: ["Explicit business/engineering decision to pursue migration, target Kotlin/runtime support policy and any affected acquirer/terminal requalification requirements."]
external_inputs_resolved: false
applicability: "conditional"
applicability_decision: "deferred"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-139: Plan and qualify a future Kotlin service migration without dual financial execution

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Rust-to-Kotlin migration is optional future work, not a reason to rewrite proven connector code before the platform launches. The execution port, canonical contracts and domain-owned schemas should make selected implementations replaceable without exposing Hyperswitch types to customers. Start with control-plane services or side-effect-free decisions before a financial executor. Differential/shadow testing must never send the same live authorization through both implementations. A safe cutover gives one implementation authority for new operations while preserving ownership of in-flight and UNKNOWN attempts, original references and callbacks. This ticket defines a triggered migration strategy, parity evidence and rollback constraints; actual connector rewrites require separately scoped implementation/certification work and are not blanket-authorized by the planning ticket.

## Prerequisites and dependency outputs

- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.
- [CTX-130](CTX-130-expand-contract-upgrades-and-client-deprecation--TODO.md) - consume its completed, reviewed deliverables: Implement staged upgrades, client compatibility and safe rollback.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Conditional language migration**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments/routing.rs](../crates/router/src/core/payments/routing.rs)

- [crates/api_models/Cargo.toml](../crates/api_models/Cargo.toml)

- [crates/hyperswitch_domain_models/src/routing.rs](../crates/hyperswitch_domain_models/src/routing.rs)

- `Proposed: services/kotlin-executor-prototype/`

- `Proposed: docs/architecture/kotlin-migration.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `execution-contract`
- `future-kotlin-executor`
- `payment-execution-state-boundary`
- `payment-writer`
- `platform-contract-catalog`

## Implementation plan

- [ ] Record business/technical triggers, candidate domains, parity scope and costs for Kotlin migration with an explicit proceed/defer decision.
- [ ] Implement or prototype language-neutral execution interfaces/client bindings and contract fixtures independent of Diesel/native DTOs.
- [ ] Compare Rust/Kotlin side-effect-free validation/routing outputs and simulator-backed financial behavior using deterministic fixtures.
- [ ] Design per-scope writer ownership/cutover epochs, callback routing and in-flight/UNKNOWN draining or delegation across versions.
- [ ] Define data/schema ownership migration, rollback boundaries, observability and certification/security requalification requirements.
- [ ] Produce a staged migration proposal and acceptance evidence before authorizing any real financial executor cutover.

## Acceptance criteria

- [ ] Migration remains conditional and does not block initial launch under the approved Rust architecture.
- [ ] Public contracts and canonical IDs remain compatible across implementations.
- [ ] Shadow comparison cannot dispatch duplicate live financial actions.
- [ ] Cutover/rollback design preserves one writer and ownership of in-flight/UNKNOWN attempts and original acquirer references.
- [ ] Parity gaps and certification implications are explicit rather than hidden behind matching HTTP responses.
- [ ] A proceed decision leads to separately scoped implementation work with measurable gates.

## Validation scenarios

- [ ] Run cross-language contract fixtures and side-effect-free differential tests.
- [ ] Use an acquirer simulator to exercise cutover, callback routing, stale workers and ambiguous outcomes.
- [ ] Review ownership/schema/rollback plans with payment and operations maintainers before any production proposal.

## Expected deliverables

- Conditional Kotlin migration ADR and domain candidate matrix.
- Language-neutral conformance prototype/evidence.
- Single-writer cutover and requalification plan.

## External inputs and applicability

Applicability: **conditional**. Initial decision: **deferred**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Explicit business/engineering decision to pursue migration, target Kotlin/runtime support policy and any affected acquirer/terminal requalification requirements.

Record evidence and update `external_inputs_resolved` only after these inputs are verified. Continue independent work while a necessary input is pending.

This is a deferred evolution track and is not a default initial-launch blocker. A proceed decision creates a separately reviewed execution program.

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
