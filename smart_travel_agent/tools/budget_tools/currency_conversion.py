'''

    TOOL responsável por converter moedas.
    Recebe como parametro:
        - currency_from: moeda de origem
        - currency_to: moeda de destino
        - amount: valor a ser convertido


'''
#https://www.exchangerate-api.com

import requests

def currency_conversion(currency_destination, currency_local, amount ) -> dict:

    currency_url = f"https://v6.exchangerate-api.com/v6/609d5a8da24c1edae813d6a4/latest/{currency_local}"
    
    response = requests.get(currency_url)

    if response.status_code != 200:
        return{
            "status" : "error",
            "message" : "Erro ao buscar cotação da moeda"
        }
        
    data = response.json()

    if "conversion_rates" not in data:
        return{
            "status" : "error",
            "message" : "Cotação não encontrada"
        }
    
    #taxa de conversão (currency_destination/currency_local)
    rate = data["conversion_rates"][currency_destination]
    
    #valor convertido
    amount_converted = amount * rate

    return{
        "status" : "success",
        "amount_local" : amount,
        "amount_converted" : amount_converted,
        "currency_local" : currency_local,
        "currency_destination" : currency_destination
    }



     
    
    
