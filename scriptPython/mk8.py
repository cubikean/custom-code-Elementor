import os
import requests
from bs4 import BeautifulSoup

# L'URL de la page web que vous souhaitez analyser
url = "https://mariokart8.nintendo.com/booster-course-pass/"  # Remplacez par l'URL réelle

# Récupérer le contenu de la page web
response = requests.get(url)
html = response.text

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Sélectionner tous les éléments avec la classe "wave_courses"
wave_courses_elements = soup.find_all(class_='wave__courses')

# Parcourir chaque élément avec la classe "wave_courses"
for index, wave_course_element in enumerate(wave_courses_elements, start=1):
    # Créer un dossier différent pour chaque élément "wave_courses"
    folder_name = f'wave_course_{index}'
    os.makedirs(folder_name, exist_ok=True)

    # Récupérer l'image de l'élément "wave_courses"
    img_elements = wave_course_element.find_all('img')

    # Parcourir toutes les images dans l'élément "wave_courses"
    for img_element in img_elements:
        img_src = img_element.get('src')
        img_filename = os.path.basename(img_src)
        img_path = os.path.join(folder_name, img_filename)

        # Télécharger l'image
        img_url = 'https://mariokart8.nintendo.com/' + img_src  # Remplacez par l'URL appropriée
        response = requests.get(img_url)
        with open(img_path, 'wb') as img_file:
            img_file.write(response.content)

    # Récupérer le texte de h4 et les spans
    h4_element = wave_course_element.find('h4')
    h4_text = h4_element.get_text(strip=True)
    span_elements = wave_course_element.find_all('span')
    span_texts = [span.get_text(strip=True) for span in span_elements]

    # Écrire le texte dans un fichier texte en spécifiant l'encodage UTF-8
    text_filename = os.path.join(folder_name, 'info.txt')
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(f'Titre : {h4_text}\n')
        text_file.write(f'Spans : {", ".join(span_texts)}\n')
