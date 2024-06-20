import requests
from dotenv import load_dotenv
import os
import json

class Historique:
    load_dotenv()
    apiKey = os.getenv("My_API")
    
    """cette fonction permet de créer un fichier json et les enregistrer dans un fichier json
        params: 
            infoplay: les donnees json
    """
    @staticmethod
    def enregistrerJson(infoplay):
        with open("data/dataLeague.json", "w") as jsonFile:
            json.dump(infoplay, jsonFile, indent=4)

    """
        cette fonction permet de récuperer la prévision metrologique a partir d'une date
            params:
                apikey: key api 
                pays: choisir une pays
                dt: date de début
                endt: date de fin
            return:
                jsonString: donnes en format json
    """
    @staticmethod
    def ArrosePlante(apiKey, pays, dt, endt):
        urlbase=f"https://api.weatherapi.com/v1/history.json?key={apiKey}&q={pays}&dt={dt}&end_dt={endt}"
        response = requests.get(urlbase)
        jsonString = None     
        try:
            if response.status_code == 200:
                print("La requête a réussi (200 OK)")
                # Traitez la réponse ici
                data = response.json()
                # Liste pour stocker les dates et prévisions
                dates = []    
                # Boucle pour extraire les dates et prévisions de chaque jour
                for forecast in data['forecast']['forecastday']:
                    date = forecast['date']
                    prevision = forecast['day']['daily_will_it_rain']
                    if prevision == 0:
                        meteo = "il pleut pas il faut arroser les plantes"
                    else:
                        meteo = "il pleut"
                    
                    dates.append({"date": date, "meteo du jour": meteo})
                
                # Enregistrer les données au format JSON
                Historique.enregistrerJson(dates)
                return dates
            else:
                print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Une erreur s'est produite lors de la requête à l'API :", e)
        except ValueError as e:
            print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
        
        return None

# Pour tester la fonction en dehors de FastAPI
apiKey = os.getenv("My_API")
pays = "Paris"
dt = "2024-06-15"
endt = "2024-06-17"
reponse = Historique.ArrosePlante(apiKey, pays, dt, endt)
print(reponse)
