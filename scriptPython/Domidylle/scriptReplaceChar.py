# Liste des labels
labels = [
    "Identifiant agence",
    "Référence agence du bien",
    "Type d'annonce",
    "Type de bien",
]

# Nouvelle chaîne CSV
raw_csv = '''"transaction"!#"1"!#"Vente"!#"maison/villa"'''

# Ajout de la ligne de labels au début sans le premier ;
labels_line = ';'.join(labels)
output_txt = labels_line + '\n' + raw_csv[1:]

# Création du fichier texte
with open('output.txt', 'w') as file:
    file.write(output_txt)

# Lecture du fichier pour remplacer !# par ;
with open('output.txt', 'r') as file:
    content = file.read()

# Remplacement des "{!#}" par ;
content = content.replace('!#', ';')
content = content.replace('"', '')

# Écriture du fichier avec les modifications
with open('output.txt', 'w') as file:
    file.write(content)
