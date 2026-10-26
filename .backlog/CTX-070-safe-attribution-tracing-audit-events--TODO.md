---
id: "CTX-070"
title: "Instrument payment attribution and privileged actions without sensitive leakage"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "payment-observability"
depends_on: ["CTX-012", "CTX-014", "CTX-019", "CTX-027", "CTX-028", "CTX-029", "CTX-049", "CTX-064"]
requires_one_of: []
conflict_domains: ["contracts:audit-events", "observability:payment-attribution", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-070: Instrument payment attribution and privileged actions without sensitive leakage

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Swarm-implemented services need a common trace and audit vocabulary to reconstruct decisions across SDK sessions, gateway admission, Rust execution, acquirer inquiry and webhooks. Propagate safe operation/attempt/event identifiers plus aggregator, merchant, environment and configuration versions where access policy permits. Trace data must never become a shadow store for raw card data, encrypted SAD, credentials or complete terminal payloads. Separate operational metrics from immutable security/audit evidence, apply tenant-scoped access and choose bounded metric labels to avoid cardinality explosions. This ticket adds platform-specific attribution to the baseline redaction infrastructure; it does not enable upstream telemetry by default. Record routing eligibility and state changes with safe reason codes rather than unbounded request/response dumps.

## Prerequisites and dependency outputs

- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) - consume its completed, reviewed deliverables: Persist authoritative payment admission and attempt ownership.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / payment-observability**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/kafka.rs](../crates/router/src/services/kafka.rs)

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- `Proposed: platform/observability/`

- `Proposed: contracts/audit-events/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:audit-events`
- `observability:payment-attribution`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define trace propagation, safe attribute allowlists and audit event schemas.
- [ ] Instrument admission, dispatch, inquiry, lifecycle, key and configuration transitions.
- [ ] Add payload redaction guards at HTTP, connector, SDK-ingress and job boundaries.
- [ ] Enforce tenant-scoped observability access and retention/classification.
- [ ] Expose operation/UNKNOWN age and state-transition metrics without unbounded labels.

## Acceptance criteria

- [ ] One synthetic operation can be followed across all participating services.
- [ ] Forbidden payload/secret fixtures never appear in logs, traces or audit events.
- [ ] Cross-aggregator observability access requires explicit platform authority.
- [ ] Metric labels avoid payment/customer IDs and other unbounded dimensions.
- [ ] Privileged actions record actor, target, reason, version and result.

## Validation scenarios

- [ ] Inject sensitive sentinel strings through error paths and scan telemetry sinks.
- [ ] Trace timeout/recovery and duplicate-request scenarios.
- [ ] Review metric cardinality and tenant-scoped log search permissions.

## Expected deliverables

- Instrumentation/redaction adapters and safe attribute catalog.
- Audit schemas and telemetry leakage regression checks.

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
