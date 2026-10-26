---
id: "CTX-058"
title: "Authenticate and deduplicate inbound acquirer notifications"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "core"
component: "inbound-acquirer-notifications"
depends_on: ["CTX-028", "CTX-044", "CTX-055", "CTX-056", "CTX-057"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment:inbound-notifications", "workflow:notification-inbox"]
external_inputs: ["Pilot acquirer callback authentication and event identity specification"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-058: Authenticate and deduplicate inbound acquirer notifications

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Acquirer callbacks are external evidence and must not be trusted because they name a valid payment or arrive at a private-looking URL. Validate the connector-specific signature, certificate or approved authentication mechanism before resolving the configured account and original attempt. Deduplicate with a durable inbox, tolerate reordered delivery and reject cross-account attribution. Native webhook modules provide integration points, but public platform state transitions must still respect their declared single-writer authority and legal progression. A notification body may contain sensitive fields, so normalize to approved safe evidence and avoid logging raw payloads. This ticket covers inbound financial notifications, not outgoing customer webhooks, and must handle credential rotation, ambiguous duplicate event IDs and unsupported authenticity mechanisms explicitly.

## Prerequisites and dependency outputs

- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.


## Relevant code and ownership

Primary repository/workstream: **core / inbound-acquirer-notifications**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/webhooks/incoming.rs](../crates/router/src/core/webhooks/incoming.rs)

- [crates/router/src/core/webhooks/types.rs](../crates/router/src/core/webhooks/types.rs)

- `Proposed: platform/payments/notifications/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment:inbound-notifications`
- `workflow:notification-inbox`

## Implementation plan

- [ ] Define pilot notification authentication, key rotation and timestamp/replay policy.
- [ ] Resolve receiving account and attempt through trusted reference mappings.
- [ ] Persist deduplicated safe inbox evidence and apply conditional transitions.
- [ ] Handle duplicate, reordered and conflicting results with reconciliation escalation.
- [ ] Return protocol-appropriate acknowledgement without leaking ownership information.

## Acceptance criteria

- [ ] Unauthenticated or wrong-account callbacks cannot change payment state.
- [ ] Duplicate deliveries do not repeat state effects or outbound events.
- [ ] Late events cannot overwrite authoritative results through an invalid transition.
- [ ] Notification logs/inbox exclude forbidden raw payment data.
- [ ] Rotation accepts only the documented overlap key set.

## Validation scenarios

- [ ] Run signature tampering, wrong-account and stale timestamp cases.
- [ ] Deliver duplicates/out-of-order success/failure notifications.
- [ ] Crash after state commit but before acknowledgement and redeliver.

## Expected deliverables

- Authenticated notification adapter and inbox consumer.
- Webhook authenticity/state-transition test fixtures.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot acquirer callback authentication and event identity specification

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
