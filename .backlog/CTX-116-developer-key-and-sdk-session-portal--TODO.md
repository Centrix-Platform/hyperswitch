---
id: "CTX-116"
title: "Build scoped key, SDK-session and rotation tooling"
status: "TODO"
phase: 4
priority: "P0"
size: "M"
repository: "dashboard"
component: "Developer experience"
depends_on: ["CTX-040", "CTX-041", "CTX-042", "CTX-043", "CTX-111"]
requires_one_of: []
conflict_domains: ["dashboard-developer-keys"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-116: Build scoped key, SDK-session and rotation tooling

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform has three authority tiers: platform administration, aggregator backend operational keys and short-lived merchant/terminal SDK sessions. The developer portal must explain those tiers and never encourage embedding a reusable operational key in an APK. Authorized users need scoped key creation, one-time secret presentation, expiry/revocation management and integration examples. SDK-session tooling should call the backend issuer using current user permissions or a safe sandbox workflow, not mint unconstrained tokens in JavaScript. Scope selection cannot exceed the actor's delegated permissions. The UI should make environment boundaries obvious, support credential overlap during rotation and show last-use metadata without exposing full secrets. Existing native API-key screens require adaptation to the finer platform authorization model.

## Prerequisites and dependency outputs

- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) - consume its completed, reviewed deliverables: Implement capability-driven navigation and aggregator-scoped portal caches.


## Relevant code and ownership

Primary repository/workstream: **dashboard / Developer experience**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/routes/api_keys.rs](../crates/router/src/routes/api_keys.rs)

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- `Proposed: services/platform-control/src/sdk-sessions/`

- `External: juspay/hyperswitch-control-center/package.json (verify pinned fork)`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `dashboard-developer-keys`

## Implementation plan

- [ ] Create scoped operational-key list/create/revoke/rotate screens with expiry, environment and permitted merchant/action constraints.
- [ ] Implement one-time secret display and copy flow with no persistence, analytics capture or subsequent reveal endpoint.
- [ ] Add SDK-session sandbox tooling that selects authorized merchant/terminal/payment constraints and displays bounded expiry/device-binding requirements.
- [ ] Provide server-side and Android examples demonstrating operational-key custody and ephemeral-session exchange.
- [ ] Expose revocation propagation, last-use metadata and rotation overlap status without logging bearer tokens.
- [ ] Require privileged actions and scope delegation through the backend authorization policy.

## Acceptance criteria

- [ ] Users cannot create keys with scopes beyond their current delegated authority.
- [ ] Operational secrets are displayed once and absent from logs, persistent browser storage and later reads.
- [ ] APK examples contain no reusable aggregator operational key.
- [ ] SDK sessions are environment-, merchant-, terminal- and action-scoped with bounded expiry.
- [ ] Revoked keys/sessions fail subsequent authorized-use tests within the documented propagation bound.
- [ ] Sandbox tooling cannot invoke a live charge accidentally through an environment switch.

## Validation scenarios

- [ ] Run key create/rotate/revoke and excessive-scope denial tests with two roles/aggregators.
- [ ] Inspect frontend storage and telemetry during one-time secret display.
- [ ] Execute documented sandbox SDK-session examples and verify claim/context constraints.

## Expected deliverables

- Developer key/session UI and safe examples.
- Secret presentation and scope-delegation regression evidence.
- Credential lifecycle integration guide.

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
