---
id: "CTX-084"
title: "Secure SDK HTTP transport, sender-constrained auth, and request integrity"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "SDK network security"
depends_on: ["CTX-006", "CTX-016", "CTX-042", "CTX-070", "CTX-076", "CTX-079", "CTX-082", "CTX-083"]
requires_one_of: []
conflict_domains: ["android/http-transport", "platform/sdk-proof-validation", "sdk-session-auth-boundary"]
external_inputs: ["Selected standard sender-constrained token profile and separate request-integrity algorithm/format.", "Approved endpoint/trust rotation policy, network timeouts, and proxy/debug behavior."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-084: Secure SDK HTTP transport, sender-constrained auth, and request integrity

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The SDK transport carries delegated authority and approved opaque payment payloads over TLS. It must validate the gateway endpoint and authenticate the enrolled device, while preventing replay or body substitution in financial requests. DPoP can constrain token possession but does not by itself authenticate arbitrary payment body fields; canonical request integrity needs its own approved contract binding amount, currency, operation, session, payload reference, and configuration version. Keep generic HTTP retries away from financial submission policy. Network timeouts after possible dispatch produce an uncertain operation that must be recovered using the original identifier. Implement certificate/network-security policy with a workable rotation story rather than hard-coding short-lived leaf certificates. Sensitive headers, proofs, envelopes, and responses must be excluded from network interceptors and diagnostics.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / SDK network security**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork gateway-sdk-core transport`

- `Proposed: platform SDK proof and canonical request validator`

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/PaymentSession.kt (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/http-transport`
- `platform/sdk-proof-validation`
- `sdk-session-auth-boundary`

## Implementation plan

- [ ] Implement owned HTTPS transport with endpoint allowlisting, certificate validation, explicit timeouts, and approved Android network-security policy.
- [ ] Create and validate sender-constrained token proofs with method/URL binding, freshness, nonce handling, and replay detection.
- [ ] Define canonical request digest/signature binding immutable business fields separately from DPoP and align it with gateway validation.
- [ ] Disable generic retries for authorization bodies; route retry/recovery decisions through payment operation state.
- [ ] Redact network interceptors and implement safe trace correlation without tokens, proofs, payment envelopes, or personal data.

## Acceptance criteria

- [ ] Invalid TLS chains, hostnames, forbidden endpoints, and cleartext payment traffic are rejected.
- [ ] A stolen token without device proof cannot submit a payment.
- [ ] Body substitution and replay fail without producing a new admitted operation.
- [ ] Financial timeouts preserve operation identity and surface pending/unknown status.
- [ ] Transport diagnostics expose safe identifiers only.

## Validation scenarios

- [ ] Replay proofs, modify URL/method/body fields, and test nonce expiry and clock skew.
- [ ] Use a test proxy with invalid trust material and prohibited host redirects.
- [ ] Drop connections before and after possible dispatch and inspect submission counts.
- [ ] Rotate supported trust material and verify documented overlap/failure behavior.

## Expected deliverables

- Android transport and proof implementation
- Gateway canonical request/proof interoperability fixtures
- Network security and retry policy

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Selected standard sender-constrained token profile and separate request-integrity algorithm/format.
- [ ] Approved endpoint/trust rotation policy, network timeouts, and proxy/debug behavior.

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
