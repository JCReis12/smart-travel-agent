# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='hotels_agent',
    description='Assistente que busca e recomenda hotéis para uma viagem.',
    instruction='''
    Você é um especialista em buscar e recomendar hotéis para uma viagem.

    Recebendo do concierge o destino do usuário você deve informar uma média de preços 
    de hotéis para o destino, e citar o nome de 1 apenas muito famoso.
    ''',
    tools=[]
)

