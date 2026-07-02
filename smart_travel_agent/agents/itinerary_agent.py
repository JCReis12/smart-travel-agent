# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='itinerary_agent',
    description='Assistente que monta um roteiro de viagem.',
    instruction='''

    ''',
    tools=[]
)

