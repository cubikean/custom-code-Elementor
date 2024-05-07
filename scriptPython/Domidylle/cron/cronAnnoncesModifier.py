import csv
import os
import unicodedata
import html

def remove_special_characters(text):
    # Normaliser les caractères Unicode en ASCII et supprimer les caractères spéciaux
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(char for char in text if not unicodedata.combining(char))
    # Décode les entités HTML
    text = html.unescape(text)
    # Supprimer les guillemets doubles
    text = text.replace('"', '')
    return text

def convert_csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r', encoding='cp1252') as csv_file, open(output_txt, 'w', encoding='utf-8') as txt_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Join each field with a ';' and remove special characters
            txt_row = ";".join(row).replace("!#", ";")
            txt_row = remove_special_characters(txt_row)
            txt_file.write(txt_row + "\n")

# Chemin du fichier CSV en entrée
input_csv_file = "Annonces.csv"

# Création du chemin pour le dossier de sortie et le fichier texte
output_folder = "output"
output_txt_file = os.path.join(output_folder, "Annonces.txt")

# Vérifier si le dossier de sortie existe, sinon le créer
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convertir le CSV en TXT
convert_csv_to_txt(input_csv_file, output_txt_file)
print("Conversion terminée.")

