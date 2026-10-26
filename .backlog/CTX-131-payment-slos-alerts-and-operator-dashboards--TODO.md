---
id: "CTX-131"
title: "Implement SLO dashboards and actionable payment health alerts"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "infra"
component: "Observability and reliability"
depends_on: ["CTX-012", "CTX-057", "CTX-063", "CTX-065", "CTX-066", "CTX-070", "CTX-124"]
requires_one_of: []
conflict_domains: ["monitoring-dashboards", "observability-rules"]
external_inputs: ["Approved service objectives, operational ownership/escalation schedule and monitoring/notification destinations; activation of real notifications is a separately authorized operational action."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-131: Implement SLO dashboards and actionable payment health alerts

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A gateway can return fast HTTP responses while accumulating unresolved payments or stale reconciliation work. Define reliability around admitted operations, final-outcome latency, UNKNOWN age, callback processing, queue age and settlement matching, with ownership for each signal. Existing monitoring and load-test assets are starting points, not proof that the B2B2B workflow is observable. Metrics must avoid secrets and uncontrolled merchant/terminal label cardinality; use correlated logs/traces and scoped investigations for detailed context. Alerts should identify affected aggregators and remediation safely without exposing their data to ordinary dashboard viewers. Separate customer-visible payment correctness indicators from infrastructure saturation and configure alert routing/runbook links through approved operational channels.

## Prerequisites and dependency outputs

- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) - consume its completed, reviewed deliverables: Authorize background jobs and constrain retry and replay behavior.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-066](CTX-066-aggregator-quotas-bulkheads-backpressure--TODO.md) - consume its completed, reviewed deliverables: Isolate aggregator capacity with quotas and fair work scheduling.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) - consume its completed, reviewed deliverables: Implement immutable administrative and privileged access auditing.


## Relevant code and ownership

Primary repository/workstream: **infra / Observability and reliability**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [monitoring/README.md](../monitoring/README.md)

- [monitoring/docker-compose.yaml](../monitoring/docker-compose.yaml)

- [config/prometheus.yaml](../config/prometheus.yaml)

- [loadtest/grafana/dashboards/k6-load-testing-results_rev3.json](../loadtest/grafana/dashboards/k6-load-testing-results_rev3.json)

- `Proposed: monitoring/platform/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `monitoring-dashboards`
- `observability-rules`

## Implementation plan

- [ ] Define SLI/SLO formulas and denominators for API admission, execution, finality, webhook delivery, SDK sessions and reconciliation freshness.
- [ ] Instrument UNKNOWN count/age, dispatch/outbox/inbox age, callback lag, unmatched settlement age, pool saturation, quota rejection and writer-epoch health.
- [ ] Build redacted operator dashboards and scoped customer-facing availability/reporting views where approved.
- [ ] Implement multi-window/error-budget and threshold alerts with severity, owner, routing, deduplication and runbook references.
- [ ] Control metric cardinality and trace/log sampling while retaining searchable operation/attempt correlation.
- [ ] Add synthetic sandbox probes and test alert firing/recovery for representative payment and dependency failures.

## Acceptance criteria

- [ ] Every critical workflow has an agreed SLI definition, owner and observable freshness/coverage.
- [ ] UNKNOWN, queue backlog and reconciliation-age breaches generate actionable alerts within the defined detection bound.
- [ ] Dashboard access and detailed drilldowns preserve aggregator authorization and redact sensitive fields.
- [ ] Metric labels cannot grow unbounded with payment IDs or secrets.
- [ ] Alerts include clear impact, owning team and tested runbook links without notifying unapproved recipients.
- [ ] Probe failures are distinguishable from real financial failures and create no uncontrolled live charges.

## Validation scenarios

- [ ] Validate metric calculations against deterministic synthetic operations and journal/reconciliation counts.
- [ ] Inject stale UNKNOWN, queue, callback and settlement scenarios and verify alert trigger/recovery.
- [ ] Review label cardinality, access controls, redaction and alert-routing configuration.

## Expected deliverables

- SLO/SLI specification and dashboards.
- Versioned alert rules and sandbox probes.
- Alert validation evidence and runbook mappings.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved service objectives, operational ownership/escalation schedule and monitoring/notification destinations; activation of real notifications is a separately authorized operational action.

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
