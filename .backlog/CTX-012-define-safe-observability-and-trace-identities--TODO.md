---
id: "CTX-012"
title: "Define safe observability, trace IDs and redaction defaults"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "observability"
depends_on: ["CTX-001", "CTX-006", "CTX-014"]
requires_one_of: []
conflict_domains: ["security-data-classification", "telemetry-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-012: Define safe observability, trace IDs and redaction defaults

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Payment support requires correlation across the gateway, native execution engine, terminal deployment and acquirer without logging sensitive payloads. Establish structured operation/attempt/event identifiers and redaction defaults before distributed tracing and diagnostics propagate raw requests into logs, crash collectors or dashboards. Include aggregator and merchant attribution only under appropriate access controls, and avoid unbounded metric label cardinality. UNKNOWN and reconciliation age must be observable separately from ordinary decline rates or HTTP failures. The blueprint does not assume that encrypted SAD may be retained in logs or queues after authorization. This foundation sets schemas and safe defaults; concrete payment instrumentation and production alert thresholds are owned by later tickets.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / observability**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router_env](../crates/router_env)

- [crates/router/src/events](../crates/router/src/events)

- [monitoring](../monitoring)

- `Proposed: docs/operations/telemetry-contract.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `security-data-classification`
- `telemetry-contracts`

## Implementation plan

- [ ] Define trace/correlation IDs and safe attribution fields spanning API, operation, native attempt and callback.
- [ ] Classify logs, metrics, traces, crash data and audit records with allowlisted fields and retention/access rules.
- [ ] Disable raw request/response capture for payment/credential/document endpoints by default.
- [ ] Define telemetry for unknown outcomes, reconciliation age, duplicate coalescing and tenant isolation failures.
- [ ] Provide synthetic canaries and review gates that detect secret/card/PIN leakage in observability outputs.

## Acceptance criteria

- [ ] A field-level telemetry schema excludes raw card, PIN, credential, bearer-token and KYB document content.
- [ ] One synthetic operation can be correlated across services without exposing its sensitive payload.
- [ ] UNKNOWN and delayed reconciliation have distinct observability signals.
- [ ] Metric label cardinality and tenant visibility are explicitly bounded.
- [ ] Default logging/crash collectors do not capture protected request bodies.

## Validation scenarios

- [ ] Inject synthetic sensitive markers and scan logs/traces/crash artifacts for leakage.
- [ ] Trace a timeout and callback using only safe operation/attempt/event identifiers.
- [ ] Review access to aggregator-specific traces from an unrelated principal.

## Expected deliverables

- Observability field and redaction schema
- Trace propagation convention
- Synthetic leakage canaries

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
