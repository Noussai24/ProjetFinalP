from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.v1.foreCast import get_weather_forecast
import os
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("forecast.html", {"request": request})


@app.post("/forecast", response_class=HTMLResponse)
async def get_forecast(request: Request, city: str = Form(...)):
    forecast_data = get_weather_forecast(city, os.getenv('api_key'), 3)
    return templates.TemplateResponse(
        "forecast.html", {
            "request": request, "forecast_data": forecast_data})
