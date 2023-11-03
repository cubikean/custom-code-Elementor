import asyncio
from pyppeteer import launch

# Fonction pour convertir une page en image
async def capture_screenshot(url, output_folder):
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    # Accéder à l'URL
    await page.goto(url)
    
    # Attendre un certain temps pour permettre le chargement complet de la page
    await page.waitFor(5000)  # Vous pouvez ajuster ce délai en fonction de vos besoins
    
    # Récupérer la hauteur totale de la page
    body_handle = await page.J("body")
    page_height = await page.evaluate('(body) => body.scrollHeight', body_handle)
    
    # Définir la taille de la fenêtre du navigateur en fonction de la hauteur de la page
    await page.setViewport({'width': 1920, 'height': page_height})
    
    # Capturer une capture d'écran de la page complète
    await page.screenshot({'path': f'{output_folder}/{url_hash}.png'})
    
    # Fermer le navigateur
    await browser.close()

# Liste des URLs à convertir en images
url_list = [
    "https://2023.beekom.fr/portfolio/cdc-aunis-atlantique/", 
"https://2023.beekom.fr/portfolio/la-rochelle-universite/", 
"https://2023.beekom.fr/portfolio/le-miroir/",
"https://2023.beekom.fr/portfolio/neel/",
"https://2023.beekom.fr/portfolio/skinclinic/",	
"https://2023.beekom.fr/portfolio/skydrone/",
"https://2023.beekom.fr/portfolio/beausejour/",
"https://2023.beekom.fr/portfolio/pole-nature/",
"https://2023.beekom.fr/portfolio/croix-rouge/",
"https://2023.beekom.fr/portfolio/natixis/",
"https://2023.beekom.fr/portfolio/groupe-michel/",
"https://2023.beekom.fr/portfolio/apline/",
"https://2023.beekom.fr/portfolio/engie/",
"https://2023.beekom.fr/portfolio/steco/",
"https://2023.beekom.fr/portfolio/seche/",	
"https://2023.beekom.fr/portfolio/izibook/",	
"https://2023.beekom.fr/portfolio/juvignac/",	
"https://2023.beekom.fr/portfolio/garance-mutuelle/",
"https://2023.beekom.fr/portfolio/chatel-cerf-volants/",
]

# Dossier de sortie pour les images capturées
output_folder = "captures"

# Créer le dossier de sortie s'il n'existe pas déjà
import os
os.makedirs(output_folder, exist_ok=True)

# Parcourir la liste des URLs et capturer les images
for url in url_list:
    url_hash = hash(url)  # Utilisez une fonction de hachage pour générer un nom de fichier unique
    asyncio.get_event_loop().run_until_complete(capture_screenshot(url, output_folder))

print("Conversion terminée. Les images sont enregistrées dans le dossier 'captures'.")
