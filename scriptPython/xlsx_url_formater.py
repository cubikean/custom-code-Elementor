import openpyxl
from urllib.parse import urlparse, unquote
import os

def extraire_nom_fichier(url):
    parsed_url = urlparse(url)
    chemin, nom_fichier = os.path.split(parsed_url.path)
    nom_sans_extension, extension = os.path.splitext(nom_fichier)
    return nom_sans_extension

def modifier_urls_colonne(input_path, output_path, colonne_index):
    # Charger le fichier Excel
    workbook = openpyxl.load_workbook(input_path)
    feuille = workbook.active

    # Parcourir les cellules de la colonne spécifiée contenant des URLs
    for row in feuille.iter_rows(min_col=colonne_index, max_col=colonne_index, values_only=False):
        cellule = row[0]

        # Vérifier si la cellule contient des URLs
        if cellule.value and isinstance(cellule.value, str) and "http" in cellule.value:
            # Extraire les URLs dans la cellule
            urls = [url.strip() for url in cellule.value.split(",")]

            # Modifier chaque URL dans la cellule
            nouvelles_urls = []
            for url in urls:
                nom_fichier = extraire_nom_fichier(url)
                nouvelles_urls.append(f"https://aimmotion.beekom.fr/wp-content/uploads/2024/02/{nom_fichier}.pdf")

            # Modifier l'URL dans la cellule
            cellule.value = nouvelles_urls[0] if len(nouvelles_urls) > 0 else None

    # Sauvegarder le fichier Excel modifié
    workbook.save(output_path)

# Exemple d'utilisation avec la colonne 18
input_file_path = "./SONOMAX2902Import.xlsx"
output_file_path = "./SONOMAX2902Importupdated.xlsx"
colonne_index = 18

modifier_urls_colonne(input_file_path, output_file_path, colonne_index)
