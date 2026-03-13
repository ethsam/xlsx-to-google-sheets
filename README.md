# 📊 Convertisseur Google Drive → Google Sheets

Script Python professionnel pour convertir automatiquement tous les fichiers Excel/CSV d'un dossier Google Drive en Google Sheets, avec exploration récursive des sous-dossiers.

**2 versions disponibles :** Service Account (automation) ou OAuth (usage personnel)

---

## 👨‍💻 Auteur

**Samuel ETHEVE**  
Chef de Projet Digital & Développeur  

📧 **Email:** setheve@viceversa.re  
📱 **Téléphone:** 0692 38 00 28  
🌐 **Web:** www.viceversa.re  

**Entreprise:** Viceversa  
Solutions Digitales sur-mesure | La Réunion (974)

---

## ✨ Fonctionnalités

✅ Exploration récursive de tous les sous-dossiers  
✅ Conversion automatique Excel (.xlsx, .xls) → Google Sheets  
✅ Support CSV, TSV, ODS  
✅ Conservation des fichiers originaux  
✅ **2 modes d'authentification** : Service Account ou OAuth  
✅ Script interactif qui demande l'ID du dossier Drive  
✅ Interface en ligne de commande moderne  
✅ Mode automatique avec `--yes`  
✅ Validation avant conversion  
✅ Rapport détaillé de conversion  
✅ Gestion d'erreurs complète  

---

## 🔐 Authentification : Service Account vs OAuth

### 📊 Comparaison

| Critère | Service Account | OAuth |
|---------|----------------|-------|
| **Usage** | Automation, serveur, cron | Usage personnel, ponctuel |
| **Authentification** | Fichier JSON unique | Navigateur (première fois) |
| **Partage requis** | ✅ Oui (partager Drive avec service account) | ❌ Non (accès direct à vos dossiers) |
| **Quota Drive** | Service account (15 GB gratuit) | Votre compte personnel |
| **Idéal pour** | Production, scripts automatiques | Tests, usage manuel |

### 🤖 Service Account (recommandé pour production)

**Fichier :** `convert_drive_to_sheets.py`

**Avantages :**
- ✅ Automatisable (cron, serveur)
- ✅ Pas d'intervention humaine
- ✅ Indépendant de votre compte personnel

**Inconvénients :**
- ⚠️ Nécessite de partager le dossier Drive
- ⚠️ Quota limité (15 GB service account gratuit)

### 👤 OAuth (recommandé pour usage personnel)

**Fichier :** `convert_drive_to_sheets_oauth.py`

**Avantages :**
- ✅ Accès direct à tous vos dossiers Drive
- ✅ Utilise votre quota personnel
- ✅ Pas besoin de partager les dossiers

**Inconvénients :**
- ⚠️ Premier lancement : navigateur s'ouvre
- ⚠️ Moins adapté à l'automation

---

## 📋 Prérequis

### 1. Python 3

Vérifiez que Python 3 est installé :

```bash
python3 --version
```

Si absent, installez-le via [python.org](https://www.python.org/downloads/)

### 2a. Service Account Google Cloud (méthode automation)

Créez un service account avec accès à l'API Google Drive :

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un projet (ou utilisez un existant)
3. Activez l'API Google Drive
4. Créez un service account
5. Téléchargez le fichier JSON de credentials
6. Renommez-le en `google-service-account.json`

**Important :** Partagez ensuite vos dossiers Drive avec l'email du service account (permissions Éditeur)

### 2b. OAuth Google Cloud (méthode personnelle)

Créez des credentials OAuth 2.0 :

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un projet (ou utilisez un existant)
3. Activez l'API Google Drive
4. Créez des **credentials OAuth 2.0** (type "Application de bureau")
5. Téléchargez le fichier JSON
6. Renommez-le en `credentials_oauth.json`

**Avantage :** Pas besoin de partager vos dossiers, vous avez déjà accès !

### 3. Espace de stockage suffisant

⚠️ **Assurez-vous d'avoir assez d'espace sur votre Google Drive**

Le script crée des **copies** des fichiers au format Google Sheets.

**Vérifier votre espace :** https://drive.google.com/settings/storage

---

## 🚀 Installation rapide

### Méthode 1 : Script automatique (recommandé)

```bash
cd convert-drive-sheets
bash install.sh
```

Le script va :
- Vérifier Python 3
- Créer l'environnement virtuel
- Installer les dépendances
- Vérifier le fichier credentials

### Méthode 2 : Installation manuelle

```bash
cd convert-drive-sheets

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate  # macOS/Linux
# OU
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install google-auth google-auth-oauthlib google-api-python-client
```

---

## 🎯 Utilisation

### Méthode 1 : Service Account (automation)

#### Via le script interactif :

```bash
bash start.sh
```

Le script demande :
1. 📁 L'ID du dossier Drive
2. 🤖 Mode automatique (oui/non)

#### Via ligne de commande :

```bash
source venv/bin/activate

# Mode interactif (avec confirmation)
python3 convert_drive_to_sheets.py FOLDER_ID

# Mode automatique (sans confirmation)
python3 convert_drive_to_sheets.py FOLDER_ID --yes
```

**Exemple :**
```bash
python3 convert_drive_to_sheets.py 1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT --yes
```

### Méthode 2 : OAuth (usage personnel)

```bash
source venv/bin/activate

# Premier lancement : navigateur s'ouvre pour authentification
python3 convert_drive_to_sheets_oauth.py FOLDER_ID --yes

# Lancements suivants : token sauvegardé, pas de navigateur
python3 convert_drive_to_sheets_oauth.py FOLDER_ID --yes
```

**Avantage OAuth :** Pas besoin de partager le dossier Drive !

---

## 💡 Trouver l'ID du dossier Drive

1. Ouvrez votre dossier dans Google Drive
2. Regardez l'URL dans votre navigateur
3. L'URL ressemble à :
   ```
   https://drive.google.com/drive/folders/1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT
   ```
4. L'ID est la partie après `/folders/` :
   ```
   1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT
   ```

---

## 📂 Exemple d'exécution

```
================================================================================
CONVERTISSEUR DRIVE → GOOGLE SHEETS
Par Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28
================================================================================

📁 Dossier cible: 1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT

🔍 Exploration du Drive...

📁 Exploration: Dossier 1
📁 Exploration: Dossier 2
📁 Exploration: Dossier 3

📊 46 éléments trouvés

📁 Dossiers: 14
📊 Google Sheets existants: 4
📄 Fichiers convertibles: 28

Fichiers à convertir:
  - Dossier 1/fichier1.xlsx
  - Dossier 2/fichier2.xlsx
  ...

⚠️  CONVERSION DE 28 FICHIERS
Continuer? (oui/non): oui

🔄 Conversion en cours...

  ✅ Converti: fichier1.xlsx → 1ABC...
  ✅ Converti: fichier2.xlsx → 1DEF...
  ...

================================================================================
✅ Conversion terminée!
   - Succès: 28
   - Erreurs: 0
================================================================================
Script développé par Samuel ETHEVE - Viceversa
Contact: setheve@viceversa.re | 0692 38 00 28
================================================================================
```

---

## 📂 Formats supportés

| Format | Extension | Type MIME |
|--------|-----------|-----------|
| Excel (nouveau) | `.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel (ancien) | `.xls` | `application/vnd.ms-excel` |
| CSV | `.csv` | `text/csv` |
| TSV | `.tsv` | `text/tab-separated-values` |
| OpenDocument | `.ods` | `application/vnd.oasis.opendocument.spreadsheet` |

---

## 📁 Structure du projet

```
convert-drive-sheets/
├── convert_drive_to_sheets.py         # Version Service Account
├── convert_drive_to_sheets_oauth.py   # Version OAuth (NEW)
├── install.sh                         # Installation automatique
├── start.sh                           # Lancement interactif
├── google-service-account.json        # Credentials Service Account
├── google-service-account.json.example
├── credentials_oauth.json             # Credentials OAuth (à créer)
├── token.pickle                       # Token OAuth sauvegardé
├── README.md                          # Ce fichier
├── QUICKSTART.md                      # Démarrage rapide
├── CONTACT.md                         # Coordonnées support
├── LICENSE.txt                        # Licence
├── .gitignore                         # Git ignore
└── venv/                              # Environnement virtuel
```

---

## 📝 Notes importantes

- ✅ Les fichiers originaux sont **conservés** (pas de suppression)
- ✅ Les Google Sheets créés portent le **même nom** que les fichiers sources
- ✅ Le script **détecte** automatiquement les fichiers déjà convertis
- ✅ Aucune modification des fichiers originaux
- ✅ Conversion par **copie** avec changement de format
- ✅ Les Sheets sont créés **dans le même dossier** que les fichiers sources
- ⚠️ Nécessite de l'**espace de stockage** disponible sur Google Drive

---

## 🔧 Git / Versioning

### Initialiser le dépôt

```bash
cd convert-drive-sheets
git init
git add .
git commit -m "Initial commit - Convertisseur Drive → Sheets"
```

### Fichiers ignorés (.gitignore)

Le fichier `.gitignore` exclut automatiquement :
- `venv/` - Environnement virtuel
- `google-service-account.json` - Credentials (secret !)
- `credentials_oauth.json` - Credentials OAuth
- `token.pickle` - Token OAuth sauvegardé
- `__pycache__/` - Fichiers Python compilés
- `.DS_Store` - Fichiers système macOS

⚠️ **Ne jamais commiter les fichiers de credentials !**

---

## 🐛 Dépannage

### "Module not found: googleapiclient"

**Solution :**
```bash
source venv/bin/activate
pip install google-auth google-auth-oauthlib google-api-python-client
```

### Service Account : "Permission denied" / "403 Forbidden"

**Cause :** Le service account n'a pas accès au dossier Drive

**Solution :**
1. Ouvrez le dossier Drive dans votre navigateur
2. Clic droit → Partager
3. Ajoutez l'email du service account avec permissions **Éditeur**

### OAuth : Navigateur ne s'ouvre pas

**Solution :**
```bash
# Supprimer le token et réessayer
rm token.pickle
python3 convert_drive_to_sheets_oauth.py FOLDER_ID
```

### "0 éléments trouvés"

**Cause Service Account :** Le service account n'a pas accès au dossier

**Cause OAuth :** Vérifiez l'ID du dossier

### "The user's Drive storage quota has been exceeded"

**Cause :** Votre espace Google Drive est plein

**Solutions :**
1. **Libérer de l'espace :**
   - Vider la corbeille Drive
   - Supprimer fichiers volumineux
   - Nettoyer Gmail (pièces jointes)
   - Nettoyer Google Photos

2. **Augmenter le stockage :**
   - Passer à Google One (100 GB → ~2€/mois)
   - https://one.google.com/storage

3. **Alternative OAuth :** Utiliser la version OAuth avec votre compte personnel si vous avez plus d'espace

---

## 🔧 Commandes utiles

### Désactiver l'environnement virtuel

```bash
deactivate
```

### Réinstaller les dépendances

```bash
source venv/bin/activate
pip install --upgrade google-auth google-auth-oauthlib google-api-python-client
```

### Supprimer l'environnement virtuel

```bash
deactivate
rm -rf venv
```

### Tester sur un petit échantillon

```bash
# Créer un dossier de test avec quelques fichiers
# Puis lancer le script en mode interactif pour valider avant
python3 convert_drive_to_sheets.py TEST_FOLDER_ID
```

### Réinitialiser OAuth

```bash
# Supprimer le token sauvegardé
rm token.pickle

# Relancer le script - navigateur s'ouvrira à nouveau
python3 convert_drive_to_sheets_oauth.py FOLDER_ID
```

---

## 🔒 Sécurité

- ✅ Utilisez un service account dédié avec permissions limitées
- ❌ Ne partagez **jamais** vos fichiers credentials
- ✅ Ajoutez tous les fichiers credentials au `.gitignore`
- ✅ Vérifiez les permissions du dossier Drive avant conversion
- ✅ Testez sur un petit échantillon avant conversion massive
- ✅ L'environnement virtuel Python isole les dépendances
- ✅ Le fichier `.gitignore` protège vos credentials
- ✅ OAuth : Le token est sauvegardé localement et protégé

---

## 📞 Support

Pour toute question, assistance ou développement personnalisé :

**Samuel ETHEVE**  
📧 setheve@viceversa.re  
📱 0692 38 00 28  
🌐 www.viceversa.re

### Services disponibles

- 🛠️ **Support technique** - Assistance et dépannage
- 💻 **Développements personnalisés** - Fonctionnalités sur-mesure
- 📚 **Formation** - Formation à l'utilisation du script
- 🔧 **Maintenance** - Mises à jour et évolutions
- 🚀 **Projets digitaux** - Solutions complètes

**Horaires :** Lun-Ven 9h-18h (GMT+4)  
**Délai de réponse :** 24-48h ouvrées

---

## 📄 Licence

© 2026 Samuel ETHEVE - Tous droits réservés

Script développé par **Viceversa** - Solutions Digitales sur-mesure

---

## 🎓 Projets & Références

- **entrepreneur.re** — Média automatisé IA
- **actus.re** — Agrégateur d'actualités automatisé
- **lequotidien.re** — Le Quotidien de La Réunion
- **promotions.re** — Catalogues promotionnels entreprises
- **salonformation.re** — Gestion salon formation

---

**Développé avec ❤️ à La Réunion (974)**

**Version:** 1.0 | **Mars 2026** | **Python 3.x**
