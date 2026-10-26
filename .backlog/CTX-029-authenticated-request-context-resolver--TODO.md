---
id: "CTX-029"
title: "Resolve trusted aggregator merchant and environment context"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "request-context"
depends_on: ["CTX-016", "CTX-019", "CTX-022"]
requires_one_of: []
conflict_domains: ["auth:request-context", "authentication-authorization-boundary", "contracts:request-context", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-029: Resolve trusted aggregator merchant and environment context

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The native authentication module supports several merchant, organization, profile and platform paths. Your public gateway must normalize them into one trusted platform context before resolving customer resources. Path parameters, terminal IDs, tenant headers and branding hostnames cannot independently establish authority. Resolve the authenticated principal, environment, active aggregator membership or key, native account mapping and any constrained merchant/device scope. Expose an immutable context to authorization, storage, caches and execution adapters while keeping native IDs internal. Handle operator context separately from ordinary aggregator context. This ticket defines trusted resolution and middleware ordering; it does not implement every authentication method. Missing, stale or contradictory ownership information must fail closed rather than fall back to a global account or default profile.

## Prerequisites and dependency outputs

- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.


## Relevant code and ownership

Primary repository/workstream: **platform / request-context**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/router/src/services/authorization.rs](../crates/router/src/services/authorization.rs)

- `Proposed: platform/identity/request_context/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:request-context`
- `authentication-authorization-boundary`
- `contracts:request-context`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define immutable request context with principal, environment, aggregator and bounded resource scope.
- [ ] Implement mapping resolution after credential verification and before resource lookup.
- [ ] Reject mismatched route aggregator, injected tenant headers and incompatible token scopes.
- [ ] Propagate context through internal adapters without accepting untrusted reconstruction.
- [ ] Define stable safe errors and context freshness/version rules.
- [ ] Provide a bounded pre-authentication key/mapping lookup with dedicated least-privilege grants and rate-limited opaque lookup identifiers; return only verifier/owner metadata needed to establish trusted context, then use scoped repositories for tenant data.

## Acceptance criteria

- [ ] Public path/header changes cannot override authenticated aggregator ownership.
- [ ] No tenant-scoped handler executes with an absent aggregator context.
- [ ] Native mappings are present only in internal context serialization.
- [ ] Operator context cannot be mistaken for an aggregator session.
- [ ] Conflicting environment or merchant claims fail before database side effects.
- [ ] Opaque-key authentication can establish aggregator context without circular RLS requirements, and its bootstrap interface cannot list or retrieve unrelated tenant resources.

## Validation scenarios

- [ ] Submit valid credentials with another aggregator path and injected native headers.
- [ ] Exercise missing, revoked and stale membership versions.
- [ ] Inspect async handoff and internal adapter context propagation.

## Expected deliverables

- Request-context middleware and typed internal context.
- Authentication/authorization ordering specification.

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
