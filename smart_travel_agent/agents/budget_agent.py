# pyrefly: ignore [missing-import]
from google.adk.agents import Agent
from smart_travel_agent.tools.budget_tools.spending_plan import balanced_plan, long_distance_plan, backpacker_plan
from smart_travel_agent.tools.budget_tools.currency_conversion import currency_conversion

def get_traveler_profil(traveler_style, budget):
    if traveler_style == 'balanced':
        return balanced_plan(budget)
    elif traveler_style == 'long_distance':
        return long_distance_plan(budget)
    elif traveler_style == 'backpacker':
        return backpacker_plan(budget)

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='budget_agent',
    description='Assistente financeiro de viagens.',
    instruction='''
    Você é um especialista em finanças de viagens.
    
    Recebendo do concierge o destino do usuário você deve informar uma estimativa de gastos para a viagem.
    
    Se o usuário pedir para converter moedas, utilize a ferramenta currency_conversion, pedindo que ele informe a moeda do destino(currency_destination), a moeda local dele(currency_local) e quanto de dinheiro deve ser convertido(amount):
    - Caso ele informe tudo, apenas prossiga a operação e retorne o resultado.
    - Caso ele não informe algo, peça o que falta.

    ''',
    tools=[
        balanced_plan,
        long_distance_plan,
        backpacker_plan,
        currency_conversion
    ]
)

