# Changelog

All notable changes to the `doc-bricks/.github` repository will be documented in this file.

## [1.0.5] - 2026-08-06

### Added
- Added a "Repository Showcase" banner grid to `profile/README.md` and `profile/README_de.md`, following the ellmos-ai org-profile pattern: verified `banner.svg` artwork for all 9 public product/tool repositories, each linking to its repository, with the existing text tables kept as the detail reference below the banners.

### Changed
- Updated verification timestamps across `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt` to `2026-08-06`.
- Re-verified the public repository index against the live GitHub organization: still 10 public repositories (`.github` plus 9 product/tool repositories); no private repository is referenced anywhere in this repository's documentation.

## [1.0.4] - 2026-08-01

### Fixed
- Corrected the ecosystem architecture diagram in `profile/README.md` and `profile/README_de.md`: `llm-note` is a notepad for humans whose content is filled by LLMs on the user's behalf — not a notepad for LLM agents. (Ref T-20260801-02)

### Changed
- Updated verification timestamps across `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt` to `2026-08-01`.
- Enhanced Shields.io badges in `profile/README.md` and `profile/README_de.md` with explicit `open-bricks` umbrella and `ellmos-ai` ecosystem integration.
- Verified 1:1 bilingual parity and public repository directory completeness across all 10 public `doc-bricks` repositories.

## [1.0.3] - 2026-07-29

### Changed
- Updated verification timestamps across `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt` to `2026-07-29`.
- Refined repository index descriptions for `MediaBrain`, `LitZentrum`, `DokuReader`, and `llm-note` to reflect latest feature sets.
- Verified bilingual 1:1 parity between English (`profile/README.md`) and German (`profile/README_de.md`) organization profile landing pages.
- Verified 100% clean UTF-8 encoding and link integrity across all public profile documentation.

## [1.0.2] - 2026-07-26

### Added
- Created German organization profile landing page `profile/README_de.md` for bilingual accessibility.
- Embedded interactive Mermaid architecture flowchart in `profile/README.md` and `profile/README_de.md` detailing document, mail, reading, and agent note workflows.
- Added modern Shields.io badges for public repository count, privacy focus, MIT license, LLM context, and language switcher.
- Added GitHub-Flavored Markdown Callouts (`> [!NOTE]`, `> [!TIP]`) highlighting local-first guarantees and LLM-readable context.

### Changed
- Updated verification timestamps across `profile/README.md`, `README.md`, and `llms.txt` to `2026-07-26`.
- Upgraded `.github/workflows/stale.yml` to `actions/stale@v10`.
- Upgraded `.github/workflows/welcome.yml` to `actions/first-interaction@v3`.

### Fixed
- Fixed UTF-8 character encoding artifact in WikiStub-Seed description within `profile/README.md`.
