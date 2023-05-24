import re
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

value = [
    "9004/bio", "9008/saisons", "9010/2015", "9061/figaro-2", "11664/class-40",
    "11687/figaro-3", "9007/les-partenaires", "9012/medias", "9016/photo",
    "9017/videos", "9999/presse", "9025/contact",
]

for i in range(len(value)):
    folder_name = value[i].split("/")[0]  # Obtenir le nom du dossier à partir du lien
    site = "http://julienpulve.com/s/" + value[i]
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    urls = [img['src'] for img in image_tags]
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', url)
        if not filename:
            print("L'expression régulière ne correspond pas à l'URL : {}".format(url))
            continue
        filepath = os.path.join(os.getcwd(), folder_name, filename.group(1))  # Chemin vers le fichier incluant le dossier

        full_url = urljoin(site, url)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Créer le dossier s'il n'existe pas

        with open(filepath, 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(full_url)
            f.write(response.content)
    print("Téléchargement terminé, les images téléchargées se trouvent dans le dossier correspondant !")
