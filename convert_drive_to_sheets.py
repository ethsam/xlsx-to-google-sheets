#!/usr/bin/env python3
"""
================================================================================
DRIVE TO SHEETS CONVERTER / CONVERTISSEUR DRIVE VERS SHEETS
================================================================================

Automatically converts Excel/CSV files to Google Sheets
with recursive subfolder exploration.

Convertit automatiquement les fichiers Excel/CSV en Google Sheets
avec exploration recursive des sous-dossiers.

Author / Auteur: Samuel ETHEVE <setheve@viceversa.re>
License / Licence: MIT
================================================================================
"""

import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDS_PATH = os.path.join(SCRIPT_DIR, 'google-service-account.json')
SCOPES = ['https://www.googleapis.com/auth/drive']

# ============================================================================
# FUNCTIONS / FONCTIONS
# ============================================================================

def get_drive_service():
    """Authenticate and return Drive service / Authentification et service Drive"""
    credentials = service_account.Credentials.from_service_account_file(
        CREDS_PATH, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

def list_all_files(service, folder_id, path=""):
    """Recursively list all files and folders / Lister recursivement tous les fichiers"""
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

                # If folder, explore recursively / Si dossier, explorer recursivement
                if item['mimeType'] == 'application/vnd.google-apps.folder':
                    print(f"  Exploring / Exploration: {item_path}")
                    sub_results = list_all_files(service, item['id'], item_path)
                    results.extend(sub_results)

            page_token = response.get('nextPageToken')
            if not page_token:
                break

        except HttpError as e:
            print(f"  HTTP Error / Erreur HTTP: {e}")
            break

    return results

def can_convert_to_sheets(mime_type):
    """Check if MIME type can be converted to Sheets / Verifier si convertible"""
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
    """Convert a file to Google Sheet in the same parent folder"""
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

        print(f"  Converted / Converti: {file_name} -> {converted['id']}")
        return converted

    except HttpError as e:
        print(f"  Error / Erreur ({file_name}): {e}")
        return None

# ============================================================================
# MAIN / PROGRAMME PRINCIPAL
# ============================================================================

def main():
    """Main program / Programme principal"""
    if len(sys.argv) < 2:
        print("Usage: python3 convert_drive_to_sheets.py FOLDER_ID [--yes]")
        print("")
        print("How to find the folder ID / Comment trouver l'ID du dossier:")
        print("   1. Open your folder in Google Drive / Ouvrez votre dossier")
        print("   2. URL: https://drive.google.com/drive/folders/ID_HERE")
        print("   3. Copy the part after /folders/ / Copiez la partie apres /folders/")
        sys.exit(1)

    folder_id = sys.argv[1]
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    print("=" * 80)
    print("DRIVE -> GOOGLE SHEETS CONVERTER / CONVERTISSEUR")
    print("By / Par Samuel ETHEVE | setheve@viceversa.re")
    print("=" * 80)
    print(f"\nTarget folder / Dossier cible: {folder_id}")
    print("\nScanning Drive / Exploration du Drive...\n")

    service = get_drive_service()

    all_files = list_all_files(service, folder_id)

    print(f"\n{len(all_files)} items found / elements trouves\n")

    convertible = [f for f in all_files if can_convert_to_sheets(f['mimeType'])]
    sheets = [f for f in all_files if f['mimeType'] == 'application/vnd.google-apps.spreadsheet']
    folders = [f for f in all_files if f['mimeType'] == 'application/vnd.google-apps.folder']

    print(f"Folders / Dossiers: {len(folders)}")
    print(f"Existing Sheets / Sheets existants: {len(sheets)}")
    print(f"Convertible files / Fichiers convertibles: {len(convertible)}\n")

    if convertible:
        print("Files to convert / Fichiers a convertir:")
        for f in convertible:
            print(f"  - {f['path']} ({f['mimeType']})")

        print(f"\nCONVERTING {len(convertible)} FILES / CONVERSION DE {len(convertible)} FICHIERS")

        if auto_confirm:
            response = 'yes'
            print("Auto-confirm enabled / Mode auto-confirmation active (--yes)")
        else:
            try:
                response = input("Continue / Continuer? (yes/oui/no/non): ")
            except EOFError:
                print("\nNo interactive input detected / Pas d'entree interactive")
                print("Use --yes to auto-confirm / Utilisez --yes pour confirmer")
                return

        if response.lower() in ['oui', 'o', 'yes', 'y']:
            print("\nConverting / Conversion en cours...\n")
            success_count = 0
            error_count = 0

            for f in convertible:
                parent_id = f['parents'][0] if f.get('parents') else folder_id
                result = convert_to_sheet(service, f['id'], f['name'], parent_id)
                if result:
                    success_count += 1
                else:
                    error_count += 1

            print("\n" + "=" * 80)
            print("Conversion complete / Conversion terminee!")
            print(f"   Success / Succes: {success_count}")
            print(f"   Errors / Erreurs: {error_count}")
            print("=" * 80)
        else:
            print("Cancelled / Annule")
    else:
        print("No files to convert / Aucun fichier a convertir")
        print("   (all files are already Sheets or not convertible)")
        print("   (tous les fichiers sont deja des Sheets ou non-convertibles)")

if __name__ == '__main__':
    main()
