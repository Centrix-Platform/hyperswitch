---
id: "CTX-041"
title: "Mint short-lived merchant terminal and payment-scoped SDK sessions"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "sdk-session-issuance"
depends_on: ["CTX-009", "CTX-021", "CTX-026", "CTX-029", "CTX-038", "CTX-040"]
requires_one_of: []
conflict_domains: ["auth:sdk-session", "authentication-authorization-boundary", "contracts:sdk-session", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-041: Mint short-lived merchant terminal and payment-scoped SDK sessions

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Native EphemeralKey is customer-oriented and must not be relabeled as a terminal security hierarchy. Build a dedicated issuance flow in which an authenticated aggregator backend requests a short-lived session for an enrolled, active merchant and terminal. Bind authority to environment, device key, audience, configuration version and preferably a specific payment session with amount/currency constraints. A publishable key identifies an integration but cannot mint operational authority. The gateway must resolve ownership and lifecycle before issuance and recheck critical revocation during use. This ticket creates the session and signing lifecycle; CTX-042 validates proof and transaction integrity. Avoid embedding acquirer credentials, native IDs or decryption authority in mobile tokens, and define renewal without silently expanding scope.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.


## Relevant code and ownership

Primary repository/workstream: **platform / sdk-session-issuance**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/diesel_models/src/ephemeral_key.rs](../crates/diesel_models/src/ephemeral_key.rs)

- `Proposed: platform/identity/sdk_sessions/`

- `Proposed: contracts/sdk-session.schema.json`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `auth:sdk-session`
- `authentication-authorization-boundary`
- `contracts:sdk-session`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define SDK-session request/response and minimal signed claims.
- [ ] Authorize backend minting against merchant, terminal, device key and operation constraints.
- [ ] Persist session/revocation metadata and implement short-lived signing-key rotation.
- [ ] Bind audience, environment, configuration version and permitted payment resources.
- [ ] Implement renewal and expiry behavior without broadening authority.

## Acceptance criteria

- [ ] Publishable keys alone cannot mint SDK authority.
- [ ] Session is unusable for a different merchant, terminal, environment or device key.
- [ ] Tokens contain no native IDs, acquirer secrets or decryption keys.
- [ ] Amount/currency and operation constraints are enforced server-side.
- [ ] Inactive merchants or revoked terminals cannot receive usable sessions.

## Validation scenarios

- [ ] Request sessions with foreign terminal and merchant combinations.
- [ ] Expire/rotate signing keys and verify defined renewal behavior.
- [ ] Attempt use beyond amount, currency or payment-session scope.

## Expected deliverables

- SDK-session issuer and claim schema.
- Minting endpoint contract and lifecycle tests.

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
