---
id: "CTX-118"
title: "Build payment operations with safe capture, refund and UNKNOWN handling"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Payment operations UI"
depends_on: ["CTX-057", "CTX-060", "CTX-061", "CTX-062", "CTX-064", "CTX-069", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-payments"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-118: Build payment operations with safe capture, refund and UNKNOWN handling

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Operators need a trustworthy view of payment intent, individual acquirer attempts and financial uncertainty. The portal must not flatten UNKNOWN into failed or offer a new authorization as an ordinary retry after a timeout. Capture, refund, reversal and terminal-completion operations follow distinct backend state machines and idempotency scopes. Aggregator and optional merchant-subset permissions apply to reads and actions. Present safe masked data, frozen processing context and audit history without cardholder payloads. A future agent should use the platform operations/read APIs rather than infer money movement from frontend status labels or native dashboard assumptions. Operator actions need explicit amounts, currency, reason and concurrency checks, while reconciliation remains the authority for unresolved outcomes.

## Prerequisites and dependency outputs

- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Payment operations UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/payments.rs](../crates/router/src/routes/payments.rs)

- [crates/router/src/routes/refunds.rs](../crates/router/src/routes/refunds.rs)

- [crates/diesel_models/src/payment_intent.rs](../crates/diesel_models/src/payment_intent.rs)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-payments`

## Implementation plan

- [ ] Build scoped payment/attempt list and detail views with immutable operation references, route versions and masked transaction metadata.
- [ ] Display admitted, dispatching, successful, failed and UNKNOWN states with status freshness and inquiry/reconciliation progress.
- [ ] Implement permitted capture/refund/reversal actions using dedicated contracts, idempotency keys, amount limits and state/version checks.
- [ ] Disable unsafe retry/reroute behavior for ambiguous outcomes and link to approved inquiry/recovery actions.
- [ ] Show terminal-completion progress, acquirer notifications, administrative actions and financial journal references in a coherent timeline.
- [ ] Handle delayed responses and duplicate clicks by tracking the original operation reference rather than submitting new financial actions.

## Acceptance criteria

- [ ] UNKNOWN is visibly distinct from failure and never offers an automatic new authorization/reroute.
- [ ] Capture/refund amounts cannot exceed backend-authorized limits under concurrent operator actions.
- [ ] Repeated clicks/refresh return the existing operation without a duplicate financial submission.
- [ ] Cross-aggregator and unauthorized merchant-subset payment access is denied.
- [ ] Historical route, credential version and terminal assignment remain traceable without secret material.
- [ ] Delayed webhook/inquiry updates converge to valid backend states in the UI.

## Validation scenarios

- [ ] Run synthetic authorization, capture, partial refund, reversal and UNKNOWN inquiry E2E scenarios.
- [ ] Test duplicate clicks, delayed network responses and concurrent refunds/captures.
- [ ] Review redaction and ownership across payment list/detail/export links and timeline data.

## Expected deliverables

- Payment/attempt operations screens.
- Financial-state and duplicate-action E2E coverage.
- Operator guidance for ambiguous outcomes.

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
