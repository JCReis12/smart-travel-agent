# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='flights_agent',
    description='Assistente que busca e recomenda voos para uma viagem.',
    instruction='''

    ''',
    tools=[]
)

