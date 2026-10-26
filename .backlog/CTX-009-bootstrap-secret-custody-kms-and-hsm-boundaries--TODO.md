---
id: "CTX-009"
title: "Bootstrap secret custody, service credentials and cryptographic boundaries"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "infra"
component: "security"
depends_on: ["CTX-001", "CTX-008", "CTX-014"]
requires_one_of: []
conflict_domains: ["infra-security", "secret-custody"]
external_inputs: ["Approved secret/KMS provider and, where applicable, acquirer/HSM custodians and procedures."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-009: Bootstrap secret custody, service credentials and cryptographic boundaries

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The platform will hold aggregator operational-key verifiers and references to acquirer credentials while terminal payment encryption should preferably terminate only in the approved vendor/acquirer security boundary. Generic application-layer JWE does not replace terminal PIN/data key management or reduce PCI scope by itself. Bootstrap a secret-store/KMS identity model, key-purpose separation and rotation workflow before credentials are copied into configuration files. Distinguish public encryption keys, device identity keys, API signing keys, database encryption keys and acquirer/HSM keys. The general gateway should not automatically receive terminal decryption authority. Physical HSM access, approved cryptographic procedures and external custodians remain explicit inputs to the selected integration.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) - consume its completed, reviewed deliverables: Define sandbox/live cells, data residency and home-region ownership.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.


## Relevant code and ownership

Primary repository/workstream: **infra / security**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [config/config.example.toml](../config/config.example.toml)

- [crates/external_services](../crates/external_services)

- [crates/router/src/configs/settings.rs](../crates/router/src/configs/settings.rs)

- `Proposed: docs/security/secret-custody.md`

- `Proposed: infra/security`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `infra-security`
- `secret-custody`

## Implementation plan

- [ ] Classify every key/secret purpose and its owning service, environment, retention and rotation policy.
- [ ] Provision or model workload identity and least-privilege access to a secret store/KMS for local and target infrastructure.
- [ ] Define immutable versioned credential references, audit access and emergency revocation.
- [ ] Separate general gateway authorization from any PCI decryption/HSM service or vendor-controlled key domain.
- [ ] Provide sandbox secret fixtures and a recovery/rotation runbook that does not print secret values.

## Acceptance criteria

- [ ] A custody matrix assigns owner and consumer identities for every secret class.
- [ ] No platform master or aggregator operational secret is embedded in an APK, browser or repository.
- [ ] Normal gateway identity cannot retrieve terminal decryption keys by default.
- [ ] Secret versions can rotate without rewriting historical attempt attribution.
- [ ] Audit and recovery procedures avoid exposing usable secrets in logs or build output.

## Validation scenarios

- [ ] Attempt cross-environment and unauthorized service secret access using synthetic credentials.
- [ ] Rotate a sandbox signing/operational credential and verify overlap plus revocation behavior.
- [ ] Review custody boundaries against the threat model and approved terminal solution.

## Expected deliverables

- Secret/key custody matrix
- Workload identity/KMS bootstrap definitions
- Rotation and recovery procedure

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Approved secret/KMS provider and, where applicable, acquirer/HSM custodians and procedures.

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
