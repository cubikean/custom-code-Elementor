from time import sleep
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup

def remove_classes(soup, classes_to_remove):
    for class_name in classes_to_remove:
        elements = soup.find_all(class_=class_name)
        for element in elements:
            element.decompose()

output_folder = 'debug-file-iae'
os.makedirs(output_folder, exist_ok=True)

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
  "/Plan-de-site",
]

classes_to_remove = ["breadcrumb", "page_mail"]  # Add your desired classes here

for i in range(len(value)):
    url = "https://iae.univ-larochelle.fr" + value[i]
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # Remove specified classes
    remove_classes(soup, classes_to_remove)

    # Extract content inside <article> tag or any other desired tag
    content_tag = soup.find("article")  # Change this to the desired tag
    if content_tag:
        content = content_tag.get_text()
    else:
        content = ""

    # Print the extracted content
    print(content)

    # Create the complete path for the output file in the specified folder
    file_path = os.path.join(output_folder, value[i].replace("/", "_") + '.txt')

    counter = 1
    while os.path.exists(file_path):
        # If the file exists, append "bis" to the file name
        file_path = os.path.join(output_folder, value[i].replace("/", "_") + f'_bis{counter}.txt')
        counter += 1

    # Write the text to the file
    with open(file_path, 'x') as f:
        f.write(content)
