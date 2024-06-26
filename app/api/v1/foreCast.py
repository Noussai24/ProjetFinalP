import requests
import json
import os
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

api_key = os.getenv('api_key')


def sauvegarder_donneesforeCast_json(donnees, nom_fichier, dossier):
    # Utiliser le répertoire de travail actuel
    chemin_complet_dossier = os.path.join(os.getcwd(), dossier)
    os.makedirs(chemin_complet_dossier, exist_ok=True)
    chemin = os.path.join(chemin_complet_dossier, nom_fichier)

    with open(chemin, "w") as json_file:
        json.dump(donnees, json_file, indent=4)
    print(f"Le fichier JSON a été sauvegardé à : {chemin}")


def get_weather_forecast(city, api_key, days):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": city,
        "days": days
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if 'forecast' in data:
        forecast_data = data['forecast']['forecastday']
        sauvegarder_donneesforeCast_json(data, "foreCast.json", "data")
        return forecast_data
    else:
        raise HTTPException(
            status_code=404,
            detail="Impossible de récupérer les données de prévision.")


@router.get("/forecast")
async def get_forecast(city: str, days: int = 3):
    forecast_data = get_weather_forecast(city, api_key, days)
    return forecast_data

# Test de l'exécution directe pour la fonctionnalité CLI
if __name__ == "__main__":
    city = 'Paris'
    days = 3
    forecast_data = get_weather_forecast(city, api_key, days)

    for forecast in forecast_data:
        date = forecast['date']
        avg_temp_c = forecast['day']['avgtemp_c']
        condition_text = forecast['day']['condition']['text']

        print("Date:", date)
        print("Température moyenne:", avg_temp_c, "°C")
        print("Conditions météorologiques:", condition_text)
        print()