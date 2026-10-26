---
id: "CTX-073"
title: "Validate public internal and event contracts across implementations"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "contract-compatibility"
depends_on: ["CTX-006", "CTX-028", "CTX-041", "CTX-042", "CTX-045", "CTX-049", "CTX-050", "CTX-059", "CTX-068", "CTX-069"]
requires_one_of: []
conflict_domains: ["contracts:compatibility", "platform-contract-catalog", "release:contract-gate"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-073: Validate public internal and event contracts across implementations

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The API-first boundary is useful only if contract changes are reviewed and independently implementable. Add compatibility validation for public onboarding/payments, SDK sessions and proof vectors, internal execution ports and asynchronous event envelopes. Keep native Rust DTOs behind the adapter, and ensure examples use public aggregator/merchant terminology. Validate schema evolution, unknown enum behavior, error semantics, idempotency scope and monetary representation across generated clients and fixtures. This ticket enables a future Kotlin implementation through conformance rather than requiring a rewrite now. Breaking changes need an explicit version/migration plan; optional event fields must not silently change business meaning. Contract checks should exercise behavior as well as structural diffs, especially UNKNOWN outcomes and duplicate handling.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) - consume its completed, reviewed deliverables: Deliver signed versioned aggregator webhooks with safe retries.
- [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) - consume its completed, reviewed deliverables: Publish approved processing configuration and invalidate stale views.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.


## Relevant code and ownership

Primary repository/workstream: **platform / contract-compatibility**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/api_models/src/payments.rs](../crates/api_models/src/payments.rs)

- [crates/api_models/src/webhooks.rs](../crates/api_models/src/webhooks.rs)

- `Proposed: contracts/`

- `Proposed: platform/tests/contracts/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:compatibility`
- `platform-contract-catalog`
- `release:contract-gate`

## Implementation plan

- [ ] Collect versioned OpenAPI/JSON Schema/Protobuf contracts under declared ownership.
- [ ] Add breaking-change detection and required compatibility metadata.
- [ ] Run positive/negative examples through gateway and Rust adapter serializers.
- [ ] Validate SDK proof, money and idempotency vectors across supported languages.
- [ ] Publish artifact versions and consumer compatibility matrix.

## Acceptance criteria

- [ ] Public schemas contain no native IDs or implementation types.
- [ ] Breaking changes fail CI without an explicit approved version transition.
- [ ] Examples validate against the published schemas.
- [ ] UNKNOWN, pending and conflict semantics survive adapter serialization.
- [ ] Event consumers tolerate documented additive evolution and reject incompatible versions safely.

## Validation scenarios

- [ ] Remove/rename a required field in a controlled test and detect the break.
- [ ] Run Rust and JVM reference serializers against shared vectors.
- [ ] Replay old supported event versions through current consumers.

## Expected deliverables

- Contract compatibility CI and conformance fixtures.
- Published version/consumer matrix and migration checklist.

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
