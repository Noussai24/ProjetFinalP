import requests
import json
import os
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

api_key = os.getenv('API_KEY', '70cb525479934787a59201748242606')



def sauvegarder_donneesforeCast_json(donnees, nom_fichier, dossier):
    # Utiliser le répertoire de travail actuel
    chemin_complet_dossier = os.path.join(os.getcwd(), dossier)
    os.makedirs(chemin_complet_dossier, exist_ok=True)
    chemin = os.path.join(chemin_complet_dossier, nom_fichier)

    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)
    print(f"Le fichier JSON a été sauvegardé à : {chemin}")


def get_weather_forecast(city, days=3):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": city,
        "days": days
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'forecast' in data:
            forecast_data = data['forecast']['forecastday']
            return forecast_data
        else:
            raise HTTPException(
                status_code=404,
                detail="Impossible de récupérer les données de prévision.")
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Erreur lors de la requête à l'API : {response.status_code}"
        )