#!/usr/bin/env python3
"""
================================================================================
CONVERTISSEUR GOOGLE DRIVE → GOOGLE SHEETS (OAuth)
================================================================================

Version OAuth qui utilise votre compte Google personnel.
Plus besoin de service account !

--------------------------------------------------------------------------------
AUTEUR:
    Samuel ETHEVE
    Chef de Projet Digital & Développeur
    
CONTACT:
    Email:      setheve@viceversa.re
    Téléphone:  0692 38 00 28
    Web:        www.viceversa.re
    
ENTREPRISE:
    Viceversa
    Solutions Digitales sur-mesure
    La Réunion (974)
    
DATE DE CRÉATION:
    Mars 2026
    
LICENCE:
    © 2026 Samuel ETHEVE - Tous droits réservés
================================================================================
"""

import os
import sys
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ============================================================================
# CONFIGURATION
# ============================================================================

# Scopes OAuth (permissions demandées)
SCOPES = ['https://www.googleapis.com/auth/drive']

# Fichier de stockage du token
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(SCRIPT_DIR, 'token.pickle')

# ============================================================================
# FONCTIONS
# ============================================================================

            # Charger les credentials OAuth depuis le fichier
            creds_file = os.path.join(SCRIPT_DIR, "credentials_oauth.json")
            if not os.path.exists(creds_file):
                print("❌ Fichier credentials_oauth.json manquant")
                print("   Créez vos credentials OAuth sur Google Cloud Console")
                print("   Documentation: README.md section OAuth")
                sys.exit(1)
            
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            print("🔐 Première utilisation - Authentification requise")
            print("   Un navigateur va s'ouvrir pour vous connecter")
            print("")
            
            # Créer les credentials OAuth inline (pas besoin de fichier JSON)
            client_config = {
                "installed": {
                    "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
                    "project_id": "YOUR_PROJECT_ID",
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_secret": "YOUR_CLIENT_SECRET",
                    "redirect_uris": ["http://localhost"]
                }
            }
            
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Sauvegarder le token pour les prochaines fois
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
        print("✅ Authentification réussie - Token sauvegardé\n")
    
    return build('drive', 'v3', credentials=creds)

def list_all_files(service, folder_id, path=""):
    """Lister récursivement tous les fichiers et dossiers"""
    results = []
    
    query = f"'{folder_id}' in parents and trashed=false"
    page_token = None
    
    while True:
        try:
            response = service.files().list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, parents)",
                pageToken=page_token,
                pageSize=1000
            ).execute()
            
            items = response.get('files', [])
            
            for item in items:
                item_path = f"{path}/{item['name']}" if path else item['name']
                item['path'] = item_path
                results.append(item)
                
                # Si c'est un dossier, explorer récursivement
                if item['mimeType'] == 'application/vnd.google-apps.folder':
                    print(f"📁 Exploration: {item_path}")
                    sub_results = list_all_files(service, item['id'], item_path)
                    results.extend(sub_results)
            
            page_token = response.get('nextPageToken')
            if not page_token:
                break
                
        except HttpError as e:
            print(f"❌ Erreur HTTP: {e}")
            break
    
    return results

def can_convert_to_sheets(mime_type):
    """Vérifier si le type MIME peut être converti en Sheets"""
    convertible_types = [
        'text/csv',
        'text/tab-separated-values',
        'application/vnd.ms-excel',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.oasis.opendocument.spreadsheet',
        'text/plain',
    ]
    return mime_type in convertible_types

def convert_to_sheet(service, file_id, file_name, parent_folder_id):
    """Convertir un fichier en Google Sheet dans le même dossier parent"""
    try:
        new_file = {
            'name': file_name,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [parent_folder_id]
        }
        
        converted = service.files().copy(
            fileId=file_id,
            body=new_file
        ).execute()
        
        print(f"  ✅ Converti: {file_name} → {converted['id']}")
        return converted
        
    except HttpError as e:
        print(f"  ❌ Erreur conversion {file_name}: {e}")
        return None

# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

def main():
    """Programme principal"""
    if len(sys.argv) < 2:
        print("❌ Usage: python3 convert_drive_to_sheets_oauth.py FOLDER_ID [--yes]")
        print("")
        print("💡 Pour trouver l'ID du dossier:")
        print("   1. Ouvrez votre dossier dans Google Drive")
        print("   2. L'URL ressemble à: https://drive.google.com/drive/folders/ID_ICI")
        print("   3. L'ID est la partie après /folders/")
        print("")
        print("📞 Support: Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28")
        sys.exit(1)
    
    folder_id = sys.argv[1]
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv
    
    print("="*80)
    print("CONVERTISSEUR DRIVE → GOOGLE SHEETS (OAuth)")
    print("Par Samuel ETHEVE | setheve@viceversa.re | 0692 38 00 28")
    print("="*80)
    print(f"\n📁 Dossier cible: {folder_id}")
    print("🔐 Méthode: OAuth (compte Google personnel)\n")
    
    service = get_drive_service()
    
    print("\n🔍 Exploration du Drive...\n")
    
    all_files = list_all_files(service, folder_id)
    
    print(f"\n📊 {len(all_files)} éléments trouvés\n")
    
    convertible = [f for f in all_files if can_convert_to_sheets(f['mimeType'])]
    sheets = [f for f in all_files if f['mimeType'] == 'application/vnd.google-apps.spreadsheet']
    folders = [f for f in all_files if f['mimeType'] == 'application/vnd.google-apps.folder']
    
    print(f"📁 Dossiers: {len(folders)}")
    print(f"📊 Google Sheets existants: {len(sheets)}")
    print(f"📄 Fichiers convertibles: {len(convertible)}\n")
    
    if convertible:
        print("Fichiers à convertir:")
        for f in convertible:
            print(f"  - {f['path']}")
        
        print(f"\n⚠️  CONVERSION DE {len(convertible)} FICHIERS")
        
        if auto_confirm:
            response = 'oui'
            print("Mode auto-confirmation activé (--yes)")
        else:
            try:
                response = input("Continuer? (oui/non): ")
            except EOFError:
                print("\n⚠️  Pas d'entrée interactive détectée")
                print("💡 Utilisez --yes pour confirmer automatiquement")
                return
        
        if response.lower() in ['oui', 'o', 'yes', 'y']:
            print("\n🔄 Conversion en cours...\n")
            success_count = 0
            error_count = 0
            
            for f in convertible:
                parent_id = f['parents'][0] if f.get('parents') else folder_id
                result = convert_to_sheet(service, f['id'], f['name'], parent_id)
                if result:
                    success_count += 1
                else:
                    error_count += 1
            
            print("\n" + "="*80)
            print(f"✅ Conversion terminée!")
            print(f"   - Succès: {success_count}")
            print(f"   - Erreurs: {error_count}")
            print("="*80)
            print("Script développé par Samuel ETHEVE - Viceversa")
            print("Contact: setheve@viceversa.re | 0692 38 00 28")
            print("="*80)
        else:
            print("❌ Annulé")
    else:
        print("✅ Aucun fichier à convertir")

if __name__ == '__main__':
    main()
