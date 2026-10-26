---
id: "CTX-092"
title: "Recover SDK operations after process death and network failure"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "android"
component: "SDK durable recovery"
depends_on: ["CTX-012", "CTX-057", "CTX-070", "CTX-076", "CTX-082", "CTX-083", "CTX-084", "CTX-090", "CTX-091"]
requires_one_of: []
conflict_domains: ["android/payment-orchestration", "android/recovery-store"]
external_inputs: ["Permitted recovery metadata retention, backup policy, and gateway status-access authorization rules.", "Vendor-supported resume/completion behavior and application upgrade compatibility requirements."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-092: Recover SDK operations after process death and network failure

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Android processes, activities, vendor services, and network sessions can disappear after an authorization has reached the acquirer. Recovery must query or resume the original operation rather than reconstructing and submitting a new charge. Persist only the minimal approved recovery metadata: operation/session identifiers, immutable non-sensitive context references, safe status, and configuration/deployment versions. Do not persist raw card, PIN, track, sensitive authentication data, or encrypted copies of prohibited data after authorization. Key or token loss requires authenticated re-bootstrap with unchanged operation constraints, not unrestricted offline authority. The initial scope is online payment acceptance; lack of connectivity must not silently enable store-and-forward authorization. Background work may retrieve status or perform approved completion steps but cannot run an unbounded generic authorization retry loop.

## Prerequisites and dependency outputs

- [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) - consume its completed, reviewed deliverables: Define safe observability, trace IDs and redaction defaults.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) - consume its completed, reviewed deliverables: Instrument payment attribution and privileged actions without sensitive leakage.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) - consume its completed, reviewed deliverables: Publish signed versioned SDK configuration manifests.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.


## Relevant code and ownership

Primary repository/workstream: **android / SDK durable recovery**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork minimal operation recovery store`

- `External: juspay/hyperswitch-sdk-android/app/src/main/kotlin/io/hyperswitch/sdk/PaymentSession.kt (verify pinned fork)`

- `Proposed: external Android fork lifecycle recovery tests`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/payment-orchestration`
- `android/recovery-store`

## Implementation plan

- [ ] Define a minimal recovery record, secure storage/access policy, expiry/deletion schedule, and exclusion from backups where appropriate.
- [ ] Persist operation correlation atomically before uncertain submission boundaries without saving sensitive payment payloads.
- [ ] Implement startup/reattachment recovery that obtains fresh constrained authority and queries the original gateway/vendor operation.
- [ ] Handle configuration changes, key invalidation, app upgrades, and terminal reassignment without changing historical operation ownership.
- [ ] Restrict background work to approved status/completion recovery and explicitly reject offline charge fallback.

## Acceptance criteria

- [ ] Process restart recovers the same financial operation and does not resubmit authorization.
- [ ] Recovery storage and backups contain no prohibited payment authentication material or operational keys.
- [ ] Token expiry is recoverable through constrained re-bootstrap without amount/merchant escalation.
- [ ] Terminal reassignment cannot expose the prior merchant’s payment details to a new deployment.
- [ ] Offline behavior reports unavailable/pending state and never creates a queued new authorization.

## Validation scenarios

- [ ] Kill process at pre-dispatch, post-dispatch, post-approval, and completion stages.
- [ ] Restore with network unavailable, expired session, invalidated Keystore key, and updated configuration.
- [ ] Inspect local database/preferences/files/backups using approved test data.
- [ ] Reassign the terminal and attempt recovery using the new deployment identity.

## Expected deliverables

- Minimal recovery store and resume workflow
- Process-death/network-loss recovery specification
- Storage and crash-recovery verification evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Permitted recovery metadata retention, backup policy, and gateway status-access authorization rules.
- [ ] Vendor-supported resume/completion behavior and application upgrade compatibility requirements.

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
