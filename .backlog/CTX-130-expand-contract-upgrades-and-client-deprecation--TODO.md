---
id: "CTX-130"
title: "Implement staged upgrades, client compatibility and safe rollback"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Release compatibility"
depends_on: ["CTX-006", "CTX-036", "CTX-068", "CTX-073", "CTX-074", "CTX-098", "CTX-100", "CTX-123"]
requires_one_of: []
conflict_domains: ["api-compatibility", "database-schema-migrations", "release-rollout", "schema-migrations"]
external_inputs: ["Approved support-window/minimum-version policy and aggregator rollout constraints; external deprecation messages require a separate authorized communication workflow."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-130: Implement staged upgrades, client compatibility and safe rollback

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Core, platform services, portal and distributed Android APKs cannot be upgraded atomically. Design compatible database migrations and configuration/event contracts so old and new versions can coexist through deployment and rollback windows. Android integrations may remain installed long after a server release, and terminal certification can constrain which software versions may transact. A rollback cannot safely undo an irreversible migration or alter the route/history of an already dispatched payment. This ticket operationalizes expand/backfill/validate/contract migrations, minimum-supported-client policy and versioned configuration. Public contract deprecations need evidence of client adoption and explicit communication preparation, not silent behavioral changes. Preserve financial state and one-writer authority while replacing application code.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-036](CTX-036-expand-backfill-validate-contract-rollout--TODO.md) - consume its completed, reviewed deliverables: Stage canonical and native tenancy migrations safely.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-074](CTX-074-tenancy-migration-recovery-rehearsal--TODO.md) - consume its completed, reviewed deliverables: Rehearse tenancy migration rollback and financial recovery.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-100](CTX-100-monitor-terminal-fleet-and-stage-configuration-revocation-rollouts--TODO.md) - consume its completed, reviewed deliverables: Monitor terminal fleets and stage configuration and revocation rollouts.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Release compatibility**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [scripts/migration_runner_entrypoint.sh](../scripts/migration_runner_entrypoint.sh)

- [.github/workflows/migration-check.yaml](../.github/workflows/migration-check.yaml)

- [.github/workflows/api-migrations-compatibility.yml](../.github/workflows/api-migrations-compatibility.yml)

- `Proposed: docs/engineering/compatibility-policy.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `api-compatibility`
- `database-schema-migrations`
- `release-rollout`
- `schema-migrations`

## Implementation plan

- [ ] Define compatibility windows and version matrices for API/event schemas, database schemas, portal, SDK, terminal adapters and certification bundles.
- [ ] Implement expand/backfill/validate/contract rollout with resumable jobs, dual-version readers where necessary and delayed destructive cleanup.
- [ ] Add server capability negotiation and minimum-client enforcement for unsafe/unsupported versions with recoverable user guidance.
- [ ] Define staged feature/configuration rollout, canary boundaries and rollback triggers that preserve frozen attempt snapshots and authority revocation.
- [ ] Prepare deprecation notices/migration guides and adoption telemetry without sending external communications in this task.
- [ ] Exercise forward/rollback paths on representative mixed-version traffic and document irreversible migration boundaries.

## Acceptance criteria

- [ ] Old/new supported versions coexist through the documented deployment window without contract or tenant-isolation failures.
- [ ] Backfills are resumable and validated before destructive schema contraction becomes eligible.
- [ ] Rollback procedures preserve durable operations, frozen routing and credential/version history.
- [ ] Unsupported SDK/terminal configurations fail safely before capture/dispatch under an explicit policy.
- [ ] Breaking changes require versioning and a documented adoption/deprecation plan.
- [ ] Mixed-version tests cover callbacks, events and client process recovery as well as synchronous API calls.

## Validation scenarios

- [ ] Run upgrade/backfill/rollback drills with mixed server, portal and SDK versions.
- [ ] Use schema/event contract compatibility tests and deliberately interrupt backfills.
- [ ] Test minimum-version enforcement and inspect in-flight/UNKNOWN operations across rollout boundaries.

## Expected deliverables

- Cross-component compatibility/deprecation policy.
- Staged migration and rollout/rollback automation.
- Mixed-version qualification evidence and migration guides.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved support-window/minimum-version policy and aggregator rollout constraints; external deprecation messages require a separate authorized communication workflow.

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
