from time import sleep
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup

output_folder = 'debug-file-iae'
os.makedirs(output_folder, exist_ok=True)


value = [
#   "/Contact",
#   "/Master-of-Business-Administration",
#   "/Futur-etudiant",
#   "/Etudiant",
#   "/Ancien-etudiant",
#   "/Professionnel",
#   "/L-IAE-La-Rochelle",
#   "/Actualites",
#   "/Formations",
#   "/Recherche",
#   "/Vie-etudiante",
#   "/Formation-professionnelle-continue",
#   "/Certificat-Management-des-RH-a-l",
#   "/mae-e-learning",
#   "/Toutes-les-formations-en-formation",
#   "/Informations-pratiques",
#   "/L-IAE-La-Rochelle-en-bref",
#   "/Organisation",
#   "/Equipe-administrative-99",
#   "/Equipe-pedagogique-100",
#   "/Faculte-de-Droit-Science-Politique",
#   "/Certification",
#   "/Partenaires",
#   "/Annuaire-de-l-IAE-La-Rochelle",
#   "/Licence",
#   "/Classe-preparatoire-aux-grandes",
#   "/Masters-11",
#   "/Doctorat",
#   "/Echanges-internationaux",
#   "/L-alternance-a-l-IAE-La-Rochelle",
#   "/La-recherche-a-l-IAE-La-Rochelle",
#   "/equipes-recherche",
#   "/Reussir-ses-etudes-a-La-Rochelle",
#   "/Associations-etudiantes",
#   "/Sportifs-de-haut-niveau",
#   "/Projets-universitaires",
#   "/Profils",
#   "/Professionnel-61",
#   "/Mentions-legales",
#   "/Plan-de-site"
    "/Associations-etudiantes"
]
for i in range(len(value)):
    url = "https://iae.univ-larochelle.fr"+ value[i]
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style", "nav", "header", "div", "section", "footer", "h1", "h2", "h3", "h4", "h5", "h6"]):
        if 'class' in script.attrs:
            if "accueil" in script.attrs['class']:
                script.extract()    # rip it out
        if 'class' in script.attrs:
            if "footer" in script.attrs['class']:
                script.extract()    # rip it out
            if "aside" in script.attrs['class']:
                script.extract()    # rip it out
            if "page_mail" in script.attrs['class']:
                script.extract()    # rip it out
            if "breadcrumb" in script.attrs['class']:
                script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # Imprimez le texte
    print(text)

    # Créez le chemin complet pour le fichier de sortie dans le dossier spécifié
    file_path = os.path.join(output_folder, value[i].replace("/", "_") + '.txt')

    counter = 1
    while os.path.exists(file_path):
        # Si le fichier existe, ajoutez "bis" au nom du fichier
        file_path = os.path.join(output_folder, value[i].replace("/", "_") + f'_bis{counter}.txt')
        counter += 1

    # Écrivez le texte dans le fichier
    with open(file_path, 'x') as f:
        f.write(text)
