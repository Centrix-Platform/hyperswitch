---
id: "CTX-081"
title: "Bind merchant terminals to approved acquirer MID/TID configurations"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "platform"
component: "Terminal processing bindings"
depends_on: ["CTX-023", "CTX-024", "CTX-025", "CTX-026", "CTX-047", "CTX-054", "CTX-055", "CTX-076", "CTX-078", "CTX-080"]
requires_one_of: []
conflict_domains: ["payment-execution-state-boundary", "payment/route-eligibility", "platform/profile-connectors", "platform/terminal-bindings"]
external_inputs: ["Acquirer-approved MID/TID allocation and enrollment rules.", "Crypto domain identifiers, certified route matrix, and supported terminal transaction capabilities."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-081: Bind merchant terminals to approved acquirer MID/TID configurations

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A terminal deployment needs an explicit approved relationship to a merchant processing configuration; its serial number must not double as an acquirer TID or route selector. Implement bindings that join aggregator ownership, merchant deployment, profile-specific MCA projection, acquirer account, MID/TID, certification bundle, crypto domain, supported operations, and configuration version. Some aggregators share an acquirer credential across merchants, but each projection and binding must preserve the authorized merchant processing identity. Routing may choose only among eligible bindings, and ciphertext prepared for one crypto domain is not portable to another route. Changes must be versioned rather than mutating historical attempts. Reassignment and credential rotation use controlled lifecycle operations and cannot rewrite the original merchant, configuration, or route recorded on a payment.

## Prerequisites and dependency outputs

- [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) - consume its completed, reviewed deliverables: Model aggregator acquirer accounts using versioned secret references.
- [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) - consume its completed, reviewed deliverables: Project canonical merchants and accounts into native profiles and MCAs.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / Terminal processing bindings**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform terminal binding repository and APIs`

- `Proposed: platform profile connector projection adapter`

- `Proposed: payment route eligibility terminal integration`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `payment-execution-state-boundary`
- `payment/route-eligibility`
- `platform/profile-connectors`
- `platform/terminal-bindings`

## Implementation plan

- [ ] Implement composite ownership constraints and APIs for proposed, approved, active, suspended, and retired bindings.
- [ ] Validate MCA projection ownership, MID/TID enrollment, certification tuple, encryption domain, currency, and operation capabilities.
- [ ] Define permitted active-binding cardinality per deployment/connector and prevent accidental overlapping duplicate assignments.
- [ ] Publish immutable binding versions to routing/configuration services and snapshot the selected version on attempts.
- [ ] Add suspension and replacement workflows that preserve existing operation completion and reconciliation.

## Acceptance criteria

- [ ] A binding cannot join a terminal, merchant, MCA, or acquirer account from another aggregator.
- [ ] Merchant processing enablement requires an approved binding with valid MID/TID and certification evidence.
- [ ] Routing rejects payloads whose encryption domain does not match the selected binding.
- [ ] Historic attempts retain their original merchant, MID/TID, and binding/configuration versions.
- [ ] Concurrent binding changes cannot create invalid overlapping active assignments.

## Validation scenarios

- [ ] Attempt cross-merchant and cross-aggregator foreign-key joins.
- [ ] Race two activation requests for incompatible bindings.
- [ ] Submit ciphertext referencing another crypto domain and verify pre-dispatch rejection.
- [ ] Retire a binding while an old authorization awaits terminal completion or inquiry.

## Expected deliverables

- Terminal binding schema and API
- Binding eligibility integration and immutable snapshots
- Binding lifecycle/concurrency test evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Acquirer-approved MID/TID allocation and enrollment rules.
- [ ] Crypto domain identifiers, certified route matrix, and supported terminal transaction capabilities.

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
