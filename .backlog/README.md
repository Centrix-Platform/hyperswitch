# CTX implementation backlog

143 individually scoped tickets translating the white-label B2B2B payment-platform blueprint into executable work.

Start with [RUNBOOK.md](RUNBOOK.md), the [architecture context](context/architecture.md), [shared contracts](context/contracts.md) and [repository map](context/repository-map.md). The complete source export has a [portable text snapshot](context/source-blueprint.txt).

Use [TRACEABILITY.md](TRACEABILITY.md) to locate requirements and [EXECUTION-PLAN.md](EXECUTION-PLAN.md) for dependency bands and coordination rules. [manifest.json](manifest.json) is the generated scheduling index; ticket frontmatter is authoritative.

```sh
python3 .backlog/tools/check_backlog.py
python3 .backlog/tools/check_backlog.py --ready
python3 .backlog/tools/check_backlog.py --refresh-index
```

All initial task filenames use `CTX-XXX-task-name--TODO.md`. Initial status is `TODO`; no architecture implementation is claimed by this planning artifact. Keep filenames stable and use frontmatter for execution status. External inputs, applicability decisions and conflict domains are separate from dependency readiness.

Sizes are relative planning buckets, not dates. P0/P1/P2 indicate importance and sequencing. Phase is a roadmap grouping; it does not override prerequisite edges. CTX-139/140 are deferred conditional evolution, not default launch gates. CTX-085/086 represent integration-dependent adapter paths; downstream one-of groups require the CTX-013-selected path.

## Coverage by phase

| Phase | Tickets | Scope |
|---|---:|---|
| 1 | 18 (CTX-001 to CTX-018) | Environment and Fork Isolation |
| 2 | 57 (CTX-019 to CTX-074; CTX-142) | Database, Tenancy and Payment Foundations |
| 3 | 34 (CTX-075 to CTX-107; CTX-141) | Terminal and SDK Customization |
| 4 | 34 (CTX-108 to CTX-140; CTX-143) | Aggregator Console, API Exposure and Production Gates |

## Current state

**TODO: 143**.

The validator checks filenames, unique IDs, metadata, concrete sections, links, missing dependencies, cycles and generated-index consistency. It does not certify code, mark external inputs resolved or approve production actions.

## Phase 1: Environment and Fork Isolation

| Ticket | Work item | Priority / size | Repository | Prerequisites |
|---|---|---|---|---|
| [CTX-001](CTX-001-define-platform-charter-and-funds-flow--TODO.md) | Define the platform charter, pilot scope and funds flow | P0 / M | platform | None |
| [CTX-002](CTX-002-decide-domain-topology-and-public-terminology--TODO.md) | Decide the native account topology and public domain terminology | P0 / M | platform | CTX-001, CTX-003 |
| [CTX-003](CTX-003-inventory-repositories-versions-and-feature-baseline--TODO.md) | Inventory repositories, pinned versions and mutually compatible features | P0 / M | multi-repo | None |
| [CTX-004](CTX-004-establish-fork-provenance-and-upstream-sync--TODO.md) | Establish controlled forks, provenance and upstream maintenance | P0 / M | multi-repo | CTX-003 |
| [CTX-005](CTX-005-define-service-boundaries-and-migration-ports--TODO.md) | Define service ownership, execution ports and the Kotlin migration boundary | P0 / M | platform | CTX-001, CTX-002, CTX-003 |
| [CTX-006](CTX-006-define-api-event-and-error-contract-standards--TODO.md) | Define API, event, monetary and error contract standards | P0 / M | platform | CTX-001, CTX-003 |
| [CTX-007](CTX-007-establish-reproducible-local-development-stack--TODO.md) | Establish a reproducible, isolated local development stack | P0 / M | core | CTX-003 |
| [CTX-008](CTX-008-define-environment-cells-and-home-region-strategy--TODO.md) | Define sandbox/live cells, data residency and home-region ownership | P0 / M | platform | CTX-001, CTX-002, CTX-003 |
| [CTX-009](CTX-009-bootstrap-secret-custody-kms-and-hsm-boundaries--TODO.md) | Bootstrap secret custody, service credentials and cryptographic boundaries | P0 / M | infra | CTX-001, CTX-008, CTX-014 |
| [CTX-010](CTX-010-establish-ci-quality-and-contract-checks--TODO.md) | Establish CI quality, migration and contract check lanes | P0 / M | multi-repo | CTX-003, CTX-006, CTX-007 |
| [CTX-011](CTX-011-establish-sbom-signing-and-license-provenance--TODO.md) | Establish SBOM, artifact signing and license provenance | P0 / M | multi-repo | CTX-003, CTX-004, CTX-010 |
| [CTX-012](CTX-012-define-safe-observability-and-trace-identities--TODO.md) | Define safe observability, trace IDs and redaction defaults | P0 / M | multi-repo | CTX-001, CTX-006, CTX-014 |
| [CTX-013](CTX-013-discover-terminal-acquirer-certification-requirements--TODO.md) | Discover the first terminal/acquirer integration and certification requirements | P0 / M | multi-repo | CTX-001, CTX-003 |
| [CTX-014](CTX-014-model-payment-trust-boundaries-and-pci-data-flow--TODO.md) | Model trust boundaries, abuse cases and PCI payment-data flows | P0 / M | platform | CTX-001, CTX-002, CTX-003 |
| [CTX-015](CTX-015-provision-baseline-postgres-redis-and-pooling-infrastructure--TODO.md) | Provision baseline PostgreSQL, Redis, pooling and backup infrastructure | P0 / M | infra | CTX-007, CTX-008, CTX-009 |
| [CTX-016](CTX-016-secure-ingress-and-isolate-native-admin-apis--TODO.md) | Secure ingress and isolate native admin and trusted-header paths | P0 / M | multi-repo | CTX-005, CTX-008, CTX-009, CTX-014 |
| [CTX-017](CTX-017-build-synthetic-fixtures-and-acquirer-fault-harness--TODO.md) | Build synthetic tenant fixtures and an acquirer fault-injection harness | P0 / M | multi-repo | CTX-006, CTX-007, CTX-014 |
| [CTX-018](CTX-018-capture-native-payment-and-api-compatibility-baseline--TODO.md) | Capture the native payment and API compatibility baseline | P0 / M | core | CTX-003, CTX-007, CTX-017 |

## Phase 2: Database, Tenancy and Payment Foundations

| Ticket | Work item | Priority / size | Repository | Prerequisites |
|---|---|---|---|---|
| [CTX-019](CTX-019-canonical-platform-aggregator-identity--TODO.md) | Create canonical platform and aggregator identifiers and native mappings | P0 / M | platform | CTX-002, CTX-005, CTX-006, CTX-008, CTX-015 |
| [CTX-020](CTX-020-aggregator-provisioning-lifecycle--TODO.md) | Provision aggregators through a resumable native-account workflow | P0 / L | platform | CTX-009, CTX-016, CTX-018, CTX-019 |
| [CTX-021](CTX-021-canonical-merchant-legal-lifecycle--TODO.md) | Model legal merchants and their onboarding lifecycle independently of profiles | P0 / M | platform | CTX-001, CTX-002, CTX-019 |
| [CTX-022](CTX-022-membership-role-grant-schema--TODO.md) | Model aggregator memberships roles and merchant-scoped grants | P0 / M | platform | CTX-006, CTX-019 |
| [CTX-023](CTX-023-acquirer-account-credential-reference-schema--TODO.md) | Model aggregator acquirer accounts using versioned secret references | P0 / M | platform | CTX-009, CTX-013, CTX-014, CTX-019 |
| [CTX-024](CTX-024-native-profile-mca-provisioning-saga--TODO.md) | Project canonical merchants and accounts into native profiles and MCAs | P0 / L | platform | CTX-020, CTX-021, CTX-023, CTX-043 |
| [CTX-025](CTX-025-certification-bundle-version-registry--TODO.md) | Track approved terminal and acquirer integration combinations | P0 / M | platform | CTX-013, CTX-019, CTX-023 |
| [CTX-026](CTX-026-terminal-deployment-binding-schema--TODO.md) | Model device deployments and merchant-specific processing bindings | P0 / M | platform | CTX-021, CTX-023, CTX-025 |
| [CTX-027](CTX-027-durable-payment-operation-attempt-schema--TODO.md) | Persist authoritative payment admission and attempt ownership | P0 / L | platform | CTX-006, CTX-015, CTX-019, CTX-021 |
| [CTX-028](CTX-028-transactional-outbox-inbox-envelopes--TODO.md) | Deliver domain events through transactional outbox and deduplicated inbox | P0 / L | platform | CTX-006, CTX-019, CTX-027 |
| [CTX-029](CTX-029-authenticated-request-context-resolver--TODO.md) | Resolve trusted aggregator merchant and environment context | P0 / M | platform | CTX-016, CTX-019, CTX-022 |
| [CTX-030](CTX-030-transaction-local-scoped-repositories--TODO.md) | Enforce transaction-local tenancy in scoped storage and pool APIs | P0 / L | core | CTX-015, CTX-019, CTX-029 |
| [CTX-031](CTX-031-canonical-row-security-ownership--TODO.md) | Protect canonical tables with RLS and composite ownership constraints | P0 / L | platform | CTX-019, CTX-021, CTX-022, CTX-023, CTX-025, CTX-026, CTX-027, CTX-028, CTX-030 |
| [CTX-032](CTX-032-native-hyperswitch-isolation-retrofit--TODO.md) | Audit and enforce isolation across native payment and account storage | P0 / L | core | CTX-018, CTX-030, CTX-031 |
| [CTX-033](CTX-033-submerchant-customer-vault-ownership--TODO.md) | Isolate submerchant customer vault and mandate access or reject those features [topology-dependent] | P0 / L | core | CTX-002, CTX-021, CTX-032 |
| [CTX-034](CTX-034-scoped-cache-queue-object-namespaces--TODO.md) | Namespace Redis queues and object storage by trusted ownership | P0 / M | platform | CTX-019, CTX-028, CTX-029 |
| [CTX-035](CTX-035-analytics-search-report-isolation--TODO.md) | Enforce aggregator and merchant scope in analytics and reporting | P0 / L | core | CTX-029, CTX-032, CTX-034 |
| [CTX-036](CTX-036-expand-backfill-validate-contract-rollout--TODO.md) | Stage canonical and native tenancy migrations safely | P0 / L | platform | CTX-019, CTX-021, CTX-026, CTX-027, CTX-031, CTX-032 |
| [CTX-037](CTX-037-oidc-portal-bff-session-authentication--TODO.md) | Implement OIDC portal sessions and explicit aggregator context switching | P0 / L | platform | CTX-016, CTX-022, CTX-029 |
| [CTX-038](CTX-038-rbac-ownership-invitation-authorization--TODO.md) | Enforce permissions ownership and bounded role delegation | P0 / L | platform | CTX-022, CTX-029 |
| [CTX-039](CTX-039-platform-operator-break-glass-authority--TODO.md) | Separate platform operator access and audited emergency authority | P0 / M | platform | CTX-014, CTX-022, CTX-029, CTX-037, CTX-038 |
| [CTX-040](CTX-040-scoped-operational-key-lifecycle--TODO.md) | Issue rotate and revoke aggregator operational API keys | P0 / M | platform | CTX-009, CTX-019, CTX-022, CTX-029, CTX-038 |
| [CTX-041](CTX-041-constrained-device-bound-sdk-sessions--TODO.md) | Mint short-lived merchant terminal and payment-scoped SDK sessions | P0 / M | platform | CTX-009, CTX-021, CTX-026, CTX-029, CTX-038, CTX-040 |
| [CTX-042](CTX-042-sdk-proof-integrity-replay-validation--TODO.md) | Validate device proof transaction integrity and replay limits | P0 / L | platform | CTX-014, CTX-029, CTX-034, CTX-041 |
| [CTX-043](CTX-043-credential-version-crypto-boundary--TODO.md) | Enforce secret retrieval rotation and cryptographic service boundaries | P0 / L | platform | CTX-009, CTX-014, CTX-023 |
| [CTX-044](CTX-044-service-identity-audience-authorization--TODO.md) | Authenticate internal services and constrain delegated context | P0 / M | platform | CTX-005, CTX-009, CTX-016, CTX-029, CTX-038 |
| [CTX-045](CTX-045-asynchronous-merchant-onboarding-api--TODO.md) | Expose idempotent aggregator merchant onboarding and operation status | P0 / L | platform | CTX-006, CTX-021, CTX-024, CTX-028, CTX-029, CTX-038, CTX-040, CTX-046 |
| [CTX-046](CTX-046-secure-kyb-document-reference-service--TODO.md) | Secure onboarding document uploads and sensitive merchant evidence | P0 / M | platform | CTX-014, CTX-021, CTX-029, CTX-034, CTX-038 |
| [CTX-047](CTX-047-merchant-lifecycle-revocation-propagation--TODO.md) | Propagate merchant activation suspension and terminal revocation safely | P0 / L | platform | CTX-021, CTX-024, CTX-028, CTX-038, CTX-041 |
| [CTX-048](CTX-048-acquirer-merchant-enrollment-adapter--TODO.md) | Integrate acquirer merchant enrollment and explicit approval evidence | P0 / L | platform | CTX-013, CTX-021, CTX-023, CTX-025, CTX-028, CTX-044, CTX-045 |
| [CTX-049](CTX-049-language-neutral-payment-execution-port--TODO.md) | Define payment execution port and implement the Rust compatibility adapter | P0 / L | core | CTX-005, CTX-006, CTX-018, CTX-027, CTX-029, CTX-044 |
| [CTX-050](CTX-050-typed-terminal-payment-monetary-contract--TODO.md) | Define typed terminal payload and monetary validation contracts | P0 / L | platform | CTX-006, CTX-014, CTX-025, CTX-026, CTX-049 |
| [CTX-051](CTX-051-durable-idempotent-payment-admission--TODO.md) | Reserve charges durably and replay equivalent operations safely | P0 / L | platform | CTX-027, CTX-029, CTX-038, CTX-042, CTX-049, CTX-050 |
| [CTX-052](CTX-052-redis-owner-safe-payment-coordination--TODO.md) | Implement short owner-safe Redis leases for payment coordination | P0 / M | core | CTX-027, CTX-034, CTX-051 |
| [CTX-053](CTX-053-conditional-dispatch-crash-recovery--TODO.md) | Claim payment attempts conditionally and recover dispatch ambiguity | P0 / L | platform | CTX-027, CTX-028, CTX-049, CTX-051, CTX-052 |
| [CTX-054](CTX-054-terminal-binding-certification-eligibility--TODO.md) | Evaluate active terminal binding and certification before routing | P0 / L | platform | CTX-025, CTX-026, CTX-029, CTX-047, CTX-050 |
| [CTX-055](CTX-055-frozen-routing-configuration-snapshot--TODO.md) | Freeze eligible route and versioned processing configuration per attempt | P0 / L | core | CTX-023, CTX-024, CTX-043, CTX-049, CTX-053, CTX-054 |
| [CTX-056](CTX-056-acquirer-reference-duplicate-semantics--TODO.md) | Implement documented downstream reference and duplicate-handling rules | P0 / L | platform | CTX-013, CTX-049, CTX-050, CTX-055 |
| [CTX-057](CTX-057-unknown-outcome-inquiry-recovery--TODO.md) | Resolve uncertain outcomes through inquiry and reconciliation | P0 / L | platform | CTX-028, CTX-053, CTX-055, CTX-056 |
| [CTX-058](CTX-058-authenticated-acquirer-notification-inbox--TODO.md) | Authenticate and deduplicate inbound acquirer notifications | P0 / L | core | CTX-028, CTX-044, CTX-055, CTX-056, CTX-057 |
| [CTX-059](CTX-059-signed-aggregator-webhook-delivery--TODO.md) | Deliver signed versioned aggregator webhooks with safe retries | P0 / L | platform | CTX-028, CTX-034, CTX-038, CTX-043, CTX-057 |
| [CTX-060](CTX-060-capture-concurrent-amount-authority--TODO.md) | Enforce capture limits and concurrent partial-capture safety | P0 / L | platform | CTX-027, CTX-049, CTX-053, CTX-055, CTX-056 |
| [CTX-061](CTX-061-refund-void-reversal-original-route--TODO.md) | Implement bounded refunds voids and reversals on the original route | P0 / L | platform | CTX-027, CTX-049, CTX-053, CTX-055, CTX-056, CTX-060 |
| [CTX-062](CTX-062-terminal-completion-script-coordination--TODO.md) | Coordinate terminal completion issuer scripts and required reversals | P0 / L | platform | CTX-013, CTX-049, CTX-050, CTX-055, CTX-057, CTX-061 |
| [CTX-063](CTX-063-scoped-worker-retry-dead-letter--TODO.md) | Authorize background jobs and constrain retry and replay behavior | P0 / L | platform | CTX-028, CTX-029, CTX-034, CTX-038, CTX-044, CTX-053 |
| [CTX-064](CTX-064-immutable-financial-transaction-journal--TODO.md) | Record immutable payment lifecycle and reconciliation evidence | P0 / M | platform | CTX-027, CTX-028, CTX-049, CTX-057, CTX-060, CTX-061 |
| [CTX-065](CTX-065-direct-settlement-reconciliation--TODO.md) | Import acquirer settlement evidence and reconcile transaction outcomes | P0 / L | platform | CTX-013, CTX-028, CTX-056, CTX-057, CTX-064 |
| [CTX-066](CTX-066-aggregator-quotas-bulkheads-backpressure--TODO.md) | Isolate aggregator capacity with quotas and fair work scheduling | P0 / L | platform | CTX-019, CTX-029, CTX-034, CTX-052, CTX-063 |
| [CTX-067](CTX-067-home-region-single-writer-failover--TODO.md) | Enforce home-region authority and controlled writer failover | P0 / L | platform | CTX-008, CTX-015, CTX-019, CTX-027, CTX-044, CTX-053, CTX-057 |
| [CTX-068](CTX-068-versioned-configuration-publication--TODO.md) | Publish approved processing configuration and invalidate stale views | P0 / L | platform | CTX-023, CTX-024, CTX-025, CTX-026, CTX-028, CTX-043, CTX-047, CTX-054, CTX-055 |
| [CTX-069](CTX-069-scoped-payment-read-search-export--TODO.md) | Expose authorized payment status search and export APIs | P0 / L | platform | CTX-029, CTX-032, CTX-035, CTX-038, CTX-049, CTX-057, CTX-064 |
| [CTX-070](CTX-070-safe-attribution-tracing-audit-events--TODO.md) | Instrument payment attribution and privileged actions without sensitive leakage | P0 / M | platform | CTX-012, CTX-014, CTX-019, CTX-027, CTX-028, CTX-029, CTX-049, CTX-064 |
| [CTX-071](CTX-071-cross-aggregator-isolation-release-gate--TODO.md) | Gate releases on adversarial ownership and privilege isolation | P0 / L | platform | CTX-031, CTX-032, CTX-033, CTX-034, CTX-035, CTX-038, CTX-040, CTX-041, CTX-046, CTX-063, CTX-069 |
| [CTX-072](CTX-072-payment-crash-concurrency-safety-gate--TODO.md) | Gate releases on payment concurrency crash and failover invariants | P0 / L | platform | CTX-017, CTX-051, CTX-052, CTX-053, CTX-055, CTX-056, CTX-057, CTX-058, CTX-060, CTX-061, CTX-062, CTX-066, CTX-067 |
| [CTX-073](CTX-073-api-event-contract-compatibility-gate--TODO.md) | Validate public internal and event contracts across implementations | P0 / L | platform | CTX-006, CTX-028, CTX-041, CTX-042, CTX-045, CTX-049, CTX-050, CTX-059, CTX-068, CTX-069 |
| [CTX-074](CTX-074-tenancy-migration-recovery-rehearsal--TODO.md) | Rehearse tenancy migration rollback and financial recovery | P0 / L | platform | CTX-015, CTX-018, CTX-036, CTX-057, CTX-064, CTX-065, CTX-067, CTX-071, CTX-072, CTX-073 |
| [CTX-142](CTX-142-first-acquirer-dispute-chargeback-domain--TODO.md) | Implement scoped first-acquirer dispute lifecycle evidence and notifications | P0 / L | platform | CTX-013, CTX-028, CTX-031, CTX-032, CTX-038, CTX-043, CTX-046, CTX-058, CTX-059, CTX-064, CTX-065, CTX-069 |

## Phase 3: Terminal and SDK Customization

| Ticket | Work item | Priority / size | Repository | Prerequisites |
|---|---|---|---|---|
| [CTX-075](CTX-075-fork-android-client-sdk-coordinates-and-release-inputs--TODO.md) | Fork Android and shared client SDK identities and release inputs | P0 / L | multi-repo | CTX-003, CTX-004, CTX-010, CTX-011, CTX-012, CTX-018 |
| [CTX-076](CTX-076-define-versioned-terminal-and-sdk-configuration-contracts--TODO.md) | Define versioned terminal and SDK configuration contracts | P0 / M | multi-repo | CTX-006, CTX-025, CTX-026, CTX-041, CTX-050, CTX-075 |
| [CTX-077](CTX-077-introduce-vendor-neutral-terminal-adapter-api--TODO.md) | Introduce a vendor-neutral terminal adapter API | P0 / L | android | CTX-013, CTX-050, CTX-062, CTX-075, CTX-076 |
| [CTX-078](CTX-078-implement-terminal-inventory-claim-and-activation-api--TODO.md) | Implement terminal inventory, claim, and activation APIs | P0 / L | platform | CTX-026, CTX-029, CTX-031, CTX-038, CTX-047, CTX-076 |
| [CTX-079](CTX-079-enroll-device-keys-and-verify-attestation-and-app-identity--TODO.md) | Enroll device keys and verify attestation and application identity | P0 / L | multi-repo | CTX-009, CTX-014, CTX-025, CTX-026, CTX-041, CTX-042, CTX-075, CTX-076, CTX-078 |
| [CTX-080](CTX-080-enforce-terminal-software-and-certification-admission-policy--TODO.md) | Enforce firmware, kernel, application, and certification admission policy | P0 / L | platform | CTX-013, CTX-014, CTX-025, CTX-026, CTX-043, CTX-078, CTX-079 |
| [CTX-081](CTX-081-bind-merchant-terminals-to-approved-acquirer-mid-tid-configurations--TODO.md) | Bind merchant terminals to approved acquirer MID/TID configurations | P0 / L | platform | CTX-023, CTX-024, CTX-025, CTX-026, CTX-047, CTX-054, CTX-055, CTX-076, CTX-078, CTX-080 |
| [CTX-082](CTX-082-publish-signed-versioned-sdk-configuration-manifests--TODO.md) | Publish signed versioned SDK configuration manifests | P0 / L | multi-repo | CTX-009, CTX-043, CTX-068, CTX-076, CTX-079, CTX-080, CTX-081 |
| [CTX-083](CTX-083-implement-aggregator-backend-sdk-session-bootstrap--TODO.md) | Implement aggregator backend SDK-session bootstrap | P0 / M | multi-repo | CTX-040, CTX-041, CTX-042, CTX-047, CTX-076, CTX-078, CTX-079, CTX-081, CTX-082 |
| [CTX-084](CTX-084-secure-sdk-http-transport-and-request-integrity--TODO.md) | Secure SDK HTTP transport, sender-constrained auth, and request integrity | P0 / L | multi-repo | CTX-006, CTX-016, CTX-042, CTX-070, CTX-076, CTX-079, CTX-082, CTX-083 |
| [CTX-085](CTX-085-integrate-first-certified-physical-terminal-vendor-adapter--TODO.md) | Integrate the first certified physical-terminal vendor adapter [integration-dependent] | P0 / L | multi-repo | CTX-013, CTX-050, CTX-062, CTX-077, CTX-079, CTX-080, CTX-081, CTX-082, CTX-084; if authorization_owner="vendor": CTX-141 |
| [CTX-086](CTX-086-integrate-first-certified-smart-terminal-payment-app--TODO.md) | Integrate the first certified smart-terminal payment application [integration-dependent] | P0 / L | multi-repo | CTX-013, CTX-050, CTX-062, CTX-077, CTX-079, CTX-080, CTX-081, CTX-082, CTX-084; if authorization_owner="vendor": CTX-141 |
| [CTX-087](CTX-087-enforce-opaque-payload-boundary-and-acquirer-crypto-adapter--TODO.md) | Enforce the opaque payment-payload boundary and acquirer crypto adapter | P0 / L | multi-repo | CTX-009, CTX-014, CTX-043, CTX-049, CTX-050, CTX-054, CTX-055, CTX-056, CTX-076, CTX-081, CTX-084; one of (CTX-085 / CTX-086); if authorization_owner="vendor": CTX-141 |
| [CTX-088](CTX-088-support-approved-application-layer-jwe-envelopes--TODO.md) | Support approved application-layer JWE envelopes where required [conditional] | P1 / L | multi-repo | CTX-009, CTX-014, CTX-043, CTX-076, CTX-082, CTX-084, CTX-087 |
| [CTX-089](CTX-089-secure-explicit-intent-binder-and-aidl-partner-communication--TODO.md) | Secure explicit intent, Binder, and AIDL partner communication | P0 / L | android | CTX-014, CTX-076, CTX-077, CTX-079, CTX-082; one of (CTX-085 / CTX-086); if authorization_owner="vendor": CTX-141 |
| [CTX-090](CTX-090-implement-sdk-payment-state-and-single-submission-orchestration--TODO.md) | Implement SDK payment-state and single-submission orchestration | P0 / L | android | CTX-051, CTX-053, CTX-057, CTX-060, CTX-061, CTX-062, CTX-076, CTX-077, CTX-083, CTX-084, CTX-087, CTX-089 |
| [CTX-091](CTX-091-integrate-terminal-completion-and-issuer-script-finalization--TODO.md) | Integrate terminal completion and issuer-script finalization | P0 / L | multi-repo | CTX-050, CTX-056, CTX-057, CTX-062, CTX-077, CTX-087, CTX-090; one of (CTX-085 / CTX-086); if authorization_owner="vendor": CTX-141 |
| [CTX-092](CTX-092-recover-sdk-operations-after-process-and-network-failure--TODO.md) | Recover SDK operations after process death and network failure | P0 / L | android | CTX-012, CTX-057, CTX-070, CTX-076, CTX-082, CTX-083, CTX-084, CTX-090, CTX-091 |
| [CTX-093](CTX-093-redact-mobile-logs-crashes-storage-and-backups--TODO.md) | Redact mobile logs, crashes, storage, and backups | P0 / M | multi-repo | CTX-012, CTX-014, CTX-070, CTX-075, CTX-076, CTX-084, CTX-087, CTX-089, CTX-092 |
| [CTX-094](CTX-094-white-label-sdk-ui-resources-localization-and-accessibility--TODO.md) | White-label optional SDK UI, resources, localization, and accessibility | P1 / M | android | CTX-006, CTX-075, CTX-076, CTX-082, CTX-090, CTX-092, CTX-093 |
| [CTX-095](CTX-095-detach-client-core-and-react-native-remote-endpoints--TODO.md) | Detach shared client-core and React Native remote endpoints | P0 / L | client-core | CTX-003, CTX-004, CTX-007, CTX-012, CTX-016, CTX-075, CTX-076, CTX-082, CTX-084, CTX-093 |
| [CTX-096](CTX-096-publish-stable-kotlin-and-java-sdk-facades--TODO.md) | Publish stable Kotlin and Java SDK compatibility facades | P0 / M | android | CTX-006, CTX-075, CTX-076, CTX-077, CTX-083, CTX-090, CTX-091, CTX-092, CTX-094 |
| [CTX-097](CTX-097-build-reference-aggregator-apk-and-secure-backend--TODO.md) | Build a reference aggregator APK and secure bootstrap backend | P1 / L | multi-repo | CTX-040, CTX-041, CTX-045, CTX-076, CTX-078, CTX-081, CTX-083, CTX-084, CTX-089, CTX-090, CTX-091, CTX-092, CTX-096 |
| [CTX-098](CTX-098-sign-and-distribute-sdk-artifacts-with-android-compatibility-ci--TODO.md) | Sign and distribute SDK artifacts with Android compatibility CI | P0 / L | multi-repo | CTX-010, CTX-011, CTX-075, CTX-076, CTX-093, CTX-095, CTX-096, CTX-097 |
| [CTX-099](CTX-099-manage-terminal-revocation-reassignment-rotation-and-decommissioning--TODO.md) | Manage terminal revocation, reassignment, rotation, and decommissioning | P0 / L | multi-repo | CTX-026, CTX-041, CTX-042, CTX-047, CTX-057, CTX-062, CTX-068, CTX-078, CTX-079, CTX-080, CTX-081, CTX-082, CTX-092 |
| [CTX-100](CTX-100-monitor-terminal-fleet-and-stage-configuration-revocation-rollouts--TODO.md) | Monitor terminal fleets and stage configuration and revocation rollouts | P1 / L | multi-repo | CTX-025, CTX-026, CTX-068, CTX-070, CTX-079, CTX-080, CTX-081, CTX-082, CTX-093, CTX-098, CTX-099 |
| [CTX-101](CTX-101-gate-mobile-release-on-adversarial-security-tests--TODO.md) | Gate mobile releases on adversarial IPC, auth, replay, and attestation tests | P0 / L | multi-repo | CTX-014, CTX-042, CTX-076, CTX-079, CTX-080, CTX-082, CTX-083, CTX-084, CTX-087, CTX-089, CTX-092, CTX-093, CTX-099; if authorization_owner="vendor": CTX-141; if application_layer_jwe=true: CTX-088 |
| [CTX-102](CTX-102-validate-sdk-crash-network-hardware-and-vendor-compatibility--TODO.md) | Validate SDK crash, network, hardware, and vendor compatibility | P0 / L | multi-repo | CTX-017, CTX-072, CTX-077, CTX-084, CTX-090, CTX-091, CTX-092, CTX-095, CTX-096, CTX-098, CTX-099; one of (CTX-085 / CTX-086) |
| [CTX-103](CTX-103-execute-terminal-app-gateway-acquirer-certification-evidence--TODO.md) | Execute exact terminal, application, gateway, and acquirer certification evidence | P0 / L | multi-repo | CTX-013, CTX-014, CTX-025, CTX-043, CTX-050, CTX-062, CTX-065, CTX-080, CTX-081, CTX-087, CTX-091, CTX-098, CTX-101, CTX-102; one of (CTX-085 / CTX-086); if authorization_owner="vendor": CTX-141; if application_layer_jwe=true: CTX-088 |
| [CTX-104](CTX-104-document-kotlin-java-ipc-status-and-recovery-integration--TODO.md) | Document Kotlin, Java, IPC, status, and recovery integration | P1 / M | multi-repo | CTX-006, CTX-076, CTX-077, CTX-083, CTX-084, CTX-089, CTX-090, CTX-091, CTX-092, CTX-095, CTX-096, CTX-097, CTX-098 |
| [CTX-105](CTX-105-build-terminal-and-acquirer-failure-simulator--TODO.md) | Build terminal and acquirer simulators with financial failure modes | P0 / L | multi-repo | CTX-017, CTX-050, CTX-051, CTX-056, CTX-057, CTX-058, CTX-062, CTX-065, CTX-076, CTX-077, CTX-090, CTX-091 |
| [CTX-106](CTX-106-preserve-immutable-terminal-configuration-and-deployment-audit-history--TODO.md) | Preserve immutable terminal, configuration, and deployment audit history | P0 / M | platform | CTX-025, CTX-026, CTX-028, CTX-055, CTX-068, CTX-070, CTX-078, CTX-079, CTX-080, CTX-081, CTX-082, CTX-099, CTX-100 |
| [CTX-107](CTX-107-prove-approved-terminal-to-acquirer-pilot-and-reconciliation-gate--TODO.md) | Prove the approved terminal-to-acquirer pilot and reconciliation gate | P0 / L | multi-repo | CTX-001, CTX-013, CTX-018, CTX-047, CTX-051, CTX-054, CTX-055, CTX-057, CTX-060, CTX-061, CTX-062, CTX-064, CTX-065, CTX-071, CTX-072, CTX-073, CTX-080, CTX-081, CTX-087, CTX-090, CTX-091, CTX-092, CTX-098, CTX-099, CTX-100, CTX-101, CTX-102, CTX-103, CTX-104, CTX-105, CTX-106; one of (CTX-085 / CTX-086); if authorization_owner="vendor": CTX-141; if application_layer_jwe=true: CTX-088 |
| [CTX-141](CTX-141-support-authenticated-vendor-executed-authorization-ownership--TODO.md) | Support authenticated vendor-executed authorization ownership where the selected integration requires it [conditional] | P0 / L | multi-repo | CTX-013, CTX-049, CTX-050, CTX-053, CTX-057, CTX-058, CTX-062, CTX-076, CTX-077, CTX-084 |

## Phase 4: Aggregator Console, API Exposure and Production Gates

| Ticket | Work item | Priority / size | Repository | Prerequisites |
|---|---|---|---|---|
| [CTX-108](CTX-108-white-label-dashboard-runtime-baseline--TODO.md) | Fork and detach the Aggregator Portal runtime from upstream branding and services | P0 / M | dashboard | CTX-003, CTX-004, CTX-006, CTX-010, CTX-012 |
| [CTX-109](CTX-109-integrate-portal-bff-secure-sessions--TODO.md) | Integrate the portal with secure BFF sessions and OIDC | P0 / L | multi-repo | CTX-037, CTX-038, CTX-044, CTX-108 |
| [CTX-110](CTX-110-verified-custom-domains-runtime-branding--TODO.md) | Implement verified custom domains and isolated runtime branding | P1 / L | multi-repo | CTX-008, CTX-016, CTX-029, CTX-034, CTX-108, CTX-109 |
| [CTX-111](CTX-111-capability-navigation-context-cache-isolation--TODO.md) | Implement capability-driven navigation and aggregator-scoped portal caches | P0 / M | dashboard | CTX-029, CTX-034, CTX-038, CTX-108, CTX-109 |
| [CTX-112](CTX-112-merchant-onboarding-lifecycle-portal--TODO.md) | Build merchant onboarding, review and lifecycle screens | P0 / L | dashboard | CTX-045, CTX-046, CTX-047, CTX-048, CTX-111 |
| [CTX-113](CTX-113-terminal-inventory-linking-lifecycle-portal--TODO.md) | Build terminal inventory, enrollment and merchant-binding screens | P0 / L | dashboard | CTX-026, CTX-047, CTX-079, CTX-081, CTX-099, CTX-100, CTX-111 |
| [CTX-114](CTX-114-acquirer-secret-configuration-projections-portal--TODO.md) | Build acquirer configuration and write-only credential management | P0 / L | dashboard | CTX-023, CTX-024, CTX-043, CTX-111 |
| [CTX-115](CTX-115-versioned-routing-policy-editor--TODO.md) | Build eligible routing policy editing, dry-run and activation | P0 / L | dashboard | CTX-054, CTX-055, CTX-068, CTX-111, CTX-114 |
| [CTX-116](CTX-116-developer-key-and-sdk-session-portal--TODO.md) | Build scoped key, SDK-session and rotation tooling | P0 / M | dashboard | CTX-040, CTX-041, CTX-042, CTX-043, CTX-111 |
| [CTX-117](CTX-117-team-memberships-roles-context-switching--TODO.md) | Build team invitations, scoped roles and deliberate context switching | P0 / L | dashboard | CTX-022, CTX-037, CTX-038, CTX-109, CTX-111 |
| [CTX-118](CTX-118-payment-operations-and-unknown-outcome-portal--TODO.md) | Build payment operations with safe capture, refund and UNKNOWN handling | P0 / L | dashboard | CTX-057, CTX-060, CTX-061, CTX-062, CTX-064, CTX-069, CTX-111 |
| [CTX-119](CTX-119-reconciliation-reports-and-secure-exports-portal--TODO.md) | Build reconciliation reports and tenant-safe exports | P0 / L | multi-repo | CTX-035, CTX-064, CTX-065, CTX-069, CTX-111 |
| [CTX-120](CTX-120-webhook-subscription-and-delivery-portal--TODO.md) | Build signed webhook configuration, delivery inspection and replay tooling | P0 / M | dashboard | CTX-059, CTX-069, CTX-111, CTX-116 |
| [CTX-121](CTX-121-isolated-platform-operator-console--TODO.md) | Build an isolated platform operator and audited support console | P0 / L | multi-repo | CTX-039, CTX-044, CTX-069, CTX-070, CTX-109, CTX-124 |
| [CTX-122](CTX-122-platform-openapi-and-integration-documentation--TODO.md) | Finalize the public platform API contract, examples and native admin isolation | P0 / L | platform | CTX-006, CTX-040, CTX-041, CTX-045, CTX-049, CTX-050, CTX-059, CTX-060, CTX-061, CTX-069, CTX-073, CTX-104, CTX-142 |
| [CTX-123](CTX-123-aggregator-contract-and-onboarding-conformance-gate--TODO.md) | Qualify aggregator portal-to-SDK contracts end to end | P0 / L | multi-repo | CTX-071, CTX-072, CTX-073, CTX-107, CTX-110, CTX-112, CTX-113, CTX-114, CTX-115, CTX-116, CTX-117, CTX-118, CTX-119, CTX-120, CTX-121, CTX-122, CTX-143 |
| [CTX-124](CTX-124-immutable-administrative-audit-trail--TODO.md) | Implement immutable administrative and privileged access auditing | P0 / L | platform | CTX-012, CTX-028, CTX-029, CTX-038, CTX-039, CTX-040, CTX-043, CTX-047, CTX-068 |
| [CTX-125](CTX-125-privacy-retention-closure-and-legal-holds--TODO.md) | Implement data lifecycle, privacy and account-closure workflows | P0 / L | multi-repo | CTX-001, CTX-009, CTX-012, CTX-033, CTX-035, CTX-046, CTX-064, CTX-065, CTX-069, CTX-124 |
| [CTX-126](CTX-126-independent-security-and-pci-solution-gate--TODO.md) | Complete independent penetration testing and PCI solution review | P0 / L | multi-repo | CTX-014, CTX-043, CTX-071, CTX-101, CTX-103, CTX-123, CTX-124, CTX-125, CTX-134; if authorization_owner="vendor": CTX-141; if application_layer_jwe=true: CTX-088 |
| [CTX-127](CTX-127-capacity-fairness-and-concurrency-qualification--TODO.md) | Qualify payment capacity, concurrency and aggregator fairness | P0 / L | multi-repo | CTX-051, CTX-052, CTX-053, CTX-063, CTX-066, CTX-067, CTX-070, CTX-072, CTX-123, CTX-134 |
| [CTX-128](CTX-128-backup-restore-key-custody-and-journal-recovery--TODO.md) | Exercise backup restore and cryptographic/journal recovery | P0 / L | infra | CTX-008, CTX-009, CTX-064, CTX-065, CTX-067, CTX-074, CTX-125, CTX-134 |
| [CTX-129](CTX-129-single-writer-regional-failover-game-day--TODO.md) | Validate single-writer regional failover and UNKNOWN-outcome recovery | P0 / L | infra | CTX-008, CTX-057, CTX-067, CTX-072, CTX-128, CTX-131, CTX-132 |
| [CTX-130](CTX-130-expand-contract-upgrades-and-client-deprecation--TODO.md) | Implement staged upgrades, client compatibility and safe rollback | P0 / L | multi-repo | CTX-006, CTX-036, CTX-068, CTX-073, CTX-074, CTX-098, CTX-100, CTX-123 |
| [CTX-131](CTX-131-payment-slos-alerts-and-operator-dashboards--TODO.md) | Implement SLO dashboards and actionable payment health alerts | P0 / L | infra | CTX-012, CTX-057, CTX-063, CTX-065, CTX-066, CTX-070, CTX-124 |
| [CTX-132](CTX-132-payment-security-and-acquirer-incident-runbooks--TODO.md) | Create and rehearse payment and security incident runbooks | P0 / L | multi-repo | CTX-039, CTX-043, CTX-047, CTX-057, CTX-065, CTX-067, CTX-070, CTX-099, CTX-124, CTX-131 |
| [CTX-133](CTX-133-licensed-aggregator-responsibility-and-onboarding-checklist--TODO.md) | Define licensed aggregator responsibilities and direct-settlement readiness | P0 / L | platform | CTX-001, CTX-002, CTX-013, CTX-014, CTX-045, CTX-048, CTX-064, CTX-065 |
| [CTX-134](CTX-134-production-infrastructure-hardening-and-scaling--TODO.md) | Implement production IaC, segmentation and resilient runtime configuration | P0 / L | infra | CTX-008, CTX-009, CTX-010, CTX-011, CTX-015, CTX-016, CTX-030, CTX-031, CTX-034, CTX-044, CTX-063, CTX-066, CTX-067, CTX-070 |
| [CTX-135](CTX-135-signed-release-candidate-and-promotion-pipeline--TODO.md) | Build signed release candidates and gated environment promotion | P0 / L | multi-repo | CTX-010, CTX-011, CTX-073, CTX-098, CTX-108, CTX-123, CTX-130, CTX-134 |
| [CTX-136](CTX-136-controlled-single-path-production-pilot--TODO.md) | Execute a controlled one-path pilot after limited release approval | P0 / L | multi-repo | CTX-103, CTX-107, CTX-123, CTX-126, CTX-127, CTX-128, CTX-129, CTX-131, CTX-132, CTX-133, CTX-135 |
| [CTX-137](CTX-137-formal-broad-launch-readiness-review--TODO.md) | Complete evidence-based readiness review for broad launch | P0 / M | multi-repo | CTX-124, CTX-125, CTX-126, CTX-127, CTX-128, CTX-129, CTX-130, CTX-131, CTX-132, CTX-133, CTX-135, CTX-136, CTX-138 |
| [CTX-138](CTX-138-upstream-and-certification-maintenance-workflow--TODO.md) | Establish upstream security, connector and certification maintenance | P1 / M | multi-repo | CTX-003, CTX-004, CTX-010, CTX-011, CTX-013, CTX-025, CTX-073, CTX-098, CTX-130, CTX-135 |
| [CTX-139](CTX-139-conditional-kotlin-payment-executor-migration--TODO.md) | Plan and qualify a future Kotlin service migration without dual financial execution [conditional] | P2 / L | multi-repo | CTX-005, CTX-006, CTX-049, CTX-055, CTX-056, CTX-057, CTX-064, CTX-067, CTX-073, CTX-123, CTX-130 |
| [CTX-140](CTX-140-conditional-ledger-balances-and-payout-domain--TODO.md) | Define a conditional double-entry ledger and funds-movement roadmap [conditional] | P2 / L | platform | CTX-001, CTX-005, CTX-006, CTX-064, CTX-065, CTX-067, CTX-125, CTX-133 |
| [CTX-143](CTX-143-dispute-case-and-evidence-handoff-portal--TODO.md) | Build dispute case, evidence and authorized handoff workflows | P0 / L | dashboard | CTX-046, CTX-059, CTX-111, CTX-118, CTX-119, CTX-124, CTX-142 |
