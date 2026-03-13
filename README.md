# 📊 Convertisseur Google Drive → Google Sheets

Script Python professionnel pour convertir automatiquement tous les fichiers Excel/CSV d'un dossier Google Drive en Google Sheets, avec exploration récursive des sous-dossiers.

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
✅ **Script interactif** qui demande l'ID du dossier Drive  
✅ Interface en ligne de commande moderne  
✅ Mode automatique avec `--yes`  
✅ Validation avant conversion  
✅ Rapport détaillé de conversion  
✅ Gestion d'erreurs complète  

---

## 📋 Prérequis

### 1. Python 3

Vérifiez que Python 3 est installé :

```bash
python3 --version
```

Si absent, installez-le via [python.org](https://www.python.org/downloads/)

### 2. Service Account Google Cloud

Créez un service account avec accès à l'API Google Drive :

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un projet (ou utilisez un existant)
3. Activez l'API Google Drive
4. Créez un service account
5. Téléchargez le fichier JSON de credentials
6. Renommez-le en `google-service-account.json`

### 3. Partager le dossier Drive

**Important :** Le service account doit avoir accès au dossier Drive

1. Ouvrez votre dossier Google Drive cible
2. Clic droit → **Partager**
3. Ajoutez l'email du service account (trouvé dans le fichier JSON)
4. Permissions : **Éditeur**
5. Confirmez le partage

### 4. Espace de stockage suffisant

⚠️ **Assurez-vous d'avoir assez d'espace sur votre Google Drive**

Le script crée des **copies** des fichiers au format Google Sheets. Si votre quota est dépassé, les conversions échoueront.

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
pip install google-auth google-api-python-client
```

---

## 🎯 Utilisation

### Méthode 1 : Script de lancement interactif (recommandé)

```bash
bash start.sh
```

Le script va demander :
1. 📁 **L'ID du dossier Drive** à convertir
2. 🤖 **Mode automatique** (oui/non)

**💡 Trouver l'ID du dossier :**
- Ouvrez votre dossier dans Google Drive
- L'URL ressemble à : `https://drive.google.com/drive/folders/1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT`
- L'ID est la partie après `/folders/` : `1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT`

### Méthode 2 : Ligne de commande directe

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
├── convert_drive_to_sheets.py    # Script principal
├── install.sh                     # Installation automatique
├── start.sh                       # Lancement interactif
├── google-service-account.json    # Credentials (à fournir)
├── google-service-account.json.example  # Exemple
├── README.md                      # Ce fichier
├── QUICKSTART.md                  # Démarrage rapide
├── CONTACT.md                     # Coordonnées support
├── LICENSE.txt                    # Licence
├── .gitignore                     # Git ignore
└── venv/                          # Environnement virtuel
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
- `__pycache__/` - Fichiers Python compilés
- `.DS_Store` - Fichiers système macOS

⚠️ **Ne jamais commiter le fichier `google-service-account.json` !**

---

## 🐛 Dépannage

### "Module not found: googleapiclient"

**Solution :**
```bash
source venv/bin/activate
pip install google-auth google-api-python-client
```

### "Permission denied" / "403 Forbidden"

**Cause :** Le service account n'a pas accès au dossier Drive

**Solution :**
1. Ouvrez le dossier Drive dans votre navigateur
2. Clic droit → Partager
3. Ajoutez l'email du service account avec permissions **Éditeur**

### "0 éléments trouvés"

**Cause :** Le service account n'a pas accès au dossier

**Solution :** Vérifiez que le dossier est bien partagé avec le service account

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

3. **Alternative :** Supprimer les fichiers `.xlsx` après conversion

### "Usage: python3 convert_drive_to_sheets.py FOLDER_ID"

**Cause :** ID du dossier non fourni

**Solution :** Utilisez `bash start.sh` ou fournissez l'ID :
```bash
python3 convert_drive_to_sheets.py 1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT
```

---

## 🔧 Commandes utiles

### Désactiver l'environnement virtuel

```bash
deactivate
```

### Réinstaller les dépendances

```bash
source venv/bin/activate
pip install --upgrade google-auth google-api-python-client
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

---

## 🔒 Sécurité

- ✅ Utilisez un service account dédié avec permissions limitées
- ❌ Ne partagez **jamais** votre fichier `google-service-account.json`
- ✅ Ajoutez `google-service-account.json` au `.gitignore`
- ✅ Vérifiez les permissions du dossier Drive avant conversion
- ✅ Testez sur un petit échantillon avant conversion massive
- ✅ L'environnement virtuel Python isole les dépendances
- ✅ Le fichier `.gitignore` protège vos credentials

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

**Développé avec ❤️ à La Réunion (974)**

**Version:** 1.0 | **Mars 2026** | **Python 3.x**
