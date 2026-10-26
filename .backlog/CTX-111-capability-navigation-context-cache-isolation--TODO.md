---
id: "CTX-111"
title: "Implement capability-driven navigation and aggregator-scoped portal caches"
status: "TODO"
phase: 4
priority: "P0"
size: "M"
repository: "dashboard"
component: "Portal shell and data access"
depends_on: ["CTX-029", "CTX-034", "CTX-038", "CTX-108", "CTX-109"]
requires_one_of: []
conflict_domains: ["dashboard-cache", "dashboard-shell"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-111: Implement capability-driven navigation and aggregator-scoped portal caches

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The portal exposes a single aggregator workspace even though Hyperswitch has native organization, merchant-account and profile concepts. Build a presentation model from the BFF session that separates action capabilities from resource ownership. Menus and buttons should reflect allowed actions, while backend authorization remains authoritative on every request. Any shared query cache, router preload, persisted filter, websocket subscription or export notification must include environment and aggregator context. Context changes must cancel stale requests and prevent late responses from repainting another workspace. Do not rely on hiding the native merchant switcher alone. This shell is a common dependency for merchant, terminal, developer and payment screens and should give feature teams one consistent scoped client and loading/error convention.

## Prerequisites and dependency outputs

- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-108](CTX-108-white-label-dashboard-runtime-baseline--TODO.md) - consume its completed, reviewed deliverables: Fork and detach the Aggregator Portal runtime from upstream branding and services.
- [CTX-109](CTX-109-integrate-portal-bff-secure-sessions--TODO.md) - consume its completed, reviewed deliverables: Integrate the portal with secure BFF sessions and OIDC.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Portal shell and data access**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authorization/roles.rs](../crates/router/src/services/authorization/roles.rs)

- `Proposed: docs/portal/scoped-data-access.md`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-cache`
- `dashboard-shell`

## Implementation plan

- [ ] Create typed session/capability bindings appropriate to the pinned React/ReScript codebase and a centralized scoped API client.
- [ ] Replace native hierarchy navigation with aggregator workspace plus nested merchants, terminals, operations and developer areas.
- [ ] Namespace all query keys, route loaders, local preferences and realtime subscriptions by environment/aggregator and permitted merchant scope where relevant.
- [ ] Cancel or discard in-flight responses on logout/context change and clear sensitive data before rendering the next workspace.
- [ ] Provide shared unauthorized/not-found/session-expired states without inferring permission from frontend state alone.
- [ ] Document the required cache and API-client pattern for later screen agents.

## Acceptance criteria

- [ ] Each route obtains aggregator context from the authenticated session and cannot grant itself access through URL changes.
- [ ] Changing aggregator or environment clears previous data and prevents stale asynchronous responses from appearing.
- [ ] Queries, persisted filters and subscriptions include the documented context namespace.
- [ ] Capabilities govern visible actions, with rejected backend responses handled correctly after permission changes.
- [ ] Feature modules can reuse the shared client without raw native admin credentials or arbitrary tenant headers.

## Validation scenarios

- [ ] Run two-aggregator browser tests including slow responses, back navigation, two tabs and context switching.
- [ ] Review query/cache keys and test server-side authorization failures after stale capability data.
- [ ] Verify websocket teardown, export notifications and logout cleanup with synthetic records.

## Expected deliverables

- Scoped portal shell, capability model and API client.
- Portal cache/context-switch regression tests.
- Frontend tenant-isolation implementation guide.

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
