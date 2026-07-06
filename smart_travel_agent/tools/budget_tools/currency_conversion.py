'''

    TOOL responsável por converter moedas.
    Recebe como parametro:
        - currency_from: moeda de origem
        - currency_to: moeda de destino
        - amount: valor a ser convertido


'''
import requests

def currency_conversion(currency_from: str, currency_to: str, amount: float) -> float:

    response = requests.get(f"API ADDRESS")
    data = response.json()
    converted_amount = data['rates'][currency_to] * amount
    return converted_amount
    

