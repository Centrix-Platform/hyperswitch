---
id: "CTX-133"
title: "Define licensed aggregator responsibilities and direct-settlement readiness"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "platform"
component: "Commercial and regulatory operating model"
depends_on: ["CTX-001", "CTX-002", "CTX-013", "CTX-014", "CTX-045", "CTX-048", "CTX-064", "CTX-065"]
requires_one_of: []
conflict_domains: ["aggregator-onboarding-policy", "operating-model"]
external_inputs: ["Intended markets and business model; qualified legal/compliance/commercial reviewers; aggregator licensing and acquirer sponsorship evidence; appropriate contract/data-processing terms."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-133: Define licensed aggregator responsibilities and direct-settlement readiness

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The customer is a licensed PayFac/aggregator, not the end merchant, but that label alone does not establish the platform's obligations or permitted funds flow. The initial architecture assumes acquirer/direct settlement and a transaction journal/reconciliation service rather than custodial balances. Document the actual roles of platform, aggregator, sub-merchant, acquirer, terminal provider and data processors for each intended market. Qualified business/legal/compliance input must determine licensing, merchant underwriting, settlement, disputes, incident notification and data-processing responsibilities; implementation agents must not invent jurisdiction rules. Convert approved decisions into aggregator onboarding and go-live prerequisites. This is a dependency for real commercial onboarding, not authorization to sign contracts, contact regulators or represent that the service is licensed.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.
- [CTX-048](CTX-048-acquirer-merchant-enrollment-adapter--TODO.md) - consume its completed, reviewed deliverables: Integrate acquirer merchant enrollment and explicit approval evidence.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.


## Relevant code and ownership

Primary repository/workstream: **platform / Commercial and regulatory operating model**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [README.md](../README.md)

- `Proposed: docs/operating-model/funds-flow.md`

- `Proposed: docs/operating-model/aggregator-readiness.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `aggregator-onboarding-policy`
- `operating-model`

## Implementation plan

- [ ] Produce an explicit funds-flow and responsibility matrix covering contracting, merchant acceptance, KYB/AML allocation, payment processing, settlement, refunds, disputes and reserves if applicable.
- [ ] Record intended countries, currencies, acquirer sponsorship/relationships and boundaries of the platform's technical-service role.
- [ ] Obtain qualified review of licensing/commercial/data-processing implications and document unresolved questions with owners.
- [ ] Define aggregator evidence/checklists for licensed status, acquirer authorization, terminal solution acceptance, support and operational readiness.
- [ ] Align API activation rules, settlement configuration and contract language with approved responsibilities.
- [ ] Define change triggers that require renewed review, including custody, balances, payouts, cross-border expansion or new acceptance channels.

## Acceptance criteria

- [ ] Approved diagrams and responsibility matrix reflect the actual proposed funds flow and selected markets.
- [ ] Required professional reviews/signoffs are recorded or remain explicit blocking external dependencies.
- [ ] Aggregator activation prerequisites are concrete and mapped to evidence and accountable reviewers.
- [ ] The direct-settlement assumption is visible and no UI/API implies unsupported custody or payouts.
- [ ] Changes that invalidate the operating model have documented reassessment triggers.
- [ ] No contracts, regulatory submissions or third-party communications occur merely by completing internal engineering artifacts.
- [ ] Dispute/chargeback response ownership and acquirer-defined deadlines/evidence/manual handoff are assigned and linked to CTX-142/143, without inventing jurisdiction-specific obligations.

## Validation scenarios

- [ ] Review responsibility allocation against onboarding, SDK, acquirer and reconciliation flows.
- [ ] Walk a sample aggregator application through the checklist and identify missing evidence.
- [ ] Have qualified business/legal/compliance owners verify conclusions and outstanding conditions.

## Expected deliverables

- Funds-flow and commercial/regulatory responsibility matrix.
- Licensed-aggregator onboarding/readiness checklist.
- Professional review register and architecture change triggers.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Intended markets and business model; qualified legal/compliance/commercial reviewers; aggregator licensing and acquirer sponsorship evidence; appropriate contract/data-processing terms.

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
