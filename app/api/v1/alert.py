import requests
import os
from dotenv import load_dotenv


load_dotenv()
# Charger les variables d'environnement depuis le fichier .env

api_key = os.getenv("api_key")
# Obtenir la clé API depuis les variables d'environnement

def recommandation_vetements(city):
    """
    Donne une recommandation de vêtements en fonction des conditions
    météorologiques.

    Args:
        city (str): Le nom de la ville pour laquelle obtenir la recommandation.

    Returns:
        str: La recommandation de vêtements basée sur les conditions météorologiques.
    """
    # URL de l'API pour les données
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    # Faire une requête GET pour obtenir les données
    response = requests.get(url)
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()

        # Extraire les informations pertinentes des données JSON
        temperature_celsius = data['current']['temp_c']
        condition = data['current']['condition']['text']
        precipitation_mm = data['current']['precip_mm']

        # Déterminer la recommandation de vêt en fonction de la tempér et des conditions météo
        if temperature_celsius < 10:
            return (
                "Il fait plutôt frais à {} avec {}°C. Tu devrais peut-être envisager de "
                "porter quelque chose de chaud !".format(data['location']['name'], temperature_celsius)
            )
        elif 10 <= temperature_celsius < 20:
            if precipitation_mm > 0:
                return (
                    "Il y a {} à {} et il fait {}°C. Prends un parapluie et peut-être un "
                    "pull léger !".format(condition, data['location']['name'], temperature_celsius)
                )
            else:
                return (
                    "À {} il fait {}°C, un t-shirt et une veste légère pourraient être parfaits "
                    "pour toi !".format(data['location']['name'], temperature_celsius)
                )
        else:
            if precipitation_mm > 0:
                return (
                    "Il pleut à {} et il fait {}°C. N'oublie pas ton parapluie !".format(
                        data['location']['name'], temperature_celsius
                    )
                )
            else:
                return (
                    "Il fait chaud à {} avec {}°C. C'est le moment de sortir les shorts et "
                    "les lunettes de soleil !".format(data['location']['name'], temperature_celsius)
                )
    else:
        return None
        # Si la requête a échoué, retourner None
