---
id: "CTX-068"
title: "Publish approved processing configuration and invalidate stale views"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "configuration-publication"
depends_on: ["CTX-023", "CTX-024", "CTX-025", "CTX-026", "CTX-028", "CTX-043", "CTX-047", "CTX-054", "CTX-055"]
requires_one_of: []
conflict_domains: ["config:publication", "configuration-publication-boundary", "contracts:configuration-snapshot", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-068: Publish approved processing configuration and invalidate stale views

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Routing, terminal bindings, credential references and certification state originate in the control plane but are consumed by payment execution and SDK sessions. Publish approved immutable configuration versions with explicit ownership, activation time and compatibility requirements. Do not let partially edited settings or a failed MCA projection become live merely because a cache was refreshed. The data plane must distinguish stale-but-allowed configuration from hard revocation and apply the selected policy before dispatch. Existing attempts keep their frozen snapshots for recovery. This ticket coordinates publication/invalidation rather than owning every configuration editor. Store safe references only, verify publisher/consumer identity and make configuration rollout observable so operators can identify which version each payment decision used without exposing secrets.

## Prerequisites and dependency outputs

- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.


## Relevant code and ownership

Primary repository/workstream: **platform / configuration-publication**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/storage_impl/src/redis/cache.rs](../crates/storage_impl/src/redis/cache.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- `Proposed: platform/configuration/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `config:publication`
- `configuration-publication-boundary`
- `contracts:configuration-snapshot`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define configuration aggregate, approval/readiness and immutable version schema.
- [ ] Implement publish-after-commit events and authenticated consumer validation.
- [ ] Atomically activate complete versions after projection prerequisites succeed.
- [ ] Add cache invalidation, revocation precedence and stale-read policy.
- [ ] Expose rollout status and compatibility checks for gateway/SDK consumers.

## Acceptance criteria

- [ ] Partial configuration edits cannot activate a mixed version.
- [ ] Every new dispatch identifies one approved configuration version.
- [ ] Hard revocation takes precedence over stale cache availability.
- [ ] In-flight snapshots remain recoverable after publication changes.
- [ ] Secrets and raw payloads never enter configuration events.

## Validation scenarios

- [ ] Interrupt publication halfway through and confirm old complete version remains active.
- [ ] Deliver configuration events out of order and repeat them.
- [ ] Revoke a binding while a consumer is disconnected then reconnect.

## Expected deliverables

- Configuration publisher/consumer and immutable snapshot contract.
- Rollout observability and stale/revoked-state tests.

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
