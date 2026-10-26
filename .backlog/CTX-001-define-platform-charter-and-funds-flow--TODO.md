---
id: "CTX-001"
title: "Define the platform charter, pilot scope and funds flow"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "architecture"
depends_on: []
requires_one_of: []
conflict_domains: ["architecture"]
external_inputs: ["Target jurisdictions, first licensed aggregator, first terminal/acquirer and commercial responsibility owners."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-001: Define the platform charter, pilot scope and funds flow

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform serves licensed Aggregators/Payment Facilitators, each onboarding its own merchants and distributing an embedded Android SDK. It is not an end-merchant SaaS signup product. The blueprint assumes acquirers settle directly and the platform initially orchestrates payments, journals transactions and reconciles settlement rather than maintaining customer balances. Those assumptions determine onboarding responsibilities, data retention, terminal certification and which financial domains belong in the first release. Establish a written product boundary before agents create schemas or enable features inherited from Hyperswitch. Record unresolved geography, network, terminal and commercial choices as inputs with named decision owners; do not invent regulatory obligations or treat unavailable evidence as approval.

## Prerequisites and dependency outputs

This is a dependency-root ticket. Inspect the pinned source and resolve the inputs below before making implementation decisions.


## Relevant code and ownership

Primary repository/workstream: **platform / architecture**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [README.md](../README.md)

- `Proposed: docs/architecture/platform-charter.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `architecture`

## Implementation plan

- [ ] Document the three-tier customer relationship, operator roles, direct-settlement assumption and prohibited scope expansion.
- [ ] Describe authorize/capture/refund/void/reversal, terminal completion and reconciliation responsibilities across the platform, aggregator and acquirer.
- [ ] Select or record required inputs for the first aggregator/merchant/terminal/acquirer pilot and online-only processing assumptions.
- [ ] Define measurable pilot success, support boundaries and the trigger for a separate balances/ledger program.
- [ ] Record jurisdictions, data residency, licensed entity evidence and professional review ownership without drafting unsupported legal rules.
- [ ] Assign dispute/chargeback notification, evidence deadlines, acquirer handoff and loss/reconciliation responsibilities; direct settlement does not remove these responsibilities.

## Acceptance criteria

- [ ] A reviewed charter identifies the paying customer and merchant hierarchy unambiguously.
- [ ] A funds-flow diagram states who holds, settles and reconciles money at every step.
- [ ] The initial product explicitly chooses direct settlement or documents the decision that would require CTX-140.
- [ ] Each unresolved commercial or jurisdiction input has an owner and a downstream gate.
- [ ] Pilot success criteria include merchant activation, terminal binding, duplicate safety and settlement reconciliation.

## Validation scenarios

- [ ] Walk through a normal sale, an ambiguous authorization timeout and a refund against the responsibility matrix.
- [ ] Check that no portal or SDK feature implies custody or merchant underwriting outside the declared responsibility.
- [ ] Review the first pilot definition with the future owners of integration and operations.

## Expected deliverables

- Product charter and initial pilot scope
- Funds-flow and responsibility matrix
- Decision/input register

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Target jurisdictions, first licensed aggregator, first terminal/acquirer and commercial responsibility owners.

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
