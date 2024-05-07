# Nom du fichier d'entrée et de sortie
fichier_entree = "labels.txt"
fichier_sortie = "sortie.txt"

# Ouvrir le fichier d'entrée en mode lecture
with open(fichier_entree, 'r') as f_entree:
    # Lire les lignes du fichier
    lignes = f_entree.readlines()

# Liste pour stocker les lignes modifiées
lignes_modifiees = []

# Parcourir chaque ligne pour supprimer les chiffres au début
for ligne in lignes:
    # Tant que le premier caractère de la ligne est un chiffre, le supprimer
    while ligne and ligne[0].isdigit():
        ligne = ligne[1:]
    
    # Ajouter la ligne modifiée à la liste
    lignes_modifiees.append(ligne)

# Ouvrir le fichier de sortie en mode écriture
with open(fichier_sortie, 'w') as f_sortie:
    # Écrire les lignes modifiées dans le fichier de sortie
    f_sortie.writelines(lignes_modifiees)

print("Opération terminée. Les chiffres ont été supprimés des lignes.")