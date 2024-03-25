import re
import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

value = [
  "/Contact",
  "/Master-of-Business-Administration",
  "/Futur-etudiant",
  "/Etudiant",
  "/Ancien-etudiant",
  "/Professionnel",
  "/L-IAE-La-Rochelle",
  "/Actualites",
  "/Formations",
  "/Recherche",
  "/Vie-etudiante",
  "/Formation-professionnelle-continue",
  "/Certificat-Management-des-RH-a-l",
  "/mae-e-learning",
  "/Toutes-les-formations-en-formation",
  "/Informations-pratiques",
  "/L-IAE-La-Rochelle-en-bref",
  "/Organisation",
  "/Equipe-administrative-99",
  "/Equipe-pedagogique-100",
  "/Faculte-de-Droit-Science-Politique",
  "/Certification",
  "/Partenaires",
  "/Annuaire-de-l-IAE-La-Rochelle",
  "/Licence",
  "/Classe-preparatoire-aux-grandes",
  "/Masters-11",
  "/Doctorat",
  "/Echanges-internationaux",
  "/L-alternance-a-l-IAE-La-Rochelle",
  "/La-recherche-a-l-IAE-La-Rochelle",
  "/equipes-recherche",
  "/Reussir-ses-etudes-a-La-Rochelle",
  "/Associations-etudiantes",
  "/Sportifs-de-haut-niveau",
  "/Projets-universitaires",
  "/Profils",
  "/Professionnel-61",
  "/Mentions-legales",
  "/Plan-de-site"
]
for i in range(len(value)):
    link_path = value[i]
    folder_name = link_path.strip("/").replace("/", "_")  # Utiliser le nom du lien comme nom de dossier
    site = "https://iae.univ-larochelle.fr" + link_path
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    
    for img in image_tags:
        src = img.get('src', '')

        # Extraire le chemin du fichier et les paramètres d'URL
        parsed_url = urlparse(src)
        path, params = parsed_url.path, parsed_url.params

        # Utiliser une expression régulière pour extraire le nom du fichier
        filename_match = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', path)
        if not filename_match:
            print("L'expression régulière ne correspond pas à l'URL : {}".format(src))
            continue

        filename = filename_match.group(1)

        # Si des paramètres d'URL existent, les ajouter au nom du fichier
        if params:
            filename += "?" + params

        filepath = os.path.join(os.getcwd(), folder_name, filename)

        full_url = urljoin(site, src)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'wb') as f:
            if 'http' not in src:
                src = '{}{}'.format(site, src)
            response = requests.get(full_url)
            f.write(response.content)

print("Téléchargement terminé, les images téléchargées se trouvent dans les dossiers correspondants !")
