import requests
from bs4 import BeautifulSoup

value = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

# Ouvrir un fichier en mode écriture
with open('donnees_apres_h1.txt', 'w', encoding='utf-8') as fichier:

    for i in range(len(value)):
        url = "https://www.matoudeco.com/fabrication-artisanale-objets-decoration.php?talents=" + value[i]

        # Envoyer une requête GET pour récupérer la page web
        response = requests.get(url)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Utiliser BeautifulSoup pour analyser le contenu HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Trouver la balise <h1> et récupérer le texte qui la suit
            h1_tag = soup.find('h1')
            if h1_tag:
                data_after_h1 = h1_tag.find_next_sibling(text=True)
                if data_after_h1:
                    donnees = data_after_h1.strip()
                    print(f"Données après <h1> dans l'URL {url}:")
                    print(donnees)
                    
                    # Écrire les données dans le fichier texte
                    fichier.write(f"Données après <h1> dans l'URL {url}:\n")
                    fichier.write(donnees + '\n\n')
                else:
                    print(f"Aucune donnée trouvée après <h1> dans l'URL {url}")
            else:
                print(f"Balise <h1> non trouvée dans l'URL {url}")
        else:
            print(f"La requête pour l'URL {url} a échoué avec le code {response.status_code}")

print("Données exportées avec succès dans le fichier 'donnees_apres_h1.txt'.")
