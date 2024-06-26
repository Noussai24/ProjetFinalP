import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv('api_key')

def sauvegarder_heures_soleil(data, nom_fichier):
    """
    Sauvegarde les heures de lever et de coucher du soleil
    dans un fichier JSON.

    Args:
        data (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
# Chemin du fichier dans le dossier "data"
    chemin = os.path.join("data", nom_fichier)
    with open(chemin, "w") as json_file:
        json.dump(data, json_file, indent=4)


def get_sunrise_sunset(city):
    """
    Récupère l'heure du lever et du coucher du soleil pour une ville donnée.

    Args:
        city (str): Le nom de la ville pour laquelle récupérer les données.
        api_key (str): La clé d'API pour accéder au service d'astronomie.

    Returns:
        str: L'heure du lever du soleil.
        str: L'heure du coucher du soleil.
    """
    # URL de l'API pour les données astronomiques
    url = f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={city}"
    # Faire une requête GET pour obtenir les données astronomiques
    response = requests.get(url)
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()
        # Récupérer les données d'astronomie
        astronomy_data = data.get("astronomy", {})
        # Vérifier si les données d'astronomie sont présentes
        if astronomy_data:
            sunrise = astronomy_data["astro"]["sunrise"]
            sunset = astronomy_data["astro"]["sunset"]
            # Sauvegarde des données dans un fichier JSON
            sauvegarder_heures_soleil({"sunrise": sunrise, "sunset": sunset}, "sunrise_sunset.json")
            # Retourner les heures de lever et de coucher du soleil
            return sunrise, sunset
    else:
        print(f"Erreur lors de la récupération des données astronomiques:{response.status_code}")
        # Retourner None pour chaque heure de lever et de coucher du soleil
        return None, None



city = "Paris"
# Appel à la fonction get_sunrise_sunset pour récupérer
# les heures de lever et de coucher du soleil
sunrise, sunset = get_sunrise_sunset(city)

# Affichage des heures de lever et de coucher du soleil si sont dispo
if sunrise is not None:
    print(f"Heure du lever du soleil à {city}: {sunrise}")
    print(f"Heure du coucher du soleil à {city}: {sunset}")
