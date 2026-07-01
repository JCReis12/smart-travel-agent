import requests

def get_coordinates(city: str) -> dict:

    coord_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}"
        f"&count=1"
        f"&language=pt"
        f"&format=json"
        f"&utm_source=chatgpt.com"
    )

    coord_response = requests.get(coord_url)

    if coord_response.status_code != 200:
        return{
            "status" : "error",
            "message" : "Erro ao buscar coordenadas."
        }

    coord_data = coord_response.json()

    if "results" not in coord_data:
        return{
            "status" : "error",
            "message" : f"A cidade de {city} não foi encontrada"
        }

    coordinates = coord_data["results"][0]

    return{
        "status" : "success",
        "latitude" : coordinates["latitude"],
        "longitude" : coordinates["longitude"]
    }

def get_weather(latitude: float, longitude: float) -> dict:
    '''
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )
    '''

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
