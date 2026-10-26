---
id: "CTX-004"
title: "Establish controlled forks, provenance and upstream maintenance"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "architecture"
depends_on: ["CTX-003"]
requires_one_of: []
conflict_domains: ["fork-provenance", "release-input-manifest"]
external_inputs: ["Approved fork organization, repository destinations, package namespace and release owners."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-004: Establish controlled forks, provenance and upstream maintenance

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The current git remote points to the public Hyperswitch upstream. Building a white-label product requires controlled fork destinations and a repeatable upstream update process across the core, dashboard and SDK/client-core repositories. Preserve native names inside compatibility layers to avoid an unmaintainable mechanical rename. Detach product-facing brands, upstream telemetry and hosted endpoints through explicit inventories while keeping required attribution. Creating a planning ticket does not authorize remote repository creation, changing existing remotes, publishing packages or modifying user changes. Implement the fork workflow once destinations and release ownership are known, with small auditable differences and an update procedure that carries integration and certification impact forward.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / architecture**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [LICENSE](../LICENSE)

- [NOTICE](../NOTICE)

- [.github/workflows](../.github/workflows)

- [config](../config)

- `External: juspay/hyperswitch-control-center/config/config.toml (verify pinned fork)`

- `Proposed: docs/engineering/fork-maintenance.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `fork-provenance`
- `release-input-manifest`

## Implementation plan

- [ ] Document desired fork destinations, access model, branch/release policy and relationship to upstream.
- [ ] Create an inventory of product-visible brands, outbound hosts, hosted assets, telemetry and module publishing coordinates.
- [ ] Define an upstream import workflow with isolated branches, conflict resolution and baseline compatibility validation.
- [ ] Assign stable ownership to notices, third-party license inventory and source provenance.
- [ ] Define which connector, SDK or crypto changes trigger recertification review.

## Acceptance criteria

- [ ] Every repository has a documented upstream/fork relationship and release owner.
- [ ] A clean rehearsal can import an upstream change without overwriting product-specific adapters.
- [ ] Branding and endpoint detachment inventories cover dashboard, SDK, client-core and runtime configuration.
- [ ] License and attribution changes are reviewed and traceable.
- [ ] Existing repository remotes and user edits remain untouched until the specific fork operation is authorized.

## Validation scenarios

- [ ] Rehearse an upstream import and rollback in an isolated checkout.
- [ ] Compare outbound endpoint inventory against source/configuration search results.
- [ ] Check third-party notices and source URLs against the pinned release manifest.

## Expected deliverables

- Fork/provenance operating procedure
- Brand and outbound-host inventory
- Upstream synchronization rehearsal

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved fork organization, repository destinations, package namespace and release owners.

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
