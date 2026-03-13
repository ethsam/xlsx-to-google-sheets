#!/bin/bash
################################################################################
# Interactive Launcher / Lanceur interactif
# Drive to Sheets Converter / Convertisseur Drive vers Sheets
#
# Author / Auteur: Samuel ETHEVE
# Email: setheve@viceversa.re
################################################################################

echo "================================================================================"
echo "DRIVE → GOOGLE SHEETS CONVERTER / CONVERTISSEUR"
echo "By / Par Samuel ETHEVE | setheve@viceversa.re"
echo "================================================================================"
echo ""

# Check virtual environment / Verifier l'environnement virtuel
if [ ! -d "venv" ]; then
    echo "Virtual environment not found / Environnement virtuel non trouve"
    echo "   Run first / Lancez d'abord: bash install.sh"
    exit 1
fi

# Check credentials / Verifier les credentials
if [ ! -f "google-service-account.json" ]; then
    echo "File missing / Fichier manquant: google-service-account.json"
    echo "   Place this file in the project folder before continuing"
    echo "   Placez ce fichier dans le dossier avant de continuer"
    exit 1
fi

# Ask for Drive folder ID / Demander l'ID du dossier Drive
echo "Google Drive folder ID to convert / ID du dossier Google Drive a convertir"
echo ""
echo "How to find the ID / Comment trouver l'ID :"
echo "   1. Open your folder in Google Drive / Ouvrez votre dossier dans Google Drive"
echo "   2. URL looks like / L'URL ressemble a: https://drive.google.com/drive/folders/ID_HERE"
echo "   3. Copy the part after /folders/ / Copiez la partie apres /folders/"
echo ""
read -p "Enter folder ID / Entrez l'ID du dossier: " FOLDER_ID

# Check ID is not empty / Verifier que l'ID n'est pas vide
if [ -z "$FOLDER_ID" ]; then
    echo "Folder ID required / ID du dossier requis"
    exit 1
fi

echo ""
echo "Folder ID / ID du dossier: $FOLDER_ID"
echo ""

# Ask for mode / Demander le mode
read -p "Automatic mode / Mode automatique (no confirmation) ? (y/o/n): " AUTO_MODE

# Activate virtual environment / Activer l'environnement virtuel
source venv/bin/activate

# Run script / Lancer le script
if [ "$AUTO_MODE" = "o" ] || [ "$AUTO_MODE" = "oui" ] || [ "$AUTO_MODE" = "y" ] || [ "$AUTO_MODE" = "yes" ]; then
    echo ""
    echo "Starting in automatic mode / Lancement en mode automatique..."
    echo ""
    python3 convert_drive_to_sheets.py "$FOLDER_ID" --yes
else
    echo ""
    echo "Starting in interactive mode / Lancement en mode interactif..."
    echo ""
    python3 convert_drive_to_sheets.py "$FOLDER_ID"
fi
