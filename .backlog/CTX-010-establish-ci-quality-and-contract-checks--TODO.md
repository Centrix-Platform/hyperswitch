---
id: "CTX-010"
title: "Establish CI quality, migration and contract check lanes"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "delivery"
depends_on: ["CTX-003", "CTX-006", "CTX-007"]
requires_one_of: []
conflict_domains: ["ci-workflows", "platform-contract-catalog", "public-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-010: Establish CI quality, migration and contract check lanes

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The core already includes Rust, OpenAPI and migration CI workflows and a justfile with distinct v1/v2 recipes. Preserve useful upstream checks while adding platform-specific contract and isolation validation. A blanket cargo --all-features invocation is not a valid baseline because the feature sets are mutually exclusive. Different agents will touch schemas, contracts, the core adapter and external frontend/SDK repositories; CI must identify which lanes are required and where generated artifacts originate. Build/release secrets should not be available to untrusted pull-request jobs. This task establishes reviewable CI policy and scoped quality lanes, while later tickets provide adversarial payment, mobile and production qualification scenarios.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) - consume its completed, reviewed deliverables: Establish a reproducible, isolated local development stack.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / delivery**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [.github/workflows/CI-pr.yml](../.github/workflows/CI-pr.yml)

- [.github/workflows/migration-check.yaml](../.github/workflows/migration-check.yaml)

- [.github/workflows/validate-openapi-spec.yml](../.github/workflows/validate-openapi-spec.yml)

- [justfile](../justfile)

- `Proposed: .github/workflows/ctx-contracts.yml`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `ci-workflows`
- `platform-contract-catalog`
- `public-contracts`

## Implementation plan

- [ ] Inventory existing workflows and retain the checks appropriate to the selected baseline.
- [ ] Add scoped Rust formatting/lint/build/test, API/event schema compatibility and migration validation lanes.
- [ ] Define equivalent frontend ReScript/TypeScript and Android client compatibility checks in their external forks.
- [ ] Restrict release credentials to trusted jobs; define concurrency, cache keys and artifact provenance.
- [ ] Document branch/review policies and a local command for each required lane.

## Acceptance criteria

- [ ] CI selects a supported feature configuration without combining mutually exclusive versions.
- [ ] A breaking contract or unsafe migration fixture is rejected by the relevant lane.
- [ ] Untrusted contribution jobs cannot access production signing or deployment secrets.
- [ ] Generated artifacts are reproducible from a recorded source/toolchain pin.
- [ ] Each local check has a documented command and owner.

## Validation scenarios

- [ ] Exercise representative pass/fail contract and migration changes in non-publishing CI.
- [ ] Audit workflow permission scopes, fork events and secret exposure.
- [ ] Compare local command outputs with CI artifacts for the pinned baseline.

## Expected deliverables

- CI lane definitions
- Branch/review and workflow permission policy
- Developer validation command catalog

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
