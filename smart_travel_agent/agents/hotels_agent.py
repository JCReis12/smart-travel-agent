# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='hotels_agent',
    description='Assistente que busca e recomenda hotéis para uma viagem.',
    instruction='''

    ''',
    tools=[]
)

