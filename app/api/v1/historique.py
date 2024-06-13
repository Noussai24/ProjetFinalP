import requests
from dotenv import load_dotenv
import os
import json

class Historique:
    load_dotenv()
    
    @staticmethod
    def ArrosePlante(apikey, pays, dt, endt):
        url = f"https://api.weatherapi.com/v1/history.json?key={apikey}&q={pays}&dt={dt}&end_dt={endt}"
        response = requests.get(url)
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
                        meteo = "il pleut pas il faut arroser les plante"
                    else:
                        meteo = "il pleut"
                    dates.append({"date": date, "meteo du jour": meteo})
                
                
                base_dir = os.path.dirname(os.path.abspath(__file__))
                data_file_path = os.path.join(base_dir, "../../data/dataHistorique.json")
                os.makedirs(os.path.dirname(data_file_path), exist_ok=True)
                
                with open(data_file_path, "w") as jsonFile:
                    # Convertir la liste en chaîne JSON
                    jsonString = json.dumps(dates, indent=4)
                    jsonFile.write(jsonString)  # Write JSON to file
            else:
                print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Une erreur s'est produite lors de la requête à l'API :", e)
        except ValueError as e:
            print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
        
        return jsonString

apiKey = os.getenv("My_API")
pays = "Paris"
dt = "2024-06-06"
endt = "2024-06-10"
reponse = Historique.ArrosePlante(apiKey, pays, dt, endt)
print(reponse)
