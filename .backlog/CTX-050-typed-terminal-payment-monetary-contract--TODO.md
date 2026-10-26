---
id: "CTX-050"
title: "Define typed terminal payload and monetary validation contracts"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "terminal-payment-contract"
depends_on: ["CTX-006", "CTX-014", "CTX-025", "CTX-026", "CTX-049"]
requires_one_of: []
conflict_domains: ["contracts:money", "contracts:terminal-payment", "platform-contract-catalog"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-050: Define typed terminal payload and monetary validation contracts

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Existing e-commerce payment request fields do not establish a complete terminal-processing protocol. Define a typed terminal payment request with integer minor-unit amounts, supported currencies, operation/session identity, terminal configuration version and a secure opaque payload reference or approved encrypted envelope. Separate transport metadata from acquirer-specific EMV/terminal data, and make capability requirements explicit. The gateway validates business constraints without decrypting terminal data in the general service. Decline unknown formats, unsupported currency exponents, overflow, negative values and caller-selected connector credentials. This ticket owns DTOs and validation semantics; vendor capture, cryptography and acquirer adapters remain separate. Public identities should derive from authenticated session scope, with any repeated body identifiers checked for equality rather than treated as authority.

## Prerequisites and dependency outputs

- [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) - consume its completed, reviewed deliverables: Define API, event, monetary and error contract standards.
- [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) - consume its completed, reviewed deliverables: Model trust boundaries, abuse cases and PCI payment-data flows.
- [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) - consume its completed, reviewed deliverables: Track approved terminal and acquirer integration combinations.
- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) - consume its completed, reviewed deliverables: Define payment execution port and implement the Rust compatibility adapter.


## Relevant code and ownership

Primary repository/workstream: **platform / terminal-payment-contract**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/api_models/src/payments.rs](../crates/api_models/src/payments.rs)

- `Proposed: contracts/terminal-payment/`

- `Proposed: platform/payments/validation/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts:money`
- `contracts:terminal-payment`
- `platform-contract-catalog`

## Implementation plan

- [ ] Define versioned discriminated payload formats and allowed metadata fields.
- [ ] Specify currency/minor-unit representation, bounds and rounding rejection rules.
- [ ] Define session/configuration/payload-reference constraints and canonical business fields.
- [ ] Implement gateway validation and executor translation without raw payload logging.
- [ ] Publish SDK/server/acquirer-adapter test vectors and error codes.
- [ ] Honor the CTX-013 authorization-owner decision. The gateway-owned branch dispatches one original request; a vendor-executed result is accepted only through the authenticated idempotent CTX-141 result/inquiry contract and is never converted into a second gateway authorization.

## Acceptance criteria

- [ ] Amounts use bounded integers and never binary floating-point financial values.
- [ ] Unsupported or malformed payload formats fail before execution.
- [ ] Repeated merchant/terminal IDs cannot broaden authenticated scope.
- [ ] Public requests cannot select arbitrary MCA IDs, URLs or credential references.
- [ ] Validation errors contain no sensitive terminal payload data.
- [ ] Unsupported authorization ownership fails closed; client/vendor success cannot produce an uncorrelated gateway charge or silently change financial state authority.

## Validation scenarios

- [ ] Run zero/negative/overflow/currency-exponent and malformed-union cases.
- [ ] Mutate configuration version and payload ownership references.
- [ ] Serialize failures and inspect logs for prohibited payment data.

## Expected deliverables

- Terminal-payment and money schemas.
- Validation library and cross-language test vectors.

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

Inputs are the actual source checkout, completed prerequisite deliverables and any explicitly required decisions above.

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
