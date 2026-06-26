from .local_weather import get_weather
from .local_time import get_local_time


def analysis_trip(weather, hour) -> dict:

    #Puxando dados de clima
    temp = weather["temperature"]
    app_temp = weather["apparent_temperature"]
    windspeed = weather["windspeed"]
    rain = weather["rain"]
    weather_code = weather["weather_code"]

    #Puxando dados de horário
    local_hour = hour["current_time"]

    #Criando uma variável para guardar o horario em formato INT
    #para usar na comparação abaixo
    hour_int_to_comper = int(local_hour.split(":")[0])





    #Temperatura
    if temp >= 30:
        temp_status = "Muito quente"
    elif temp >= 24:
        temp_status = "Agradável"
    elif temp <= 23:
        temp_status = "Frio"

    #Sensação térmica
    if app_temp >= 29:
        app_temp_status = "Clima abafado"
    elif temp >= 23:
        app_temp_status = "Clima ameno e ambiente"
    elif temp <= 22:
        app_temp_status = "Clima gelido"

    #Chuva
    if rain > 0:
        rain_status = "Chovendo"
    else:
        rain_status = "Sem chuva"

    #Estado climático geral
    if weather_code == 0:
        weather_status = "Céu limpo"
    elif weather_code == 2:
        weather_status = "Parcialmente nublado"
    elif weather_code == 3:
        weather_status = "Nublado"
    elif weather_code == 61:
        weather_status = "Chuva leve"
    elif weather_code == 63:
        weather_status = "Chuva moderada"
    elif weather_code == 65:
        weather_status = "Chuva forte"
    else:
        weather_status = "Clima variável"
    
    #Horário
    if 6 <= hour_int_to_comper < 12:
        period_day = "Manhã"
    elif 12 <= hour_int_to_comper < 18:
        period_day = "Tarde"
    else:
        period_day = "Noite"

    #Turismo e passeio
    if temp < 32 and rain == 0:
        tourism_status = "Bom para passeios"
    else:
        tourism_status = "Clima desfavorável"


    return{
        "temperature" : temp,
        "temp_status" : temp_status,
        "apparent_temperature" : app_temp,
        "app_temp_status" : app_temp_status,
        "rain" : rain,
        "rain_status" : rain_status,
        "weather_status" : weather_status,
        "period_day" : period_day,
        "tourism_status" : tourism_status,
        "windspeed" : windspeed
    }