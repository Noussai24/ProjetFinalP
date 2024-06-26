from fastapi import FastAPI, HTTPException
from app.api.v1.comparateur import get_current_weather, compare_weather, find_best_destination

app = FastAPI()

API_KEY = "61064c6295144de9b63101812242904"


@app.get("/weather/compare/{cities}")
def compare_weather_endpoint(cities: str):
    """
    Compare les conditions météorologiques pour une liste de villes et 
    retourne la ville avec la température la plus élevée.
    """
    city_list = cities.split(",")
    weather_comparison = compare_weather(city_list, API_KEY)
    if not weather_comparison:
        raise HTTPException(status_code=404, detail="Aucune donnée météorologique disponible pour les villes spécifiées.")
    best_destination = find_best_destination(weather_comparison)
    return {"best_destination": best_destination,
            "weather_data": weather_comparison}
