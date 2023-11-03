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

# Sélectionner la div avec l'id "driver-grid"
driver_grid_div = soup.find(id='driver-grid')

# Sélectionner toutes les balises img dans la div "driver-grid"
img_elements = driver_grid_div.find_all('img')

# Créer un dossier pour les images
image_folder = 'driver_images'
os.makedirs(image_folder, exist_ok=True)

# Parcourir chaque image et télécharger
for index, img_element in enumerate(img_elements, start=1):
    img_src = img_element.get('data-src')
    if img_src:
        img_filename = os.path.basename(img_src)  # Obtenir le nom du fichier de l'URL
        img_filename = img_filename.replace('_th', '')  # Supprimer "th" du nom si présent
        img_path = os.path.join(image_folder, img_filename)

        # Télécharger l'image
        img_url = 'https://mariokart8.nintendo.com/' + img_src  # Remplacez par l'URL appropriée
        response = requests.get(img_url)
        with open(img_path, 'wb') as img_file:
            img_file.write(response.content)
