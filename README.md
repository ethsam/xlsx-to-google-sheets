<p align="center">
  <h1 align="center">Drive to Sheets Converter</h1>
  <p align="center">
    Automatically convert Excel, CSV, TSV, and ODS files from Google Drive to native Google Sheets — with recursive folder support.
  </p>
  <p align="center">
    <a href="README.fr.md">Lire en Francais</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Google%20Drive-API%20v3-4285F4.svg" alt="Google Drive API v3">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg" alt="Platform">
</p>

---

## Features

- **Recursive folder exploration** — traverses entire folder hierarchies automatically
- **Multiple formats** — Excel (.xlsx, .xls), CSV, TSV, ODS
- **Two auth methods** — Service Account (automation) or OAuth 2.0 (personal use)
- **Non-destructive** — original files are always preserved
- **Smart detection** — skips files that are already Google Sheets
- **Interactive or batch mode** — manual confirmation or `--yes` for automation
- **Detailed reporting** — success/failure counts after conversion

## Supported Formats

| Format | Extension | MIME Type |
|--------|-----------|-----------|
| Excel (modern) | `.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel (legacy) | `.xls` | `application/vnd.ms-excel` |
| CSV | `.csv` | `text/csv` |
| TSV | `.tsv` | `text/tab-separated-values` |
| OpenDocument | `.ods` | `application/vnd.oasis.opendocument.spreadsheet` |

---

## Quick Start

```bash
# 1. Clone & install
git clone git@github.com:ethsam/xlsx-to-google-sheets.git
cd convert-drive-sheets
bash install.sh

# 2. Add your credentials (see Authentication below)
cp google-service-account.json.example google-service-account.json

# 3. Run
bash start.sh
```

---

## Authentication

### Option A: Service Account (recommended for automation)

Best for: cron jobs, servers, CI/CD pipelines, production use.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or select existing)
3. Enable the **Google Drive API**
4. Go to **IAM & Admin > Service Accounts** and create one
5. Download the JSON key file
6. Rename it to `google-service-account.json` and place it in the project root
7. **Share your Drive folder** with the service account email (as Editor)

```bash
python3 convert_drive_to_sheets.py FOLDER_ID --yes
```

### Option B: OAuth 2.0 (for personal use)

Best for: one-time use, personal accounts, no folder sharing needed.

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create **OAuth 2.0 credentials** (Desktop application)
3. Download and rename to `credentials_oauth.json`
4. On first run, a browser window opens for authentication
5. Token is cached in `token.pickle` for subsequent runs

```bash
python3 convert_drive_to_sheets_oauth.py FOLDER_ID --yes
```

### Which one should I use?

| | Service Account | OAuth 2.0 |
|---|---|---|
| **Best for** | Automation, servers | Personal, one-time use |
| **Setup** | JSON key file | Browser login |
| **Folder sharing** | Required | Not needed |
| **Token refresh** | Automatic | Cached (auto-refresh) |
| **Headless servers** | Yes | No (needs browser) |

---

## Usage

### Interactive mode

```bash
bash start.sh
```

The script will prompt you for:
- The Google Drive folder ID
- Whether to run in automatic mode

### Command line

```bash
# Service Account
python3 convert_drive_to_sheets.py FOLDER_ID [--yes]

# OAuth
python3 convert_drive_to_sheets_oauth.py FOLDER_ID [--yes]
```

**Flags:**
- `FOLDER_ID` — the Google Drive folder ID (required)
- `--yes` / `-y` — skip confirmation prompt (batch mode)

### Finding a folder ID

```
https://drive.google.com/drive/folders/1aBcDeFgHiJkLmNoPqRsTuVwXyZ
                                        └──────────┬──────────────┘
                                              This is the ID
```

---

## Project Structure

```
convert-drive-sheets/
├── convert_drive_to_sheets.py          # Main script (Service Account)
├── convert_drive_to_sheets_oauth.py    # OAuth version
├── install.sh                          # Automated installer
├── start.sh                            # Interactive launcher
├── google-service-account.json.example # Service Account template
├── credentials_oauth.json.example      # OAuth template
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
├── README.md                           # Documentation (English)
└── README.fr.md                        # Documentation (French)
```

---

## How It Works

```
                    ┌─────────────────┐
                    │  Google Drive    │
                    │  Folder ID      │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Authenticate   │
                    │  (SA or OAuth)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Recursive      │
                    │  Exploration    │◄──── Handles subfolders
                    └────────┬────────┘      & pagination
                             │
                    ┌────────▼────────┐
                    │  Classify       │
                    │  Files          │──── Skip existing Sheets
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  User           │
                    │  Confirmation   │──── or --yes flag
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Convert via    │
                    │  Drive API      │──── files().copy()
                    └────────┬────────┘     with Sheets MIME
                             │
                    ┌────────▼────────┐
                    │  Report         │
                    │  Results        │
                    └─────────────────┘
```

The conversion uses the Google Drive API `files().copy()` method, changing the MIME type to `application/vnd.google-apps.spreadsheet`. The converted file is placed in the same folder as the original. **Original files are never modified or deleted.**

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `source venv/bin/activate` then `pip install -r requirements.txt` |
| `Permission denied` (Service Account) | Share the Drive folder with the service account email as **Editor** |
| `Quota exceeded` | Free up Drive storage or use OAuth version with a different account |
| OAuth browser doesn't open | Delete `token.pickle` and run again |
| `File not found: google-service-account.json` | Copy the example file and fill in your credentials |

---

## Security

> **Never commit credential files to git.** The `.gitignore` is configured to exclude:
> - `google-service-account.json`
> - `credentials_oauth.json`
> - `token.pickle` / `token.json`
> - All `*.json` files (except examples)

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Samuel ETHEVE**
- Email: setheve@viceversa.re
- Web: [viceversa.re](https://www.viceversa.re)

Built in Reunion Island (974)
