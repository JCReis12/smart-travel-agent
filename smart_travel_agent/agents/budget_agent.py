# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='budget_agent',
    description='Assistente financeiro de viagens.',
    instruction='''

    ''',
    tools=[]
)

