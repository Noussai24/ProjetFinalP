from fastapi import FastAPI, HTTPException
from app.api.v1.historique import Historique
from app.api.v1.alert import recommandation_vetements 
from app.api.v1.comparateur import  compare_weather, find_best_destination
from app.api.v1.Fonction_Astro import get_sunrise_sunset
from app.api.v1.foreCast import get_weather_forecast


app = FastAPI()

@app.get("/")
# Route de base

def read_root():
    
    # Route de base qui retourne un message de bienvenue.
    return {"message": "Bienvenue sur l'App méteoPro !"}

@app.get("/recommandation/{city}")
# Route pour obtenir la recommandation de vêtements basée sur la météo
def get_recommandation(city: str):
    try:
        print("Hello, world! : " +city )
        recommendation = recommandation_vetements(city)
        # Appeler la fonction pour obtenir la recommandation de vêtements
        if recommendation.startswith("Erreur"):
        # Vérifier si la recommandation contient une erreur
            raise HTTPException(status_code=400, detail=recommendation)
        return {"city": city, "recommendation": recommendation}
        # Retourner la recommandation dans un format JSON
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # Lever une exception HTTP avec le code 500 en cas d'erreur 


@app.get("/historique/{pays}/{dt}/{endt}")
def read_root(pays:str, dt:str, endt:str):
    try:
        datameteo = Historique.ArrosePlante( pays, dt, endt)
        if datameteo is not None:
            # Retourner directement les données sans conversion en chaîne JSON
            return datameteo
        else:
            raise HTTPException(status_code=500, detail="Erreur lors de la récupération des données météorologiques")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/weather/compare/{cities}")
def compare_weather_endpoint(cities: str):
    """
    Compare les conditions météorologiques pour une liste de villes et 
    retourne la ville avec la température la plus élevée.
    """
    city_list = cities.split(",")
    weather_comparison = compare_weather(city_list)
    if not weather_comparison:
        raise HTTPException(status_code=404, detail="Aucune donnée météorologique disponible pour les villes spécifiées.")
    best_destination = find_best_destination(weather_comparison)
    return {"best_destination": best_destination,
            "weather_data": weather_comparison}


@app.get("/heures/{city}")
def read_root(city: str):
    try:
        sunrise, sunset = get_sunrise_sunset(city)
        if sunrise and sunset:
            return {f"L'heure de lever et coucher de soleil à":city, "est": sunrise, "et":sunset}
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/forecast/{pays}/{days}")
def read_root(pays: str, days:int):
    try:
        dataforecast = get_weather_forecast( pays, days)
        if dataforecast is not None:
            # Retourner directement les données sans conversion en chaîne JSON
            return dataforecast
        else:
            raise HTTPException(status_code=500, detail="Erreur lors de la récupération des données météorologiques")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))