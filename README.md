# Projet final
# MétéoPro


[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

## Description 
Cette application web météorologique, développée avec FastAPI, offre une gamme complète de fonctionnalités pour récupérer et analyser des données météorologiques grâce à l'API de https://www.weatherapi.com/. Elle fournit des prévisions météorologiques, des recommandations vestimentaires, des données historiques et astronomiques, ainsi que des comparaisons de températures entre différentes villes.

## Fonctionnalités
* Recommandations Vestimentaires : Envoie des alertes avec des recommandations vestimentaires basées sur la température actuelle.(author: TAIF Yasmina)
* Données Météorologiques Historiques : Permet de récupérer les données météorologiques passées pour déterminer si vous devez arroser vos plantes (author: ARJOUN Imen).
* Données Astronomiques : Fournit les heures de lever et de coucher du soleil pour une ville donnée (author: BAYOUDH Fadwa).
* Comparaison des Températures des Villes : Compare les températures de différentes villes et recommande la meilleure destination pour les vacances (author: BOUHIDEL Salim).
* Prévisions Météorologiques : Récupère les prévisions météorologiques des jours à venir pour une ville donnée (author: AYADI Noussaiba ).


## Technologies Utilisées
- Langage de Programmation : Python
- Framework Web : FastAPI
- API Météorologique : WeatherAPI
- Gestion de Versions : Git, GitHub
- Intégration Continue : CircleCI
- Tests : pytest (tests unitaires), Postman (tests API), flake8 (qualité du   code)
- Normes de Code : PEP 8

### Installation

##### 1- Clonez le dépôt GitHub : 
git clone git@github.com:ImenHzl/ProjetFinal.git
##### 2- Accédez au répertoire du projet :
cd ProjetFinal
##### 3- Créez et activez un environnement virtuel
python -m venv env
- activer le venv:
Pour Windows
.\venv\Scripts\activate
Pour macOS/Linux
source env/bin/activate




##### 4- Installez les dépendances :

- pip install pipreqs
- pipreqs ./


## Utilisation
##### 1- lancez le serveur FastAPI :
uvicorn app.main:app --reload
##### 2- Accédez à la documentation interactive de l'API :
http://127.0.0.1:8000/docs


## Tests
##### 1- Pour exécutez les tests unitaires :
pytest
##### 2- Pour vérifier la qualité du code avec flake8 :
Installez dans l'environnement virtuel:
pip install flake8 flake8-html
flake8
Pour générer le rapport HTML, exécutez la commande suivante :
flake8 --format=html --htmldir=flake8-report

##### 3- Pour exécuter les tests de performance et les tests API: 
L'outil "Postman".
## Versions
Listez les versions ici 
_exemple :_
**Dernière version stable :** 5.0
**Dernière version :** 5.1
Liste des versions : [Cliquer pour afficher](https://github.com/your/project-name/tags)
_(pour le lien mettez simplement l'URL de votre projets suivi de ``/tags``)_

## Auteurs

* **TAIF Yasmina**
* **ARJOUN Imen**
* **Bayoudh Fadwa**
* **BOUHIDEL Salim**
* **AYYADI NOUSSAIBA**

###### Lien vers la répository de projet: https://github.com/ImenHzl/ProjetFinal.git .



