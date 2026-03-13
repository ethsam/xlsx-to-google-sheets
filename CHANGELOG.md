# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-03-13

### Added

- Bilingual documentation (English + French)
- `README.md` in English for international audience
- `README.fr.md` in French with cross-links
- `requirements.txt` with pinned minimum versions
- MIT License for open-source distribution
- Contributing guidelines
- Architecture diagram in documentation
- Authentication comparison table

### Changed

- Project restructured for open-source GitHub distribution
- Documentation rewritten with badges, tables, and diagrams

### Removed

- Client-specific documentation files (CONTACT.md, INFO.md, QUICKSTART.md, etc.)
- Proprietary license replaced by MIT

## [1.0.0] - 2026-03-01

### Added

- Recursive Google Drive folder exploration
- Automatic conversion: Excel (.xlsx, .xls), CSV, TSV, ODS to Google Sheets
- Service Account authentication (`convert_drive_to_sheets.py`)
- OAuth 2.0 authentication (`convert_drive_to_sheets_oauth.py`)
- Interactive launcher (`start.sh`)
- Automated installer (`install.sh`)
- Original files preserved (non-destructive)
- Interactive and batch mode (`--yes` flag)
- Automatic pagination for large folders
- Detailed conversion report (success/error counts)
- `.gitignore` protecting credential files
