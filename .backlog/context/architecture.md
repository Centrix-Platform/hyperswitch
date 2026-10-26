# Architectural baseline for every CTX ticket

This is a standalone execution context for the backlog requested on 2026-10-22. It translates the previously delivered architectural blueprint into engineering boundaries, not implemented functionality. All tickets initially have status `TODO`.

The original export is [the architecture blueprint](../../output/pdf/white-label-b2b2b-payment-gateway-blueprint.pdf). A portable text snapshot of that export is retained in [source-blueprint.txt](source-blueprint.txt). The core inspection baseline is commit `c5ecb434b419d2c473cf2882a3866de9146abdec`.

## Product and funds-flow scope

The paying customers are licensed Aggregators/Payment Facilitators, not the merchants those customers onboard. The platform provides infrastructure and orchestration. Aggregators own their processing configurations, operational integration authority and merchant relationships. Their Android APKs embed the white-label SDK and integrate approved physical or smart-terminal capture components.

The initial funds-flow assumption is direct acquirer settlement. Build payment orchestration, an immutable transaction journal and settlement reconciliation. Customer balances, reserves, fees held by the platform and payouts require a separately approved financial-ledger program. CTX-001 and CTX-133 resolve business and jurisdiction responsibilities; CTX-140 describes the conditional ledger extension.

The pilot is one aggregator, one merchant, one terminal family and one acquirer, followed from onboarding through reconciliation. Broader support follows validated integration and release evidence. Future Java/Kotlin migration must remain possible through language-neutral contracts.

## Canonical and native entities

| Canonical public domain | Initial Hyperswitch projection | Important qualification |
|---|---|---|
| Platform environment/deployment cell | Infrastructure Tenant configuration | Tenant selects schemas, prefixes and analytics placement; it is not a super-admin identity. |
| Aggregator | MerchantAccount, preferably with a dedicated Organization | Aggregator is the primary customer isolation boundary. |
| Merchant owned by an aggregator | Canonical merchant record mapped to BusinessProfile | Legal/KYB lifecycle and independent merchant resource ownership are additional responsibilities. |
| Acquirer integration | Connector implementation | Connector is code and protocol capability. |
| Merchant processing configuration | Profile-associated MCA | MCA is configured access to a connector, not physical terminal identity. |
| Acquirer account/credentials | Aggregator-owned configuration plus versioned secret reference | One account may project to multiple authorized profile-specific MCAs. |
| Terminal deployment | New canonical terminal domain | Enrollment, device/app identity, merchant assignment and revocation are independent of MCA lifecycle. |
| Terminal binding | New versioned binding | Links deployment, merchant, processing projection, MID/TID, certification and encryption domain. |

CTX-002 must choose between the requested profile-backed merchant topology and native Platform/Connected accounts based on actual requirements. Never implement both as incompatible assumptions. The v1 customer and stored-payment-method schemas inspected in the core are MerchantAccount-scoped, not automatically BusinessProfile-scoped. Disable unsupported saved-card/customer/mandate features or implement and verify their complete merchant ownership boundary before exposure. CTX-033 owns that consequence of the topology choice.

Preserve native Rust types and storage names inside the compatibility adapter. Public payloads use `aggregator_id`, canonical `merchant_id`, `terminal_id` and operation/payment IDs. Native tenant, merchant-account, profile and MCA IDs are internal mappings.

## Logical service boundaries and state authority

| Domain | Owned data and responsibilities |
|---|---|
| Identity and authorization | Users, memberships, grants, operational-key verifiers, SDK sessions, request authority. |
| Merchant management | Legal merchant registry, KYB references, approval, suspension, onboarding jobs. |
| Terminal management | Inventory, enrollment, device/app identity, deployments, certification bindings, signed configurations. |
| Processing configuration | Acquirer account references, profile/MCA projections, permitted routes and configuration versions. |
| Platform payment workflow | Authenticated durable admission, public operation identity, policy, execution-port correlation. |
| Native payment execution initially | Hyperswitch payment attempts, connector calls and results behind a platform-owned execution port. |
| Webhooks and reconciliation | Verified inboxes, signed delivery, inquiry, financial journal and settlement matching. |
| Portal and reporting | Tenant-scoped presentation/read models; not an independent source of financial truth. |

Start with logical separation and a manageable deployment layout. Each aggregate has one authoritative writer. Separate services do not directly mutate one another's schemas or coordinate financial side effects through long database transactions. Publish versioned events using durable outbox/inbox patterns with at-least-once delivery and idempotent consumers.

OpenAPI owns public contracts; internal ports/events can use versioned JSON Schema or Protobuf. Rust/Diesel models must not become the public API or Kotlin ABI. A future Kotlin implementation replaces a port or domain incrementally; shadow only side-effect-free decisions. Never duplicate a live authorization to compare implementations.

## Transaction path

```text
Aggregator Android APK
  -> white-label Kotlin/Java facade and device-bound SDK session
  -> approved vendor secure capture / payment application
  -> gateway TLS + authenticated transaction request
  -> trusted aggregator / merchant / terminal context
  -> durable PostgreSQL operation reservation
     (Redis coordinates concurrency and caches safe results)
  -> approved binding / certification eligibility
  -> frozen route, configuration and credential version
  -> language-neutral PaymentExecutor -> Hyperswitch Rust adapter
  -> applicable acquirer/crypto security boundary
  -> aggregator's acquiring network / issuer
  -> verified result, terminal completion or UNKNOWN recovery
  -> SDK operation status + signed aggregator webhook
  -> immutable journal and settlement reconciliation
```

The gateway resolves ownership from authenticated context. A TID, serial number or request-body `terminal_id` is not authentication. Only approved bindings can enter routing. Ciphertext prepared for one acquirer/key domain is not generally portable to another; fallback may require a new certified terminal interaction.

CTX-013 also declares authorization ownership. If a vendor payment app already performs authorization, CTX-141 adds authenticated result/inquiry ingestion for that original transaction. An app result is not a request to submit another gateway charge. The selected owner is immutable per operation and must match certification/recovery evidence.

Store immutable attempt snapshots for attribution and recovery. Configuration edits or credential rotation must not silently change an in-flight attempt's processing identity. Account/merchant/terminal suspension blocks new activity and propagates revocation while allowing specifically authorized inquiry, reversal and reconciliation of existing obligations.

## Tenancy and storage invariants

1. Validate principal -> aggregator -> merchant -> terminal -> binding on every applicable request.
2. Resolve tenant context on the server. Strip untrusted internal routing/identity headers at ingress.
3. Use scoped repositories and explicit database transactions. Bind `app.aggregator_id` with `set_config(..., true)` before tenant SQL and release the connection only after commit/rollback.
4. Use both RLS `USING` and `WITH CHECK`, non-owner runtime roles, relevant `FORCE ROW LEVEL SECURITY` and composite ownership foreign keys.
5. Cover native Hyperswitch tables, accounts pools, workers and replicas. New-registry RLS does not secure native payment/customer tables by itself.
6. Scope caches, Redis key/value paths, queues, object keys, signed downloads, search and ClickHouse/report queries as well as SQL.
7. A session setting protects against missing predicates, not arbitrary SQL from a fully compromised service. Stronger cells/credentials may be required by the chosen threat model.
8. Prefer authoritative PostgreSQL payment admission/state initially. Optional RedisKv/drainer paths require equivalent ownership and durability treatment before use.
9. Use expand/backfill/validate/contract migrations; preserve user changes and historical attribution.
10. Sandbox/live data, keys, token audiences, devices, callbacks and configurations must remain distinct.

Opaque-key verification needs a narrow pre-authentication verifier/owner lookup before aggregator context is known. This bootstrap interface must not become a general unscoped tenant-data API. Background publishers/workers similarly discover safe work metadata through known scopes or a narrowly privileged discovery interface, then enter scoped transactions for payload access. Do not grant blanket worker BYPASSRLS to solve discovery.

## Payment safety invariants

- PostgreSQL uniquely reserves `(environment, aggregator, merchant, operation_scope, idempotency_key)`; environment may be structurally separated by deployment/cell.
- Equal key and canonical request return the existing operation or its safe result. Changed immutable fields return a conflict.
- Redis uses short owner-valued leases and atomic compare/renew/release. Lost locks or expired TTLs do not authorize a second financial dispatch.
- Persist admission and an appropriately safe dispatch reference before the side effect. Do not keep a database transaction open across acquirer I/O.
- Use conditional state transitions and durable versions. Database fencing does not cancel a request already running at an external acquirer.
- Track whether an upstream outcome may exist. `UNKNOWN` is not a decline and is not permission to route elsewhere.
- Reuse a downstream reference only under the acquirer's documented duplicate semantics. A unique reference field alone is insufficient evidence of deduplication.
- Recover by inquiry, callback, approved reversal and reconciliation. Preserve ambiguity when evidence is unavailable.
- Retain durable duplicate protection longer than transient Redis caches. Bound contract-defined replay windows and preserve the business reference.
- One home-region authority writes a payment. Regional promotion must prevent concurrent financial writers.
- Inbound and outbound webhooks can be duplicated or reordered; use IDs, signatures, versions, inboxes and explicit transition rules.
- Financial totals, capture/refund authority and terminal completion require concurrency checks across their complete lifecycle.

Native automatic/manual/clear-PAN retries and retryable-connector expansion must be inventoried and constrained for terminal traffic. A correct facade UNKNOWN policy does not prevent hidden downstream retries by itself. CTX-049/055/056 implement the restriction and CTX-072 exercises it under faults.

## Authentication and credential hierarchy

Platform control credentials belong to isolated platform operators/automation. Aggregator operational keys belong to one customer's backend, have environment/scopes/expiry/revocation, and are stored as verifiers rather than reusable plaintext. They do not belong in browsers or APKs.

SDK sessions are short-lived, constrained to an authorized merchant/terminal and preferably a payment session, device-bound where supported and validated for audience/environment. A publishable key identifies an integration, not operational authority. Native customer-oriented ephemeral keys are not assumed to implement this terminal policy.

Portal authentication uses OIDC and a BFF with secure HttpOnly cookies, CSRF protection, membership validation and server-authorized aggregator context switching. RBAC controls actions; ownership policy controls resources. Hidden UI menus or a customer-supplied path/header do not establish authority.

## Android and crypto boundaries

The Android SDK spans native API modules and shared client-core/React Native/assets. Fork/white-label the relevant dependency chain. Inspect backend, logging, asset, SDK configuration, confirm and Airborne/update endpoints; do not leave upstream production fallback paths.

Prefer certified vendor capture and acquirer-approved opaque encryption/token transport. Do not expose clear PAN/track/PIN to a generic host SDK to add custom RSA encryption afterward. JWE is conditional for an explicitly approved application-layer contract; it does not replace terminal key management or establish PCI scope reduction. The general gateway should not receive decryption authority by default.

Android attestation is server-verified evidence, not terminal certification. Use vendor trust roots on terminals without the assumed Google ecosystem. Same-app SDK calls can remain local; cross-app intents/services require explicit components and runtime caller/UID/signing authorization. Signature permissions alone do not authorize differently signed partner APKs.

Recover process/network failures with the original operation reference. Do not implement offline or WorkManager authorization resubmission by default. Store only minimum safe recovery data. SAD retention after authorization is prohibited even when encrypted; include queues, diagnostics, crash artifacts and backups in the design.

Hardware/kernel approval does not by itself approve a new end-to-end terminal/app/gateway/acquirer path. Version and validate the applicable combination, L3/integration evidence and change triggers. Qualified reviewers own final assessment and certification determinations.

Dispute/chargeback obligations remain relevant under direct settlement. CTX-142 owns verified attribution, lifecycle/deadline provenance, evidence and notifications for the selected acquirer. CTX-143 owns scoped portal case/evidence/manual-handoff workflows. Neither a payment journal nor an agent-invented deadline substitutes for the authoritative acquirer process.

## Delivery phases and evidence

- Phase 1: fork/environment/provenance isolation, product/topology/contracts/threat model and test foundations.
- Phase 2: canonical/native tenancy, identity/keys, durable execution, callbacks, reconciliation and isolation/failure gates.
- Phase 3: terminal enrollment/bindings, SDK/vendor adapters, secure payloads, recovery and integration certification.
- Phase 4: white-label portal/public integration exposure, operational evidence, limited pilot and broader launch readiness.

APIs and identity foundations appear in Phase 2 so Phase 3 does not build against temporary insecure interfaces. Some phase tracks can proceed concurrently when dependencies and conflict domains allow. Phase is a roadmap grouping, not permission to skip prerequisites.

Certification, real customer/acquirer inputs, production credentials, external communication and live charges/deployments require their own explicit delivery authorization and evidence. Creating these tickets does not perform or authorize those actions. CTX-139 and CTX-140 are conditional evolution tracks and are not launch blockers for the selected initial scope.
