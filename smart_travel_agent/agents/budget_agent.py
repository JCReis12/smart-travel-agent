# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='budget_agent',
    description='Assistente financeiro de viagens.',
    instruction='''
    Você é um especialista em finanças de viagens.
    
    Recebendo do concierge o destino do usuário você deve informar uma estimativa de gastos
    para a viagem.
    ''',
    tools=[]
)

