import requests
from config.config import OPENWEATHER_API_KEY

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather_desc = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]
        country = data["sys"]["country"]

        return (
            f"The current weather in {city_name}, {country} is {weather_desc} "
            f"with a temperature of {temperature}°C and humidity of {humidity}%."
        )
    except requests.exceptions.RequestException as e:
        return f"Unable to fetch weather data. Error: {e}"
    except KeyError:
        return "Could not retrieve weather details. Please check the city name."
