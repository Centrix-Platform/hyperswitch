---
id: "CTX-016"
title: "Secure ingress and isolate native admin and trusted-header paths"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "ingress"
depends_on: ["CTX-005", "CTX-008", "CTX-009", "CTX-014"]
requires_one_of: []
conflict_domains: ["authentication-authorization-boundary", "ingress-routing", "trusted-request-context"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-016: Secure ingress and isolate native admin and trusted-header paths

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Public customers must call the platform-owned API, not native Hyperswitch administration endpoints with a tenant or merchant header of their choosing. Introduce ingress trust rules that authenticate public traffic, enforce environment/audience separation and keep native admin/internal routes private. A reverse proxy must strip untrusted forwarded identity, merchant/profile/tenant routing and internal-key headers before adding server-resolved context. Separate platform operator and aggregator surfaces without relying on hidden navigation. TLS, allowed hosts, callback ingress and request-size/time budgets need documented ownership across edge and application layers. This foundation makes later scoped repositories and service identities meaningful; it must not introduce a shared public master key as a shortcut.

## Prerequisites and dependency outputs

- [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) - consume its completed, reviewed deliverables: Define service ownership, execution ports and the Kotlin migration boundary.
- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / ingress**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/app.rs](../crates/router/src/routes/app.rs)

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [config](../config)

- `Proposed: infra/ingress`

- `Proposed: docs/security/ingress-trust.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `authentication-authorization-boundary`
- `ingress-routing`
- `trusted-request-context`

## Implementation plan

- [ ] Inventory public, portal, native-admin, internal-service and callback route surfaces.
- [ ] Define TLS/host/environment routing, WAF/rate-limit placement and trusted proxy boundaries.
- [ ] Strip client-supplied internal identity/tenant headers and bind resolved context only after authentication.
- [ ] Keep native admin/internal APIs reachable only through authorized workloads or isolated operator access.
- [ ] Document callback exception authentication, body limits, timeout budgets and audit signals.

## Acceptance criteria

- [ ] A public client cannot reach native admin operations or inject a different native tenant/profile.
- [ ] Sandbox credentials/hosts are rejected at live boundaries.
- [ ] Trusted internal context has authenticated provenance and cannot be supplied by an arbitrary caller.
- [ ] Callback routes require their own verified authentication and are not general API bypasses.
- [ ] Operator access is separate and auditable.

## Validation scenarios

- [ ] Probe public/native route inventory using invalid credentials and forged routing/forwarded headers.
- [ ] Exercise cross-environment, host-spoofing, oversized-body and timeout cases.
- [ ] Verify authorized internal connectivity and denied untrusted connectivity in the sandbox topology.

## Expected deliverables

- Ingress/private route policy
- Trusted-header sanitization implementation
- Edge trust-boundary validation evidence

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
