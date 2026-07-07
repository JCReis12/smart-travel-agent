import requests

url = "https://www.roadgoat.com/business/cities-api"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)
