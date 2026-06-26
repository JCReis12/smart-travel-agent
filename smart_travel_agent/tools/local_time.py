from datetime import datetime
import pytz

def get_local_time(city: str) -> dict:

    timezones = {
        "miami": "America/New_York",
        "new york": "America/New_York",
        "los angeles": "America/Los_Angeles",
        "chicago": "America/Chicago",
        "las vegas": "America/Los_Angeles",
        "toronto": "America/Toronto",
        "mexico city": "America/Mexico_City",
        "cancun": "America/Cancun",
        "rio de janeiro": "America/Sao_Paulo",
        "sao paulo": "America/Sao_Paulo",
        "buenos aires": "America/Argentina/Buenos_Aires",
        "cusco": "America/Lima",
        "cartagena": "America/Bogota",
        "londres": "Europe/London",
        "edimburgo": "Europe/London",
        "paris": "Europe/Paris",
        "nice": "Europe/Paris",
        "lyon": "Europe/Paris",
        "roma": "Europe/Rome",
        "milao": "Europe/Rome",
        "firenze": "Europe/Rome",
        "venezia": "Europe/Rome",
        "madrid": "Europe/Madrid",
        "barcelona": "Europe/Madrid",
        "sevilha": "Europe/Madrid",
        "lisboa": "Europe/Lisbon",
        "porto": "Europe/Lisbon",
        "berlim": "Europe/Berlin",
        "munique": "Europe/Berlin",
        "frankfurt": "Europe/Berlin",
        "amsterdam": "Europe/Amsterdam",
        "bruxelas": "Europe/Brussels",
        "viena": "Europe/Vienna",
        "praga": "Europe/Prague",
        "budapeste": "Europe/Budapest",
        "varsovia": "Europe/Warsaw",
        "zurique": "Europe/Zurich",
        "genebra": "Europe/Zurich",
        "copenhague": "Europe/Copenhagen",
        "estocolmo": "Europe/Stockholm",
        "oslo": "Europe/Oslo",
        "helsinque": "Europe/Helsinki",
        "atenas": "Europe/Athens",
        "santorini": "Europe/Athens",
        "dublin": "Europe/Dublin",
        "monaco": "Europe/Monaco",
        "rekyjavik": "Atlantic/Reykjavik",
        "istambul": "Europe/Istanbul",
        "moscou": "Europe/Moscow",
        "tokyo": "Asia/Tokyo",
        "seul": "Asia/Seoul",
        "beijing": "Asia/Shanghai",
        "hong kong": "Asia/Hong_Kong",
        "bangkok": "Asia/Bangkok",
        "singapura": "Asia/Singapore",
        "dubai": "Asia/Dubai",
        "sidney": "Australia/Sydney",
        "cairo": "Africa/Cairo",
        "marrakech": "Africa/Casablanca",
        "cape town": "Africa/Johannesburg"
    }

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