import pdfplumber
import re

# Chemin vers le fichier PDF
pdf_path = 'C:/Users/Beekom/Downloads/FLUX_POLIRIS.pdf'

# Liste pour stocker les lignes correspondantes
matched_lines = []

# Ouvrir le fichier PDF avec pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Parcourir toutes les pages du PDF
    for page_num in range(len(pdf.pages)):
        # Extraire le texte de la page
        page = pdf.pages[page_num]
        text = page.extract_text()
        
        # Séparer le texte en lignes
        lines = text.split('\n')
        
        # Parcourir chaque ligne
        for line in lines:
            # Vérifier si la ligne commence par un nombre entre 1 et 307
            if re.match(r'^([1-9]|[1-9][0-9]|[12][0-9][0-9]|30[0-7])\s', line.strip()):
                matched_lines.append(line.strip())

with open('output.txt', 'w', encoding='utf-8') as file:
    for line in matched_lines:
        file.write(line + '\n')

print("Extraction terminée. Les données ont été enregistrées dans 'output.txt'.")

