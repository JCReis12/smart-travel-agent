from datetime import datetime
import pytz
from smart_travel_agent.data.concierge_data_loaders.timezones_loader import timezones

def get_local_time(city: str) -> dict:

    city_lower = city.lower()

    if city_lower not in timezones:
        return{
            "status" : "error",
            "message" : f"A cidade de {city} não foi encontrada"
        }
    
    timezone = pytz.timezone(timezones[city_lower])

    current_time = datetime.now(timezone).strftime("%H:%M")

    return{
        "status" : "success",
        "current_time" : current_time
    }