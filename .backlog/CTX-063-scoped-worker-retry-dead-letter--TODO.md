---
id: "CTX-063"
title: "Authorize background jobs and constrain retry and replay behavior"
status: "TODO"
phase: 2
priority: "P0"
size: "L"
repository: "platform"
component: "worker-safety"
depends_on: ["CTX-028", "CTX-029", "CTX-034", "CTX-038", "CTX-044", "CTX-053"]
requires_one_of: []
conflict_domains: ["workflow:dead-letter", "workflow:worker-ownership"]
external_inputs: []
external_inputs_resolved: true
applicability: "required"
applicability_decision: "selected"
requires_decisions: []
conditional_dependencies: []
source_baseline: "c5ecb434b419d2c473cf2882a3866de9146abdec"
---

# CTX-063: Authorize background jobs and constrain retry and replay behavior

Read this ticket with the [architecture baseline](context/architecture.md), [shared contracts](context/contracts.md), [repository map](context/repository-map.md) and [execution runbook](RUNBOOK.md). This is planned work; no implementation is claimed.

## Context and intended outcome

Background workers must carry the same trusted environment and aggregator ownership as synchronous APIs, but they also need service authority to continue approved workflows after the initiating user session expires. Define which actions revalidate current permissions, which use an already-authorized durable command, and how merchant suspension affects execution. Existing scheduler modules are integration points rather than proof that new jobs are scoped. Retries, dead-letter inspection and operator replay must preserve original operation identity and cannot bypass payment recovery rules. A queue message is untrusted until its envelope and referenced record are validated. Keep financial dispatch retries separate from safe provisioning, notification and inquiry retries, with bounded backoff and fair per-aggregator consumption.

## Prerequisites and dependency outputs

- [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) - consume its completed, reviewed deliverables: Deliver domain events through transactional outbox and deduplicated inbox.
- [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) - consume its completed, reviewed deliverables: Resolve trusted aggregator merchant and environment context.
- [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) - consume its completed, reviewed deliverables: Namespace Redis queues and object storage by trusted ownership.
- [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) - consume its completed, reviewed deliverables: Enforce permissions ownership and bounded role delegation.
- [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) - consume its completed, reviewed deliverables: Authenticate internal services and constrain delegated context.
- [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) - consume its completed, reviewed deliverables: Claim payment attempts conditionally and recover dispatch ambiguity.


## Relevant code and ownership

Primary repository/workstream: **platform / worker-safety**. Verify the selected feature baseline before editing. Listed existing paths are inspection starting points; proposed paths need agreement with CTX-005/006.

- [crates/scheduler/src/consumer.rs](../crates/scheduler/src/consumer.rs)

- [crates/scheduler/src/consumer/workflows.rs](../crates/scheduler/src/consumer/workflows.rs)

- [crates/scheduler/src/db/process_tracker.rs](../crates/scheduler/src/db/process_tracker.rs)

- `Proposed: platform/jobs/`


Coordinate these advisory exclusive write domains before changing shared code or generated artifacts:

- `workflow:dead-letter`
- `workflow:worker-ownership`

## Implementation plan

- [ ] Define typed job envelope and authority/ownership validation at consumption.
- [ ] Implement job-specific retry classifications and durable claim/version handling.
- [ ] Revalidate current lifecycle for actions that create new financial activity.
- [ ] Add scoped dead-letter inspection, replay authorization and safe diagnostic records.
- [ ] Integrate scheduler adapters with per-aggregator concurrency and expiry limits.
- [ ] Define RLS-compatible job/outbox discovery: poll known aggregator scopes or use a narrowly granted metadata-only discovery interface, then enter the authenticated aggregator transaction before reading tenant payloads; do not grant general workers BYPASSRLS.

## Acceptance criteria

- [ ] Worker cannot access another aggregator by altering a message field.
- [ ] Financial dispatch is never retried through generic exception backoff.
- [ ] Replay preserves original operation and event identity.
- [ ] Expired/revoked commands follow documented policy rather than silently running.
- [ ] Dead-letter payloads contain no raw payment data or credentials.
- [ ] Workers can discover eligible work without blanket tenant-data access; a forged discovery result cannot open another aggregator payload outside a scoped transaction.

## Validation scenarios

- [ ] Inject forged ownership and stale lifecycle versions into queued jobs.
- [ ] Crash/replay one job repeatedly and inspect idempotent effects.
- [ ] Attempt foreign-aggregator dead-letter inspection and replay.

## Expected deliverables

- Scoped worker library and retry policy matrix.
- Dead-letter/replay APIs and adversarial job tests.

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
