from smart_travel_agent.tools.concierge_tools.analysis_trip import analysis_trip
from smart_travel_agent.tools.concierge_tools.local_weather import get_weather, get_coordinates
from smart_travel_agent.tools.concierge_tools.local_time import get_local_time

def recomendation_trip(city: str) -> dict:

    #Coordenadas
    coord = get_coordinates(city)

    if coord["status"] == "error":
        return coord

    latitude = coord["latitude"]
    longitude = coord["longitude"]


    #Clima
    weather = get_weather(latitude, longitude)

    if weather["status"] == "error":
        return weather
    
    
    #Hora local
    hour = get_local_time(city)

    if hour["status"] == "error":
        return hour
    

    #Análise final
    analysis = analysis_trip(weather, hour)

    return analysis