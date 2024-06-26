
from fastapi import FastAPI, HTTPException
from app.api.v1.alert import recommandation_vetements 

app = FastAPI()
# Création de l'application FastAPI

@app.get("/")
# Route de base

def read_root():
    
    # Route de base qui retourne un message de bienvenue.
    return {"message": "Bienvenue sur l'App méteoPro !"}

@app.get("/recommandation/{city}")
# Route pour obtenir la recommandation de vêtements basée sur la météo
def get_recommandation(city: str):
    try:
        print("Hello, world! : " +city )
        recommendation = recommandation_vetements(city)
        # Appeler la fonction pour obtenir la recommandation de vêtements
        if recommendation.startswith("Erreur"):
        # Vérifier si la recommandation contient une erreur
            raise HTTPException(status_code=400, detail=recommendation)
        return {"city": city, "recommendation": recommendation}
        # Retourner la recommandation dans un format JSON
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # Lever une exception HTTP avec le code 500 en cas d'erreur 


