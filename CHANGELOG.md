# Changelog

## [1.0.4](https://github.com/straddle-build/straddle-python/compare/v1.0.0...v1.0.4) (2026-09-13)


### ⚠ BREAKING CHANGES

* **api:** 16 breaking changes to the SDK surface.
    - Response content type of `bridge.createBankAccountPaykey` changed from `text/plain` to `application/json`.
    - `400` error response of `bridge.createBankAccountPaykey` changed from `error_response` to `error_response`.
    - Response content type of `customers.create` changed from `text/plain` to `application/json`.
    - `400` error response of `customers.create` changed from `error_response` to `error_response`.
    - Response content type of `charges.create` changed from `text/plain` to `application/json`.
    - `400` error response of `charges.create` changed from `error_response` to `error_response`.
    - Response content type of `payouts.create` changed from `text/plain` to `application/json`.
    - `400` error response of `payouts.create` changed from `error_response` to `error_response`.
    - Property `payout.created_at` is now required.
    - Property `payout.created_at` type changed from `string<date-time> | null` to `string<date-time>`.
    - Property `payout.updated_at` is now required.
    - Property `payout.updated_at` type changed from `string<date-time> | null` to `string<date-time>`.
    - Property `unmasked_payout.created_at` is now required.
    - Property `unmasked_payout.created_at` type changed from `string<date-time> | null` to `string<date-time>`.
    - Property `unmasked_payout.updated_at` is now required.
    - Property `unmasked_payout.updated_at` type changed from `string<date-time> | null` to `string<date-time>`.
* **api:** 4 breaking changes to the SDK surface.
    - Property `embed_error_response.data` type changed from `unknown | null` to `unknown`.
    - Schema `customer_address` shape changed.
    - Schema `unmasked_compliance_profile` shape changed.
    - Schema `compliance_profile` shape changed.

### Features

* **api:** update property embed_error_response.data (+3 more changes) ([e66d4b9](https://github.com/straddle-build/straddle-python/commit/e66d4b94c45713b4d6037976fbb77dd0faa9f758))
* **api:** update SDK surface (17 changes) ([0a4bf62](https://github.com/straddle-build/straddle-python/commit/0a4bf62e68a0979478667fd2c9ddf9903ab33a67))


### Chores

* **api:** regenerate SDK ([6d9023f](https://github.com/straddle-build/straddle-python/commit/6d9023f8cb00ae387c2c759dea915fb1f314dc18))
* release 1.0.4 ([d019d90](https://github.com/straddle-build/straddle-python/commit/d019d9030d3e657f6582971ca309806d10d53f11))
* release 1.0.4 ([5f16e1d](https://github.com/straddle-build/straddle-python/commit/5f16e1d6a9f4b2aa1aff78919a6a0eeecba3c8e4))

## [1.0.0](https://github.com/straddle-build/straddle-python/compare/v0.1.0...v1.0.0) (2026-09-03)


### Features

* **api:** initial SDK generation ([baec056](https://github.com/straddle-build/straddle-python/commit/baec056eb5e576ee2d382891e27609ee73eddb34))


### Chores

* **api:** update generated SDK content ([f84daa4](https://github.com/straddle-build/straddle-python/commit/f84daa48f8ec27e8e5ab914486e18f7dc2e8b106))
* release 1.0.0 ([fd0bf55](https://github.com/straddle-build/straddle-python/commit/fd0bf556b2df7abea436726487a30b9348a1ddf5))
* release 1.0.0 ([bd5c1ca](https://github.com/straddle-build/straddle-python/commit/bd5c1ca9c6c1c1437ef63c2c10d2db9cc99509e6))
