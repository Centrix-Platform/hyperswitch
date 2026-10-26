---
id: "CTX-018"
title: "Capture the native payment and API compatibility baseline"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "core"
component: "compatibility"
depends_on: ["CTX-003", "CTX-007", "CTX-017"]
requires_one_of: []
conflict_domains: ["native-compatibility-fixtures"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-018: Capture the native payment and API compatibility baseline

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform will insert admission, identity, terminal routing and provisioning boundaries around existing Rust payment execution. Capture native behavior before changing it so later agents can tell intentional contract changes from regressions. Select the pinned feature baseline and a non-live stub/sandbox connector. Record MerchantAccount/Profile/MCA creation, payment creation/confirmation, callback updates, readback and relevant capture/refund behavior, including native identifier and status mappings. Avoid treating upstream Redis locking or a caller-supplied payment ID as the full platform idempotency design. This evidence supports the execution adapter and compatibility gates, while later fault suites verify the new guarantees rather than reproducing implementation details as trivial tests.

## Prerequisites and dependency outputs

- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.
- [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) - consume its completed, reviewed deliverables: Establish a reproducible, isolated local development stack.
- [CTX-017](CTX-017-build-synthetic-fixtures-and-acquirer-fault-harness--TODO.md) - consume its completed, reviewed deliverables: Build synthetic tenant fixtures and an acquirer fault-injection harness.


## Relevant code and ownership

Primary repository/workstream: **core / compatibility**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/payments.rs](../crates/router/src/core/payments.rs)

- [crates/api_models/src/payments.rs](../crates/api_models/src/payments.rs)

- [crates/router/src/core/admin.rs](../crates/router/src/core/admin.rs)

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- [crates/router/tests](../crates/router/tests)

- `Proposed: docs/verification/native-baseline.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `native-compatibility-fixtures`

## Implementation plan

- [ ] Run an isolated baseline native merchant/profile/MCA provisioning sequence on the pinned feature set.
- [ ] Capture payment creation/confirmation, callback/readback and supported lifecycle transitions using synthetic inputs.
- [ ] Record identifier/status/error mappings and existing retry/lock/storage settings relevant to the future facade.
- [ ] Save sanitized contract fixtures and commands, with external calls stubbed or sandbox-scoped.
- [ ] Document gaps between native behavior and the proposed public guarantees without claiming they are already implemented.

## Acceptance criteria

- [ ] Baseline evidence includes reproducible source/configuration pins and commands.
- [ ] No live payment, real merchant onboarding or externally delivered notification occurs.
- [ ] Sanitized fixtures capture meaningful existing API/status behavior.
- [ ] The mapping identifies which guarantees the future platform layer must add.
- [ ] The same native flow can be rerun as the Rust adapter compatibility check.

## Validation scenarios

- [ ] Re-run the fixture flow from a reset synthetic environment and compare stable semantic outputs.
- [ ] Verify callback correlation and capture/refund transitions against native stored identifiers.
- [ ] Confirm output artifacts omit secrets and payment payload contents.

## Expected deliverables

- Native compatibility fixture pack
- Baseline execution/evidence report
- Native/public behavior gap register

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
