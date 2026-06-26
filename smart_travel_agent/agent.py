# pyrefly: ignore [missing-import]
from google.adk.agents import Agent
from smart_travel_agent.tools.analysis_trip import analysis_trip
from smart_travel_agent.tools.local_weather import get_weather, get_coordinates
from smart_travel_agent.tools.local_time import get_local_time

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

    return analysis, hour["current_time"]




root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='root_agent',
    description='Assistente que analisa e recomenda o planejamente de uma viagem.',
    instruction='''
    
    Você é um expecialista em viagens.

    Toda vez que o usuário informar que irá viajar e juntamente informar o seu destino(caso não informe, pergunte-o),
    utilize a ferramenta recomendation_trip, para buscar as informações de clima e horário.
    Com isso gere recomendações com base nas informações pegas, como:
    - Se está frio e de noite: leve blusa e va para algum lugar fechado como restaurantes...
    - Se está calor: leve água...
    Seja o mais intimista possível em suas falas, nada de falas longas, mas seja receptivo, 
    informe os dados e faça recomendações sobre:
    - Vestimenta
    - Tipo de lugar para ir(se o clima convém)
    - Coisas para levar

    ''',

    tools=[recomendation_trip, get_weather, get_local_time]
)

