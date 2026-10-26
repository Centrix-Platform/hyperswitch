---
id: "CTX-101"
title: "Gate mobile releases on adversarial IPC, auth, replay, and attestation tests"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Mobile security acceptance gate"
depends_on: ["CTX-014", "CTX-042", "CTX-076", "CTX-079", "CTX-080", "CTX-082", "CTX-083", "CTX-084", "CTX-087", "CTX-089", "CTX-092", "CTX-093", "CTX-099"]
requires_one_of: []
conflict_domains: ["android/security-fixtures", "security/mobile-gate"]
external_inputs: ["Security review owner, approved test devices/lab access, severity policy, and exception authority.", "Vendor restrictions on instrumentation and approved synthetic payment data."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}, {"decision": "application_layer_jwe", "value": true, "depends_on": ["CTX-088"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-101: Gate mobile releases on adversarial IPC, auth, replay, and attestation tests

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Turn the terminal/mobile threat model into executable negative tests and independent review evidence before distribution. Attack paths include malicious host/partner applications, stolen SDK tokens, replayed proofs, substituted request bodies, fake terminal IDs, tampered manifests, forged attestation, downgraded configuration, rooted/untrusted device evidence, and old deployment authority after transfer. Tests must verify both no financial side effect and no cross-merchant data exposure. Device attestation is one signal rather than a universal rooted-device detector or certification claim. Use approved synthetic test data and instrumented sandbox systems; do not introduce dangerous production capture hooks to aid testing. Findings need explicit severity, owner, remediation, and re-test results. This gate complements gateway isolation tests and vendor/acquirer certification; none of those substitutes for another.

## Prerequisites and dependency outputs

- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) - consume its completed, reviewed deliverables: Validate device proof transaction integrity and replay limits.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) - consume its completed, reviewed deliverables: Enroll device keys and verify attestation and application identity.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.
- [CTX-089](CTX-089-secure-explicit-intent-binder-and-aidl-partner-communication--TODO.md) - consume its completed, reviewed deliverables: Secure explicit intent, Binder, and AIDL partner communication.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) - consume its completed, reviewed deliverables: Redact mobile logs, crashes, storage, and backups.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.

- Conditional prerequisite: when `application_layer_jwe` equals `true`, complete [CTX-088](CTX-088-support-approved-application-layer-jwe-envelopes--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Mobile security acceptance gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork adversarial security test apps`

- `Proposed: platform SDK authentication abuse-test harness`

- `Proposed: mobile release security gate evidence`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/security-fixtures`
- `security/mobile-gate`

## Implementation plan

- [ ] Map threats to executable attacker APK, proxy, replay, tampered configuration, and attestation fixtures.
- [ ] Implement negative tests for IPC caller identity, token/device binding, body integrity, freshness, downgrade, and deployment revocation.
- [ ] Verify rejected attacks do not create admitted operations, leak merchant data, or emit sensitive diagnostics.
- [ ] Run independent mobile/security review against release candidates and track findings with accountable remediation.
- [ ] Integrate a release gate and signed evidence manifest with documented applicability and unresolved-risk authority.

## Acceptance criteria

- [ ] All mandatory threat-model abuse cases have reproducible pass/fail evidence.
- [ ] Unauthorized/replayed/tampered requests produce no new authorization or merchant-data disclosure.
- [ ] Old deployment authority fails after revoke/reassign according to policy.
- [ ] No critical/high release-blocking finding remains without the explicitly designated exception process.
- [ ] Evidence identifies exact SDK, app, gateway, policy, and device versions tested.

## Validation scenarios

- [ ] Run attacker APK IPC invocation and callback injection cases.
- [ ] Replay stolen tokens/proofs and mutate canonical financial fields.
- [ ] Use invalid attestation chains/challenges and tampered/stale signed manifests.
- [ ] Inspect logs/storage/support bundles during rejected attacks for leakage.

## Expected deliverables

- Executable mobile adversarial test suite
- Security review and remediation evidence
- Release security gate manifest

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Security review owner, approved test devices/lab access, severity policy, and exception authority.
- [ ] Vendor restrictions on instrumentation and approved synthetic payment data.

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
