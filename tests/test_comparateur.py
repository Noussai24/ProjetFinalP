
import pytest
from unittest.mock import patch
from app.api.v1.comparateur import compare_weather, find_best_destination

# Données météorologiques fictives pour les villes
city_data = {
    "Paris": {
        "temperature": 22.5,
        "conditions": "Ciel nuageux"
    },
    "Londres": {
        "temperature": 18.2,
        "conditions": "Pluie légère"
    },
    "Nice": {
        "temperature": 25.8,
        "conditions": "Ensoleillé"
    },
    "Bamako": {
        "temperature": 32.1,
        "conditions": "Chaud et sec"
    }
}

# Clé API fictive
api_key = "api_key_fictive"

# Liste des villes à comparer
cities_to_compare = ["Paris", "Londres", "Nice", "Bamako"]


def mock_get_current_weather(city, api_key):

    """Fonction simulée pour get_current_weather"""
    return {"current": {"temp_c": city_data[city]["temperature"],
                        "condition": {"text": city_data[city]["conditions"]}}}


@pytest.fixture
def patch_get_current_weather():
    """Fixture pour remplacer get_current_weather par la fonction simulée"""
    with patch("app.api.v1.comparateur.get_current_weather",
               mock_get_current_weather):
        yield


def test_compare_weather(patch_get_current_weather):
    """Tester la fonction compare_weather"""
    weather_data = compare_weather(cities_to_compare, api_key)

    # Vérifier les résultats attendus
    assert weather_data["Paris"]["temperature"] == 22.5
    assert weather_data["Londres"]["conditions"] == "Pluie légère"
    assert weather_data["Nice"]["temperature"] == 25.8
    assert weather_data["Bamako"]["conditions"] == "Chaud et sec"


def test_find_best_destination():
    """Tester la fonction find_best_destination"""
    weather_data = {
        "Paris": {
            "temperature": 22.5,
            "conditions": "Ciel nuageux"
        },
        "Londres": {
            "temperature": 18.2,
            "conditions": "Pluie légère"
        },
        "Nice": {
            "temperature": 25.8,
            "conditions": "Ensoleillé"
        },
        "Bamako": {
            "temperature": 32.1,
            "conditions": "Chaud et sec"
        }
    }

    # Meilleure destination avec des données complètes
    best_destination = find_best_destination(weather_data)
    assert best_destination == "Bamako"

    # Aucune destination avec des données vides
    weather_data = {}
    best_destination = find_best_destination(weather_data)
    assert best_destination is None
