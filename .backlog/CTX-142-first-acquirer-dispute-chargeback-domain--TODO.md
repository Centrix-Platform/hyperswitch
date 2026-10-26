---
id: "CTX-142"
title: "Implement scoped first-acquirer dispute lifecycle evidence and notifications"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "Dispute and chargeback management"
depends_on: ["CTX-013", "CTX-028", "CTX-031", "CTX-032", "CTX-038", "CTX-043", "CTX-046", "CTX-058", "CTX-059", "CTX-064", "CTX-065", "CTX-069"]
requires_one_of: []
conflict_domains: ["contracts:disputes", "database-schema-migrations", "native:dispute-adapter", "platform-contract-catalog", "schema:dispute-ownership", "workflow:dispute-evidence", "workflow:dispute-ingestion"]
external_inputs: ["Pilot acquirer dispute/chargeback authentication and event/inquiry specifications, external identity/correlation rules, authoritative lifecycle and deadline/timezone semantics.", "Approved evidence requirements, permitted submission/action APIs and their duplicate/receipt semantics; authorized sandbox access or authoritative fixtures.", "Aggregator/acquirer responsibility and escalation owners plus approved dispute-document retention/access policy; no legal deadline or liability assumption may be invented by implementation agents."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-142: Implement scoped first-acquirer dispute lifecycle evidence and notifications

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The inspected native dispute model links payment, attempt, merchant, optional profile/MCA, connector dispute ID, status, evidence and challenge_required_by; existing routes expose retrieval, synchronization and actions. Those native surfaces do not replace the canonical merchant boundary or establish the pilot acquirer's actual dispute rules. Implement one acquirer dispute path behind platform-owned contracts with authenticated ingestion, durable deduplication, immutable original-payment attribution and a declared authoritative dispute-state writer. Separate the original authorization outcome from later chargeback events. Preserve source-provided lifecycle and deadline provenance; missing or ambiguous deadlines require explicit manual handoff rather than invented dates. Evidence uses purpose-authorized secure references and supported acquirer submission semantics. Read APIs, events and notifications must respect aggregator and merchant scope. Link journal and settlement exceptions without creating balances, automatically refunding or rerouting disputed payments. Unsupported actions remain unavailable with an actionable owner and handoff procedure.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.
- [CTX-058](CTX-058-authenticated-acquirer-notification-inbox--TODO.md) - consume its completed, reviewed deliverables: Authenticate and deduplicate inbound acquirer notifications.
- [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) - consume its completed, reviewed deliverables: Deliver signed versioned aggregator webhooks with safe retries.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.


## Relevant code and ownership

Primary repository/workstream: **platform / Dispute and chargeback management**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/dispute.rs](../crates/diesel_models/src/dispute.rs)

- [crates/router/src/core/disputes.rs](../crates/router/src/core/disputes.rs)

- [crates/router/src/routes/disputes.rs](../crates/router/src/routes/disputes.rs)

- [crates/router/src/core/webhooks/incoming.rs](../crates/router/src/core/webhooks/incoming.rs)

- [crates/api_models/src/disputes.rs](../crates/api_models/src/disputes.rs)

- `Proposed: platform/disputes/`

- `Proposed: contracts/public/disputes/`

- `Proposed: platform/tests/disputes/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:disputes`
- `database-schema-migrations`
- `native:dispute-adapter`
- `platform-contract-catalog`
- `schema:dispute-ownership`
- `workflow:dispute-evidence`
- `workflow:dispute-ingestion`

## Implementation plan

- [ ] Confirm pilot acquirer dispute event/authentication, stages, external identities, deadline/timezone rules, evidence types, action permissions and submission/inquiry capabilities; publish a capability matrix and select one authoritative dispute-state writer/native projection direction.
- [ ] Create canonical dispute and history records with composite aggregator/merchant ownership, immutable original payment/attempt/account/route references, source event/version provenance, optional authoritative deadlines and durable inbox deduplication; quarantine unmatched external events for scoped reconciliation.
- [ ] Implement authenticated webhook and/or inquiry ingestion through the CTX-058 trust boundary; resolve ownership from configured receiving account and original payment references, reject cross-account correlation, and process duplicate/reordered/conflicting events through explicit legal transitions.
- [ ] Expose scoped dispute list/detail/history APIs and safe versioned outbox/webhook events, including action capabilities, exact source deadline or unknown status, permitted reason/amount/currency fields and reconciliation references; keep native IDs internal.
- [ ] Implement authorized evidence attachment using CTX-046 storage primitives with dispute-specific purpose, ownership, scanning, retention and access policy; add an idempotent first-acquirer submission adapter only for supported actions and preserve pending/unknown submission acknowledgement until verified.
- [ ] Create manual-handoff/escalation records for unsupported action, unavailable authentication/inquiry, unmatched correlation, missing deadline or uncertain evidence receipt; identify responsible aggregator/acquirer operator without simulating acceptance, inventing deadlines or auto-accepting liability.
- [ ] Append deduplicated dispute/chargeback facts to CTX-064 journal and correlate CTX-065 settlement adjustments/exceptions; preserve original payment state and route, add tenant/native isolation coverage, and validate the bounded pilot path with authoritative acquirer fixtures.

## Acceptance criteria

- [ ] Unauthenticated, wrong-account and cross-aggregator/merchant dispute events cannot expose or mutate a dispute; every dispute resolves to the original immutable payment/attempt ownership or remains quarantined without guessed attribution.
- [ ] Duplicate or reordered events do not duplicate dispute records, financial journal facts or evidence submissions; one declared authority controls lifecycle transitions and conflicting source evidence is auditable.
- [ ] Deadlines retain authoritative source, timezone/precision and update history; absent or ambiguous deadlines remain explicitly unknown with a manual escalation, never a fabricated default date or unsupported countdown.
- [ ] List/detail/history, evidence references and notifications enforce the same aggregator/merchant permissions as payment reads, including restricted roles and revoked access; native IDs and raw payment/SAD contents are absent.
- [ ] Evidence is submitted only through a supported, authorized original-acquirer account adapter; repeated requests and response-loss preserve submission identity and pending/unknown state until confirmed, and document upload alone never implies acquirer acceptance or a won dispute.
- [ ] Unsupported accept/defend/representment/evidence actions expose a documented manual handoff and cannot be invoked through native admin escape routes; changing routing or merchant assignment cannot redirect an existing dispute.
- [ ] Journal/reconciliation links preserve amount/currency/source provenance without rewriting the original payment outcome, creating balances, automatically issuing a refund or treating a dispute notification alone as confirmed settlement.

## Validation scenarios

- [ ] Run authentic, forged, wrong-account, duplicated, reordered and unmatched pilot dispute fixtures against two aggregators with overlapping external references; assert scoped quarantine, deduplication and immutable payment attribution.
- [ ] Exercise authoritative deadline changes, missing dates, timezone boundaries and late notifications; verify source history and manual escalation without invented due dates or implicit legal conclusions.
- [ ] Attach foreign/quarantined/expired evidence references and attempt unsupported actions; verify denial, purpose-bound storage access and safe manual-handoff outputs.
- [ ] Crash after evidence submission but before acknowledgement, replay the request and resolve by documented acquirer inquiry or manual confirmation; assert no fabricated receipt or duplicate unsafe external action.
- [ ] Correlate synthetic opened/won/lost/chargeback-settlement scenarios to journal and reconciliation records after routing changes, terminal reassignment and merchant suspension; run native/runtime-role isolation tests and scan events/logs for sensitive data.

## Expected deliverables

- Versioned canonical dispute/read/evidence-action API and event contracts plus first-acquirer capability/deadline provenance matrix.
- Owner-scoped dispute schema/repository, authenticated ingestion/inbox adapter and declared native compatibility projection.
- Secure evidence-reference/submission adapter or explicit unsupported-action manual-handoff implementation, with journal and settlement correlation.
- Pilot acquirer contract fixtures, adversarial isolation/reordering tests and evidence-submission recovery runbook.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot acquirer dispute/chargeback authentication and event/inquiry specifications, external identity/correlation rules, authoritative lifecycle and deadline/timezone semantics.
- [ ] Approved evidence requirements, permitted submission/action APIs and their duplicate/receipt semantics; authorized sandbox access or authoritative fixtures.
- [ ] Aggregator/acquirer responsibility and escalation owners plus approved dispute-document retention/access policy; no legal deadline or liability assumption may be invented by implementation agents.

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
