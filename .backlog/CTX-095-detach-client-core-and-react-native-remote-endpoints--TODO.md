---
id: "CTX-095"
title: "Detach shared client-core and React Native remote endpoints"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "client-core"
component: "Shared client endpoint ownership"
depends_on: ["CTX-003", "CTX-004", "CTX-007", "CTX-012", "CTX-016", "CTX-075", "CTX-076", "CTX-082", "CTX-084", "CTX-093"]
requires_one_of: []
conflict_domains: ["android/initialization", "client-core/endpoints", "client-core/remote-assets"]
external_inputs: ["Owned service hosts, CDN/storage destinations, telemetry policy, and remote update product decision.", "Pinned client-core fork and retained Airborne/remote update documentation and signing model."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-095: Detach shared client-core and React Native remote endpoints

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The inspected Android SDK initializes shared React Native functionality and exposes overrides for backend, logging, asset, SDK configuration, confirm, and Airborne update endpoints. Rebranding the Kotlin package alone leaves network and remote-code/configuration dependencies that could continue to contact upstream services. Inventory each retained feature across the pinned Android/client-core forks, including defaults, redirects, environment fallback, bundled assets, analytics, and remote update channels. Route approved behavior to owned infrastructure and disable unused features explicitly. Mobile configuration must not download arbitrary tenant code or select uncontrolled hosts. If remote updates remain, establish ownership, signing/integrity validation, staged rollout, rollback, and release compatibility. This work preserves a documented baseline while allowing later removal of shared UI/runtime dependencies through separate architectural decisions.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) - consume its completed, reviewed deliverables: Establish controlled forks, provenance and upstream maintenance.
- [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) - consume its completed, reviewed deliverables: Establish a reproducible, isolated local development stack.
- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) - consume its completed, reviewed deliverables: Redact mobile logs, crashes, storage, and backups.


## Relevant code and ownership

Primary repository/workstream: **client-core / Shared client endpoint ownership**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/Hyperswitch.kt (verify pinned fork)`

- `External: juspay/hyperswitch-sdk-android/hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/model/Model.kt (verify pinned fork)`

- `Proposed: external hyperswitch-client-core endpoint and remote update configuration after pinned-tree discovery`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/initialization`
- `client-core/endpoints`
- `client-core/remote-assets`

## Implementation plan

- [ ] Trace native initialization and shared client-core endpoint resolution, including all default/fallback and remote asset/update paths.
- [ ] Configure owned sandbox/live endpoints for backend, logging, assets, configuration, confirm, and retained Airborne functions.
- [ ] Remove or explicitly disable unused upstream telemetry/update features and ensure failure does not fall back to upstream production.
- [ ] Implement authenticated asset/update integrity, approved host policies, and compatibility gates for any retained remote delivery mechanism.
- [ ] Capture network egress from all retained SDK flows and publish the owned dependency/endpoint manifest.

## Acceptance criteria

- [ ] Retained production features contact only approved hosts and declared third-party vendor services.
- [ ] Missing or invalid owned configuration fails explicitly without upstream production fallback.
- [ ] Remote assets/code/configuration are integrity-checked under the approved release policy.
- [ ] Sandbox and live endpoints cannot be mixed within one payment session.
- [ ] The dependency/endpoint manifest includes native and shared-runtime execution paths.

## Validation scenarios

- [ ] Capture cold-start, payment, error, asset-load, configuration-fetch, and update-check egress.
- [ ] Remove owned endpoint configuration and simulate service outages/redirects.
- [ ] Tamper with remote assets/update signatures and exercise rollback compatibility.
- [ ] Run the existing payment-sheet baseline with retained features after endpoint detachment.

## Expected deliverables

- Owned endpoint and remote dependency manifest
- Android/client-core endpoint detachment changes
- Egress and remote-update integrity evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Owned service hosts, CDN/storage destinations, telemetry policy, and remote update product decision.
- [ ] Pinned client-core fork and retained Airborne/remote update documentation and signing model.

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
