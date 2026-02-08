# Utiliser une image Python légère officielle
FROM python:3.9-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY src/ ./src/
COPY data/ ./data/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut au lancement du conteneur
CMD ["python", "src/main.py"]
