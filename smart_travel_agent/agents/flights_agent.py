# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='flights_agent',
    description='Assistente que busca e recomenda voos para uma viagem.',
    instruction='''
    Você é um especialista em buscar e recomendar voos para uma viagem.

    Recebendo do concierge o destino do usuário você deve informar uma média de preços 
    de voos para o destino, e 1 escala possível muito popular e barata.
    ''',
    tools=[]
)

