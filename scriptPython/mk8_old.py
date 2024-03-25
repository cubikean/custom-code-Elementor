import os
import requests
from bs4 import BeautifulSoup

# L'URL de la page web que vous souhaitez analyser
url = "https://mariokart8.nintendo.com"  # Remplacez par l'URL réelle

# Récupérer le contenu de la page web
response = requests.get(url)
html = response.text

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Sélectionner tous les éléments avec la classe "cup"
cup_elements = soup.find_all(class_='cup')

# Parcourir chaque élément avec la classe "cup"
for index, cup_element in enumerate(cup_elements, start=1):
    # Créer un dossier différent pour chaque élément "cup"
    folder_name = f'cup_{index}'
    os.makedirs(folder_name, exist_ok=True)

    # Extraire le nom de la coupe (texte de tous les h5)
    h5_elements = cup_element.find_all('h5')
    cup_names = [h5.get_text(strip=True) for h5 in h5_elements]

    # Récupérer le lien vers la page
    link_element = cup_element.find_parent('a')
    page_link = link_element.get('href') if link_element else ''

    # Écrire les noms de la coupe et le lien vers la page dans un fichier texte
    text_filename = os.path.join(folder_name, 'info.txt')
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        text_file.write('Noms de la coupe : \n')
        for name in cup_names:
            text_file.write(f' - {name}\n')
        text_file.write(f'Lien vers la page : {page_link}\n')

    # Extraire et télécharger les images de la coupe
    ul_element = cup_element.find('ul', class_='thumb-set')
    if ul_element:
        li_elements = ul_element.find_all('li')
        for img_index, li_element in enumerate(li_elements, start=1):
            img_element = li_element.find('img')
            img_src = img_element.get('data-src') if img_element else ''
            if img_src:
                img_filename = f'img_{img_index}.jpg'
                img_path = os.path.join(folder_name, img_filename)

                # Télécharger l'image
                img_url = 'https://mariokart8.nintendo.com/' + img_src
                response = requests.get(img_url)
                with open(img_path, 'wb') as img_file:
                    img_file.write(response.content)
