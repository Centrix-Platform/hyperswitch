---
id: "CTX-121"
title: "Build an isolated platform operator and audited support console"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Platform administration"
depends_on: ["CTX-039", "CTX-044", "CTX-069", "CTX-070", "CTX-109", "CTX-124"]
requires_one_of: []
conflict_domains: ["authentication-authorization-boundary", "platform-console", "platform-operator-auth"]
external_inputs: ["Platform operator identity group, strong-authentication policy and approved support/break-glass workflow."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-121: Build an isolated platform operator and audited support console

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Global platform visibility is an administrative capability, not an infrastructure Tenant identity or a hidden option in an aggregator session. Provide an independently authenticated control-plane console for provisioning, fleet health and narrowly scoped support actions. Normal aggregator credentials must never access it, and ordinary runtime database roles should not acquire RLS bypass permissions merely to power a dashboard. Cross-aggregator reporting can use dedicated redacted read models and explicit administrative APIs. Sensitive support access should be time-bounded, justified and fully auditable, with impersonation avoided or visibly constrained by the approved policy. The console must preserve environment boundaries and distinguish observing an incident from authorizing a financial operation or deploying a production configuration.

## Prerequisites and dependency outputs

- [CTX-039](CTX-039-platform-operator-break-glass-authority--TODO.md) - consume its completed, reviewed deliverables: Separate platform operator access and audited emergency authority.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-109](CTX-109-integrate-portal-bff-secure-sessions--TODO.md) - consume its completed, reviewed deliverables: Integrate the portal with secure BFF sessions and OIDC.
- [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) - consume its completed, reviewed deliverables: Implement immutable administrative and privileged access auditing.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Platform administration**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/router/src/services/authorization/roles.rs](../crates/router/src/services/authorization/roles.rs)

- `Proposed: services/platform-admin/`

- `Proposed: docs/operations/platform-support-access.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `authentication-authorization-boundary`
- `platform-console`
- `platform-operator-auth`

## Implementation plan

- [ ] Define operator roles and separate login/origin/session audience with strong authentication and least-privilege administrative APIs.
- [ ] Build aggregator provisioning/status and redacted global operational views from approved control-plane read models.
- [ ] Implement explicit target-aggregator support sessions with reason, expiry and recorded scope; integrate break-glass controls from CTX-039.
- [ ] Keep credentials, full payment payloads and unrestricted SQL access out of the console.
- [ ] Separate read/support functions from configuration and financially sensitive actions, applying the approved approval policy.
- [ ] Provide visible context banners and auditable termination/revocation of privileged sessions.

## Acceptance criteria

- [ ] Aggregator sessions and operational keys cannot authenticate to the platform operator surface.
- [ ] Global views use approved administrative APIs/read models rather than granting normal application roles RLS bypass.
- [ ] Every privileged support action records actor, reason, target, scope and outcome in the immutable audit trail.
- [ ] Privileged access expires/revokes as specified and cannot silently cross sandbox/live environments.
- [ ] The console presents redacted information and never exposes plaintext acquirer secrets or raw card data.
- [ ] Break-glass activation and termination produce reviewable evidence and notifications through approved channels.

## Validation scenarios

- [ ] Test role/audience/origin boundaries with aggregator and platform identities.
- [ ] Exercise time-bound support access, revocation, denied actions and audit completeness in a non-production environment.
- [ ] Verify runtime DB grants and redaction in global views and error responses.

## Expected deliverables

- Isolated platform operator console and administrative API integration.
- Privileged access/security test evidence.
- Support and break-glass operating guide.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Platform operator identity group, strong-authentication policy and approved support/break-glass workflow.

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
