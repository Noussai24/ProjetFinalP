import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from app.api.v1.foreCast import get_weather_forecast  # Import relatif correct
import os
load_dotenv()

app = FastAPI()

api_key = os.getenv('API_KEY', '70cb525479934787a59201748242606')

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prévisions météorologiques"}



@app.get("/forecast/{city}")
def fetch_forecast(city: str):
    try:
        forecast_data = get_weather_forecast(city, 3)
        processed_data = [
            {
                "Date": forecast['date'],
                "Température moyenne": forecast['day']['avgtemp_c'],
                "Conditions météorologiques": forecast['day']['condition']['text'],
            } for forecast in forecast_data
        ]
        return {
            "Ville": city,
            "Prévisions": processed_data
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))