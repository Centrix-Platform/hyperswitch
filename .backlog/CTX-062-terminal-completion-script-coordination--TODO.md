---
id: "CTX-062"
title: "Coordinate terminal completion issuer scripts and required reversals"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "terminal-completion"
depends_on: ["CTX-013", "CTX-049", "CTX-050", "CTX-055", "CTX-057", "CTX-061"]
requires_one_of: []
conflict_domains: ["contracts:terminal-protocol", "payment-execution-state-boundary", "payment:terminal-completion", "platform-contract-catalog"]
external_inputs: ["Pilot terminal vendor/acquirer completion, issuer-script and reversal specification"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-062: Coordinate terminal completion issuer scripts and required reversals

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A card-present flow can require terminal completion, issuer authentication data or issuer scripts after the host authorization response. Treat these as an explicit approved protocol rather than assuming an e-commerce success response finishes the transaction. Coordinate the device-bound session, original attempt, completion acknowledgement and required reversal behavior with the selected vendor/acquirer integration. SDK process death or user cancellation cannot establish that an authorization failed. Store only approved safe completion metadata and references, with strict handling of any transient sensitive payload. This ticket defines the server side and counterpart contract; terminal-vendor execution belongs to SDK adapters. Unsupported completion features must block enabling that integration rather than being silently discarded, and recovery must preserve the original route.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.


## Relevant code and ownership

Primary repository/workstream: **platform / terminal-completion**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- `Proposed: platform/payments/terminal_completion/`

- `Proposed: contracts/terminal-completion/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:terminal-protocol`
- `payment-execution-state-boundary`
- `payment:terminal-completion`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define pilot completion/script exchange and security/expiry requirements.
- [ ] Implement original-attempt completion state and device-bound acknowledgement endpoint.
- [ ] Coordinate timeout, cancellation and missing-completion inquiry/reversal rules.
- [ ] Prevent duplicate script/completion application using protocol-specific sequence identity.
- [ ] Publish SDK adapter contract and process-death recovery scenarios.

## Acceptance criteria

- [ ] Host approval is not reported as terminal-complete before required protocol steps.
- [ ] Completion messages are bound to original payment and enrolled device.
- [ ] Missing acknowledgement follows documented recovery/reversal policy.
- [ ] Duplicate completion cannot create a second financial operation.
- [ ] Sensitive transient protocol data follows approved storage and logging restrictions.

## Validation scenarios

- [ ] Kill APK after host approval and before completion acknowledgement.
- [ ] Replay scripts/completion messages and alter attempt/device IDs.
- [ ] Simulate terminal decline after host approval according to pilot protocol.

## Expected deliverables

- Terminal completion server workflow and SDK contract.
- Pilot protocol recovery fixtures and data-retention rules.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot terminal vendor/acquirer completion, issuer-script and reversal specification

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
