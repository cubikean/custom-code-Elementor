#!/usr/bin/env python
from flask import Flask
import os
import time
import shutil

app = Flask(__name__)

class Watcher:
    @staticmethod
    def process():
        """
        Process the event, in this case, execute your script.
        """
        # Check if the file Annonces.csv exists
        if os.path.exists('Annonces.csv'):
            # Run your script
            print('Traitement du fichier Annonces.csv')
            Watcher.run_scripts()

            # Rename the processed file with timestamp
            timestamp = time.strftime("%Y%m%d%H%M%S")
            new_name = f'annonces_{timestamp}.csv'
            os.rename('Annonces.csv', new_name)

            # Move the processed file to 'pastAnnonces' folder
            past_folder = 'pastAnnonces'
            if not os.path.exists(past_folder):
                os.makedirs(past_folder)
            
            shutil.move(new_name, os.path.join(past_folder, new_name))

    @staticmethod
    def run_scripts():
        """
        Execute the cronAnnoncesModifier.py script.
        """
        # Lecture du fichier pour remplacer !# par ;
        with open('Annonces.csv', 'r') as file:
            content = file.read()

        # Remplacement des "{!#}" par ;
        content = content.replace('!#', ';')
        content = content.replace('"', '')

        # Écriture du fichier avec les modifications dans le dossier 'output'
        output_folder = 'output'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = os.path.join(output_folder, 'Annonces.txt')

        with open(output_file_path, 'w') as file:
            file.write(content)

    @app.route('/run_scripts')
    def run_scripts_endpoint():
        """
        Endpoint to run the scripts.
        """
        Watcher.process()
        return 'Scripts exécutés avec succès !', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
