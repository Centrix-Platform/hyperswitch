---
id: "CTX-097"
title: "Build a reference aggregator APK and secure bootstrap backend"
status: "TODO"
phase: 3
priority: "P1"
size: "L"
repository: "multi-repo"
component: "Integrator reference applications"
depends_on: ["CTX-040", "CTX-041", "CTX-045", "CTX-076", "CTX-078", "CTX-081", "CTX-083", "CTX-084", "CTX-089", "CTX-090", "CTX-091", "CTX-092", "CTX-096"]
requires_one_of: []
conflict_domains: ["samples/aggregator-apk", "samples/aggregator-backend"]
external_inputs: ["Owned sandbox identity/API endpoints, sample backend hosting assumptions, and test aggregator credentials supplied through secure provisioning.", "Licensed vendor artifacts/test devices for optional hardware sample variants."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-097: Build a reference aggregator APK and secure bootstrap backend

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A production SDK needs a runnable integration example that demonstrates the complete trust boundary rather than embedding privileged credentials in a sample APK. Build a reference aggregator backend that holds a scoped sandbox operational key and issues only authorized mobile bootstrap responses. Pair it with a Kotlin host APK and a Java integration fixture showing terminal enrollment/selection, session attachment, confirmation, pending/unknown status, completion, and recovery. Keep merchant selection backend-authorized and prevent samples from becoming public unrestricted token minting endpoints. Use fake adapters by default, with explicit provisioning for approved physical or smart terminal variants. The samples must use owned sandbox configuration, minimal test data, redacted diagnostics, and documented deployment prerequisites. They are reference code, not an assertion of production certification or a generic SoftPOS implementation.

## Prerequisites and dependency outputs

- [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) - consume its completed, reviewed deliverables: Issue rotate and revoke aggregator operational API keys.
- [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) - consume its completed, reviewed deliverables: Mint short-lived merchant terminal and payment-scoped SDK sessions.
- [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) - consume its completed, reviewed deliverables: Expose idempotent aggregator merchant onboarding and operation status.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) - consume its completed, reviewed deliverables: Implement terminal inventory, claim, and activation APIs.
- [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) - consume its completed, reviewed deliverables: Bind merchant terminals to approved acquirer MID/TID configurations.
- [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) - consume its completed, reviewed deliverables: Implement aggregator backend SDK-session bootstrap.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.
- [CTX-089](CTX-089-secure-explicit-intent-binder-and-aidl-partner-communication--TODO.md) - consume its completed, reviewed deliverables: Secure explicit intent, Binder, and AIDL partner communication.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.
- [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) - consume its completed, reviewed deliverables: Integrate terminal completion and issuer-script finalization.
- [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) - consume its completed, reviewed deliverables: Recover SDK operations after process death and network failure.
- [CTX-096](CTX-096-publish-stable-kotlin-and-java-sdk-facades--TODO.md) - consume its completed, reviewed deliverables: Publish stable Kotlin and Java SDK compatibility facades.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Integrator reference applications**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork reference aggregator sample APK`

- `Proposed: reference secure aggregator backend service`

- `Proposed: Kotlin/Java host integration examples`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `samples/aggregator-apk`
- `samples/aggregator-backend`

## Implementation plan

- [ ] Implement an authenticated sandbox backend with scoped operational-key loading from a secret source and authorized SDK-session bootstrap.
- [ ] Build a reference APK using the stable facade and fake adapter by default, with explicit approved vendor build variants.
- [ ] Demonstrate merchant/terminal assignment, single submission, state observation, completion, and original-operation recovery.
- [ ] Add a Java fixture and secure IPC example where the selected vendor requires it.
- [ ] Document setup, synthetic data, credential provisioning, teardown, and security limits; scan packaged artifacts for secrets.

## Acceptance criteria

- [ ] APK artifacts contain no platform or aggregator operational credentials.
- [ ] The backend refuses unauthorized merchant/terminal and arbitrary session constraints.
- [ ] The example displays pending/unknown without initiating a new payment.
- [ ] A developer can run the fake-adapter flow from documented sandbox prerequisites.
- [ ] Vendor variants are gated by explicit dependencies and approved provisioning.

## Validation scenarios

- [ ] Run the sample from clean sandbox setup and complete a fake-adapter payment/recovery flow.
- [ ] Inspect APK strings/resources and repository history fixtures for embedded secrets.
- [ ] Call bootstrap with unauthenticated requests and another aggregator’s identifiers.
- [ ] Kill the sample process after dispatch and recover the original operation.

## Expected deliverables

- Reference aggregator APK and Java fixture
- Secure sandbox bootstrap backend
- Runnable setup and teardown guide

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Owned sandbox identity/API endpoints, sample backend hosting assumptions, and test aggregator credentials supplied through secure provisioning.
- [ ] Licensed vendor artifacts/test devices for optional hardware sample variants.

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
