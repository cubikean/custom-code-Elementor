from PIL import Image
import numpy as np
import os

def hex_to_rgb(hex_color):
    """
    Convertit une couleur hexadécimale en tuple RGB.
    
    :param hex_color: Couleur hexadécimale (ex: '#ff0000' ou 'ff0000' pour rouge).
    :return: Tuple RGB (ex: (255, 0, 0)).
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def ajouter_bruit_aux_zones(image_array, masque_array, intensite_bruit):
    """
    Ajoute un bruit aléatoire uniquement aux zones définies par un masque dans une image.
    
    :param image_array: Tableau numpy de l'image en valeurs normalisées (0-1).
    :param masque_array: Tableau numpy du masque en valeurs normalisées (0-1).
    :param intensite_bruit: Intensité du bruit (valeur entre 0 et 1).
    :return: Tableau numpy de l'image avec du bruit ajouté aux zones du masque.
    """
    bruit = np.random.normal(0, intensite_bruit, image_array.shape)
    image_bruitee = image_array + (bruit * masque_array[:, :, None])  # Appliquer le bruit uniquement aux zones définies par le masque
    image_bruitee = np.clip(image_bruitee, 0, 1)  # S'assurer que les valeurs restent dans l'intervalle [0, 1]
    return image_bruitee

def appliquer_effet(image_base_path, image_masque_path, couleur_hex, output_path, intensite_bruit=None):
    """
    Applique une couleur avec un effet de produit, et éventuellement du bruit, aux zones définies par un masque sur une image de base tout en
    conservant la transparence.
    
    :param image_base_path: Chemin de l'image de base (format PNG).
    :param image_masque_path: Chemin de l'image de masque (format PNG, en niveaux de gris).
    :param couleur_hex: Couleur en format hexadécimal (ex: '#ff0000').
    :param output_path: Chemin pour enregistrer l'image résultante (format PNG).
    :param intensite_bruit: Intensité du bruit (valeur entre 0 et 1), si None pas de bruit ajouté.
    """
    # Convertir la couleur hexadécimale en RGB
    couleur_rgb = hex_to_rgb(couleur_hex)
    
    # Ouvrir les images PNG
    image_base = Image.open(image_base_path).convert('RGBA')  # Charger avec alpha pour conserver la transparence
    image_masque = Image.open(image_masque_path).convert('L')  # Convertir le masque en niveaux de gris

    # Convertir les images en tableaux numpy
    image_base_array = np.array(image_base, dtype=np.float32) / 255.0  # Normaliser entre 0 et 1
    image_masque_array = np.array(image_masque, dtype=np.float32) / 255.0  # Normaliser entre 0 et 1

    # Créer un tableau pour la nouvelle couleur, normalisé entre 0 et 1
    couleur_array = np.array(couleur_rgb, dtype=np.float32) / 255.0

    # Appliquer l'effet de produit aux zones définies par le masque, en préservant la transparence
    for i in range(3):  # Pour chaque canal de couleur (R, G, B)
        image_base_array[:, :, i] = np.where(
            image_masque_array > 0,  # Si la zone du masque est blanche (non nulle)
            image_base_array[:, :, i] * couleur_array[i],  # Appliquer l'effet de produit
            image_base_array[:, :, i]  # Sinon, garder la couleur originale
        )

    # Ajouter du bruit uniquement aux zones définies par le masque, si spécifié
    if intensite_bruit is not None:
        image_base_array[:, :, :3] = ajouter_bruit_aux_zones(image_base_array[:, :, :3], image_masque_array, intensite_bruit)

    # Conserver le canal alpha tel quel
    alpha_channel = image_base_array[:, :, 3]

    # Convertir le tableau numpy en image PIL
    image_resultante_array = (image_base_array * 255).astype(np.uint8)
    image_resultante_array[:, :, 3] = (alpha_channel * 255).astype(np.uint8)  # Re-appliquer le canal alpha

    image_resultante = Image.fromarray(image_resultante_array, 'RGBA')

    # Enregistrer l'image résultante en PNG en conservant la transparence
    image_resultante.save(output_path, format='PNG')

# Liste des couleurs
colors = ["#972e25", "#2b3a44", "#637d96", "#7d765a", "#766a5e", "#383e42", "#4c4a44", "#0e0e10", "#f1ece1", "#333336", "#71716f"]

# Liste des couleurs pour lesquelles on ajoute du bruit
colors_avec_bruit = ["#333336", "#71716f"]

# Chemin du dossier principal
dossier_principal = './import'

# Dossier de sortie
dossier_sortie = './export'
os.makedirs(dossier_sortie, exist_ok=True)

# Extensions de fichiers d'image valides
extensions_valides = ['.png', '.jpg', '.jpeg']

# Parcourir chaque sous-répertoire dans le dossier principal
for sous_dossier in os.listdir(dossier_principal):
    chemin_sous_dossier = os.path.join(dossier_principal, sous_dossier)

    if os.path.isdir(chemin_sous_dossier):
        # Créer le même sous-dossier dans le dossier de sortie
        chemin_sortie_sous_dossier = os.path.join(dossier_sortie, sous_dossier)
        os.makedirs(chemin_sortie_sous_dossier, exist_ok=True)

        # Trouver tous les fichiers d'image dans le sous-dossier
        fichiers_images = [f for f in os.listdir(chemin_sous_dossier) if os.path.isfile(os.path.join(chemin_sous_dossier, f)) and os.path.splitext(f)[1].lower() in extensions_valides]
        
        for fichier_base in fichiers_images:
            chemin_fichier_base = os.path.join(chemin_sous_dossier, fichier_base)
            
            # Appliquer les effets de couleur pour chaque fichier de masque
            for fichier_masque in fichiers_images:
                if fichier_masque != fichier_base:  # Ignorer le fichier de base lui-même pour éviter de l'utiliser comme masque
                    chemin_fichier_masque = os.path.join(chemin_sous_dossier, fichier_masque)

                    # Effectuer le traitement pour chaque couleur
                    for idx, couleur_hex in enumerate(colors):
                        nom_fichier_sortie = f'{os.path.splitext(fichier_base)[0]}_{os.path.splitext(fichier_masque)[0]}_{idx + 1}.png'
                        chemin_fichier_sortie = os.path.join(chemin_sortie_sous_dossier, nom_fichier_sortie)

                        # Déterminer si cette couleur nécessite du bruit
                        if couleur_hex in colors_avec_bruit:
                            appliquer_effet(chemin_fichier_base, chemin_fichier_masque, couleur_hex, chemin_fichier_sortie, intensite_bruit=0.03)
                        else:
                            appliquer_effet(chemin_fichier_base, chemin_fichier_masque, couleur_hex, chemin_fichier_sortie)

print("Traitement terminé pour tous les masques. Les images ont été sauvegardées dans le dossier output_images.")
