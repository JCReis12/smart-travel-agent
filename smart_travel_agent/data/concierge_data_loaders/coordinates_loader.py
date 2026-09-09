import requests

def get_coordinates(city: str) -> dict:

    coord_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}"
        f"&count=1"
        f"&language=pt"
        f"&format=json"
        f"&utm_source=chatgpt.com"
    )

    coord_response = requests.get(coord_url)

    if coord_response.status_code != 200:
        return{
            "status" : "error",
            "message" : "Erro ao buscar coordenadas."
        }

    coord_data = coord_response.json()

    if "results" not in coord_data:
        return{
            "status" : "error",
            "message" : f"A cidade de {city} não foi encontrada"
        }

    coordinates = coord_data["results"][0]

    return{
        "status" : "success",
        "latitude" : coordinates["latitude"],
        "longitude" : coordinates["longitude"]
    }