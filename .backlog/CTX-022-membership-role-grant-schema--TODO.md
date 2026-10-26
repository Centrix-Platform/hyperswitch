---
id: "CTX-022"
title: "Model aggregator memberships roles and merchant-scoped grants"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "membership-domain"
depends_on: ["CTX-006", "CTX-019"]
requires_one_of: []
conflict_domains: ["contracts:authorization", "database-schema-migrations", "platform-contract-catalog", "schema:membership"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-022: Model aggregator memberships roles and merchant-scoped grants

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Native user roles can reference tenant, organization, merchant and profile entities, but your customer-facing authorization model must be expressed as aggregator membership and permitted merchant scope. Define canonical memberships independently from portal session tokens, with explicit status, role assignment, authorization version and invitation state. A user may belong to several aggregators, while each active session must select one authorized membership. Role definitions may contain action permissions and bounded merchant sets, not arbitrary native IDs. This ticket supplies persistent authorization facts; CTX-037 and CTX-038 implement session issuance and enforcement. Prevent self-escalation through role editing, preserve who granted authority, and make revocation changes observable without erasing history or relying solely on token expiry.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.


## Relevant code and ownership

Primary repository/workstream: **platform / membership-domain**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/user_role.rs](../crates/diesel_models/src/user_role.rs)

- [crates/diesel_models/src/role.rs](../crates/diesel_models/src/role.rs)

- [crates/router/src/services/authorization/permissions.rs](../crates/router/src/services/authorization/permissions.rs)

- `Proposed: platform/identity/memberships/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:authorization`
- `database-schema-migrations`
- `platform-contract-catalog`
- `schema:membership`

## Implementation plan

- [ ] Create membership, role, permission-grant, merchant-scope and invitation records.
- [ ] Define permission vocabulary and bounded defaults for administrator, onboarding, operations, developer and analyst.
- [ ] Add authorization_version and immutable grant/revocation history.
- [ ] Constrain grants and merchant-set references to their owning aggregator.
- [ ] Define role-edit delegation limits and membership uniqueness.

## Acceptance criteria

- [ ] User membership can represent several aggregators without implicit cross-aggregator authority.
- [ ] Merchant-limited grants cannot reference another aggregator merchant.
- [ ] Every grant and revocation records an actor and authorization version.
- [ ] Inactive memberships cannot be used as effective grants.
- [ ] Default roles contain explicitly enumerated permissions.

## Validation scenarios

- [ ] Build a permission matrix for all default roles and inspect unexpected privileges.
- [ ] Insert foreign merchant-scope relationships and expect database rejection.
- [ ] Revoke a membership and verify version increment and retained audit history.

## Expected deliverables

- Membership and grant migrations.
- Permission catalog and authorization repository contract.

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
