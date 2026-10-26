---
id: "CTX-091"
title: "Integrate terminal completion and issuer-script finalization"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "multi-repo"
component: "Terminal completion workflow"
depends_on: ["CTX-050", "CTX-056", "CTX-057", "CTX-062", "CTX-077", "CTX-087", "CTX-090"]
requires_one_of: [["CTX-085", "CTX-086"]]
conflict_domains: ["android/terminal-completion", "payment-execution-state-boundary", "payment/terminal-completion"]
external_inputs: ["CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.", "Exact vendor/acquirer issuer script, completion, advice, and reversal protocol documentation.", "Approved test scripts, timeout rules, retention restrictions, and operational exception handling."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: ["authorization_owner", "pilot_terminal_adapter"]
conditional_dependencies: [{"decision": "authorization_owner", "value": "vendor", "depends_on": ["CTX-141"]}]
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-091: Integrate terminal completion and issuer-script finalization

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A successful online authorization may still require terminal completion, issuer authentication data, issuer script processing, or advice/reversal according to the exact vendor/acquirer protocol. Implement this as an explicit stage attached to the original payment attempt, not a second charge or an optional UI callback. Sensitive EMV-related material must stay within the approved payload/security boundary and retention rules. The server and SDK must agree which party drives completion, how completion acknowledgments are deduplicated, what a failed or absent acknowledgment means, and when an inquiry, advice, or reversal is required. Hardware disconnection after issuer approval is a financial exception with protocol-specific handling. Record safe terminal outcome metadata and retain immutable attempt correlation while allowing an operation to remain unresolved until the approved completion/reconciliation process finishes. Use the same CTX-013-selected adapter and approved combination throughout this ticket; the alternative adapter is not an initial pilot prerequisite.

## Prerequisites and dependency outputs

- [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) - consume its completed, reviewed deliverables: Define typed terminal payload and monetary validation contracts.
- [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) - consume its completed, reviewed deliverables: Implement documented downstream reference and duplicate-handling rules.
- [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) - consume its completed, reviewed deliverables: Resolve uncertain outcomes through inquiry and reconciliation.
- [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) - consume its completed, reviewed deliverables: Coordinate terminal completion issuer scripts and required reversals.
- [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) - consume its completed, reviewed deliverables: Introduce a vendor-neutral terminal adapter API.
- [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) - consume its completed, reviewed deliverables: Enforce the opaque payment-payload boundary and acquirer crypto adapter.
- [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) - consume its completed, reviewed deliverables: Implement SDK payment-state and single-submission orchestration.

One selected implementation is required from: [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) or [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md). Use the exact CTX-013-selected terminal/app/acquirer combination; an unrelated completed branch is insufficient.

- Required recorded decision: `authorization_owner` in [decisions.json](decisions.json), with owner evidence.

- Required recorded decision: `pilot_terminal_adapter` in [decisions.json](decisions.json), with owner evidence.

- Conditional prerequisite: when `authorization_owner` equals `"vendor"`, complete [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md). An unresolved decision blocks this gate; an optional feature cannot bypass its qualification.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / Terminal completion workflow**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: external Android fork adapter completion implementation`

- `Proposed: platform terminal completion instructions and acknowledgment APIs`

- `Proposed: approved acquirer completion/reversal adapter`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `android/terminal-completion`
- `payment-execution-state-boundary`
- `payment/terminal-completion`

## Implementation plan

- [ ] Specify the vendor/acquirer completion sequence, data ownership, permitted data lifetime, timeout, and failure/reversal rules.
- [ ] Map server completion instructions to the vendor adapter without exposing sensitive issuer data through general host APIs.
- [ ] Persist safe completion state and correlation; make instruction delivery and acknowledgments idempotent.
- [ ] Implement reconnect and original-operation resume for completion where the vendor contract permits it.
- [ ] Emit completion failure/advice/reversal work through the existing server workflow without a new authorization.
- [ ] Validate completion against the selected vendor/acquirer protocol and approved hardware evidence; use mocks only for development, never to close the production completion gate.

## Acceptance criteria

- [ ] Approval requiring completion is not prematurely reported as fully finalized.
- [ ] Duplicate instructions and acknowledgments cannot repeat a financial side effect.
- [ ] Completion uses the original attempt and frozen terminal/acquirer configuration.
- [ ] Lost terminal connectivity follows documented inquiry/advice/reversal policy.
- [ ] Logs and durable records retain only allowed completion metadata and safe references.
- [ ] Evidence identifies the CTX-013-selected adapter and exact approved combination; an unselected adapter or mock-only completion cannot satisfy the production acceptance gate.

## Validation scenarios

- [ ] Run issuer-script success, rejection, partial execution, and no-script fixtures.
- [ ] Disconnect terminal after approval but before completion acknowledgment.
- [ ] Duplicate and reorder completion instructions, acknowledgments, and acquirer callbacks.
- [ ] Restart both SDK and server worker mid-completion and verify original-operation recovery.

## Expected deliverables

- SDK/server terminal completion integration
- Vendor-specific completion and exception sequence fixtures
- Completion/advice/reversal test evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] CTX-013 path-selection record and the completed selected adapter (CTX-085 or CTX-086), with exact vendor/application/acquirer evidence; one-of selection is consistent across the pilot.
- [ ] Exact vendor/acquirer issuer script, completion, advice, and reversal protocol documentation.
- [ ] Approved test scripts, timeout rules, retention restrictions, and operational exception handling.

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
