#!/bin/bash
################################################################################
# Script de lancement - Convertisseur Drive → Google Sheets
#
# Auteur: Samuel ETHEVE
# Email: setheve@viceversa.re
# Tél: 0692 38 00 28
################################################################################

echo "================================================================================"
echo "CONVERTISSEUR DRIVE → GOOGLE SHEETS"
echo "Par Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28"
echo "================================================================================"
echo ""

# Vérifier que l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "⚠️  Environnement virtuel non trouvé"
    echo "   Lancer d'abord: bash install.sh"
    exit 1
fi

# Vérifier le fichier credentials
if [ ! -f "google-service-account.json" ]; then
    echo "❌ Fichier google-service-account.json manquant"
    echo "   Placez ce fichier dans le dossier avant de continuer"
    exit 1
fi

# Demander l'ID du dossier Drive
echo "📁 ID du dossier Google Drive à convertir"
echo ""
echo "💡 Pour trouver l'ID :"
echo "   1. Ouvrez votre dossier dans Google Drive"
echo "   2. L'URL ressemble à: https://drive.google.com/drive/folders/ID_ICI"
echo "   3. Copiez la partie après /folders/"
echo ""
read -p "🔑 Entrez l'ID du dossier: " FOLDER_ID

# Vérifier que l'ID n'est pas vide
if [ -z "$FOLDER_ID" ]; then
    echo "❌ ID du dossier requis"
    exit 1
fi

echo ""
echo "📊 ID du dossier: $FOLDER_ID"
echo ""

# Demander le mode (interactif ou auto)
read -p "🤖 Mode automatique (pas de confirmation) ? (o/n): " AUTO_MODE

# Activer l'environnement virtuel
source venv/bin/activate

# Lancer le script avec l'ID
if [ "$AUTO_MODE" = "o" ] || [ "$AUTO_MODE" = "oui" ]; then
    echo ""
    echo "🚀 Lancement en mode automatique..."
    echo ""
    python3 convert_drive_to_sheets.py "$FOLDER_ID" --yes
else
    echo ""
    echo "🚀 Lancement en mode interactif..."
    echo ""
    python3 convert_drive_to_sheets.py "$FOLDER_ID"
fi
