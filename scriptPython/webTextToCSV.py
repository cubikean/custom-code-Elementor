from time import sleep
from urllib.request import urlopen
import os
import csv
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
  "/Plan-de-site"
]

classes_to_remove = ["breadcrumb", "page_mail", "blocs_title"]  # Add your desired classes here

# Lists to store data
data = []

for i in range(len(value)):
    url = "https://iae.univ-larochelle.fr" + value[i]
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # Remove specified classes
    remove_classes(soup, classes_to_remove)

    # Extract title and content
    content_tag = soup.find("article")  # Change this to the desired tag
    title_tag = content_tag.find("h1")
    title = title_tag.get_text() if title_tag else "Pas de titre"

    content = content_tag.get_text(separator=' ', strip=True) if content_tag else ""

    # Append data to list
    data.append({'Title': title, 'Content': content})

    # Print the extracted content on the same line
    print(f"Title:{title} | Content:{content}")

    file_path = os.path.join(output_folder, value[i].replace("/", "_") + '.txt')

    counter = 1
    while os.path.exists(file_path):
        # If the file exists, add "bis" to the file name
        file_path = os.path.join(output_folder, value[i].replace("/", "_") + f'_bis{counter}.txt')
        counter += 1

    # Write the extracted content to the file on the same line
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Title:{title}\n\nContent:{content}")

    print("File created:", file_path)

