---
id: "CTX-020"
title: "Provision aggregators through a resumable native-account workflow"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "aggregator-provisioning"
depends_on: ["CTX-009", "CTX-016", "CTX-018", "CTX-019"]
requires_one_of: []
conflict_domains: ["native:admin", "workflow:aggregator-provisioning"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["native_account_topology"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-020: Provision aggregators through a resumable native-account workflow

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The chosen topology maps one aggregator to a native MerchantAccount and preferably one Organization, inside an infrastructure Tenant selected by platform placement. Native account creation does not establish the commercial or operational lifecycle of your customer. Build a resumable control-plane workflow that creates the canonical aggregator, organization and account, records each native identifier, and activates access only after required provisioning succeeds. There is no atomic transaction across platform storage and native administration APIs. Recovery must inspect recorded outcomes and avoid creating duplicate organizations or accounts after timeouts. Only platform authority may initiate this workflow; aggregator credentials cannot provision peers or choose native schema names. Tenant infrastructure creation remains a separate operator responsibility.

## Prerequisites and dependency outputs

- [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) - consume its completed, reviewed deliverables: Bootstrap secret custody, service credentials and cryptographic boundaries.
- [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) - consume its completed, reviewed deliverables: Secure ingress and isolate native admin and trusted-header paths.
- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.
- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.

- Required recorded decision: `native_account_topology` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **platform / aggregator-provisioning**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/core/admin.rs](../crates/router/src/core/admin.rs)

- [crates/diesel_models/src/organization.rs](../crates/diesel_models/src/organization.rs)

- [crates/diesel_models/src/merchant_account.rs](../crates/diesel_models/src/merchant_account.rs)

- `Proposed: platform/aggregators/provisioning/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `native:admin`
- `workflow:aggregator-provisioning`

## Implementation plan

- [ ] Define provisioning states and idempotency scope for platform requests.
- [ ] Implement private adapter calls for organization and MerchantAccount provisioning.
- [ ] Persist step results and deterministic lookup references before advancing.
- [ ] Add recovery reconciliation for lost responses and partial native resources.
- [ ] Gate activation on environment placement, key bootstrap and required configuration readiness.

## Acceptance criteria

- [ ] Repeating one provisioning request returns the same aggregator and operation.
- [ ] A failure after organization creation resumes without duplicating it.
- [ ] No aggregator API can create another aggregator or select an arbitrary native tenant.
- [ ] Activation is blocked while mandatory steps are incomplete.
- [ ] Provisioning events expose public IDs and safe status only.

## Validation scenarios

- [ ] Crash after each native create call and resume the workflow.
- [ ] Return an ambiguous native timeout and reconcile by recorded reference.
- [ ] Attempt provisioning with aggregator authority and expect denial.

## Expected deliverables

- Aggregator provisioning state machine and private adapter.
- Operator endpoint contract and recovery procedure.

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
