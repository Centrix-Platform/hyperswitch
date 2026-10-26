---
id: "CTX-122"
title: "Finalize the public platform API contract, examples and native admin isolation"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "platform"
component: "Public API product"
depends_on: ["CTX-006", "CTX-040", "CTX-041", "CTX-045", "CTX-049", "CTX-050", "CTX-059", "CTX-060", "CTX-061", "CTX-069", "CTX-073", "CTX-104", "CTX-142"]
requires_one_of: []
conflict_domains: ["api-docs", "gateway-ingress", "platform-contract-catalog", "public-api-contract"]
external_inputs: ["Approved public API hostname/versioning policy and eventual documentation hosting destination; sandbox execution can use local/stub services."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-122: Finalize the public platform API contract, examples and native admin isolation

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Your customers integrate with aggregator, merchant and terminal concepts, while Hyperswitch internally names their aggregator a MerchantAccount. Publish one coherent versioned platform contract that hides that translation and stays stable across Rust/Kotlin implementations. Native admin endpoints remain private compatibility/control-plane interfaces and must not become an undocumented customer escape hatch. This ticket consolidates implemented endpoint schemas, authentication scopes, asynchronous operations, idempotency and error behavior into executable documentation and conformance assets. It must document UNKNOWN outcomes, replay limits, currency/minor units and webhook ordering precisely. Documentation generation or publication should follow repository conventions and the approved delivery pipeline; writing this backlog does not authorize external publication or exposing currently private routes.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) - consume its completed, reviewed deliverables: Deliver signed versioned aggregator webhooks with safe retries.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.
- [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) - consume its completed, reviewed deliverables: Expose authorized payment status search and export APIs.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-104](CTX-104-document-kotlin-java-ipc-status-and-recovery-integration--TODO.md) - consume its completed, reviewed deliverables: Document Kotlin, Java, IPC, status, and recovery integration.
- [CTX-142](CTX-142-first-acquirer-dispute-chargeback-domain--TODO.md) - consume its completed, reviewed deliverables: Implement scoped first-acquirer dispute lifecycle evidence and notifications.


## Relevant code and ownership

Primary repository/workstream: **platform / Public API product**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/openapi/src/openapi.rs](../crates/openapi/src/openapi.rs)

- [crates/openapi/src/openapi_v2.rs](../crates/openapi/src/openapi_v2.rs)

- [.github/workflows/validate-openapi-spec.yml](../.github/workflows/validate-openapi-spec.yml)

- [crates/router/src/routes/app.rs](../crates/router/src/routes/app.rs)

- `Proposed: api-reference/platform/v1/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `api-docs`
- `gateway-ingress`
- `platform-contract-catalog`
- `public-api-contract`

## Implementation plan

- [ ] Finalize versioned OpenAPI schemas for onboarding, terminals, keys/sessions, charges, status, capture/refund and reporting with stable public identifiers.
- [ ] Define security schemes, permission requirements, idempotency scopes/retention behavior, async operation links and consistent error envelopes.
- [ ] Generate validated examples, server/client fixtures and migration guidance without leaking native IDs, secret-store references or operational secrets.
- [ ] Add integration tutorials covering aggregator backend custody, SDK-session exchange, terminal binding, uncertain outcomes and webhook verification.
- [ ] Enforce ingress/network isolation for native admin routes and document service-authenticated compatibility access.
- [ ] Wire schema linting, breaking-change detection and executable examples into CI; stage documentation for approved publication.
- [ ] Include CTX-142 dispute/case read, authoritative deadline, evidence-action/manual-handoff and safe dispute-event contracts in the final OpenAPI and integrator examples; document conditional action support and duplicate submission recovery.

## Acceptance criteria

- [ ] All exposed platform endpoints and supported events match the implemented versioned contract.
- [ ] Examples validate and execute against a clean sandbox without native admin credentials.
- [ ] Native admin routes are inaccessible from aggregator/public ingress, including path/method aliases.
- [ ] Security scopes, UNKNOWN handling, idempotency conflicts and async onboarding semantics are explicit.
- [ ] A breaking contract change fails the configured compatibility check unless intentionally versioned.
- [ ] No secret or production account data appears in schemas, examples or generated docs.
- [ ] Published public documentation covers the implemented dispute/chargeback APIs and safe events, with owner scope, evidence readiness, authoritative deadline provenance and supported/manual actions accurately represented.

## Validation scenarios

- [ ] Run OpenAPI lint/schema generation and existing native validation where affected.
- [ ] Execute representative onboarding-to-charge/webhook examples against synthetic sandbox resources.
- [ ] Test public ingress access to native admin routes and compare deployed route inventory with the public schema.

## Expected deliverables

- Versioned platform OpenAPI/event schemas.
- Executable integration examples and aggregator documentation.
- Native-admin isolation and API compatibility CI evidence.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved public API hostname/versioning policy and eventual documentation hosting destination; sandbox execution can use local/stub services.

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
