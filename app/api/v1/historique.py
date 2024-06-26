import requests
from dotenv import load_dotenv
import os
import json

class Historique:
    load_dotenv()
    apiKey = os.getenv("api_key")

    @staticmethod
    def enregistrerJson(infoplay):
        """Cette fonction permet de créer un fichier JSON et
        de l'enregistrer.
        Params:
            infoplay: Les données JSON
        """
        with open("data/dataHistorique.json", "w") as jsonFile:
            json.dump(infoplay, jsonFile, indent=4)

    @staticmethod
    def ArrosePlante(pays, dt, endt):
        """
        Cette fonction permet de récupérer la prévision météorologique
        à partir d'une date.
        Params:
            pays: Choisir un pays
            dt: Date de début
            endt: Date de fin
        Return:
            Liste de dictionnaires contenant les prévisions
        """
        urlbase = f"https://api.weatherapi.com/v1/history.json?key={Historique.apiKey}&q={pays}&dt={dt}&end_dt={endt}"
        try:
            response = requests.get(urlbase)
            if response.status_code == 200:
                print("La requête a réussi (200 OK)")
                data = response.json()
                dates = []
                for forecast in data['forecast']['forecastday']:
                    date = forecast['date']
                    prevision = forecast['day']['daily_will_it_rain']
                    if prevision == 0:
                        meteo = "il pleut pas il faut arroser les plantes"
                    else:
                        meteo = "il pleut"
                    dates.append({"date": date, "meteo du jour": meteo})
                Historique.enregistrerJson(dates)
                return dates
            else:
                print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Une erreur s'est produite lors de la requête à l'API :", e)
        except ValueError as e:
            print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
        return []

# Pour tester la fonction en dehors de FastAPI
if __name__ == "__main__":
    apiKey = os.getenv("My_API")
    pays = "France"
    dt = "2024-06-15"
    endt = "2024-06-17"
    reponse = Historique.ArrosePlante(pays, dt, endt)
    print(reponse)
