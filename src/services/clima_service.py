import requests

def buscar_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        res = requests.get(url)
        data = res.json()
    except Exception as e:
        print("ERRO CLIMA:", e)
        raise

    return {
        "temperatura": data["current_weather"]["temperature"],
        "vento": data["current_weather"]["windspeed"],
        "unidades": {
            "temperatura": "°C"
        }
    }