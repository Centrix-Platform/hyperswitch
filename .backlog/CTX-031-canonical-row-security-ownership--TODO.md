---
id: "CTX-031"
title: "Protect canonical tables with RLS and composite ownership constraints"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "canonical-database-isolation"
depends_on: ["CTX-019", "CTX-021", "CTX-022", "CTX-023", "CTX-025", "CTX-026", "CTX-027", "CTX-028", "CTX-030"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "schema:rls", "storage:database-roles"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-031: Protect canonical tables with RLS and composite ownership constraints

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Application predicates are necessary but a missed filter must not expose another aggregator's canonical records. Add PostgreSQL row security to tenant-owned platform tables using trusted transaction-local context and both read and write checks. Runtime roles must not own tables or have BYPASSRLS; force row security where applicable and keep migration/operator privileges separate. Composite foreign keys and scoped uniqueness enforce ownership relationships independently of query policy. This ticket covers canonical schemas only; CTX-032 covers native Hyperswitch data. A session-setting policy is defense against omitted predicates, not protection against a fully compromised service capable of setting arbitrary context. Deny missing context, constrain function privileges and include metadata, event and audit tables in the coverage inventory.

## Prerequisites and dependency outputs

- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator memberships roles and merchant-scoped grants.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-030](CTX-030-transaction-local-scoped-repositories--TODO.md) - consume its completed, reviewed deliverables: Enforce transaction-local tenancy in scoped storage and pool APIs.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / canonical-database-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform/migrations/`

- `Proposed: platform/tests/tenancy/rls/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `schema:rls`
- `storage:database-roles`

## Implementation plan

- [ ] Classify canonical tables as tenant-owned, global reference or privileged control-plane.
- [ ] Create non-owner runtime grants and approved current-context helper functions.
- [ ] Apply USING/WITH CHECK policies and FORCE RLS to tenant-owned tables.
- [ ] Validate composite references, scoped uniqueness and supporting indexes.
- [ ] Add schema introspection coverage checks for newly introduced tenant tables.

## Acceptance criteria

- [ ] Missing context returns no tenant rows and rejects tenant writes.
- [ ] Cross-aggregator SELECT, INSERT, UPDATE and DELETE are denied.
- [ ] Runtime roles have no table ownership or BYPASSRLS.
- [ ] Every canonical tenant table is classified and covered by policy.
- [ ] Cross-owner relationships fail even through privileged test inserts.

## Validation scenarios

- [ ] Execute adversarial CRUD with real runtime roles, not the migration owner.
- [ ] Inspect pg_class/pg_policy/pg_roles coverage automatically.
- [ ] Compare query plans for representative scoped reads and updates.

## Expected deliverables

- Canonical RLS/grant migrations.
- Automated policy coverage and ownership-constraint checks.

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
