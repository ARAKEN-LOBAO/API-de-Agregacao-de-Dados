import requests

def buscar_cidade(nome):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={nome}&count=1&language=pt&format=json"

    try:
        res = requests.get(url)
        data = res.json()
    except Exception as e:
        print("ERRO CIDADE:", e)
        return None

    if "results" not in data:
        return None

    cidade = data["results"][0]

    return {
        "nome": cidade["name"],
        "uf": cidade.get("admin1", ""),
        "latitude": cidade["latitude"],
        "longitude": cidade["longitude"]
    }