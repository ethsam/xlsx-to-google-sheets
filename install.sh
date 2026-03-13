#!/bin/bash
################################################################################
# Script d'installation automatique
# Convertisseur Google Drive → Google Sheets
#
# Auteur: Samuel ETHEVE
# Email: setheve@viceversa.re
# Tél: 0692 38 00 28
################################################################################

echo "================================================================================"
echo "INSTALLATION - Convertisseur Drive → Google Sheets"
echo "Par Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28"
echo "================================================================================"
echo ""

# Vérifier Python 3
echo "🔍 Vérification de Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "   Installez-le via: https://www.python.org/downloads/"
    exit 1
fi
echo "✅ Python 3 trouvé: $(python3 --version)"
echo ""

# Créer l'environnement virtuel
echo "📦 Création de l'environnement virtuel..."
if [ -d "venv" ]; then
    echo "⚠️  Un environnement virtuel existe déjà"
    read -p "   Le recréer ? (o/n): " recreate
    if [ "$recreate" = "o" ] || [ "$recreate" = "oui" ]; then
        rm -rf venv
        python3 -m venv venv
        echo "✅ Environnement virtuel recréé"
    else
        echo "↪️  Conservation de l'environnement existant"
    fi
else
    python3 -m venv venv
    echo "✅ Environnement virtuel créé"
fi
echo ""

# Activer l'environnement virtuel
echo "⚙️  Activation de l'environnement virtuel..."
source venv/bin/activate
echo "✅ Environnement virtuel activé"
echo ""

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install --quiet google-auth google-api-python-client
echo "✅ Dépendances installées:"
echo "   - google-auth"
echo "   - google-api-python-client"
echo ""

# Vérifier le fichier credentials
echo "🔑 Vérification du fichier credentials..."
if [ -f "google-service-account.json" ]; then
    echo "✅ Fichier google-service-account.json trouvé"
else
    echo "⚠️  Fichier google-service-account.json manquant"
    echo "   Placez ce fichier dans le dossier avant de continuer"
fi
echo ""

echo "================================================================================"
echo "✅ INSTALLATION TERMINÉE !"
echo "================================================================================"
echo ""
echo "📋 Prochaines étapes:"
echo ""
echo "1. Partager votre dossier Google Drive avec le service account"
echo "   → Ouvrir le dossier Drive"
echo "   → Clic droit → Partager"
echo "   → Ajouter l'email du service account (dans google-service-account.json)"
echo "   → Permissions: Éditeur"
echo ""
echo "2. Modifier l'ID du dossier dans convert_drive_to_sheets.py si nécessaire"
echo ""
echo "3. Lancer le script:"
echo "   source venv/bin/activate"
echo "   python3 convert_drive_to_sheets.py --yes"
echo ""
echo "================================================================================"
echo "📞 Support: Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28"
echo "================================================================================"
