# Lecture du fichier des labels
with open('sortie.txt', 'r') as file:
    labels = file.read().strip().split('\n')

# Ajout d'un ';' à la fin de chaque ligne
# labels = [line + ';' for line in labels]

# Lecture du fichier CSV
with open('output.csv', 'r') as file:
    raw_csv = file.read()

# Ajout des labels au début du fichier CSV
labels_line = ';'.join(labels)
output_txt = labels_line + '\n' + raw_csv

# Création du fichier de sortie
with open('output.txt', 'w') as file:
    file.write(output_txt)

# Lecture du fichier de sortie pour remplacer '!#' par ';' et des guillemets
with open('output.txt', 'r') as file:
    content = file.read()

# Remplacement des '!#' par ';'
content = content.replace('!#', ';')

# Écriture du fichier avec les modifications
with open('output.txt', 'w') as file:
    file.write(content)

print("Traitement terminé. Le fichier 'output.txt' a été créé avec succès.")
