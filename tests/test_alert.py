import pytest
from unittest.mock import patch
import requests
from app.api.v1.alert import recommandation_vetements


def test_recommandation_vetements_froid(mocker):
    """
    Teste la recommandation pour une température froide.
    """
    # Mock la réponse de l'API pour une température froide
    mock_response = {
        'location': {'name': 'Paris'},
        'current': {
            'temp_c': 5,
            'condition': {'text': 'Sunny'},
            'precip_mm': 0
        }
    }
    # Mock la réponse de requests.get pour retourner mock_response
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response

    # Résultat attendu pour cette température et ces conditions
    expected_result = "Il fait plutôt frais à Paris avec 5°C. Tu devrais peut-être envisager de porter quelque chose de chaud !"
    # Vérifie que la fonction retourne bien le résultat attendu
    assert recommandation_vetements('Paris') == expected_result


def test_recommandation_vetements_printemps_avec_pluie(mocker):
    """
    Teste la recommandation pour une température printanière avec pluie.
    """
    # Mock la réponse de l'API pour une température printanière avec pluie
    mock_response = {
        'location': {'name': 'Lyon'},
        'current': {
            'temp_c': 15,
            'condition': {'text': 'Rain'},
            'precip_mm': 5
        }
    }
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response

    # Résultat attendu pour cette température et ces conditions
    expected_result = "Il y a Rain à Lyon et il fait 15°C. Prends un parapluie et peut-être un pull léger !"
    # Vérifie que la fonction retourne bien le résultat attendu
    assert recommandation_vetements('Lyon') == expected_result


def test_recommandation_vetements_printemps_sans_pluie(mocker):
    """
    Teste la recommandation pour une température printanière sans pluie.
    """
    # Mock la réponse de l'API pour une température printanière sans pluie
    mock_response = {
        'location': {'name': 'Marseille'},
        'current': {
            'temp_c': 18,
            'condition': {'text': 'Cloudy'},
            'precip_mm': 0
        }
    }
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response

    # Résultat attendu pour cette température et ces conditions
    expected_result = "À Marseille il fait 18°C, un t-shirt et une veste légère pourraient être parfaits pour toi !"
    # Vérifie que la fonction retourne bien le résultat attendu
    assert recommandation_vetements('Marseille') == expected_result


def test_recommandation_vetements_chaud_avec_pluie(mocker):
    """
    Teste la recommandation pour une température chaude avec pluie.
    """
    # Mock la réponse de l'API pour une température chaude avec pluie
    mock_response = {
        'location': {'name': 'Nice'},
        'current': {
            'temp_c': 25,
            'condition': {'text': 'Rain'},
            'precip_mm': 10
        }
    }
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response

    # Résultat attendu pour cette température et ces conditions
    expected_result = "Il pleut à Nice et il fait 25°C. N'oublie pas ton parapluie !"
    # Vérifie que la fonction retourne bien le résultat attendu
    assert recommandation_vetements('Nice') == expected_result


def test_recommandation_vetements_chaud_sans_pluie(mocker):
    """
    Teste la recommandation pour une température chaude sans pluie.
    """
    # Mock la réponse de l'API pour une température chaude sans pluie
    mock_response = {
        'location': {'name': 'Toulouse'},
        'current': {
            'temp_c': 30,
            'condition': {'text': 'Sunny'},
            'precip_mm': 0
        }
    }
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response

    # Résultat attendu pour cette température et ces conditions
    expected_result = "Il fait chaud à Toulouse avec 30°C. C'est le moment de sortir les shorts et les lunettes de soleil !"
    # Vérifie que la fonction retourne bien le résultat attendu
    assert recommandation_vetements('Toulouse') == expected_result


def test_recommandation_vetements_requete_echoue(mocker):
    """
    Teste le cas où la requête échoue.
    """
    # Mock la réponse de requests.get pour simuler une requête échouée
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.status_code = 404

    # Vérifie que la fonction retourne None en cas de requête échouée
    assert recommandation_vetements('InvalidCity') is None
