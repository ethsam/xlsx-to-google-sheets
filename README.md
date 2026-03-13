# 📊 Convertisseur Excel → Google Sheets

Convertit automatiquement tous les fichiers Excel/CSV d'un dossier Google Drive en Google Sheets.

**Par Samuel ETHEVE** | setheve@viceversa.re | 0692 38 00 28

---

## 🚀 Démarrage rapide (3 commandes)

```bash
bash install.sh                    # 1. Installer
cp google-service-account.json.example google-service-account.json  # 2. Configurer
bash start.sh                      # 3. Lancer
```

---

## 🎯 Quelle version utiliser ?

### Service Account (recommandé)
✅ **Utilisez le script normal** `convert_drive_to_sheets.py`

**Quand ?**
- Automation (cron, serveur)
- Scripts automatiques
- Production

**Prérequis :**
- Fichier `google-service-account.json`
- Partager le dossier Drive avec le service account

### OAuth (optionnel)
✅ **Utilisez** `convert_drive_to_sheets_oauth.py`

**Quand ?**
- Usage personnel ponctuel
- Vous ne voulez pas partager le dossier
- Vous avez plus d'espace sur votre compte perso

**Prérequis :**
- Fichier `credentials_oauth.json`
- Navigateur (connexion 1ère fois)

---

## 📦 Installation

### 1. Créer l'environnement

```bash
bash install.sh
```

### 2. Configurer les credentials

**Service Account :**
```bash
cp google-service-account.json.example google-service-account.json
# Éditer avec vos vraies credentials
```

**OU OAuth :**
```bash
cp credentials_oauth.json.example credentials_oauth.json
# Éditer avec vos vraies credentials
```

### 3. Partager le dossier Drive (Service Account uniquement)

1. Ouvrir le dossier dans Google Drive
2. Clic droit → Partager
3. Ajouter l'email du service account (dans le JSON)
4. Permissions : Éditeur

---

## ▶️ Utilisation

### Méthode 1 : Script interactif (le plus simple)

```bash
bash start.sh
```

Le script demande :
- L'ID du dossier Drive
- Mode auto (oui/non)

### Méthode 2 : Ligne de commande

**Service Account :**
```bash
python3 convert_drive_to_sheets.py FOLDER_ID --yes
```

**OAuth :**
```bash
python3 convert_drive_to_sheets_oauth.py FOLDER_ID --yes
```

**Trouver l'ID du dossier :**
```
https://drive.google.com/drive/folders/1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT
                                          └─────────────┬─────────────┘
                                                        ID du dossier
```

---

## 🔧 Dépannage

**"Module not found" ?**
```bash
source venv/bin/activate
pip install google-auth google-auth-oauthlib google-api-python-client
```

**"Permission denied" (Service Account) ?**
→ Partagez le dossier Drive avec l'email du service account

**"Quota exceeded" ?**
→ Libérez de l'espace Drive ou utilisez la version OAuth

**OAuth : navigateur ne s'ouvre pas ?**
```bash
rm token.pickle
python3 convert_drive_to_sheets_oauth.py FOLDER_ID
```

---

## 📁 Fichiers

```
convert-drive-sheets/
├── convert_drive_to_sheets.py          # ← Service Account (principal)
├── convert_drive_to_sheets_oauth.py    # ← OAuth (optionnel)
├── start.sh                            # ← Lancement interactif
├── install.sh                          # ← Installation auto
├── google-service-account.json         # ← Vos credentials
└── credentials_oauth.json              # ← OAuth (si besoin)
```

---

## 📞 Support

**Samuel ETHEVE**  
📧 setheve@viceversa.re  
📱 0692 38 00 28  
🌐 www.viceversa.re

Viceversa — Solutions Digitales | La Réunion (974)

---

## 🔒 Sécurité

⚠️ **Ne jamais commiter les fichiers credentials** (protégés par `.gitignore`)

---

**Développé avec ❤️ à La Réunion | Version 1.0 | Mars 2026**
