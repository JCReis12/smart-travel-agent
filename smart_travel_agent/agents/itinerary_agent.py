# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='itinerary_agent',
    description='Assistente que monta um roteiro de viagem.',
    instruction='''
    Você é um especialista em montar roteiros de viagem.
    
    Recebendo do concierge o destino do usuário você deve informar uma lista pequena de sugestões 
    de lugares para visitar no local, 1 sugestão por dia.
    ''',
    tools=[]
)

