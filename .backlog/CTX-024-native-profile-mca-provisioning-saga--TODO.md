---
id: "CTX-024"
title: "Project canonical merchants and accounts into native profiles and MCAs"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "native-provisioning"
depends_on: ["CTX-020", "CTX-021", "CTX-023", "CTX-043"]
requires_one_of: []
conflict_domains: ["database-schema-migrations", "native:admin", "schema:profile-mapping", "workflow:merchant-projection"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-024: Project canonical merchants and accounts into native profiles and MCAs

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Canonical merchants must be translated to native BusinessProfiles under the aggregator MerchantAccount, and authorized processing accounts must be projected to the necessary profile-associated MCAs. Native identifiers stay internal. Existing admin functions and storage models provide provisioning surfaces, but platform state and native state cannot share an assumed distributed transaction. Implement an idempotent saga with explicit step records, reconciliation and safe handling of lost responses. Keep canonical merchant approval separate from native projection readiness. Some native MCA credentials may need secure materialization inside the execution boundary; a secret reference alone is not automatically usable by existing connector code. Declare that adapter responsibility and never solve it by copying credentials into job payloads or public metadata.

## Prerequisites and dependency outputs

- [CTX-020](CTX-020-aggregator-provisioning-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Provision aggregators through a resumable native-account workflow.
- [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Model legal merchants and their onboarding lifecycle independently of profiles.
- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / native-provisioning**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/admin.rs](../crates/router/src/core/admin.rs)

- [crates/diesel_models/src/business_profile.rs](../crates/diesel_models/src/business_profile.rs)

- [crates/diesel_models/src/merchant_connector_account.rs](../crates/diesel_models/src/merchant_connector_account.rs)

- `Proposed: platform/processing/projections/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `database-schema-migrations`
- `native:admin`
- `schema:profile-mapping`
- `workflow:merchant-projection`

## Implementation plan

- [ ] Define profile and MCA projection commands, deterministic references and readiness states.
- [ ] Create profile under the resolved aggregator account and persist its mapping.
- [ ] Materialize authorized profile-specific MCA configuration through the secure credential adapter.
- [ ] Reconcile already-created native resources after crashes and lost responses.
- [ ] Detect drift, disabled MCA state and mapping collisions without auto-adopting unrelated resources.

## Acceptance criteria

- [ ] Replay provisions one profile and the expected bounded MCA set.
- [ ] Native account/profile ownership is checked before adopting resources.
- [ ] Canonical activation remains separate from projection success.
- [ ] Jobs and logs contain secret references, never plaintext connector credentials.
- [ ] Projection drift produces an actionable blocked state with audit evidence.

## Validation scenarios

- [ ] Crash between native creation and canonical mapping commit.
- [ ] Return a native resource belonging to another account and reject adoption.
- [ ] Rotate the credential reference and verify versioned secure projection behavior.

## Expected deliverables

- Profile/MCA projection saga and reconciliation job.
- Projection status contract and secure adapter specification.

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
