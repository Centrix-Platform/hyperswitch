---
id: "CTX-006"
title: "Define API, event, monetary and error contract standards"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "contracts"
depends_on: ["CTX-001", "CTX-003"]
requires_one_of: []
conflict_domains: ["event-contracts", "platform-contract-catalog", "public-contracts"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-006: Define API, event, monetary and error contract standards

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Many agents will build control APIs, the SDK, the dashboard and adapters concurrently. A shared contract standard must exist before they diverge on identifier types, money, errors, asynchronous states and idempotency. Public terminology follows aggregator/merchant/terminal semantics; native merchant/profile/MCA references remain internal. Charge amounts use integer minor units with currency-specific validation. Accepted HTTP work can remain financially pending or UNKNOWN, and duplicate messages are expected. Define public OpenAPI and internal event/port schemas independently of Rust implementation types, including compatibility and versioning rules. This ticket establishes shared conventions; later domain tickets own their concrete endpoints and must feed validated schemas back into the contract catalog.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **platform / contracts**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/api_models](../crates/api_models)

- [crates/openapi](../crates/openapi)

- [api-reference](../api-reference)

- [proto](../proto)

- `Proposed: contracts/platform/openapi.yaml`

- `Proposed: contracts/events`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `event-contracts`
- `platform-contract-catalog`
- `public-contracts`

## Implementation plan

- [ ] Specify public ID formats, environment separation, timestamps, currency/minor-unit amounts, pagination and merchant references.
- [ ] Define idempotency headers/scopes, request fingerprint semantics, safe replay and structured 401/403/404/409/422/429 errors.
- [ ] Define asynchronous operation resources and distinct transport, business and financial states including UNKNOWN.
- [ ] Specify versioned event envelopes with environment, aggregator, resource version, event ID and safe trace metadata.
- [ ] Define OpenAPI/JSON Schema or Protobuf ownership, backward compatibility, client generation and change-review gates.

## Acceptance criteria

- [ ] Contract conventions are independent of native request and Diesel structs.
- [ ] Examples distinguish a pending operation from an approved or declined financial result.
- [ ] An event envelope supports tenant-scoped at-least-once delivery and consumer deduplication.
- [ ] Money encoding, idempotency scope and error semantics are consistent across SDK and portal APIs.
- [ ] Compatibility rules identify breaking changes before a generated client or deployment is published.

## Validation scenarios

- [ ] Validate representative onboarding, charge, operation-status and webhook examples against draft schemas.
- [ ] Compare generated Java/Kotlin and frontend DTO encodings for IDs, timestamps and amounts.
- [ ] Exercise duplicate request, changed-body conflict and unknown-outcome examples in contract fixtures.

## Expected deliverables

- Public/internal contract style guide
- Event envelope and error schemas
- Versioning and compatibility policy

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
