---
id: "CTX-136"
title: "Execute a controlled one-path pilot after limited release approval"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Pilot qualification"
depends_on: ["CTX-103", "CTX-107", "CTX-123", "CTX-126", "CTX-127", "CTX-128", "CTX-129", "CTX-131", "CTX-132", "CTX-133", "CTX-135"]
requires_one_of: []
conflict_domains: ["production-pilot", "release-approval", "release-integration"]
external_inputs: ["Explicit limited live-pilot approval; participating licensed aggregator/merchant/acquirer and certified terminal; live credentials/connectivity/settlement evidence; authorized operators, limits and change window."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-136: Execute a controlled one-path pilot after limited release approval

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The first production slice should use one licensed aggregator, one approved merchant, one terminal family and one acquirer through settlement reconciliation. Limit blast radius with explicit participants, transaction limits, monitoring and abort conditions. Distinguish a simulator/sandbox rehearsal from a real-money pilot: sandbox evidence never proves live settlement, and a backlog ticket never authorizes production charges or contacting external parties. This pilot requires its own narrowly scoped release approval after prerequisite qualification; it then produces evidence for the broad go-live review in CTX-137, avoiding a circular dependency. Include capture/refund/reversal and ambiguous-outcome recovery appropriate to the approved integration, while never manufacturing unsafe real-money fault conditions merely to complete a checklist.

## Prerequisites and dependency outputs

- [CTX-103](CTX-103-execute-terminal-app-gateway-acquirer-certification-evidence--TODO.md) - consume its completed, reviewed deliverables: Execute exact terminal, application, gateway, and acquirer certification evidence.
- [CTX-107](CTX-107-prove-approved-terminal-to-acquirer-pilot-and-reconciliation-gate--TODO.md) - consume its completed, reviewed deliverables: Prove the approved terminal-to-acquirer pilot and reconciliation gate.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.
- [CTX-126](CTX-126-independent-security-and-pci-solution-gate--TODO.md) - consume its completed, reviewed deliverables: Complete independent penetration testing and PCI solution review.
- [CTX-127](CTX-127-capacity-fairness-and-concurrency-qualification--TODO.md) - consume its completed, reviewed deliverables: Qualify payment capacity, concurrency and aggregator fairness.
- [CTX-128](CTX-128-backup-restore-key-custody-and-journal-recovery--TODO.md) - consume its completed, reviewed deliverables: Exercise backup restore and cryptographic/journal recovery.
- [CTX-129](CTX-129-single-writer-regional-failover-game-day--TODO.md) - consume its completed, reviewed deliverables: Validate single-writer regional failover and UNKNOWN-outcome recovery.
- [CTX-131](CTX-131-payment-slos-alerts-and-operator-dashboards--TODO.md) - consume its completed, reviewed deliverables: Implement SLO dashboards and actionable payment health alerts.
- [CTX-132](CTX-132-payment-security-and-acquirer-incident-runbooks--TODO.md) - consume its completed, reviewed deliverables: Create and rehearse payment and security incident runbooks.
- [CTX-133](CTX-133-licensed-aggregator-responsibility-and-onboarding-checklist--TODO.md) - consume its completed, reviewed deliverables: Define licensed aggregator responsibilities and direct-settlement readiness.
- [CTX-135](CTX-135-signed-release-candidate-and-promotion-pipeline--TODO.md) - consume its completed, reviewed deliverables: Build signed release candidates and gated environment promotion.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Pilot qualification**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [config/deployments/production.toml](../config/deployments/production.toml)

- `Proposed: docs/releases/pilot-plan.md`

- `Proposed: docs/releases/pilot-evidence/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `production-pilot`
- `release-approval`
- `release-integration`

## Implementation plan

- [ ] Prepare a pilot plan naming exact release candidate, aggregator/merchant/device/acquirer participants, sandbox versus live stage, limits, duration and accountable operators.
- [ ] Rehearse the complete flow in sandbox and collect prerequisite certification, commercial, security and operational evidence.
- [ ] Obtain documented limited-pilot authorization from the designated release/business/acquirer participants before any live deployment or transaction.
- [ ] Execute only the approved pilot actions through standard tools/APIs, monitoring invariants and stopping on defined financial/security signals.
- [ ] Reconcile all pilot effects through acquirer/settlement records and resolve UNKNOWN operations with original references.
- [ ] Produce redacted pilot results, incidents, residual risks and recommendations for CTX-137 broad-launch review.

## Acceptance criteria

- [ ] Pilot scope and approval explicitly distinguish sandbox rehearsal from live financial actions.
- [ ] No live action occurs before the required limited-pilot authorization and selected participant approvals.
- [ ] Only approved entities, artifacts, transaction types and financial/traffic limits participate.
- [ ] Every pilot transaction is traceable to terminal, operation, acquirer and settlement/reversal evidence.
- [ ] No unresolved blocking financial, security or isolation issue remains hidden in a successful UI status.
- [ ] Pilot evidence is sufficient for CTX-137 review and does not itself authorize broad launch.

## Validation scenarios

- [ ] Verify all prerequisite evidence and limited approval signatures before the live stage.
- [ ] Compare operation/journal records to acquirer inquiries and final settlement/reversal artifacts.
- [ ] Review monitoring, abort criteria, operator timeline and closure of every pilot exception.

## Expected deliverables

- Sandbox rehearsal and limited live-pilot plan.
- Scoped approval/evidence register.
- Reconciled pilot report and broad-launch recommendations.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Explicit limited live-pilot approval; participating licensed aggregator/merchant/acquirer and certified terminal; live credentials/connectivity/settlement evidence; authorized operators, limits and change window.

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
