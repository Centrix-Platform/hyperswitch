---
id: "CTX-110"
title: "Implement verified custom domains and isolated runtime branding"
status: "TODO"
phase: 4
priority: "P1"
size: "L"
repository: "multi-repo"
component: "White-label tenancy"
depends_on: ["CTX-008", "CTX-016", "CTX-029", "CTX-034", "CTX-108", "CTX-109"]
requires_one_of: []
conflict_domains: ["dashboard-branding", "platform-ingress", "portal-domains"]
external_inputs: ["Controlled DNS zones/test hostnames, certificate-provider account and approved aggregator branding assets."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-110: Implement verified custom domains and isolated runtime branding

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Each licensed aggregator may present the portal under its own approved domain and branding, but a Host header or logo selection must never select authorization scope. Resolve a verified domain to permitted branding and identity configuration while deriving data access independently from the authenticated session. Unverified domains, dangling DNS and cross-tenant CDN cache entries can create account confusion or takeover risks. Runtime branding should remain validated data such as colors, names and image references; arbitrary tenant JavaScript is excluded. Define ownership verification, certificate renewal, reassignment and removal before allowing self-service. The design must account for asset storage ACLs, CSP, cookie scopes and safe error pages when branding resolution fails or an account is suspended.

## Prerequisites and dependency outputs

- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-108](CTX-108-white-label-dashboard-runtime-baseline--TODO.md) - consume its completed, reviewed deliverables: Fork and detach the Aggregator Portal runtime from upstream branding and services.
- [CTX-109](CTX-109-integrate-portal-bff-secure-sessions--TODO.md) - consume its completed, reviewed deliverables: Integrate the portal with secure BFF sessions and OIDC.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / White-label tenancy**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [config/config.example.toml](../config/config.example.toml)

- `Proposed: services/platform-control/src/domains/`

- `Proposed: infra/domains/`

- `External: juspay/hyperswitch-control-center/config/config.toml (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-branding`
- `platform-ingress`
- `portal-domains`

## Implementation plan

- [ ] Define domain ownership/verification states and a branding schema with safe asset types, size limits and contrast/accessibility requirements.
- [ ] Implement verified DNS/token-based ownership onboarding, revalidation, certificate lifecycle and domain-removal handling through approved infrastructure APIs.
- [ ] Resolve trusted ingress hostnames to branding records while rejecting unknown hosts and separating domain identity from session authority.
- [ ] Namespace asset/CDN caches by verified domain, environment and configuration version; prevent cross-tenant cache poisoning.
- [ ] Apply CSP and sanitized assets without tenant-provided executable scripts, and integrate custom-domain authentication redirects with CTX-109.
- [ ] Document domain transfer, suspension and certificate incident procedures.

## Acceptance criteria

- [ ] Only verified, active domains serve aggregator branding and unknown hosts do not render another aggregator configuration.
- [ ] Session authority remains unchanged by a forged Host or forwarded-host value.
- [ ] Branding/asset caches cannot return one aggregator content to another host.
- [ ] Domain removal and revalidation invalidate stale routing and certificate associations.
- [ ] Branding supports approved accessibility requirements and rejects executable or unsafe assets.

## Validation scenarios

- [ ] Exercise verification, expired proof, dangling DNS, reassignment and removal using controlled test domains.
- [ ] Test Host/forwarded-host spoofing, cache-key variance and cookie behavior across two aggregators.
- [ ] Inspect CSP enforcement, asset validation and certificate-renewal failure handling.

## Expected deliverables

- Verified domain and branding APIs/configuration.
- Isolated asset/CDN deployment rules.
- Domain lifecycle and test evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Controlled DNS zones/test hostnames, certificate-provider account and approved aggregator branding assets.

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
