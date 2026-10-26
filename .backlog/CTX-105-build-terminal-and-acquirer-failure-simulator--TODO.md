---
id: "CTX-105"
title: "Build terminal and acquirer simulators with financial failure modes"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Terminal/acquirer simulator"
depends_on: ["CTX-017", "CTX-050", "CTX-051", "CTX-056", "CTX-057", "CTX-058", "CTX-062", "CTX-065", "CTX-076", "CTX-077", "CTX-090", "CTX-091"]
requires_one_of: []
conflict_domains: ["testing/acquirer-simulator", "testing/terminal-simulator"]
external_inputs: ["Selected vendor/acquirer safe protocol examples and permitted synthetic payload specifications.", "Expected downstream duplicate/inquiry/reversal semantics to model explicitly."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-105: Build terminal and acquirer simulators with financial failure modes

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Agents need deterministic integration environments before hardware labs and external certification are available. Extend the platform simulator harness with a terminal adapter fake and acquirer protocol simulator that share original operation correlation and realistic failure timing. Simulate approval, decline, uncertain delivery, callback duplication/reordering, inquiry resolution, terminal completion, issuer-script failure, reversal, and settlement mismatch. Model downstream duplicate behavior explicitly; a transaction reference alone must not imply acquirer deduplication. Use synthetic opaque payloads and clearly label simulator-only formats so no one treats them as production cryptography or certification fixtures. Scenarios should be seedable and produce inspectable safe traces and financial side-effect counts. The simulator supports orchestration and idempotency validation but cannot replace named vendor wire-format tests or formal approval.

## Prerequisites and dependency outputs

- [CTX-017](CTX-017-build-synthetic-fixtures-and-acquirer-fault-harness--TODO.md) - consume its completed, reviewed deliverables: Build synthetic tenant fixtures and an acquirer fault-injection harness.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-058](CTX-058-authenticated-acquirer-notification-inbox--TODO.md) - consume its completed, reviewed deliverables: Authenticate and deduplicate inbound acquirer notifications.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal/acquirer simulator**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform terminal/acquirer simulator harness`

- `Proposed: external Android fork fake terminal adapter scenarios`

- `Proposed: synthetic settlement and financial failure fixtures`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `testing/acquirer-simulator`
- `testing/terminal-simulator`

## Implementation plan

- [ ] Define versioned scenario fixtures and a controllable clock/fault schedule across terminal, gateway, and acquirer boundaries.
- [ ] Implement fake terminal capture/completion/recovery behavior conforming to the adapter API.
- [ ] Implement acquirer authorization/inquiry/callback/reversal behavior with configurable duplicate semantics and reference retention.
- [ ] Generate safe transaction/settlement fixtures, delayed/duplicate events, and explicit side-effect counters.
- [ ] Integrate deterministic scenarios into SDK/server contract and failure-gate pipelines with clear simulator-only labeling.

## Acceptance criteria

- [ ] Scenarios reproduce dispatch-before-crash and response-lost unknown outcomes deterministically.
- [ ] Tests can prove authorization counts independently from SDK callback counts.
- [ ] Duplicate semantics are scenario-configured rather than assumed from reference presence.
- [ ] Terminal completion and reconciliation mismatch paths are supported.
- [ ] Simulator data contains no real cardholder, PIN, or production cryptographic material.

## Validation scenarios

- [ ] Run success, decline, timeout-before-dispatch, timeout-after-approval, and callback-first scenarios.
- [ ] Disable simulated downstream deduplication and verify gateway recovery avoids blind resubmission.
- [ ] Duplicate/reorder callbacks and completion acknowledgments.
- [ ] Generate a settlement discrepancy and verify the reconciliation workflow identifies it.

## Expected deliverables

- Deterministic terminal/acquirer simulator modules
- Versioned financial failure scenario library
- SDK/server integration harness and side-effect reports

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Selected vendor/acquirer safe protocol examples and permitted synthetic payload specifications.
- [ ] Expected downstream duplicate/inquiry/reversal semantics to model explicitly.

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
