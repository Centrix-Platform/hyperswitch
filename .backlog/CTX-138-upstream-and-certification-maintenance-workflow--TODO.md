---
id: "CTX-138"
title: "Establish upstream security, connector and certification maintenance"
status: "TODO"
phase: 4
priority: "P1"
size: "M"
repository: "multi-repo"
component: "Fork lifecycle"
depends_on: ["CTX-003", "CTX-004", "CTX-010", "CTX-011", "CTX-013", "CTX-025", "CTX-073", "CTX-098", "CTX-130", "CTX-135"]
requires_one_of: []
conflict_domains: ["certification-evidence-registry", "certification-registry", "fork-maintenance", "upstream-sync"]
external_inputs: ["Access to selected upstream/vendor security channels and terminal/acquirer change-control contacts; external subscriptions/communications require the approved organization workflow."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-138: Establish upstream security, connector and certification maintenance

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Forking the engine, dashboard and Android/client-core creates an ongoing responsibility to absorb upstream fixes without silently changing payment behavior or invalidating approved terminal combinations. Track pinned commits, local patches, licenses, security advisories and connector protocol changes across repositories. A dependency upgrade can affect cryptography, capture flow, Android packaging, acquirer message mapping or certification requirements even when the public API is unchanged. Establish an ownership and evidence workflow rather than automatically merging all upstream changes. Changes should run the existing compatibility/security/conformance gates and trigger external recertification review when relevant. Prepare subscriptions and review schedules, but do not contact third parties or enable unsolicited outbound notifications during implementation without the established authorized workflow.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) - consume its completed, reviewed deliverables: Establish controlled forks, provenance and upstream maintenance.
- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) - consume its completed, reviewed deliverables: Establish SBOM, artifact signing and license provenance.
- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-130](CTX-130-expand-contract-upgrades-and-client-deprecation--TODO.md) - consume its completed, reviewed deliverables: Implement staged upgrades, client compatibility and safe rollback.
- [CTX-135](CTX-135-signed-release-candidate-and-promotion-pipeline--TODO.md) - consume its completed, reviewed deliverables: Build signed release candidates and gated environment promotion.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Fork lifecycle**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [Cargo.toml](../Cargo.toml)

- [.github/workflows/CI-pr.yml](../.github/workflows/CI-pr.yml)

- [.github/CODEOWNERS](../.github/CODEOWNERS)

- `Proposed: docs/engineering/upstream-maintenance.md`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `certification-evidence-registry`
- `certification-registry`
- `fork-maintenance`
- `upstream-sync`

## Implementation plan

- [ ] Maintain a cross-repository upstream/pin/patch inventory with owners, update cadence and security support policy.
- [ ] Create automated advisory/dependency/commit-diff collection and classify changes affecting connectors, crypto, terminal software, SDK behavior and data contracts.
- [ ] Define controlled upstream synchronization with isolated branches, conflict review and preservation of platform boundaries/attribution.
- [ ] Map material changes to regression suites and certification/change-control review in the terminal/acquirer registry.
- [ ] Build release notes and upgrade recommendations with evidence and explicit compatibility/deprecation implications.
- [ ] Rehearse one representative security or connector upgrade through non-production qualification and document response timelines.

## Acceptance criteria

- [ ] Every fork and critical dependency has a known upstream, pinned baseline, owner and supported update policy.
- [ ] Security advisories and relevant connector/terminal changes create reviewable tracked work.
- [ ] Updates cannot bypass contract, tenancy, financial-state or certification impact checks.
- [ ] Certification-sensitive changes identify the correct external reviewer and required evidence before release.
- [ ] Local patches and applicable licenses remain discoverable across synchronization.
- [ ] A non-production update rehearsal demonstrates the maintenance workflow end to end.

## Validation scenarios

- [ ] Compare inventory against actual manifests/submodules and release manifests.
- [ ] Inject a sample advisory/material connector diff and verify classification/routing.
- [ ] Run representative upstream upgrade qualification with schema, SDK and payment conformance checks.

## Expected deliverables

- Upstream/dependency/patch ownership register.
- Security and certification change-control workflow.
- Upgrade rehearsal and release-note templates.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Access to selected upstream/vendor security channels and terminal/acquirer change-control contacts; external subscriptions/communications require the approved organization workflow.

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
