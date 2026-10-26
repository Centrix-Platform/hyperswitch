---
id: "CTX-140"
title: "Define a conditional double-entry ledger and funds-movement roadmap"
status: "TODO"
phase: 4
priority: "P2"
size: "L"
repository: "platform"
component: "Conditional financial accounting"
depends_on: ["CTX-001", "CTX-005", "CTX-006", "CTX-064", "CTX-065", "CTX-067", "CTX-125", "CTX-133"]
requires_one_of: []
conflict_domains: ["funds-flow", "future-ledger", "operating-model"]
external_inputs: ["Approved future funds-flow/business scope; qualified accounting/legal/compliance review; banking/acquirer/payout relationships and jurisdiction-specific obligations before implementation."]
external_inputs_resolved: false
applicability: "conditional"
applicability_decision: "deferred"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-140: Define a conditional double-entry ledger and funds-movement roadmap

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The initial direct-settlement platform needs an immutable transaction journal and reconciliation, but it need not invent custodial balances or payout execution. If the business later owns merchant balances, fees, reserves, splits, prefunding or payouts, establish a dedicated accounting domain before exposing those features. Double-entry accounting must be designed around actual legal entities, currencies, settlement obligations and reconciliation sources; it cannot be inferred from payment statuses alone. Changing funds flow also triggers licensing/commercial/security review and likely new acquirer relationships. This conditional ticket captures decision triggers, accounting invariants and an implementation roadmap, not a production ledger implementation or authorization to move funds. Keep financial truth separate from analytics and from language migration concerns.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) - consume its completed, reviewed deliverables: Enforce home-region authority and controlled writer failover.
- [CTX-125](CTX-125-privacy-retention-closure-and-legal-holds--TODO.md) - consume its completed, reviewed deliverables: Implement data lifecycle, privacy and account-closure workflows.
- [CTX-133](CTX-133-licensed-aggregator-responsibility-and-onboarding-checklist--TODO.md) - consume its completed, reviewed deliverables: Define licensed aggregator responsibilities and direct-settlement readiness.


## Relevant code and ownership

Primary repository/workstream: **platform / Conditional financial accounting**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- `Proposed: docs/architecture/future-ledger.md`

- `Proposed: docs/operating-model/funds-flow.md`

- `Proposed: services/ledger/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `funds-flow`
- `future-ledger`
- `operating-model`

## Implementation plan

- [ ] Define explicit business triggers and required professional review for custody, balance, fee, reserve, split or payout features.
- [ ] Model legal-entity/currency-specific chart of accounts, immutable balanced postings, pending/available funds and external settlement relationships.
- [ ] Specify idempotent posting commands, reversals/corrections, reconciliation, close/reporting and audit/retention invariants.
- [ ] Design domain boundaries and event contracts with payment execution, merchant lifecycle and settlement services without shared table writes.
- [ ] Produce phased implementation tickets for ledger, fees/reserves and payout workflows only after the operating-model decision is approved.
- [ ] Document migration/reconciliation of the existing journal and prevention of duplicate payout/financial writers.

## Acceptance criteria

- [ ] The feature remains conditional and is not an initial direct-settlement launch blocker.
- [ ] Business/legal/accounting triggers and responsibility changes are documented with accountable reviewers.
- [ ] Proposed postings balance per defined legal entity/currency and cannot be mutated to rewrite history.
- [ ] Payment status changes alone cannot create unsupported available balances or duplicate external payouts.
- [ ] Reconciliation and reversal/correction behavior are specified for all proposed funds movements.
- [ ] The roadmap separates ledger truth, pricing/reserves and payout execution into owned domains and gated delivery work.

## Validation scenarios

- [ ] Review sample accounting scenarios with qualified finance/accounting owners using synthetic transactions.
- [ ] Check conservation/balance/idempotency invariants across authorization, capture, refund, dispute, fee and settlement examples relevant to the proposed scope.
- [ ] Review changed funds flow against the approved commercial/regulatory model before generating implementation commitments.

## Expected deliverables

- Conditional funds-flow/ledger decision record.
- Accounting model and invariant examples.
- Gated ledger/fee/reserve/payout domain roadmap.

## External inputs and applicability

Applicability: **conditional**. Initial decision: **deferred**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved future funds-flow/business scope; qualified accounting/legal/compliance review; banking/acquirer/payout relationships and jurisdiction-specific obligations before implementation.

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
