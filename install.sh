#!/bin/bash
################################################################################
# Automated Installer / Script d'installation automatique
# Drive to Sheets Converter / Convertisseur Drive vers Sheets
#
# Author / Auteur: Samuel ETHEVE
# Email: setheve@viceversa.re
################################################################################

echo "================================================================================"
echo "INSTALLATION - Drive → Google Sheets Converter / Convertisseur"
echo "By / Par Samuel ETHEVE | setheve@viceversa.re"
echo "================================================================================"
echo ""

# Check Python 3 / Verifier Python 3
echo "Checking Python 3 / Verification de Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed / Python 3 n'est pas installe"
    echo "   Install from / Installez via: https://www.python.org/downloads/"
    exit 1
fi
echo "Python 3 found / Python 3 trouve: $(python3 --version)"
echo ""

# Create virtual environment / Creer l'environnement virtuel
echo "Creating virtual environment / Creation de l'environnement virtuel..."
if [ -d "venv" ]; then
    echo "A virtual environment already exists / Un environnement virtuel existe deja"
    read -p "   Recreate it / Le recreer ? (y/o/n): " recreate
    if [ "$recreate" = "o" ] || [ "$recreate" = "oui" ] || [ "$recreate" = "y" ] || [ "$recreate" = "yes" ]; then
        rm -rf venv
        python3 -m venv venv
        echo "Virtual environment recreated / Environnement virtuel recree"
    else
        echo "Keeping existing environment / Conservation de l'environnement existant"
    fi
else
    python3 -m venv venv
    echo "Virtual environment created / Environnement virtuel cree"
fi
echo ""

# Activate virtual environment / Activer l'environnement virtuel
echo "Activating virtual environment / Activation de l'environnement virtuel..."
source venv/bin/activate
echo "Virtual environment activated / Environnement virtuel active"
echo ""

# Install dependencies / Installer les dependances
echo "Installing dependencies / Installation des dependances..."
if [ -f "requirements.txt" ]; then
    pip install --quiet -r requirements.txt
else
    pip install --quiet google-auth google-auth-oauthlib google-api-python-client
fi
echo "Dependencies installed / Dependances installees:"
echo "   - google-auth"
echo "   - google-auth-oauthlib"
echo "   - google-api-python-client"
echo ""

# Check credentials / Verifier les credentials
echo "Checking credentials / Verification des credentials..."
if [ -f "google-service-account.json" ]; then
    echo "google-service-account.json found / trouve"
else
    echo "google-service-account.json missing / manquant"
    echo "   Place this file in the folder before continuing"
    echo "   Placez ce fichier dans le dossier avant de continuer"
fi
echo ""

echo "================================================================================"
echo "INSTALLATION COMPLETE / INSTALLATION TERMINEE"
echo "================================================================================"
echo ""
echo "Next steps / Prochaines etapes:"
echo ""
echo "1. Share your Google Drive folder with the service account"
echo "   Partagez votre dossier Google Drive avec le service account"
echo "   -> Open folder in Drive / Ouvrir le dossier Drive"
echo "   -> Right-click -> Share / Clic droit -> Partager"
echo "   -> Add service account email (from JSON) / Ajouter l'email du SA"
echo "   -> Permissions: Editor / Editeur"
echo ""
echo "2. Run the script / Lancer le script:"
echo "   bash start.sh"
echo ""
echo "================================================================================"
