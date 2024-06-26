from fastapi import FastAPI, HTTPException
from app.api.v1.historique import Historique



app = FastAPI()

@app.get("/historique/{pays}/{dt}/{endt}")
def read_root(pays:str, dt:str, endt:str):
    try:
        datameteo = Historique.ArrosePlante( pays, dt, endt)
        if datameteo is not None:
            # Retourner directement les données sans conversion en chaîne JSON
            return datameteo
        else:
            raise HTTPException(status_code=500, detail="Erreur lors de la récupération des données météorologiques")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
