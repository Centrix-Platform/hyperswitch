---
id: "CTX-141"
title: "Support authenticated vendor-executed authorization ownership where the selected integration requires it"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Conditional vendor authorization execution branch"
depends_on: ["CTX-013", "CTX-049", "CTX-050", "CTX-053", "CTX-057", "CTX-058", "CTX-062", "CTX-076", "CTX-077", "CTX-084"]
requires_one_of: []
conflict_domains: ["android/terminal-api", "contracts/payment-execution-port", "payment-execution-state-boundary", "payment/authorization-ownership", "payment/vendor-result-ingestion", "platform-contract-catalog"]
external_inputs: ["CTX-013’s explicit gateway-versus-vendor authorization-owner decision and exact selected terminal/application/acquirer tuple.", "Vendor/acquirer documentation for authoritative result authentication, signature/key discovery and rotation or server authentication, provider reference uniqueness, finality, inquiry, timeout, completion, and reversal semantics.", "Approved vendor sandbox/test application, authenticated test vectors, callback/inquiry access, and secure provisioning of test credentials without attaching secrets to the ticket.", "Protocol support for pre-reserved operation correlation or an explicitly approved adoption procedure when authorization precedes gateway admission."]
external_inputs_resolved: false
applicability: "conditional"
applicability_decision: "pending"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-141: Support authenticated vendor-executed authorization ownership where the selected integration requires it

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

CTX-013 must explicitly select whether the gateway or the approved vendor payment application owns authorization for the first terminal integration. This conditional ticket applies when the vendor application performs the financial authorization itself. Its result is evidence about an existing provider transaction, never a request to submit another gateway charge. Extend the language-neutral execution port, terminal DTOs, durable state machine, and authenticated result/inquiry ingestion to represent that ownership. A client callback or displayed success is not authoritative: verify documented vendor signatures or authenticated provider evidence and reconcile ambiguous outcomes through the original route. Preserve provider references, finality, merchant/deployment identity, frozen processing configuration, and required terminal completion. Duplicate or reordered reports must map idempotently to one operation. Gateway authorization dispatch and cross-acquirer failover remain prohibited for vendor-owned attempts, including after timeout.

## Prerequisites and dependency outputs

- [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) - consume its completed, reviewed deliverables: Discover the first terminal/acquirer integration and certification requirements.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.
- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-058](CTX-058-authenticated-acquirer-notification-inbox--TODO.md) - consume its completed, reviewed deliverables: Authenticate and deduplicate inbound acquirer notifications.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) - consume its completed, reviewed deliverables: Secure SDK HTTP transport, sender-constrained auth, and request integrity.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Conditional vendor authorization execution branch**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform language-neutral payment execution port and terminal payment DTOs`

- `Proposed: platform authenticated vendor-result callback and inquiry adapter`

- `Proposed: platform vendor-owned attempt state and dispatcher exclusion`

- `Proposed: external Android fork vendor-owned terminal result and completion mapping`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/terminal-api`
- `contracts/payment-execution-port`
- `payment-execution-state-boundary`
- `payment/authorization-ownership`
- `payment/vendor-result-ingestion`
- `platform-contract-catalog`

## Implementation plan

- [ ] Record CTX-013’s authorization-owner decision and approved vendor/acquirer contract; add explicit gateway-owned versus vendor-owned execution modes with immutable per-operation ownership.
- [ ] Extend execution-port/terminal DTOs with vendor operation/session identity, safe provider reference, evidence reference, finality, inquiry capability, and completion ownership without trusting mobile status assertions.
- [ ] Reserve and correlate the durable operation before vendor invocation where supported; define a separately validated adoption path only if the vendor protocol requires it, with uniqueness preventing one provider transaction from attaching to multiple payments.
- [ ] Implement authenticated vendor-result and inquiry ingestion using the documented signature/authentication scheme; validate environment, amount, currency, merchant, terminal deployment, freshness, provider identity, and original operation correlation.
- [ ] Project validated results idempotently into attempts/state/outbox events, handle provisional/unknown and conflicting evidence, and preserve original provider route and terminal-completion workflow.
- [ ] Enforce an execution fence that excludes vendor-owned operations from gateway authorization dispatch and automatic cross-route fallback; use original-reference inquiry/reconciliation after uncertain outcomes.
- [ ] Add contract, concurrency, tampering, reordering, timeout, crash, and completion tests against the approved vendor sandbox or authenticated protocol fixtures, with mock-only evidence insufficient for production readiness.

## Acceptance criteria

- [ ] CTX-013 documents the selected authorization owner and exact vendor/application/acquirer combination; gateway capture-only integrations can leave this ticket conditional and unexecuted.
- [ ] A vendor-executed approval, decline, callback, retry, or inquiry can never enqueue or invoke a second gateway authorization.
- [ ] Only authenticated and fully correlated provider evidence can establish authoritative financial state; mobile success alone remains unverified/pending.
- [ ] Duplicate and reordered results map to one durable operation/provider transaction, while mismatched or conflicting evidence is rejected or quarantined with safe audit records.
- [ ] Unknown outcomes query/reconcile the original provider reference and route; no timeout changes execution owner, merchant, or acquirer.
- [ ] Terminal completion/finality and safe result events preserve the selected protocol’s required sequence and do not prematurely declare final success.
- [ ] Integration evidence includes exact adapter, contract, signing/authentication configuration references, fault scenarios, and financial side-effect counts without secret or prohibited payment-data retention.

## Validation scenarios

- [ ] Import the same authenticated vendor authorization concurrently through client forwarding, direct callback, and inquiry; assert one operation mapping, one result transition, and zero gateway authorization calls.
- [ ] Reject forged signatures, wrong vendor/environment/merchant/terminal, altered amount/currency, stale/replayed evidence, and provider references already attached to another operation.
- [ ] Kill the host or ingesting worker after vendor approval but before result persistence, then recover through original-reference inquiry without another charge.
- [ ] Deliver provisional/final results out of order, conflicting final evidence, and completion-required approval with lost acknowledgment; verify permitted state transitions and exception/reconciliation handling.
- [ ] Run both execution modes against the selected authenticated integration fixtures and confirm gateway-owned flows retain their normal dispatch while vendor-owned flows cannot enter it.

## Expected deliverables

- Authorization-ownership execution contract and CTX-013 selection record integration
- Authenticated vendor-result/inquiry adapter and idempotent state projection
- SDK terminal result/completion mapping for vendor-owned execution
- Integration/fault evidence proving no duplicate gateway authorization

## External inputs and applicability

Applicability: **conditional**. Initial decision: **pending**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013’s explicit gateway-versus-vendor authorization-owner decision and exact selected terminal/application/acquirer tuple.
- [ ] Vendor/acquirer documentation for authoritative result authentication, signature/key discovery and rotation or server authentication, provider reference uniqueness, finality, inquiry, timeout, completion, and reversal semantics.
- [ ] Approved vendor sandbox/test application, authenticated test vectors, callback/inquiry access, and secure provisioning of test credentials without attaching secrets to the ticket.
- [ ] Protocol support for pre-reserved operation correlation or an explicitly approved adoption procedure when authorization precedes gateway admission.

Record evidence and update `external_inputs_resolved` only after these inputs are verified. Continue independent work while a necessary input is pending.

Activate this conditional branch only with the recorded integration requirement and owner evidence. Downstream conditional prerequisites enforce its completion before qualified use.

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
