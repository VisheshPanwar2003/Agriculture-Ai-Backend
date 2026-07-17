import os

from fastapi import APIRouter

from dotenv import load_dotenv

from services.weather_service import WeatherService

load_dotenv()

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

weather_service = WeatherService(
    os.getenv("WEATHER_API_KEY")
)

@router.get("/{city}")

async def get_weather(city: str):

    return weather_service.get_weather_by_city(city)