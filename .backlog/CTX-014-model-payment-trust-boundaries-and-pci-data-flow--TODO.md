---
id: "CTX-014"
title: "Model trust boundaries, abuse cases and PCI payment-data flows"
status: "TODO"
phase: 1
priority: "P0"
size: "M"
repository: "platform"
component: "security"
depends_on: ["CTX-001", "CTX-002", "CTX-003"]
requires_one_of: []
conflict_domains: ["architecture-domain-model", "security-data-classification"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-014: Model trust boundaries, abuse cases and PCI payment-data flows

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

The white-label platform adds nested authority, customer-supplied APKs, terminal identity, portal sessions and cross-domain automation to a payment switch. Threat-model these boundaries before adopting an encryption or tenancy mechanism as a security guarantee. Terminal ID strings are not device authentication; public encryption does not authenticate the sender; RLS request settings do not protect against a fully compromised service; Redis locks do not ensure payment deduplication after failover. The preferred architecture keeps raw capture in an approved vendor component and general gateway services outside decryption custody where possible. Actual PCI scope and solution approval require qualified assessment of the deployed combination, not assumptions based on tokenization or encrypted transport.

## Prerequisites and dependency outputs

- [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) - consume its completed, reviewed deliverables: Define the platform charter, pilot scope and funds flow.
- [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) - consume its completed, reviewed deliverables: Decide the native account topology and public domain terminology.
- [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) - consume its completed, reviewed deliverables: Inventory repositories, pinned versions and mutually compatible features.


## Relevant code and ownership

Primary repository/workstream: **platform / security**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/router/src/services/authentication.rs](../crates/router/src/services/authentication.rs)

- [crates/router/src/services/authorization.rs](../crates/router/src/services/authorization.rs)

- [crates/router/src/core/api_locking.rs](../crates/router/src/core/api_locking.rs)

- `Proposed: docs/security/platform-threat-model.md`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `architecture-domain-model`
- `security-data-classification`

## Implementation plan

- [ ] Draw trust/data-flow diagrams for portal, aggregator backend, SDK, terminal service, gateway, native engine, credentials and acquirer.
- [ ] Classify CHD, SAD, PII, credentials, encrypted blobs, tokens, audit records and their allowed transient/persistent locations.
- [ ] Enumerate cross-tenant IDOR, key escalation, malicious APK/IPC, stale device, replay, supply-chain and duplicate-charge abuse cases.
- [ ] Specify controls and evidence ownership, including minimum capture/decryption exposure and one-writer recovery behavior.
- [ ] Record unresolved assessment/certification questions and feed required changes into domain ticket acceptance criteria.

## Acceptance criteria

- [ ] Each sensitive field has an owner, trust boundary, processing purpose and retention/deletion requirement.
- [ ] Abuse cases cover malicious aggregator clients and stale/compromised device credentials.
- [ ] The model contains no unsupported assertion that encryption alone removes PCI scope.
- [ ] Controls distinguish device identity, terminal certification, token authority and payment integrity.
- [ ] Assessment and external integration questions have evidence owners and explicit gates.

## Validation scenarios

- [ ] Tabletop cross-aggregator access, stolen SDK token, poisoned configuration and unknown upstream outcome.
- [ ] Trace synthetic SAD through databases, outbox, crash collector and backup inventory to identify prohibited persistence.
- [ ] Review the data-flow model against the chosen topology and later vendor evidence.

## Expected deliverables

- Threat model and abuse-case register
- Sensitive-data flow/retention matrix
- Assessment question and control register

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
