---
id: "CTX-034"
title: "Namespace Redis queues and object storage by trusted ownership"
status: "TODO"
phase: 2
priority: "P0"
size: "M"
repository: "platform"
component: "distributed-storage-isolation"
depends_on: ["CTX-019", "CTX-028", "CTX-029"]
requires_one_of: []
conflict_domains: ["storage:object-prefixes", "storage:redis-namespaces", "workflow:queue-routing"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-034: Namespace Redis queues and object storage by trusted ownership

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Hyperswitch Tenant already defines an infrastructure Redis prefix, but aggregators share that infrastructure tenant in the proposed model. Add environment, cell and aggregator ownership to platform cache keys, queues, object references and deduplication scopes. Merchant-specific data needs the additional merchant dimension where appropriate. Derive namespaces only from trusted request/job context; caller-selected paths and native tenant headers cannot bypass isolation. Cover negative caches, role caches, configuration entries, SDK replay records, secure document references and exported report objects. Namespace isolation complements authorization and does not make bucket URLs or queue messages safe by themselves. Migration must prevent old unscoped cache entries from being consumed as authoritative state or exposing another customer's data.

## Prerequisites and dependency outputs

- [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) - consume its completed, reviewed deliverables: Create canonical platform and aggregator identifiers and native mappings.
- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.


## Relevant code and ownership

Primary repository/workstream: **platform / distributed-storage-isolation**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/hyperswitch_interfaces/src/configs.rs](../crates/hyperswitch_interfaces/src/configs.rs)

- [crates/storage_impl/src/redis/cache.rs](../crates/storage_impl/src/redis/cache.rs)

- [crates/router/src/services/authorization.rs](../crates/router/src/services/authorization.rs)

- `Proposed: platform/storage/namespaces/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `storage:object-prefixes`
- `storage:redis-namespaces`
- `workflow:queue-routing`

## Implementation plan

- [ ] Define canonical namespace builders and resource-specific ownership dimensions.
- [ ] Inventory existing cache/queue/object usage touched by the platform slice.
- [ ] Implement trusted-context key construction and opaque object reference resolution.
- [ ] Migrate or invalidate legacy entries with a versioned prefix rollout.
- [ ] Require authorization for cache hits, queue consumption and presigned object URLs.

## Acceptance criteria

- [ ] Equivalent business IDs in two aggregators never collide in cache or object paths.
- [ ] No public API accepts arbitrary Redis keys, bucket paths or queue names.
- [ ] Cache hits apply the same authorization as database reads.
- [ ] Legacy unscoped entries cannot satisfy new tenant-scoped reads.
- [ ] Object download/upload authority is bounded to owner, operation and expiry.

## Validation scenarios

- [ ] Populate identical resource IDs for two aggregators and compare lookups.
- [ ] Replay another aggregator object reference and reject it.
- [ ] Roll out a namespace version change with old entries present.

## Expected deliverables

- Namespace library and resource inventory.
- Cache invalidation/rollout procedure and isolation tests.

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
