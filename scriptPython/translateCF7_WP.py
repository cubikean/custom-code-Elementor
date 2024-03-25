# -*- coding: utf-8 -*-

import pyautogui
import keyboard
import time

# Votre liste de mots
words = """
Merci pour votre message. Il a été envoyé.
Une erreur s'est produite lors de l'envoi de votre message. Veuillez réessayer plus tard.
Une erreur s'est glissée dans un ou plusieurs champs. Veuillez vérifier et réessayer.
Une erreur s'est produite lors de l'envoi de votre message.Veuillez réessayer plus tard.
Vous devez accepter les termes et conditions avant d'envoyer votre message.
Veuillez remplir ce champ.
Ce champ a une entrée trop longue.
Ce champ a une entrée trop courte.
Une erreur inconnue s'est produite lors du téléchargement du fichier.
Vous n'êtes pas autorisé à télécharger des fichiers de ce type.
Le fichier téléchargé est trop volumineux.
Une erreur s'est produite lors du téléchargement du fichier.
Veuillez saisir une date au format AAAA-MM-JJ.
La date de ce champ est trop tôt.
La date de ce champ est trop tardive.
Veuillez saisir un numéro.
Le chiffre de ce champ est trop petit.
Ce champ a un numéro trop long.
La réponse à la question est incorrecte.
Veuillez saisir votre adresse e-mail.
Veuillez saisisr une URL
Veuillez saisir un numéro de téléphone.

"""

# Split la liste en lignes
lines = words.split('\n')
time.sleep(2)

# Boucle sur chaque ligne
for line in lines:
    # Si la ligne est vide, passe a la suivante
    if not line.strip():
        continue

    # emule la frappe de la ligne
    keyboard.write(line)

    # # Appuie sur Enter
    # pyautogui.press('enter')
    # time.sleep(.1)

    # line_count += 1
    # Si ce n'est pas la derniere ligne, ajoute 5 tabulations
    # if line_count % 4 == 0:
    keyboard.press_and_release('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # line_count = 0
    time.sleep(.1)

    # Attend un court moment pour la lisibilite
    time.sleep(.1)



