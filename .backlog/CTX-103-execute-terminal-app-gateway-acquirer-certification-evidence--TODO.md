---
id: "CTX-103"
title: "Execute exact terminal, application, gateway, and acquirer certification evidence"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "External terminal/acquirer approval gate"
depends_on: ["CTX-013", "CTX-014", "CTX-025", "CTX-043", "CTX-050", "CTX-062", "CTX-065", "CTX-080", "CTX-081", "CTX-087", "CTX-091", "CTX-098", "CTX-101", "CTX-102"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["certification-evidence-registry", "certification/evidence", "certification/terminal-acquirer"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Vendor/acquirer/test-body engagement, schedules, fees, test accounts/devices/cards/tools, and authorized submission contacts.", "Applicable L3/acceptance/PCI requirements and formal approval decisions.", "Externally provisioned test keys handled only through approved secure procedures."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}, {"decision": "application_layer_jwe", "value": true, "depends_on": ["CTX-088"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-103: Execute exact terminal, application, gateway, and acquirer certification evidence

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Sandbox engineering tests and a pre-certified terminal do not establish approval for a changed application/gateway/acquirer integration. Execute the applicable certification and acceptance process for each exact production tuple with the responsible vendor, acquirer, and test body. The tuple includes hardware, secure software, kernel, payment application, SDK, host protocol, gateway adapter, crypto/key domain, network environment, and transaction capabilities. Determine which existing approvals can be relied upon and which modifications require L3 or other acceptance testing; do not presume that every deployment has the same program. Store only permitted evidence and test data, never production key material. Approval status must feed the certification admission policy before activation. This is an external gate with real lead times and cannot be closed by an agent declaring unit tests sufficient. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-101](CTX-101-gate-mobile-release-on-adversarial-security-tests--TODO.md) - consume its completed, reviewed deliverables: Gate mobile releases on adversarial IPC, auth, replay, and attestation tests.
- [CTX-102](CTX-102-validate-sdk-crash-network-hardware-and-vendor-compatibility--TODO.md) - consume its completed, reviewed deliverables: Validate SDK crash, network, hardware, and vendor compatibility.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.

- Conditional prerequisite: when `application_layer_jwe` equals `true`, complete [CTX-088](CTX-088-support-approved-application-layer-jwe-envelopes--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / External terminal/acquirer approval gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: certification evidence registry and approved deployment bundles`

- `Proposed: terminal/acquirer certification test plans`

- `Proposed: production admission certification gate`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `certification-evidence-registry`
- `certification/evidence`
- `certification/terminal-acquirer`

## Implementation plan

- [ ] Confirm applicable approval programs, responsible parties, exact tuple, scope, change classification, and certification entry criteria.
- [ ] Submit required architecture, protocol, key-management, test-tool, and software-version evidence through authorized channels.
- [ ] Execute mandated positive/negative, completion, reversal, duplicate, timeout, and reconciliation test cases.
- [ ] Track defects, retests, formal acceptance artifacts, conditions, expiry, and approved transaction capabilities.
- [ ] Register accepted certification bundles and change-control triggers in platform admission policy; keep production disabled until required approvals exist.

## Acceptance criteria

- [ ] Formal evidence names the exact approved terminal/app/gateway/acquirer tuple and permitted operations.
- [ ] All mandatory certification findings are resolved or formally accepted by the responsible external authority.
- [ ] Approval validity, conditions, expiry, and change triggers are recorded.
- [ ] Admission policy permits only approved tuples and blocks unapproved variants.
- [ ] No production secrets or prohibited authentication data are stored in certification artifacts.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.

## Validation scenarios

- [ ] Cross-check submitted build hashes and versions against the release manifest.
- [ ] Run required acquirer/test-body scripts and retain permitted result references.
- [ ] Change one certified component version and verify recertification/admission behavior.
- [ ] Audit evidence access, redaction, and expiry/revocation handling.

## Expected deliverables

- Formal approval/certification evidence references
- Certified deployment tuple and capability registry
- Recertification and change-control checklist

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Vendor/acquirer/test-body engagement, schedules, fees, test accounts/devices/cards/tools, and authorized submission contacts.
- [ ] Applicable L3/acceptance/PCI requirements and formal approval decisions.
- [ ] Externally provisioned test keys handled only through approved secure procedures.

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
