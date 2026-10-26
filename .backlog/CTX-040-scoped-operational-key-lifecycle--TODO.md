---
id: "CTX-040"
title: "Issue rotate and revoke aggregator operational API keys"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "operational-keys"
depends_on: ["CTX-009", "CTX-019", "CTX-022", "CTX-029", "CTX-038"]
requires_one_of: []
conflict_domains: ["auth:operational-keys", "authentication-authorization-boundary", "database-schema-migrations", "schema:api-key"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-040: Issue rotate and revoke aggregator operational API keys

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Native API keys already have a merchant owner, hashed verifier, prefix and optional expiry, but do not by themselves express the full public aggregator permission model. Implement platform operational keys for aggregator backends with explicit environment, scopes, optional bounded merchant access, expiry and revocation state. Treat these as delegated authority rather than secrets derived from a platform master key. Show secret material only at issuance, support overlap during rotation and make revocation observable by all gateway instances. The key identity must not be included in payment idempotency scope, because rotation cannot permit a duplicate charge. Do not place operational keys in mobile SDKs or browser assets, and keep native execution credentials behind the adapter.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.


## Relevant code and ownership

Primary repository/workstream: **platform / operational-keys**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/api_keys.rs](../crates/diesel_models/src/api_keys.rs)

- [crates/router/src/core/api_keys.rs](../crates/router/src/core/api_keys.rs)

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: platform/identity/operational_keys/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:operational-keys`
- `authentication-authorization-boundary`
- `database-schema-migrations`
- `schema:api-key`

## Implementation plan

- [ ] Define operational-key record, secure verifier algorithm and public lookup prefix.
- [ ] Implement create/list/rotate/revoke APIs with bounded delegated scopes.
- [ ] Integrate authentication, environment binding and authorization-version checks.
- [ ] Support overlap rotation and bounded revocation-cache propagation.
- [ ] Emit safe key lifecycle audit events without logging secrets.
- [ ] Provide a bounded pre-authentication key/mapping lookup with dedicated least-privilege grants and rate-limited opaque lookup identifiers; return only verifier/owner metadata needed to establish trusted context, then use scoped repositories for tenant data.

## Acceptance criteria

- [ ] Plaintext secret is returned once and never stored in ordinary key records.
- [ ] Keys authorize only their aggregator, environment and granted scopes.
- [ ] Rotation does not change idempotency identity of existing operations.
- [ ] Revocation takes effect within a tested documented interval.
- [ ] List/read APIs expose safe metadata only.
- [ ] Opaque-key authentication can establish aggregator context without circular RLS requirements, and its bootstrap interface cannot list or retrieve unrelated tenant resources.

## Validation scenarios

- [ ] Inspect persistence and logs after issuance for plaintext key material.
- [ ] Rotate a key while replaying an existing idempotent charge.
- [ ] Try a sandbox key against live endpoints and foreign resources.

## Expected deliverables

- Operational-key service and verifier storage.
- Key management API contract and rotation tests.

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
