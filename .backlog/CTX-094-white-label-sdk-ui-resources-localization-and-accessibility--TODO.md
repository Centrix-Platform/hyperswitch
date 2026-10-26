---
id: "CTX-094"
title: "White-label optional SDK UI, resources, localization, and accessibility"
status: "TODO"
phase: 3
priority: "P1"
size: "M"
repository: "android"
component: "SDK presentation"
depends_on: ["CTX-006", "CTX-075", "CTX-076", "CTX-082", "CTX-090", "CTX-092", "CTX-093"]
requires_one_of: []
conflict_domains: ["android/branding-resources", "android/optional-ui"]
external_inputs: ["Product naming, brand assets, supported locales, terminal screen sizes, and accessibility requirements.", "Approved user-facing wording for uncertain outcomes and support escalation."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-094: White-label optional SDK UI, resources, localization, and accessibility

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The aggregator APK should present an owned, configurable payment experience while keeping payment authority independent of styling. Provide an optional SDK UI layer above the stable orchestration API, allowing aggregators with custom screens to use a headless facade. Load approved branding data from signed configuration or validated initialization, including colors, logos, display names, and support links; do not execute tenant-supplied JavaScript. UI states must accurately represent pending, unknown, completion-required, declined, and successful outcomes, and must not encourage a second payment while an operation is unresolved. Resource naming and localization must avoid conflicts with host applications. Accessibility, large font settings, screen readers, rotation, and terminal-specific screen sizes are part of the delivery contract rather than a post-certification cosmetic change. This ticket is always required for public branding/resource isolation and an explicit presentation decision. A reviewed headless-only outcome satisfies it without building a new optional UI module; presentation implementation is required only if selected in the product scope.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) - consume its completed, reviewed deliverables: Fork Android and shared client SDK identities and release inputs.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) - consume its completed, reviewed deliverables: Redact mobile logs, crashes, storage, and backups.


## Relevant code and ownership

Primary repository/workstream: **android / SDK presentation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork optional gateway-sdk-ui module`

- `Proposed: external Android fork namespaced resources and localization`

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/Hyperswitch.kt (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/branding-resources`
- `android/optional-ui`

## Implementation plan

- [ ] Record whether CTX-001 selects headless-only delivery or optional SDK presentation, including the supported host integration surface.
- [ ] Isolate product namespaces, resource names, public branding metadata and approved asset handling without changing payment authority.
- [ ] Keep headless workflow APIs independent of presentation runtime/resources and document the host contract for pending, UNKNOWN and completion-required states.
- [ ] If presentation is selected, implement validated themes and authoritative state messaging; forbid a retry-as-new-charge action for unresolved operations.
- [ ] If presentation is selected, externalize/localize strings and verify screen-reader, contrast, font scaling, rotation and approved terminal layouts.
- [ ] Compile a headless reference host for either decision; produce visual previews/accessibility evidence only for selected presentation modules.

## Acceptance criteria

- [ ] A recorded headless-only or presentation-selected decision defines the delivered scope.
- [ ] A host can integrate and recover payments using the headless SDK without optional UI runtime/resources.
- [ ] Branding/resource changes cannot alter endpoints, permissions, amount or processing bindings.
- [ ] The headless host contract and sample preserve original operation identity during UNKNOWN recovery.
- [ ] When presentation is selected, localized accessible screens represent financial states accurately and never offer an unsafe new charge for UNKNOWN.
- [ ] Owned branding/resource scope is detached from upstream presentation while required attribution remains intact.

## Validation scenarios

- [ ] Build a Kotlin/Java headless sample with optional UI dependencies absent and exercise confirmation, pending and recovery results.
- [ ] Embed two synthetic branding configurations in separate host builds and verify namespace/resource isolation and unchanged payment contracts.
- [ ] When presentation is selected, inspect supported form factors, localization, font scaling and screen-reader flows; otherwise record the reviewed headless host-state contract.
- [ ] Verify an ambiguous result in the chosen sample returns to the original operation rather than submitting a second charge.

## Expected deliverables

- Presentation decision plus branding/resource namespace isolation
- Verified headless host integration and optional UI module only when selected
- Selected-UI localization/accessibility evidence or reviewed headless host-state guidance

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Product naming, brand assets, supported locales, terminal screen sizes, and accessibility requirements.
- [ ] Approved user-facing wording for uncertain outcomes and support escalation.

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
