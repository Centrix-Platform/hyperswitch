---
id: "CTX-017"
title: "Build synthetic tenant fixtures and an acquirer fault-injection harness"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "test-infrastructure"
depends_on: ["CTX-006", "CTX-007", "CTX-014"]
requires_one_of: []
conflict_domains: ["synthetic-test-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-017: Build synthetic tenant fixtures and an acquirer fault-injection harness

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Payment and tenancy correctness require repeatable adversarial scenarios, not only happy-path connector sandbox calls. Build synthetic fixtures for two aggregators with overlapping external references, merchants, terminals and credentials, plus a controlled acquirer double. The harness must expose barriers around dispatch so later tests can crash workers, delay replies, duplicate callbacks and simulate an approved transaction whose response was lost. Use synthetic tokens and approved test data; ordinary fixture files must not contain real CHD, SAD or live secrets. This is a reusable testing capability, not a claim that a mock proves vendor certification. Domain tickets supply their specific assertions and the integration gates compose them into financial and isolation evidence.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) - consume its completed, reviewed deliverables: Establish a reproducible, isolated local development stack.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / test-infrastructure**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/test_utils](../crates/test_utils)

- [crates/router/tests](../crates/router/tests)

- [cypress-tests](../cypress-tests)

- [loadtest](../loadtest)

- `Proposed: tests/ctx_platform/fixtures`

- `Proposed: tests/ctx_platform/acquirer_double`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `synthetic-test-contracts`

## Implementation plan

- [ ] Create seeded synthetic hierarchies with overlapping external IDs across aggregators/environments.
- [ ] Implement a controllable acquirer double with deterministic references, outcomes and documented duplicate behavior modes.
- [ ] Expose pause/crash barriers before/after durable admission, send, upstream acceptance, response and callback persistence.
- [ ] Support duplicate/out-of-order callbacks, delayed settlement files, Redis loss and stale device/config fixtures.
- [ ] Publish fixture/cleanup interfaces and redact captured traffic at the harness boundary.

## Acceptance criteria

- [ ] Each scenario runs deterministically with a seed and isolated namespace.
- [ ] The harness can distinguish upstream acceptance from lost responses and track actual side-effect counts.
- [ ] Two-aggregator fixtures cover ID collisions without sharing authority.
- [ ] Fixtures and captured artifacts contain only synthetic approved test material.
- [ ] Capabilities and limitations are documented so mocks are not treated as certification evidence.

## Validation scenarios

- [ ] Run the same timeout/duplicate callback scenario repeatedly and compare recorded state and call counts.
- [ ] Run two isolated suites concurrently and verify no fixture cross-contamination.
- [ ] Scan fixture artifacts for prohibited real-looking secret/card/PIN content and validate redaction.

## Expected deliverables

- Synthetic hierarchy fixture library
- Deterministic acquirer/fault harness
- Scenario and cleanup API documentation

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
