import os
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve HTML from {url}")
        return None

def extract_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', {'id': 'content'})
    if content_div:
        return str(content_div)
    else:
        print("No div with id 'content' found.")
        return None

def save_to_file(url, content):
    filename = f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"HTML content saved to {filename}")

def main():
    urls = [
            "https://iae.univ-larochelle.fr/Contact",
            "https://iae.univ-larochelle.fr/Master-of-Business-Administration",
            "https://iae.univ-larochelle.fr/Futur-etudiant",
            "https://iae.univ-larochelle.fr/Etudiant",
            "https://iae.univ-larochelle.fr/Ancien-etudiant",
            "https://iae.univ-larochelle.fr/Professionnel",
            "https://iae.univ-larochelle.fr/L-IAE-La-Rochelle",
            "https://iae.univ-larochelle.fr/Actualites",
            "https://iae.univ-larochelle.fr/Formations",
            "https://iae.univ-larochelle.fr/Recherche",
            "https://iae.univ-larochelle.fr/Vie-etudiante",
            "https://iae.univ-larochelle.fr/Formation-professionnelle-continue",
            "https://iae.univ-larochelle.fr/Certificat-Management-des-RH-a-l",
            "https://iae.univ-larochelle.fr/mae-e-learning",
            "https://iae.univ-larochelle.fr/Toutes-les-formations-en-formation",
            "https://iae.univ-larochelle.fr/Informations-pratiques",
            "https://iae.univ-larochelle.fr/L-IAE-La-Rochelle-en-bref",
            "https://iae.univ-larochelle.fr/Organisation",
            "https://iae.univ-larochelle.fr/Equipe-administrative-99",
            "https://iae.univ-larochelle.fr/Equipe-pedagogique-100",
            "https://iae.univ-larochelle.fr/Faculte-de-Droit-Science-Politique",
            "https://iae.univ-larochelle.fr/Certification",
            "https://iae.univ-larochelle.fr/Partenaires",
            "https://iae.univ-larochelle.fr/Annuaire-de-l-IAE-La-Rochelle",
            "https://iae.univ-larochelle.fr/Licence",
            "https://iae.univ-larochelle.fr/Classe-preparatoire-aux-grandes",
            "https://iae.univ-larochelle.fr/Masters-11",
            "https://iae.univ-larochelle.fr/Doctorat",
            "https://iae.univ-larochelle.fr/Echanges-internationaux",
            "https://iae.univ-larochelle.fr/L-alternance-a-l-IAE-La-Rochelle",
            "https://iae.univ-larochelle.fr/La-recherche-a-l-IAE-La-Rochelle",
            "https://iae.univ-larochelle.fr/equipes-recherche",
            "https://iae.univ-larochelle.fr/Reussir-ses-etudes-a-La-Rochelle",
            "https://iae.univ-larochelle.fr/Associations-etudiantes",
            "https://iae.univ-larochelle.fr/Sportifs-de-haut-niveau",
            "https://iae.univ-larochelle.fr/Projets-universitaires",
            "https://iae.univ-larochelle.fr/Profils",
            "https://iae.univ-larochelle.fr/Professionnel-61",
            "https://iae.univ-larochelle.fr/Mentions-legales",
            "https://iae.univ-larochelle.fr/Plan-de-site",
            "https://iae.univ-larochelle.fr/Master-Tourisme-parcours-Gestion",
            "https://iae.univ-larochelle.fr/Master-Management-des-systemes-d",
            "https://iae.univ-larochelle.fr/master-marketing-vente-parcours-marketing-digital",
            "https://iae.univ-larochelle.fr/Master-Sciences-pour-l",
            "https://iae.univ-larochelle.fr/Master-Management-et",
    ]

    for url in urls:
        html_content = get_html_content(url)
        if html_content:
            extracted_content = extract_content(html_content)
            if extracted_content:
                save_to_file(url, extracted_content)

if __name__ == "__main__":
    main()
