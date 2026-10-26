---
id: "CTX-071"
title: "Gate releases on adversarial ownership and privilege isolation"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "isolation-release-gate"
depends_on: ["CTX-031", "CTX-032", "CTX-033", "CTX-034", "CTX-035", "CTX-038", "CTX-040", "CTX-041", "CTX-046", "CTX-063", "CTX-069"]
requires_one_of: []
conflict_domains: ["release:security-gate", "tests:tenant-isolation"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-071: Gate releases on adversarial ownership and privilege isolation

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Tenant isolation is an end-to-end property across APIs, SQL, caches, workers, documents, reporting and credentials. Build a release gate using two aggregators with overlapping external references, multiple merchants, restricted roles and distinct terminal/acquirer accounts. Test real runtime database roles and deployed adapters rather than mocks that bypass RLS or authorization. Include native-backed resources, feature-disabled stored-payment paths, stale sessions, forged terminal claims and asynchronous export/download flows. This ticket consolidates acceptance evidence; it should expose missing enforcement and require correction in owning tickets instead of adding a permissive test-only bypass. Keep failure reports safe and actionable. The selected topology must be reflected honestly, especially where BusinessProfile does not scope customer or vault records.

## Prerequisites and dependency outputs

- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.
- [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) - consume its completed, reviewed deliverables: Audit and enforce isolation across native payment and account storage.
- [CTX-033](CTX-033-submerchant-customer-vault-ownership--TODO.md) - consume its completed, reviewed deliverables: Isolate submerchant customer vault and mandate access or reject those features.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-035](CTX-035-analytics-search-report-isolation--TODO.md) - consume its completed, reviewed deliverables: Enforce aggregator and merchant scope in analytics and reporting.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) - consume its completed, reviewed deliverables: Secure onboarding document uploads and sensitive merchant evidence.
- [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) - consume its completed, reviewed deliverables: Authorize background jobs and constrain retry and replay behavior.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.


## Relevant code and ownership

Primary repository/workstream: **platform / isolation-release-gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/storage_impl/src/connection.rs](../crates/storage_impl/src/connection.rs)

- `Proposed: platform/tests/isolation/`

- `Proposed: platform/tests/fixtures/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `release:security-gate`
- `tests:tenant-isolation`

## Implementation plan

- [ ] Create reusable adversarial multi-aggregator fixtures and endpoint/resource matrix.
- [ ] Automate ownership substitution across CRUD, lists, search, exports and callbacks.
- [ ] Exercise runtime RLS roles, cache hits, jobs and object-reference access.
- [ ] Add privilege-escalation, revoked-token and terminal-binding attacks.
- [ ] Publish deterministic CI gate with coverage exceptions requiring explicit rationale.

## Acceptance criteria

- [ ] Every exposed tenant-owned resource has a negative ownership test.
- [ ] Database tests run as non-owner runtime roles.
- [ ] Cache/job/export paths cannot bypass synchronous authorization.
- [ ] Unsupported stored-payment features are tested as denied.
- [ ] CI fails on a deliberate missing predicate or forged ownership mutation.

## Validation scenarios

- [ ] Run the full matrix against the local stack with seeded overlapping IDs.
- [ ] Introduce controlled authorization/RLS mutations and confirm gate detection.
- [ ] Verify reports contain no sensitive test secrets or payment payloads.

## Expected deliverables

- Isolation integration suite and coverage report.
- Release gate configuration and reproducible fixture seed.

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
