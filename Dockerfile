# Utiliser une image de base officielle de Python
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier tout le code source dans le conteneur
COPY . .

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8000
# Définir la commande de démarrage
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]