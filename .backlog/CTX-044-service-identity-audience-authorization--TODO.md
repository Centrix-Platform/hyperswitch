---
id: "CTX-044"
title: "Authenticate internal services and constrain delegated context"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "service-authentication"
depends_on: ["CTX-005", "CTX-009", "CTX-016", "CTX-029", "CTX-038"]
requires_one_of: []
conflict_domains: ["auth:service-identity", "authentication-authorization-boundary", "contracts:internal-auth", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-044: Authenticate internal services and constrain delegated context

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Splitting control-plane and execution domains introduces service-to-service trust boundaries that must not rely on a private network alone. Define workload identity, audience-bound credentials and explicit permissions for provisioning, execution, configuration publication, webhook processing and reporting. A caller cannot become an aggregator by supplying an aggregator_id header; the receiving service must validate both caller capability and delegated context. Distinguish operator automation, background workers and user-delegated actions, and preserve causation for audit. This ticket owns internal authentication and authorization conventions, not a mesh migration. Select transport identity compatible with the deployment platform, rotate credentials automatically and prevent internal execution/admin endpoints from accepting public mobile or operational tokens directly.

## Prerequisites and dependency outputs

- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.


## Relevant code and ownership

Primary repository/workstream: **platform / service-authentication**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: platform/identity/service_auth/`

- `Proposed: contracts/internal-auth/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:service-identity`
- `authentication-authorization-boundary`
- `contracts:internal-auth`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define service principals, audiences and allowed call graph per domain.
- [ ] Implement workload token/mTLS verification and short-lived credential rotation.
- [ ] Specify signed or otherwise authenticated delegated-context transport.
- [ ] Add recipient checks for service capability, ownership and environment.
- [ ] Remove public token acceptance from private native admin/execution ingress.

## Acceptance criteria

- [ ] Each internal endpoint rejects wrong service audience and unauthorized caller roles.
- [ ] Injected aggregator headers cannot create delegated authority.
- [ ] SDK and operational tokens cannot call native administrative APIs.
- [ ] Service identity rotation works without disabling caller authentication.
- [ ] Audit traces preserve service identity and original actor where applicable.

## Validation scenarios

- [ ] Call execution/provisioning APIs with wrong audience and copied public tokens.
- [ ] Tamper with delegated ownership context.
- [ ] Rotate workload credentials while running the baseline flow.

## Expected deliverables

- Internal identity middleware and call-graph policy.
- Delegated-context contract and rotation integration tests.

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
