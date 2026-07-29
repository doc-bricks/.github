# doc-bricks

<p align="center">
  <img src="logo.jpg" alt="doc-bricks logo" width="120" />
</p>

<p align="center">
  <strong>Local-First Desktop Tools for Document Libraries, Reading, Mail Intake, OCR, Literature Management, and LLM-Agent Notes</strong>
</p>

<p align="center">
  <a href="https://github.com/doc-bricks/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Public_Repos-10-blue?style=flat-square&logo=github" alt="Public Repositories" /></a>
  <a href="https://github.com/doc-bricks"><img src="https://img.shields.io/badge/Focus-Local--First_Document_Tools-emerald?style=flat-square" alt="Focus" /></a>
  <a href="https://github.com/doc-bricks"><img src="https://img.shields.io/badge/Privacy-100%25_Local_Data-purple?style=flat-square" alt="Privacy" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/llms.txt"><img src="https://img.shields.io/badge/LLM_Context-llms.txt-orange?style=flat-square" alt="LLM Context" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/profile/README_de.md"><img src="https://img.shields.io/badge/Language-Deutsch-blue?style=flat-square" alt="German Version" /></a>
</p>

> [!NOTE]
> **Local-First & LLM-Ready:** All doc-bricks tools run locally on your system, keeping documents, PDFs, and notes private. Machine-readable context is available in [`llms.txt`](https://github.com/doc-bricks/.github/blob/main/llms.txt) for LLM agents and crawlers.

> [!TIP]
> **Deutsche Version:** Eine deutschsprachige Übersetzung dieser Organisations-Startseite finden Sie unter [`profile/README_de.md`](https://github.com/doc-bricks/.github/blob/main/profile/README_de.md).

---

## Ecosystem Architecture

```mermaid
graph TD
    subgraph Intake ["Mail & Document Intake"]
        MP["MailProcessor (Tray Launcher)"] --> UMC["UniversalMailCleaner"]
        MP --> UDG["UniversalDocsGrabber"]
        MP --> UIM["UniversalInvoiceMail"]
    end

    subgraph Library ["Document & Media Libraries"]
        DR["DokuReader (Document Hub)"]
        CM["CleanMarkdown (Reader & Editor)"]
        LZ["LitZentrum (Literature & BibTeX)"]
        MB["MediaBrain (PySide6 Media Library)"]
    end

    subgraph AgentNotes ["Agent Notes & Knowledge"]
        LN["llm-note (SQLite & Notebooks)"]
    end

    UDG -->|"PDF / OCR Archive"| DR
    UIM -->|"Invoices & DATEV CSV"| DR
    CM -->|"Export PDF / Handoff"| DR
    LZ -->|"BibTeX & Notes"| LN
    DR -->|"Metadata JSON Export"| LN
    MB -->|"Private SQLite Context"| LN
```

---

## Start Here

| Goal | Recommended Tool | Core Capability |
|---|---|---|
| Manage local document libraries, topics, and PDF bundles | [DokuReader](https://github.com/doc-bricks/DokuReader) | Local-first document library, preview workflow, reading state, PDF bundling, and metadata JSON export |
| Read and edit Markdown without cloud lock-in | [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Local Markdown viewer/editor with clean reading mode, PDF export, session handoff, and PWA companion |
| Organize local media and document context | [MediaBrain](https://github.com/doc-bricks/MediaBrain) | PySide6 media library manager with smart playlists, provider detection, tags, blacklist, and private SQLite storage |
| Manage literature, PDFs, BibTeX, and research notes | [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literature manager for academic reading, bibliography workflows, and PDF-centered research |
| Launch the mail-tool family from one tray app | [MailProcessor](https://github.com/doc-bricks/MailProcessor) | System tray entry point for Universal Mail Cleaner, UniversalDocsGrabber, and UniversalInvoiceMail |
| Download and archive mail attachments locally | [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | IMAP/Gmail attachment downloader with OCR, PDF conversion, dedupe, and review workflows |
| Clean large IMAP or Gmail mailboxes safely | [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Mailbox cleaner with safe trash mode, labels, scheduler, and large-item cleanup |
| Collect invoices and receipts from mail | [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Invoice extractor with Gmail/IMAP input, OCR, PDF conversion, JSON export, and DATEV-oriented workflows |
| Keep local notes for LLM agents | [llm-note](https://github.com/doc-bricks/llm-note) | Local-first SQLite notes, plain-text notebooks, six locales, and a standalone agent skill extracted from BACH |

---

## Public Repository Directory

This index covers every public doc-bricks repository visible on GitHub as of **2026-07-29**. Private or internal repositories are intentionally not listed on the public organization profile.

| Repository | Role | Discovery notes |
|---|---|---|
| [.github](https://github.com/doc-bricks/.github) | Organization profile and shared community-health files | Start page, issue templates, pull request template, security policy, and `llms.txt` |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown reading and editing | Markdown viewer/editor, reading mode, PDF export, session handoff, PWA companion |
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Document library | Local-first document manager, reading state, topic organization, preview workflow, PDF bundling, metadata-only JSON export |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literature management | PDF library, BibTeX workflows, academic reading, research notes, JSON export |
| [llm-note](https://github.com/doc-bricks/llm-note) | Agent notes and notebooks | Local-first SQLite note log, plain-text notebooks, six locales, CLI/Python API, and standalone agent skill |
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | Mail tool launcher | System tray entry point for Universal Mail Cleaner, UniversalDocsGrabber, and UniversalInvoiceMail |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Media and document hub | PySide6 media library manager, smart playlists, provider detection, tags, blacklist, private SQLite storage |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Mail attachment intake | IMAP/Gmail document downloader, OCR, PDF conversion, dedupe, PWA review |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Invoice and receipt intake | Invoice and receipt email archiver, OCR, PDF conversion, JSON export, DATEV-style CSV export |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Mailbox cleanup | Gmail and IMAP cleaner, safe trash mode, labels, scheduler, large-item cleanup |

---

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

---

## Design Principles

- **Local first:** documents, mail exports, indexes, and reading state stay on the user's machine by default.
- **Privacy-conscious:** tools avoid cloud processing unless an external service such as Gmail is explicitly configured by the user.
- **Document-practical:** each project targets repeated real workflows: reading, previewing, cleaning, exporting, archiving, and handoff.
- **Structured exports:** JSON, BibTeX, PDF, and companion formats are documented so data can move between desktop tools and later automation.
- **Readable maintenance:** READMEs, tests, and `llms.txt` files are kept useful for both human maintainers and LLM-based assistants.

---

## Discovery Signals

Useful search phrases for the public doc-bricks profile include `local-first document tools`, `Python document management`, `PySide6 PDF OCR`, `DokuReader metadata JSON export`, `MediaBrain smart playlists private SQLite`, `Gmail IMAP attachment downloader`, `Markdown PDF export`, `literature manager GitHub`, `invoice mail OCR DATEV export`, and `local-first LLM agent notes`.

---

## Machine-Readable Context

For crawlers and LLM tools, see [`llms.txt`](https://github.com/doc-bricks/.github/blob/main/llms.txt). It lists the canonical repositories, project roles, and preferred search phrases for the doc-bricks organization.

---

## Ecosystem

doc-bricks is the document-work branch of the brick suite:

[open-bricks](https://github.com/open-bricks) | [file-bricks](https://github.com/file-bricks) | [dev-bricks](https://github.com/dev-bricks)

Part of the [ellmos-ai](https://github.com/ellmos-ai) ecosystem: [llm-note](https://github.com/doc-bricks/llm-note) was extracted from [ellmos-ai/bach](https://github.com/ellmos-ai/bach)'s Notizblock/Denkarium patterns and remains usable as a standalone agent-notes skill.

---

## Related (other orgs)

| Project | Description |
|---|---|
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Multilingual knowledge-stub dataset (630 terms, 12 domains, DE/EN + es/ja/ru/zh) with a web publisher — deployable as a self-contained wiki module |
