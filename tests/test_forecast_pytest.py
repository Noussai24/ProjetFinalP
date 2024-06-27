import unittest
import responses
import os
import sys

# Ajoutez le chemin du projet à sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi import HTTPException
from app.api.v1.foreCast import get_weather_forecast

class TestWeatherForecast(unittest.TestCase):

    @responses.activate
    def test_get_weather_forecast_success(self):
        api_key = '70cb525479934787a59201748242606'
        city = 'Paris'
        days = 3

        # Mocking the API response
        responses.add(
            responses.GET,
            f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}",
            json={
                "forecast": {
                    "forecastday": [
                        {
                            "date": "2024-06-28",
                            "day": {
                                "avgtemp_c": 23.5,
                                "condition": {
                                    "text": "Sunny"
                                }
                            }
                        },
                        {
                            "date": "2024-06-29",
                            "day": {
                                "avgtemp_c": 24.5,
                                "condition": {
                                    "text": "Partly cloudy"
                                }
                            }
                        },
                        {
                            "date": "2024-06-30",
                            "day": {
                                "avgtemp_c": 22.5,
                                "condition": {
                                    "text": "Rain"
                                }
                            }
                        }
                    ]
                }
            },
            status=200
        )

        forecast_data = get_weather_forecast(city, days)
        self.assertEqual(len(forecast_data), 3)
        self.assertEqual(forecast_data[0]['date'], "2024-06-28")
        self.assertEqual(forecast_data[0]['day']['avgtemp_c'], 23.5)
        self.assertEqual(forecast_data[0]['day']['condition']['text'], "Sunny")

    @responses.activate
    def test_get_weather_forecast_failure(self):
        api_key = '70cb525479934787a59201748242606'
        city = 'Paris'
        days = 3

        # Mocking the API response
        responses.add(
            responses.GET,
            f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}",
            json={
                "error": {
                    "code": 1006,
                    "message": "No matching location found."
                }
            },
            status=400
        )

        with self.assertRaises(HTTPException) as context:
            get_weather_forecast(city, days)
        
        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Erreur lors de la requête à l'API : 400")

if __name__ == '__main__':
    unittest.main()
