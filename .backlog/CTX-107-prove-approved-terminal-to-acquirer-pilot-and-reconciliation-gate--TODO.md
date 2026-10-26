---
id: "CTX-107"
title: "Prove the approved terminal-to-acquirer pilot and reconciliation gate"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Terminal pilot release gate"
depends_on: ["CTX-001", "CTX-013", "CTX-018", "CTX-047", "CTX-051", "CTX-054", "CTX-055", "CTX-057", "CTX-060", "CTX-061", "CTX-062", "CTX-064", "CTX-065", "CTX-071", "CTX-072", "CTX-073", "CTX-080", "CTX-081", "CTX-087", "CTX-090", "CTX-091", "CTX-092", "CTX-098", "CTX-099", "CTX-100", "CTX-101", "CTX-102", "CTX-103", "CTX-104", "CTX-105", "CTX-106"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["certification-evidence-registry", "certification/pilot-evidence", "release-integration", "release/terminal-pilot"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Approved pilot participants, external acquirer/vendor certification decisions, and test or controlled-live transaction authorization.", "Settlement files/inquiry access, designated operational owners, and formal launch authority.", "Resolved device/software/key provisioning and support escalation arrangements."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}, {"decision": "application_layer_jwe", "value": true, "depends_on": ["CTX-088"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-107: Prove the approved terminal-to-acquirer pilot and reconciliation gate

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Close Phase 3 with one controlled aggregator, merchant, terminal family, and acquirer path spanning approved onboarding, enrollment, binding, secure capture, routing, authorization, terminal completion, recovery, refund/reversal as supported, and settlement reconciliation. A visible approval alone is insufficient: verify financial records and external settlement/inquiry evidence, unresolved-outcome handling, isolation, and operational controls. Use the exact release artifacts and certified tuple, with production activation permitted only after required external approvals and named launch authority. Start in approved sandbox or certification environments and use controlled live pilot transactions only under explicit operational authorization. Document what is supported and retain expansion gates for other vendors/networks. This gate should expose remaining external blockers rather than inventing certification or declaring readiness from simulator tests. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite. This qualification ticket runs only synthetic/sandbox/certification transactions under the selected external test authorization. CTX-136 exclusively owns a separately approved limited live pilot after operational readiness gates; this ticket does not create a shortcut to production.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) - consume its completed, reviewed deliverables: Capture the native payment and API compatibility baseline.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) - consume its completed, reviewed deliverables: Reserve charges durably and replay equivalent operations safely.
- [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) - consume its completed, reviewed deliverables: Evaluate active terminal binding and certification before routing.
- [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) - consume its completed, reviewed deliverables: Freeze eligible route and versioned processing configuration per attempt.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) - consume its completed, reviewed deliverables: Enforce capture limits and concurrent partial-capture safety.
- [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) - consume its completed, reviewed deliverables: Implement bounded refunds voids and reversals on the original route.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) - consume its completed, reviewed deliverables: Record immutable payment lifecycle and reconciliation evidence.
- [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) - consume its completed, reviewed deliverables: Import acquirer settlement evidence and reconcile transaction outcomes.
- [CTX-071](CTX-071-cross-aggregator-isolation-release-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on adversarial ownership and privilege isolation.
- [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) - consume its completed, reviewed deliverables: Gate releases on payment concurrency crash and failover invariants.
- [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) - consume its completed, reviewed deliverables: Validate public internal and event contracts across implementations.
- [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) - consume its completed, reviewed deliverables: Enforce firmware, kernel, application, and certification admission policy.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) - consume its completed, reviewed deliverables: Sign and distribute SDK artifacts with Android compatibility CI.
- [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) - consume its completed, reviewed deliverables: Manage terminal revocation, reassignment, rotation, and decommissioning.
- [CTX-100](CTX-100-monitor-terminal-fleet-and-stage-configuration-revocation-rollouts--TODO.md) - consume its completed, reviewed deliverables: Monitor terminal fleets and stage configuration and revocation rollouts.
- [CTX-101](CTX-101-gate-mobile-release-on-adversarial-security-tests--TODO.md) - consume its completed, reviewed deliverables: Gate mobile releases on adversarial IPC, auth, replay, and attestation tests.
- [CTX-102](CTX-102-validate-sdk-crash-network-hardware-and-vendor-compatibility--TODO.md) - consume its completed, reviewed deliverables: Validate SDK crash, network, hardware, and vendor compatibility.
- [CTX-103](CTX-103-execute-terminal-app-gateway-acquirer-certification-evidence--TODO.md) - consume its completed, reviewed deliverables: Execute exact terminal, application, gateway, and acquirer certification evidence.
- [CTX-104](CTX-104-document-kotlin-java-ipc-status-and-recovery-integration--TODO.md) - consume its completed, reviewed deliverables: Document Kotlin, Java, IPC, status, and recovery integration.
- [CTX-105](CTX-105-build-terminal-and-acquirer-failure-simulator--TODO.md) - consume its completed, reviewed deliverables: Build terminal and acquirer simulators with financial failure modes.
- [CTX-106](CTX-106-preserve-immutable-terminal-configuration-and-deployment-audit-history--TODO.md) - consume its completed, reviewed deliverables: Preserve immutable terminal, configuration, and deployment audit history.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.

- Conditional prerequisite: when `application_layer_jwe` equals `true`, complete [CTX-088](CTX-088-support-approved-application-layer-jwe-envelopes--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal pilot release gate**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: terminal pilot test plan and release evidence`

- `Proposed: sandbox/pilot end-to-end harness`

- `Proposed: terminal payment launch and expansion gate`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `certification-evidence-registry`
- `certification/pilot-evidence`
- `release-integration`
- `release/terminal-pilot`

## Implementation plan

- [ ] Assemble the pilot manifest with exact aggregator/merchant/deployment, certified tuple, release artifacts, endpoints, keys-by-reference, and authorized operators.
- [ ] Execute the end-to-end lifecycle using approved test scripts and safe evidence collection across SDK, gateway, acquirer, and reconciliation.
- [ ] Inject duplicate requests, network loss, ambiguous outcome, revocation, and completion/reversal failures within approved pilot procedures.
- [ ] Verify settlement/journal alignment, permission isolation, alerts, support diagnosis, emergency disable, and recovery runbooks.
- [ ] Record release decision, external approvals, unresolved blockers, supported capabilities, and explicit criteria for expanding the fleet.
- [ ] Resolve every one-of prerequisite to the same CTX-013 pilot selection, record the chosen adapter and exact tuple, and leave the other adapter in the expansion lane.

## Acceptance criteria

- [ ] A complete approved payment lifecycle reconciles to the external acquirer/settlement evidence.
- [ ] Duplicate and ambiguous-outcome scenarios produce no unexplained second financial action.
- [ ] Terminal/merchant suspension prevents new capture while original operations remain safely recoverable.
- [ ] Release evidence names all exact artifacts, policy/config versions, approvals, and operators.
- [ ] Production or fleet expansion remains blocked when certification, reconciliation, security, or operational gates fail.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.
- [ ] Qualification evidence identifies a sandbox/certification environment and cannot be mistaken for limited-live-pilot or broad-launch authorization.

## Validation scenarios

- [ ] Run approved authorization/capture/refund/reversal and terminal completion cases supported by the selected path.
- [ ] Recover after app/server failure and lost response using original operation references.
- [ ] Match gateway journal, acquirer inquiry, callbacks, and settlement records.
- [ ] Exercise tenant-negative access, emergency disable, and rollback/recovery playbooks.
- [ ] Attempt to use live endpoints or credentials from the qualification profile and verify the environment/authorization boundary rejects the action.

## Expected deliverables

- Pilot end-to-end and reconciliation evidence pack
- Launch/expansion gate decision record
- Terminal payment operational runbooks and supported-scope manifest

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Approved pilot participants, external acquirer/vendor certification decisions, and test or controlled-live transaction authorization.
- [ ] Settlement files/inquiry access, designated operational owners, and formal launch authority.
- [ ] Resolved device/software/key provisioning and support escalation arrangements.

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
