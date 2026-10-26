---
id: "CTX-045"
title: "Expose idempotent aggregator merchant onboarding and operation status"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "merchant-onboarding"
depends_on: ["CTX-006", "CTX-021", "CTX-024", "CTX-028", "CTX-029", "CTX-038", "CTX-040", "CTX-046"]
requires_one_of: []
conflict_domains: ["contracts:merchant-onboarding", "platform-contract-catalog", "workflow:merchant-onboarding"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-045: Expose idempotent aggregator merchant onboarding and operation status

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The requested POST /v1/aggregators/{aggregator_id}/merchants endpoint is a platform-owned public contract, not a renamed native admin route. It accepts legal merchant details and owned references, reserves an idempotent onboarding operation and returns an asynchronous status resource while profile projection and acquirer enrollment proceed. Resolve the path aggregator from authenticated authority, keep native IDs internal and distinguish canonical lifecycle, projection readiness and processing approval. This ticket orchestrates the public workflow using domain services rather than duplicating KYB storage or connector onboarding logic. Repeated submissions and client timeouts must return the same merchant/operation when the request is equivalent, while conflicting reuse fails. A created profile must never be presented as an activated processing account.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / merchant-onboarding**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/admin.rs](../crates/router/src/core/admin.rs)

- [crates/router/src/core/connector_onboarding.rs](../crates/router/src/core/connector_onboarding.rs)

- `Proposed: platform/merchants/api/`

- `Proposed: contracts/public/openapi.yaml`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:merchant-onboarding`
- `platform-contract-catalog`
- `workflow:merchant-onboarding`

## Implementation plan

- [ ] Publish onboarding OpenAPI request, safe response, errors and 202 Location semantics.
- [ ] Implement scoped request validation and idempotent operation reservation.
- [ ] Orchestrate canonical merchant creation, native projection and enrollment references.
- [ ] Expose authorized operation and merchant status polling.
- [ ] Emit lifecycle events and actionable recoverable/blocked onboarding reasons.

## Acceptance criteria

- [ ] Path aggregator mismatch is rejected before merchant creation.
- [ ] Equivalent idempotent retries return the same merchant and operation.
- [ ] Conflicting request reuse returns a stable 409 error.
- [ ] Initial response exposes pending status rather than implied processing approval.
- [ ] All document, routing, settlement and account references are ownership-checked.

## Validation scenarios

- [ ] Replay onboarding after network timeout and worker restart.
- [ ] Use foreign document/acquirer references and reject the request.
- [ ] Exercise blocked acquirer enrollment and later successful resumption.

## Expected deliverables

- Public onboarding/status API and workflow adapter.
- OpenAPI examples and onboarding integration tests.

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
