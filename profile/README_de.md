# doc-bricks

<p align="center">
  <img src="logo.jpg" alt="doc-bricks Logo" width="120" />
</p>

<p align="center">
  <strong>Local-First Desktop-Werkzeuge für Dokumentenbibliotheken, Leseumgebungen, Mail-Erfassung, OCR, Literaturverwaltung und LLM-Agenten-Notizen</strong>
</p>

<p align="center">
  <a href="https://github.com/doc-bricks/.github/blob/main/profile/README_de.md"><img src="https://img.shields.io/badge/Öffentliche_Repos-10-blue?style=flat-square&logo=github" alt="Öffentliche Repositories" /></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/Dachorganisation-open--bricks-blue?style=flat-square&logo=github" alt="Dachorganisation: open-bricks" /></a>
  <a href="https://github.com/ellmos-ai"><img src="https://img.shields.io/badge/Ökosystem-ellmos--ai-purple?style=flat-square&logo=github" alt="Ökosystem: ellmos-ai" /></a>
  <a href="https://github.com/doc-bricks"><img src="https://img.shields.io/badge/Fokus-Local--First_Dokumentenwerkzeuge-emerald?style=flat-square" alt="Fokus" /></a>
  <a href="https://github.com/doc-bricks"><img src="https://img.shields.io/badge/Datenschutz-100%25_Lokale_Daten-purple?style=flat-square" alt="Datenschutz" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/LICENSE"><img src="https://img.shields.io/badge/Lizenz-MIT-blue?style=flat-square" alt="Lizenz" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/llms.txt"><img src="https://img.shields.io/badge/LLM_Kontext-llms.txt-orange?style=flat-square" alt="LLM-Kontext" /></a>
  <a href="https://github.com/doc-bricks/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Sprache-English-blue?style=flat-square" alt="Englische Version" /></a>
</p>

> [!NOTE]
> **Local-First & LLM-Bereit:** Alle doc-bricks-Werkzeuge laufen vollständig lokal auf Ihrem System. Dokumente, PDFs und Notizen verbleiben strikt privat. Maschinenlesbarer Kontext für LLM-Agenten und Crawler ist in [`llms.txt`](https://github.com/doc-bricks/.github/blob/main/llms.txt) hinterlegt.

> [!TIP]
> **English Version:** For the English version of this organization profile, see [`profile/README.md`](https://github.com/doc-bricks/.github/blob/main/profile/README.md).

---

## Systemarchitektur im Ökosystem

```mermaid
graph TD
    subgraph Intake ["Mail- & Dokumenten-Erfassung"]
        MP["MailProcessor (Tray-Starter)"] --> UMC["UniversalMailCleaner"]
        MP --> UDG["UniversalDocsGrabber"]
        MP --> UIM["UniversalInvoiceMail"]
    end

    subgraph Library ["Dokumenten- & Medienbibliotheken"]
        DR["DokuReader (Dokumenten-Zentrum)"]
        CM["CleanMarkdown (Reader & Editor)"]
        LZ["LitZentrum (Literatur & BibTeX)"]
        MB["MediaBrain (PySide6 Medienbibliothek)"]
    end

    subgraph HumanNotes ["Notizblock für Menschen — befüllt durch LLMs im Auftrag des Nutzers"]
        LN["llm-note (SQLite & Notizbücher)"]
    end

    UDG -->|"PDF / OCR-Archiv"| DR
    UIM -->|"Rechnungen & DATEV-CSV"| DR
    CM -->|"PDF-Export / Übergabe"| DR
    LZ -->|"BibTeX & Notizen"| LN
    DR -->|"Metadaten-JSON-Export"| LN
    MB -->|"Privater SQLite-Kontext"| LN
```

---

## Schnellstart-Übersicht

| Ziel | Empfohlenes Werkzeug | Kernfunktion |
|---|---|---|
| Lokale Dokumentenbibliotheken, Themen und PDF-Pakete verwalten | [DokuReader](https://github.com/doc-bricks/DokuReader) | Local-First Dokumentenverwaltung, Vorschau, Lesestatus, PDF-Bündelung und Metadaten-JSON-Export |
| Markdown ohne Cloud-Abhängigkeit lesen und bearbeiten | [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Lokaler Markdown-Viewer/Editor mit fokussiertem Lesemodus, PDF-Export, Sitzungsübergabe und PWA-Begleiter |
| Lokale Medien und Dokumentenkontexte organisieren | [MediaBrain](https://github.com/doc-bricks/MediaBrain) | PySide6 Medienbibliothek mit intelligenten Playlists, Anbietererkennung, Tags, Blacklist und privater SQLite-Ablage |
| Literatur, PDFs, BibTeX und Forschungsnotizen pflegen | [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literaturverwaltung für akademisches Lesen, Bibliografie-Workflows und PDF-zentrierte Recherche |
| Mail-Werkzeuge zentral aus der Taskleiste starten | [MailProcessor](https://github.com/doc-bricks/MailProcessor) | System-Tray-Starter für Universal Mail Cleaner, UniversalDocsGrabber und UniversalInvoiceMail |
| Mail-Anhänge lokal herunterladen und archivieren | [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | IMAP/Gmail-Anhangs-Downloader mit OCR, PDF-Konvertierung, Dublettenerkennung und Prüf-Workflows |
| Große IMAP- oder Gmail-Postfächer sicher bereinigen | [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Postfach-Bereinigung mit sicherem Papierkorb-Modus, Labels, Zeitplaner und Großdatei-Bereinigung |
| Rechnungen und Belege aus Mails erfassen | [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Rechnungsextraktor mit Gmail/IMAP-Eingang, OCR, PDF-Konvertierung, JSON-Export und DATEV-orientierten Workflows |
| Lokale Notizen für LLM-Agenten führen | [llm-note](https://github.com/doc-bricks/llm-note) | Local-First SQLite-Notizen, Plaintext-Notizbücher, sechs Sprachen und eigenständiger Agenten-Skill |

---

## Funktions- & Format-Matrix

| Repository | Formate & Quellen | Hauptfunktionen | Primärer Anwendungsfall | Ausgabe & Exporte |
|---|---|---|---|---|
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown, Text, HTML | Ablenkungsfreier Lesemodus, Split-View, Live-Vorschau | Konzentriertes Lesen und saubere Bearbeitung | Formatiertes PDF, HTML, PWA-Sitzungsübergabe |
| [DokuReader](https://github.com/doc-bricks/DokuReader) | PDF, EPUB, TXT, MD | Multi-Tab-Reader, Themenbäume, Lesezeichen, Lesestatus | Zentrales Archiv für Dokumente und Recherche | PDF-Pakete, Metadaten-JSON-Export |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | PDF, BibTeX, DOI-Referenzen | Akademischer Katalog, Zitationsmanagement, Notizen | Wissenschaftliche Literatur & Zitationsverwaltung | BibTeX `.bib`, strukturierter JSON-Index |
| [llm-note](https://github.com/doc-bricks/llm-note) | SQLite, Plaintext Markdown | Agenten-Notizblock, Prompt-Ablage, strukturierte Notizen | Speicherpersistenz & Notiz-Inbox für LLMs | SQLite-DB, Markdown-Notizbücher, CLI/Python-API |
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | IMAP, Gmail, EML | System-Tray-Starter, Hintergrunddienst, Statusanzeige | Zentraler Zugriff und Launcher für Mail-Tools | Prozess-Manager, Desktop-Benachrichtigungen |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Audio, Video, Bilder, Dokumente | Smarte Playlists, Anbieter-Erkennung, Tagging, Blacklist | Lokale Medien- und Dokumentverwaltung | Private SQLite-DB, Playlist-Exporte |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | IMAP/Gmail-Anhänge, PDFs, Bilder | Automatischer Download, Duplikaterkennung, OCR-Pipeline | Automatische Erfassung von Mail-Anhängen | Durchsuchbare PDFs, OCR-Text, PWA-Review |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | IMAP/Gmail-Rechnungen, Belege | Header-Extraktion, OCR, Betragserkennung, Dublettenfilter | Automatisierte Buchhaltungs- und Belegaufnahme | Durchsuchbare PDFs, DATEV-kompatible CSV, JSON |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | IMAP, Gmail-Postfächer | Größenfilter, regelbasierte Bereinigung, sicherer Papierkorb | Postfachpflege & Speicherplatzrückgewinnung | Bereinigtes Postfach, Prüfprotokolle |

---

## Repository Showcase

Unser lokales Dokumenten-Werkzeugset — die Banner dienen als direkte Links; Detailinformationen finden sich in der Tabelle darunter:

<p align="center"><a href="https://github.com/doc-bricks/CleanMarkdown"><img src="https://raw.githubusercontent.com/doc-bricks/CleanMarkdown/main/assets/banner.svg" alt="CleanMarkdown" width="680" style="border:2px solid #38bdf8;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/DokuReader"><img src="https://raw.githubusercontent.com/doc-bricks/DokuReader/master/assets/banner.svg" alt="DokuReader" width="680" style="border:2px solid #f472b6;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/LitZentrum"><img src="https://raw.githubusercontent.com/doc-bricks/LitZentrum/master/assets/banner.svg" alt="LitZentrum" width="680" style="border:2px solid #2dd4bf;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/llm-note"><img src="https://raw.githubusercontent.com/doc-bricks/llm-note/main/assets/banner.svg" alt="llm-note" width="680" style="border:2px solid #fbbf24;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/MailProcessor"><img src="https://raw.githubusercontent.com/doc-bricks/MailProcessor/main/assets/banner.svg" alt="MailProcessor" width="680" style="border:2px solid #e879f9;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/MediaBrain"><img src="https://raw.githubusercontent.com/doc-bricks/MediaBrain/master/assets/banner.svg" alt="MediaBrain" width="680" style="border:2px solid #a3e635;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/UniversalDocsGrabber"><img src="https://raw.githubusercontent.com/doc-bricks/UniversalDocsGrabber/master/assets/banner.svg" alt="UniversalDocsGrabber" width="680" style="border:2px solid #fb923c;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/UniversalInvoiceMail"><img src="https://raw.githubusercontent.com/doc-bricks/UniversalInvoiceMail/master/assets/banner.svg" alt="UniversalInvoiceMail" width="680" style="border:2px solid #34d399;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/doc-bricks/UniversalMailCleaner"><img src="https://raw.githubusercontent.com/doc-bricks/UniversalMailCleaner/master/assets/banner.svg" alt="UniversalMailCleaner" width="680" style="border:2px solid #818cf8;border-radius:8px;display:block;margin:0 auto"></a></p>

Weitere Repositories ohne eigenes Artwork: **[.github](https://github.com/doc-bricks/.github)** (Organisationsprofil und zentrale Community-Dateien)

---

## Verzeichnis der öffentlichen Repositories

Dieser Index führt jedes öffentliche doc-bricks-Repository auf GitHub mit Stand **2026-08-14** auf. Private oder interne Repositories werden im öffentlichen Profil bewusst nicht aufgeführt.

| Repository | Rolle | Beschreibung |
|---|---|---|
| [.github](https://github.com/doc-bricks/.github) | Organisationsprofil und gemeinsame Community-Dateien | Startseite, Issue-Templates, Pull-Request-Vorlage, Sicherheitsrichtlinie und `llms.txt` |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown-Lesen und Bearbeiten | Markdown-Viewer/Editor, Lesemodus, PDF-Export, Sitzungsübergabe, PWA-Begleiter |
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Dokumentenbibliothek | Local-First Dokumentenverwaltung, Lesestatus, Themenorganisation, Vorschau, PDF-Bündelung, Metadaten-JSON-Export |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literaturverwaltung | PDF-Bibliothek, BibTeX-Workflows, akademisches Lesen, Forschungsnotizen, JSON-Export |
| [llm-note](https://github.com/doc-bricks/llm-note) | Agenten-Notizen und Notizbücher | Local-First SQLite-Notizprotokoll, Plaintext-Notizbücher, sechs Sprachen, CLI/Python-API und eigenständiger Agenten-Skill |
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | Mail-Werkzeug-Starter | System-Tray-Einstiegspunkt für Universal Mail Cleaner, UniversalDocsGrabber und UniversalInvoiceMail |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Medien- und Dokumentenzentrum | PySide6 Medienbibliotheksverwaltung, smarte Playlists, Anbietererkennung, Tags, Blacklist, private SQLite-Ablage |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Mail-Anhangs-Erfassung | IMAP/Gmail-Dokumenten-Downloader, OCR, PDF-Konvertierung, Duplikaterkennung, PWA-Prüfung |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Rechnungs- und Beleg-Erfassung | Rechnungs- und Beleg-Archivierung, OCR, PDF-Konvertierung, JSON-Export, DATEV-kompatibler CSV-Export |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Postfach-Bereinigung | Gmail- und IMAP-Bereiniger, sicherer Papierkorb-Modus, Labels, Zeitplaner, Großdatei-Bereinigung |

---

## Projekt-Familien

### Dokumenten-Lesen und Bibliotheken

| Anwendung | Beschreibung |
|---|---|
| [DokuReader](https://github.com/doc-bricks/DokuReader) | Local-First Dokumentenbibliothek mit Themenorganisation, Vorschauen, Lesestatus, PDF-Bündelung und Metadatenexport |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Markdown-Viewer/Editor für sauberes Lesen, Bearbeiten, PDF-Export und Sitzungsübergabe |
| [LitZentrum](https://github.com/doc-bricks/LitZentrum) | Literaturverwaltungs-Suite mit PDF, BibTeX, JSON-Export und forschungsorientierter Strukturierung |
| [MediaBrain](https://github.com/doc-bricks/MediaBrain) | Local-First PySide6 Medienbibliothek mit smarten Playlists, Anbietererkennung, Tags, Blacklist und privater SQLite-Ablage |

### Mail- und Erfassungs-Workflows

| Anwendung | Beschreibung |
|---|---|
| [MailProcessor](https://github.com/doc-bricks/MailProcessor) | System-Tray-Starter für Universal Mail Cleaner, UniversalDocsGrabber und UniversalInvoiceMail |
| [UniversalMailCleaner](https://github.com/doc-bricks/UniversalMailCleaner) | Lokale Gmail- und IMAP-Postfachbereinigung mit Sicherheitsmodi und Zeitplaner-Unterstützung |
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Anhangs-Downloader und Dokumentenarchiv-Ersteller für IMAP/Gmail-Eingang, OCR, PDF-Konvertierung und PWA-Review |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Rechnungs- und Beleg-Erfassungspipeline für lokale Archive, OCR/PDF-Konvertierung, JSON-Export und DATEV-orientierte Workflows |

### PDF, OCR und Export

| Anwendung | Beschreibung |
|---|---|
| [UniversalDocsGrabber](https://github.com/doc-bricks/UniversalDocsGrabber) | Konvertiert heruntergeladene Mail-Dokumente in prüfbares PDF/OCR-Archivmaterial |
| [UniversalInvoiceMail](https://github.com/doc-bricks/UniversalInvoiceMail) | Konvertiert Rechnungs- und Beleg-Mails in PDF/OCR-Archivmaterial und buchhaltungsrelevante Exporte |
| [CleanMarkdown](https://github.com/doc-bricks/CleanMarkdown) | Exportiert Markdown-Lesesitzungen nach PDF und begleitende Webformate |

### Notizen und Agenten-Handoffs

| Anwendung | Beschreibung |
|---|---|
| [llm-note](https://github.com/doc-bricks/llm-note) | Local-First Notizen und Notizbuch-Inboxes für LLM-Agenten, hervorgegangen aus den Notizblock/Denkarium-Mustern von BACH |

---

## Design-Prinzipien

- **Local first:** Dokumente, Mail-Exporte, Indizes und der Lesestatus verbleiben standardmäßig auf dem System des Nutzers.
- **Datenschutzbewusst:** Werkzeuge verzichten auf externe Cloud-Verarbeitung, sofern nicht ausdrücklich ein externer Dienst (wie z. B. Gmail) eingerichtet wurde.
- **Praxisnah:** Jedes Projekt adressiert konkrete, wiederkehrende Arbeitsabläufe: Lesen, Vorschau, Bereinigen, Exportieren, Archivieren und Übergabe.
- **Strukturierte Exporte:** JSON, BibTeX, PDF und Begleitformate sind standardisiert dokumentiert, sodass Daten nahtlos zwischen Desktop-Tools und Automatisierungen transferiert werden können.
- **Verständliche Pflege:** READMEs, Tests und `llms.txt`-Dateien sind für menschliche Entwickler sowie für LLM-Assistenten gleichermaßen optimiert.

---

## Such- und Entdeckungssignale

Empfohlene Suchbegriffe für das öffentliche doc-bricks-Profil sind `local-first document tools`, `Python Dokumentenverwaltung`, `PySide6 PDF OCR`, `DokuReader metadata JSON export`, `MediaBrain smart playlists private SQLite`, `Gmail IMAP attachment downloader`, `Markdown PDF export`, `literature manager GitHub`, `invoice mail OCR DATEV export` und `local-first LLM agent notes`.

---

## Maschinenlesbarer Kontext

Für Crawler und LLM-Werkzeuge steht [`llms.txt`](https://github.com/doc-bricks/.github/blob/main/llms.txt) zur Verfügung. Dort sind die kanonischen Repositories, Projektrollen und bevorzugten Suchbegriffe der Organisation doc-bricks dokumentiert.

---

## Ökosystem

doc-bricks ist der Zweig für Dokumentenarbeit innerhalb der Bricks-Suite:

[open-bricks](https://github.com/open-bricks) | [file-bricks](https://github.com/file-bricks) | [dev-bricks](https://github.com/dev-bricks)

Teil des [ellmos-ai](https://github.com/ellmos-ai)-Ökosystems: [llm-note](https://github.com/doc-bricks/llm-note) wurde aus den Notizblock/Denkarium-Mustern von [ellmos-ai/bach](https://github.com/ellmos-ai/bach) ausgegliedert und ist als eigenständiger Agenten-Notiz-Skill einsetzbar.

---

## Verwandte Projekte (andere Organisationen)

| Projekt | Beschreibung |
|---|---|
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Mehrsprachiger Knowledge-Stub-Datensatz (630 Begriffe, 12 Domänen, DE/EN + es/ja/ru/zh) mit Web-Publisher — als eigenständiges Wiki-Modul einsetzbar |
