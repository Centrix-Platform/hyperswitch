---
id: "CTX-108"
title: "Fork and detach the Aggregator Portal runtime from upstream branding and services"
status: "TODO"
phase: 4
priority: "P0"
size: "M"
repository: "dashboard"
component: "Portal foundation"
depends_on: ["CTX-003", "CTX-004", "CTX-006", "CTX-010", "CTX-012"]
requires_one_of: []
conflict_domains: ["dashboard-build", "dashboard-runtime", "dashboard-shell"]
external_inputs: ["Platform product name, approved logo/support assets and intended sandbox/live endpoint domains."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-108: Fork and detach the Aggregator Portal runtime from upstream branding and services

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The inspected Hyperswitch Control Center is a separate React and ReScript application with some TypeScript, not a frontend directory in this Rust checkout. Its README.md, package.json and config/config.toml are known upstream entry points; locate actual modules after checking out the pinned fork. Establish a reproducible portal baseline that uses the platform domain language and approved backend, asset and telemetry endpoints. Preserve applicable licenses while changing product names, support destinations, deployment metadata and environment configuration. Avoid a cosmetic rename that leaves upstream remote configuration or production fallback endpoints active. This ticket establishes the shared application shell and configuration contract used by subsequent portal work; it does not implement merchant onboarding or grant users cross-aggregator visibility.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) - consume its completed, reviewed deliverables: Establish controlled forks, provenance and upstream maintenance.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) - consume its completed, reviewed deliverables: Establish CI quality, migration and contract check lanes.
- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Portal foundation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `External: juspay/hyperswitch-control-center/README.md (verify pinned fork)`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`

- `External: juspay/hyperswitch-control-center/config/config.toml (verify pinned fork)`

- `Proposed: docs/portal/runtime-configuration.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-build`
- `dashboard-runtime`
- `dashboard-shell`

## Implementation plan

- [ ] Inventory retained build/runtime dependencies and endpoint sources in the pinned React/ReScript fork, including remote assets, logging and optional features.
- [ ] Create an environment-validated runtime configuration schema for portal API, authentication, assets and support destinations, failing closed on missing live configuration.
- [ ] Replace product names, logos, favicon, document metadata, support links and sample account references while preserving legal attribution.
- [ ] Build a platform vocabulary adapter so aggregator, merchant and terminal names do not expose native MerchantAccount/BusinessProfile terminology.
- [ ] Produce a reproducible development build and smoke journey against platform sandbox APIs; document exact build commands and ownership of generated bindings.

## Acceptance criteria

- [ ] Portal builds from a clean checkout using the pinned package manager and compiler versions.
- [ ] All enabled network destinations are inventoried and belong to an explicit environment allowlist.
- [ ] Missing live configuration produces an actionable startup error rather than an upstream fallback.
- [ ] Navigation, login shell and metadata use platform terminology and retained attribution remains intact.
- [ ] A non-production smoke session loads the configured backend without embedding operational API keys.

## Validation scenarios

- [ ] Run the actual fork build, formatter and relevant existing lint checks.
- [ ] Capture browser network traffic through startup and one retained feature, comparing destinations to the allowlist.
- [ ] Exercise invalid and omitted runtime settings and inspect generated artifacts for upstream production URLs and secrets.

## Expected deliverables

- Pinned portal fork/runtime inventory and build instructions.
- Validated environment configuration and white-label application shell.
- Baseline portal smoke and endpoint allowlist evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Platform product name, approved logo/support assets and intended sandbox/live endpoint domains.

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
