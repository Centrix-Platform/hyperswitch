---
id: "CTX-115"
title: "Build eligible routing policy editing, dry-run and activation"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "dashboard"
component: "Routing configuration UI"
depends_on: ["CTX-054", "CTX-055", "CTX-068", "CTX-111", "CTX-114"]
requires_one_of: []
conflict_domains: ["dashboard-routing"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-115: Build eligible routing policy editing, dry-run and activation

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregator routing policies must operate inside terminal, merchant, currency, certification and encryption-domain constraints. A generic list of available connector names is insufficient for card-present traffic: ciphertext prepared for one acquirer may not be usable by another, and an UNKNOWN financial outcome must not trigger a new route automatically. The backend eligibility service and configuration publisher own these rules. The portal should edit versioned policy drafts, validate references, show safe dry-run explanations and activate approved revisions without altering attempts already dispatched. Keep native Hyperswitch routing representations behind the compatibility adapter. This ticket gives operators visibility and control over policy lifecycle while preventing frontend configuration from bypassing certified processing boundaries.

## Prerequisites and dependency outputs

- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.
- [CTX-114](CTX-114-acquirer-secret-configuration-projections-portal--TODO.md) - consume its completed, reviewed deliverables: Build acquirer configuration and write-only credential management.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Routing configuration UI**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/routing.rs](../crates/router/src/core/routing.rs)

- [crates/router/src/routes/routing.rs](../crates/router/src/routes/routing.rs)

- [crates/api_models/src/routing.rs](../crates/api_models/src/routing.rs)

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-routing`

## Implementation plan

- [ ] Implement draft routing policy create/edit using a typed platform model and eligible connector/binding selectors.
- [ ] Integrate validation/dry-run endpoints with explanations for excluded routes, unsupported currencies and incompatible encryption/certification domains.
- [ ] Display policy diffs, version history and merchant/terminal impact before staged activation.
- [ ] Activate/deactivate through server-controlled version checks and optional approval policy, recording actor and reason.
- [ ] Show frozen route snapshots for historical attempts and clearly distinguish safe new-attempt failover from uncertain financial outcomes.
- [ ] Document rollback as publishing a valid policy revision rather than mutating past attempt history.

## Acceptance criteria

- [ ] Policies cannot reference another aggregator configuration or bypass backend eligibility rules.
- [ ] Dry runs are side-effect-free and never submit an authorization to an acquirer.
- [ ] Activation is versioned and rejects stale editor updates.
- [ ] Already admitted/dispatched attempts retain their frozen route and credential/configuration versions.
- [ ] Incompatible ciphertext routes and UNKNOWN automatic reroutes are rejected or unavailable.
- [ ] Policy history identifies actor, reason and effective version.

## Validation scenarios

- [ ] Run editor journeys for invalid policies, dry-run, staged activation and stale-version conflicts.
- [ ] Compare portal previews with backend eligibility fixtures including encryption-domain/certification failures.
- [ ] Verify policy changes do not alter historical attempts and dry runs make no financial network calls.

## Expected deliverables

- Versioned routing editor and impact/dry-run views.
- Routing lifecycle and eligibility E2E evidence.
- Operator policy activation/rollback guide.

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
