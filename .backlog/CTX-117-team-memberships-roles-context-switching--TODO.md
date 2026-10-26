---
id: "CTX-117"
title: "Build team invitations, scoped roles and deliberate context switching"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Team and access management"
depends_on: ["CTX-022", "CTX-037", "CTX-038", "CTX-109", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-auth", "dashboard-team"]
external_inputs: ["Approved invitation email identity/templates and controlled development mail delivery; sending real invitations requires a separately authorized operational workflow."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-117: Build team invitations, scoped roles and deliberate context switching

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregator teams require memberships distinct from native infrastructure tenants and from the merchants they manage. Portal administrators can invite teammates and delegate permitted actions within their aggregator, but they must not grant themselves platform authority or assign permissions beyond their own delegation rights. Users may legitimately belong to several aggregators; switching must establish a newly authorized server session and clear prior workspace state. Invitations need bounded validity, verified acceptance and replay-safe transitions. Custom roles, merchant subsets, membership suspension and last-administrator protection should follow the approved authorization model. This ticket implements the user-facing workflows around backend membership/RBAC services and must account for revoked memberships in existing tabs and sessions rather than relying on a fresh login.

## Prerequisites and dependency outputs

- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-037](CTX-037-oidc-portal-bff-session-authentication--TODO.md) - consume its completed, reviewed deliverables: Implement OIDC portal sessions and explicit aggregator context switching.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-109](CTX-109-integrate-portal-bff-secure-sessions--TODO.md) - consume its completed, reviewed deliverables: Integrate the portal with secure BFF sessions and OIDC.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Team and access management**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/user.rs](../crates/router/src/routes/user.rs)

- [crates/router/src/routes/user_role.rs](../crates/router/src/routes/user_role.rs)

- [crates/router/src/services/authorization/roles.rs](../crates/router/src/services/authorization/roles.rs)

- [crates/diesel_models/src/user_role.rs](../crates/diesel_models/src/user_role.rs)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-auth`
- `dashboard-team`

## Implementation plan

- [ ] Build team/member lists, invitation create/cancel/accept and membership status screens through platform identity APIs.
- [ ] Implement role/permission and optional merchant-subset selection constrained by delegable server capabilities.
- [ ] Support membership revoke/suspend and role changes with authorization-version invalidation and audited reasons.
- [ ] Implement explicit aggregator context switching that reauthorizes membership and resets scoped caches/subscriptions.
- [ ] Protect required administrator continuity using the agreed last-admin/ownership-transfer policy.
- [ ] Add safe expired/replayed invitation and email-identity mismatch error paths without exposing other organizations.

## Acceptance criteria

- [ ] An aggregator administrator manages only its own memberships and eligible role assignments.
- [ ] Custom roles cannot grant platform permissions or rights beyond the actor's delegation authority.
- [ ] Invitations are expiring, revocable and single-use according to the identity contract.
- [ ] Role changes/revocation invalidate existing session authority within the defined bound.
- [ ] Context switching obtains a new authorized workspace and does not display prior cached data.
- [ ] The agreed last-administrator invariant holds under concurrent changes.

## Validation scenarios

- [ ] Run invitation acceptance/replay/expiry and identity-mismatch flows using a controlled mail sink.
- [ ] Test privilege escalation, cross-aggregator membership IDs and concurrent last-admin removals.
- [ ] Exercise two tabs during revocation and context switching with delayed API responses.

## Expected deliverables

- Team, role and context-switching portal workflows.
- Delegation/session invalidation E2E coverage.
- Aggregator access-management operator guide.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved invitation email identity/templates and controlled development mail delivery; sending real invitations requires a separately authorized operational workflow.

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
