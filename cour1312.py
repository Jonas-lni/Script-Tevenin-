#!/usr/bin/env python3

import sys

def generate_emails():
    print("Entrez des noms et prénoms séparés par des ';' :")
    input_data = sys.stdin.read().strip()

    # Séparer les différentes paires de noms et prénoms
    pairs = input_data.split(';')
    emails = []

    for pair in pairs:
        # Ignorer les entrées vides
        if not pair.strip():
            continue

        try:
            prenom, nom = pair.strip().split()
        except ValueError:
            print(f"Erreur de format pour l'entrée : '{pair.strip()}'. Format attendu : 'prenom nom'.")
            continue

        # Générer l'adresse email
        email = f"{prenom.lower()}.{nom.lower()}@eecs.fr"
        emails.append(email)

    # Afficher les emails générés
    print("\nAdresses email générées :")
    for email in emails:
        print(email)

if __name__ == "__main__":
    generate_emails()

# j'ai juste un commentaire 
