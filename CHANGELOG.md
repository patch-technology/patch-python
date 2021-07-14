# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.0] - 2021-07-14

### Changed

- [BREAKING] Changed `order.price_cents_usd` and `order.patch_fee_cents_usd` from string to integer.

## [1.6.0] - 2021-07-14

### Added

- Order responses return a `registry_url` field
- Add support for Bitcoin estimates

## [1.5.2] - 2021-03-30

### Fixed

- Fixes [#23](https://github.com/patch-technology/patch-python/issues/23) by allowing the expected parameter `total_price_cents_usd`

## [1.5.1] - 2021-03-02

### Fixed

- Fixed an `AttributeError` that was thrown when Projects with Sustainable Development Goals were retrieved.

## [1.5.0] - 2021-03-01

### Changed

- Changed base URL from https://api.usepatch.com to https://api.patch.io

## [1.4.0] - 2021-02-15

### Added

- Adds Sustainable Development Goals (SDGs) field to projects
- Adds the ability to filter Projects on country, type, minimum_available_mass

### Changed

- vehicle estimates now support optional `make`, `model` and `year` fields.

## [1.3.1] - 2021-02-09

### Fixed

- Adds missing dependency.

## [1.3.0] - 2021-02-08

### Added

- Adds support for creating Shipping/Flight/Vehicle estimates.
- Sets the library version to 1.3.0 to track the [Patch Ruby SDK](https://github.com/patch-technology/patch-ruby) and [Patch Node SDK](https://github.com/patch-technology/patch-node).

## [1.0.1] - 2021-01-22

### Added

- Pre-release of v1 Library
- Adds support for Orders, Estimates, Projects and Preferences
