---
id: "CTX-083"
title: "Implement aggregator backend SDK-session bootstrap"
status: "TODO"
phase: 3
priority: "P0"
size: "M"
repository: "multi-repo"
component: "SDK session bootstrap"
depends_on: ["CTX-040", "CTX-041", "CTX-042", "CTX-047", "CTX-076", "CTX-078", "CTX-079", "CTX-081", "CTX-082"]
requires_one_of: []
conflict_domains: ["android/session-bootstrap", "platform/sdk-session-api", "sdk-session-auth-boundary"]
external_inputs: ["Aggregator backend authentication and delivery channel for SDK bootstrap responses.", "Token lifetime, refresh policy, per-session financial constraints, and supported device proof scheme."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-083: Implement aggregator backend SDK-session bootstrap

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Aggregator operational credentials belong on the aggregator backend and must never be packaged in the host APK. The integration flow authenticates the aggregator backend, verifies its merchant and terminal authority, and creates a constrained SDK session bound to the enrolled device key and intended payment. Mobile code receives only short-lived delegated authority and safe configuration references. A publishable integration identifier is not authorization to mint unrestricted sessions. Define recovery and refresh semantics so an expired token can resume an existing operation without increasing amount, switching merchant, or creating a new charge. Bootstrap errors must distinguish inactive merchant, revoked deployment, unavailable trust evidence, and unsupported configuration without leaking another aggregator's inventory. Rate limits and audit records must identify the backend credential and delegated device session separately.

## Prerequisites and dependency outputs

- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / SDK session bootstrap**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform SDK session API integration`

- `Proposed: external Android fork SDK session bootstrap client`

- `Proposed: reference aggregator backend session endpoint`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/session-bootstrap`
- `platform/sdk-session-api`
- `sdk-session-auth-boundary`

## Implementation plan

- [ ] Implement a reference aggregator-backend request that authenticates with a scoped operational key and requests a merchant/terminal payment session.
- [ ] Verify aggregator membership, active merchant/deployment/binding, configuration version, amount/currency constraints, and device-key possession.
- [ ] Return a short-lived audience-restricted token, immutable payment-session identity, and verified configuration reference.
- [ ] Implement SDK session intake and refresh/recovery contracts that preserve operation identity and original constraints.
- [ ] Document expiry, revocation, rate limits, and key separation; ensure no mobile minting path uses a publishable identifier as authority.

## Acceptance criteria

- [ ] No operational or platform key is needed by, returned to, or stored in the APK.
- [ ] Session claims are derived from server ownership checks rather than trusted request IDs.
- [ ] Tokens are scoped to the intended device key, merchant, terminal, environment, and payment constraints.
- [ ] Refresh cannot increase authority or silently create another operation.
- [ ] Revoked deployments and suspended merchants cannot receive new capture sessions.

## Validation scenarios

- [ ] Request sessions with another aggregator’s merchant/terminal identifiers.
- [ ] Attempt public session minting using only a publishable integration identifier.
- [ ] Refresh after amount change, key rotation, merchant suspension, and operation completion.
- [ ] Inspect sample APK resources/network traces for operational key exposure.

## Expected deliverables

- Aggregator-backend bootstrap reference implementation
- SDK session bootstrap/refresh contract
- Delegation abuse and expiry test evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Aggregator backend authentication and delivery channel for SDK bootstrap responses.
- [ ] Token lifetime, refresh policy, per-session financial constraints, and supported device proof scheme.

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
