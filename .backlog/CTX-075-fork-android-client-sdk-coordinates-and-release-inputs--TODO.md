---
id: "CTX-075"
title: "Fork Android and shared client SDK identities and release inputs"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Android fork foundation"
depends_on: ["CTX-003", "CTX-004", "CTX-010", "CTX-011", "CTX-012", "CTX-018"]
requires_one_of: []
conflict_domains: ["android/build-identity", "client-core/dependency-graph", "sdk/release-inputs"]
external_inputs: ["Approved organization/repository names, product namespace, Maven coordinates, artifact registry, and signing ownership.", "Access to the Android and client-core fork repositories and their selected revision policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-075: Fork Android and shared client SDK identities and release inputs

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The Android repository is external to this Rust checkout and must be cloned at a pinned fork revision before implementation. The inspected upstream baseline is f77ec2f6883e324484e2f7cf6ce6d0939aa8e533. It contains a Kotlin-facing API with React Native and shared hyperswitch-client-core dependencies; renaming one namespace will not detach the product. Establish an owned SDK identity without prematurely changing payment behavior, cryptography, or terminal acquisition. Preserve applicable upstream license and attribution obligations, record reproducible dependency inputs, and distinguish Maven coordinates, application sample IDs, manifest authorities, resources, and shared JavaScript identifiers. This ticket establishes a buildable foundation used by subsequent terminal work. Existing checkout payment-sheet behavior remains a regression baseline; it is not evidence of certified card-present acceptance.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) - consume its completed, reviewed deliverables: Establish controlled forks, provenance and upstream maintenance.
- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) - consume its completed, reviewed deliverables: Establish SBOM, artifact signing and license provenance.
- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Android fork foundation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/app/build.gradle (verify pinned fork)`

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/Hyperswitch.kt (verify pinned fork)`

- `Proposed: external Android fork build identity and release-input manifest`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/build-identity`
- `client-core/dependency-graph`
- `sdk/release-inputs`

## Implementation plan

- [ ] Clone the approved Android and client-core forks at recorded revisions and inventory submodules, generated assets, packages, licenses, and release scripts.
- [ ] Create an owned namespace and Maven coordinate plan; apply it consistently to library modules, samples, manifests, resource prefixes, and dependency references.
- [ ] Record Gradle, Kotlin, Java, Android SDK/NDK, Node, package-manager, React Native, and client-core build inputs with integrity references.
- [ ] Remove accidental production release targets and configure sandbox endpoints and artifact destinations through explicit environment configuration.
- [ ] Build the renamed libraries and sample application; record upstream synchronization boundaries and preserved attribution.

## Acceptance criteria

- [ ] A clean checkout produces the owned SDK artifacts and installable sample without manual source edits.
- [ ] No duplicate provider authority, package, or resource collision occurs when upstream and forked SDKs coexist in a host test application.
- [ ] The manifest lists exact external repository revisions and build tool versions.
- [ ] License notices are preserved and product branding references are inventoried for later endpoint/UI work.
- [ ] The existing sandbox payment-sheet smoke flow remains reproducible with owned configuration.

## Validation scenarios

- [ ] Build debug and release variants from a fresh checkout using documented prerequisites.
- [ ] Inspect merged manifests and packaged resources for upstream identity collisions.
- [ ] Compare dependency lock information against the release-input manifest.
- [ ] Compile a host app that declares both SDK coordinates in an isolated compatibility experiment.

## Expected deliverables

- Pinned Android/client-core fork manifest
- Owned build identity and reproducible build configuration
- Baseline build and smoke-test evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved organization/repository names, product namespace, Maven coordinates, artifact registry, and signing ownership.
- [ ] Access to the Android and client-core fork repositories and their selected revision policy.

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
