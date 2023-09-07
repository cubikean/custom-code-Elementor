import os

# Récupérez le chemin du répertoire du script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Obtenez ou créez le répertoire "webMatouEndText" s'il n'existe pas déjà
output_directory = os.path.join(script_directory, "webMatouEndText")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Obtenez une liste de tous les fichiers .txt dans le répertoire du script
fichiers_txt = [fichier for fichier in os.listdir(script_directory) if fichier.endswith(".txt")]

# Parcourez tous les fichiers .txt et traitez-les
for fichier_txt in fichiers_txt:
    # Construisez le chemin complet du fichier d'entrée
    chemin_fichier_entree = os.path.join(script_directory, fichier_txt)
    
    # Construisez le nom du fichier de sortie en ajoutant "_essentiel" au nom d'origine
    nom_fichier_sortie = fichier_txt.replace(".txt", "_essentiel.txt")
    chemin_fichier_sortie = os.path.join(output_directory, nom_fichier_sortie)

    # Initialisez une variable pour indiquer si nous devons conserver les lignes
    conserver_lignes = False

    # Initialisez une variable pour stocker les lignes à conserver
    lignes_a_conserver = []

    # Ouvrez le fichier d'entrée en mode lecture
    with open(chemin_fichier_entree, "r") as f_entree:
        lignes = f_entree.readlines()
        
        # Ajoutez la première ligne du fichier à la liste à conserver
        lignes_a_conserver.append(lignes[1])

        # Parcourez chaque ligne du fichier
        for ligne in lignes:
            # Si la ligne commence par "AJOUTER AU PANIER", arrêtez de conserver les lignes
            if ligne.startswith("AJOUTER AU PANIER"):
                break
            
            # Si la ligne commence par "Couleur :", commencez à conserver les lignes
            if ligne.startswith("Couleur :"):
                conserver_lignes = True
            
            # Si nous devons conserver les lignes, ajoutez-les à la liste
            if conserver_lignes:
                lignes_a_conserver.append(ligne)

    # Ouvrez le fichier de sortie en mode écriture
    with open(chemin_fichier_sortie, "w") as f_sortie:
        # Écrivez les lignes à conserver dans le fichier de sortie
        for ligne in lignes_a_conserver:
            f_sortie.write(ligne)
