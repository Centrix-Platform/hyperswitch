---
id: "CTX-013"
title: "Discover the first terminal/acquirer integration and certification requirements"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "multi-repo"
component: "certification"
depends_on: ["CTX-001", "CTX-003"]
requires_one_of: []
conflict_domains: ["pilot-integration-contracts"]
external_inputs: ["Vendor SDK/protocol and terminal evidence; acquirer sandbox, MID/TID and duplicate/inquiry/reversal documentation; approval owners."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-013: Discover the first terminal/acquirer integration and certification requirements

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The initial product must support an exact terminal model, firmware/kernel/payment-application version, gateway integration and acquirer network. A terminal advertised as pre-certified does not prove that a new end-to-end processing path is approved. Obtain vendor protocols, device trust/enrollment requirements, MID/TID allocation rules, encrypted payload formats, downstream duplicate behavior, inquiry/reversal flows and certification evidence requirements for the chosen pilot. Distinguish physical readers, smart-terminal payment apps and COTS acceptance solutions; the general Hyperswitch checkout SDK is not an approved replacement for their secure capture stack. This ticket records authoritative external inputs and their versions so later agents can implement adapters without guessing sensitive wire formats or financial semantics.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **multi-repo / certification**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [add_connector.md](../add_connector.md)

- [crates/hyperswitch_connectors](../crates/hyperswitch_connectors)

- `Proposed: docs/integrations/pilot-terminal-acquirer.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `pilot-integration-contracts`

## Implementation plan

- [ ] Select the initial terminal/acquirer combination or enumerate the required decision inputs from CTX-001.
- [ ] Collect versioned vendor SDK/protocol, sandbox, trust roots, signing identity and terminal enrollment documentation.
- [ ] Document authorization/completion/inquiry/reversal, duplicate reference semantics and settlement artifacts.
- [ ] Build the approved-combination/certification matrix, expiry and change-trigger rules.
- [ ] Assign evidence owners and a certification execution path for CTX-103 and pilot gating.
- [ ] Record gateway-versus-vendor authorization ownership, selected physical/smart adapter, and supplementary-JWE requirement in .backlog/decisions.json with versioned vendor/acquirer evidence; mark pending inputs unresolved until actually supplied.

## Acceptance criteria

- [ ] The selected combination identifies model, firmware, kernel, application, network and crypto domain versions.
- [ ] No wire format, trust root, certification status or duplicate guarantee is invented.
- [ ] Required inquiry/reversal and terminal completion flows are documented with authoritative evidence.
- [ ] Missing contracts, sandbox access and approval owners are explicit blockers for dependent adapters.
- [ ] The matrix distinguishes component approval from end-to-end integration acceptance.
- [ ] The approved pilot tuple explicitly selects CTX-085 or CTX-086, gateway or vendor authorization, and whether JWE is required; decision evidence activates the correct dependency branch.

## Validation scenarios

- [ ] Review the matrix with supplied vendor/acquirer evidence and note validity dates.
- [ ] Walk through approved, declined, timed-out and terminal-incomplete authorizations using the supplied protocol.
- [ ] Verify every selected dependency has a reproducible version/reference.

## Expected deliverables

- Terminal/acquirer capability and certification matrix
- Versioned integration input register
- Certification evidence plan

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Vendor SDK/protocol and terminal evidence; acquirer sandbox, MID/TID and duplicate/inquiry/reversal documentation; approval owners.

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
