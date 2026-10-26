---
id: "CTX-143"
title: "Build dispute case, evidence and authorized handoff workflows"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Dispute operations UI"
depends_on: ["CTX-046", "CTX-059", "CTX-111", "CTX-118", "CTX-119", "CTX-124", "CTX-142"]
requires_one_of: []
conflict_domains: ["dashboard-disputes", "dispute-evidence-contract"]
external_inputs: ["Selected provider dispute schemas, deadline/timezone rules, evidence requirements and approved electronic submission/inquiry capabilities from CTX-142.", "Approved evidence disclosure/retention policy, authorized aggregator/acquirer handoff roles and controlled synthetic provider cases; real submissions or communications require their separately authorized workflow."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-143: Build dispute case, evidence and authorized handoff workflows

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators need visibility and scoped actions for disputes and chargebacks linked to their merchants and original payment attempts. CTX-142 owns verified provider ingestion, correlation, state transitions, evidence contracts and safe read/events; this ticket consumes those APIs rather than inferring a dispute from an arbitrary webhook or browser-supplied payment ID. Deadlines, allowed evidence and submission capabilities come from the selected provider contract, never hard-coded universal rules. Documents used for merchant KYB cannot automatically be reused as dispute evidence: enforce purpose-specific schemas, authorization, retention and permitted disclosure. Supported submission requires validated evidence, explicit authorized intent and durable duplicate protection. When no approved adapter exists, provide a documented aggregator/acquirer handoff with immutable audit. Chargebacks must not imply platform balances or an unimplemented ledger.

## Prerequisites and dependency outputs

- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.
- [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) - consume its completed, reviewed deliverables: Deliver signed versioned aggregator webhooks with safe retries.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.
- [CTX-118](CTX-118-payment-operations-and-unknown-outcome-portal--TODO.md) - consume its completed, reviewed deliverables: Build payment operations with safe capture, refund and UNKNOWN handling.
- [CTX-119](CTX-119-reconciliation-reports-and-secure-exports-portal--TODO.md) - consume its completed, reviewed deliverables: Build reconciliation reports and tenant-safe exports.
- [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) - consume its completed, reviewed deliverables: Implement immutable administrative and privileged access auditing.
- [CTX-142](CTX-142-first-acquirer-dispute-chargeback-domain--TODO.md) - consume its completed, reviewed deliverables: Implement scoped first-acquirer dispute lifecycle evidence and notifications.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Dispute operations UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/disputes.rs](../crates/router/src/routes/disputes.rs)

- [crates/router/src/core/disputes.rs](../crates/router/src/core/disputes.rs)

- [crates/api_models/src/disputes.rs](../crates/api_models/src/disputes.rs)

- [crates/router/src/routes/files.rs](../crates/router/src/routes/files.rs)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`

- `Proposed: docs/portal/dispute-evidence-workflows.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-disputes`
- `dispute-evidence-contract`

## Implementation plan

- [ ] Build aggregator/merchant-scoped case lists and details showing original payment/attempt correlation, provider references, status, amount/currency, freshness and provider-defined deadlines with timezone/source metadata.
- [ ] Derive available actions from server permissions, case state and approved adapter capabilities; display unsupported or unverified states without synthesizing deadlines or allowing arbitrary state edits.
- [ ] Implement purpose-specific evidence manifests and secure upload/reference selection using approved schemas, ownership checks, allowed file/content rules, retention and disclosure controls; do not automatically expose or reuse KYB documents.
- [ ] Provide draft validation and authorized submission only where CTX-142 declares an approved adapter; use stable submission operation references, state/version checks and duplicate-click recovery.
- [ ] Implement explicit manual aggregator/acquirer handoff where submission is unsupported, tracking responsible party, provider receipt/reference, follow-up and outcome without falsely marking evidence submitted.
- [ ] Display immutable case/evidence/submission/handoff audit timelines and scoped notifications, with recoverable pending/unknown submission states and no automatic duplicate resubmission.

## Acceptance criteria

- [ ] Case lists, linked payments, evidence objects, exports and actions cannot expose or modify another aggregator or unauthorized merchant case.
- [ ] Deadlines and required evidence are sourced from provider-specific contracts/events with explicit timezone/freshness; missing or ambiguous deadlines are flagged rather than invented.
- [ ] Evidence has purpose-specific schema, allowed content, current authorization and controlled disclosure; KYB access alone does not authorize dispute evidence use.
- [ ] Electronic submission is available only for approved adapter capabilities and permitted case states; duplicate clicks, retries or browser restarts reuse one durable submission operation.
- [ ] An uncertain submission outcome remains pending/unknown until provider inquiry/receipt resolves it, without blind retransmission.
- [ ] Manual handoff records responsible party and verifiable receipt/outcome in immutable audit without asserting unsupported electronic submission.
- [ ] Views describe dispute and reconciliation effects without creating platform balances, reserve movements or unsupported ledger postings.

## Validation scenarios

- [ ] Run supported-provider and manual-only provider journeys covering case receipt, evidence validation, submission/handoff, provider acknowledgement and final outcome using synthetic cases.
- [ ] Attempt cross-aggregator case/payment/document IDs and unauthorized evidence reuse; verify purpose-specific access and file/download expiry.
- [ ] Test provider-defined deadline/timezone updates, missing dates, stale/reordered case events and concurrent/stale-version actions.
- [ ] Inject duplicate clicks, browser death, response loss and unknown submission outcomes; count provider side effects and reconstruct submission/audit history.
- [ ] Inspect previews, logs, notifications and exports for secret/payment-sensitive leakage and unsupported balance/accounting claims.

## Expected deliverables

- Scoped dispute case and provider-defined evidence/action screens.
- Approved electronic submission and explicit manual handoff workflows.
- Purpose/ownership/deadline/idempotency E2E evidence and operator guidance.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Selected provider dispute schemas, deadline/timezone rules, evidence requirements and approved electronic submission/inquiry capabilities from CTX-142.
- [ ] Approved evidence disclosure/retention policy, authorized aggregator/acquirer handoff roles and controlled synthetic provider cases; real submissions or communications require their separately authorized workflow.

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
