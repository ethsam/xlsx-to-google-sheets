# 🚀 Démarrage Rapide

## Installation en 3 étapes

### 1️⃣ Créer l'environnement virtuel

```bash
cd convert-drive-sheets
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OU
venv\Scripts\activate  # Windows
```

**OU** utilisez le script automatique :
```bash
bash install.sh
```

### 2️⃣ Configurer les credentials

1. Renommez `google-service-account.json.example` en `google-service-account.json`
2. Remplacez le contenu par vos vraies credentials Google Cloud

### 3️⃣ Partager le dossier Drive

1. Ouvrez votre dossier Google Drive
2. Clic droit → **Partager**
3. Ajoutez l'email du service account (dans `google-service-account.json`)
4. Permissions : **Éditeur**

---

## Lancement (3 méthodes)

### Méthode 1 : Script interactif (le plus simple) ✨

```bash
bash start.sh
```

Le script demande :
- 📁 L'ID du dossier Drive
- 🤖 Mode automatique (oui/non)

### Méthode 2 : Ligne de commande

```bash
source venv/bin/activate
python3 convert_drive_to_sheets.py FOLDER_ID --yes
```

### Méthode 3 : Mode interactif

```bash
source venv/bin/activate
python3 convert_drive_to_sheets.py FOLDER_ID
```

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

## ⚠️ Avant de commencer

✅ Python 3 installé  
✅ Fichier `google-service-account.json` présent  
✅ Dossier Drive partagé avec le service account  
✅ **Espace de stockage suffisant** sur Google Drive  

---

## 🐛 Problème ?

**Erreur "Module not found" ?**
```bash
source venv/bin/activate
pip install google-auth google-api-python-client
```

**Erreur "Permission denied" ?**  
→ Partagez le dossier Drive avec le service account (Éditeur)

**Erreur "Quota exceeded" ?**  
→ Libérez de l'espace ou passez à Google One

**Erreur "Usage: ... FOLDER_ID" ?**  
→ Utilisez `bash start.sh` (interactif) ou fournissez l'ID :
```bash
python3 convert_drive_to_sheets.py 1aettJQjng2Vm1gOiaibinN8jP4CQZ0IT
```

---

## 📁 Versionner avec Git

```bash
git init
git add .
git commit -m "Initial commit"
```

⚠️ Le `.gitignore` protège automatiquement vos credentials !

---

📚 **Documentation complète :** `README.md`  
📞 **Support :** Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28
