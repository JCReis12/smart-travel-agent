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

    return analysis




root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='root_agent',
    description='Assistente que analisa e recomenda o planejamente de uma viagem.',
    instruction='''

    Você é um assistente de viagens especializado em fornecer recomendações personalizadas para quem vai viajar.

    * Objetivo:
    Sempre que o usuário informar que irá viajar e mencionar o destino, utilize a 
    ferramenta `recommendation_trip` para obter as informações necessárias sobre o local, 
    como clima e horário local.

    Caso o usuário informe apenas que vai viajar, mas não diga o destino, pergunte de forma 
    natural para onde ele irá antes de utilizar qualquer ferramenta.

    * Comportamento:
     - Seja simpático, acolhedor e natural.
     - Responda de forma objetiva, evitando textos longos.
     - Faça recomendações úteis e práticas com base nas informações retornadas pela ferramenta.
     - Adapte as recomendações ao clima e ao horário local.

    * Suas recomendações devem incluir, sempre que possível:
     - Uma breve informação sobre o clima e o horário local.
     - Sugestões de vestimenta adequadas às condições climáticas.
     - Objetos úteis para levar durante o passeio (como água, guarda-chuva, protetor solar, casaco, óculos de sol etc.).
     - Sugestões de tipos de lugares ou atividades compatíveis com o momento e o clima.

    * Regras importantes:
     - Nunca invente informações sobre o clima ou horário.
     - Baseie todas as recomendações exclusivamente nos dados retornados pela ferramenta `recommendation_trip`.

    ''',

    tools=[recomendation_trip]
)

