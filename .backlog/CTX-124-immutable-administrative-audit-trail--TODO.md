---
id: "CTX-124"
title: "Implement immutable administrative and privileged access auditing"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "platform"
component: "Audit and governance"
depends_on: ["CTX-012", "CTX-028", "CTX-029", "CTX-038", "CTX-039", "CTX-040", "CTX-043", "CTX-047", "CTX-068"]
requires_one_of: []
conflict_domains: ["administrative-audit", "audit-storage"]
external_inputs: ["Business/security-approved retention and privileged audit-access policy; immutable-storage capabilities in the chosen cloud/provider."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-124: Implement immutable administrative and privileged access auditing

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Financial journal entries and security/admin audit events serve different purposes. Record who changed memberships, keys, merchant state, terminal bindings, processing credentials, routing and privileged support access without copying secrets or raw payment payloads into a permanent log. Audit records need trusted actor/context, target, action, reason, version, result and correlation identifiers, with a strategy for detecting tampering and privileged deletion. Event persistence must be coupled reliably to successful mutations through the outbox or equivalent transactional boundary. Define which high-risk actions fail closed if durable auditing is unavailable. Read access and retention must remain scoped, while approved platform reviewers can investigate cross-aggregator events through a separate controlled path.

## Prerequisites and dependency outputs

- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-039](CTX-039-platform-operator-break-glass-authority--TODO.md) - consume its completed, reviewed deliverables: Separate platform operator access and audited emergency authority.
- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.


## Relevant code and ownership

Primary repository/workstream: **platform / Audit and governance**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/events/routing_api_logs.rs](../crates/router/src/events/routing_api_logs.rs)

- [crates/router/src/events/outgoing_webhook_logs.rs](../crates/router/src/events/outgoing_webhook_logs.rs)

- `Proposed: services/audit/`

- `Proposed: docs/security/audit-coverage.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `administrative-audit`
- `audit-storage`

## Implementation plan

- [ ] Define canonical audit event schemas and an action coverage matrix distinguishing operational journal, application logs and administrative audit.
- [ ] Emit durable events for successful/denied high-risk mutations with trusted actor, effective scope, target, reason, old/new safe versions and correlation IDs.
- [ ] Persist/ship events through a transactionally reliable pipeline into access-controlled append-only storage with integrity/tamper evidence and monitored retention controls.
- [ ] Implement scoped audit queries/exports and separately authorized platform investigation access.
- [ ] Specify audit-unavailable behavior, clock/order guarantees and service-actor delegation chains.
- [ ] Document retention, legal holds, integrity verification and privileged-access review without storing credentials or sensitive authentication data.

## Acceptance criteria

- [ ] Every action in the approved coverage matrix produces a durable, redacted and attributable record.
- [ ] Successful mutations cannot be silently committed without required audit durability under tested failures.
- [ ] Normal runtime and aggregator roles cannot edit/delete audit history or read other aggregators events.
- [ ] Tampering/deletion attempts are detectable through the selected integrity controls.
- [ ] Audit retention/legal-hold policy is enforceable and independent of generic application log retention.
- [ ] Audit queries preserve useful provenance without secret, card or PIN payload fields.

## Validation scenarios

- [ ] Run mutation-to-audit contract tests including rollback, queue outage, duplicate delivery and denied access.
- [ ] Attempt unauthorized read/update/delete and verify integrity monitoring on controlled test objects.
- [ ] Sample redaction and reconstruct a credential/terminal/routing change timeline from audit records.

## Expected deliverables

- Audit event schema, coverage matrix and durable pipeline.
- Scoped audit query/export implementation.
- Integrity, outage and retention verification report.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Business/security-approved retention and privileged audit-access policy; immutable-storage capabilities in the chosen cloud/provider.

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
