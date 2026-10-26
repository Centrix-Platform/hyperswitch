# Repository and source map

Inspection baseline: core commit `c5ecb434b419d2c473cf2882a3866de9146abdec`, 2026-10-22. Re-verify the target checkout and pins when executing a ticket. Existing files are context/read locations, not permission to overwrite unrelated changes.

## Available checkout

| Existing path | Relevance |
|---|---|
| `Cargo.toml`, `Cargo.lock` | Workspace/toolchain/dependency baseline. |
| `crates/router/Cargo.toml`, `justfile` | Feature sets and build recipes; v1/v2 are mutually exclusive. |
| `crates/hyperswitch_interfaces/src/configs.rs` | Tenant schema/accounts/Redis/analytics placement. |
| `crates/diesel_models/src/merchant_account.rs` | Native aggregator projection and account features. |
| `crates/diesel_models/src/business_profile.rs` | Profile-owned processing configuration. |
| `crates/diesel_models/src/merchant_connector_account.rs` | Profile-associated connector credential/configuration projection. |
| `crates/diesel_models/src/customers.rs`, `payment_method.rs` | Native customer/vault ownership caveat. |
| `crates/diesel_models/src/api_keys.rs`, `ephemeral_key.rs` | Native key/expiry models and customer-oriented ephemeral keys. |
| `crates/router/src/services/authentication.rs` | Native authentication, SDK/platform resolution and context integration. |
| `crates/router/src/services/authorization.rs` and `authorization/` | Permission and role integration points. |
| `crates/router/src/routes/app.rs` | Route inventory and native/internal API surfaces. |
| `crates/router/src/core/admin.rs` | Native account/profile/MCA provisioning integration. |
| `crates/router/src/core/payments.rs`, `core/payments/` | Native execution flow and lifecycle operations. |
| `crates/router/src/core/payments/routing.rs` | Native route evaluation/selection integration. |
| `crates/router/src/core/api_locking.rs` | Existing Redis API locking; not the complete new idempotency contract. |
| `crates/storage_impl/src/lib.rs`, `src/payments/payment_intent.rs` | Pools, storage context and PostgreSQL/RedisKv paths. |
| `crates/api_models`, `crates/openapi`, `api-reference`, `proto` | Native public/internal contracts to adapt, not expose wholesale. |
| `crates/hyperswitch_connectors`, `add_connector.md` | Connector implementation guidance and extension points. |
| `crates/analytics`, `monitoring` | Analytics/report scope and operational visibility. |
| `migrations`, `v2_migrations`, `v2_compatible_migrations` | Distinct migration tracks; select the actual baseline before changes. |
| `.github/workflows`, `scripts`, `config` | Existing delivery/configuration tooling. |
| `crates/test_utils`, `crates/router/tests`, `cypress-tests`, `loadtest` | Existing test/simulator/capacity integration points. |

The working tree already contained user edits to `docker-compose.yml` and `package-lock.json` before backlog creation. The PDF in `output/pdf/` is a prior deliverable. This backlog does not modify any of those files.

## External repositories

These repositories are not checked out in this workspace. Verify fork ownership, pins, available licenses/modules and paths before editing. Do not create local paths and assume they are the real SDK/dashboard source.

- [Control Center](https://github.com/juspay/hyperswitch-control-center): React/ReScript with some TypeScript. Inspected source locations: `README.md`, `package.json`, `config/config.toml`. Runtime configuration contains endpoints and branding/feature settings.
- [Android SDK](https://github.com/juspay/hyperswitch-sdk-android): inspected at `f77ec2f6883e324484e2f7cf6ce6d0939aa8e533` for the blueprint. Relevant verified upstream locations include `app/src/main/kotlin/io/hyperswitch/sdk/Hyperswitch.kt`, `app/src/main/kotlin/io/hyperswitch/sdk/PaymentSession.kt`, `hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/model/Model.kt`, `hyperswitch-sdk-android-api/src/main/kotlin/io/hyperswitch/PaymentConfiguration.kt` and `app/build.gradle`.
- [Client Core](https://github.com/juspay/hyperswitch-client-core): shared SDK/client-core/submodule and runtime build/configuration inputs. Its `README.md` describes shared setup and endpoint environment variables.
- Vendor terminal SDKs, payment applications, attestation roots, HSM interfaces and acquirer protocols: inputs to CTX-013, not bundled or verified by the general source checkout.

`Model.kt` in the inspected Android API exposes override endpoints for backend, logging, assets, SDK configuration, confirmation and Airborne. The main Android initialization uses shared React Native implementation. White-label and security reviews must cover that full dependency and egress chain.

## Proposed implementation locations

Ticket touchpoints prefixed `Proposed:` are design suggestions, not existing packages or committed service layouts. CTX-005 chooses actual modules/deployment boundaries. CTX-006 chooses contract catalog paths. Do not independently create parallel `gateway`, `platform`, `ctx` and Kotlin modules that own the same aggregate.

When a ticket points at an existing native file, inspect its selected feature branch and call chain before editing. Directory references indicate a search starting point, not a requirement to rewrite the directory. Follow any newly applicable AGENTS.md instructions in the execution checkout.
