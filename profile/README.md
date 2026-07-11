# doc-bricks

<!-- last-checked: 2026-07-11 -->

![doc-bricks logo](logo.jpg)

**Local-first document tools for reading, cleaning, collecting, converting, and organizing PDFs, Markdown files, mail attachments, invoices, media libraries, research libraries, and LLM-ready notes.**

doc-bricks builds practical desktop applications for document-heavy workflows. The projects focus on local document libraries, safe mail processing, OCR, PDF export, literature management, media organization, and structured handoff formats that remain useful for humans and LLM-assisted maintenance.

Public index status: verified on 2026-07-11 against the live GitHub organization. The profile lists 10 public repositories total: `.github` plus 9 product/tool repositories. Private or internal repositories are intentionally not listed.

## Start Here

| Need | Start with | Why |
|---|---|---|
| Read, organize, and export a local document library | [DokuReader](https://github.com/doc-bricks/DokuReader) | Topic-based document manager with previews, reading state, PDF bundling, and metadata-only JSON export |
| Work with Markdown notes and clean reading sessions | [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Local Markdown viewer/editor with reading mode, raw editing, PDF export, and PWA companion |
| Organize local media and document context | [MediaBrain](https://github.com/doc-bricks/MediaBrain) | PySide6 media library manager with smart playlists, provider detection, tags, blacklist, and private SQLite storage |
| Manage literature, PDFs, BibTeX, and research notes | [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literature manager for academic reading, bibliography workflows, and PDF-centered research |
| Launch the mail-tool family from one tray app | [MailProcessor](https://github.com/doc-bricks/MailProcessor) | System tray entry point for Universal Mail Cleaner, UniversalDocsGrabber, and UniversalInvoiceMail |
| Download and archive mail attachments locally | [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | IMAP/Gmail attachment downloader with OCR, PDF conversion, dedupe, and review workflows |
| Clean large IMAP or Gmail mailboxes safely | [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Mailbox cleaner with safe trash mode, labels, scheduler, and large-item cleanup |
| Collect invoices and receipts from mail | [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Invoice extractor with Gmail/IMAP input, OCR, PDF conversion, JSON export, and DATEV-oriented workflows |
| Keep local notes for LLM agents | [llm-note](https://github.com/doc-bricks/llm-note) | Local-first SQLite notes, plain-text notebooks, six locales, and a standalone agent skill extracted from BACH |

## Public Repository Directory

This index covers every public doc-bricks repository visible on GitHub as of 2026-07-11. Private or internal repositories are intentionally not listed on the public organization profile.

| Repository | Role | Discovery notes |
|---|---|---|
| [.github](https://github.com/doc-bricks/.github) | Organization profile and shared community-health files | Start page, issue templates, pull request template, security policy, and `llms.txt` |
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Document library | Local-first document manager, reading state, topic organization, preview workflow, PDF bundling, metadata-only JSON export |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown reading and editing | Markdown viewer/editor, reading mode, PDF export, session handoff, PWA companion |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literature management | PDF library, BibTeX workflows, academic reading, research notes, JSON export |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Mail attachment intake | IMAP/Gmail document downloader, OCR, PDF conversion, dedupe, PWA review |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Mailbox cleanup | Gmail and IMAP cleaner, safe trash mode, labels, scheduler, large-item cleanup |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Invoice and receipt intake | Invoice and receipt email archiver, OCR, PDF conversion, JSON export, DATEV-style CSV export |
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | Mail tool launcher | System tray entry point for Universal Mail Cleaner, UniversalDocsGrabber, and UniversalInvoiceMail |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Media and document hub | PySide6 media library manager, smart playlists, provider detection, tags, blacklist, private SQLite storage |
| [llm-note](https://github.com/doc-bricks/llm-note) | Agent notes and notebooks | Local-first SQLite note log, plain-text notebooks, six locales, CLI/Python API, and standalone agent skill |

## Project Families

### Document Reading And Libraries

| App | Description |
|---|---|
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Local-first document library with topic organization, previews, read status, PDF bundling, and metadata export |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown viewer/editor for clean reading, editing, PDF export, and session handoff |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literature management suite with PDF, BibTeX, JSON export, and research-oriented organization |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Local-first PySide6 media library manager with smart playlists, provider detection, tags, blacklist, and private SQLite storage |

### Mail And Intake Workflows

| App | Description |
|---|---|
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | System tray launcher for Universal Mail Cleaner, UniversalDocsGrabber, and UniversalInvoiceMail |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Local Gmail and IMAP mailbox cleanup with safe modes and scheduler support |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Attachment downloader and document archive builder for IMAP/Gmail intake, OCR, PDF conversion, and PWA review |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Invoice and receipt collection pipeline for local archives, OCR/PDF conversion, JSON export, and DATEV-style CSV export |

### PDF, OCR, And Export

| App | Description |
|---|---|
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Converts downloaded mail documents into reviewable PDF/OCR archive material |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Converts invoice and receipt mail into PDF/OCR archive material and accounting-oriented exports |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Exports Markdown reading sessions to PDF and companion web formats |

### Notes And Agent Handoffs

| App | Description |
|---|---|
| [llm-note](https://github.com/doc-bricks/llm-note) | Local-first notes and notebook inboxes for LLM agents, extracted from BACH Notizblock/Denkarium patterns |

## Design Principles

- **Local first:** documents, mail exports, indexes, and reading state stay on the user's machine by default.
- **Privacy-conscious:** tools avoid cloud processing unless an external service such as Gmail is explicitly configured by the user.
- **Document-practical:** each project targets repeated real workflows: reading, previewing, cleaning, exporting, archiving, and handoff.
- **Structured exports:** JSON, BibTeX, PDF, and companion formats are documented so data can move between desktop tools and later automation.
- **Readable maintenance:** READMEs, tests, and `llms.txt` files are kept useful for both human maintainers and LLM-based assistants.

## Discovery Signals

Useful search phrases for the public doc-bricks profile include `local-first document tools`, `Python document management`, `PySide6 PDF OCR`, `DokuReader metadata JSON export`, `MediaBrain smart playlists private SQLite`, `Gmail IMAP attachment downloader`, `Markdown PDF export`, `literature manager GitHub`, `invoice mail OCR DATEV export`, and `local-first LLM agent notes`.

## Machine-Readable Context

For crawlers and LLM tools, see [`llms.txt`](https://github.com/doc-bricks/.github/blob/main/llms.txt). It lists the canonical repositories, project roles, and preferred search phrases for the doc-bricks organization.

## Ecosystem

doc-bricks is the document-work branch of the brick suite:

[open-bricks](https://github.com/open-bricks) | [file-bricks](https://github.com/file-bricks) | [dev-bricks](https://github.com/dev-bricks)

Part of the [ellmos-ai](https://github.com/ellmos-ai) ecosystem.

## Related (other orgs)

| Project | Description |
|---|---|
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Multilingual knowledge-stub dataset (630 terms, 12 domains, DE/EN + es/ja/ru/zh) with a web publisher — deployable as a self-contained wiki module |
