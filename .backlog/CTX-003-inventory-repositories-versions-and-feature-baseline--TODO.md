---
id: "CTX-003"
title: "Inventory repositories, pinned versions and mutually compatible features"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "architecture"
depends_on: []
requires_one_of: []
conflict_domains: ["release-input-manifest"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-003: Inventory repositories, pinned versions and mutually compatible features

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Only the Rust core repository is available in this workspace. Its inspection baseline is commit c5ecb434b419d2c473cf2882a3866de9146abdec and router defaults include v1 and redis-rs. The dashboard and Android/client-core sources are separate upstream repositories, not local directories. The Android implementation includes shared client-core/React Native pieces and endpoint/configuration assets; a Kotlin package rename alone is insufficient. The core justfile notes that v1 and v2 features cannot be enabled together. A reproducible, compatible baseline prevents every later agent from independently selecting features or referring to files that are not checked out. Record the current user edits rather than overwriting docker-compose.yml or package-lock.json while establishing the inventory.

## Prerequisites and dependency outputs

This is a dependency-root ticket. Inspect the pinned source and resolve the inputs below before making implementation decisions.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / architecture**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [Cargo.toml](../Cargo.toml)

- [Cargo.lock](../Cargo.lock)

- [crates/router/Cargo.toml](../crates/router/Cargo.toml)

- [justfile](../justfile)

- [diesel.toml](../diesel.toml)

- [diesel_v2.toml](../diesel_v2.toml)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`

- `External: juspay/hyperswitch-sdk-android/README.md (verify pinned fork)`

- `External: juspay/hyperswitch-client-core/README.md (verify pinned fork)`

- `Proposed: docs/architecture/repository-manifest.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `release-input-manifest`

## Implementation plan

- [ ] Record current core SHA, workspace/toolchain requirements, feature set, migrations, dependencies and local changes.
- [ ] Inventory dashboard, Android, client-core and necessary SDK modules/submodules with owner URL and intended fork/pinned SHA.
- [ ] Produce a compatibility matrix connecting core API features, dashboard runtime settings, SDK interfaces and terminal vendor versions.
- [ ] Choose one supported core feature baseline and document the separate commands for any retained compatibility checks.
- [ ] Label all external paths as external until the target fork and checkout are verified.

## Acceptance criteria

- [ ] A repository/version manifest identifies provenance and exact pins for every release input.
- [ ] The selected feature set does not combine mutually exclusive v1/v2 configurations.
- [ ] Unfetched repositories and unverified vendor modules are visibly unresolved inputs.
- [ ] Existing user changes are recorded and preserved.
- [ ] Every downstream ticket can resolve its repository and supported toolchain from the manifest.

## Validation scenarios

- [ ] Compare manifest SHA and features with git rev-parse HEAD and crates/router/Cargo.toml.
- [ ] Resolve each retained submodule/dependency pin in an isolated clone when source access exists.
- [ ] Run baseline build commands for the chosen feature set rather than cargo --all-features.

## Expected deliverables

- Repository and version manifest
- Feature/API compatibility matrix
- Baseline command and local-change inventory

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
