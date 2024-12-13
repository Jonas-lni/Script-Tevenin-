#!/bin/bash

# Vérifie si un nom de fichier a été fourni
if [ -z "$1" ]; then
    echo "Usage: $0 <nom_du_fichier> [python_version]"
    echo "Exemple: $0 mon_script.py python3"
    exit 1
fi

# Nom du fichier à créer
filename="$1"

# Ajoute l'extension .py si elle est absente
if [[ "$filename" != *.py ]]; then
    filename="$filename.py"
fi

# Version de Python (par défaut python3)
python_version="${2:-python3}"
