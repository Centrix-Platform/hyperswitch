---
id: "CTX-135"
title: "Build signed release candidates and gated environment promotion"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Release engineering"
depends_on: ["CTX-010", "CTX-011", "CTX-073", "CTX-098", "CTX-108", "CTX-123", "CTX-130", "CTX-134"]
requires_one_of: []
conflict_domains: ["artifact-provenance", "release-pipeline"]
external_inputs: ["Approved artifact registries/signing identities and deployment environments; explicit release-authority policy and separate live promotion approvals when later requested."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-135: Build signed release candidates and gated environment promotion

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A release candidate spans Rust core, platform services, React/ReScript portal, Android artifacts, API schemas, configuration and migration plans. Produce a coherent manifest with provenance and compatibility evidence rather than independently deploying latest branches. Build/sign once and promote immutable artifacts through controlled environments, keeping secrets and environment parameters outside the binary. This ticket can create and qualify non-live candidates before a limited production pilot; broad launch approval belongs to CTX-137 and must not create a dependency cycle with pilot evidence. Ensure rollback is realistic for schema/configuration changes and one-writer state. The pipeline must enforce approvals for live actions, but implementing or testing the pipeline does not itself authorize production deployment, financial traffic or external publication.

## Prerequisites and dependency outputs

- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) - consume its completed, reviewed deliverables: Establish SBOM, artifact signing and license provenance.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-108](CTX-108-white-label-dashboard-runtime-baseline--TODO.md) - consume its completed, reviewed deliverables: Fork and detach the Aggregator Portal runtime from upstream branding and services.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.
- [CTX-130](CTX-130-expand-contract-upgrades-and-client-deprecation--TODO.md) - consume its completed, reviewed deliverables: Implement staged upgrades, client compatibility and safe rollback.
- [CTX-134](CTX-134-production-infrastructure-hardening-and-scaling--TODO.md) - consume its completed, reviewed deliverables: Implement production IaC, segmentation and resilient runtime configuration.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Release engineering**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [.github/workflows/CI-pr.yml](../.github/workflows/CI-pr.yml)

- [.github/workflows/release-stable-version.yml](../.github/workflows/release-stable-version.yml)

- [.github/workflows/validate-openapi-spec.yml](../.github/workflows/validate-openapi-spec.yml)

- `Proposed: .github/workflows/platform-release.yml`

- `Proposed: docs/releases/release-manifest.schema.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `artifact-provenance`
- `release-pipeline`

## Implementation plan

- [ ] Define a release manifest linking source commits, image/package digests, SDK versions, OpenAPI/event versions, config/certification bundles and migration compatibility.
- [ ] Build signed artifacts with SBOM/provenance, dependency/security checks and immutable repository retention.
- [ ] Implement promote-by-digest through development, conformance and staging environments with verified signatures and separated credentials.
- [ ] Attach conformance, migration, performance and security evidence as it becomes available; encode required gate policies for pilot and broad release distinctly.
- [ ] Provide rollback/abort procedures preserving financial state, supported clients and configuration snapshots.
- [ ] Exercise non-production promotion and a denied live promotion without required approvals, recording the release-candidate evidence bundle.

## Acceptance criteria

- [ ] A manifest resolves every deployed component to immutable signed artifacts and known compatibility/certification versions.
- [ ] The same built artifacts are promoted without rebuilding against environment-specific secrets.
- [ ] Non-production promotion works and unauthorized live promotion fails closed.
- [ ] Pilot and broad-launch gates are distinct, with CTX-137 consuming pilot evidence rather than blocking RC creation.
- [ ] Rollback/abort metadata identifies schema boundaries and preserves active operation history.
- [ ] No production deployment, public package publication or charge is executed by the pipeline authoring/qualification task.

## Validation scenarios

- [ ] Run clean build/sign/verify/promote in controlled non-production environments.
- [ ] Tamper with an artifact/manifest and verify promotion refusal.
- [ ] Test missing approvals, incompatible migration/client versions and rollback/abort flow using synthetic operations.

## Expected deliverables

- Signed multi-repository release manifest and artifact pipeline.
- Environment promotion/gate policies.
- Non-live release-candidate qualification and rollback evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved artifact registries/signing identities and deployment environments; explicit release-authority policy and separate live promotion approvals when later requested.

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
