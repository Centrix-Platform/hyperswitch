---
id: "CTX-120"
title: "Build signed webhook configuration, delivery inspection and replay tooling"
status: "TODO"
phase: 4
priority: "P0"
size: "M"
repository: "dashboard"
component: "Webhook developer UI"
depends_on: ["CTX-059", "CTX-069", "CTX-111", "CTX-116"]
requires_one_of: []
conflict_domains: ["dashboard-webhooks"]
external_inputs: ["Controlled webhook receiver and approved public HTTPS test endpoint; no customer notifications are sent by this authoring task."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-120: Build signed webhook configuration, delivery inspection and replay tooling

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregator integrations depend on reliable lifecycle and payment notifications delivered at least once, potentially out of order. The backend webhook service owns signing, retry schedules, delivery limits and safe replay. The portal should allow authorized subscription management and expose redacted delivery metadata without becoming an SSRF proxy or a way to retrieve signing secrets repeatedly. Endpoint verification, permitted event filters and environment separation remain server-enforced. Replaying a notification is not replaying a financial operation and must be labeled accordingly. Key rotation requires overlapping verification guidance and clear active/retiring versions. This ticket implements the developer/operator experience using existing subscription and delivery APIs, including failure diagnosis that does not reveal another aggregator payload or internal network details.

## Prerequisites and dependency outputs

- [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) - consume its completed, reviewed deliverables: Deliver signed versioned aggregator webhooks with safe retries.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.
- [CTX-116](CTX-116-developer-key-and-sdk-session-portal--TODO.md) - consume its completed, reviewed deliverables: Build scoped key, SDK-session and rotation tooling.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Webhook developer UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/webhooks.rs](../crates/router/src/core/webhooks.rs)

- [crates/router/src/routes/webhook_events.rs](../crates/router/src/routes/webhook_events.rs)

- [crates/api_models/src/webhook_events.rs](../crates/api_models/src/webhook_events.rs)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-webhooks`

## Implementation plan

- [ ] Build subscription create/edit/disable and permitted event-filter selection with endpoint verification status.
- [ ] Implement write-only signing-secret issuance/rotation display and show key identifiers/retirement timing for verifier configuration.
- [ ] Create delivery list/detail with redacted payload previews, response summaries, attempt times and correlation IDs.
- [ ] Expose authorized notification replay/retry through backend idempotent controls, with rate limits and explicit event reference.
- [ ] Provide verifier examples covering signature timestamps, replay windows, event IDs and resource-version ordering.
- [ ] Surface endpoint validation and safe SSRF-related errors without bypassing backend egress controls.

## Acceptance criteria

- [ ] Only authorized aggregator subscriptions and deliveries are accessible.
- [ ] Webhook endpoints pass backend URL/egress validation and cannot target prohibited internal destinations.
- [ ] Signing secrets are displayed once and rotation supports documented overlap without exposing retired material.
- [ ] Replay sends the selected event notification and never creates a financial payment/refund action.
- [ ] Delivery views redact secrets/payment-sensitive fields and preserve useful correlation metadata.
- [ ] Examples correctly handle duplicate and reordered events.

## Validation scenarios

- [ ] Run subscribe/verify/deliver/fail/retry/replay/rotate journeys against a controlled receiver.
- [ ] Test cross-aggregator delivery IDs, prohibited URLs and excessive replay attempts.
- [ ] Execute verifier examples with valid, expired, tampered and duplicate events.

## Expected deliverables

- Webhook subscription/delivery/replay UI.
- Signature verifier examples and rotation guidance.
- Delivery/ownership/SSRF regression evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Controlled webhook receiver and approved public HTTPS test endpoint; no customer notifications are sent by this authoring task.

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
