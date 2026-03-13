# 🧪 Test du Workflow

## Test rapide du script start.sh

```bash
cd convert-drive-sheets
bash start.sh
```

**Le script demande :**

1. 📁 ID du dossier Google Drive
   - Exemple : `1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT`

2. 🤖 Mode automatique ?
   - `o` = Oui (pas de confirmation)
   - `n` = Non (demande confirmation avant conversion)

---

## Workflow complet

### 1. Installation (une seule fois)

```bash
bash install.sh
```

### 2. Configuration credentials

Renommer et éditer :
```bash
cp google-service-account.json.example google-service-account.json
# Éditer avec vos vraies credentials
```

### 3. Partager le dossier Drive

- Partager avec l'email du service account
- Permissions : Éditeur

### 4. Lancement

```bash
bash start.sh
```

---

## Test avec Git

```bash
# Initialiser le repo
git init

# Vérifier le .gitignore
git status

# Le fichier google-service-account.json ne doit PAS apparaître !

# Commit initial
git add .
git commit -m "Initial commit - Convertisseur Drive"
```

---

## Fichiers ignorés par Git

Le `.gitignore` protège automatiquement :

- ✅ `google-service-account.json` (credentials)
- ✅ `venv/` (environnement virtuel)
- ✅ `__pycache__/` (Python cache)
- ✅ `.DS_Store` (macOS)
- ✅ `*.log` (logs)

**Résultat :** Vous pouvez versionner le code sans risque de fuiter vos credentials ! 🔒

---

**Auteur :** Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28
