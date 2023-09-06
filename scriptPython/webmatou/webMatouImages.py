import requests
from bs4 import BeautifulSoup
import re
import os

value = [
"grand-sac-tapis-turquoise-noir-jaune-et-blanc-en-plastique-recycle-matou-deco-118.php",
"grand-sac-tapis-gris-noir-et-blanc-en-plastique-recycle-matou-deco-119.php",
"grand-sac-tapis-bleu-rouge-noir-et-blanc-en-plastique-recycle-matou-deco-120.php",
"grand-sac-tapis-couleurs-multiples-en-plastique-recycle-matou-deco-122.php",
"moyen-sac-tapis-turquoise-noir-jaune-et-blanc-en-plastique-recycle-matou-deco-112.php",
"sac-moyen-tapis-couleurs-multiples-en-plastique-recycle-matou-deco-113.php",
"sac-moyen-tapis-gris-noir-et-blanc-en-plastique-recycle-matou-deco-121.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-85.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-44.php",
"corbeille-somone-rouge-jaune-et-bleu-en-osier-et-plastique-recycle-matou-deco-38.php",
"grand-panier-palmarin-beige-et-chocolat-en-osier-et-plastique-recycle-matou-deco-110.php",
"abat-jour-vintage-nbodienne-uni-naturel-en-osier-matou-deco-123.php",
"bac-en-osier-nbodienne-uni-naturel-en-osier-matou-deco-126.php",
"couffin-nbodienne-uni-naturel-en-osier-matou-deco-127.php",
"grand-panier-a-anse-nbodienne-uni-naturel-en-osier-matou-deco-125.php",
"panier-moyen-a-anse-nbodienne-uni-naturel-en-osier-matou-deco-124.php",
"corbeille-ajouree-granda-uni-naturel-et-bleu-en-osier-et-plastique-recycle-matou-deco-161.php",
"lot-de-3-paniers-palmarin-multicolors-en-osier-et-plastique-recycle-matou-deco-163.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-96.php",
"corbeille-a-fruits-etoilee-somone-beige-et-turquoise-en-osier-et-plastique-recycle-matou-deco-56.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-63.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-64.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-65.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-66.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-67.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-68.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-69.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-70.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-71.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-72.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-73.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-74.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-75.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-76.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-77.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-78.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-79.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-80.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-81.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-82.php",
"panier-rond-ngaye-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-109.php",
"panier-rond-ngaye-bleu-en-osier-et-plastique-recycle-matou-deco-108.php",
"panier-rond-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-107.php",
"panier-rond-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-106.php",
"panier-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-105.php",
"panier-ngaye-jaune-en-osier-et-plastique-recycle-matou-deco-104.php",
"panier-ngaye-jaune-et-blanc-en-osier-et-plastique-recycle-matou-deco-103.php",
"panier-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-102.php",
"panier-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-101.php",
"panier-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-100.php",
"panier-ngaye-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-99.php",
"panier-ngaye-uni-naturel-en-osier-et-plastique-recycle-matou-deco-98.php",
"panier-ngaye-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-97.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-95.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-94.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-93.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-92.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-91.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-90.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-89.php",
"lot-de-3-corbeilles-ovales-palmarin-uni-naturel-blanc-et-violet-en-osier-et-plastique-recycle-matou-deco-138.php",
"petite-corbeille-a-pain-somone-uni-vert-en-osier-et-plastique-recycle-matou-deco-26.php",
"panier-ngaparou-noir-et-blanc-en-osier-et-plastique-recycle-matou-deco-144.php",
"panier-moyen-palmarin-beige-et-chocolat-en-osier-et-plastique-recycle-matou-deco-129.php",
"baume-karidou-karite-ylang-ylang-produit-cosmetique-naturel-biologique-171.php",
"baume-karimango-karite-mangue-produit-cosmetique-naturel-biologique-172.php",
"baume-levres-karilip-karite-fleurs-d-hibiscus-bissap-bio-produit-cosmetique-naturel-biologique-173.php",
"creme-de-jour-a-l-huile-de-baobab-bio-produit-cosmetique-naturel-biologique-174.php",
"creme-de-nuit-a-l-huile-d-argan-bio-produit-cosmetique-naturel-biologique-175.php",
"eau-douce-lotion-nettoyante-produit-cosmetique-naturel-biologique-184.php",
"huile-d-hibiscus-bissap-aux-extraits-d-abricot-bio-produit-cosmetique-naturel-biologique-176.php",
"huile-de-baobab-aux-extraits-d-ylang-ylang-bio-produit-cosmetique-naturel-biologique-177.php",
"huile-de-moringa-aux-extraits-de-menthe-poivree-bio-produit-cosmetique-naturel-biologique-178.php",
"huile-silhouette-raffermissante-et-anti-cellulite-produit-cosmetique-naturel-biologique-179.php",
"huile-vierge-aux-fleurs-d-hibiscus-bissap-bio-produit-cosmetique-naturel-biologique-180.php",
"huile-vierge-de-baobab-bio-produit-cosmetique-naturel-biologique-181.php",
"huile-vierge-de-moringa-bio-produit-cosmetique-naturel-biologique-182.php",
"huile-vierge-de-pasteque-bio-produit-cosmetique-naturel-biologique-183.php",
"serum-precieux-eclat-anti-taches-nuit-produit-cosmetique-naturel-biologique-185.php",
"grande-tarre-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-149.php",
"corbeille-ovale-moyenne-palmarin-uni-naturel-blanc-et-violet-en-osier-et-plastique-recycle-matou-deco-135.php",
"corbeille-ajouree-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-160.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-88.php",
"corbeille-ovale-grande-palmarin-uni-naturel-blanc-et-violet-en-osier-et-plastique-recycle-matou-deco-136.php",
"corbeille-ovale-petite-palmarin-uni-naturel-blanc-et-violet-en-osier-et-plastique-recycle-matou-deco-137.php",
"grand-panier-palmarin-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-111.php",
"lot-de-3-paniers-palmarin-beige-et-chocolat-en-osier-et-plastique-recycle-matou-deco-131.php",
"lot-de-3-paniers-palmarin-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-132.php",
"grand-panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-170.php",
"panier-moyen-palmarin-beige-et-chocolat-en-osier-et-plastique-recycle-matou-deco-128.php",
"panier-moyen-palmarin-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-133.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-164.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-165.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-166.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-167.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-168.php",
"panier-palmarin-avec-poignees-et-couvercle-multicolors-en-osier-et-plastique-recycle-matou-deco-169.php",
"petit-panier-palmarin-beige-et-chocolat-en-osier-et-plastique-recycle-matou-deco-130.php",
"petit-panier-palmarin-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-134.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-86.php",
"corbeille-somone-vert-beige-et-noir-en-osier-et-plastique-recycle-matou-deco-36.php",
"corbeille-somone-bleu-rouge-et-jaune-en-osier-et-plastique-recycle-matou-deco-37.php",
"corbeille-somone-bleu-rouge-et-jaune-en-osier-et-plastique-recycle-matou-deco-39.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-40.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-41.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-42.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-43.php",
"corbeille-somone-noir-beige-et-vert-en-osier-et-plastique-recycle-matou-deco-45.php",
"corbeille-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-46.php",
"corbeille-a-fruits-etoilee-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-47.php",
"corbeille-a-fruits-etoilee-somone-bleu-rose-et-vert-en-osier-et-plastique-recycle-matou-deco-48.php",
"corbeille-a-fruits-etoilee-somone-beige-rouge-et-orange-en-osier-et-plastique-recycle-matou-deco-49.php",
"corbeille-a-fruits-etoilee-somone-blanc-rouge-et-jaune-en-osier-et-plastique-recycle-matou-deco-50.php",
"corbeille-a-fruits-etoilee-somone-turquoise-et-beige-en-osier-et-plastique-recycle-matou-deco-51.php",
"corbeille-a-fruits-etoilee-somone-rose-bleu-et-vert-en-osier-et-plastique-recycle-matou-deco-52.php",
"corbeille-a-fruits-etoilee-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-53.php",
"corbeille-a-fruits-etoilee-somone-beige-et-turquoise-en-osier-et-plastique-recycle-matou-deco-54.php",
"corbeille-a-fruits-etoilee-somone-beige-et-turquoise-en-osier-et-plastique-recycle-matou-deco-55.php",
"lot-de-6-sets-de-table-somone-noir-et-blanc-en-osier-et-plastique-recycle-matou-deco-16.php",
"lot-de-6-sets-de-table-somone-noir-et-bleu-clair-en-osier-et-plastique-recycle-matou-deco-17.php",
"set-de-table-somone-turquoise-et-blanc-en-osier-et-plastique-recycle-matou-deco-27.php",
"set-de-table-somone-uni-noir-en-osier-et-plastique-recycle-matou-deco-24.php",
"set-de-table-somone-uni-turquoise-en-osier-et-plastique-recycle-matou-deco-23.php",
"set-de-table-somone-uni-naturel-en-osier-et-plastique-recycle-matou-deco-22.php",
"set-de-table-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-19.php",
"set-de-table-somone-orange-et-bleu-en-osier-et-plastique-recycle-matou-deco-10.php",
"set-de-table-somone-noir-et-bleu-clair-en-osier-et-plastique-recycle-matou-deco-9.php",
"set-de-table-somone-noir-et-blanc-en-osier-et-plastique-recycle-matou-deco-8.php",
"set-de-table-somone-orange-et-noir-en-osier-et-plastique-recycle-matou-deco-7.php",
"set-de-table-somone-rouge-et-blanc-en-osier-et-plastique-recycle-matou-deco-6.php",
"set-de-table-somone-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-5.php",
"set-de-table-somone-orange-et-blanc-en-osier-et-plastique-recycle-matou-deco-4.php",
"set-de-table-somone-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-3.php",
"lot-de-6-sets-de-table-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-1.php",
"petite-corbeille-a-pain-somone-bleu-et-rouge-en-osier-et-plastique-recycle-matou-deco-32.php",
"petite-corbeille-a-pain-somone-rouge-et-vert-en-osier-et-plastique-recycle-matou-deco-31.php",
"petite-corbeille-a-pain-somone-noir-et-jaune-en-osier-et-plastique-recycle-matou-deco-30.php",
"corbeille-granda-uni-naturel-et-noir-en-osier-et-plastique-recycle-matou-deco-158.php",
"corbeille-ngaparou-orange-et-beige-en-osier-et-plastique-recycle-matou-deco-142.php",
"lot-de-3-tarres-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-150.php",
"panier-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-139.php",
"panier-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-140.php",
"panier-ngaparou-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-141.php",
"panier-ngaparou-blanc-et-rose-en-osier-et-plastique-recycle-matou-deco-143.php",
"panier-ngaparou-orange-et-blanc-en-osier-et-plastique-recycle-matou-deco-145.php",
"panier-ngaparou-bleu-et-jaune-en-osier-et-plastique-recycle-matou-deco-146.php",
"moyenne-tarre-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-148.php",
"petite-tarre-ngaparou-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-147.php",
"corbeille-granda-uni-naturel-et-marron-en-osier-et-plastique-recycle-matou-deco-159.php",
"lot-de-3-pots-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-153.php",
"panier-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-151.php",
"panier-plat-granda-uni-naturel-et-noir-en-osier-et-plastique-recycle-matou-deco-154.php",
"panier-plat-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-155.php",
"panier-plat-granda-uni-naturel-et-marron-en-osier-et-plastique-recycle-matou-deco-156.php",
"porte-parapluie-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-162.php",
"pot-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-152.php",
"pot-cone-granda-uni-naturel-et-blanc-en-osier-et-plastique-recycle-matou-deco-157.php",
"lot-de-6-sets-de-table-somone-bleu-et-blanc-en-osier-et-plastique-recycle-matou-deco-13.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-87.php",
"petite-corbeille-a-pain-somone-noir-vert-et-beige-en-osier-et-plastique-recycle-matou-deco-29.php",
"lot-de-6-sets-de-table-somone-rouge-et-blanc-en-osier-et-plastique-recycle-matou-deco-14.php",
"lot-de-6-sets-de-table-somone-uni-naturel-en-osier-et-plastique-recycle-matou-deco-21.php",
"panier-ngaye-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-83.php",
"corbeille-a-fruits-etoilee-somone-noir-et-beige-en-osier-et-plastique-recycle-matou-deco-35.php",
"petite-corbeille-a-pain-somone-vert-et-naturel-en-osier-et-plastique-recycle-matou-deco-28.php",
"lot-de-6-sets-de-table-somone-orange-et-noir-en-osier-et-plastique-recycle-matou-deco-15.php",
"corbeille-a-fruits-etoilee-somone-jaune-rouge-et-blanc-en-osier-et-plastique-recycle-matou-deco-61.php",
"lot-de-2-corbeilles-a-pain-somone-rouge-vert-et-bleu-rouge-en-osier-et-plastique-recycle-matou-deco-117.php",
"petite-corbeille-a-pain-somone-uni-jaune-en-osier-et-plastique-recycle-matou-deco-25.php",
"lot-de-2-corbeilles-a-pain-somone-noir-beige-vert-et-noir-jaune-en-osier-et-plastique-recycle-matou-deco-116.php",
"lot-de-6-sets-de-table-somone-vert-et-blanc-en-osier-et-plastique-recycle-matou-deco-11.php",
"corbeille-a-fruits-etoilee-somone-blanc-rouge-et-jaune-en-osier-et-plastique-recycle-matou-deco-59.php",
"lot-de-6-sets-de-table-somone-orange-et-blanc-en-osier-et-plastique-recycle-matou-deco-12.php",
"set-de-table-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-20.php",
"corbeille-a-fruits-etoilee-somone-rouge-orange-et-beige-en-osier-et-plastique-recycle-matou-deco-60.php",
"grande-corbeille-a-pain-somone-rouge-jaune-et-beige-en-osier-et-plastique-recycle-matou-deco-34.php",
"corbeille-a-fruits-etoilee-somone-rouge-beige-et-orange-en-osier-et-plastique-recycle-matou-deco-57.php",
"lot-de-6-sets-de-table-somone-orange-et-bleu-en-osier-et-plastique-recycle-matou-deco-18.php",
"corbeille-a-fruits-etoilee-somone-rouge-jaune-et-blanc-en-osier-et-plastique-recycle-matou-deco-58.php",
"lot-de-6-sets-de-table-somone-couleurs-multiples-en-osier-et-plastique-recycle-matou-deco-2.php",
"panier-ngaye-chocolat-et-beige-en-osier-et-plastique-recycle-matou-deco-84.php",
"corbeille-a-fruits-etoilee-somone-blanc-jaune-et-rouge-confectionne-en-osier-et-plastique-recycle-matou-deco-62.php",
"lot-de-3-corbeilles-a-pain-somone-uni-jaune-uni-vert-vert-et-naturel-en-osier-et-plastique-recycle-matou-deco-33.php",]

for i in range(len(value)):
    url = "https://www.matoudeco.com/" + value[i]
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image elements inside divs with class "bigger" and "cellule"
        img_elements_bigger = soup.select('div.bigger img[src]')
        img_elements_cellule = soup.select('div.cellule img[src]')

        # Create a directory to store the images
        image_dir = 'images_' + re.sub(r'[\/\-\.?]', '_', value[i])
        os.makedirs(image_dir, exist_ok=True)

        # Function to check if an image URL has a .jpg extension
        def is_jpg_url(url):
            return url.endswith('.jpg')

        # Download and save images from divs with class "bigger"
        for img in img_elements_bigger:
            img_url = "https://www.matoudeco.com/" + img['src']
            if is_jpg_url(img_url):
                img_name = os.path.basename(img_url)
                img_path = os.path.join(image_dir, img_name)

                # Download the image
                img_data = requests.get(img_url).content

                # Save the image locally
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)

        # Download and save images from divs with class "cellule"
        for img in img_elements_cellule:
            img_url = "https://www.matoudeco.com/" + img['src']
            if is_jpg_url(img_url):
                img_name = os.path.basename(img_url)
                img_path = os.path.join(image_dir, img_name)

                # Download the image
                img_data = requests.get(img_url).content

                # Save the image locally
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)

        # Rest of your code to extract text and save it in a text file
        # ...

        # Print a message to indicate the process is completed
        print(f"Images (.jpg) and text extracted from {url} and saved in {image_dir}")

    else:
        print(f"Failed to fetch data from {url}, status code: {response.status_code}")
