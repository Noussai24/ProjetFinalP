import pytest
import json
import os
from unittest.mock import patch, mock_open

from app.api.v1.Fonction_Astro import sauvegarder_heures_soleil, get_sunrise_sunset


@pytest.fixture
def sample_data():
    return json.loads('{"sunrise": "05:00 AM", "sunset": "07:00 PM"}')


def test_sauvegarder_heures_soleil(sample_data):
    mock_file = mock_open()
    with patch("builtins.open", mock_file):
        sauvegarder_heures_soleil(sample_data, "test_sunrise_sunset.json")
        mock_file.assert_called_once_with(os.path.join("data", "test_sunrise_sunset.json"), "w")


@patch("requests.get")
def test_get_sunrise_sunset(mock_get, sample_data):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    mock_get.return_value = MockResponse({"astronomy": {"astro": sample_data}}, 200)

    api_key = "fake_api_key"
    city = "Paris"
    sunrise, sunset = get_sunrise_sunset(city, api_key)

    assert sunrise == "05:00 AM"
    assert sunset == "07:00 PM"


@patch("requests.get")
def test_get_sunrise_sunset_failure(mock_get):
    mock_get.return_value = MockResponse(None, 404)

    api_key = "fake_api_key"
    city = "Paris"
    sunrise, sunset = get_sunrise_sunset(city, api_key)

    assert sunrise is None
    assert sunset is None


class MockResponse:

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
