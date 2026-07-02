'''
1. Perfil "Equilibrado" (Padrão)
Ideal para viagens nacionais de avião ou internacionais curtas (América do Sul, por exemplo), onde as passagens não são um absurdo de caras e você quer um equilíbrio entre conforto e passeios.

    - Passagens (Aéreas/Terrestres): 30%
    - Hospedagem: 25%
    - Alimentação: 20%
    - Passeios e Atrações: 15%
    - Transporte Local e Compras: 5%
    - Fundo de Emergência: 5%

2. Perfil "Longa Distância" (Foco no Deslocamento)
Perfeito para viagens intercontinentais (Europa, Ásia, EUA). O custo para chegar ao destino engole uma parte enorme do orçamento, o que exige dar uma segurada nos gastos lá dentro.

    - Passagens: 45% a 50%
    - Hospedagem: 20%
    - Alimentação: 15%
    - Passeios e Atrações: 10%
    - Fundo de Emergência e Seguro Viagem: 5%

3. Perfil "Mochileiro / Econômico"
Se você já conseguiu uma passagem muito barata (ou vai de carona/ônibus) e planeja ficar em hostels ou Airbnb compartilhado, o foco muda totalmente para a experiência local.

    - Passagens: 15%
    - Hospedagem: 25%
    - Alimentação: 25%
    - Passeios e Vida Noturna: 25%
    - Transporte Local / Emergências: 10%
'''

def balanced_plan(budget):
    balanced = {
        'passagens': budget * 0.30,
        'hospedagem': budget * 0.25,
        'alimentacao': budget * 0.20,
        'passeios': budget * 0.15,
        'transporte': budget * 0.05,
        'emergencia': budget * 0.05
    }
    return balanced

def long_distance_plan(budget):
    long_distance = {
        'passagens': budget * 0.45,
        'hospedagem': budget * 0.20,
        'alimentacao': budget * 0.15,
        'passeios': budget * 0.10,
        'transporte': budget * 0.05,
        'emergencia': budget * 0.05
    }
    return long_distance

def backpacker_plan(budget):
    backpacker = {
        'passagens': budget * 0.15,
        'hospedagem': budget * 0.25,
        'alimentacao': budget * 0.25,
        'passeios': budget * 0.25,
        'transporte': budget * 0.05,
        'emergencia': budget * 0.05
    }
    return backpacker