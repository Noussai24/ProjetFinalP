import requests
import os
import json


def sauvegarder_donneesCurrentComp_json(donnees, nom_fichier, dossier):
    """
    Sauvegarde les données dans un fichier JSON.

    Args:
        donnees (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
        dossier (str): Le dossier où le fichier JSON sera sauvegardé.
    """
    # Chemin complet du fichier JSON
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "w") as json_file:
        # Écrit les données au format JSON avec indentation
        json.dump(donnees, json_file, indent=4)


def get_current_weather(city, api_key):
    """
    Récupère les données météorologiques actuelles pour une ville donnée.

    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données.
        api_key (str): La clé API pour accéder aux données de l'API WeatherAPI.

    Returns:
        dict: Les données météorologiques actuelles pour la ville spécifiée.
    """
    # URL de l'API pour les données météorologiques actuelles
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    # Faire une requête GET pour obtenir les données
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()
        # Retourner les données météorologiques actuelles
        return data
    else:
        # Si la requête échoue, afficher un message d'erreur
        print(f"Erreur lors de la récupération des données météorologiques pour {city}: {response.status_code}")
        # Retourner None si les données météorologiques ne sont pas disponibles
        return None


def compare_weather(cities, api_key):
    """Compare les conditions météorologiques actuelles pour plusieurs villes.

    Args:
        cities (list): Une liste de noms de villes à comparer.
        api_key (str): La clé d'API pour accéder
        aux données de l'API WeatherAPI.

    Returns:
        dict: Un dictionnaire contenant les données météorologiques actuelles
        pour chaque ville comparée.
    """
    # Initialiser un dictionnaire pour stocker les données météorologiques
    weather_data = {}

    # Parcourir chaque ville dans la liste
    for city in cities:
        # Récupérer les données météorologiques actuelles pour la ville
        data = get_current_weather(city, api_key)
        # Vérifier si les données sont disponibles
        if data:
            # Ajouter les données au dictionnaire de comparaison
            weather_data[city] = {
                "temperature": data["current"]["temp_c"],
                "conditions": data["current"]["condition"]["text"]
            }

    # Sauvegarder les données dans un fichier JSON
    sauvegarder_donneesCurrentComp_json(weather_data, "compare.json", "data")

    # Retourner le dictionnaire contenant les données
    return weather_data


def find_best_destination(weather_data):
    """
    Trouve la ville avec la température la plus élevée.

    Args:
        weather_data (dict): Les données météorologiques
        actuelles pour chaque ville.

    Returns:
        str: Le nom de la ville avec la température la plus élevée.
    """
    if not weather_data:
        return None

    # Trouver la ville avec la température la plus élevée
    best_city = max(weather_data, key=lambda city: weather_data[city]["temperature"])
    return best_city

# Clé API WeatherAPI


api_key = "61064c6295144de9b63101812242904"

# Liste des villes à comparer
cities_to_compare = ["Paris", "London", "nice", "bamako", "melbourn", "jeddah"]

# Comparaison des conditions météorologiques
weather_comparison = compare_weather(cities_to_compare, api_key)

# Affichage des résultats
for city, data in weather_comparison.items():
    print(f"Conditions météorologiques actuelles à {city}:")
    print(f"Température: {data['temperature']}°C")
    print(f"Conditions: {data['conditions']}")
    print()

# Trouver et afficher la meilleure destination
best_destination = find_best_destination(weather_comparison)
if best_destination:
    print(f"La meilleure destination est la ville: {best_destination}")
else:
    print("Aucune donnée météorologique disponible.")
