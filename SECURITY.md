# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `doc-bricks` organization, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@open-bricks.org`
   - `security@ellmos.ai`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 7 to 14 days
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Tool | Supported Release | Security Updates |
|---|---|---|
| Active repositories (`CleanMarkdown`, `DokuReader`, `DokuZen`, `LitZentrum`, `llm-note`, `MailProcessor`, `MediaBrain`, `PDFtoPDFocr`, `UniversalDocsGrabber`, `UniversalInvoiceMail`, `UniversalMailCleaner`, `.github`) | Latest commit on `main`/`master` | :white_check_mark: Supported |

---

## Security Invariants / Sicherheitsinvarianten

- **Zero-Egress & Local-First:** All document processing, OCR conversion, Markdown rendering, and SQLite storage routines run 100% locally with zero unconsented telemetry or cloud data egress.
- **Unprivileged User Mode (Non-Elevation):** None of the desktop utilities require elevated administrator/root permissions.
- **Integrity & Source Preservation:** OCR and conversion tools preserve original input files by default and write outputs non-destructively.
