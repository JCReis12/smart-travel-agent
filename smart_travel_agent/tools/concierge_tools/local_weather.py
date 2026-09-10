import requests
from data.concierge_data_loaders.coordinates_loader import get_coordinates


def get_weather(latitude: float, longitude: float) -> dict:

    # ARRUMAR # coordinates = get_coordinates(city)

    weather_url = (
        
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&hourly=temperature_2m"
        f"&current=temperature_2m,apparent_temperature,is_day,wind_speed_10m,rain,weather_code"
        
    )

    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return{
            "status" : "error",
            "message" : "Erro ao buscar clima"
        }
    
    weather_data = weather_response.json()
    
    weather = weather_data["current"]
    
    return{
        "status" : "success",
        "temperature" : weather["temperature_2m"],
        "apparent_temperature" : weather["apparent_temperature"],
        "is_day" : weather["is_day"],
        "windspeed" : weather["wind_speed_10m"],
        "rain" : weather["rain"],
        "weather_code" : weather["weather_code"]
    }
