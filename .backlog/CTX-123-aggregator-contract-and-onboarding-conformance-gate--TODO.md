---
id: "CTX-123"
title: "Qualify aggregator portal-to-SDK contracts end to end"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Integration qualification"
depends_on: ["CTX-071", "CTX-072", "CTX-073", "CTX-107", "CTX-110", "CTX-112", "CTX-113", "CTX-114", "CTX-115", "CTX-116", "CTX-117", "CTX-118", "CTX-119", "CTX-120", "CTX-121", "CTX-122", "CTX-143"]
requires_one_of: []
conflict_domains: ["cross-repo-conformance", "sandbox-fixtures"]
external_inputs: ["Non-production acquirer/terminal fixtures or simulator credentials; controlled hardware if the selected vendor cannot be simulated."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-123: Qualify aggregator portal-to-SDK contracts end to end

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A B2B2B integration spans portal sessions, aggregator backend keys, merchant provisioning, device enrollment, ephemeral SDK authority and payment/reconciliation state. Unit tests within one fork cannot establish that these contracts agree. Build an executable conformance gate using one representative aggregator and adversarial second-aggregator fixtures against pinned core, platform, portal and Android artifacts. The gate should exercise the actual asynchronous states and partial failures, not replace acquirer approval or PCI assessment. Use simulators and sandbox networks for automation; any hardware-required segment must be declared with reproducible setup and captured evidence. Keep this gate financial-side-effect-free outside specifically controlled sandbox flows and never duplicate live authorizations to compare implementations.

## Prerequisites and dependency outputs

- [CTX-071](CTX-071-cross-aggregator-isolation-release-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on adversarial ownership and privilege isolation.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-107](CTX-107-prove-approved-terminal-to-acquirer-pilot-and-reconciliation-gate--TODO.md) - consume its completed, reviewed deliverables: Prove the approved terminal-to-acquirer pilot and reconciliation gate.
- [CTX-110](CTX-110-verified-custom-domains-runtime-branding--TODO.md) - consume its completed, reviewed deliverables: Implement verified custom domains and isolated runtime branding.
- [CTX-112](CTX-112-merchant-onboarding-lifecycle-portal--TODO.md) - consume its completed, reviewed deliverables: Build merchant onboarding, review and lifecycle screens.
- [CTX-113](CTX-113-terminal-inventory-linking-lifecycle-portal--TODO.md) - consume its completed, reviewed deliverables: Build terminal inventory, enrollment and merchant-binding screens.
- [CTX-114](CTX-114-acquirer-secret-configuration-projections-portal--TODO.md) - consume its completed, reviewed deliverables: Build acquirer configuration and write-only credential management.
- [CTX-115](CTX-115-versioned-routing-policy-editor--TODO.md) - consume its completed, reviewed deliverables: Build eligible routing policy editing, dry-run and activation.
- [CTX-116](CTX-116-developer-key-and-sdk-session-portal--TODO.md) - consume its completed, reviewed deliverables: Build scoped key, SDK-session and rotation tooling.
- [CTX-117](CTX-117-team-memberships-roles-context-switching--TODO.md) - consume its completed, reviewed deliverables: Build team invitations, scoped roles and deliberate context switching.
- [CTX-118](CTX-118-payment-operations-and-unknown-outcome-portal--TODO.md) - consume its completed, reviewed deliverables: Build payment operations with safe capture, refund and UNKNOWN handling.
- [CTX-119](CTX-119-reconciliation-reports-and-secure-exports-portal--TODO.md) - consume its completed, reviewed deliverables: Build reconciliation reports and tenant-safe exports.
- [CTX-120](CTX-120-webhook-subscription-and-delivery-portal--TODO.md) - consume its completed, reviewed deliverables: Build signed webhook configuration, delivery inspection and replay tooling.
- [CTX-121](CTX-121-isolated-platform-operator-console--TODO.md) - consume its completed, reviewed deliverables: Build an isolated platform operator and audited support console.
- [CTX-122](CTX-122-platform-openapi-and-integration-documentation--TODO.md) - consume its completed, reviewed deliverables: Finalize the public platform API contract, examples and native admin isolation.
- [CTX-143](CTX-143-dispute-case-and-evidence-handoff-portal--TODO.md) - consume its completed, reviewed deliverables: Build dispute case, evidence and authorized handoff workflows.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Integration qualification**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [cypress-tests/README.md](../cypress-tests/README.md)

- [cypress-tests/cypress.config.js](../cypress-tests/cypress.config.js)

- [crates/router/src/routes/app.rs](../crates/router/src/routes/app.rs)

- `Proposed: tests/platform-conformance/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `cross-repo-conformance`
- `sandbox-fixtures`

## Implementation plan

- [ ] Define a versioned cross-repository compatibility matrix and deterministic fixtures for two aggregators, merchants, devices and processing accounts.
- [ ] Automate backend onboarding, portal lifecycle, terminal enrollment/binding and SDK-session exchange using public contracts.
- [ ] Execute sandbox charge, duplicate submission, pending/UNKNOWN resolution, completion, capture/refund and settlement matching journeys.
- [ ] Add negative ownership/delegation cases for portal, backend keys, SDK tokens, webhooks, exports and document links.
- [ ] Capture artifact versions, simulator/hardware assumptions, request/operation references and redacted evidence in one qualification report.
- [ ] Integrate stable automated portions into CI and provide a declared hardware qualification job for remaining cases.

## Acceptance criteria

- [ ] A clean environment runs the full approved sandbox lifecycle using pinned artifacts and documented fixtures.
- [ ] All ownership-negative cases fail without disclosing or mutating another aggregator resources.
- [ ] Duplicate/restart/timeout scenarios converge without creating an extra admitted financial operation.
- [ ] Portal, SDK and public API agree on states, identifiers, amounts and supported versions.
- [ ] Hardware-only or external dependencies are explicitly classified and do not masquerade as automated passes.
- [ ] The report identifies reproducible failures and attaches redacted evidence to the tested release candidate.

## Validation scenarios

- [ ] Run the complete conformance pack from a clean seeded environment.
- [ ] Deliberately break a schema/state/ownership invariant and confirm the gate detects the regression.
- [ ] Compare portal/SDK views to authoritative operation/journal/reconciliation records after fault scenarios.

## Expected deliverables

- Cross-repository conformance runner and fixtures.
- Version compatibility matrix.
- Release-bound integration qualification report.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Non-production acquirer/terminal fixtures or simulator credentials; controlled hardware if the selected vendor cannot be simulated.

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
