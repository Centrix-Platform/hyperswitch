---
id: "CTX-007"
title: "Establish a reproducible, isolated local development stack"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "core"
component: "developer-environment"
depends_on: ["CTX-003"]
requires_one_of: []
conflict_domains: ["local-dev-infra"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-007: Establish a reproducible, isolated local development stack

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The existing core has Compose configurations, migrations and development recipes, with local user changes in docker-compose.yml and package-lock.json. Future agents need a repeatable environment for native baseline flows, scoped APIs and failure injection without editing shared developer settings or accidentally connecting to real acquirers. Build an additive local profile or override with explicit service names, ports, disposable synthetic data and non-production secrets. Keep sandbox and live identifiers/configuration distinct even in test fixtures. The dashboard and SDK checkouts are external inputs until provisioned; document their integration points rather than fabricating local paths. This task produces a usable development baseline, not production deployment or a replacement for the later operational hardening work.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **core / developer-environment**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [docker-compose.yml](../docker-compose.yml)

- [docker-compose-development.yml](../docker-compose-development.yml)

- [config/config.example.toml](../config/config.example.toml)

- [justfile](../justfile)

- [migrations](../migrations)

- `Proposed: docker-compose.ctx-development.yml`

- `Proposed: scripts/ctx-dev`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `local-dev-infra`

## Implementation plan

- [ ] Document baseline prerequisites and commands for the pinned Rust/Node/Android components.
- [ ] Add an isolated Compose override or equivalent local profile for core, PostgreSQL, Redis and stub services.
- [ ] Define synthetic seed/reset flows, per-agent ports/namespaces and local secret provisioning.
- [ ] Expose health checks and an end-to-end local smoke command with all external hosts stubbed or explicitly blocked.
- [ ] Document how external dashboard/SDK checkouts attach and how to remove only task-owned resources.

## Acceptance criteria

- [ ] A clean setup can run the selected baseline and smoke flow from documented commands.
- [ ] Multiple worktrees can run without overwriting a shared database or colliding on fixed ports.
- [ ] Seed data contains no real cardholder, merchant or operational credentials.
- [ ] The local flow cannot silently reach live acquirer endpoints.
- [ ] Existing user-edited files remain intact or an explicit reviewed additive diff is provided.

## Validation scenarios

- [ ] Run setup twice and confirm idempotent health/seed behavior.
- [ ] Start a second isolated instance with distinct ports and verify its data stays separate.
- [ ] Inspect network destinations during the smoke scenario.

## Expected deliverables

- Development profile and setup guide
- Synthetic seed/reset tooling
- Local smoke command

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
