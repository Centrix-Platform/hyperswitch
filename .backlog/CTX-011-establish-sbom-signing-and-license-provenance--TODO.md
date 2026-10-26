---
id: "CTX-011"
title: "Establish SBOM, artifact signing and license provenance"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "supply-chain"
depends_on: ["CTX-003", "CTX-004", "CTX-010"]
requires_one_of: []
conflict_domains: ["ci-workflows", "release-signing"]
external_inputs: ["Approved package registries, signing identities and artifact retention policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-011: Establish SBOM, artifact signing and license provenance

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

White-label distribution spans Rust images, JavaScript bundles, Android AARs, sample APKs and shared SDK assets. A successful source build does not establish the provenance of the artifact installed by an aggregator or hosted for a mobile runtime. Introduce an inventory/SBOM and signed artifact verification model with separate environment/release identities. Preserve required source/license notices while removing product-facing branding. Remote asset and update packages need the same provenance scrutiny as native binaries. This foundation supports later Maven publishing, SDK remote configuration and production release promotion; it does not itself authorize uploading artifacts to a package registry or distributing an unapproved terminal integration.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) - consume its completed, reviewed deliverables: Establish controlled forks, provenance and upstream maintenance.
- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / supply-chain**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [LICENSE](../LICENSE)

- [NOTICE](../NOTICE)

- [Cargo.lock](../Cargo.lock)

- [Dockerfile](../Dockerfile)

- [.github/workflows](../.github/workflows)

- `External: juspay/hyperswitch-sdk-android/app/build.gradle (verify pinned fork)`

- `Proposed: docs/security/artifact-provenance.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `ci-workflows`
- `release-signing`

## Implementation plan

- [ ] Inventory release artifact types and transitive dependency sources across all forks.
- [ ] Generate machine-readable SBOMs and retain license/notice attribution from pinned inputs.
- [ ] Define signing identities, verification policy, provenance attestations and revocation/replacement handling.
- [ ] Verify runtime SDK assets/update bundles against approved signed inputs.
- [ ] Document reproducible build inputs and how artifacts are promoted unchanged across environments.

## Acceptance criteria

- [ ] Every release artifact can be traced to a source SHA, dependency graph and toolchain.
- [ ] An unsigned or tampered artifact is rejected by the defined consumer/deployment verification path.
- [ ] Required notices ship with the relevant distributed product.
- [ ] Build provenance does not embed live secrets or access tokens.
- [ ] The release process distinguishes artifact integrity from terminal/acquirer certification.

## Validation scenarios

- [ ] Rebuild representative image/AAR/bundle inputs and compare recorded provenance.
- [ ] Alter a signed test artifact and confirm verification fails.
- [ ] Review dependency licenses and notices against the SBOM.

## Expected deliverables

- SBOM and provenance pipeline
- Artifact signing/verification policy
- Distribution notice package

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved package registries, signing identities and artifact retention policy.

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
