# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2022-05-29

### Added

- Strict type checking for code and tests with `mypy`.

### Fixed

- Moved `py.typed` to correct location ensuring compatibility with mypy.
- CI.

## [0.1.1] - 2022-03-20

Better code quality enforcements and a leaner project structure. BytesIOEx
boasts of a 98% coverage now!

### Added

- PEP-561 compliance (`py.typed`).
- More pre-commit hooks for maintaining code quality.
- Adopted semantic versioning.
- `tbump` for version handling.
- Flake8, Bandit and Pylint.
- Follow Google-style Python coding guidelines.

### Changed

- `requirements` file now has a constraints file.
- All old tasks replaced with `tox-gh-actions` in CI.
- Beautified `README.md` (and `docs/index.md`).

### Removed

- `conftest.py`. `pytest` config is now in `pyproject.toml`.
- `TODO.md`; its contents have been moved to `README.md` > Roadmap.
- `docs/reference.md`; contents moved to `docs/index.md`.

## [0.1.0]

### Added

- Automated build and publish on commit
- [Docs](https://bytesioex.rtfd.io)

### Changed

- Smaller function names.

### Fixed

- Import errors.
- Code cleanup.

<!-- VERSION LINKS -->

[0.1.2]: https://github.com/demberto/bytesioex/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/demberto/bytesioex/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/demberto/bytesioex/releases/tag/v0.0.1
