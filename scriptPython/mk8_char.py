import os
import re
import requests
from bs4 import BeautifulSoup

# Fonction pour nettoyer un nom de fichier
def clean_filename(filename):
    # Remplacez tous les caractères non alphanumériques et non espaces par des underscores
    cleaned = re.sub(r'[^A-Za-z0-9\s]', '_', filename)
    return cleaned

# L'URL de la page web que vous souhaitez analyser
url = "https://www.mariowiki.com/Mario_Kart_8_Deluxe"  # Remplacez par l'URL réelle

# Récupérer le contenu de la page web
response = requests.get(url)
html = response.text

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Sélectionner tous les éléments <li class="gallerybox">
gallerybox_elements = soup.find_all(class_='gallerybox')

# Parcourir chaque élément <li class="gallerybox">
for index, gallerybox_element in enumerate(gallerybox_elements, start=1):
    # Extraire le nom de l'élément
    name_element = gallerybox_element.find('a', title=True)
    item_name = name_element['title']

    # Nettoyer le nom de l'élément pour supprimer les caractères spéciaux
    cleaned_name = clean_filename(item_name)

    # Extraire l'URL de l'image
    img_element = gallerybox_element.find('img', src=True)
    img_url = img_element['src']

    folder_name = f'{cleaned_name}'
    os.makedirs(folder_name, exist_ok=True)

    # Télécharger l'image
    img_response = requests.get(img_url)
    img_filename = os.path.basename(img_url)
    img_path = os.path.normpath(os.path.join(folder_name, img_filename))

    with open(img_path, 'wb') as img_file:
        img_file.write(img_response.content)

    # Créer un fichier texte avec le nom de l'élément
    text_filename = os.path.normpath(os.path.join(folder_name, 'info.txt'))
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(f'{item_name}')
