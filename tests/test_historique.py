import requests
import json
from app.api.v1.historique import Historique
import pytest
from dotenv import load_dotenv
import os

load_dotenv()
apiKey = os.getenv("My_API")

def test_arroseplante_jour_de_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il pleut tous les jours
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-15"
    endt = "2024-06-15"

    # Exécution de la fonction
    data = Historique.ArrosePlante(apiKey, pays, dt, endt)

    # Vérification du type de retour
    assert isinstance(data, list)

    # Vérification du nombre de jours
    assert len(data) == 1

    # Vérification des données du jour
    assert data[0]["date"] == "2024-06-15"
    assert data[0]["meteo du jour"] == "il pleut"

def test_arroseplante_jour_sans_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il ne pleut pas
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-16"
    endt = "2024-06-16"

    # Exécution de la fonction
    data = Historique.ArrosePlante(apiKey, pays, dt, endt)

    # Vérification du type de retour
    assert isinstance(data, list)

    # Vérification du nombre de jours
    assert len(data) == 1

    # Vérification des données du jour
    assert data[0]["date"] == "2024-06-16"
    assert data[0]["meteo du jour"] == "il pleut"

