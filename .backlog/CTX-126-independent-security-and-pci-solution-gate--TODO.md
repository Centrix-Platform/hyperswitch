---
id: "CTX-126"
title: "Complete independent penetration testing and PCI solution review"
status: "TODO"
phase: 4
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Security production gate"
depends_on: ["CTX-014", "CTX-043", "CTX-071", "CTX-101", "CTX-103", "CTX-123", "CTX-124", "CTX-125", "CTX-134"]
requires_one_of: []
conflict_domains: ["certification-evidence", "certification-evidence-registry", "security-assessment"]
external_inputs: ["Qualified independent security tester and relevant PCI assessor/solution provider; signed scope/rules of engagement; approved test environments; terminal/acquirer evidence and authorized business risk reviewers."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}, {"decision": "application_layer_jwe", "value": true, "depends_on": ["CTX-088"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-126: Complete independent penetration testing and PCI solution review

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A payment gateway and terminal solution require assessment of the deployed data flow, administrative plane, SDK and ability to affect payment security. Public-key encryption, device attestation and a previously certified terminal do not by themselves establish PCI scope reduction or certify the new gateway integration. Obtain qualified review of the chosen architecture, key custody and service-provider responsibilities, then remediate findings in the implementation. Independent testing must use an explicitly authorized scope and controlled environments; this ticket is not authorization to scan external acquirers or customer applications. Keep penetration testing, PCI assessment and acquirer/EMV integration acceptance as distinct evidence tracks. Record findings without storing live cardholder data or secrets in the backlog.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) - consume its completed, reviewed deliverables: Enforce secret retrieval rotation and cryptographic service boundaries.
- [CTX-071](CTX-071-cross-aggregator-isolation-release-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on adversarial ownership and privilege isolation.
- [CTX-101](CTX-101-gate-mobile-release-on-adversarial-security-tests--TODO.md) - consume its completed, reviewed deliverables: Gate mobile releases on adversarial IPC, auth, replay, and attestation tests.
- [CTX-103](CTX-103-execute-terminal-app-gateway-acquirer-certification-evidence--TODO.md) - consume its completed, reviewed deliverables: Execute exact terminal, application, gateway, and acquirer certification evidence.
- [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) - consume its completed, reviewed deliverables: Qualify aggregator portal-to-SDK contracts end to end.
- [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) - consume its completed, reviewed deliverables: Implement immutable administrative and privileged access auditing.
- [CTX-125](CTX-125-privacy-retention-closure-and-legal-holds--TODO.md) - consume its completed, reviewed deliverables: Implement data lifecycle, privacy and account-closure workflows.
- [CTX-134](CTX-134-production-infrastructure-hardening-and-scaling--TODO.md) - consume its completed, reviewed deliverables: Implement production IaC, segmentation and resilient runtime configuration.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.

- Conditional prerequisite: when `application_layer_jwe` equals `true`, complete [CTX-088](CTX-088-support-approved-application-layer-jwe-envelopes--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Security production gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [README.md](../README.md)

- [config/deployments/production.toml](../config/deployments/production.toml)

- `Proposed: docs/security/assessment-evidence/`

- `Proposed: docs/security/payment-data-flow.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `certification-evidence`
- `certification-evidence-registry`
- `security-assessment`

## Implementation plan

- [ ] Prepare current data-flow diagrams, asset inventory, threat model, capture/encryption/decryption boundaries, key custody and integration/certification matrix.
- [ ] Engage qualified independent assessors/testers under a documented scope, rules of engagement and approved test accounts/environments.
- [ ] Assess portal/API tenancy, IAM, SDK/device/IPC, supply chain, secrets, segmentation and payment-state/idempotency failure controls.
- [ ] Track and remediate findings through linked execution tickets with severity, owner and independent retest evidence.
- [ ] Obtain solution-specific PCI scope/responsibility conclusions and confirm terminal/acquirer acceptance evidence separately.
- [ ] Assemble a release-bound assessment report with accepted residual risks and explicit expiry/change triggers.

## Acceptance criteria

- [ ] Authorized independent testing covers the documented portal, API, device and operational boundaries.
- [ ] All release-blocking findings are remediated and retested or have formally approved dispositions under policy.
- [ ] PCI scope/responsibility is documented by the appropriate qualified parties for the actual deployed solution.
- [ ] Terminal/acquirer approval evidence is tracked separately from penetration-test completion.
- [ ] Assessment evidence identifies exact software/configuration versions and material change triggers.
- [ ] No unapproved external scanning, live-card use or credential disclosure occurs as a side effect of implementation.

## Validation scenarios

- [ ] Review scope completeness against threat model, asset inventory and data-flow diagrams.
- [ ] Reproduce and independently retest critical/high findings in the controlled environment.
- [ ] Check evidence linkage, signoffs, report dates and configuration hashes for the release candidate.

## Expected deliverables

- Independent test scope and redacted findings/remediation register.
- PCI solution scope/responsibility evidence.
- Release-bound security acceptance report.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Qualified independent security tester and relevant PCI assessor/solution provider; signed scope/rules of engagement; approved test environments; terminal/acquirer evidence and authorized business risk reviewers.

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
