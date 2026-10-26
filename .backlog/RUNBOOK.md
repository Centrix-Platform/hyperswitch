# CTX backlog execution runbook

This folder is a planning artifact for future coordinated execution. Creating it did not implement the architecture, complete a ticket, provision external infrastructure or authorize live charges/deployments/messages. Every initial ticket is `TODO`.

## Start here

1. Read [README.md](README.md), [context/architecture.md](context/architecture.md), [context/contracts.md](context/contracts.md) and [context/repository-map.md](context/repository-map.md).
2. Run `python3 .backlog/tools/check_backlog.py` from the repository root.
3. Review the dependency frontier using `python3 .backlog/tools/check_backlog.py --ready`.
4. Assign one bounded ticket to an agent with its repository/branch/worktree, dependencies, conflict domains and missing external inputs.
5. Require dependency output evidence and resolved external inputs before dependent implementation. An earlier ticket number or a finished draft is not evidence of a completed prerequisite.

## Ticket format

Each task is `.backlog/CTX-XXX-lowercase-task-slug--TODO.md`. IDs are stable. The double hyphen before `TODO` is intentional. Frontmatter carries identity, phase, priority, size, repository, component, dependencies, conflict domains, external-input requirement and applicability.

Keep filenames stable while executing unless the coordinator deliberately manages a rename and updates all links/index entries. Frontmatter is the execution status authority; the initial `--TODO` suffix records the requested initial ticket naming. Use `TODO`, `IN_PROGRESS`, `BLOCKED`, `DONE` or `SKIPPED` in frontmatter, with an explanation/evidence for BLOCKED or SKIPPED. Do not mark a ticket done because another ticket contains a related implementation.

Priority means sequencing/importance, not permission to bypass a dependency. Size is a relative planning bucket, not a calendar estimate. Phase groups the original four milestones; dependencies can cross phase boundaries. Applicability decisions must be explicit, especially account topology, optional SDK presentation/JWE and later ledger/Kotlin programs.

## Selecting parallel work

- A task is dependency-ready only when every required dependency is `DONE`. If a dependency is intentionally `SKIPPED`, the coordinator must first remove/replace its edge with documented equivalent evidence; skipping is not completion.
- The validator distinguishes a dependency frontier from external-input readiness. It does not infer that credentials, contracts, certification or business decisions exist.
- Use `conflict_domains` as advisory exclusive write leases. Matching domains require coordination even if dependency graphs permit parallel work.
- Distinct domains do not prove file-disjointness. Check actual file ownership before starting an agent.
- Serialize schema migration allocation, root contract edits, auth/pool boundaries, shared manifest changes and release/signing configuration.
- Agents may analyze the same source concurrently. They should not mutate the same shared checkout or generated contract without a coordinator-owned integration plan.
- Prefer one isolated worktree/branch per implementation task. Cross-repository tickets need an explicit integration owner and pinned contract order.
- Shared contracts are merged before clients implement against them. Use consumer fixtures and compatible stubs rather than independently inventing temporary DTOs.

Never start all 143 tickets indiscriminately. The coordinator selects a small frontier, resolves inputs, grants file/domain ownership, integrates evidence and recalculates readiness.

## Selected integration and conditional dependencies

`requires_one_of` groups do not require every alternative. For the physical/smart adapter group, only the exact CTX-013-selected adapter in [decisions.json](decisions.json) can satisfy readiness. Completing the unselected adapter does not qualify the chosen terminal/application/acquirer combination. Both adapter tickets remain available as implementation/expansion work.

CTX-002 owns the native topology decision. CTX-013 owns the first adapter, authorization owner and supplementary-JWE requirement. Resolve each registry entry with its allowed value and evidence before marking the owner DONE. The validator blocks affected assignments while a relevant decision remains pending.

If `application_layer_jwe` is true, CTX-088 becomes a prerequisite of the applicable security/certification gates. If `authorization_owner` is `vendor`, CTX-141 becomes a prerequisite of the selected smart-terminal/result-ingestion and qualification gates. These conditional edges are machine-readable and included in cycle validation even when inactive. Update the chosen ticket's applicability decision and verified external inputs before assignment.

CTX-094 is a required branding/resource-isolation and presentation-decision task. A documented, verified headless-only delivery can complete it; building a new optional UI module is not mandatory. The headless Kotlin/Java facade must work without optional presentation runtime dependencies.

The registry is planning and evidence metadata, not runtime authorization or routing configuration. Implemented services use their approved, versioned domain configuration and identity contracts. A backlog edit must never directly activate processing or change a live payment route.

## Execution contract for an assigned agent

Read the ticket context and prerequisite deliverables. Verify the actual repository SHA, feature baseline and applicable local instructions. Native touchpoints are inspection locations; `Proposed:` paths need architectural agreement. External repositories must be obtained and pinned deliberately.

Implement only the assigned scope. Preserve unrelated user edits. Maintain the ownership, security, payment-safety and compatibility invariants in the shared context. If the ticket is too broad for one reviewable change, propose child tickets under new IDs and preserve a clear completion gate; do not silently drop acceptance criteria.

Run the ticket's meaningful validation scenarios. For Rust, use the selected compatible feature recipe and crate-scoped checks; the core's v1/v2 features are mutually exclusive. For migrations, verify new/upgrade/backfill/rollback-or-forward-recovery behavior. For SDK and terminal work, mock evidence supplements rather than substitutes for applicable hardware/vendor/acquirer acceptance.

Record exact commands/results, configuration and evidence pointers. Do not paste secrets, payment payloads, SAD, customer documents or credentials into tickets, test outputs or review comments. Synthetic markers are sufficient for leakage tests.

## Handoff and completion evidence

Update the ticket's final handoff section with:

- Source commits/PRs and repositories changed.
- Final contract/schema/configuration versions and actual implementation paths.
- Acceptance criteria satisfied, with concise evidence links.
- Commands/scenarios run, outcomes and any important environment limitations.
- Migration/rollout/backout or forward-recovery considerations.
- External approvals/certification evidence where required, without assuming completion.
- Remaining risks, resolved decisions, follow-up IDs and downstream consumer guidance.

Update status, then regenerate the manifest/index using `python3 .backlog/tools/check_backlog.py --refresh-index` and run validation again. Coordinate shared README/manifest edits to avoid concurrent overwrites.

`DONE` means the ticket deliverables exist, its meaningful checks pass and necessary review/evidence is present. Documentary ADR tickets can be done when their explicit decision/output acceptance is satisfied; they do not imply related code is implemented. A conditional ticket may be `SKIPPED` only after its decision and downstream implications are recorded.

## External and high-impact gates

Vendor/acquirer protocols, terminal trust roots, signing identities, sandbox credentials, MID/TID allocations and certification acceptance are real inputs. Do not manufacture these fields or certify a mock. Record a blocking input and continue independent work when possible.

The platform does not assume that encryption removes PCI scope. Qualified reviewers and the selected vendor/acquirer own final applicable assessment/certification evidence. Legal/commercial responsibilities need accountable professional review rather than agent-invented requirements.

Building local code, fixtures and reviewable release artifacts is distinct from deploying a live system, moving funds, onboarding a real regulated customer, changing production custody or messaging third parties. Obtain the action-specific authorization before those steps when it has not already been given.

CTX-135 prepares a release candidate. CTX-136 runs a limited pilot only after its pilot-specific authorization and controls; CTX-137 uses pilot evidence to gate broader launch. Do not create a circular requirement that broader launch approval is required merely to produce the restricted pilot evidence.

CTX-139 (Kotlin replacement) and CTX-140 (balances/ledger/payouts) are conditional evolution tracks. They are not default launch blockers. A future program must preserve one financial writer and must not duplicate live authorizations for comparison.
