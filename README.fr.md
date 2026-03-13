<p align="center">
  <h1 align="center">Convertisseur Drive vers Sheets</h1>
  <p align="center">
    Convertit automatiquement les fichiers Excel, CSV, TSV et ODS de Google Drive en Google Sheets natifs — avec exploration recursive des dossiers.
  </p>
  <p align="center">
    <a href="README.md">Read in English</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Google%20Drive-API%20v3-4285F4.svg" alt="Google Drive API v3">
  <img src="https://img.shields.io/badge/licence-MIT-green.svg" alt="Licence MIT">
  <img src="https://img.shields.io/badge/plateforme-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg" alt="Plateforme">
</p>

---

## Fonctionnalites

- **Exploration recursive** — parcourt automatiquement toutes les sous-arborescences
- **Formats multiples** — Excel (.xlsx, .xls), CSV, TSV, ODS
- **Deux methodes d'authentification** — Service Account (automation) ou OAuth 2.0 (usage personnel)
- **Non destructif** — les fichiers originaux sont toujours preserves
- **Detection intelligente** — ignore les fichiers deja au format Google Sheets
- **Mode interactif ou batch** — confirmation manuelle ou `--yes` pour l'automatisation
- **Rapport detaille** — nombre de succes/erreurs apres conversion

## Formats Supportes

| Format | Extension | Type MIME |
|--------|-----------|-----------|
| Excel (moderne) | `.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel (ancien) | `.xls` | `application/vnd.ms-excel` |
| CSV | `.csv` | `text/csv` |
| TSV | `.tsv` | `text/tab-separated-values` |
| OpenDocument | `.ods` | `application/vnd.oasis.opendocument.spreadsheet` |

---

## Demarrage Rapide

```bash
# 1. Cloner & installer
git clone git@github.com:ethsam/xlsx-to-google-sheets.git
cd convert-drive-sheets
bash install.sh

# 2. Ajouter vos credentials (voir Authentification ci-dessous)
cp google-service-account.json.example google-service-account.json

# 3. Lancer
bash start.sh
```

---

## Authentification

### Option A : Service Account (recommande pour l'automatisation)

Ideal pour : taches cron, serveurs, pipelines CI/CD, production.

1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Creer un projet (ou en selectionner un existant)
3. Activer l'**API Google Drive**
4. Aller dans **IAM & Admin > Comptes de service** et en creer un
5. Telecharger le fichier de cle JSON
6. Le renommer en `google-service-account.json` et le placer a la racine du projet
7. **Partager votre dossier Drive** avec l'email du service account (en tant qu'Editeur)

```bash
python3 convert_drive_to_sheets.py FOLDER_ID --yes
```

### Option B : OAuth 2.0 (pour usage personnel)

Ideal pour : usage ponctuel, comptes personnels, pas besoin de partager le dossier.

1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Creer des **identifiants OAuth 2.0** (Application de bureau)
3. Telecharger et renommer en `credentials_oauth.json`
4. Au premier lancement, une fenetre navigateur s'ouvre pour l'authentification
5. Le token est mis en cache dans `token.pickle` pour les lancements suivants

```bash
python3 convert_drive_to_sheets_oauth.py FOLDER_ID --yes
```

### Quelle methode choisir ?

| | Service Account | OAuth 2.0 |
|---|---|---|
| **Ideal pour** | Automatisation, serveurs | Usage personnel, ponctuel |
| **Configuration** | Fichier cle JSON | Connexion navigateur |
| **Partage du dossier** | Obligatoire | Non necessaire |
| **Rafraichissement du token** | Automatique | Cache (auto-rafraichissement) |
| **Serveurs headless** | Oui | Non (necessite un navigateur) |

---

## Utilisation

### Mode interactif

```bash
bash start.sh
```

Le script vous demandera :
- L'ID du dossier Google Drive
- Si vous souhaitez le mode automatique

### Ligne de commande

```bash
# Service Account
python3 convert_drive_to_sheets.py FOLDER_ID [--yes]

# OAuth
python3 convert_drive_to_sheets_oauth.py FOLDER_ID [--yes]
```

**Options :**
- `FOLDER_ID` — l'ID du dossier Google Drive (obligatoire)
- `--yes` / `-y` — passe la confirmation (mode batch)

### Trouver l'ID d'un dossier

```
https://drive.google.com/drive/folders/1aBcDeFgHiJkLmNoPqRsTuVwXyZ
                                        └──────────┬──────────────┘
                                            Voici l'ID
```

---

## Structure du Projet

```
convert-drive-sheets/
├── convert_drive_to_sheets.py          # Script principal (Service Account)
├── convert_drive_to_sheets_oauth.py    # Version OAuth
├── install.sh                          # Installateur automatique
├── start.sh                            # Lanceur interactif
├── google-service-account.json.example # Template Service Account
├── credentials_oauth.json.example      # Template OAuth
├── requirements.txt                    # Dependances Python
├── LICENSE                             # Licence MIT
├── README.md                           # Documentation (Anglais)
└── README.fr.md                        # Documentation (Francais)
```

---

## Fonctionnement

```
                    ┌─────────────────┐
                    │  Google Drive    │
                    │  ID du Dossier  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Authentification│
                    │  (SA ou OAuth)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Exploration    │
                    │  Recursive      │◄──── Sous-dossiers
                    └────────┬────────┘      & pagination
                             │
                    ┌────────▼────────┐
                    │  Classification │
                    │  des fichiers   │──── Ignore les Sheets existants
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Confirmation   │
                    │  utilisateur    │──── ou flag --yes
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Conversion via │
                    │  API Drive      │──── files().copy()
                    └────────┬────────┘     avec MIME Sheets
                             │
                    ┌────────▼────────┐
                    │  Rapport des    │
                    │  resultats      │
                    └─────────────────┘
```

La conversion utilise la methode `files().copy()` de l'API Google Drive en changeant le type MIME vers `application/vnd.google-apps.spreadsheet`. Le fichier converti est place dans le meme dossier que l'original. **Les fichiers originaux ne sont jamais modifies ni supprimes.**

---

## Depannage

| Probleme | Solution |
|----------|----------|
| `ModuleNotFoundError` | Executez `source venv/bin/activate` puis `pip install -r requirements.txt` |
| `Permission denied` (Service Account) | Partagez le dossier Drive avec l'email du service account en tant qu'**Editeur** |
| `Quota exceeded` | Liberez de l'espace Drive ou utilisez la version OAuth avec un autre compte |
| Le navigateur OAuth ne s'ouvre pas | Supprimez `token.pickle` et relancez |
| `File not found: google-service-account.json` | Copiez le fichier example et remplissez vos credentials |

---

## Securite

> **Ne commitez jamais les fichiers de credentials dans git.** Le `.gitignore` est configure pour exclure :
> - `google-service-account.json`
> - `credentials_oauth.json`
> - `token.pickle` / `token.json`
> - Tous les fichiers `*.json` (sauf les exemples)

---

## Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le depot
2. Creez une branche (`git checkout -b feature/ma-fonctionnalite`)
3. Commitez vos changements
4. Poussez la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une Pull Request

---

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour les details.

---

## Auteur

**Samuel ETHEVE**
- Email : setheve@viceversa.re
- Web : [viceversa.re](https://www.viceversa.re)

Developpe a La Reunion (974)
