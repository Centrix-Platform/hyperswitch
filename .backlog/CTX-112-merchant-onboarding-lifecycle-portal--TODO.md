---
id: "CTX-112"
title: "Build merchant onboarding, review and lifecycle screens"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Merchant management UI"
depends_on: ["CTX-045", "CTX-046", "CTX-047", "CTX-048", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-merchants"]
external_inputs: ["Synthetic legal-entity/document fixtures and the business-approved review/activation policy from CTX-001/CTX-133."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-112: Build merchant onboarding, review and lifecycle screens

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregators onboard their own legal merchants, represented canonically by platform Merchant records and initially projected into Hyperswitch BusinessProfiles. The portal must make the distinction between record creation, review, acquirer enrollment and processing activation explicit. Creating a BusinessProfile is not approval to transact. Use the asynchronous onboarding operation and documented lifecycle from the backend tickets rather than calling native admin endpoints from the browser. Onboarding may involve sensitive KYB documents, restricted reviewer actions and retryable provisioning steps. A future swarm agent should implement usable forms, progress visibility and recovery without inventing country-specific compliance rules or bypassing acquirer requirements. Merchant suspension must surface its effect on new sessions and terminal processing while preserving historical operations.

## Prerequisites and dependency outputs

- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.
- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-048](CTX-048-acquirer-merchant-enrollment-adapter--TODO.md) - consume its completed, reviewed deliverables: Integrate acquirer merchant enrollment and explicit approval evidence.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Merchant management UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- `Proposed: services/platform-control/src/merchants/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-merchants`

## Implementation plan

- [ ] Build merchant list/detail and create forms from the platform onboarding contract, using country/business fields supported by the approved model.
- [ ] Integrate authorized document upload references, review status and asynchronous operation polling/events without exposing storage internals.
- [ ] Display canonical onboarding/acquirer/provisioning statuses and actionable validation failures separately from processing eligibility.
- [ ] Implement permitted review, activate, suspend and resume actions with reason capture and conflict/version handling.
- [ ] Provide idempotent resubmission and interrupted-form recovery without reusing stale sensitive uploads or creating duplicate merchants.
- [ ] Show assigned terminal and processing summaries through scoped read APIs.

## Acceptance criteria

- [ ] An aggregator can create and inspect its merchant using the public contract without native MerchantAccount/Profile identifiers.
- [ ] Creation returns a pending lifecycle until all required approvals and projections succeed.
- [ ] Unauthorized reviewers and cross-aggregator merchant/document IDs are rejected and displayed safely.
- [ ] Suspension/resumption reflects backend eligibility and preserves payment history.
- [ ] Repeated submission with the original operation reference does not create duplicate merchants.
- [ ] Forms and errors satisfy the agreed keyboard/accessibility baseline.

## Validation scenarios

- [ ] Run portal E2E journeys for create, document failure, pending enrollment, approval, activation and suspension.
- [ ] Test duplicate submit, browser refresh during provisioning and stale-version conflicts.
- [ ] Attempt cross-aggregator reads, document access and unauthorized lifecycle transitions.

## Expected deliverables

- Merchant lifecycle screens and form bindings.
- Onboarding/status E2E coverage.
- Operator guide for supported review actions.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Synthetic legal-entity/document fixtures and the business-approved review/activation policy from CTX-001/CTX-133.

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
