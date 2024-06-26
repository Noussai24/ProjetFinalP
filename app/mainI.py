from fastapi import FastAPI, HTTPException
from app.api.v1.historique import Historique
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")
pays = "Paris"
dt = "2024-06-06"
endt = "2024-06-08"
app = FastAPI()

@app.get("/historique/{pays}/{dt}/{endt}")
def read_root(pays:str, dt:str, endt:str):
    try:
        datameteo = Historique.ArrosePlante(apiKey, pays, dt, endt)
        if datameteo is not None:
            # Retourner directement les données sans conversion en chaîne JSON
            return datameteo
        else:
            raise HTTPException(status_code=500, detail="Erreur lors de la récupération des données météorologiques")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
