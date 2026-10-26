---
id: "CTX-048"
title: "Integrate acquirer merchant enrollment and explicit approval evidence"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "acquirer-enrollment"
depends_on: ["CTX-013", "CTX-021", "CTX-023", "CTX-025", "CTX-028", "CTX-044", "CTX-045"]
requires_one_of: []
conflict_domains: ["contracts:acquirer-onboarding", "platform-contract-catalog", "workflow:acquirer-enrollment"]
external_inputs: ["Pilot acquirer enrollment API, duplicate semantics, approval evidence and test access"]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-048: Integrate acquirer merchant enrollment and explicit approval evidence

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The native connector onboarding module currently demonstrates connector-specific flows, including PayPal, rather than a universal physical-terminal merchant enrollment API. Build an acquirer-specific adapter behind a language-neutral enrollment port for the pilot processing network. It must submit only authorized merchant evidence, capture assigned MID/TID or enrollment references, and distinguish received, pending, approved, rejected and ambiguous outcomes. Enrollment approval and terminal integration certification remain separate facts. External onboarding may not support idempotency, so use stable references and documented inquiry/manual-review behavior instead of resubmitting blindly. This ticket supplies one production-capable adapter and capability contract; it must not pretend that all acquirers share payloads, regulatory requirements or terminal activation semantics.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.


## Relevant code and ownership

Primary repository/workstream: **platform / acquirer-enrollment**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/connector_onboarding.rs](../crates/router/src/core/connector_onboarding.rs)

- [crates/api_models/src/connector_onboarding.rs](../crates/api_models/src/connector_onboarding.rs)

- `Proposed: platform/processing/enrollment/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:acquirer-onboarding`
- `platform-contract-catalog`
- `workflow:acquirer-enrollment`

## Implementation plan

- [ ] Define enrollment port, statuses and per-acquirer capability metadata.
- [ ] Implement pilot submission, inquiry and authenticated callback mapping.
- [ ] Persist external references and approval evidence with ownership checks.
- [ ] Handle duplicate/ambiguous submissions through documented lookup or review.
- [ ] Publish enrollment readiness into merchant lifecycle and connector projection workflows.

## Acceptance criteria

- [ ] Pilot acquirer approval is represented independently from profile existence and certification.
- [ ] Retries follow documented external duplicate semantics.
- [ ] Rejected/pending enrollment cannot enable live processing.
- [ ] Assigned external identifiers remain attributed to the correct merchant/account.
- [ ] Sensitive KYB evidence is transmitted through approved secure references/channels.

## Validation scenarios

- [ ] Simulate approval, rejection, timeout and duplicate callbacks.
- [ ] Crash after submission and recover using the original external reference.
- [ ] Attempt callback attribution to another aggregator and reject it.

## Expected deliverables

- Enrollment port and pilot acquirer adapter.
- Approval-state fixtures and recovery runbook.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Pilot acquirer enrollment API, duplicate semantics, approval evidence and test access

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
