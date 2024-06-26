import os
import json
from app.api.v1.foreCast import sauvegarder_donneesforeCast_json, get_weather_forecast
import pytest


def test_sauvegarder_donneesforeCast_json():
    donnees = {
        "example": "data"
    }
    nom_fichier = "test_foreCast.json"
    dossier = "test_data"

    # Appeler la fonction de sauvegarde
    sauvegarder_donneesforeCast_json(donnees, nom_fichier, dossier)

    # Vérifier que le fichier a été créé
    chemin = os.path.join(dossier, nom_fichier)
    assert os.path.exists(chemin)

    # Vérifier le contenu du fichier
    with open(chemin, "r") as file:
        data = json.load(file)
    assert data == donnees

    # Nettoyer le fichier de test
    os.remove(chemin)
    assert not os.path.exists(chemin)


def test_get_weather_forecast():
    city = "Paris"
    api_key = "4c57c92aa17e4b82857172100241506"
    days = 3
    forecast_data = get_weather_forecast(city, api_key, days)

    assert isinstance(forecast_data, list)
    assert len(forecast_data) == 3

    for forecast in forecast_data:
        assert "date" in forecast
        assert "day" in forecast
        assert "avgtemp_c" in forecast["day"]
        assert "condition" in forecast["day"]
        assert "text" in forecast["day"]["condition"]
