import os
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def rename_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = remove_accents(filename)
            new_filename = new_filename.replace(' ', '_')
            new_filename = new_filename.replace('-', '_')

            if filename != new_filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f'Renamed: {filename} -> {new_filename}')

# Remplacez "votre_repertoire" par le chemin du répertoire où se trouvent vos fichiers à renommer.
rename_files(r'C:\Users\Beekom\Desktop\dev\INSITU\docs\images\images_end')
