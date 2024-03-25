import re
import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter

# Liste des noms à rechercher
noms_a_rechercher = ["Hugo CHATIGNY", "Autre Nom"]

# Fonction pour sélectionner le fichier PDF source
def select_pdf_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Sélectionnez le fichier PDF source",
        filetypes=[("Fichiers PDF", "*.pdf")],
    )

    root.destroy()  # Close the Tkinter window

    return file_path

# Fonction pour extraire le texte et trouver le nom dans la liste
def extract_and_rename(pdf_path, noms_a_rechercher):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        for nom in noms_a_rechercher:
            if nom in text:
                return nom

    return None

# Sélection du fichier PDF source
input_pdf_path = select_pdf_file()

if not input_pdf_path:
    print("Aucun fichier sélectionné. Sortie du programme.")
else:
    # Extraction du nom de la liste
    extracted_name = extract_and_rename(input_pdf_path, noms_a_rechercher)

    if extracted_name:
        print("Nom extrait:", extracted_name)

        # Traitement du fichier PDF
        input_pdf = PdfReader(open(input_pdf_path, "rb"))

        for i in range(len(input_pdf.pages)):
            output = PdfWriter()
            output.add_page(input_pdf.pages[i])
            output_pdf_path = "{}_page{}.pdf".format(extracted_name, i + 1)
            with open(output_pdf_path, "wb") as output_stream:
                output.write(output_stream)

        print("Le découpage du PDF est terminé.")
    else:
        print("Aucun nom de la liste trouvé dans le PDF.")
