import pytest
from unittest.mock import patch, MagicMock

# Importez les fonctions à tester depuis le module correct
from app.api.v1.alert import recommandation_vetements, sauvegarder_donneesCurrent_json

# Fixture pour mocker requests.get
@pytest.fixture
def mock_requests_get():
    # Utilisation de patch pour remplacer requests.get par un mock
    with patch('app.api.v1.alert.requests.get') as mock_get:
        yield mock_get

# Fixture pour mocker sauvegarder_donneesCurrent_json
@pytest.fixture
def mock_sauvegarder_donnees():
    # Utilisation de patch pour remplacer sauvegarder_donneesCurrent_json par un mock
    with patch('app.api.v1.alert.sauvegarder_donneesCurrent_json') as mock_sauvegarder:
        yield mock_sauvegarder

# Utilisation de pytest.mark.parametrize pour définir plusieurs cas de test
@pytest.mark.parametrize("api_response, expected_result", [
    # Cas où la température est de 5°C avec un temps clair
    ({
        'location': {'name': 'Paris'},
        'current': {'temp_c': 5, 'condition': {'text': 'Clear'}, 'precip_mm': 0}
    }, "Il fait plutôt frais à Paris avec 5°C. Tu devrais peut-être envisager de porter quelque chose de chaud !"),
    # Cas où la température est de 15°C avec un temps partiellement nuageux sans précipitations
    ({
        'location': {'name': 'Paris'},
        'current': {'temp_c': 15, 'condition': {'text': 'Partly cloudy'}, 'precip_mm': 0}
    }, "À Paris il fait 15°C, un t-shirt et une veste légère pourraient être parfaits pour toi !"),
    # Cas où la température est de 15°C avec un temps partiellement nuageux et des précipitations
    ({
        'location': {'name': 'Paris'},
        'current': {'temp_c': 15, 'condition': {'text': 'Partly cloudy'}, 'precip_mm': 5}
    }, "Il y a Partly cloudy à Paris et il fait 15°C. Prends un parapluie et peut-être un pull léger !"),
    # Cas où la température est de 25°C avec un temps ensoleillé
    ({
        'location': {'name': 'Paris'},
        'current': {'temp_c': 25, 'condition': {'text': 'Sunny'}, 'precip_mm': 0}
    }, "Il fait chaud à Paris avec 25°C. C'est le moment de sortir les shorts et les lunettes de soleil !"),
    # Cas où la température est de 25°C avec de la pluie
    ({
        'location': {'name': 'Paris'},
        'current': {'temp_c': 25, 'condition': {'text': 'Rain'}, 'precip_mm': 10}
    }, "Il pleut à Paris et il fait 25°C. N'oublie pas ton parapluie !")
])
def test_recommandation_vetements(mock_requests_get, mock_sauvegarder_donnees, api_response, expected_result):
    # Configurer le mock pour requests.get pour retourner une réponse fictive
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = api_response
    mock_requests_get.return_value = mock_response

    # Appeler la fonction avec une ville fictive
    result = recommandation_vetements('Paris')

    # Vérifier que sauvegarder_donneesCurrent_json a été appelé correctement
    mock_sauvegarder_donnees.assert_called_once_with(api_response, 'currentMet_Paris.json', 'data')

    # Vérifier que le résultat est celui attendu
    assert result == expected_result
