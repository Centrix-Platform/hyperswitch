---
id: "CTX-098"
title: "Sign and distribute SDK artifacts with Android compatibility CI"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "SDK release engineering"
depends_on: ["CTX-010", "CTX-011", "CTX-075", "CTX-076", "CTX-093", "CTX-095", "CTX-096", "CTX-097"]
requires_one_of: []
conflict_domains: ["android/compatibility-ci", "sdk/release-pipeline"]
external_inputs: ["Artifact registry, release-signing custody, CI identity permissions, and release authority.", "Supported Android API/ABI/toolchain and vendor distribution/license constraints."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-098: Sign and distribute SDK artifacts with Android compatibility CI

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

SDK consumers need reproducible, traceable artifacts whose version, dependencies, public API, and supported Android environment are known. Establish release automation for the owned Maven packages and sample APKs, keeping artifact signing separate from application signing and terminal key provisioning. A library AAR is not an installed application; distinguish repository artifact signatures/provenance from APK signing identities used in device/IPC authorization. Publish compatibility metadata for Android API levels, ABI/toolchain constraints, Kotlin/Java versions, vendor adapter versions, and shared client-core dependencies. Production release signing uses controlled secret access and an approval trail, while pull-request builds cannot access signing material. Obfuscation rules and consumer ProGuard/R8 configuration must preserve required callbacks and serializers without exposing internal implementation as public API.

## Prerequisites and dependency outputs

- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) - consume its completed, reviewed deliverables: Establish SBOM, artifact signing and license provenance.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) - consume its completed, reviewed deliverables: Redact mobile logs, crashes, storage, and backups.
- [CTX-095](CTX-095-detach-client-core-and-react-native-remote-endpoints--TODO.md) - consume its completed, reviewed deliverables: Detach shared client-core and React Native remote endpoints.
- [CTX-096](CTX-096-publish-stable-kotlin-and-java-sdk-facades--TODO.md) - consume its completed, reviewed deliverables: Publish stable Kotlin and Java SDK compatibility facades.
- [CTX-097](CTX-097-build-reference-aggregator-apk-and-secure-backend--TODO.md) - consume its completed, reviewed deliverables: Build a reference aggregator APK and secure bootstrap backend.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / SDK release engineering**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/app/build.gradle (verify pinned fork)`

- `Proposed: external Android fork CI and Maven publishing configuration`

- `Proposed: SDK artifact provenance and consumer verification documentation`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/compatibility-ci`
- `sdk/release-pipeline`

## Implementation plan

- [ ] Create isolated CI jobs for build, API compatibility, dependency integrity, lint/static checks, and selected emulator/device tests.
- [ ] Generate signed Maven artifacts, provenance, SBOMs, checksums, and release manifests from pinned source inputs.
- [ ] Configure controlled release credentials and distinguish Maven signing, sample APK signing, partner app identity, and terminal key material.
- [ ] Publish consumer shrinker/obfuscation rules and verify release-mode serialization and vendor callback behavior.
- [ ] Document version promotion, rollback/deprecation, vulnerability response, and downstream verification.

## Acceptance criteria

- [ ] Published artifacts map unambiguously to source revisions and reproducible release inputs.
- [ ] Untrusted pull-request jobs cannot access release signing or registry publishing credentials.
- [ ] Release-mode sample apps pass public API and required vendor/fake-adapter smoke tests.
- [ ] Artifacts include SBOM, signature/provenance, compatibility matrix, and required notices.
- [ ] Consumers can verify artifact integrity using documented commands.

## Validation scenarios

- [ ] Build signed release candidates in the controlled pipeline and verify them from a clean consumer.
- [ ] Run R8/minification builds with Kotlin and Java facade fixtures.
- [ ] Attempt release secret access from an untrusted job context.
- [ ] Compare generated provenance/dependency manifests to pinned inputs.

## Expected deliverables

- SDK release/distribution pipeline
- Signed Maven artifact/provenance specification
- Android/toolchain compatibility matrix

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Artifact registry, release-signing custody, CI identity permissions, and release authority.
- [ ] Supported Android API/ABI/toolchain and vendor distribution/license constraints.

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
