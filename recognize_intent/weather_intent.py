from API.weather_api import get_weather
from config.config import INTENT_KEYWORDS
import re

def recognize_weather_intent(user_input):
    weather_keywords = INTENT_KEYWORDS.get("weather", [])  # Fetch weather keywords
    return any(keyword in user_input.lower() for keyword in weather_keywords)


def extract_city_from_input(user_input):
    city_pattern = re.compile(r"\b(?:in|at|on|of|for|about|near|to)\s+([\w\s]+)", re.IGNORECASE)
    match = city_pattern.search(user_input)
    if match:
        city = match.group(1).strip()
        return city.capitalize()
    return "Kathmandu"

def handle_weather_intent(user_input, memory):
    # Extract city from input
    city = extract_city_from_input(user_input) or "Kathmandu"  # Default to Kathmandu
    response = get_weather(city)

    # Log the weather response in memory
    memory.chat_memory.add_ai_message(response)

    return response