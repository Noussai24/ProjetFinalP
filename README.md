# Projet Final
# MétéoPro

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

## Description de l'api
Cette api web météorologique, développée avec FastAPI, offre des premieres fonctionnalités pour récupérer et analyser des données météorologiques en utilisant l'API de [WeatherAPI](https://www.weatherapi.com/).
## Fonctionnalités
* **Prévisions Météorologiques :** Récupère les prévisions météorologiques des jours à venir pour une ville donnée. *(author: AYADI Noussaiba)*

## Technologies Utilisées
- **Langage de Programmation :** Python
- **Framework Web :** FastAPI
- **API Météorologique :** WeatherAPI
- **Gestion de Versions :** Git, GitHub
- **Intégration Continue :** CircleCI
- **Tests :** pytest (tests unitaires), Postman (tests API), flake8 (qualité du code)
- **Normes de Code :** PEP 8

## Installation

### 1. Clonez le dépôt GitHub
```bash
git clone git@github.com:ImenHzl/ProjetFinal.git
2. Accédez au répertoire du projet
cd ProjetFinal
3. Créez et activez un environnement virtuel
python -m venv env
Pour Windows
.\env\Scripts\activate
4. Installez les dépendances : ils sont regroupés dans un fichier lié à la racine 
pip install -r requirements.txt
Utilisation
1. Lancez le serveur FastAPI
uvicorn mainN:app --reload
2. Accédez à la documentation interactive de l'API
http://127.0.0.1:8000/docs

## Fonctionnement de la fonction foreCast

La fonction foreCast est responsable de récupérer les prévisions météorologiques pour une ville donnée. Elle interagit avec l'API de WeatherAPI pour obtenir les données nécessaires.

1. Fonction foreCast
les bibliothèques nécessaires sont :
**1/ requests : Une bibliothèque Python simple et élégante pour effectuer des requêtes HTTP.
Installation : pip install requests
**2/ json : Une bibliothèque standard Python pour travailler avec des données JSON, elle fait partie de la bibliothèque standard Python.
**3/ os : Une bibliothèque standard Python pour interagir avec le système d'exploitation, elle fait partie de la bibliothèque standard Python.
** fastapi : Un framework web moderne et rapide (hautes performances) pour construire des APIs avec Python 3.7+ basé sur les annotations de type standard Python.
Installation : pip install fastapi
4/ dotenv : Une bibliothèque pour lire les clés d'environnement à partir d'un fichier .env.
Installation : pip install python-dotenv
=======pip install requests fastapi python-dotenv
2. Exécution du script foreCast avec Python
python foreCast.py

locust pour test de charge et nous avons assimiler 10 utilisateur
C:\Users\nouss\POEC\ProjetFinal\tests> locust -f locustfile.py --host=http://127.0.0.1:8000