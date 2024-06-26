from fastapi import FastAPI
from app.api.v1.foreCast import router as forecast_router
from app.api.mainN import app as api_router_v2

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather Forecast API"}


app.include_router(forecast_router, prefix="/api/v1")
app.mount("/api/v2", api_router_v2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
