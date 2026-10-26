---
id: "CTX-054"
title: "Evaluate active terminal binding and certification before routing"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "terminal-routing-eligibility"
depends_on: ["CTX-025", "CTX-026", "CTX-029", "CTX-047", "CTX-050"]
requires_one_of: []
conflict_domains: ["config:certification-evaluator", "configuration-publication-boundary", "payment-execution-state-boundary", "payment:terminal-eligibility"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-054: Evaluate active terminal binding and certification before routing

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A payload's terminal ID, reported firmware or requested TID cannot establish routing permission. Resolve the authenticated device deployment and its merchant, then evaluate active processing bindings against certification approval, observed device/app versions, encryption domain, acquirer enrollment, currency and operation capabilities. Aggregator routing preferences may rank only the resulting eligible set. Certification expiry or missing version evidence must fail according to an explicit policy rather than using a permissive default. This evaluator is side-effect free and suitable for future implementation comparison, while the final admission/execution path still rechecks critical revocation. Keep old binding versions available for recovery of existing attempts; removing eligibility for new charges must not erase original-route information.

## Prerequisites and dependency outputs

- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.


## Relevant code and ownership

Primary repository/workstream: **platform / terminal-routing-eligibility**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments/routing.rs](../crates/router/src/core/payments/routing.rs)

- [crates/router/src/core/routing.rs](../crates/router/src/core/routing.rs)

- `Proposed: platform/terminals/eligibility/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `config:certification-evaluator`
- `configuration-publication-boundary`
- `payment-execution-state-boundary`
- `payment:terminal-eligibility`

## Implementation plan

- [ ] Implement trusted deployment/device lookup and ownership chain verification.
- [ ] Evaluate lifecycle, certification dimensions, encryption domain and capability intersection.
- [ ] Return typed eligibility decisions and safe rejection reasons.
- [ ] Define freshness/revocation checks at admission and immediately before dispatch.
- [ ] Publish deterministic eligibility vectors for supported terminal/acquirer combinations.

## Acceptance criteria

- [ ] Unbound, revoked or foreign devices produce no eligible route.
- [ ] Unsupported firmware/app/currency/operation combinations fail closed.
- [ ] Routing preferences cannot introduce an ineligible connector.
- [ ] New-charge suspension does not destroy historical recovery bindings.
- [ ] Eligibility output includes the exact approved binding and certification versions.

## Validation scenarios

- [ ] Run approved/expired/revoked/unknown-version certification fixtures.
- [ ] Try a valid terminal token with another merchant binding.
- [ ] Suspend a terminal between admission and dispatch and verify policy.

## Expected deliverables

- Terminal eligibility service/library.
- Deterministic decision fixtures and rejection contract.

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
