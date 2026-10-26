---
id: "CTX-078"
title: "Implement terminal inventory, claim, and activation APIs"
status: "TODO"
phase: 3
priority: "P0"
size: "L"
repository: "platform"
component: "Terminal lifecycle API"
depends_on: ["CTX-026", "CTX-029", "CTX-031", "CTX-038", "CTX-047", "CTX-076"]
requires_one_of: []
conflict_domains: ["contracts/terminal-sdk", "platform-contract-catalog", "platform/terminal-registry"]
external_inputs: ["Vendor device inventory/provisioning evidence and legitimate transfer procedures.", "Aggregator ownership verification and operational activation policy."]
external_inputs_resolved: false
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-078: Implement terminal inventory, claim, and activation APIs

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

A terminal serial number or client-submitted terminal_id is not proof that a device belongs to an aggregator or merchant. Build the server lifecycle that registers approved stock, permits an authorized aggregator to claim a device or deployment, and activates it only after identity and processing prerequisites are satisfied. Keep physical device inventory distinct from a merchant-specific deployment, because reassignment must not rewrite historical payment ownership. Enrollment should use expiring challenges or vendor enrollment evidence and idempotent operations rather than reusable activation secrets embedded in APKs. The registry exposes safe status to SDK configuration and routing services, while privileged inventory administration remains in the platform control plane. This ticket establishes lifecycle APIs; attestation verification and acquirer binding validation are implemented by their dedicated tickets.

## Prerequisites and dependency outputs

- [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) - consume its completed, reviewed deliverables: Model device deployments and merchant-specific processing bindings.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) - consume its completed, reviewed deliverables: Protect canonical tables with RLS and composite ownership constraints.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) - consume its completed, reviewed deliverables: Propagate merchant activation suspension and terminal revocation safely.
- [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) - consume its completed, reviewed deliverables: Define versioned terminal and SDK configuration contracts.


## Relevant code and ownership

Primary repository/workstream: **platform / Terminal lifecycle API**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- `Proposed: platform terminal registry service and APIs`

- `Proposed: platform terminal inventory and deployment migrations`

- `Proposed: terminal lifecycle OpenAPI operations`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `contracts/terminal-sdk`
- `platform-contract-catalog`
- `platform/terminal-registry`

## Implementation plan

- [ ] Define inventory, claim, enrollment-pending, activated, suspended, and decommissioned transitions with authorized actors and audit events.
- [ ] Implement aggregator-scoped idempotent claim/enrollment APIs with expiring one-use challenge references.
- [ ] Separate immutable physical device identity from versioned merchant deployment records and enforce unique active assignments.
- [ ] Require validated device enrollment and approved processing prerequisites before activation; fail closed when dependencies are unavailable.
- [ ] Expose tenant-scoped inventory/read status and lifecycle events for SDK sessions, routing, and console consumers.

## Acceptance criteria

- [ ] An aggregator cannot claim, read, or activate another aggregator’s terminal records.
- [ ] A serial number alone cannot activate a device or obtain a payment-capable SDK session.
- [ ] Duplicate claim requests return the same lifecycle resource without creating duplicate active deployments.
- [ ] Activation is blocked until explicit identity, merchant, and processing checks are satisfied.
- [ ] All lifecycle transitions preserve actor, timestamp, reason, and previous deployment identity.

## Validation scenarios

- [ ] Attempt cross-aggregator enumeration and claim using known terminal identifiers.
- [ ] Replay expired and consumed enrollment challenges.
- [ ] Race two claims for the same device and inspect unique active-assignment enforcement.
- [ ] Activate while merchant, certification, or enrollment prerequisites are suspended.

## Expected deliverables

- Terminal lifecycle API and persistence implementation
- Enrollment/activation state diagram and contract fixtures
- Lifecycle authorization and concurrency evidence

## External inputs and applicability

Applicability: **required**. Initial decision: **selected**. Do not infer that an unavailable vendor account, approval or input has been supplied.

- [ ] Vendor device inventory/provisioning evidence and legitimate transfer procedures.
- [ ] Aggregator ownership verification and operational activation policy.

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
