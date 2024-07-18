# Naviguez vers votre dossier de projet
cd C:\Users\Lucie\Documents\Projets_Git\SpaceX-Launch-Dashboard\SpaceX-Launch-Dashboard

# Créez un environnement virtuel
python -m venv env

# Activez l'environnement virtuel sous Windows
.\env\Scripts\activate


# Installez Django et Graphene-Django
pip install --upgrade pip
pip install django graphene-django

# Créez un nouveau projet Django
django-admin startproject spacex_dashboard .

# Créez une nouvelle application Django
python manage.py startapp launches

# Run le server
python manage.py runserver