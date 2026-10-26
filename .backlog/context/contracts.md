# Shared contract and relational execution context

These examples are architectural drafts carried from the blueprint. CTX-002 resolves native topology, CTX-006 owns conventions and domain tickets produce executable schemas. A ticket must implement the agreed versions rather than copying an example without ownership, validation and concurrency controls.

## Identifier and authority vocabulary

- `platform_id`: operator environment/cell identity, separate from an IAM role.
- `aggregator_id`: licensed platform customer and primary public tenant boundary.
- `merchant_id`: canonical merchant owned by an aggregator; not a native MerchantAccount ID.
- `terminal_id`: an enrolled logical deployment, not the acquirer TID.
- `binding_id`: versioned approved deployment/merchant/processing relationship.
- `operation_id`: durable command/workflow and recovery identity.
- `payment_id`: canonical financial resource mapped to native execution records.
- `attempt_id`: immutable execution-attempt identity with upstream reference and route snapshot.
- Native `hs_tenant_id`, organization, MerchantAccount, profile and MCA identifiers remain inside projections/adapters.

Public examples use shortened opaque IDs. Choose and validate actual formats in CTX-006; SQL UUID examples and public aliases need an explicit serialization mapping.

## Relational ownership model

| Aggregate/table concept | Ownership and integrity |
|---|---|
| platforms/cells | Environment and native tenant placement, controlled by platform automation. |
| aggregators | Platform placement plus unique native Organization/MerchantAccount mappings per cell. |
| merchants | Composite aggregator/merchant identity, unique external reference within aggregator, legal/KYB references, lifecycle and profile mapping. |
| memberships/grants | Principal plus authorized aggregator/merchant/action scope and authorization version. |
| acquirer_accounts | Aggregator-owned network configuration and versioned secret reference. |
| profile_connectors | Merchant-owned native MCA projection referencing an aggregator-owned acquirer account. |
| terminal_deployments | Enrolled device/app identity and merchant assignment, active/version/revocation state. |
| terminal_bindings | Composite owner-safe references to deployment, merchant and connector plus MID/TID, certification and encryption domain. |
| certification_bundles | Exact model/firmware/kernel/app/network/key-domain combination, evidence, validity and change history. |
| payment_operations | Unique scoped idempotency key, canonical fingerprint, safe status/result and native execution mapping. |
| acquirer_attempts | Operation, frozen processing identity, upstream reference, dispatch/outcome evidence and reconciliation state. |
| inbox/outbox/jobs | Unique event/delivery IDs, owner context, safe references, version/attempt/backoff state. |
| journal/settlement | Immutable financial attribution and reconciliation references without introducing a balances ledger implicitly. |

Composite foreign keys must prove aggregator ownership and merchant ownership at relationship creation, not merely application filtering at read time. Put tenant fields first in appropriate access/unique indexes. Preserve globally unique IDs or explicit shared mappings across platform cells where needed. Enforce active-binding uniqueness and define append-only historical deployment/reassignment behavior. Do not use free-form metadata as an authorization or routing authority.

Native references across service ownership boundaries use idempotent provisioning, mapping validation and reconciliation. Do not create a distributed SQL transaction or claim an application-maintained string reference is an enforced cross-service foreign key. The source blueprint contains illustrative DDL; CTX-019 through CTX-036 replace that draft with a coherent migration set for the selected topology.

## Transaction-local RLS pattern

```sql
BEGIN;
-- $1 is resolved from authenticated server context, never trusted from a body.
SELECT set_config('app.aggregator_id', $1, true);
-- Scoped repositories execute parameterized statements on this transaction.
COMMIT;
```

```sql
CREATE FUNCTION gateway.current_aggregator_id()
RETURNS uuid LANGUAGE sql STABLE AS $$
  SELECT NULLIF(current_setting('app.aggregator_id', true), '')::uuid
$$;

ALTER TABLE gateway.merchants ENABLE ROW LEVEL SECURITY;
ALTER TABLE gateway.merchants FORCE ROW LEVEL SECURITY;

CREATE POLICY merchant_aggregator_isolation
ON gateway.merchants TO gateway_app
USING (aggregator_id = gateway.current_aggregator_id())
WITH CHECK (aggregator_id = gateway.current_aggregator_id());
```

Provision `gateway_app` as a non-owner, non-BYPASSRLS runtime role separately. Scope native storage and non-SQL paths too. Missing context must deny tenant access. Workers, retries, rollback/savepoint paths, accounts pools and replica routing all need coverage.

## Merchant onboarding

```http
POST /v1/aggregators/{aggregator_id}/merchants
Authorization: Bearer <aggregator-operational-key>
Idempotency-Key: merchant-onboarding-8472
Content-Type: application/json
```

```json
{
  "external_reference": "merchant-8472",
  "legal_entity": {
    "registered_name": "Comercial Ejemplo SA de CV",
    "trading_name": "Ejemplo Centro",
    "country": "MX",
    "business_type": "company",
    "merchant_category_code": "5411",
    "kyb_document_set_id": "documents-8472"
  },
  "contact": {
    "name": "Operations Team",
    "email": "operations@example-merchant.com"
  },
  "business_address": {
    "line1": "Av. Ejemplo 100",
    "city": "Ciudad de Mexico",
    "postal_code": "06000",
    "country": "MX"
  },
  "processing": {
    "currencies": ["MXN"],
    "channels": ["card_present"],
    "requested_acquirer_accounts": [{
      "acquirer_account_id": "acqacct_primary",
      "settlement_profile_id": "settlement_approved_01"
    }],
    "routing_policy_id": "routing_retail_mx_v3"
  },
  "metadata": {"aggregator_store_reference": "store-019"}
}
```

Match path authority to the authenticated key, require `merchants:create` and verify every referenced object belongs to the same authorized hierarchy. Store secure document/settlement references rather than leaking their content. Reserve onboarding idempotently, create the canonical merchant, provision native projections and submit acquirer enrollment as an asynchronous saga. Persist progress and recover incomplete steps. Creating a BusinessProfile does not approve processing.

```http
HTTP/1.1 202 Accepted
Location: /v1/aggregators/agg_A/operations/onboard_123
```

```json
{
  "operation_id": "onboard_123",
  "merchant": {
    "id": "mer_B",
    "external_reference": "merchant-8472",
    "status": "pending_review"
  },
  "processing_status": "not_enabled"
}
```

## Endpoint families

| Endpoint family | Required authority / behavior |
|---|---|
| `/v1/aggregators/{a}/merchants` | Scoped onboarding, lists, detail and lifecycle transitions. |
| `/v1/aggregators/{a}/terminal-enrollments` | Inventory/claim/challenge enrollment under a known aggregator. |
| `/v1/aggregators/{a}/merchants/{m}/terminal-bindings` | Approved deployment/merchant/acquirer binding only. |
| `/v1/aggregators/{a}/sdk-sessions` | Server-to-server issuance constrained to an authorized device/payment session. |
| `/v1/charges` | SDK/payment authority determines hierarchy; typed opaque payment payload. |
| `/v1/operations/{id}` | Ownership-checked status and recovery; canonical operation types/versions. |
| `/v1/payments/{id}/captures` | Original processing authority and concurrency-safe remaining amount. |
| `/v1/payments/{id}/refunds` | Independent idempotency plus original payment/route and refund amount constraints. |
| Subscription/report/admin families | Explicit action and resource scope; native admin remains private. |

Normalize the aggregator-scoped onboarding operation link and generic status API under the final OpenAPI contract. A facade may expose a canonical operation endpoint and an authorized alias; do not leave clients with unimplemented response URLs.

## SDK session and charge constraints

An aggregator backend authenticates with an operational key and requests a session for a known active merchant/terminal. The issuer constrains environment, audience, scope, payment session, currency/amount, configuration version and device key. The SDK never receives the operational key. Public keys and publishable integration IDs do not authorize session minting by themselves.

```json
{
  "aud": "terminal-payments",
  "aggregator_id": "agg_A",
  "merchant_id": "mer_B",
  "terminal_id": "term_C",
  "payment_session_id": "session_D",
  "scope": "payment:confirm payment:read",
  "currency": "MXN",
  "maximum_amount_minor": 12500,
  "configuration_version": 18,
  "cnf": {"jkt": "device-key-thumbprint"}
}
```

Real tokens also require issuer, subject, expiry, token identifiers and algorithm/key validation from the agreed token profile. DPoP constrains token possession but does not on its own bind arbitrary transaction bodies. Define separate canonical transaction integrity or an approved protocol binding.

```json
{
  "payment_session_id": "session_D",
  "merchant_reference": "order-20261022-001",
  "amount_minor": 12500,
  "currency": "MXN",
  "terminal_configuration_version": 18,
  "payment_payload": {
    "type": "acquirer_encrypted",
    "format": "approved-vendor-format-v1",
    "reference": "secure-payload-reference"
  }
}
```

Secure references require an explicitly defined lifetime and handling policy; they are not justification to store reusable SAD indefinitely. When payload transport is inline or vendor-mediated, use the approved contract. Key domains and eligibility determine the processing path before decryption/forwarding.

## Idempotency, dispatch and outcomes

```text
ADMITTED -> DISPATCHING -> SUCCEEDED
                       -> FAILED
                       -> UNKNOWN -> inquiry / callback / reversal / reconciliation
```

These are workflow states. Define distinct payment authorization/capture/refund/terminal-completion states in the concrete contract; an approved authorization is not automatically a completed terminal sale or settled payment. Terminal UI cancellation is not evidence that an acquirer authorization never occurred.

Fingerprint immutable business fields and a stable secure-payload identity. Define exact retry behavior for randomized ciphertext so clients do not accidentally change semantics while reusing the key. A durable unique insert and conditional state claim arbitrate admission/dispatch. Acquirer I/O happens outside database transactions. Recover crashes conservatively; lease expiry, a database rollback, an HTTP timeout or Redis loss cannot prove the acquirer saw nothing.

Store only safe idempotent results. Do not replay tokens, card data or unredacted credentials. Downstream duplicate semantics, inquiry reference formats and retention windows come from the selected acquirer, not assumptions.

## Errors and events

- `401`: authentication invalid/expired or token profile rejected.
- `403` or ownership-safe `404`: valid identity lacks action/resource authority, following the chosen disclosure policy.
- `409`: changed immutable request under an existing idempotency scope, stale version or conflicting lifecycle transition.
- `422`: structurally valid request with unsupported/invalid domain configuration.
- `429`: scoped limit exceeded, with a documented retry policy.
- `202`: asynchronous acceptance; financial success remains separate.

Event envelopes need schema version, event ID/type, timestamp, environment/cell, aggregator, resource ID/version, safe correlation and a minimal domain payload. Use outbox/inbox IDs, per-resource transition/version rules, signatures and retry/dead-letter policy. Delivery is at least once and may be reordered. Do not promise global event order.
