from app.api.v1.Fonction_Astro import get_sunrise_sunset

from fastapi import FastAPI, HTTPException

app = FastAPI()

api_key = "4c57c92aa17e4b82857172100241506"

@app.get("/heures/{city}")
def read_root(city: str):
    try:
        sunrise, sunset = get_sunrise_sunset(city, api_key)
        if sunrise and sunset:
            return {f"L'heure de lever et coucher de soleil à":city, "est": sunrise, "et":sunset}
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
